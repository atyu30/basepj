Django_Blog是一个基于Django、Bootstrap开发的极简博客应用。

1. 支持相册管理
2. 采用富文本编辑器 django-ckeditor

####安装运行
版本要求：python2.7，django1.6  
推荐使用virtualenv安装方式，virtualenv能提供一个隔离的python环境，首先安装virtualenv:  
    
    $ pip install --upgrade virtualenv

然后使用virtualenv创建一个python虚拟环境  

    $ mkdir ~/.virtualenvs
    $ virtualenv ~/.virtualenvs/django_blog
激活虚拟环境django_blog  

    $ source ~/.virtualenvs/django_blog/bin/activate

现在正式开始下载安装：  
    
    (django_blog) $ cd /home/${user}/workspace #你可以把project下载到任意你想放的地方
    (django_blog) $ cd django_blog
    (django_blog) $ pip install -r requirementstxt
    (django_blog) $ python manage.py makemigrations
    (django_blog) $ python manage.py syncdb
    (django_blog) $ python manage.py collectstatic
    (django_blog) $ python manage.py runserver localhost:8000
