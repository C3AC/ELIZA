import re

PATRONES = [
    (re.compile(r'me siento (.+)', re.IGNORECASE), [
        "¿Por qué te sientes {0}?",
        "Cuéntame más sobre por qué te sientes {0}.",
        "Eso suena interesante."
    ]),
    (re.compile(r'estoy (.+)', re.IGNORECASE), [
        "¿Qué te hace sentir {0}?",
        "¿Desde cuándo estás {0}?",
        "¿Te gusta estar {0}?"
    ]),
    (re.compile(r'mi (.+)', re.IGNORECASE), [
        "¿Qué pasa con tu {0}?",
        "¿Siempre tu {0} ha sido así?",
        "¿Te preocupa tu {0}?"
    ]),
    (re.compile(r'trabajo', re.IGNORECASE), [
        "¿Qué opinas de tu trabajo?",
        "¿Te gusta tu trabajo?",
        "¿Cómo va tu trabajo?"
    ]),
    (re.compile(r'.*\?', re.IGNORECASE), [
        "Esa es una buena pregunta.",
        "No estoy seguro, ¿qué piensas tú?",
        "¿Puedes explicarlo un poco más?"
    ]),
]