from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from bureau.models import Newspaper, Redactor, Topic


def index(request) -> HttpResponse:
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()
    num_newspapers = Newspaper.objects.count()

    context = {
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_newspapers": num_newspapers
    }

    return render(request, "bureau/index.html", context=context)


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 10
    queryset = Newspaper.objects.order_by("-published_date")


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 10
    queryset = Topic.objects.order_by("name")


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 10


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
    queryset = Newspaper.objects.prefetch_related("topic", "publishers")


class RedactorDetailView(generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.prefetch_related(
        "newspapers"
    )

class TopicDetailView(generic.DetailView):
    model = Topic
    queryset = Topic.objects.prefetch_related("newspapers")
