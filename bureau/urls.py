from django.urls import path

from bureau.views import (
    index,
    NewspaperListView,
    TopicListView,
    RedactorListView,
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
]

app_name = "bureau"
