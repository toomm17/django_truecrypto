from django.urls import path

from . import views


urlpatterns = [
   path('login/', views.LoginPageView.as_view(), name='login'),
   path('logout/', views.LogoutView.as_view(), name='logout'),
   path('api/', views.ApiUserView.as_view(), name='reg')
]

