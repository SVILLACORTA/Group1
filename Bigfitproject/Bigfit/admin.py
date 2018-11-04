from django.contrib import admin
from .models import *


class WeightTrackerInline(admin.TabularInline):
    model = WeightTracker
    ordering = ('record_date',)


class UserAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'target_weight', 'feet', 'inches', 'date_of_birth', 'gender', 'zip_code'
                    , 'email', 'start_date', 'end_date', 'password']
    inlines = [WeightTrackerInline]


admin.site.register(User, UserAdmin)


class WeightTrackerAdmin(admin.ModelAdmin):
    list_display = ['user', 'record_date', 'weight']


admin.site.register(WeightTracker, WeightTrackerAdmin)
