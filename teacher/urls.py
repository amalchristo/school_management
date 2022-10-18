from django.urls import path
from. import views
app_name='teacher'

urlpatterns = [
    path('', views.home,name='home'),
    path('login',views.loginfun,name='log'),
    path('signup',views.signupfun,name='sign'),
    path('welcome',views.welcome,name='welcome')
]