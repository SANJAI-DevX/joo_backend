from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ContactInfoAdminView,
    ContentBlockAdminViewSet,
    DriverAdminViewSet,
    PublicContactInfoView,
    PublicContentBlocksView,
)

router = DefaultRouter()
router.register("admin/blocks", ContentBlockAdminViewSet, basename="content-admin-blocks")
router.register("admin/drivers", DriverAdminViewSet, basename="content-admin-drivers")

urlpatterns = [
    path("blocks/", PublicContentBlocksView.as_view(), name="content-blocks"),
    path("contact-info/", PublicContactInfoView.as_view(), name="content-contact-info"),
    path("admin/contact-info/", ContactInfoAdminView.as_view(), name="content-admin-contact-info"),
    path("", include(router.urls)),
]
