from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'shop/homepage.html')  # Ensure you have a template at 'shop/home.html'

def productdetail(request):
    return render(request, 'shop/productdetail.html')  # Ensure you have a template at 'shop/product_detail.html'

def wishlist(request):
    return render(request, 'shop/wishlist.html')  # Ensure you have a template at 'shop/wishlist.html'