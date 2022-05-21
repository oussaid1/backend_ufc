from django.urls import path
from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
     path('recs/<str:board_id>/',views.respond,name = 'repond'),
     path('signup',views.registration_view), 
     path('login',views.login_view), 
]