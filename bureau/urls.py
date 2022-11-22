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
    RedactorCreateView,
    RedactorUpdateView,
    RedactorDeleteView,
    assign_redactor_to_newspaper,
    delete_redactor_from_newspaper,
)


urlpatterns = [
    path("", index, name="index"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path(
        "newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"
    ),
    path("topics/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path(
        "newspapers/<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update",
    ),
    path(
        "newspapers/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path("topics/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update"),
    path("topics/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic-delete"),
    path(
        "redactors/create/",
        RedactorCreateView.as_view(),
        name="redactor-create",
    ),
    path(
        "redactors/<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update",
    ),
    path(
        "redactors/<int:pk>/delete/",
        RedactorDeleteView.as_view(),
        name="redactor-delete",
    ),
    path(
        "redactors/<int:pk>/assign_to_newspaper/",
        assign_redactor_to_newspaper,
        name="assign-to-newspaper",
    ),
    path(
        "redactors/<int:pk>/delete_from_newspaper/",
        delete_redactor_from_newspaper,
        name="delete-from-newspaper",
    ),
]

app_name = "bureau"
