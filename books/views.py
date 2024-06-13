from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from .models import Books
from .forms import CategoryForm, BookForm


class Index(View):
    def get(self, request):
        return render(request, "index.html")
    

class ProductListView(View):
    
    def get(self, request):
        products = Books.objects.all()
        return render(request, "posts/list.html", {"products": products})
    
    
class CreateCategoryView(View):
    
    def get(self, request):
        form = CategoryForm()
        return render(request, "posts/create.html", {"form": form})
    
    def post(self, request):
        form = CategoryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.publisher = request.user
            post.save()
            return redirect("index")
        return render(request, "posts/create.html", {"form": form})
    
    
class CreateProductView(View):
    def get(self, request):
        form = BookForm()
        return render(request, "posts/create.html", {"form": form})
    
    def post(self, request):
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.publisher = request.user
            post.save()
            return redirect("index")
        return render(request, "posts/create.html", {"form": form})
    
    
class ProductDetail(View):
    def get(self, request, slug):
        product = get_object_or_404(Books, slug=slug)
        return render(request, "posts/detail.html", {"product": product})
    
    def post(self, request, slug):
        product = get_object_or_404(Books, slug=slug)
        return render(request, "posts/detail.html", {"product": product})
    

class UpdeteProductView(UpdateView):
    # permission_required = "change_post"
    # permission_denied_message = "Postni yangilay olmaysiz"
    queryset = Books.objects.all()
    form_class = BookForm
    template_name = "posts/update.html"
    context_object_name = "form"
    success_url = reverse_lazy("index")


class DeleteProductView(DeleteView):
    # permission_required = "delete_post"
    # permission_denied_message = "Postni o'chira olmaysiz"
    queryset = Books.objects.all()
    template_name = "posts/delete.html"
    success_url = reverse_lazy("index")