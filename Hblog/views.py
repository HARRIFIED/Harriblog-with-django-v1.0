from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from hitcount.views import HitCountDetailView

# def home(request):
#     return render(request, 'home.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))

def DislikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    disliked = False
    if post.dislikes.filter(id=request.user.id).exists():
        post.disllikes.remove(request.user)
        disliked = False
    else:
        post.dislikes.add(request.user)
        disliked = True
        return HttpResponseRedirect(reverse('article-detail',args=[str(pk)]))


class Homeview(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(Homeview, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context 


def CategoryView(request, categories):
    category_posts = Post.objects.filter(category=categories)
    return render(request, 'blog_categories.html', {'categories':categories.title(), 'category_posts': category_posts})
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(CategoryView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context 

def SearchArticle(request):  
    if request.method == "POST":
        searched = request.POST['searched']
        articles = Post.objects.all().filter(title=searched) 
        return render(request, 'search.html', {'searched': searched,
        'articles': articles})
    else:
        return render(request, 'search.html', {})
    
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(SearchArticle, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context 
    

 
class ArticleDetailView(HitCountDetailView):
    model = Post
    template_name = 'article_detail.html'
    count_hit = True

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["category_menu"] = category_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context 


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class UpdatePostview(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = EditForm
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comments.html'
    success_url = reverse_lazy('home')
    ordering = ['-date_added']
    
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    