from django.contrib import admin
from .models import Shoplist, Items

class ShoplistAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'id',)

admin.site.register(Shoplist, ShoplistAdmin)
admin.site.register(Items)
