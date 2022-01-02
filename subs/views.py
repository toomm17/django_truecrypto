from django.contrib.auth import login, logout, get_user_model
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication

from .serializers import UserSerializer
from .form import LoginForm
from . import auth

User = get_user_model()


class ApiUserView(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        email = request.data['email']
        User.objects.create_user(email)
        return Response(status=status.HTTP_201_CREATED)


class LoginPageView(View):

    @staticmethod
    def get(request):
        form = LoginForm(request.POST or None)
        context = {'form': form, 'current_page': 'Вход'}
        return render(request, 'subs/form_page.html', context)

    @staticmethod
    def post(request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            user.backend = 'subs.auth.WithoutPasswordBackend'
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'subs/form_page.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
