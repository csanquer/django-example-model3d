from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from badges.models import Badge

class Model3d(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200, blank=True, default='')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Event Listeners
@receiver(post_save, sender=Model3d)
def add_badge(sender, instance, created, **kwargs):
    if instance.views >= 1000:
        starBadge = Badge.objects.get(name='star')
        starBadge.users.add(instance.owner)
        starBadge.save()

    ownerModelNb = sender.objects.filter(owner=instance.owner).count()
    if ownerModelNb >= 3 :
        collectorBadge = Badge.objects.get(name='collector')
        collectorBadge.users.add(instance.owner)
        collectorBadge.save()
