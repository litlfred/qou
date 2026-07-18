# α_EM B2 lift — q↔t dictionary shape adjudication (2026-07-18)

**Bean:** `qou-tq20`, tranche 6 — the load-bearing step named by the
tranche-5 structured null ([#4022](https://github.com/litlfred/qou/pull/4022)).

**Probe:** [`computations/alpha_em/alpha_em_qt_dictionary_shape_probe.py`](../../computations/alpha_em/alpha_em_qt_dictionary_shape_probe.py)
→ [`alpha-em-qt-dictionary-shape.witness.json`](../../computations/alpha_em/alpha-em-qt-dictionary-shape.witness.json)
— 4/4 PASS (pre-stated method + tolerance).

**Scope guard (STRICT):** scope-(a) kills (these shapes, alone, as-is); c
pinned by pre-stated rule; no fit; nothing wired; `1/(8π)` stays phase-4.

## Setup

- **Corpus input** (grep first): the canonical rate variable is
  `λ = ln q` ([`crossing-energy-decomposition`](../../content/quantum-observable-universe/observations/crossing-energy-decomposition.md)).
- **Anchor forced** by consistency-1: `q = 1 ↔ t = ∞` (both ends carry the
  multiplicity ratio 3). So dictionaries in the canonical rate are
  reciprocal: `t = c/|λ|^p`, `p ∈ {1, 2}` (pre-stated class).
- **Method** (overdetermined): pin the single constant `c` at one interior
  point (`q* = 0.8`), then every other grid point is a falsifiable
  prediction. Pass bar (pre-stated): ≤ 1% max relative deviation.

## Result — the class is killed

| Shape | c (pinned) | max rel dev over 6-point grid |
|---|---|---|
| `t = c/\|λ\|` | 0.10858 | **18.9%** |
| `t = c/λ²` | 0.02423 | **31.1%** |

Both are O(1) misses — **structural**, not tuning failures (both exceed 10%;
the heat family and the Markov family have genuinely different shapes in the
canonical rate variable).

## Honest reading + reorientation

Within the canonical-rate reciprocal power-law class, **the heat family does
not realize the Markov deformation** — scope-(a): these shapes, alone, as-is,
are excluded. This does **not** refute the τ-identification; it **redirects
the geometric family**: the q-deformation, if realized geometrically, lives
in the **modular direction** (deforming the modulus τ₀) rather than the heat
direction (proper time at fixed modulus). That is the next candidate family
— a genuinely different geometric object (theta ratios as functions of the
modulus, connecting to the #3963 period-matrix front).

## Position

```
qou-tq20: #3985 interface → #3992 ℂ-model → #3999 constructor →
          #4019 consistency-1 (PASS) → #4022 deformation (NULL) →
          THIS dictionary shapes (CLASS KILLED, family redirected to modular)
Wall: the τ-identification — open; next candidate geometric family: the
modular (τ₀-direction) deformation of the isotypic theta weights.
```
