from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return HttpResponse("<h1>Main page</h1>")


def about(request):
    logger.info('Visited the "About Me" page')
    return HttpResponse("<h1>About me</h1>")

