from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Business
from accounts.forms import BusinessForm

def custom_logout(request):
    logout(request)
    return redirect('home')  # Redirect to the login page or any other page

def business_details(request):
    user = request.user
    has_business = Business.objects.filter(owner=user).exists()
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.owner = user
            business.save()
            return redirect('review_list_view')  # Redirect to a success page
    else:
        form = BusinessForm()

    context = {
        'form': form,
        'has_business': has_business,
    }
    return render(request, 'accounts/business_details.html', context)
