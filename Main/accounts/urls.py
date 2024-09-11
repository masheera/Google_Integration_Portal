from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('login/',TemplateView.as_view(template_name = 'account/login.html'),name='login'),
    path('accounts/logout/', views.custom_logout, name='logout'),
    path('business-details/', views.business_details, name='business_details'),
]