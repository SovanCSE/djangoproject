from django.contrib import admin

# Register your models here.
from .models import Company, Language, Programmer

admin.site.register(Company)
admin.site.register(Language)
admin.site.register(Programmer)
