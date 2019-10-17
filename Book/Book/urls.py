"""Book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 出版社列表
    url(r'^publisher_list/', views.publisher_list),
    # 添加出版社
    url(r'^add_publisher/', views.add_publisher),
    # 删除出版社
    url(r'^delete_publisher/', views.delete_publisher),
    # 编辑出版社
    url(r'^edit_publisher/', views.edit_publisher),

    url(r'^book_list/', views.book_list),
    # 添加书籍
    url(r'^add_book/', views.add_book),
    # 删除书籍
    url(r'^delete_book/', views.delete_book),
    # 编辑书籍
    url(r'^edit_book/', views.edit_book),

    # 作者列表
    url(r'^author_list/', views.author_list),
    # 添加作者
    url(r'^add_author/', views.add_author),
    # 删除作者
    url(r'^delete_author/', views.delete_author),
    # 编辑作者
    url(r'^edit_author/', views.edit_author),

]
