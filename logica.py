import random
import re
from checks import saludo_valido
from patrones import PATRONES, SALUDOS, OFENSIVOS


def procesar(entrada):
    global saludo_valido
    
    entrada_normalizada = entrada.lower().strip()
    
    if not saludo_valido:
        if es_saludo(entrada_normalizada):
            saludo_valido = True
            return respuesta_saludo()
        else:
            return "Hola, me gustaría que me saludases primero."
        
    if contiene_ofensivo(entrada_normalizada):
        return respuesta_ofensivo()
    
    for patron, respuestas in PATRONES:
        match = patron.search(entrada)
        if match:
            return generar_respuesta_patron(match, respuestas)

    return respuesta_por_defecto()


def es_saludo(entrada):
    for saludo in SALUDOS:
        if saludo in entrada:
            return True
    return False


def respuesta_saludo():
    respuestas = [
        "¡Hola! Me alegra conocerte. ¿Cómo te sientes hoy?",
        "¡Hola! Soy ELIZA. ¿En qué puedo ayudarte?",
        "¡Saludos! ¿Qué te trae por aquí hoy?",
        "¡Hola! Cuéntame, ¿cómo ha sido tu día?",
        "¡Hola! Es un placer hablar contigo. ¿Qué tienes en mente?"
    ]
    return random.choice(respuestas)


def contiene_ofensivo(entrada):
    for palabra in OFENSIVOS:
        if palabra in entrada:
            return True
    return False


def respuesta_ofensivo():
    respuestas = [
        "Prefiero que mantengamos una conversación respetuosa.",
        "No me gusta ese tipo de lenguaje. ¿Podemos hablar de otra cosa?",
        "Creo que sería mejor si cambiamos el tema.",
        "Me gustaría que fuéramos más constructivos en nuestra conversación.",
        "¿Por qué no me cuentas algo más positivo?"
    ]
    return random.choice(respuestas)


def generar_respuesta_patron(match, respuestas):

    respuesta_elegida = random.choice(respuestas)
    
    if match.groups():
        try:
            return respuesta_elegida.format(*match.groups())
        except (IndexError, ValueError):
            return respuesta_elegida
    
    return respuesta_elegida


def respuesta_por_defecto():
    respuestas = [
        "No puedo entender tu mensaje "
        "¿Podrías explicarlo de otra manera?",
        "Eso suena interesante, ¿puedes contarme más?",
        "No estoy seguro de lo que quieres decir, ¿puedes aclararlo?",
        "¿Puedes darme más detalles sobre eso?",
        "No estoy seguro de cómo responder a eso, ¿puedes reformular?",
        "Eso es intrigante, ¿puedes elaborarlo un poco más?",
        "No estoy seguro de cómo responder a eso, ¿puedes darme más contexto?"
    ]
    return random.choice(respuestas)

