from django.contrib import admin
from .models import Profile


admin.site.register(Profile)

# resolve interface bug sticky-nav-bar
admin.autodiscover()
admin.site.enable_nav_sidebar = False
