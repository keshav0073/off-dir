from django.shortcuts import render,HttpResponse,redirect
from . import forms
from django.contrib.auth.models import User
from .models import *

# Create your views here.
def index(request):
    try:
        footer=footer_icon.objects.all()
        sli=slider.objects.all()
        dr=dr_gedar.objects.all()
        pol_party=political_party.objects.all()
        Testimonial=Testimonials.objects.all()
        Gallery=Gallery_home.objects.all()
        obj=Artical.objects.all().first()
        obj1=Artical.objects.all()
        return render(request,'index.html',{'footer':footer,'sli':sli,'dr':dr,'obj':obj,'obj1':obj1,
        'pol_party':pol_party,'Testimonial':Testimonial,'Gallery':Gallery})
    except:
        return render(request,'index.html',{'footer':footer,'sli':sli,'dr':dr,'obj':obj,'obj1':obj1,
        'pol_party':pol_party,'Testimonial':Testimonial,'Gallery':Gallery})


def about(request):
    footer=footer_icon.objects.all()
    sli=slider.objects.all()
    dr=dr_gedar.objects.all()
    ab_sli=about_slider.objects.all()
    ab_in=about_inner.objects.all()
    return render(request,'about.html',{'footer':footer,'sli':sli,'dr':dr,'ab_sli':ab_sli,'ab_in':ab_in})


def blog(request):
    footer=footer_icon.objects.all()
    dr=dr_gedar.objects.all()
    ab_sli=about_slider.objects.all()
    obj1=Artical.objects.all()
    obj=Artical.objects.all()
    cat=category.objects.all()
    num_count=[]
    for x in obj1:
        # print("here:",x.title)
        title=x.title
        com=comment.objects.filter(title=title).count()
        num_count.append(com)
    # print(num_count)
    print(obj1)

    z_obj=zip(obj1,num_count)
    # print(z_obj)
    z_list=[]
    for x in z_obj:
            # print(x)
            z_list.append(x)

    Recent=[]
    for x in obj[0:3:-1]:
        # print(x)
        Recent.append(x)
    # print(Recent)
    return render(request,'blog.html',{'footer':footer,'dr':dr,'ab_sli':ab_sli,'obj1':obj1,'Recent':Recent,'cat':cat,
    'z_list':z_list})
   

def blog_detail(request,slug):
    # print(slug)
    footer=footer_icon.objects.all()
    dr=dr_gedar.objects.all()
    ab_sli=about_slider.objects.all()
    obj1=Artical.objects.filter(slug=slug)
    for x in obj1:
        title=x.title
    # print(title)
    obj=Artical.objects.all()
    # print("artical is:",obj)
    cat=category.objects.all()
    Recent=[]
    for x in obj[0:3:-1]:
        # print(x)
        Recent.append(x)
    # print(Recent)
    com=comment.objects.filter(title=title)
    # print(com)
    num_comment=com.count()
    return render(request,'blog-detail.html',{'footer':footer,'dr':dr,'ab_sli':ab_sli,'Recent':Recent,
    'obj1':obj1,'cat':cat,'title':title,'com':com,'num_comment':num_comment})


def contact(request):
    footer=footer_icon.objects.all()
    dr=dr_gedar.objects.all()
    ab_sli=about_slider.objects.all()
    return render(request,'contact.html',{'footer':footer,'dr':dr,'ab_sli':ab_sli})

def gallery(request):
    footer=footer_icon.objects.all()
    dr=dr_gedar.objects.all()
    ab_sli=about_slider.objects.all()
    Gallery=Gallery_home.objects.all()
    return render(request,'gallery.html',{'footer':footer,'dr':dr,'ab_sli':ab_sli,'Gallery':Gallery})

def contact_form(request):
    form=forms.Contactform(request.POST or None)
    if request.method == "POST":
        # print("post request coming")
        if form.is_valid():
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            Email=request.POST.get("email")
            phone_number=request.POST.get("phone_number")
            message=request.POST.get("message")
            # print(first_name,last_name)
            x=Contact(first_name=first_name,last_name=last_name,email=Email,number=phone_number,message=message)
            x.save()
        else:
            first_name=form.cleaned_data['first_name'].strip()
            last_name=form.cleaned_data['last_name'].strip()
            Email=form.cleaned_data['email'].strip()
            phone_number=form.cleaned_data['phone_number'].strip()
            message=form.cleaned_data['message'].strip()
            # print("first name is :",first_name)
            # print(last_name,Email,phone_number,message)
            x=Contact(first_name=first_name,last_name=last_name,email=Email,number=phone_number,message=message)
            x.save()

    return redirect('index')

def comment_form(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        website=request.POST.get('website')
        data=request.POST.get('comment')
        title=request.POST.get('title')
        # print(title)
        # print(email,name,website,comment)
        x=comment(name=name,email=email,website=website,text=data,title=title)
        x.save()
        # print("data save")
    return redirect('blog')

def cat(request,slug):
    # print("in cat:",slug)
    footer=footer_icon.objects.all()
    dr=dr_gedar.objects.all()
    ab_sli=about_slider.objects.all()
    obj1=Artical.objects.all()
    obj=category.objects.filter(type=slug)
    cat=category.objects.all()
    Recent=[]
    for x in obj1[0:3:-1]:
        # print(x)
        Recent.append(x)
    global y;
    for x in obj:
        y=x.id
        # print(x.id)
        obj1=Artical.objects.filter(joner=y)
        # print(obj1)
    num_count=[]
    for x in obj1:
        # print("here:",x.title)
        title=x.title
        com=comment.objects.filter(title=title).count()
        num_count.append(com)
    # print(num_count)

    z_obj=zip(obj1,num_count)
    # print(z_obj)
    z_list=[]
    for x in z_obj:
            # print(x)
            z_list.append(x)

    return render(request,"blog_cat1.html",{'footer':footer,'dr':dr,'ab_sli':ab_sli,'obj1':obj1,'cat':cat,'Recent':Recent,
    'z_list':z_list})
   
def get_query(request):
    # print(request)
    footer=footer_icon.objects.all()
    dr=dr_gedar.objects.all()
    ab_sli=about_slider.objects.all()
    cat=category.objects.all()
    obj=Artical.objects.all()
    Recent=[]
    for x in obj[0:3:-1]:
        # print(x)
        Recent.append(x)
    # print(Recent)
    if request.method == "POST":
        x=request.POST.get("search")
        # print("post request comming:",x)
        obj1=Artical.objects.filter(title=x)
        if obj1:
            # print(obj1)
            num_count=[]
            for x in obj1:
                # print("here:",x.title)
                title=x.title
                com=comment.objects.filter(title=title).count()
                num_count.append(com)
                # print(num_count)
                z_obj=zip(obj1,num_count)
                # print(z_obj)
                z_list=[]
                for x in z_obj:
                        # print(x)
                        z_list.append(x)
                return render(request,"search_result.html",{'footer':footer,'dr':dr,'ab_sli':ab_sli,'obj1':obj1,'cat':cat,'Recent':Recent,
                'z_list':z_list})
        else:
            return render(request,"search_result.html",{'footer':footer,'dr':dr,'ab_sli':ab_sli,'cat':cat,'Recent':Recent})
