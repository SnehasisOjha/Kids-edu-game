from django.contrib import admin
from .models import Student, Game, Score


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'phone')
    search_fields = ('name', 'email')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'created_at')
    search_fields = ('title',)


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('student', 'game', 'points', 'date_played')
    list_filter = ('game',)
