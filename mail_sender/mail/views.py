# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .tasks import send_email_task
from .forms import MailForm
from .models import SubscriberUser


def home(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_list = [user.email for user in SubscriberUser.objects.filter(is_follow=True)]
            send_email_task.delay(subject, message, recipient_list) ##
            return render(request, 'send/success.html')
    form = MailForm
    return render(request,'send/home.html',{'form': form})
