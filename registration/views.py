"""
Registration Application - View Classes and Functions

Views will strive to utilize the inheritance of class based views.  However, where appropriate, function based views should be employed to reduce complexity of code.  Simple is better than complex.
"""
from django.shortcuts import render
from django.views import generic
from registration.models import UserReg


class RegisterView(generic.CreateView):
    """
    How we will handle  registration requests.
    """
    model = UserReg
    success_url = 'registration:reg-complete'
    template_name = 'registration/register.html'
    fields = ['name', 'email']

class ThankYouView(generic.View):
    """
    A simple view to display a thank you message upon regiration completion.
    """
    template_name = 'registration/thankyou.html'
