from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AdminLoginView,
    FeedbackAdminViewSet,
    FeedbackCommentAdminViewSet,
    FeedbackCommentListCreateView,
    FeedbackCreateView,
    FeedbackListView,
    FeedbackReactView,
)

router = DefaultRouter()
router.register("admin/items", FeedbackAdminViewSet, basename="feedback-admin")
router.register("admin/comments", FeedbackCommentAdminViewSet, basename="feedback-comment-admin")

urlpatterns = [
    path("", FeedbackListView.as_view(), name="feedback-list"),
    path("submit/", FeedbackCreateView.as_view(), name="feedback-create"),
    path("<int:pk>/react/", FeedbackReactView.as_view(), name="feedback-react"),
    path("<int:pk>/comments/", FeedbackCommentListCreateView.as_view(), name="feedback-comments"),
    path("admin/login/", AdminLoginView.as_view(), name="feedback-admin-login"),
    path("", include(router.urls)),
]
