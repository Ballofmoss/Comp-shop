import keyword
from math import log
from products.models import Products
from django.db.models import Q

# from django.contrib.postgres.search import (
#     SearchVector,
#     SearchQuery,
#     SearchRank,
#     SearchHeadline,
# )


def q_search(query):
    if not query or not query.strip():
        return Products.objects.all()

    keywords = [word for word in query.split() if len(word) > 2]

    if not keywords:
        return Products.objects.all()

    q_objects = Q()

    for token in keywords:
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    return Products.objects.filter(q_objects).distinct()
