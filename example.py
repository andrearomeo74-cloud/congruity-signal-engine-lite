from core.congruity import compute_congruity
from core.signals import classify_signal
from core.decision import suggest_action

data = {
    "V": 0.65,
    "E": 0.80,
    "I": 0.75,
    "S": 0.70
}

C = compute_congruity(**data)
signal = classify_signal(C)
action = suggest_action(signal)

print({
    "C": round(C, 3),
    "signal": signal,
    "action": action
})
