from django.db import models
from django.contrib.auth.models import User
# ------------------------- [edit] -------------------#

class Question(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    modify_date = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length = 200)    # 질문의 제목
    content = models.TextField()                    # 질문의 내용
    create_date = models.DateTimeField()            # 질문을 작성한 일시

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

