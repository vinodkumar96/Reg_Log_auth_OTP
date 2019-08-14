from django.conf.urls import url
from . import views
app_name = "OTP_app"
urlpatterns =[
    url(r'^$',views.home),
    url(r'^reg$',views.reg),
    url(r'^log$',views.log),
    url(r'^OTP$',views.OTP),
]