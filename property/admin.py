from django.contrib import admin

from .models import Flat, Plaint


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    readonly_fields = ["created_at",]
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',)
    list_filter = ('new_building',)
    list_editable = ('new_building',)


@admin.register(Plaint)
class Complaints(admin.ModelAdmin):
    raw_id_fields = ('apartment',)
    list_display = ('who_complained', 'apartment', 'text_complaint', 'created_at',)


#
# admin.site.register(Flat, FlatAdmin)
# admin.site.register(Complaint)

