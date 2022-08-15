from django.forms import Form, CharField


class FormularioBusqueda (Form):
    producto =CharField(max_length=150)


class FormularioInsertarDatos(Form):
    marca = CharField(max_length=150)

class FormularioInsertarDatos_perro(Form):
    marca = CharField(max_length=150)

class FormularioInsertarDatos_peces(Form):
    marca = CharField(max_length=150)