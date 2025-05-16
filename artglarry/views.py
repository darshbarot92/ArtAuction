from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
import datetime
import smtplib
# Create your views here.
# email for previous bid.
def home(request):
    u_id=request.session.get('user')
    a_id=request.session.get('artist')
    
    if u_id or a_id:
        if u_id:
            res=register.objects.get(id=u_id)
            return render(request,'index.html',{'username':res.username})
        if a_id:
            res=artist_register.objects.get(id=a_id)
            return render(request,'index.html',{'username':res.artist_username})
    data=art.objects.all()
    return render(request,'index.html',{'data':data[0:5]})

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        u_account=request.POST.get('u_account')
        a_account=request.POST.get('a_account')
        if u_account and a_account:
            return render(request,'validation.html',{'error':'Select only One Account'})
        elif u_account:
            res=register.objects.filter(username=username,password=password)
            if len(res)==1:
                request.session['user']=res[0].id
                return redirect('home')
            return render(request,'validation.html',{'login':'Please login here'})
        elif a_account:
            res=artist_register.objects.filter(artist_username=username,password=password)
            if len(res)==1:
                request.session['artist']=res[0].id
                return redirect('home')
            return render(request,'validation.html',{'login':'Please login here'})
        else:
            return render(request,'validation.html',{'error':'Select One Account'})
    return render(request,'validation.html')

