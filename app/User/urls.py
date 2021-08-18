from django.urls import path
from . import views

urlpatterns = [
   path('logout/', views.LogoutAPIView.as_view(), name='logout'),
   path('', views.LogUser.as_view(), name='login'),
   path('auth/', views.AuthUser.as_view(), name='auth')

]