from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.templatetags.static import static

class HomeView(generic.base.TemplateView):
    template_name = 'umi/home.html'

class TestView(generic.base.TemplateView):
    template_name = 'umi/test.html'

class UmiRandomView(generic.base.TemplateView):
    template_name = 'umi/umiRandom.html'