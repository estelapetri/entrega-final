"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import ( saludar_a, sumar,
                            mostrar_familiares,
                           BuscarFamiliar, AltaFamiliar,
                        ActualizarFamiliar, BorrarFamiliar,
                        BuscarVehiculo, AltaVehiculo, ActualizarVehiculo, BorrarVehiculo,
                        BuscarMascota, AltaMascota, ActualizarMascota, BorrarMascota)
                           
#from blog.views import index as blog_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar_a/<nombre>/', saludar_a),
    path('sumar/<int:a>/<int:b>/', sumar),
    path('mi-familia/', mostrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),#as_view es un metodo de clase, transforma la clase en funcion
    path('mi-familia/alta', AltaFamiliar.as_view()),
     # EL paramatro pk hace referencia al identificador único en la base de datos para Familiar.
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),

    path('Mascota/buscar', BuscarMascota.as_view()),
    path('Mascota/actualizar/<int:pk>', ActualizarMascota.as_view()),#as_view es un metodo de clase, transforma la clase en funcion
    path('Mascota/alta', AltaMascota.as_view()),
    path('Mascota/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('Vehiculo/buscar', BuscarVehiculo.as_view()),
    path('Vehiculo/actualizar/<int:pk>', ActualizarMascota.as_view()),#as_view es un metodo de clase, transforma la clase en funcion
    path('Vehiculo/alta', AltaVehiculo.as_view()),
    path('Vehiculo/borrar/<int:pk>', BorrarVehiculo.as_view()),
    path('Vehiculo/actualizar/<int:pk>', ActualizarVehiculo.as_view()),
    path('Mascota/borrar/<int:pk>', BorrarMascota.as_view()),
]
