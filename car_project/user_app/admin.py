from django.contrib import admin

from main_app.models import Manufacturer, Car, Comments, Country
from user_app.models import User

admin.site.register(User)
admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Comments)
admin.site.register(Country)
