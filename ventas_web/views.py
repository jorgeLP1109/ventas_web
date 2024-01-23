# En views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy




"""def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})"""
@login_required(login_url='/login/')  # Redirects unauthenticated users to the login page
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'product_create.html', {'form': form})

"""@login_required
def edit_product(request, id_producto):
    product = get_object_or_404(Product, id=id_producto)
    
    # Asegúrate de que solo los administradores puedan editar productos
    if not request.user.is_staff:
        return redirect('product_list')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product_edit.html', {'form': form, 'product': product})
"""    


"""class CustomLoginView(LoginView):
    def get_success_url(self):
        return '/'
"""        

@login_required
def edit_product(request, id_producto):
    # Obtén el producto específico o redirecciona si no se encuentra
    product = get_object_or_404(Product, id=id_producto)

    # Asegúrate de que solo los administradores puedan editar productos
    if not request.user.is_staff:
        return redirect('product_list')

    if request.method == 'POST':
        # Si se envió el formulario, procesa la información
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        # Si es una solicitud GET, muestra el formulario con los datos actuales del producto
        form = ProductForm(instance=product)

    return render(request, 'product_edit.html', {'form': form, 'product': product})
def custom_login(request):
    # Lógica de la vista login
    return render(request, 'login.html')


class CustomLogoutView(LogoutView):
    # Lógica personalizada si es necesario
    
    
    pass   

def home(request):
    return render(request, 'home.html')

def otra_vista(request):
    # Puedes agregar lógica adicional aquí si es necesario

    # Datos que puedes pasar a la plantilla (puedes personalizar según tus necesidades)
    data = {
        'titulo': 'Bienvenido a Mi Tienda',
        'mensaje': 'Explora nuestra increíble selección de productos.',
    }

    # Renderiza la plantilla 'home.html' con los datos proporcionados
    return render(request, 'home.html', data)

"""class CustomLoginView(LoginView):
    def get_success_url(self):
        return '/'

# Añade esta línea
custom_login = CustomLoginView.as_view()"""

class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('home')
