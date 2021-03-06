from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post, Comment
from .forms import CommentForm, CreatePostForm, UpdatePostForm


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post_details', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    categories = Category.objects.all()
    ordering = ['-date_added']

    def get_context_data(self, *args, **kwargs):
        category_list = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_list"] = category_list
        return context


class PostView(DetailView):
    model = Post
    template_name = 'posts/post_details.html'

    def get_context_data(self, *args, **kwargs):
        category_list = Category.objects.all()
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context = super(PostView, self).get_context_data(*args, **kwargs)
        context["category_list"] = category_list
        context["total_likes"] = post.total_likes()
        context["liked"] = liked
        return context


class CreatePostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/post_create.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'posts/post_update.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('home')


class CreateCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'categories/category_create.html'
    success_url = reverse_lazy("home")

    def get_context_data(self, *args, **kwargs):
        category_list = Category.objects.all()
        context = super(CreateCategoryView, self).get_context_data(
            *args, **kwargs)
        context["category_list"] = category_list
        return context


def CategoryView(request, category_name):
    category_posts = Post.objects.filter(
        category=category_name.replace('-', ' '))
    return render(request, 'categories/categories.html', {'category_name': category_name.replace('-', ' ').title(), 'category_posts': category_posts})


def CategoryListView(request):
    category_list = Category.objects.all()
    for cat in category_list:
        cat.name.title()
    return render(request, 'categories/category_list.html', {'category_list': category_list})


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'posts/add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.name = (self.request.user.first_name +
                              " " + self.request.user.last_name)
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
