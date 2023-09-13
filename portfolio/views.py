from django.shortcuts import render,redirect
from django.contrib import messages
from portfolio.models import Contact,Blogs,Internship

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')




def contact(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Please login to access the page')
        return redirect('/auth/login')
    if request.method=='POST':
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('des')

        query=Contact(name=fname,email=femail,
                      phonenumber=fphoneno,
                      description=fdesc)
        query.save()

        messages.success(request,'Your form has been submitted succesfully')
        return redirect('/contact')
    

    return render(request,'contact.html')

def handleBlog(request):
    posts=Blogs.objects.all()
    context={
        'posts':posts
    }
    return render(request,'blog.html',context)

def intenshipdetails(request):
    if not request.user.is_authenticated:
        messages.warning(request,'Please login to access the page')
        return redirect('/auth/login')

    if request.method=='POST':
        fname=request.POST.get('name')
        fusn=request.POST.get('usn')
        femail=request.POST.get('email')
        foffer=request.POST.get('offer')
        fstartdate=request.POST.get('startdate')
        fenddate=request.POST.get('enddate')
        fprojreport=request.POST.get('projreport')
        fcname=request.POST.get('cname')

#upper case
        fname=fname.upper()
        fusn=fusn.upper()
        fcname=fcname.upper()
        fprojreport=fprojreport.upper()
        foffer=foffer.upper()

        check1=Internship.objects.filter(usn=fusn)
        check2=Internship.objects.filter(email=femail)

        if check1 or check2:
            messages.warning(request,'Your details are stored already')
        return redirect('/intenshipdetails')


        query=Internship(
        fullname=fname,
        usn=fusn,
        email=femail,
        collegename=fcname,
        offer_status=foffer,
        start_date=fstartdate,
        end_date=fenddate,
        proj_report=fprojreport
        )
        query.save()
        messages.success(request,'Form submitted Successfully')
        return redirect('/intenshipdetails')
    
    
    return render(request,'intenshipdetails.html')

    