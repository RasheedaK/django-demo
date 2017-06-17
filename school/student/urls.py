from django.conf.urls import url
from .views import viewForm

urlpatterns = [
    url(r'^$', viewForm, name='student')
]