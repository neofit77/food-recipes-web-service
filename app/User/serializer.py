from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError




class LogoutSerializer(serializers.Serializer):
    jwt_token = serializers.CharField()
    csrftoken = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['jwt_token'].split('proba-proba')[1]
        return attrs

    def create(self, validated_data):
        pass

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')


    # def save(self):
    #     RefreshToken(self.jwt_token.split('proba-proba')[1]).blacklist()