from django.contrib import admin
from .models import CreateVote, Option, Select

# Register your models here.
admin.site.register(CreateVote)
admin.site.register(Option)
admin.site.register(Select)