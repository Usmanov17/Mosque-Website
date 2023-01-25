from django.contrib import admin
from .models import Product, Status, Namaz, Mosque, Notification

# Register your models here.
admin.site.register(Product)
admin.site.register(Status)
admin.site.register(Namaz)
admin.site.register(Mosque)
admin.site.register(Notification)