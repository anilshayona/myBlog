from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from theBlog.models import Post, Category, Comment
from .forms import PostForm, EditPostForm, CategoryForm, EditCategoryForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, request


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comments.html'
    # fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        popular = Post.objects.annotate(num_likes=Count('likes')).all().order_by('-num_likes')[:3]
        post_list = Post.objects.all()
        p = Paginator(Post.objects.all(), self.paginate_by)
        loop_times = p.page_range
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        context['loop_times'] = loop_times
        context['popular'] = popular
        context['post_list'] = post_list
        return context


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    cat_menu = Category.objects.all()
    post_list = Post.objects.all()
    popular = Post.objects.annotate(num_likes=Count('likes')).all().order_by('-num_likes')[:3]
    return render(request, 'categories.html',
                  {'cats': cats.title(), 'category_posts': category_posts, 'category_names': cat_menu, 'popular': popular, 'post_list': post_list})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        post_list = Post.objects.all()
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        popular = Post.objects.annotate(num_likes=Count('likes')).all().order_by('-num_likes')[:3]
        context['popular'] = popular
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        context['post_list'] = post_list
        # context["url"] = url
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']


class UpdateCategoryView(UpdateView):
    model = Category
    form_class = EditCategoryForm
    template_name = 'update_category.html'
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy('home')
