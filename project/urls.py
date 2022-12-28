
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView 
from ejemplo.views import (mostrar_familiares,mostrar_mascota, mostrar_vehiculo,
                           BuscarFamiliar, AltaFamiliar,
                           ActualizarFamiliar, BorrarFamiliar,
                           AltaVehiculo,  BorrarVehiculo,
                           AltaMascota, ActualizarMascota, BorrarMascota,
                           BuscarMascota, BuscarVehiculo, ActualizarVehiculo) 

""""
from ejemplo.views import (index, mostrar_familiares, BuscarFamiliar, 
                            AltaFamiliar, ActualizarFamiliar, DetalleFamiliar, FamiliarList, FamiliarCrear, FamiliarBorrar)
"""
from ejemplo.views import (mostrar_familiares, BuscarFamiliar, 
                            AltaFamiliar, ActualizarFamiliar, FamiliarDetalle, FamiliarList, FamiliarCrear, FamiliarBorrar,  FamiliarActualizar)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi-familia/', mostrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),#as_view es un metodo de clase, transforma la clase en funcion
    path('mi-familia/alta', AltaFamiliar.as_view()),
     # EL paramatro pk hace referencia al identificador único en la base de datos para Familiar.
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()), # NUEVA RUTA PARA BUSCAR FAMILIAR
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()), # NUEVA RUTA PARA DETALLE DE FAMILIAR
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()), # NUEVA RUTA PARA LISTAR FAMILIAR
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('suceso_de_actualizacion/',TemplateView.as_view(template_name="ejemplo/suceso_de_actualizacion.html")),

    path('mascota/', mostrar_mascota),
    path('mascota/buscar', BuscarMascota.as_view()),
    path('mascota/alta', AltaMascota.as_view()),
    path('mascota/actualizar/<int:pk>', ActualizarMascota.as_view()),#as_view es un metodo de clase, transforma la clase en funcion
    path('mascota/borrar/<int:pk>', BorrarMascota.as_view()),
    


    path('vehiculo/', mostrar_vehiculo),
    path('vehiculo/buscar', BuscarVehiculo.as_view()),
    path('vehiculo/actualizar/<int:pk>', ActualizarVehiculo.as_view()),#as_view es un metodo de clase, transforma la clase en funcion
    path('vehiculo/alta', AltaVehiculo.as_view()),
    path('vehiculo/borrar/<int:pk>', BorrarVehiculo.as_view()),
   
]
