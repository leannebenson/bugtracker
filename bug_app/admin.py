from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bug_app.models import MyUser


admin.site.register(MyUser, UserAdmin)
