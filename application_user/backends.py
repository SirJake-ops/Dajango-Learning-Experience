# application_user/backends.py
import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

logger = logging.getLogger(__name__)


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(email=username)
        except user_model.DoesNotExist:
            return None

        if user:
            if user.check_password(password):
                if self.user_can_authenticate(user):
                    return user
                else:
                    logger.warning(f"User not authenticated: {user}")
            else:
                logger.warning(f"Password check failed: {user, password}")
        return None
