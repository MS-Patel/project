from django.http.response import HttpResponse
from django.shortcuts import render
from bank.forms import LandingForm
from django.contrib.auth.decorators import login_required
from .models import Landing


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
    ledger = Landing.objects.get(username_id=request.user.id)
    context = {"ledger": ledger}
    return render(request, "show.html", context)
