from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "homepage.html"

# class HomePageView(View):
#
#     def get(self, request):
#         return render(request, 'homepage.html')
#
#     def post(self, request):
#         pass