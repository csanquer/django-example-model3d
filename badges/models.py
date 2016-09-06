import datetime
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Badge(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200, blank=True, default='')
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.name

# Event Listeners
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def add_user_badge(sender, instance, created, **kwargs):

    if timezone.now() - instance.date_joined >= datetime.timedelta(days=365):
        pionneerBadge = Badge.objects.get(name='pionneer')
        pionneerBadge.users.add(instance)
        pionneerBadge.save()
