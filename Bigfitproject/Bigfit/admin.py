from django.contrib import admin
from .models import *


class WeightTrackerInline(admin.TabularInline):
    model = WeightTracker
    ordering = ('record_date',)


class CalorieTrackerInline(admin.TabularInline):
    model = CalorieTracker
    ordering = ('record_date',)


class UserAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'username', 'password','target_weight', 'feet'
                    , 'inches', 'date_of_birth', 'gender', 'zip_code']
    inlines = [WeightTrackerInline, CalorieTrackerInline]


admin.site.register(User, UserAdmin)


class WeightTrackerAdmin(admin.ModelAdmin):
    list_display = ['user', 'record_date', 'weight']


admin.site.register(WeightTracker, WeightTrackerAdmin)


class CalorieTrackerAdmin(admin.ModelAdmin):
    list_display = ['user', 'record_date', 'calories']


admin.site.register(CalorieTracker, CalorieTrackerAdmin)
