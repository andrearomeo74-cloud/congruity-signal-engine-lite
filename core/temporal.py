def compute_delta(current, previous):
    return current - previous

def compute_drift(deltas):
    return sum(abs(d) for d in deltas)
