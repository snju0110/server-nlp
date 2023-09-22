from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse


def startup(requeest):

    return JsonResponse({"Test":"Successful"}, safe=False)