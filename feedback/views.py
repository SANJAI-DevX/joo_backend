from django.contrib.auth import authenticate
from rest_framework import status, viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Feedback
from .serializers import FeedbackAdminSerializer, FeedbackCreateSerializer, FeedbackListSerializer


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
            {"detail": "Thank you! Your feedback has been submitted and will appear after review."},
            status=status.HTTP_201_CREATED,
        )


class AdminLoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    parser_classes = [JSONParser, FormParser]

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
