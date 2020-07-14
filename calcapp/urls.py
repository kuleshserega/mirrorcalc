from django.conf.urls import url

from .views import MirrorCalcView

app_name = 'calcapp'


urlpatterns = [
    url(r'^calc/$', MirrorCalcView.as_view(), name='calc'),
]
