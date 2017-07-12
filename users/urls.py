from django.conf.urls import url
from django.contrib.auth.views import login
from users import views

urlpatterns = [
    url(r'^logout/', views.logout_view, name='logout'),
]
