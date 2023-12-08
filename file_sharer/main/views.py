from django.shortcuts import render

# Create your views here.
#function for signing in 
def signUp(request):
    return render(request,'index.html')
#function for login
def login(request):
    return render(request,'index.html')
#function for view page/index page
def index(request):
    return render(request,'index.html')
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