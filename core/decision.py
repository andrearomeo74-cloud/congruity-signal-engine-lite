def suggest_action(signal):
    return {
        "GREEN": "CONTINUE",
        "YELLOW": "MONITOR",
        "ORANGE": "REVIEW",
        "RED": "PAUSE"
    }.get(signal, "UNKNOWN")
