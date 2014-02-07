from django.contrib.auth.backends import ModelBackend
from django.contrib.sites.models import Site
from socialregistration.contrib.facebook.models import FacebookProfile


class FacebookAuth(ModelBackend):
    supports_object_permissions = False
    supports_anonymous_user = False
    
    def authenticate(self, uid = None):
        try:
            return FacebookProfile.objects.filter(
                uid = uid,
                site = Site.objects.get_current())[:1][0].user
        except IndexError:
            return None
