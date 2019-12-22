from django.urls import path
from .views import (
    PagesView
)
app_name = 'pages'
urlpatterns = [
    path('', PagesView.as_view(), name='pages-home'),
    path('about/', PagesView.as_view(template_name='pages/about.html'), name='pages-about'),
    path('contact/', PagesView.as_view(template_name='pages/contact.html'), name='pages-contact'),
    ]