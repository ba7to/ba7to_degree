import code
from django.shortcuts import render,redirect
from  .models  import Student
def message(request):
    X = Student.objects.none()  # Initialize X with an empty queryset
    if request.method == 'POST':
        code = request.POST.get("secret_number")
        X = Student.objects.filter(secret_code=code)
        if X.exists():
            return render(request, "html/index.html", {'x':X}) 
    return render(request, "html/index.html", {'x':X})
def Dd(request):
    return render(request,"html/dd.html",{'x':Student.objects.filter(secret_code=code)})

# Create your views here.
