from multiprocessing import context

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User  # اضافه کردن مدل کاربر


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')  # آدرس داشبورد شما

    if request.method == 'POST':
        email_input = request.POST.get('email')
        password_input = request.POST.get('password')

        if email_input and password_input:
            try:
                # ۱. پیدا کردن کاربر از روی فیلد ایمیل در دیتابیس
                user_obj = User.objects.get(email=email_input)

                # ۲. فرستادن یوزرنیم اصلی دیتابیس و پسورد برای احراز هویت
                user = authenticate(request, username=user_obj.username, password=password_input)

                if user is not None:
                    login(request, user)
                    return redirect('/dashboard/')  # <--- حتما مطمئن شو این صفحه رو ساختی
                else:
                    messages.error(request, 'your password is wrong')
            except User.DoesNotExist:
                messages.error(request, 'your email is wrong')
        else:
            messages.error(request, 'please enter your email and password')

    return render(request, 'login.html')


def dashboard(request):

    return render(request, 'dashboard.html')



from django.shortcuts import render, redirect
from .forms import CustomerForm, NoteForm

def dashboard_view(request):
    if request.method == 'POST':
        # اگر فرم مشتری ارسال شده بود
        if 'add_customer' in request.POST:
            form = CustomerForm(request.POST)
            if form.is_valid():
                form.save() # 🌟 این خط جادویی داده‌ها را مستقیماً در دیتابیس ذخیره می‌کند!
                return redirect('dashboard')