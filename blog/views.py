from datetime import timezone

from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, FormView, DetailView

from blog.forms import ArticleForm
from blog.models import Article


def test(request):
    return HttpResponse("hello")


class Blog(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-published_date')[:10]
    template_name = 'blog/index.html'

    '''
    def get_queryset(self):
        filter_val = self.request.GET.get('filter', 'amount=20')
        order = self.request.GET.get('orderby', 'amount')
        new_context = SalesOrder.objects.all().order_by(order)
        return new_context
    
    def get_context_data(self, **kwargs):
        context = super(TestList, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', 'amount=33')
        context['orderby'] = self.request.GET.get('orderby', 'amount')
        return context
    '''

class New(FormView):
    template_name = 'blog/add.html'
    form_class = ArticleForm
    success_url = '/blog/'

    def form_valid(self, form):
        art = Article()
        art.title = self.request.POST['title']
        art.content = self.request.POST['content']
        art.image = self.request.FILES['image']
        art.save()
        print(art.image.name)
        return super().form_valid(form)


class ArticleDetailView(DetailView):

    model = Article
    template_name = 'blog/arcticle_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context