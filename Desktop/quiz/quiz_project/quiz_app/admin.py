from django.contrib import admin
from quiz_app.models import Quiz, Answer,UserAnswer

# class AnswerInline(admin.TabularInline):
#     model = Answer
#     extra = 3

# class QuizAdmin(admin.ModelAdmin):
#     inlines = [AnswerInline]


admin.site.register(Quiz)
admin.site.register(Answer)
admin.site.register(UserAnswer)
