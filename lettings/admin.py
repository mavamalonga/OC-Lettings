from django.contrib import admin
from .models import Letting, Address


class LettingAdmin(admin.ModelAdmin):
	pass
admin.site.register(Letting, LettingAdmin)

class AddressAdmin(admin.ModelAdmin):
	pass
admin.site.register(Address, AddressAdmin)

