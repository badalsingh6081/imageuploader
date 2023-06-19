from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import FileForm
from .models import File
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form= FileForm(request.POST,request.FILES)
            if form.is_valid():
                doc=form.save(commit=False)
                doc.user = request.user
                doc.save()
                messages.success(request,'File Uploaded Successfully')
                return render(request,'myapp/home.html',{'form':form})
    
        form = FileForm
        return render(request,'myapp/home.html',{'form':form})
    else:
        return render(request,'log/login.html')
        


def searchbytitle(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title=request.POST.get('title')
            data=File.objects.filter(title__icontains=title)
            print(data)
            if data :
                return render(request,'log/dashboard.html',{'file':data})
            else:
                messages.success(request,'No Match Found')
                return redirect('/searchtitle/')    
    
        return render(request,'myapp/searchtitle.html')    
    else:
        return render(request,'log/login.html')



    

def searchbydate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            date=request.POST.get('date')
            data=File.objects.filter(date=date)
            if data:
                return render(request,'log/dashboard.html',{'file':data})
            else:
                messages.success(request,'No match found')
                return redirect('/searchdate/')    
            

        return render(request,'myapp/searchdate.html')    
    else:
        return render(request,'log/login.html')

