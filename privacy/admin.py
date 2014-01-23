from django.contrib import admin
from privacy.models import Policy, PostedData

admin.site.register(Policy)
admin.site.register(PostedData)