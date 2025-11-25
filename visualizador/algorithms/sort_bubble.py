# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j, done
    items = list(vals)
    n = len(items)
    i = 0
    j = 0
    done = False

def step():
    global items, n, i, j, done

    if done:
        return {"done": True}

    # Si termina la pasada
    if j >= n - i - 1:
        i += 1
        j = 0
        # Si ya no quedan más pasadas
        if i >= n - 1:
            done = True
            return {"done": True}

    a = j
    b = j + 1
    swap = False

    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    j += 1

    return {"a": a, "b": b, "swap": swap, "done": False}