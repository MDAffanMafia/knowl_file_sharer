from django.shortcuts import render,redirect
from main.models import User
from django.contrib.auth import authenticate
# Create your views here.

#enabling user  session 
def enableSession(request,userId,userName):
     request.session['userId']=userId
     request.session['userName']=userName
     
#fetching the user      
def fetchUser(request,userName,password):
     allUser=User.objects.all()
     for user in allUser:
            if user.name==userName and password==password:
                print("found")
                enableSession(request,user.id,user.name)
                print("after")
                return True
     return  False   
 
 #function for signing in    
def signUp(request):
    if request.method=='POST':
        userName=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirmPassword=request.POST['confirmPassword']
        #if password and confirmPassword do not match 
        if password!=confirmPassword:
            print("password are not matching")
            message="Password are not matching"
            return render(request,'signUp.html',{'passwordMatch':message})
        allUser=User.objects.all()
        #if the email already exist
        for user in allUser:
            if user.userEmail==email:
                message="The email already exist"
                return render(request,'signUp.html',{'emailExist':message})
        #if user exist save 
        newUser=User(name=userName,userEmail=email,password=password)
        user=newUser.save()
        #enabling user session
        if fetchUser(request,userName,password):
            print("this")
            return redirect('/')
            
        return render(request,'index.html')
    return render(request,'signUp.html')

#function for login
def login(request):
    if request.method=='POST':
        userName=request.POST['username']
        password=request.POST['password']
        #if userName or password will not match
        #checking whether user exist
        if fetchUser(request,userName,password):
            return render(request,'index.html')
        message="UserName or password incorrect"
        return  render(request,'login.html',{'loginStatus':message})     
    return render(request,'login.html')



#function for view page/index page
def index(request):
    print("this")
    #loading session
    currentSession=request.session.get('userId')
    return render(request,'index.html',{'currentSession':currentSession})
#function for uploading file
def uploadFile(request):
    return render(request,'index.html')
#function for searching other peers
def searchUser(request):
    return render(request,'index.html')
#function for sharing file
def shareFile(request):
    return render(request,'index.html')
#function for logout
def logout(request):
    return render(request,'index.html')