def user_reg(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        u_account=request.POST.get('u_account')
        a_account=request.POST.get('a_account')
        if u_account and a_account:
            return render(request,'validation.html',{'error':'Select only One Account'})
        elif u_account:
            usr=register()
            usr.username=username
            usr.password=password
            usr.email=email
            usr.save()
            return render(request,'validation.html',{'login':'Please login here'})
        elif a_account:
            usr=artist_register()
            usr.artist_username=username
            usr.password=password
            usr.email=email
            usr.save()
            return render(request,'validation.html',{'login':'Please login here'})
        else:
            return render(request,'validation.html',{'error':'Select One Account'})
    return render(request,'validation.html')

def profile(request):
    u_id=request.session.get('user')
    a_id=request.session.get('artist')
    if u_id:
        res=register.objects.get(id=u_id)
        return render(request,'profile.html',{'u_username':res.username})
    if a_id:
        res=artist_register.objects.get(id=a_id)
        return render(request,'profile.html',{'a_username':res.artist_username})

def logout(request):
    u_id=request.session.get('user')
    a_id=request.session.get('artist')
    if u_id:
        del request.session['user']
    elif a_id:
        del request.session['artist']
    return redirect('home')
def fillter_data(request):

    data=art.objects.all()
    if data:
        for i in data:
            d=str(i.date).split('-')
            a=datetime.datetime.now()
            b=datetime.datetime(int(d[0]),int(d[1]),int(d[2]))
            bid=user_bid.objects.filter(artist_art=i).last()
            
            if a>b:
                if bid:
                    name=bid.user_name.username
                    res=register.objects.get(username=name)
                    obj=sold()
                    obj.buyer=res
                    obj.art=i
                    obj.amount=bid.bid_price
                    obj.save()
                    user_bid.objects.get(user_name=res,artist_art=i).delete()
                    art_obj=art.objects.get(artist_name=i.artist_name,art_name=i.art_name)
                    art_obj.status='sold'
                    art_obj.save()
                    
                    # mail to art wiiner.
                    s=smtplib.SMTP('smtp.gmail.com',587)
                    s.starttls()
                    s.login('darshbarot68@gmail.com','dhpx moys yzoc qzcl')
                    massage=f'Congratulations Your Bat is maximum on {i.art_name} Please provide your details art delivery.'
                    s.sendmail('darshbarot68@gmail.com',res.email,massage)
                    s.quit()
                else:
                    art_obj=art.objects.get(artist_name=i.artist_name,art_name=i.art_name)
                    art_obj.status='sold'
                    art_obj.save()
    return redirect('product')
# error
def product(request):
    u_id=request.session.get('user')
    a_id=request.session.get('artist')
                     
    data=art.objects.filter(status='pending')
    if u_id or a_id:
        if u_id:
            res=register.objects.get(id=u_id)
            return render(request,'products.html',{'data':data,'username':res.username})
        if a_id:
            res=artist_register.objects.get(id=a_id)
            return render(request,'products.html',{'data':data,'username':res.artist_username})

    return render(request,'products.html',{'data':data})

def upload_art(request):
    u_id=request.session.get('artist')
    if u_id==None:
        return HttpResponse('Sorry this service is Not avilabel Now.')
    a_id=request.session.get('artist')
    artist=artist_register.objects.get(id=a_id)
    if request.method=='POST':
        image=request.FILES.get('image')
        art_name=request.POST.get('art_name')
        date=request.POST.get('date')
        splt=date.split('-')
        date=datetime.datetime(int(splt[0]),int(splt[1]),int(splt[2]))
        art_obj=art()
        art_obj.artist_name=artist
        art_obj.art=image
        art_obj.date=date.strftime('%Y-%m-%d')
        art_obj.art_name=art_name
        art_obj.status='pending'
        art_obj.save()
        return redirect('home')
    return render(request,'upload_art.html',{'username':artist.artist_username})

def product_detail(request):
    u_id=request.session.get('user')
    a_id=request.session.get('artist')
    if u_id:

        user=register.objects.get(id=u_id)
        username=user.username
    elif a_id:
        user=artist_register.objects.get(id=a_id)
        username=user.artist_username
    
    if request.method=='POST':

        id=request.POST.get('id')
        data=art.objects.get(id=id)
        max_bid=user_bid.objects.filter(artist_art=data).last()
        if max_bid:
            max_bid=max_bid.bid_price
        else:
            max_bid=0
        if u_id==None and a_id==None:
            return render(request,'product_detail.html',{'data':data,'max_bid':max_bid})
        return render(request,'product_detail.html',{'data':data,'username':username,'max_bid':max_bid})
    

def user_bids(request):
    
    u_id=request.session.get('user')
    a_id=request.session.get('artist')
    if u_id==None and a_id==None:
        id=request.POST.get('id')
        data=art.objects.get(id=id)
        e_art=user_bid.objects.filter(artist_art=data).last()
        # breakpoint()
        if e_art==None:
            bid=0            
        else:
            bid=e_art.bid_price

        return render(request,'product_detail.html',{'data':data,'max_bid':bid,'login':'.'})
    if u_id:
        user=register.objects.get(id=u_id)
        id=request.POST.get('id')
        data=art.objects.get(id=id)
        bid=request.POST.get('usr_bid')
        e_art=user_bid.objects.filter(artist_art=data).last()
        if e_art:
            if int(bid)>e_art.bid_price:
                obj=user_bid()
                obj.user_name=user
                obj.artist_art=data
                obj.bid_price=int(bid)
                obj.save()
                s=smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login('darshbarot68@gmail.com','dhpx moys yzoc qzcl')
                massage=f'Your Bid has been over taken, rebid for Art_Name:- {data.art_name}'
                s.sendmail('darshbarot68@gmail.com',user.email,massage)
                s.quit()
                
                e_art.delete()
                return render(request,'product_detail.html',{'data':data,'max_bid':bid,'username':user.username})
            else:

                return render(request,'product_detail.html',{'data':data,'max_bid':e_art.bid_price,'username':user.username,'bid_error':'.'})
            
        else:
            obj=user_bid()
            obj.user_name=user
            obj.artist_art=data
            obj.bid_price=int(bid)
            obj.save()
        return render(request,'product_detail.html',{'data':data,'max_bid':bid,'username':user.username,'succes':'.'})
    
    else:
        a_id=request.session.get('artist')
        user=artist_register.objects.get(id=a_id)
        id=request.POST.get('id')
        data=art.objects.get(id=id)
        if a_id:
            return render(request,'product_detail.html',{'data':data,'username':user.artist_username,'error':'.'})
        else:
            return render(request,'product_detail.html',{'data':data,'error':'.'})
        
def order(request):
    u_id=request.session.get('user')
    a_id=request.session.get('artist')
    if u_id:
        res=register.objects.get(id=u_id)
        data=sold.objects.filter(buyer=res)
    else:
        res=artist_register.objects.get(id=a_id)
        data=art.objects.filter(artist_name=res)
        # breakpoint()
        return render(request,'uploaded_art.html',{'username':res.artist_username,'data':data})
    return render(request,'order_history.html',{'username':res.username,'data':data})

def confirm_order(request):
    u_id=request.session.get('user')
    if request.method=='POST':
        res=register.objects.get(id=u_id)
        data=sold.objects.filter(buyer=res,address=None)

        u_add=request.POST.get('address')
        u_city=request.POST.get('city')
        u_state=request.POST.get('state')
        u_no=request.POST.get('number')
        for i in data:
            obj=sold.objects.get(buyer=i.buyer,art=i.art)
            obj.address=u_add
            obj.state=u_state
            obj.city=u_city
            obj.contact=u_no
            obj.save()
        
        return redirect('order')
    return render(request,'detail.html')