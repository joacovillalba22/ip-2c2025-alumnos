# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1        # insertion arranca en 1
    j = None

def step():
    global items, n, i, j

    # Si terminamos
    if i >= n:
        return {"done": True}

    # Primera vez para este i → iniciamos j
    if j is None:
        j = i
        return {"a": j, "b": j, "swap": False, "done": False}

    # Comparación y swap hacia la izquierda
    if j > 0 and items[j - 1] > items[j]:
        items[j - 1], items[j] = items[j], items[j - 1]
        a = j - 1
        b = j
        j -= 1
        return {"a": a, "b": b, "swap": True, "done": False}

    # Ya no se puede mover más → avanzar al siguiente i
    i += 1
    j = None

    if i >= n:
        return {"done": True}

    return {"a": i, "b": i, "swap": False, "done": False}