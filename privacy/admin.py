from django.contrib import admin
from privacy.models import Policy, PostedData, Authority

admin.site.register(Policy)
admin.site.register(PostedData)
admin.site.register(Authority)