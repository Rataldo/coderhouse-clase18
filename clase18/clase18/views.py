from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader #necesario importar esto para que funcione el template loader
import datetime



def saludo(request):
    return HttpResponse("Hola Django - coder")

def segunda_vista(request):
    return HttpResponse("<br><br> aqui probando mas cosas")

def template1(self):

    nombre = "Rene"
    
    apellido = "Aranzaez"
    
    lista_de_notas = [1,2,2,6,7,8,9,9]
    
    dicc = {"nombre": nombre, "apellido": apellido,
            "hoy": datetime.datetime.now(),
            "notas": lista_de_notas}
    
    # mi_html = open("./clase18/templates/template1.html") #continuar la ruta directamente despues de lo que aparece en consola
    
    # template = Template(mi_html.read())
    
    # mi_html.close()
    
    # mi_contexto = Context(dicc) #aqui es donde podemos agregar el contexto para ser usado en el template
    
    # documento = template.render(mi_contexto)
    
    plantilla = loader.get_template("template1.html") #aqui usamos el template loader para resumir todo lo anterior
    
    documento = plantilla.render(dicc)
    
    return HttpResponse(documento)

