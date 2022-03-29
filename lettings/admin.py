from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Letting, Address
from profiles.models import Profile


class LettingAdmin(admin.ModelAdmin):
	pass
admin.site.register(Letting, LettingAdmin)

class AddressAdmin(admin.ModelAdmin):
	pass
admin.site.register(Address, AddressAdmin)

class ProfileAdmin(admin.ModelAdmin):
	pass
admin.site.register(Profile, ProfileAdmin)
