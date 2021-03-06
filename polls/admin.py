from django.contrib import admin

from .models import Question, Choice

class ChoiceAdmin(admin.StackedInline):
    fieldsets = [
        ("Вариант ответа", {"fields" : ["text", "votes"]} ),
    ]
    
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Текст вопроса", {"fields" : ["text"]} ),
        ("Дата вопроса", {"fields" : ["pubDate"]} ),
    ]

    inlines = [ChoiceAdmin]
    list_filter = ["pubDate"]
    search_fields = ["text"]





admin.site.register(Question, QuestionAdmin)
