from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from rest_framework.authentication import CSRFCheck
from rest_framework import exceptions


def enforce_csrf(request):
    """CSRF validation"""
    check = CSRFCheck()
    check.process_request(request)
    reason = check.process_view(request, None, (), {})
    if reason:
        raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)

class MyAuthentication(JWTAuthentication):
    """Midleware class for Jvalidation JWT token"""

    def authenticate(self, request):
        """Function for JWT authentication if token exist function them validate,
            if token not valid function except error, if token is valid function return user object and token
            if token not exist function return None"""
        header = self.get_header(request)

        if header is None:
            token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
        else:
            token = self.get_raw_token(header)
        if token is None:
            return None
        raw_token = token.split('StringKojiRazdvajaDveVrsteTokenaSplitomVracamVrednosti')[0]
        validated_token = self.get_validated_token(raw_token)
        enforce_csrf(request)
        return self.get_user(validated_token), validated_token