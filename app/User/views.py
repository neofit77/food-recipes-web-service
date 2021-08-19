from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView, LoginView
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import LoginSerializer
from rest_framework import generics, status, views, permissions
from rest_framework.authentication import BasicAuthentication


class LogForm(APIView):
    """Load login form"""
    authentication_classes = [BasicAuthentication]

    def get(self, request):
        return render(request, 'User/login.html')


class LogUser(APIView):
    """Function that create access and refresh tokens"""
    authentication_classes = [BasicAuthentication]
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = LoginSerializer
    template_name='User/loged.html'

    def post(self, request):
        """Function that create access and refresh tokens and store it in httpOnly cookies"""
        user = authenticate(username=request.data['username'],password=request.data['password'])
        tokens = user.tokens()
        data = {}
        data['refresh'] = tokens['refresh']
        data['access'] = tokens['access']
        data['username'] = request.data['username']
        data['password'] = request.data['password']
        data['csrfmiddlewaretoken'] = request.data['csrfmiddlewaretoken']

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        response = Response()
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value='{}StringKojiRazdvajaDveVrsteTokenaSplitomVracamVrednosti{}'.format(data["access"], data["refresh"]),
            expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )
        csrf.get_token(request)
        response.data = {"Success": "Login successfully", "data": data}
        return response


class LogoutAPIView(generics.GenericAPIView):
    """Logout user entering fake JWT in cookie"""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'User/logout.html'

    def get(self, request):
        """Set cookie with fake JWT"""
        response = Response()
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value='{}StringKojiRazdvajaDveVrsteTokenaSplitomVracamVrednosti{}'.format('ddd', 'fff'),
            expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
        return response