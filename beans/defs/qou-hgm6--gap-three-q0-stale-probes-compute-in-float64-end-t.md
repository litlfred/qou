---
# qou-hgm6
title: 'GAP: three q0-stale probes compute in float64 end-to-end — the literal cannot be drained without fixing that first'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T02:45:28Z
updated_at: 2026-11-16T19:28:00Z
parent: qou-2002
---

Found while draining `qou-3f7a`'s q0-value drift (2026-09-04).

## The finding

Five of the ten NEW-stale q0 sites were **not stale witnesses at all** — they are
**hardcoded retired-pin literals in the producers**. The drift audit's own
instruction is *"fix by RE-RUNNING THE PRODUCER, never by hand-editing the
number"*, and for a hardcoded literal **that remedy cannot work**: re-running
reproduces the literal faithfully. Measured — I re-ran all of them and the audit
still flagged the same files.

| producer | line | literal | arithmetic |
|---|---|---|---|
| `probes/rho_f_categorical_probe.py` | 145 | `_mp.mpf("1.1099785955573347")` | mpmath — **fixed** |
| `mu_p_pin_sensitivity_map.py` | 57 | `mpf("1.1099785955573347")` | mpmath — **fixed** |
| `probes/rho_binding_constancy_probe.py` | 25 | `1.10997859555733471` | **float64** |
| `a3_magnitude_berezinian_crossterm_probe.py` | 41 | `1.1099785955573347` | **float64** |
| `probes/saddle_offset_zero_location_probe.py` | 80 | 60-digit literal | **float64** |

The two mpmath ones are fixed (live value from `q_muon_at()`). **The three float64
ones are deliberately NOT fixed**, and that is what this bean is for.

## Why swapping their literal would be laundering

These three import **no mpmath at all** — measured: `mpmath=0` in each;
`a3` uses 3 `math.*` ops, `saddle_offset` 4 plus `Fraction`,
`rho_binding_constancy` delegates. They compute in float64 end to end.

Replacing one float literal with another would **drain the audit while leaving
the defect**, which is exactly the "hand-edit a number to make a gate green"
AGENTS.md bans. The literal is a symptom; the arithmetic is the defect.

## The purest instance, measured

`saddle_offset_zero_location_probe.py:80` assigns a **60-digit** literal to a bare
Python name:

    Q0 = 1.10997859555733471989976322048322502665620840878015405145269

    as a Python float : 1.1099785955573347
    digits retained   : 16

The author wrote 60 digits of intent and got **16**. This is the float64-padding
trap `_precision.py`'s own docstring warns about, in source form rather than at
serialization: *"the number reads as measured while carrying ~15 significant
digits"*.

## What the fix requires

Convert all three to `mpmath` end to end (`set_compute_dps()`, `mpf` throughout,
`fmt` at serialization) and take q0 from `q_parameter`. That **will move their
numbers** — by the float64→50dps difference as well as the 0.0769 ppb re-pin — so
each needs its verdict re-checked, not just a green gate.

## Not decided here

Two of them stamp `q0Anchor: independent` (`a3-magnitude-berezinian-crossterm`,
`rho-f-categorical-probe`) while demonstrably carrying a q0 into their witness.
That label is the subject of bean `qou-324i` (in-progress, sibling claim) and is
deliberately left alone.

## Also blocked, for different reasons

- `hadron-knot-table` — the last `Q0_FLIP` on main. Its producer is out of reach:
  measured >7200 s reaching atom 4 of 19, deuterium alone ≥7170 s.
- `_deprecated/alpha-high-precision` — deprecated tree.

## 2026-11-16 — 50-dps Saddle-Offset Quadratic Root, Berezinian Lift, & rho_binding Constancy Formalized (PR #8169)

- **Lean 4 formalization** (`folio/quantum-observable-universe/lean/QOU/MassTheory/PlancherelNormalisationAndScaleBounds.lean`, `0` `sorry`):
  - `discriminant_193_rational_bracket` & `saddleQuadPoly_at_qQuadRoot_and_bounds`: proves `q_quad = (-9 + √193)/56 ∈ (0.087, 0.088)` is an exact root of `1 - 9q - 28q² = 0`.
  - `berezinianEvenLift_fit_and_residual`: proves zero-mixing lift `= 1`, exact surjectivity fit witness `B* = A(1 - r*)D C⁻¹`, and residual formula.
  - `rho_binding_mirror_mismatch_zero_of_universal`: proves mirror ratio cancellation under a single universal `α_M`.
- **50-dps verification probe**: `computations/probes/plancherel_normalisation_and_scale_bounds_probe.py` and `computations/probes/plancherel-normalisation-and-scale-bounds-probe.witness.json` (PR `litlfred/qou#8169`, head `32d6039de208cfa3dab898932c88023a55ef3267`).
