from django.shortcuts import (render, redirect, 
                    get_object_or_404, get_list_or_404)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Entry, Tag
from django_blog.settings import PAGE_SIZE

def about(request):
    return render(request, 'blog/about.html')

from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.core.urlresolvers import reverse
from django.views import generic

import forms


class CkEditorFormView(generic.FormView):
    form_class = forms.BlogForm
    #form_class = forms.CkEditorForm
    template_name = 'blog/form.html'

    def get_success_url(self):
        return reverse('ckeditor-form')

ckeditor_form_view = CkEditorFormView.as_view()


def SearchViews(request):
    if 'search' in request.GET:
        search=request.GET['search']
        articles=Entry.objects.filter(title__icontains=search)
        return render_to_response('blog/search_result.html',
                                  {'articles': articles, 'query': search})
    else:
        message='Empty search form'
    return HttpResponse(message)

def blog_home(request):
    return redirect('home', permanent=True)

def not_found(request):
    return render(request, '404.html', {})

def admin_criteria(request):
    '''
        if not login or not super user ,
        then return all published and public articles
    '''
    criteria = {'status':'p'}
    if not(request.user and request.user.is_superuser):
        criteria['is_public']=True
    return criteria

def index(request):
    blog_list = get_list_or_404(
                                Entry.objects.order_by('-publish_time'), 
                                **admin_criteria(request)
    )

    paginator =  Paginator(blog_list, PAGE_SIZE)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'blogs':blogs})


def blog_detail(request,blog_id, blog_link=''):
    blog = get_object_or_404(Entry, 
                            pk=blog_id, 
                            **admin_criteria(request)
    )
    blog.access_count+=1
    blog.save()
    return render(request, 'blog/blog-post.html', {'blog':blog})

def author_blogs(request, username):
    blog_list = get_list_or_404(
                Entry.objects.order_by('-publish_time'), 
                author__username=username,
                **admin_criteria(request)
    )

    paginator =  Paginator(blog_list, PAGE_SIZE)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html',{'blogs':blogs})

def archives(request):
    blogs = get_list_or_404(Entry.objects.order_by('-publish_time'), 
                            **admin_criteria(request)
    )
    paginator =  Paginator(blogs, PAGE_SIZE)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blog/archives.html', {'blogs':blogs})


def tag(request, tag_title):
    '''
    query blogs by tags
    '''
    blogs = get_list_or_404(Entry.objects.order_by('-publish_time'),
                            tags__in=Tag.objects.filter(title=tag_title),
                            **admin_criteria(request)
    )

    paginator =  Paginator(blogs, PAGE_SIZE)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blog/archives.html', {'blogs':blogs})

