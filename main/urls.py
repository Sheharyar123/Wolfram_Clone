from django.urls import path
from .views import (
    HomePageView,
    ServicePage1View,
    ServicePage2View,
    ServicePage3View,
    ServicePage4View,
    ServicePage5View,
    ServicePage6View,
    CustomersView,
    ContactView,
)

app_name = "main"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path(
        "services/implementation_consulting/",
        ServicePage1View.as_view(),
        name="service1",
    ),
    path(
        "services/sap_services_consulting/",
        ServicePage2View.as_view(),
        name="service2",
    ),
    path(
        "services/process_consulting/",
        ServicePage3View.as_view(),
        name="service3",
    ),
    path(
        "services/project_management/",
        ServicePage4View.as_view(),
        name="service4",
    ),
    path(
        "services/development/",
        ServicePage5View.as_view(),
        name="service5",
    ),
    path(
        "services/support/",
        ServicePage6View.as_view(),
        name="service6",
    ),
    path("customers/", CustomersView.as_view(), name="customers"),
    path("contact/", ContactView.as_view(), name="contact"),
]
