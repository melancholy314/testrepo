from django.contrib import admin
from .models import spektakl, mesta

# Register your models here.

class spektaklAdmin(admin.ModelAdmin):
    fieldsets1 = [
        ('id', {'fields': ['id']}),
        ('nazvanie', {'fields': ['nazvanie']})
    ]

class mestaAdmin(admin.ModelAdmin):
    fieldsets2 = [
        ('id', {'fields': ['id']}),
        ('spektakl', {'fields': ['spektakl']}),
        ('sektor', {'fields': ['sektor']}),
        ('mesto', {'fields': ['mesto']}),
        ('tel', {'fields': ['tel']}),
        ('sms', {'fields': ['sms']}),
        ('time', {'fields': ['time']}),

    ]

admin.site.register(spektakl, spektaklAdmin)
admin.site.register(mesta, mestaAdmin)