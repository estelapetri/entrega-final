from ejemplo.models import Familiar, Vehiculo, Mascota
Familiar(nombre="Rosario", direccion="Rio Parana 745", numero_pasaporte=123123,).save()
Familiar(nombre="Alberto", direccion="Rio Parana 745", numero_pasaporte=890890).save()
Familiar(nombre="Samuel", direccion="Rio Parana 745", numero_pasaporte=345345 ).save()
Familiar(nombre="Florencia", direccion="Rio Parana 745", numero_pasaporte=56756,).save()


Mascota(animal="gato", nombre="Boris", dueno="Estela").save()
Mascota(animal="hamster", nombre="Perez", dueno="Rosario").save()
Mascota(animal="perro", nombre="Nala", dueno="Mariano").save()

Vehiculo(tipo="Moto", marca="Yamaha",titular="Hernan").save()
Vehiculo(tipo="Auto", marca="Toyota",titular="Josefina").save()
Vehiculo(tipo="bicicleta", marca="None",titular="Tamara").save()
print("Se cargo con éxito los usuarios de pruebas")