from django.contrib import admin
from .models import User,Files,FileAccess
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','userEmail','password']
    
@admin.register(Files)
class Files(admin.ModelAdmin):
    list_display=['fileName','content','dateUploaded']    

@admin.register(FileAccess)
class FileAccess(admin.ModelAdmin):
    list_display=['userId','fileId']

