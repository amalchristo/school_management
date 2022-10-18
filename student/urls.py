from django.urls import path
from. import views

urlpatterns = [
    path('homest',views.homest),
    path('login',views.loginfee)
]