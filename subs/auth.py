from django.contrib.auth.backends import BaseBackend

from django.contrib.auth import get_user_model

User = get_user_model()


class WithoutPasswordBackend(BaseBackend):

    def authenticate(self, email):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None