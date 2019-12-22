from django.shortcuts import render
from django.views import View

# Create your views here.

# class base views
class PagesView(View):
    template_name = 'pages/home.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
        
    # def post(request, *args, **kwargs):
    #     return render(request, 'pages/home.html', {})

# # function based views (HTTP methods)
# def home_view(request, *args, **kwargs):
#     return render(request, 'pages/home.html', {})