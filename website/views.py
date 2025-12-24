from django.shortcuts import render
from django import forms
from website.forms import ContactForm , NewsletterForm
from django.http import HttpResponse , HttpResponseRedirect 
from django.shortcuts import redirect
from django.contrib import messages

def Home_view(request):
    return render(request , 'website\index.html')

def About_view(request):
    return render(request , 'website\\about.html')

def Contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully')
        else:
            messages.add_message(request, messages.SUCCESS, 'Successfully')
    form = ContactForm()
    return render(request , 'website\contact.html',{'form':form})

def Newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    return redirect('/')

def Elements_view(request):
    return render(request , 'website\elements.html')




