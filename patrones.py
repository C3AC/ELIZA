import re

PATRONES = [
    (re.compile(r'me siento (.+)', re.IGNORECASE), [
        "¿Por qué te sientes {0}?",
        "Cuéntame más sobre por qué te sientes {0}.",
        "Eso suena interesante.",
    ]),
    (re.compile(r'estoy (.+)', re.IGNORECASE), [
        "¿Qué te hace sentir {0}?",
        "¿Desde cuándo estás {0}?",
        "¿Te gusta estar {0}?"
    ]),
    (re.compile(r'mi (\w+)', re.IGNORECASE), [
        "¿Por qué es importante para ti tu {0}?",
        "¿Cómo te afecta tu {0}?",
        "¿Qué te gustaría cambiar sobre tu {0}?"
    ]), 
    (re.compile(r'trabajo', re.IGNORECASE), [
        "¿Qué opinas de tu trabajo?",
        "¿Te gusta tu trabajo?",
        "¿Cómo va tu trabajo?"
    ]),
    (re.compile(r'.*\?', re.IGNORECASE), [
        "Esa es una buena pregunta.",
        "No estoy seguro, ¿qué piensas tú?",
        "¿Puedes explicarlo un poco más?",
        "No estoy segura de poder darte una buena respuesta"
    ]),
    (re.compile(r'quiero (.+)', re.IGNORECASE), [
        "¿Por qué quieres {0}?",
        "¿Qué te impide conseguir {0}?",
        "¿Cómo te sentirías si consiguieras {0}?"
    ]),
    (re.compile(r'\b(ok|okay|está bien|esta bien|bueno)\b', re.IGNORECASE), [
        "Entiendo, ¿quieres hablar de algo más?",
        "Está bien, ¿hay algo más que te gustaría discutir?",
        "De acuerdo, ¿cómo puedo ayudarte hoy?",
        "Perfecto, ¿qué más tienes en mente?"
    ]),
]

SALUDOS = [
    "hola", "hi", "buenas", "buen día", "buenos días", "buenas tardes", 
    "buenas noches", "hey", "qué tal", "cómo estás", "saludos"
]

OFENSIVOS = [
    "idiota", "estúpido", "tonto", "imbécil", "estupidez", "malo", 
    "odio", "odiar", "maldito", "mierda", "inútil", "basura"
]
