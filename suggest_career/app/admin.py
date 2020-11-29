from django.contrib import admin
from django.contrib.admin import register, ModelAdmin

from suggest_career.app.models import User, MBTI


@register(User)
class UserAdmin(ModelAdmin):
    pass


@register(MBTI)
class MBTIAdmin(ModelAdmin):
    pass
