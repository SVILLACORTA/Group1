from django.contrib import admin
from .models import *


class WeightTrackerInline(admin.TabularInline):
    model = WeightTracker
    ordering = ('record_date',)


class AccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'password', 'start_date', 'end_date']


admin.site.register(Account, AccountAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'target_weight', 'feet'
                    , 'inches', 'date_of_birth', 'gender', 'zip_code']
    # ordering = ('last_name','first_name','id')
    inlines = [WeightTrackerInline]


admin.site.register(User, UserAdmin)


class WeightTrackerAdmin(admin.ModelAdmin):
    list_display = ['user', 'record_date', 'weight']
    # ordering = ('user','user_id','record_date')


admin.site.register(WeightTracker, WeightTrackerAdmin)
