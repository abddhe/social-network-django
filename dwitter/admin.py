from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from .models import Profile, Dweet
from django.dispatch import receiver
# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


class DweetAdmin(admin.ModelAdmin):
    model = Dweet
    list_displayed = ['body', 'user']


admin.site.register(Dweet, DweetAdmin)
