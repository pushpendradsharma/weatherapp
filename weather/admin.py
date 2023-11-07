from weather.models import SearchData
from django.contrib import admin

# Register your models here.
@admin.register(SearchData)
class SearchDataAdmin(admin.ModelAdmin):
    list_display=['id','user','location','timestamp']