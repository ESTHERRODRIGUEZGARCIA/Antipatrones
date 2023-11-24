# calculadora/views.py

from django.shortcuts import render
from django.http import JsonResponse

def calcular(num1, num2, operacion):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            if num2 != 0:
                resultado = num1 / num2
            else:
                return JsonResponse({'error': 'No se puede dividir entre cero.'})
        else:
            return JsonResponse({'error': 'Operación no soportada.'})

        # Puedes guardar el historial de operaciones si es necesario
        # HistorialOperaciones.objects.create(operacion=operacion, resultado=resultado)

        return JsonResponse({'resultado': resultado})

    except ValueError:
        return JsonResponse({'error': 'Los números ingresados no son válidos.'})

def calculadora(request):
    return render(request, 'calculadora/index.html')