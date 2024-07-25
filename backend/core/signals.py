from django.db.models.signals import pre_save
# anything we use in presave is going to go into models and is gonna fire the action before the model can save the process
from django.contrib.auth.models import User


def updateUser(sender, instance, **kwargs):
    if instance.email != '':
        instance.username = instance.email

pre_save.connect(updateUser, sender=User)
# to connect this signals.py goto apps and define ready func