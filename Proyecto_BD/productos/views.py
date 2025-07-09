from django.shortcuts import render, redirect,  get_object_or_404
from .models import Producto
from django.contrib import messages
from .models import Producto
# Create your views here.

def bienvenida(request):
    return render(request, 'bienvenida.html')

def mostrarIndex(request):
    return render(request, 'index.html')

def mostrarFormRegistrar(request):
    return render(request, 'form_registrar.html')

def mostrarFormActualizar(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'form_actualizar.html', {'producto': producto})

def insertarProducto(request):
    if request.method == 'POST':
        # Capturamos los datos ingresados en el formulario
        nom = request.POST.get('txtnom')
        mar = request.POST.get('cbomar')
        pre = request.POST.get('txtpre')
        
        # Creamos un objeto de tipo Producto
        pro = Producto(nombre=nom, marca=mar, precio=pre)
        # Guardamos en la base de datos
        pro.save()
        messages.success(request, 'Producto registrado con éxito')
        return redirect('form_registrar')  # Redirige para evitar doble inserción       
    
    # Si no es POST o hay error, se muestra el formulario de nuevo
    return render(request, 'form_registrar.html')


def mostrarListado(request):
    productos = Producto.objects.all()  # Obtiene todos los productos de la base de datos
    return render(request, 'listado.html', {'productos': productos})


def actualizarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.nombre = request.POST['txtnom']
        producto.marca = request.POST['cbomar']
        producto.precio = request.POST['txtpre']
        producto.save()
        return redirect('listar_productos')

def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar_productos')


