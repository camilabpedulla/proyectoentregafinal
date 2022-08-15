from django.urls import path 
from appveterinaria.views import *


urlpatterns =  [
    path ("inicio/", index,name="inicio"),
    path ("perros/", indes, name="perros"),
    path ("peces/", indez,name="peces"),
    path ("gatos/", indef, name="gatos"),
    path ("info/", indea, name="info"),
    path ("sugerenciasgatos/", insertardatosgatos, name="gatosbus"),
    path ("sugerenciasperro/", insertardatosperro, name="perrobus"),
    path ("sugerenciaspeces/", insertardatospeces, name="pecesbus"),
 
]   



