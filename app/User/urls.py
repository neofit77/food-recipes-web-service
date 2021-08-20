from django.urls import path
from . import views

urlpatterns = [
   path('logout/', views.LogoutAPIView.as_view(), name='logout'),
   path('auth/', views.LogUser.as_view(), name='auth'),
   path('', views.LogForm.as_view(), name='login'),
   path('registration/', views.RegisterView.as_view(), name='registration')


]