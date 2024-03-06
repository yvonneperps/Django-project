from django.shortcuts import render,redirect

from patients.forms import EmployeeForm
from patients.forms import StudentForm
from patients.forms import Student


# Create your views here.
def employee_form(request):
    form = EmployeeForm()
    return render(request, 'employee_form.html', {'form':form})
def employee_list(request,id=0):
   if request.method == 'GET':
       if id==0:
           form = StudentForm()
       else:
        employee = Student.objects.get(pk=id)
        form = StudentForm(instance=employee)
       return render(request, 'employee_list.html', {'form':form})
   else:
        if id==0:
            form = StudentForm(request.POST)
        else:
            employee = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
            return redirect('Student/show')

def show(request):
    context = {'show': Student.objects.all()}
    return render(request, 'show.html', context)