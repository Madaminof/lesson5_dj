from django.shortcuts import redirect, render

from .forms import ProductForm
from .models import Books,Books_Category,Author,Review
# Create your views here.



def Get_Books_Category(request):
    books_categor = Books_Category.objects.all()
    context = {
        'books_categor': books_categor
    }
    return render(request, 'book_category.html', context=context)

def Get_Books(request,pk):
    books = Books.objects.filter(category_id=pk)
    context = {
        'books': books      
    }
    return render(request, 'books.html', context=context)

def detail(request, pk):
    product1 = Books.objects.get(pk=pk)
    context = {
        'product1': product1
    }
    return render(request, 'product_detail.html', context=context)



def Get_Author(request,pk):
    author=Author.objects.get(pk=pk)
    context={'author':author}
    return render(request,'author.html',context=context)


def Get_Review(request,pk):
    rewiew=Review.objects.get(pk=pk)
    context={'rewiew':rewiew}
    return render(request,'reviews.html',context=context)





def add_products(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('Get_Books')
    context = {
        'form': form
        }
    return render(request, 'create.html', context=context)


def update_products(request, pk):
    data = Books.objects.get(pk=pk)
    form = ProductForm(request.POST, request.FILES, instance=data)
    if form.is_valid():
        print(1)
        form.save()
        return redirect('products:Get_Books_Category')
    context = {
        'form': form
        }
    return render(request, 'update.html', context=context)




from django.shortcuts import get_object_or_404

def delete_product(request, pk):
    product = get_object_or_404(Books, pk=pk)
    
    if request.method == 'POST':
        product.delete()
        return redirect('products:Get_Books_Category')   
    
    return render(request, 'delete.html', {'product': product})









