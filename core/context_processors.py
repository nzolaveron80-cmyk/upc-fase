from django.conf import settings

from .models import SiteConfig


def site(request):
    return {"site": SiteConfig.load(), "MEDIA_URL": settings.MEDIA_URL}
