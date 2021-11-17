from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

from .models import Article

from .forms import ArticleCreateForm , RawArticleForm

from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    DeleteView,
    UpdateView
)


# Create your views here.



# def article_list_view(request):
#     queryset = Article.objects.all()
#     context = {
#         'object_list': queryset
#     }
#     return render(request,'blog/article_list.html',context)



# def article_create_view(request):
#     my_form = RawArticleForm()
#     if request.method == "POST":
#         my_form = RawArticleForm(request.POST)
#         if my_form.is_valid():
#             #now datat is good
#             print(my_form.cleaned_data)
#             Article.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#         #my_form = RawArticleForm()
#     # Product.objects.create(title=my_new_title)

#     context = {
#         "form": my_form
#     }

#     return render(request,"articles/article_create.html",context)


def article_create_view(request):
    form = ArticleCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleCreateForm()
    
    context = {
        'form': form
    }
    return render(request,"blog/article_create.html",context)



# def article_detail_view(request,id):
#     obj = get_object_or_404(Article,id=id)
#     context={
#         "object": obj
#     }
#     return render(request,'blog/article_detail.html',context)




                                                    #Tutorial Version

class ArticleCreateView(CreateView):
    template_name ='blog/article_create.html'
    form_class = ArticleCreateForm
    queryset = Article.objects.all()
    #success_url = '/'

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '/'



class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()  #<app_name>/<model_name>_list.html


class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    #queryset = Article.objects.all()  #<app_name>/<model_name>_list.html

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)



class ArticleUpdateView(UpdateView):
    template_name ='blog/article_create.html'
    form_class = ArticleCreateForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    template_name = 'blog/article_delete.html'
    #queryset = Article.objects.all()  #<app_name>/<model_name>_list.html

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)

    def get_success_url(self):
        return reverse('blog:articles-list')


