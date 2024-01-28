from django.shortcuts import render

from .forms import ProductForms
from .models import Product


def update_product(request):
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES)
        message = 'Error'
        if form.is_valid():
            product = Product.objects.get(pk=request.POST['product'])
            product.info = form.cleaned_data['info']
            product.price = form.cleaned_data['price']
            product.quantity = form.cleaned_data['quantity']
            product.img = form.cleaned_data['img']
            product.save()
            message = 'Updating'
    else:
        form = ProductForms()
        message = 'Заполните форму'
    return render(request, 'app_hw_4/form.html', {'form': form, 'message': message})


def img(request, id_):
    product = Product.objects.get(pk=id_)
    print(product.img.url)
    return render(request, 'app_hw_4/img.html', {'img': product.img.url})
