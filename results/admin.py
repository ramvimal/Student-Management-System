from .models import Result
from django.contrib import admin


@admin.register(Result)
class Result(admin.ModelAdmin):
    list_display = ('student','sem')
    fields = ('student','sem','seo','c_sharp','php','python','java','ac_year') 
    list_filter = (['student','sem'])
    search_fields = (['student','sem'])