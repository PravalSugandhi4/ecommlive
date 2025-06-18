from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Render the home page of the shop.
    """
    return render(request, 'shop/base.html')  # Ensure you have a template at 'shop/home.html'