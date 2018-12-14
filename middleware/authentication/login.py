# Authentication Backend
# Must implements two required methods: get_user(user_id) and authenticate(request, **credentials)
# True:  return User instance of auth.models
# False: return None

from django.contrib.auth import get_user_model

User = get_user_model()


class CustomBackend:

    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            # TODO: log
            pass
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None