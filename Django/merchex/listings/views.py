from django.shortcuts import render
from django.http import HttpResponse
from listings.forms import ContactUsForm, BandForm
from listings.models import Band, Listing
from django.core.mail import send_mail
from django.shortcuts import redirect

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'band': bands})

def band_detail(request, id):
   band = Band.objects.get(id=id)
   return render(request, 'listings/band_detail.html', {'band': band})

def about(request):
    return render(request, 'listings/about.html')

def lists(request):
    listt = Listing.objects.all()
    return render(request, 'listings/list.html', {'list': listt})

def email_sent(request):
    return render(request, 'listings/email_sent.html')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)
    return render(request, 'listings/band_update.html', {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        band.delete()
        return redirect('band-list')
    return render(request, 'listings/band_delete.html', {'band': band})
