from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ContactInfo, ContentBlock, Driver
from .serializers import (
    ContactInfoSerializer,
    ContentBlockAdminSerializer,
    ContentBlockPublicSerializer,
    DriverSerializer,
)


class PublicContentBlocksView(APIView):
    """Returns every content block as a flat {key: {en, ta}} map for the live site."""

    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        blocks = ContentBlock.objects.all()
        data = {block.key: {"en": block.value_en, "ta": block.value_ta} for block in blocks}
        return Response(data)


class PublicContactInfoView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        info = ContactInfo.load()
        return Response(ContactInfoSerializer(info).data)


class ContentBlockAdminViewSet(viewsets.ModelViewSet):
    """Admin CRUD for content blocks. Blocks are seeded ahead of time — admins edit
    values only; the key/section/order are read-only to keep the frontend wiring intact."""

    queryset = ContentBlock.objects.all()
    serializer_class = ContentBlockAdminSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]
    http_method_names = ["get", "patch", "head", "options"]

    def get_queryset(self):
        queryset = super().get_queryset()
        section = self.request.query_params.get("section")
        if section:
            queryset = queryset.filter(section=section)
        return queryset


class ContactInfoAdminView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        info = ContactInfo.load()
        return Response(ContactInfoSerializer(info).data)

    def patch(self, request):
        info = ContactInfo.load()
        serializer = ContactInfoSerializer(info, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DriverAdminViewSet(viewsets.ModelViewSet):
    """Admin CRUD for the dynamic driver list shown in the site footer."""

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(contact_info=ContactInfo.load())
