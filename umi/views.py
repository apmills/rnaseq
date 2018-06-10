from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.templatetags.static import static

class HomeView(generic.base.TemplateView):
    template_name = 'umi/home.html'

class IntroView(generic.base.TemplateView):
    template_name = 'umi/intro.html'

class TestView(generic.base.TemplateView):
    template_name = 'umi/test.html'

class UmiRandomView(generic.base.TemplateView):
    template_name = 'umi/umiRandom.html'

class AmpBiasView(generic.base.TemplateView):
    template_name = 'umi/ampBias.html'

class GeneBiasView(generic.base.TemplateView):
    template_name = 'umi/geneBias.html'

class MammalDataView(generic.base.TemplateView):
    template_name = 'umi/mammalData.html'

class AboutView(generic.base.TemplateView):
    template_name = 'umi/about.html'

class ConcView(generic.base.TemplateView):
    template_name = 'umi/conclusion.html'

class RefView(generic.base.TemplateView):
    template_name = 'umi/references.html'
