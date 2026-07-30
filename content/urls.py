from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ContactInfoAdminView,
    ContentBlockAdminViewSet,
    PublicContactInfoView,
    PublicContentBlocksView,
)

router = DefaultRouter()
router.register("admin/blocks", ContentBlockAdminViewSet, basename="content-admin-blocks")

urlpatterns = [
    path("blocks/", PublicContentBlocksView.as_view(), name="content-blocks"),
    path("contact-info/", PublicContactInfoView.as_view(), name="content-contact-info"),
    path("admin/contact-info/", ContactInfoAdminView.as_view(), name="content-admin-contact-info"),
    path("", include(router.urls)),
]
