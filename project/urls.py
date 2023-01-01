from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView 
from ejemplo.views import (mostrar_familiares,mostrar_mascota, mostrar_vehiculo,
                           BuscarFamiliar, AltaFamiliar,
                           ActualizarFamiliar, BorrarFamiliar,
                           AltaVehiculo,  BorrarVehiculo,
                           AltaMascota, ActualizarMascota, BorrarMascota,
                           BuscarMascota, BuscarVehiculo, ActualizarVehiculo) 

#from vyj.views import index, PostListar, PostCrear
from vyj.views import (index, PostDetalle, PostListar,
                      PostCrear, PostBorrar, PostActualizar,
                      UserSignUp, UserLogin, UserLogout,
                      AvatarActualizar, UserActualizar, MensajeCrear, MensajeListar, MensajeDetalle)

from django.contrib.admin.views.decorators import staff_member_required

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
    #*************** FINAL A PRESENTAR
    

    path('success_updated_message/',TemplateView.as_view(template_name="vyj_updated_message.html")),
    path('vyj/', index, name="vyj-index"),
    path('vyj/', PostListar.as_view(), name="vyj-listar"),
    path('vyj/<int:pk>/detalle/', PostDetalle.as_view(), name="vyj-detalle"),
    path('vyj/listar/', PostListar.as_view(), name="vyj-listar"),
    path('vyj/crear/', PostCrear.as_view(), name="vyj-crear"),
    path('vyj/<int:pk>/borrar/',staff_member_required(PostBorrar.as_view()), name="vyj-borrar"),
    #estaba la linea 66
    path('vyj/signup/',UserSignUp.as_view(), name="vyj-signup"),
    path('vyj/login/',UserLogin.as_view(), name="vyj-login"),
    path('vyj/logout/',UserLogout.as_view(), name="vyj-logout"),
    path('vyj/<int:pk>/actualizar/', staff_member_required(PostActualizar.as_view()), name="vyj-actualizar"),# lo cambien de lugar
    path('vyj/avatars/<int:pk>/actualizar/', AvatarActualizar.as_view(), name="vyj-avatars-actualizar"),
    path('vyj/user/<int:pk>/actualizar/', UserActualizar.as_view(), name="vyj-user-actualizar"),
    path('vyj/mensajes/crear/', MensajeCrear.as_view(), name="vyj-mensajes-crear"),
    path('vyj/mensajes/<int:pk>/detalle', MensajeDetalle.as_view(), name="vyj-mensajes-detalle"),
    path('vyj/mensajes/listar', MensajeListar.as_view(), name="vyj-mensajes-listar"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
