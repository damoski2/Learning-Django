from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect

from .models import Product

from .forms import ProductCreateForm, RawProductForm

# Create your views here.




# def product_create_view(request):
#     my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             #now datat is hood
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#         #my_form = RawProductForm()
#     # Product.objects.create(title=my_new_title)

#     context = {
#         "form": my_form
#     }

#     return render(request,"products/product_create.html",context)



# def product_create_view(request):
#     print(request.GET)
    
#     if request.method == "POST":
#         my_new_title = request.POST.get('title')
#         print(my_new_title)

#     # Product.objects.create(title=my_new_title)
#     context = {
        
#     }

#     return render(request,"products/product_create.html",context)



def product_create_view(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
    
    context = {
        'form': form
    }

    return render(request,"products/product_create.html",context)



# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     #context = {
#     #    'title': obj.title,
#     #   'description':obj.description, 
#     #}
#     context ={
#         'object': obj
#     }
#     return render(request,"products/product_details.html",context)


def product_detail_view(request,id):
    #obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product,id=id)
    # try:
    #     obj = Product.objects.get(id=id)
    # except Product.DoesNotExist:
    #     raise Http404
    context={
        "object": obj
    }
    return render(request,"products/product_details.html",context)



def product_delete_view(request,id):
    obj = get_object_or_404(Product, id=id)
    
    if request.method == "POST":
        #Confirming delete
        obj.delete()
        return redirect('../../')
    context={
        'object': obj
    }
    return render(request,"products/product_delete.html",context)



def product_list_view(request):
    queryset = Product.objects.all()  # List of objects
    context = {
        'object_list': queryset
    }
    return render(request,"products/product_list.html",context)


def product_update_view(request):
    initial_data = {
        'title': "My Awesome Tile"
    }
    obj = Product.objects.get(id=1)
    form = ProductCreateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
    context = { 
        'form': form
    }
    return render(request,"products/product_create.html", context)