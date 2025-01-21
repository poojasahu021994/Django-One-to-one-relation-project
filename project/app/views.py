from django.shortcuts import render

def department(request):
    return render(request,'deparmtent_Form.html')

def dep_data(request):
    print(request.method)

    dep_name=request.POST.get('dep_name')
    dep_description=request.POST.get('dep_description')
    dep_HOD=request.POST.get('dep_HOD')
    Department.object.create()


# Create your views here.
