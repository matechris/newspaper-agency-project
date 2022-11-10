from django.urls import path

from bureau.views import (
    index,
    NewspaperListView,
    TopicListView,
    RedactorListView,
    NewspaperDetailView,
    RedactorDetailView,
    TopicDetailView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
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
    path(
        "newspapers/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create"
    ),
    path(
        "newspapers/<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update"
    ),
    path(
        "newspapers/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete"
    ),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-create"
    ),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update"
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete"
    ),
]

app_name = "bureau"
