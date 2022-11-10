from django.urls import path

from bureau.views import (
    index,
    NewspaperListView,
    TopicListView,
    RedactorListView,
    NewspaperDetailView,
    RedactorDetailView,
    TopicDetailView,
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "newspapers/",
        NewspaperListView.as_view(),
        name="newspaper-list"
    ),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list"
    ),
    path(
        "redactors/",
        RedactorListView.as_view(),
        name="redactor-list"
    ),
    path(
        "redactors/<int:pk>/",
        RedactorDetailView.as_view(),
        name="redactor-detail"
    ),
    path(
        "newspapers/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail"
    ),
    path(
        "topics/<int:pk>/",
        TopicDetailView.as_view(),
        name="topic-detail"
    ),
]

app_name = "bureau"
