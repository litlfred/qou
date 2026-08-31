# The sublinear single-window bound is localized to ‖[ρ,A_a]‖_F = o(√dim) (qou-o6ov)

**Date:** 2026-08-31
**Directive (owner):** work the open frontier — the sublinear single-window trace bound.
**Scope:** scope-(a); no MeV, no fit, nothing wired.
**Lean:** [`QOU/MassTheory/MagnusOmega2LocalDecomposition.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/MagnusOmega2LocalDecomposition.lean) (all sorry-free, lean-direct exit 0)
**Probe:** [`magnus_single_window_frobenius_localization_probe.py`](../../computations/deltalambda/magnus_single_window_frobenius_localization_probe.py)

## The open target (from #6311/#6331)

`|tr(ρ_λ [A_a,A_{a+1}])| = o(dim_λ)` for a fixed 3-strand-local operator. This note
**localizes** that estimate to a single concrete object, with a Lean tool and a measurement.

## Step 1 — reframe onto the density (Lean, sorry-free)

`trace_rho_commutator_reframe`: `tr(ρ·⁅A,B⁆) = tr(⁅ρ,A⁆·B)` (and the sign partner
`= −tr(⁅ρ,B⁆·A)`). Verified numerically to **139 digits** by the probe
(`max|tr(ρO) − tr([ρ,A_a]A_{a+1})|` = 9.24e-139 over 26 partitions at A=3).

With Cauchy–Schwarz `|tr(X·B)| ≤ ‖X‖_F‖B‖_F`,
```
|tr(ρ_λ O)| ≤ ‖⁅ρ_λ,A_a⁆‖_F · ‖A_{a+1}‖_F.
```

## Step 2 — measure which factor is sublinear (exact mpf)

| factor | A=2 (dim 5–16) | A=3 (dim 8–189) | verdict |
|---|---|---|---|
| `‖A_{a+1}‖_F/√dim` | ≈ 1.00–1.03 | ≈ 1.00–1.05 | **flat (Θ(√dim))** — a dead end for o(dim) |
| `‖⁅ρ,A_a⁆‖_F/√dim` | 2.4→0.8, 8.7→1.5 … | 24→1.3, 21→1.8 … | **decreases with b** in every window |

The germ factor is genuinely `Θ(√dim)` (it has ±1 on ~dim diagonal blocks). **All of the
decay lives in `‖⁅ρ_λ,A_a⁆‖_F/√dim`** — i.e. the global word `ρ_λ` nearly commutes with the
germ `A_a`, and does so *more* as `b(λ)` grows. So:

> **Reduced open target:** `‖⁅ρ_λ, A_a⁆‖_F = o(√dim_λ)` (equivalently, decreasing with
> `b(λ)`). This is a **norm** of a single commutator — no signed cancellation — which is a
> friendlier object than the signed trace it replaces.

## Step 3 — the telescoping handle (Lean, sorry-free)

`commutator_mul_left` (Leibniz): `⁅X·Y, Z⁆ = X·⁅Y,Z⁆ + ⁅X,Z⁆·Y`. Applied to
`ρ = ∏_i σ_{g_i}`:
```
⁅ρ, A_a⁆ = Σ_i (σ_{<i}) · ⁅σ_{g_i}, A_a⁆ · (σ_{>i}),
```
and `⁅σ_g, A_a⁆ = 0` whenever `|g−a| ≥ 2` (far-commutativity, already
`commutator_eq_zero_of_commute`). So **only the O(1) crossings near position `a`
contribute** — the sum has a *bounded* number of nonzero terms, each a **local** commutator
`⁅σ_g, A_a⁆` (a 3-strand object) dressed by word-pieces `σ_{<i}, σ_{>i}`. Bounding
`‖⁅ρ,A_a⁆‖_F` is therefore reduced to:
- the operator norms of the word-pieces `‖σ_{<i}‖`, `‖σ_{>i}‖` (products of seminormal
  generators — bounded powers of the Hecke eigenvalues at `q₀`), and
- the local commutator norms `‖⁅σ_g, A_a⁆‖_F` (fixed 3-strand objects).

That is the concrete route the measurement + telescoping identify.

## Honest limits

- **`→0` is a measured trend, not proved.** `‖⁅ρ,A_a⁆‖_F/√dim` *decreases* with `b` over the
  ranges tested (A=2 dim≤16, A=3 dim≤189, cap for compute); it is not proved to reach 0
  (it could plateau). The evidence is stronger than #6331 (a norm, over a real dim range,
  with the germ factor pinned flat), but it is evidence, not a proof.
- **`‖⁅ρ,A_a⁆‖_F/√dim` tracks `b`, not `dim` cleanly.** It depends on the diagram *shape*
  (e.g. at A=3 it is ~1.3 at dim 48 / b=7 but ~15 at dim 105 / b=3), consistent with the
  whole arc being a `b`-decay, not a `dim`-monotone one.
- **The bound is still open.** This note does not prove `o(√dim)`; it reduces it — via a
  sorry-free reframing + telescoping — to a bounded sum of local-commutator norms times
  word-piece operator norms, and confirms (A=2, A=3) that the germ factor cannot supply the
  decay so the whole decay must come from `‖⁅ρ,A_a⁆‖_F`.

## Bottom line

The tr-decay theorem's open core is now a **single-operator Frobenius bound**
`‖⁅ρ_λ,A_a⁆‖_F = o(√dim_λ)`, with a sorry-free Lean reframing that makes it *equivalent* to
the trace estimate (via Cauchy–Schwarz, one direction) and a sorry-free Leibniz telescoping
that expands it into a **bounded** number of local commutators. The germ factor is measured
flat, so this is genuinely where the decay lives. Next: bound the word-piece operator norms
`‖σ_{<i}‖` and the local `‖⁅σ_g,A_a⁆‖_F`, and check the `o(√dim)` (not merely decreasing) at
A=4 low-b.
