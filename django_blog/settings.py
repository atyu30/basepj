#!/usr/bin/env python
# encoding: utf-8

import time
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xhcg42=d%md&1jcy$c8%#p5e+59!)25v$m$%uq*^1hfx%23i+p'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
DEBUG = True

TEMPLATE_DEBUG = True

STATIC_URL = '/static/'

#for deployment, collects the static files into STATIC_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_URL = '/media/'

TEMPLATE_DIRS =  (
    os.path.join(BASE_DIR, 'templates').replace('\\','/'),        
    os.path.join(BASE_DIR, 'django_blog/apps/blog/templates').replace('\\','/'),        
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'django.contrib.messages.context_processors.messages',
    'apps.blog.processor.tag_list',
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    #'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'reversion',
    'apps.blog',
    'apps.items',
    'apps.bootstrap_pagination',
    'ckeditor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_blog.urls'

WSGI_APPLICATION = 'django_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "djangoblog6",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "3306",
    }
}


ALLOWED_HOSTS = ['*',]

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
TIME_ZONE = 'Etc/GMT%+-d'%(time.timezone/3600)
LANGUAGE_CODE = 'zh-cn'
SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = False

PAGE_SIZE = 7

#compressor
INSTALLED_APPS += ("compressor",)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'compressor.finders.CompressorFinder',
)

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'toolbar': 'Full',
        'toolbarGroups' : [
            { 'name': 'clipboard',   'groups': [ 'clipboard', 'undo' ] },
            { 'name': 'editing',     'groups': [ 'find', 'selection', 'spellchecker' ] },
            { 'name': 'links' },
            { 'name': 'insert' },
            { 'name': 'forms' },
            { 'name': 'tools' },
            { 'name': 'document',       'groups': [ 'mode', 'document', 'doctools' ] },
            { 'name': 'others' },
            '/',
            { 'name': 'basicstyles', 'groups': [ 'basicstyles', 'cleanup' ] },
            { 'name': 'paragraph',   'groups': [ 'list', 'indent', 'blocks', 'align', 'bidi' ] },
            { 'name': 'styles' },
            { 'name': 'colors' },
            { 'name': 'about' },
        ],
        'width' : 960,
        'height' : 380,
        'removeButtons' : 'Underline,Subscript,Superscript',
        'format_tags' : 'p;h1;h2;h3;pre',
        'removeDialogTabs' : 'image:advanced;link:advanced',
        'allowedContent' : True,
    },
}

CKEDITOR_UPLOAD_PATH = "article"
