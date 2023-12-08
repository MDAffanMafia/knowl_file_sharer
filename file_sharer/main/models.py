from django.db import models


def user_directory_path(userId, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(userId, filename)


# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=200)
    userEmail=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    
#for the file uploaded
class Files(models.Model):
    userId=models.IntegerField()
    fileName=models.CharField( max_length=50)
    content=models.FileField(upload_to="prodFiles")
    dateUploaded=models.DateField()

#for the user that can acces the files
class FileAccess(models.Model):
    userId=models.IntegerField()
    fileId=models.IntegerField()
    
            