from django.shortcuts import render
from .models import Post
from groups.models import Group
from django.utils.text import slugify
from .forms import PostCreateForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
import misaka
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def PostCreate(request, slug):
    if request.method == 'POST':
        post_form = PostCreateForm(request.POST)
        if post_form.is_valid:
            group = get_object_or_404(Group, slug=slug)
            post_create = post_form.save(commit=False)
            post_create.user = request.user.username
            post_create.message_html = misaka.html(post_create.message)
            post_create.group = group
            post_create.save()
            return HttpResponseRedirect(reverse('groups:group_single', kwargs={'slug':slug}))
        else:
            print(post_form.errors)
    else:
        post_form = PostCreateForm()

    return render(request, 'posts/post_create.html', {'post_form':post_form})

@login_required
def PostDelete(request, slug, pk):
    post = get_object_or_404(Post, pk=pk)
    group = post.group
    slug = group.slug
    post.delete()
    return HttpResponseRedirect(reverse('groups:group_single', kwargs={'slug': slug}))


def UserPostDetail(request, username):
    user_username = username
    post_all = Post.objects.filter(user=user_username)
    return render(request, 'posts/user_post_detail.html', {'user_username': user_username, 'post_all':post_all})