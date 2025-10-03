from django.shortcuts import render

def index(request):
    # Lista de diccionarios con datos de dulces
    dulces = [
        {"nombre": "Chocobar", "precio": 2.50, "disponible": True},
        {"nombre": "Gomitas de Frutas", "precio": 1.75, "disponible": True},
        {"nombre": "Galletas de Chocolate", "precio": 3.00, "disponible": False},
    ]
    
    # Contexto para enviar a la plantilla
    context = {
        'lista_dulces': dulces
    }
    
    return render(request, 'index.html', context)