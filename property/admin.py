from django.contrib import admin

from .models import Flat, Plaint,Owner


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    readonly_fields = ["created_at",]
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town',
                    'owners_phonenumber', 'owner_pure_phone')
    list_filter = ('new_building',)
    list_editable = ('new_building',)
    raw_id_fields = ('like_by',)


@admin.register(Plaint)
class Complaints(admin.ModelAdmin):
    raw_id_fields = ('apartment',)
    list_display = ('who_complained', 'apartment', 'text_complaint', 'created_at',)


@admin.register(Owner)
class Owner(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    list_display = ('name', 'phone', 'pure_phone',)

