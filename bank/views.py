from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from bank.forms import LandingForm
from django.contrib.auth.models import User
from .models import Landing, UserOtp
import random

# Create your views here.


def home(request):
    return render(request, "index.html")


@login_required
def dataform(request):
    if request.method == 'POST':
        form = LandingForm(request.POST)
        if form.is_valid():
            data = Landing()
            data.username = request.user
            data.full_name = form.cleaned_data['full_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            netbalance = form.cleaned_data['credit'] - \
                form.cleaned_data['debit']
            data.balance = netbalance
            data.update()
            return render(request, "index.html")

    else:
        form = LandingForm()
    return render(request, "form.html", {'form': form})


@login_required
def show(request):
    if request.method == 'POST':
        usr = request.user
        print(UserOtp.objects.filter(user=usr).last().otp)
        get_otp = request.POST.get('otp')
        if get_otp:
            usr = request.user
            if int(get_otp) == UserOtp.objects.filter(user=usr).last().otp:
                ledger = Landing.objects.get(username_id=request.user.id)
                context = {"ledger": ledger, "otp": False}
                return render(request, "show.html", context)
            else:
                messages.error(request, 'Invalid OTP')
                return render(request, "show.html", {"otp": True})

    else:
        usr = User.objects.get(username=request.user)
        usr_otp = random.randint(100000, 999999)
        UserOtp.objects.create(user=usr, otp=usr_otp)
        print(usr_otp)
        mess = f"Hello {usr.username},\nYour OTP for login is {usr_otp}\n Don't Share it with anyone"

        context = {"otp": True}

        return render(request, "show.html", context)
