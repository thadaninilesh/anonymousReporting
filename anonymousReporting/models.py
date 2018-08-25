from django.db import models
from django.utils import timezone


class Authority(models.Model):
    authority_name = models.CharField(max_length=1000, default='Anonymous Organization')
    added_on = models.DateTimeField('date added', default=timezone.now)

    class Meta:
        verbose_name = "Authority",
        verbose_name_plural = "Authorities"


class OtherQuestions(models.Model):
    question = models.TextField(max_length=1000, default='Random Question')
    # radio, dropdown, text field type
    question_type = models.CharField(max_length=50)
    isRequired = models.CharField(max_length=5, default='False')
    added_on = models.DateTimeField('date published', default=timezone.now)

    class Meta:
        verbose_name = "Other Question",
        verbose_name_plural = "Other Questions"


class Answers(models.Model):
    uniqueAnswerID = models.AutoField(primary_key=True)
    uniqueUserID = models.TextField(max_length=200)
    authority = models.ForeignKey(Authority, on_delete=models.CASCADE)
    user_name = models.CharField(default='Anonymous', max_length=150)
    user_location = models.CharField(max_length=200)
    issue_date = models.DateTimeField('issue date', default=timezone.now)

    class Meta:
        verbose_name = "Answer",
        verbose_name_plural = "Answers"


class UserAnswerMapping(models.Model):
    uniqueUserAnswerMappingID = models.AutoField(primary_key=True)
    uniqueAnswerID = models.ForeignKey(Answers, on_delete=models.CASCADE, null=True)
    uniqueUserID = models.TextField(max_length=100, null=True)
    uniqueQuestionID = models.ForeignKey(OtherQuestions, on_delete=models.CASCADE)
    answer = models.TextField(max_length=1000, null=True)

    class Meta:
        verbose_name = "User Answer One To May Relationship",
        verbose_name_plural = "User Answer One To May Relationships"



