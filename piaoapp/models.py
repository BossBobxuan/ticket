from django.db import models
from django import forms
# Create your models here.
class StudentForm(forms.Form):
    name = forms.CharField(label = '姓名',widget = forms.TextInput(attrs={'class':'weui_input','placeholder':'请输入姓名'}))
    IdNumber = forms.CharField(label = '证件',widget = forms.TextInput(attrs={'class':'weui_input','placeholder':'请输入证件号'}))
    PhoneNumber = forms.CharField(label = '电话',widget = forms.TextInput(attrs={'class':'weui_input','placeholder':'请输入电话号码'}))
class Student(models.Model):
    name = models.CharField(max_length = 20)
    IdNumber = models.CharField(max_length = 20)
    PhoneNumber = models.CharField(max_length = 20)     
class Number(models.Model):
    title = models.CharField(max_length = 30)
    number = models.IntegerField()