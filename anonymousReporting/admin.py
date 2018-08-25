from django.contrib import admin

# Register your models here.
from .models import Authority, OtherQuestions, Answers, UserAnswerMapping


admin.site.site_header="Anonymous Issue Reporting"
admin.site.register(Authority)
admin.site.register(OtherQuestions)
admin.site.register(Answers)
admin.site.register(UserAnswerMapping)