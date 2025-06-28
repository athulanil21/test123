from django.contrib import admin
from web.models import RegistrationClass, AboutClass


# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'dob', 'education', 'message')


admin.site.register(RegistrationClass, RegistrationAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')


admin.site.register(AboutClass, AboutAdmin)