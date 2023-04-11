from django.views.generic import TemplateView


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
