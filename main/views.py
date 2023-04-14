from django.contrib import messages
from django_countries.data import COUNTRIES
from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from .forms import ContactForm
from .utils import send_contact_email


class HomePageView(TemplateView):
    template_name = "main/index.html"


class ServicePage1View(TemplateView):
    template_name = "main/services1.html"


class ServicePage2View(TemplateView):
    template_name = "main/services2.html"


class ServicePage3View(TemplateView):
    template_name = "main/services3.html"


class ServicePage4View(TemplateView):
    template_name = "main/services4.html"


class ServicePage5View(TemplateView):
    template_name = "main/services5.html"


class ServicePage6View(TemplateView):
    template_name = "main/services6.html"


class CustomersView(TemplateView):
    template_name = "main/customers.html"


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {"form": form}
        return render(request, "main/contact.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            message = request.POST.get("message")
            choices = request.POST.get("choices")
            organization = request.POST.get("organization")
            department = request.POST.get("department")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            phone_no = request.POST.get("phone_no")
            extension = request.POST.get("extension")
            country = COUNTRIES[request.POST.get("country")]
            context = {
                "message": message,
                "choices": choices,
                "organization": organization,
                "department": department,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "phone_no": phone_no,
                "extension": extension,
                "country": country,
            }
            messages.success(request, "Your message was sent successfully!")
            send_contact_email("main/emails/send_contact_email.html", context)
        else:
            messages.error(
                request, "There was a problem sending your email. Please try again!"
            )
        return redirect("main:contact")
