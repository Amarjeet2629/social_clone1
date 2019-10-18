from django.shortcuts import render
from .models import Group, GroupMember
from django.utils.text import slugify
from .forms import GroupCreateForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
import misaka
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def CreateGroup(request):
    if request.method == 'POST':
        create_form = GroupCreateForm(request.POST)
        if create_form.is_valid:
            group_form = create_form.save(commit=False)
            group_form.slug = slugify(group_form.name)
            group_form.description_html = misaka.html(group_form.description)
            # group_form.members.add(request.user)
            group_form.save()

            return HttpResponseRedirect(reverse('index'))
        else:
            print(create_form.errors)
    else:
        create_form = GroupCreateForm()
    return render(request, 'groups/group_create.html',
                  {'create_form': create_form})


def GroupList(request):
    group_list = Group.objects.all()
    return render(request, 'groups/group_list.html',
                  {'group_list': group_list})


def GroupSingle(request, slug):
    group = get_object_or_404(Group, slug=slug)
    return render(request, 'groups/group_single.html', {'group': group})

@login_required
def GroupJoin(request, slug):
    group_name = get_object_or_404(Group, slug=slug)
    group = GroupMember(group=group_name, user=request.user)
    group_name.member.add(group.user)
    return HttpResponseRedirect(reverse('groups:group_single', kwargs={'slug':slug}))

@login_required
def GroupLeave(request, slug):
    group_name = get_object_or_404(Group, slug=slug)
    group_mem = get_object_or_404(GroupMember, group=group_name, user=request.user)
    group_name.member.remove(group_mem.user)
    group_mem.delete()
    return HttpResponseRedirect(reverse('groups:group_single', kwargs={'slug': slug}))
