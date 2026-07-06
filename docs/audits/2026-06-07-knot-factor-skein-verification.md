# Verification: the Step-4 Skein knot factor `a_K` is the h-content reduction

**Date:** 2026-06-07
**Block:** [`conj:knot-factor-frobenius-pairing`](../../content/quantum-observable-universe/mass-theory/knot-factor-frobenius-pairing.md), Step 4.
**Cross-ref:** [`nuclear-knot-classification.md`](../../content/quantum-observable-universe/mass-theory/nuclear-knot-classification.md).

## Scope

This is a **bounded verification**, not a proof of the conjecture. It
settles what the Step-4 "knot factor" `a_K` actually is, because the
phrase *"Skein eigenvalue of `4_1`"* in the block is ambiguous — it could
mean the literal figure-eight knot invariant, or a reduced model
quantity. The answer (below) is the latter, and the Step-4 product
formula is internally consistent with `nuclear-knot-classification`.

Witness:
[`computations/knot-factor-skein-verification.witness.json`](../../computations/knot-factor-skein-verification.witness.json)
(producer `knot_factor_skein_verification.py`, sympy, `all_ok = True`).

## Findings

**1. The Skein product reproduces the canonical table (verified).** With
the per-knot pn-crossing signs of `nuclear-knot-classification.md`, the
product `a_K = ∏_c (1 + sign(c)·h)`, `h = q − q⁻¹`, expands exactly to the
canonical `a_K` column:

| A | crossing signs | `∏(1+sign(c)h)` | canonical `a_K` |
|---|----------------|-----------------|-----------------|
| 2 | `+` | `1 + h` | `1 + h` ✓ |
| 3 | `+, −` | `1 − h²` | `1 − h²` ✓ |
| 4 | `+, −, +, −` | `(1 − h²)²` | `(1 − h²)²` ✓ |

(Numerically at `q₀ ≈ 1.1097`: `1.2086`, `0.9565`, `0.9149`, matching the
table.) So Step 4's product form and the `nuclear-knot-classification`
h-content column are the **same** quantity written two ways — there is no
inconsistency between the blocks.

**2. Clean identity (verified).** `1 − h² = 4 − [3]_q`, with
`[3]_q = q² + 1 + q⁻²`.

**3. `a_K` is the h-content reduction, not the literal knot invariant.**
`a_K = 1 − h²` is degree 1 in `h²` (exponents `{2,0,−2}` in `q`). The
genuine figure-eight Jones polynomial `V(4_1)(t) = t² − t + 1 − t⁻¹ + t⁻²`
is a distinct, higher-degree invariant (span 4, all integer powers). So
`a_K` is **`1` minus the summed h-content of the pn-crossings** — a
reduced model quantity — **not** `V(4_1)`. The block's "Skein eigenvalue
of `4_1`" should be read as this h²-content reduction.

## What stays open

- The crossing-sign assignment per knot (`+` for pn, `−` for pp/nn,
  etc.) is a **modelling input** from `nuclear-knot-classification`, not
  derived here.
- The `A ≥ 5` generalisation via the Wenzl–LR branching identity on the
  self-conjugate stratum (`hecke-branching-trace-decomposition`).
- The claim that this h-content reduction `a_K` is the canonical knot
  factor entering the six-term mass formula.

The block stays `kind: "conjecture"`. This note removes the
"Skein eigenvalue" ambiguity and certifies the Step-4 product is
consistent with the canonical table; it does not close the conjecture.
