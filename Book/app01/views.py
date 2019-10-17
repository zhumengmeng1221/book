from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01 import models
# Create your views here.

# 出版社列表
def publisher_list(request):
    ret = models.Publisher.objects.all().order_by("id")
    return render(request,"publisher_list.html",{"publisher":ret})

# 添加新的出版社
def add_publisher(request):
    error = ""
    # 如果是POST请求，我就取到用户填写的数据
    if request.method == "POST":
        add_publisher = request.POST.get("add_name")
        if add_publisher:
            # 从数据库中获取所以的出版社
            all_publisher = models.Publisher.objects.all()
            # 循环判断新添加的出版社名字是否已经存在
            for i in all_publisher:
                # 如果存在返回错误提示
                if i.name == add_publisher:
                    error = "%s 已经存在" % (add_publisher)
                    return render(request,'add_publisher.html', {"error": error})
            # 通过ORM去数据库里创建一条记录
            models.Publisher.objects.create(name=add_publisher)
            # 引导用户访问出版社列表页，查看是否添加成功 ———> 跳转
            return redirect("/publisher_list/")
        else:
            error = "error：出版社名字不能为空 ！"
    # 用户第一次来，我给他返回一个用来填写的HTML页面
    return render(request,'add_publisher.html', {"error": error})
# 删除出版社
def delete_publisher(request):
    del_id = request.GET.get("id")
    if del_id:
        models.Publisher.objects.get(id=del_id).delete()
        return redirect("/publisher_list/")
    else:
        return HttpResponse('<h1 style="color: red">ERROR : 删除的出版社不存在 !</h1>')

# 编辑出版社
def edit_publisher(request):
    edit_id = request.POST.get("id")
    edit_newname = request.POST.get("name")
    edit_publisher = models.Publisher.objects.get(id=edit_id)
    edit_publisher.name = edit_newname
    edit_publisher.save()
    return redirect("/publisher_list/")

    edit_id = request.GET.get("id")
    if edit_id:
        # 获取到当前编辑的出版社对象
        edit_obj = models.Publisher.objects.get(id=edit_id)
        return render(request, "edit_publisher.html", {"publisher": edit_obj})
    else:
        return HttpResponse('<h1 style="color: red">ERROR : 编辑的出版社不存在 !</h1>')

# 展示书籍
def book_list(request):
    all_book = models.Book.objects.all().order_by("id")
    return render(request,"book_list.html",{"all_book":all_book})

#添加书籍
def add_book(request):
    error = ""
    if request.method == "POST":
        add_name = request.POST.get("name")
        publisher = request.POST.get("publish_id")
        if add_name:
            models.Book.objects.create(name=add_name,publish_id=publisher)
            return redirect("/book_list/")
        else:
            error = "error:书名不能为空"

    ret = models.Book.objects.all()
    return render(request,"add_book.html",{"publish_list":ret,"error":error})

#删除书籍
def delete_book(request):
    delete_id = request.GET.get("id")
    if delete_id:
        models.Book.objects.get(id=delete_id).delete()
        return redirect("/book_list/")
    else:
        return HttpResponse('<h1 style="color: red">ERROR : 删除的书籍不存在 !</h1>')

# 编辑书籍
def edit_book(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        if edit_id:
            new_publisher_id = request.POST.get("publisher_id")
            new_name = request.POST.get("name")
            edit_book_obj = models.Book.objects.get(id=edit_id)
            edit_book_obj.name = new_name
            edit_book_obj.publish_id = new_publisher_id
            edit_book_obj.save()
            return redirect(("/book_list/"))
    edit_id = request.GET.get("id")
    if edit_id:
        publisher_list = models.Publisher.objects.all()
        edit_obj = models.Book.objects.get(id=edit_id)
        return render(request,"edit_book.html",{"book_obj": edit_obj, "publisher_list": publisher_list})
    else:
        return HttpResponse('<h1 style="color: red">ERROR : 编辑的书籍不存在 !</h1>')

#作者列表
def author_list(request):
    all_author = models.Author.objects.all().order_by("id")
    return render(request,"author_list.html",{"author_list":all_author})

#添加作者
def add_author(requst):
    error = ""
    if requst.method == "POST":
        new_author_name = requst.POST.get("author_name")
        if new_author_name:
            books = requst.POST.getlist("books")
            new_author_obj = models.Author.objects.create(name=new_author_name)
            new_author_obj.book.set(books)
            return redirect("/author_list/")
        else:
            error = "error: 作者不能为空"
    ret = models.Author.objects.all()
    return render(requst,"add_author.html",{"book_list": ret, "error": error})

#删除作者
def delete_author(request):
    delete_id = request.GET.get("id")
    if delete_id:
        models.Author.objects.get(id = delete_id).delete()
        return redirect("/author_list/")
    else:
        return HttpResponse('<h1 style="color: red">ERROR : 删除的作者不存在 !</h1>')

# 编辑作者
def edit_author(request):
    # 如果编辑完提交数据过来
    if request.method == "POST":
        # 拿到提交过来的编辑后的数据
        edit_author_id = request.POST.get("author_id")
        new_author_name = request.POST.get("author_name")
        # 拿到编辑后作者关联的书籍信息
        new_books = request.POST.getlist("books")
        # 根据ID找到当前编辑的作者对象
        edit_author_obj = models.Author.objects.get(id=edit_author_id)
        # 更新作者的名字
        edit_author_obj.name = new_author_name
        # 更新作者关联的书的对应关系
        edit_author_obj.book.set(new_books)
        # 将修改提交到数据库
        edit_author_obj.save()
        # 返回作者列表页,查看是否编辑成功
        return redirect("/author_list/")
    # 从URL里面取要编辑的作者的id信息
    edit_id = request.GET.get("id")
    # 找到要编辑的作者对象
    edit_author_obj = models.Author.objects.get(id=edit_id)
    # 查询所有的书籍对象
    ret = models.Book.objects.all()
    return render(request, "edit_author.html", {"book_list": ret, "author": edit_author_obj})



























