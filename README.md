# Congruity Signal Engine Lite

A minimal implementation of **continuous proportional evaluation** for complex systems.

This project provides a simple computational layer that evaluates whether a system remains **structurally proportionate** to the resources required to sustain it.

## Concept

Technological systems can be **operationally stable** while still transferring disproportionate pressure to the larger systems that sustain them.

This project explores a minimal formulation of that relationship:

C = V / (E + I + S)

Where:

- **V** → Functional value produced
- **E** → Energy demand
- **I** → Informational complexity
- **S** → Structural / infrastructural load

The resulting index (**C**) acts as a **proportionality signal**.

## Purpose

This is not a full engine.

It is a **minimal, auditable prototype** that demonstrates:

- how proportional relationships can be computed
- how they evolve over time
- how they can generate simple decision signals

## Architecture

Input → Congruity → Temporal Analysis → Signal → Decision Support

## Example

Input:

```json
{
  "V": 0.65,
  "E": 0.80,
  "I": 0.75,
  "S": 0.70
}
```

Output:

```json
{
  "C": 0.29,
  "signal": "ORANGE",
  "action": "REVIEW"
}
```

## Signals

- 🟢 GREEN → proportional
- 🟡 YELLOW → attention
- 🟠 ORANGE → structural drift
- 🔴 RED → critical incongruity

## Position in Governance Stack

Operational Closure  
→ Congruity Evaluation (this layer)  
→ Signal Layer  
→ Decision Layer (Flow / Pause)  
→ Planetary Admissibility

## Scope

This repository intentionally exposes only a **minimal layer**.

Advanced dynamics, adaptive weighting, and multi-scale modelling are outside the scope of this version.

## Vision

The long-term direction is to enable systems to:

- continuously evaluate their proportionality
- detect structural imbalance early
- support governance of large-scale infrastructures

including **AI systems operating at planetary scale**.

## License

MIT (for the lite implementation only)
