# The Milnor deficit sign and the weight bar-parity: a convergence, not a derivation

**Date:** 2026-08-01 · **Branch:** `claude/milnor-sign-weight-parity-derivation-2026-08-01` ·
**PR:** #4481 · **Axis:** Δ_λ / Milnor-parity sign law (#4389) · **Builds on:** #4399 Tie B ·
**Tier:** scope-(a) refutation of a derivation route (proved closed-form structure + Lean-proved
order/parity facts; **no fit**; nothing wired).

## 0. The question

#4399 Tie B flagged that the Ocneanu-weight bar-sign `(−1)^{n-1}` (at `n = 3A`, `= (−1)^{3A−1} =
(−1)^{A−1}`) equals the Milnor-parity cluster-deficit sign `(−1)^{A−1}` (#4389), and scoped it as a
"candidate derivation, not proved." This note settles it: **does the deficit sign provably descend
from the weight parity?** No — and there is a concrete structural reason.

## 1. The obstruction (exact)

The proved Borromean deficit closed form is `1 − τ_Borr = h⁴(3+h²)/(h²+4)`:

- its **leading order is `h⁴ = h^{2(A−1)}`** (the Milnor / `(A−1)`-fold-commutator depth);
- the `(q−q⁻¹)^{n-1}` Ocneanu-weight prefactor `h^{n−1} = h⁸` (for `n = 9`) is **ABSENT** — because
  `τ_A` is a *normalized* (link/unlink) ratio, the weight prefactor **cancels**;
- the deficit is **bar-even** (a function of `h²`): its sign is a leading-**coefficient** effect, not
  a bar-parity flip.

Across `A`: the deficit order `2(A−1)` is even and **strictly below** the weight order `3A−1`
(`3A−1 − 2(A−1) = A+1 > 0`). So the weight prefactor is both **cancelled** and **subleading** — it
cannot set the deficit's leading sign.

| A | n=3A | deficit order `2(A−1)` | weight order `n−1` | weight bar-sign | Milnor deficit sign |
|---|------|------------------------|--------------------|-----------------|----------------------|
| 2 | 6 | 2 | 5 | `−` | `−` |
| 3 | 9 | 4 | 8 | `+` | `+` |
| 4 | 12 | 6 | 11 | `−` | `−` |

The signs coincide in **value** while the source orders differ — the hallmark of a convergence.

## 2. Verdict — scope-(a) refutation

**The weight bar-parity cannot be the mechanism of the Milnor deficit sign** (the weight cancels in
the normalized trace and is higher-order). The `(−1)^{A−1}` match is a **convergence via distinct
mechanisms** — Ocneanu-weight prefactor parity vs `(A−1)`-fold-commutator / Milnor depth — **not a
derivation**.

Lean-proved sorry-free
([`MilnorWeightParityConvergence.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/MilnorWeightParityConvergence.lean)):
`deficit_order_even`, `weight_order_gt_deficit`, `weight_parity_eq_cluster_sign`,
`convergence_not_derivation`.

## 3. Why this matters

- **Sharpens #4399 Tie B** — from "candidate derivation, not proved" to "this specific route
  **refuted**."
- **Anti-laundering safeguard** — it forbids passing the `(−1)^{A−1}` coincidence off as a derivation
  of the sign law #4389 explicitly leaves **open** (A=4 measured). Other derivations of the sign law
  remain open; this closes one route, honestly.

| statement | status |
|---|---|
| Borromean deficit leading `h⁴`, weight prefactor `h⁸` absent (cancels), bar-even | **verified (exact)** |
| weight order `3A−1 > 2(A−1)`; `(−1)^{3A−1} = (−1)^{A−1}` | **Lean-proved sorry-free** |
| weight-parity ⇒ deficit-sign **derivation** | **refuted (scope-(a))** |
| the Milnor-parity sign law (general) | **OPEN** (#4389; A=4 measured) — unchanged |

Refs: probe
[`milnor_weight_parity_convergence_probe.py`](../../computations/deltalambda/milnor_weight_parity_convergence_probe.py);
Lean [`MilnorWeightParityConvergence.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/MilnorWeightParityConvergence.lean);
#4399 (Tie B convergence); #4389 (Milnor-parity sign law).
