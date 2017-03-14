from django.shortcuts import render
from django.http import HttpResponse
from piaoapp.models import StudentForm,Student,Number
import re
import json
# Create your views here.
def index(req):
    number = Number.objects.all()
    if len(number) > 0:
        title = number[0].title
        number = number[0].number
    else:
        return HttpResponse('<h1>当前无抢票活动</h1>')
    if req.method == 'POST':
        patten = re.compile(r'^\d*$')
        student = StudentForm(req.POST)
        if student.is_valid():
            if patten.match(req.POST['PhoneNumber']):
                print(req.POST['PhoneNumber'])
                if len(Student.objects.filter(PhoneNumber__exact= student.cleaned_data['PhoneNumber'])) > 0:
                    return render(req,'getticket.html',{})
                indbnumber = len(Student.objects.all())
                if indbnumber >= number:
                    return render(req,'dbfull.html',{})
                modelstudent = Student()
                modelstudent.name = student.cleaned_data['name']
                modelstudent.IdNumber = student.cleaned_data['IdNumber']
                modelstudent.PhoneNumber = student.cleaned_data['PhoneNumber']
                modelstudent.save()
                return render(req,'success.html',{})
            else:
                return HttpResponse('<h1>请输入正确的信息</h1>')
    else:
        student = StudentForm()
    return render(req,'index.html',{'form':student,'title':title})
def getnumber(req):
    number = Number.objects.all()[0].number
    stunumber = len(Student.objects.all())
    return HttpResponse('剩余票数：%d'%(number - stunumber))
def signup(req):
    if req.POST['username'] == 'abc':
        data = {'state':'repeat'}
        jsonstring = json.dumps(data)
        return HttpResponse(jsonstring)
    else:
        print(req.POST['username'])
        print(req.POST['password'])
        print(req.POST['label'])
        data = {'state':'success'}
        jsonstring = json.dumps(data)
        return HttpResponse(jsonstring)
def getdata(req):
    data = [{'ownername':'fucker','activityTitle':'letgetfucking','intereastednumber':3,'latitude':39.2,'longitude':115.25},
            {'ownername':'fucker2','activityTitle':'letgetfucking2','intereastednumber':4,'latitude':120.2,'longitude':36.2},
            ]
    print(req.GET)
    jsonstring = json.dumps(data)
    return HttpResponse(jsonstring)
    