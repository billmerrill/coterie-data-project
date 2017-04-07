from django.contrib import admin
from .models import Constellation, Star

# Register your models here.
admin.site.register(Constellation)

class StarAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':
                            ['constellation',
                             'hyg_id',
                             'bayer_flamsteed_designation',
                             'proper_name']}),
                ('Properties', {'fields': ('magnitude', 'right_ascention', 'declination')})]

admin.site.register(Star, StarAdmin)
