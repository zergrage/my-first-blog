from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):  # 클래스는 객체를 정의한다. 포스트 안 모델.모델에 의해 이게 장고 디비로 가는 거라는 지시인걸 아는거.
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title