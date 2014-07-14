from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from MainApp.models import Medicine,Users,Orders,Purchase
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

def HomePage(request):
	l=CartList(request)
	isLoggedin=False
	u,isLoggedin=LogCheck(request)
	return render(request,'main.html',{'u':u,'log':isLoggedin,'l':l,'total':len(l),'redirect':"main",})
def LogCheck(request):
	try:
		email=request.session['user_login'];
		u=Users.objects.get(useremail__iexact=email)
		return u,True
	except KeyError:
		return None,False
def SearchPage(request,query):
	##query=request.GET["query"]
	##query="i"
	l=CartList(request)
	u,isLoggedin=LogCheck(request)
	m=Medicine.objects.filter(name__contains=query)
	return render(request,'search.html',{'m':m,'query':query,'l':l,'total':len(l),'u':u,'log':isLoggedin,'redirect':"search/"+query,})
def ProductPage(request,id):
	m=Medicine.objects.get(medid__iexact=id)
	l=CartList(request)
	u,isLoggedin=LogCheck(request)
	return render(request,'product.html',{'m':m,'l':l,'total':len(l),'u':u,'log':isLoggedin,'redirect':"product/"+id,})
def CartList(request):
	value=request.COOKIES.get('Items_count')
	arr=[]
	if(value==None):
		arr=[]
	else:
		arr=value.split("-")
		arr=arr[:len(arr)-1]
	l=[]
	for i in arr:
		kval=request.COOKIES.get('Item'+i).split("-")
		med=Medicine.objects.get(medid=int(kval[0]))
		l.append(Cart(med,int(kval[1])))
	return l
def CheckCookie(request):
	if request.session.test_cookie_worked():
		print ">>>> TEST COOKIE WORKED!"
		request.session.delete_test_cookie()
def Login(request):
	try:
		if request.session['user_login']:
			return HttpResponseRedirect('/main/')
	except KeyError:
		print("No user Logged IN ")
	if(request.method=='POST'):
		email=request.POST['email']
		passwd=request.POST['pass']
		u=Users.objects.get(useremail__iexact=email)
		if(u.userpass==passwd):
			request.session['user_login']=email
			return HttpResponseRedirect('/main/')
		else:
			return render(request,'login.html',{'warning':True,})
		print request.POST['checkbox']
	else:
		warning=False
		return render(request,'login.html')

def Logout(request):
	del request.session['user_login']
	return HttpResponseRedirect('/main/')
	
def Signup(request):
	try:
		if request.session['user_login']:
			return HttpResponseRedirect('/main/')
	except KeyError:
		print("No user Logged IN ")
	if(request.method=='POST'):
		email=request.POST['email']
		fname=request.POST['fname']
		lname=request.POST['lname']
		passwd=request.POST['pass']
		rpasswd=request.POST['rpass']
		gender=request.POST['gender']
		ph=request.POST['ph']
		add=request.POST['add']
		city=request.POST['city']
		result=validate(email,fname,lname,passwd,rpasswd,gender,ph,add,city)
		if result==None:
			try:
				u=Users.objects.get(useremail=email)
				return render(request,'signup.html',{'warning':True,'msg':"Email Address Already Exist"})
			except ObjectDoesNotExist:
				if(gender=="male"):
					gender="M"
				else:
					gender="F"
				u=Users(userfname=fname,userlname=lname,useremail=email,userpass=passwd,gender=gender,userph=int(ph),useradd1=add,useradd2=city)
				u.save()
				request.session['user_login']=email
				return HttpResponseRedirect('/main/')
		else:
			return render(request,'signup.html',{'warning':True,'msg':result})
			
	else:	
		return render(request,'signup.html')

		
def validate(email,fname,lname,passwd,rpasswd,gender,ph,add,city):
	if not passwd == rpasswd:
		return "Password Didnot Match"
	return None
	
def AddBasket(request,id,count):
	u=Medicine.objects.get(medid=id)
	print u.name
	print count
	value=request.COOKIES.get('Items_count')
	print value
	response=HttpResponseRedirect('/product/'+str(id))
	if value==None:
		response.set_cookie('Items_count', str(u.medid)+"-")
	else:
		if str(u.medid) not in value.split("-"): 
			response.set_cookie('Items_count', value+str(u.medid)+"-")
	value1=request.COOKIES.get('Item'+str(u.medid))
	if value1==None:
		print ">>>>>NEW"
		response.set_cookie('Item'+str(u.medid),str(id)+"-"+str(count))
	else:
		print ">>>>> Already Created"
		c=int(value1.split("-")[1])
		print value1;
		response.set_cookie("Item"+id,str(id)+"-"+str(int(count)+c))
	return response;


def ClearCart(request):
	response=HttpResponseRedirect('/main/')
	if request.COOKIES.has_key('Items_count'):
		value=request.COOKIES.get('Items_count')
		arr=value.split("-")
		arr=arr[:len(arr)-1]
		response.delete_cookie('Items_count')
		for i in arr:
			response.delete_cookie('Item'+i)
	return response

def RemoveItem(request,id,redirect):
	response=HttpResponseRedirect('/'+redirect+'/')
	if request.COOKIES.has_key('Items_count'):
		value=request.COOKIES.get('Items_count').split("-")
		del(value[value.index(id)])
		response.set_cookie('Items_count',"-".join(value))
		response.delete_cookie('Item'+id)
	return response;
def Checkout(request):
	l=CartList(request)
	u,isLoggedin=LogCheck(request)
	totalitem=0
	totalprice=0
	for i in l:
		totalitem+=i.count
		totalprice+=i.price
	return render(request,'checkout.html',{'l':l,'total':len(l),'u':u,'log':isLoggedin,'totalitem':totalitem,'totalprice':totalprice,})
def OrderProcess(request):
	l=CartList(request)
	u,isLoggedin=LogCheck(request)
	if isLoggedin:
		order=Orders(date=datetime.now().date(),shipaddress=u.useradd1+","+u.useradd2)
		order.save()
		for i in l:
			p=Purchase(userid=Users.objects.get(userid=u.userid),item=Medicine.objects.get(medid=i.med.medid),quantity=i.count)
			p.save()
		return HttpResponseRedirect('/clearcart/')
	else:
		return HttpResponseRedirect('/main/')
	
class Cart():
	def __init__(self,med,count):
		self.med=med
		self.count=count
		self.price=med.price*count
