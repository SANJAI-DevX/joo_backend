from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AdminLoginView, FeedbackAdminViewSet, FeedbackCreateView, FeedbackListView

router = DefaultRouter()
router.register("admin/items", FeedbackAdminViewSet, basename="feedback-admin")

urlpatterns = [
    path("", FeedbackListView.as_view(), name="feedback-list"),
    path("submit/", FeedbackCreateView.as_view(), name="feedback-create"),
    path("admin/login/", AdminLoginView.as_view(), name="feedback-admin-login"),
    path("", include(router.urls)),
]
