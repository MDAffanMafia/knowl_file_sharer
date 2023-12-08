from django.shortcuts import render,redirect
from django.http import HttpResponse
from main.models import User,Files,FileAccess
from django.contrib.auth import authenticate
import datetime
# Create your views here.

#enabling user  session 
def enableSession(request,userId,userName):
     request.session['userId']=userId
     request.session['userName']=userName
#fetching  the user by email
def fetchUserByEmail(userEmail):
    allUser=User.objects.all()
    for user in allUser:
        if user.userEmail==userEmail:
            return {'userName':user.name,'email':user.userEmail,'userId':user.id}    
        return {'userName':"not found",'email':"not found"}
#fetching the user by username and password      
def fetchUser(request,userName,password):
     allUser=User.objects.all()
     for user in allUser:
            if user.name==userName and password==password:
                enableSession(request,user.id,user.name)
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
    #loading session
    currentSession=request.session.get('userId')
    #loading files of the user 
    userFiles=Files.objects.filter(userId=request.session.get('userId'))
    sharedFiles=FileAccess.objects.filter(userId=request.session.get('userId'))
    allFiles=Files.objects.all()
    
    
    
    
    return render(request,'index.html',{'currentSession':currentSession,'userFiles':userFiles,'sharedFiles':sharedFiles,'allFiles':allFiles})
#function for uploading file
def uploadFile(request):
    if request.method=='POST':
        userId=request.session['userId']
        content=request.FILES.get('Uploadfile')
        #changing the filename by appending userId to avoid duplication
        content.name=str(userId)+content.name
        fileName=content.name
        dateUploaded=datetime.date.today()
        newFile=Files(userId=userId,fileName=fileName,content=content,dateUploaded=dateUploaded)
        newFile.save()
    return redirect("/")
#function for searching other peers
def searchUser(request):
    if request.method=='POST':
        userEmail=request.POST['userEmail']
        fileId=request.POST['fileId']
        searchUser=fetchUserByEmail(userEmail)
        fromRoute=request.POST['routeStatus']
        if fromRoute=="fromIndex":
           if searchUser['userName']!="not found":
              userId=searchUser['userId']
              fileShare=FileAccess(userId=userId,fileId=fileId)
              fileShare.save()  
           return render(request,'userDetail.html',{'userDetail':searchUser,'shared':"successfully shared"})
        return render(request,'userDetail.html',{'userDetail':searchUser})
    return render(request,'index.html')
#function for sharing file
def shareFile(request):
    return render(request,'index.html')
#function for logout
def logout(request):
    return render(request,'index.html')
#function fo displaying the user details
def userDetail(request):
    
    return render(request,'userDetail.html')