from django.db import models

class Post(models.Model):
    title = models.CharField(verbose_name="제목", max_length=128)
    body = models.TextField(verbose_name="내용", default="")
    created_at = models.DateTimeField(verbose_name="작성일", auto_now_add=True)
    photo = models.ImageField(verbose_name='이미지', null=True, upload_to='diary_photo')

    def __str__(self): 
        return self.title
