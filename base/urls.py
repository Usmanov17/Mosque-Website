from django.urls import path
from .views import HomepageView, ProductListView, Prayer_times, InfoView, NotificationView, MosquesView, DonationView,  sendEmail

app_name='base'

urlpatterns=[
    path("", HomepageView.as_view(), name='homepage'),
    path('support/', DonationView.as_view(), name='donation'),
    path("info/", InfoView.as_view(), name='info'),
    path('products/', ProductListView.as_view(), name='products'),
    path("prayer-times/", Prayer_times.as_view(), name='prayer-times'),
    path("notifications/", NotificationView.as_view(), name='notifications'),
    path("mosques/", MosquesView.as_view(), name='mosques'),
    path('send_mail/', sendEmail, name='send_email'),
]