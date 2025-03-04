from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)


admin.site.register(Flat, FlatAdmin)
