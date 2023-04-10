from django.shortcuts import render
from django.views.generic import TemplateView, View
from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = "main/index.html"


class ContactPageView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {"form": form}
        return render(request, "main/contact.html", context)
