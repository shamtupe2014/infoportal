from django.contrib import admin
from.models import register

class registerAdmin(admin.ModelAdmin):
    list_display=["first_name","last_name","mobile_no","email","team"]

admin.site.register(register,registerAdmin)
