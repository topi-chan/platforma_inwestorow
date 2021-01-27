from django.contrib import admin

from .models import Institution, News, User

admin.site.register(Institution)
admin.site.register(News)
admin.site.register(User)
