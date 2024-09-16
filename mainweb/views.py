from django.shortcuts import render

# Create your views here.


def shopView(request):

    return render(request, "mainweb/shop.html")

def singleView(request):

    return render(request, "mainweb/single.html")

def CartView(request):

    return render(request, "mainweb/cart.html")

def checkOutView(request):

    return render(request, "mainweb/checkout.html")

def thanksView(request):

    return render(request, "mainweb/thankyou.html")




def homeView(request):

    return render(request, "mainweb/index.html")


def aboutView(request):

    return render(request, "mainweb/about.html")


def contactView(request):

    return render(request, "mainweb/contact.html")
