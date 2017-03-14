from django.contrib import admin
from piaoapp.models import Student,Number
# Register your models here.
class Studentshow(admin.ModelAdmin):
    list_display = ('name','IdNumber','PhoneNumber')
    search_fields = ('PhoneNumber',)
class Numbershow(admin.ModelAdmin):
    list_display = ('title','number')
admin.site.register(Student,Studentshow)
admin.site.register(Number,Numbershow)