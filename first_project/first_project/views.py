from django.http import HttpResponse
from django.shortcuts import render
from student.models import module_1

def function_one(request):
    return HttpResponse("The respons page")

def HomePage(request):
    if request.method=='POST':
        a=request.POST['name']
        b=request.POST['class']
        c=request.POST['Section']
        d=request.POST['rollnumber']
        e=request.POST['Subject']
        f=request.POST['emailid']
        g=request.POST['Mobile']
        input_value=module_1(roll_number=d,student_name=a,student_class=b,student_section=c,student_email=f,phone_number=g,subject=e)
        input_value.save()
    return render(request,"index.html")

def SecondPage(request):
    DataOutput=module_1.objects.all()
    data={
        'data_valu':DataOutput
    }
    return render(request,"output.html",data)