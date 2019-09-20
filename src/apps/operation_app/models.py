from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


# Create your models here.

def user_directory_path(instance, filename):
    """动态生成上传文件的存储路径"""
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'id_{0}/{1}'.format(instance.user_id.id, filename)


class DuplicateCheckFileSystemStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        if max_length and len(name) > max_length:
            raise (Exception("name's length is greater than max_length"))
        return name

    def _save(self, name, content):
        if self.exists(name):
            # if the file exists, do not call the superclasses _save method
            return name
        # if the file is new, DO call it
        return super(DuplicateCheckFileSystemStorage, self)._save(name, content)


class FilesRecorder(models.Model):
    """用于记录文件与用户对应关系的表"""
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='')
    file_name = models.CharField(max_length=254, null=False)
    hashed_name = models.CharField(max_length=40, null=False)
    content_type = models.CharField(max_length=80, null=False)
    file_type = models.CharField(max_length=30, null=True)
    size = models.CharField(max_length=20, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    deleting_time = models.DateTimeField(null=True, default=None)
    was_in_trashbin = models.BooleanField(default=False)


class SharingRecorder(models.Model):
    """用于记录分享文件与用户对应关系的表"""
    file = models.ForeignKey(to=FilesRecorder, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='owner')
    sharer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='sharer')
    receiver = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='receiver')
    sharing_time = models.DateTimeField(auto_now_add=True)
    is_private_sharing = models.BooleanField(default=False)
    expiry = models.DateTimeField()
    was_deleted = models.BooleanField(null=False, default=False)
    deleted_time = models.DateTimeField(null=True)





