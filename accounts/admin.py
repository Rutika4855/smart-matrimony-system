from django.contrib import admin
from .models import Profile, Preference, Interest, Message, Favorite

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'gender', 'location', 'age')
    search_fields = ('user__username', 'full_name', 'location')

@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'preferred_gender', 'min_age', 'max_age')

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'status', 'date_sent')
    list_filter = ('status',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp')

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'favorite_user', 'created_at')
