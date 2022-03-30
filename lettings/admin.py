from django.contrib import admin
from .models import Letting, Address


admin.site.register(Letting)
admin.site.register(Address)

# resolve interface bug sticky-nav-bar
admin.autodiscover()
admin.site.enable_nav_sidebar = False
