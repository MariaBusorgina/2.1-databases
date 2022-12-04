from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET['sort']
    template = 'catalog.html'
    phones = list(Phone.objects.all().values())
    if sort == 'name':
        phones = sorted(phones, key=lambda x: x['name'])
    elif sort == 'min_price':
        phones = sorted(phones, key=lambda x: x['price'])
    else:
        phones = sorted(phones, key=lambda x: x['price'], reverse=True)
    context = {
        "phones": phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_obj = Phone.objects.filter(slug=slug).values()
    context = {
        "phone": phones_obj[0]
               }
    return render(request, template, context)
