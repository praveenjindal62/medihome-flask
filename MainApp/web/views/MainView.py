from web.views.interfaces.ViewInterface import ViewInterface
from flask import render_template,redirect,Response,abort
from models.Users import Users
from models.Product import Product
import json
from bson.objectid import ObjectId

def checkUserExists(__user_parameters):
    userObj=Users()
    return userObj.find(__user_parameters).count()>0

def getUserFName(__user_parameters):
    userObj=Users()
    return userObj.find(__user_parameters)
def checkLogin(session):
    try:
        if session['user_login']:
            __user_parameter={'email':session['user_login']}
            if checkUserExists(__user_parameter):
                u={'fname':getUserFName(__user_parameter)[0]['fname']}
                return True,u
            return False,None
        return False,None
    except KeyError:
        return False,None

class MainView(ViewInterface):
    def process(self,request,session):
        log,u=checkLogin(session)
        return render_template('main.html',log=log,u=u)

class SignupView(ViewInterface):
    def __validate(self,_signup_parameters):
        if(_signup_parameters['pass'] != _signup_parameters['rpass']):
            return "Password Didnot Match"
        return None

    def process(self,request,session):
        try:
            if session['user_login']:
                return redirect('/main')
        except KeyError:
            pass
        if(request.method=='POST'):
            keys=['email','fname','lname','pass','rpass','gender','ph','add','city']
            _signup_parameters = {x:request.values.get(x) for x in keys}
            validateError=self.__validate(_signup_parameters)
            userObj=Users()
            if validateError==None:
                if(userObj.find({'email':_signup_parameters['email']}).count()>0):
                    return render_template('signup.html',warn={'warning':True,'msg':"Email Address Already Exist"})
                userObj.insert(_signup_parameters)
                #session['user_login']=_signup_parameters['email']
                return render_template('signupdone.html')      
            else:
                return render_template('signup.html',warn={'warning':True,'msg':'validateError'})      
        else:	
            return render_template('signup.html',warn={'warning':False})

class SigninView(ViewInterface):
    def process(self,request,session):
        try:
            if session['user_login']:
                return redirect('/main')
        except KeyError:
            pass
        if(request.method=='POST'):
            keys=['email','pass']
            _signin_parameters = {x:request.values.get(x) for x in keys}
            if(checkUserExists(_signin_parameters)):
                session['user_login']=_signin_parameters['email']
                return redirect('/main/')
            else:
                return render_template('signin.html',warning=True)
        else:
            return render_template('signin.html',warning=False)

class ViewCartView(ViewInterface):
    def process(self,request,session):
        return render_template('viewcart.html')

class CheckOutView(ViewInterface):
    def process(self,request,session):
        return render_template('checkout.html')

class ClearCartView(ViewInterface):
    def process(self,request,session):
        pass

class LogOutView(ViewInterface):
    def process(self,request,session):
        session.pop('user_login')
        return render_template('logout.html')

class SearchView(ViewInterface):
    def process(self,request,session):
        query=request.values.get('query')
        productObj=Product()
        prodList=productObj.findAll(query)
        log,u=checkLogin(session)
        return render_template('search.html',query=query,m=prodList,log=log,u=u)

class ProductView(ViewInterface):
    def process(self,request,session):
        _id=request.values.get('id')
        productObj=Product()
        prodDetail=productObj.find({'_id':ObjectId(_id)})
        if(prodDetail.count()!=1):
            return abort(404)
        log,u=checkLogin(session)
        return render_template('product.html',m=prodDetail[0],log=log,u=u)


