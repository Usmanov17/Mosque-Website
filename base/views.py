from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Product, Namaz, Mosque, Notification
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

class HomepageView(TemplateView):
    template_name='homepage.html'

class InfoView(TemplateView):
    template_name='info.html'

class DonationView(TemplateView):
    template_name='donation.html'

class NotificationView(ListView):
    template_name='notifications.html'
    context_object_name='notifications'
    queryset=Notification.objects.all()

class Prayer_times(ListView):
    template_name='prayer_times.html'
    context_object_name='prayer_times'
    queryset=Namaz.objects.all()
    
class ProductListView(ListView):
    template_name="products.html"
    context_object_name='products'
    queryset=Product.objects.all()

class MosquesView(ListView):
    template_name='mosques.html'
    context_object_name='mosques'
    queryset=Mosque.objects.all()

def sendEmail(request):

    if request.method == 'POST':

        template=render_to_string('email_template.html', {
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email=EmailMessage(
            template,
            settings.EMAIL_HOST_USER,
            ['inha.masjid@gmail.com']
            )

        email.fail_silently=False
        email.send()
    return render(request, 'email_sent.html')