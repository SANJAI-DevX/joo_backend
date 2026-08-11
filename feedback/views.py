from django.contrib.auth import authenticate
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.views import APIView

from .models import Feedback, FeedbackComment
from .serializers import (
    FeedbackAdminSerializer,
    FeedbackCommentCreateSerializer,
    FeedbackCommentSerializer,
    FeedbackCreateSerializer,
    FeedbackListSerializer,
)


class FeedbackListView(APIView):
    def get(self, request):
        limit = request.query_params.get("limit")
        queryset = Feedback.objects.filter(is_approved=True)
        if limit and limit.isdigit():
            queryset = queryset[: int(limit)]
        serializer = FeedbackListSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)


class FeedbackCreateView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = FeedbackCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Thank you! Your feedback has been submitted and is now live on the site."},
            status=status.HTTP_201_CREATED,
        )


class FeedbackReactView(APIView):
    """Adds, switches, or removes a person's reaction on a feedback post.

    The client tracks its own reaction locally (there's no login), so it tells
    us both the new reaction it wants (or null to just remove) and whatever it
    previously had recorded (or null if this is the first reaction), and we
    move one tally from the old bucket to the new one. This is how the button
    supports true unlike and switching between emoji, like Facebook/Instagram.
    """

    authentication_classes = []
    permission_classes = [AllowAny]

    REACTION_FIELDS = {
        "love": "likes",
        "laugh": "laugh_count",
        "wow": "wow_count",
        "clap": "clap_count",
    }

    def post(self, request, pk):
        new_reaction = request.data.get("reaction") or None
        previous_reaction = request.data.get("previous_reaction") or None

        for value in (new_reaction, previous_reaction):
            if value is not None and value not in self.REACTION_FIELDS:
                return Response(
                    {"detail": "Invalid reaction type. Use one of: love, laugh, wow, clap."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if new_reaction is None and previous_reaction is None:
            return Response(
                {"detail": "Provide a reaction to add/switch to, or a previous_reaction to remove."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        with transaction.atomic():
            feedback = get_object_or_404(
                Feedback.objects.select_for_update(), pk=pk, is_approved=True
            )

            if previous_reaction and previous_reaction != new_reaction:
                field_name = self.REACTION_FIELDS[previous_reaction]
                setattr(feedback, field_name, max(0, getattr(feedback, field_name) - 1))

            if new_reaction and new_reaction != previous_reaction:
                field_name = self.REACTION_FIELDS[new_reaction]
                setattr(feedback, field_name, getattr(feedback, field_name) + 1)

            feedback.save(update_fields=["likes", "laugh_count", "wow_count", "clap_count"])

        return Response(
            {
                "id": feedback.id,
                "reactions": {
                    "love": feedback.likes,
                    "laugh": feedback.laugh_count,
                    "wow": feedback.wow_count,
                    "clap": feedback.clap_count,
                },
            }
        )


class FeedbackCommentListCreateView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, FormParser]

    def get(self, request, pk):
        feedback = get_object_or_404(Feedback, pk=pk, is_approved=True)
        comments = feedback.comments.all()
        serializer = FeedbackCommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        feedback = get_object_or_404(Feedback, pk=pk, is_approved=True)
        serializer = FeedbackCommentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save(feedback=feedback)
        return Response(FeedbackCommentSerializer(comment).data, status=status.HTTP_201_CREATED)


class AdminLoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, FormParser]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "admin_login"

    def post(self, request):
        username = request.data.get("username", "").strip()
        password = request.data.get("password", "")

        if not username or not password:
            return Response({"detail": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is None or not user.is_staff:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "username": user.username})


class FeedbackAdminViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackAdminSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class FeedbackCommentAdminViewSet(viewsets.ModelViewSet):
    """Lets staff review and delete inappropriate comments. Read/delete only —
    comment content itself isn't edited from the admin panel."""

    queryset = FeedbackComment.objects.all().select_related("feedback")
    serializer_class = FeedbackCommentSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "delete", "head", "options"]

    def get_queryset(self):
        queryset = super().get_queryset()
        feedback_id = self.request.query_params.get("feedback")
        if feedback_id and feedback_id.isdigit():
            queryset = queryset.filter(feedback_id=feedback_id)
        return queryset
