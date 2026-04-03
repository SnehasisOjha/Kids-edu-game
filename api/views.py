from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def get_questions(request):
    questions = [
        {"id": 1, "question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
        {"id": 2, "question": "What color is the sky?", "options": ["Blue", "Green", "Red"], "answer": "Blue"},
    ]
    return JsonResponse({"questions": questions})
