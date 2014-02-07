from django.contrib.auth.backends import ModelBackend
from django.contrib.sites.models import Site
from socialregistration.contrib.twitter.models import TwitterProfile


class TwitterAuth(ModelBackend):
    
    def authenticate(self, twitter_id=None):
        try:
            return TwitterProfile.objects.filter(
                twitter_id=twitter_id,
                site=Site.objects.get_current()
            )[:1][0].user
        except IndexError:
            return None
