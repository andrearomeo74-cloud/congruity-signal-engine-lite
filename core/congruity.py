def compute_congruity(V, E, I, S, eps=1e-6):
    return V / (E + I + S + eps)
