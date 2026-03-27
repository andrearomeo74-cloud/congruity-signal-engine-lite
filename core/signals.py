def classify_signal(C):
    if C > 0.6:
        return "GREEN"
    elif C > 0.4:
        return "YELLOW"
    elif C > 0.25:
        return "ORANGE"
    else:
        return "RED"
