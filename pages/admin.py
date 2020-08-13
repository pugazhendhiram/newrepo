from django.contrib import admin
from pages.models import demomodel
# Register your models here.
class adminFeature(admin.ModelAdmin):
    list_display=['id','name','age','Department']
    list_display_links=['name',]
    search_fields = ['id','name','age']
    list_filter = ['age',]

admin.site.register(demomodel, adminFeature)
