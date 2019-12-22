from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Article
from .forms import ArticleModelForm

# Create your views here.

# --------------<1> built-in generic views------------------------------
# class ArticleListView(ListView):
#     queryset = Article.objects.all() # <appname>/<modelname>.html
    
# class ArticleDetailView(DetailView):
#     queryset = Article.objects.all() # limit the scope of all objects, can use filter to reduce the scope
    
#     def get_object(self):
#         id_ = self.kwargs.get('id')
#         return get_object_or_404(Article, id=id_)

# class ArticleCreateView(CreateView):
#     model = Article
#     form_class = ArticleModelForm
#     queryset = Article.objects.all()
#     # success_url = '/'
    
#     def form_valid(self,form):
#         print(form.cleaned_data)
#         return super().form_valid(form)
        
# class ArticleUpdateView(UpdateView):
#     model = Article
#     form_class = ArticleModelForm
#     queryset = Article.objects.all()
#     # success_url = '/'
    
#     def get_object(self):
#         id_ = self.kwargs.get('id')
#         return get_object_or_404(Article, id=id_)
        
#     def form_valid(self,form):
#         print(form.cleaned_data)
#         return super().form_valid(form)
        
# class ArticleDeleteView(DeleteView):
#     # queryset = Article.objects.all()
#     success_url = '../../'
    
#     def get_object(self):
#         id_ = self.kwargs.get('id')
#         return get_object_or_404(Article, id=id_)
        
#     # def get_success_url(self):
#     #     return reverse('blog:article-list')


# --------------<2> raw class based views------------------------------
class ArticleObjectMixin(object):
    model = Article
    lookup = 'id'
    
    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj
    
class ArticleListView(View):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()
    
    def get_queryset(self):
        return self.queryset
    
    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.get_queryset()
        }
        return render(request, self.template_name, context)

class ArticleDetailView(ArticleObjectMixin, View):
    template_name = 'blog/article_detail.html'
    
    def get(self, request, id, *args, **kwargs):
        obj = self.get_object()
        context = {
            'object': obj
        }
        return render(request, self.template_name, context)
        
class ArticleCreateView(View):
    template_name = 'blog/article_form.html'
    
    def get(self, request, *args, **kwargs):
        form = ArticleModelForm()
        context={
            'form': form
        }
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            form.save()
            form=ArticleModelForm()
        context={
            'form': form
        }
        return render(request, self.template_name, context)

class ArticleUpdateView(ArticleObjectMixin, View):
    template_name = 'blog/article_form.html'
    
    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ArticleModelForm(instance=obj)
            context['form'] = form
            context['object'] = obj
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ArticleModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['form'] = form
            context['object'] = obj
        return render(request, self.template_name, context)
        
class ArticleDeleteView(ArticleObjectMixin, View):
    template_name = 'blog/article_confirm_delete.html'
        
    def get(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)
        
    def post(self, request, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            return redirect('../../')
        return render(request, self.template_name, context)

## --------------<3> function based views-------------------------------
# def article_list_view(request):
#     queryset = Article.objects.all()
    
#     context = {
#         'object_list': qureyset
#     }
    
#     return render(request, 'blog/article_list.html', context)
    
# def article_detail_view(request, id):
#     obj = get_object_or_404(Article, id=id)
    
#     context = {
#         'object': obj
#     }
    
#     return render(request, 'blog/article_detail.html', context)
    
# def article_create_view(request):
#     form = ArticleModelForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form=ArticleModelForm()
#     context={
#         'form': form
#     }
#     return render(request, 'blog/article_form.html', context)
    
# def article_update_view(request, id):
#     obj = get_object_or_404(Article, id=id)
#     form = ArticleModelForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form': form
#     }
#     return render(request, 'blog/article_form.html', context)
    
# def article_delete_view(request, id):
#     obj=get_object_or_404(Article, id=id)
#     if request.method == 'POST':
#         obj.delete()
#         return redirect('../../')
#     context={
#         'object': obj
#     }
#     return render(request, 'blog/article_confirm_delete.html', context)