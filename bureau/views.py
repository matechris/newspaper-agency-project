from django.http import HttpResponse
from django.shortcuts import render

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
