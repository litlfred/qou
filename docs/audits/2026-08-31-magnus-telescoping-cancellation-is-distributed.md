# The o(dim) cancellation is DISTRIBUTED (within-term dressing + between-term κ), not pairwise (qou-o6ov)

**Date:** 2026-08-31
**Directive (owner):** next (continue the surviving route).
**Scope:** scope-(a); no MeV, no fit, nothing wired.
**Probe:** [`magnus_telescoping_cancellation_probe.py`](../../computations/deltalambda/magnus_telescoping_cancellation_probe.py)
**Follows:** #6349 (the o(dim) is a cancellation, not a norm effect — the operator-norm route
is a dead end).

## What the surviving route must explain

#6349 showed the local commutators `‖⁅σ_g,A_a⁆‖_F` are `Θ(√dim)`, so the O(dim)
submultiplicative bound cannot give the measured `o(dim)`: it is a **cancellation**. By the
Leibniz telescoping (Lean `commutator_mul_left`, on main),
```
⁅ρ,A_a⁆ = Σ_{i: |g_i−a|≤1} T_i,   T_i = (σ_{<i})·⁅σ_{g_i},A_a⁆·(σ_{>i}),
```
a sum of O(1) terms each of Frobenius norm `Θ(√dim)`, yet `‖⁅ρ,A_a⁆‖_F/√dim` decreases with
`b`. This probe measures *how* they cancel:
`κ = ‖Σ_i T_i‖_F / Σ_i ‖T_i‖_F ∈ (0,1]` (1 = none, →0 = total), plus the per-term norms.

Reconstruction cross-check `Σ_i T_i = ⁅ρ,A_a⁆` (the Lean identity, numerically): **1.14e-139
(A=2) / 8.14e-139 (A=3)**.

## Measured (interior germ `a`, exact mpf)

| | A=2 (dim 5→16) | A=3 (dim 8→189, tail 48) |
|---|---|---|
| # terms | **12 (constant)** | **12 (constant)** — O(1) near-`a` support confirmed |
| between-term `κ` | 0.118 → 0.092 (×1.3) | 0.181 → 0.079 (×2.3) |
| within-term `Σ‖T_i‖_F/√dim` | 64.5 → 20.8 (×3.1) | 123 → 16.2 (×7.6) |
| product `‖⁅ρ,A_a⁆‖_F/√dim` | 7.6 → 1.9 (×4) | 22.3 → 1.3 (×17) |

**The `o(dim)` cancellation is distributed across two independent scales:**

1. **Within-term (the dominant one).** Each `T_i = σ_{<i}·⁅σ_{g_i},A_a⁆·σ_{>i}` has Frobenius
   norm *well below* its submultiplicative bound `‖σ_{<i}‖_op·‖⁅σ_{g_i},A_a⁆‖_F·‖σ_{>i}‖_op`
   (which is `Θ(√dim)·const`), and `Σ‖T_i‖_F/√dim` **decreases with b** (×7.6 at A=3). The
   word-piece dressing does not inflate the local commutator the way submultiplicativity
   allows — a cancellation *inside* each term.
2. **Between-term.** The 12 terms sum to ~8–18 % of their norm-sum (`κ ≈ 0.1`), and `κ`
   **decreases with b** (×2.3 at A=3) and **sharpens with A** (×1.3 at A=2 → ×2.3 at A=3).

Both contribute (product = ×17 at A=3); the within-term dressing suppression is larger, but
neither alone accounts for the decay.

## What this rules out and what it leaves

- **Not a pairwise cancellation.** The decay is not `T_i + T_j ≈ 0` for paired terms — it is
  spread across all 12 terms *and* inside each term's dressing. A clean "telescoping collapse"
  argument will not capture it.
- **Two things must be proved together:** (i) the within-term bound
  `‖σ_{<i}·⁅σ_{g_i},A_a⁆·σ_{>i}‖_F = o(√dim)` — a *conjugation* estimate on how the word-pieces
  dress a fixed local commutator (this is where most of the decay is), and (ii) the
  between-term `κ → 0`. Both are sign/phase statements, not norm bounds — consistent with the
  cumulant/connected-diagram framing.

## Honest limits

- **Interior `a` only, `max_λ`-at-each-b, dim capped ≤ 200** (ρ-materialization). The trends
  are clear but are evidence, not proof.
- **Does `‖⁅ρ,A_a⁆‖_F/√dim → 0` or plateau?** Not settled here — it tracks `b`, not `dim`
  cleanly (the large-dim b=4,5 samples at A=3 are 9.0, 4.9). So whether the *whole* o(dim) is
  in the commutator, or partly in the trace/Cauchy–Schwarz step, is still open — the next
  measurement is the **CS slack** `‖⁅ρ,A_a⁆‖_F·‖A_{a+1}‖_F / |t|`.
- **The bound is still open.** This maps the cancellation; it does not prove it.

## Bottom line

The Leibniz telescoping is the exact decomposition (verified to 8e-139), with a **constant
12 terms**, but the `o(dim)` cancellation is **distributed** — mostly a within-term dressing
suppression (`Σ‖T_i‖_F/√dim ↓ ×7.6`) plus a between-term `κ ↓ ×2.3`, both sharpening with `b`
(and `κ` with `A`). No pairwise/collapse shortcut exists; the proof needs a conjugation
estimate on the word-piece dressing *and* the between-term phase cancellation — both
sign-level, matching the cumulant/connected-diagram route. Next: the CS slack, to locate the
last piece (commutator vs trace).
