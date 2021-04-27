from django.contrib import admin
from quiz.models import Quiz

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
	list_display = ('question',)


admin.site.site_header = "QUIZ_CHALLANGE ADMIN"
admin.site.site_title = "Quiz_Challange Admin area"
admin.site.index_title = "Welcome to the Quiz Challange admin area"

admin.site.register(Quiz, QuizAdmin)

