# howdy/urls.py
from django.conf.urls import url
from SR import views

urlpatterns = [
    url(r"^$", views.HomePageView.as_view()),
    url(r"^question/$", views.usesounddevice),
]