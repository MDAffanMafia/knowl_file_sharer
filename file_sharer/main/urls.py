from django.urls import path,reverse
from main import views
urlpatterns = [
    path('signUp',views.signUp,name='signUp'),
    path('login',views.login,name='login'),
    path('',views.index,name='index'),
    path('uploadFile',views.uploadFile,name='uploadFile'),
    path('searchUser',views.searchUser,name='searchUser'),
    path('shareFile',views.shareFile,name='shareFile'),
    path('logout',views.logout,name="logout"), 
    path('userDetail',views.userDetail,name='userDetail'),
]