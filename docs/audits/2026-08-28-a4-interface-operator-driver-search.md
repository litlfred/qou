# The A=4 magnitude interface-operator driver route — MEASURED negative (scope-(a))

**Date:** 2026-08-28 · **Bean:** `qou-foh0` (A1) · **Tier:** scope-(a) wall,
measured · **Discipline:** no fit, no wiring, `free_parameters = 0`. The magnitude
stays open; nothing is claimed derived.

## What was asked

`qou-foh0`'s "NEXT HONEST STEP" proposed deriving the A=4 one-scalar magnitude `m`
(the per-pair bond magnitude in `A4InterfaceMagnitude.lean`) from the **interface
operator** `I = c·σ + d` spectral data — the Hecke eigenvalues `q, −q⁻¹` (for the
`pp` bond, `c=1, d=0`, per `a_operator_categorical.py::INTERFACE_COEFS`) — *rather
than* by inverting the AME anchor. This is the honest categorical-driver route. This
audit measures whether it works.

## Setup (all proved / derived upstream)

- `det(I + G) = (1 − 5m²)(1 − m²)`, `b₄ = −ln det`, physical iff `m < 1/√5`
  (`A4InterfaceMagnitude.lean`, exchange spectrum `{±√5, ±1}`, surjective in `m`).
- Required magnitudes (anchor-inversions, **diagnostic-only, never wired**): from the
  sibling qou-j16x under the `E₀ = 4.18598 MeV` det-gate normalization,
  `m*(b₄) = 0.41642`, `m*(μ₄) = 0.35182`; both sit in the physical window `(0, 1/√5)`.

## Method (anti-fit — no winner is ever selected)

Enumerate the natural *parameter-free* dimensionless functionals of `{q, −q⁻¹, h}`
(`h = 1 − q⁻¹`) at the canonical proton-pinned `q₀`, in two families, and classify
each by physicality and distance to the targets:
[`computations/deltalambda/a4_interface_operator_driver_search_probe.py`](../../computations/deltalambda/a4_interface_operator_driver_search_probe.py)
(mpmath, 50 dps, no float64; witness `a4-interface-operator-driver-search.witness.json`).

## Measured result

**Scale-like family (overlap ratios) — ALL overshoot the writhe ceiling (scope-(b)):**

| functional | `m` | `5m²` | physical? |
|---|---|---|---|
| `1/q²` | 0.8117 | 3.29 | ✗ |
| `1/(q²+1)` | 0.4480 | 1.004 | ✗ |
| `z_C = √q/(q+1)` (excised) | 0.4993 | 1.247 | ✗ |
| `z_D = q³/(q²+1)` (canonical naive) | 0.6127 | 1.877 | ✗ |
| `1/[2]_q` | 0.4973 | 1.237 | ✗ |
| `1/q^{3/2}` | 0.9009 | 4.06 | ✗ |
| `1/q³` | 0.7312 | 2.67 | ✗ |

Every "how big is the exchange overlap" functional exceeds `1/√5`, so the naive
braiding overlap is scope-(b) unphysical — the whole-window, both-convention form of
this is now Lean-proved (`A4InterfaceMagnitude.zD_unphysical`, this PR).

**Gap-like family (channel split) + square roots — reaches the target band, no
uniqueness:**

| functional | `m` | physical? | rel. to `m*(b₄)` |
|---|---|---|---|
| `(q²−1)/(q²+1)` | 0.1040 | ✓ | 0.750 |
| `h = 1−1/q` | 0.0991 | ✓ | 0.762 |
| `√((q²−1)/(q²+1))` | 0.3224 | ✓ | 0.226 |
| `√(q−1)` | 0.3316 | ✓ | 0.204 |
| `√(h)` | 0.3148 | ✓ | 0.244 |
| **`√(1−1/q²)`** | **0.4340** | ✓ | **0.042** |

Four functionals land in the band `(0.30, 1/√5)`; the closest, `√(1−1/q²)`, is 4.2 %
from `m*(b₄)` — an order of magnitude above the sibling's 0.1 % "derived-lead" bar,
and *one of several*, not singled out.

## Verdict — SCOPE-(a), confirmed by measurement

The interface operator does **not** supply a parameter-free driver for `m`:

1. The overlap-scale functionals overshoot (scope-(b) excluded).
2. The channel-split family + roots *reaches* the target band — but no single
   functional matches a target to `< 0.1 %`, and **several** land in the band.
   Reaching a target by *choosing among a rich functional family with no uniqueness
   principle* is exactly the signature of a **fit** (an anchor inversion in disguise).

So `qou-foh0`'s proposed next step is measured to a negative: the `{q, −q⁻¹}`
eigenvalue data does not categorically fix `m`. This *extends* the sibling qou-j16x
(which tested derived *constants* as `m` and likewise found no `< 0.1 %` match) to the
specific interface-operator functionals foh0 named. The magnitude stays scope-(a)
open. Nothing is wired; `free_parameters = 0`.

## What would change the verdict

A **categorical uniqueness argument** singling out one functional of `{q, −q⁻¹}`
*before* looking at the target — e.g. a Lean-proved identity forcing the per-pair
bond weight to equal a specific spectral invariant — would convert a band-member into
a derivation. None is known. Absent that, the honest state is: the A=4 magnitude
needs one scalar that no interface-operator functional derives without a choice.
