import logging

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Game, Student
from .forms import StudentSignupForm

logger = logging.getLogger(__name__)


def index(request):
    games = Game.objects.all()
    signup_success = request.GET.get('signup') == '1'
    return render(request, 'backend/index.html', {'games': games, 'signup_success': signup_success})


def signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            try:
                student = Student.objects.create(
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    age=form.cleaned_data['age'],
                    phone=form.cleaned_data['phone'],
                    password=make_password(form.cleaned_data['password'])
                )
                logger.info('Student created: id=%s name=%s', student.pk, student.name)
                return render(request, 'backend/index.html', {
                    'games': Game.objects.all(),
                    'signup_success': True,
                    'new_student_id': student.pk,
                    'new_student_name': student.name
                })
            except Exception as e:
                logger.error('Signup error: %s', e, exc_info=True)
                return render(request, 'backend/index.html', {
                    'signup_errors': [f'Server error: {str(e)}'],
                    'games': Game.objects.all()
                })
        else:
            # Collect form errors into a flat list
            errors = []
            for field, field_errors in form.errors.items():
                for error in field_errors:
                    errors.append(error)
            return render(request, 'backend/index.html', {
                'signup_errors': errors,
                'games': Game.objects.all()
            })
    return redirect('index')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('login-email', '').strip()
        password = request.POST.get('login-password', '')

        if not email or not password:
            return render(request, 'backend/index.html', {
                'login_errors': ['Email and password are required.'],
                'games': Game.objects.all()
            })

        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            return render(request, 'backend/index.html', {
                'login_errors': ['No account found with that email.'],
                'games': Game.objects.all()
            })

        if check_password(password, student.password):
            # Store student in session
            request.session['student_id'] = student.pk
            request.session['student_name'] = student.name
            return render(request, 'backend/index.html', {
                'login_success': True,
                'student_name': student.name,
                'games': Game.objects.all()
            })
        else:
            return render(request, 'backend/index.html', {
                'login_errors': ['Incorrect password.'],
                'games': Game.objects.all()
            })
    return redirect('index')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('f-email', '').strip()
        new_password = request.POST.get('f-pass', '')
        confirm_password = request.POST.get('f-confirm', '')

        errors = []
        if not email:
            errors.append('Email is required.')
        if not new_password:
            errors.append('New password is required.')
        if new_password != confirm_password:
            errors.append('Passwords do not match.')

        if errors:
            return render(request, 'backend/index.html', {
                'forgot_errors': errors,
                'games': Game.objects.all()
            })

        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            return render(request, 'backend/index.html', {
                'forgot_errors': ['No account found with that email.'],
                'games': Game.objects.all()
            })

        student.password = make_password(new_password)
        student.save()
        logger.info('Password reset for student: id=%s', student.pk)

        return render(request, 'backend/index.html', {
            'forgot_success': True,
            'games': Game.objects.all()
        })
    return redirect('index')
