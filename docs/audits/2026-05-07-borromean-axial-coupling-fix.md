# Borromean axial-coupling fix

Date: 2026-05-07

Restored `/home/runner/work/qou/qou/folio-assistant/computations/borromean-axial-coupling.py` from `_deprecated/` and fixed the core bug.

## Bug

The deprecated script used

$$
\beta \cdot \sigma_1 \cdot \beta^{-1}.
$$

Any trace-like observable of that expression is cyclic-trivial:

$$
\mathrm{tr}(\beta \sigma_1 \beta^{-1}) = \mathrm{tr}(\sigma_1).
$$

So the old "Borromean suppression" was forced to be `1` identically.

## Fix

The restored script keeps that identity as an explicit diagnostic, then switches to the non-conjugate probe

$$
\beta \cdot \sigma_1.
$$

This is sensitive to the Borromean word and therefore no longer collapses by cyclicity.

## Current status

- cyclic diagnostic: still exactly trivial, as expected.
- direct `β·σ₁` probe: nontrivial.
- probe value: `g_A ≈ 1.3186` from `(5/3) · |tr_std(βσ₁) / tr_triv(βσ₁)|`.

This was an **audit-only probe**, not the final bound-state observable.  The principled observable should use the `G^{-1}` + LP-active-set formula rather than a raw trace ratio.

## 2026-05-07 follow-up: y_λ-weighted Markov trace

The first restoration evaluated the seminormal trace only on the
two-dimensional standard representation `ρ_(2,1)`, which still
under-uses the Specht tower of `n=3`.  The principled Markov trace at
`n=3` is

$$
\mathrm{tr}_M(w) \;=\; \sum_{\lambda \vdash 3} y_\lambda \cdot \chi_\lambda(w),
$$

with `y_λ` the Jones–Markov central coefficients and `χ_λ` the Hecke
character on the Specht module `V_λ`.  The restored script now
consumes the canonical `y_λ` table from
[`y-lambda-jones-markov-witness.json`](../../folio-assistant/computations/y-lambda-jones-markov-witness.json)
and reports per-partition contributions in addition to the totals.

| partition | `y_λ` | `χ_λ(β·σ₁)` | channel `y_λ·χ_λ` |
|---|---|---|---|
| `[3]`     | `+0.4154` | `+1.1100` | `+0.4611` |
| `[2,1]`   | `+0.2809` | `+0.2369` | `+0.0665` |
| `[1,1,1]` | `+0.0227` | `−0.9009` | `−0.0205` |
| **total** |           |           | `+0.5071` |

Result:

- `tr_M(σ_1) = 0.4993` (= `z_markov`, as required by definition).
- `tr_M(β·σ_1) = 0.5071`.
- suppression `= tr_M(β·σ_1) / tr_M(σ_1) = 1.0156`.
- `g_A_predicted = (5/3) · 1.0156 = 1.6927`.
- gap to PDG `1.2754`: relative error `32.7%`.

The trace-cyclicity bug is **fixed** (`tr_M(β·σ_1) ≠ tr_M(σ_1)`) and
the Specht tower is now fully sampled, but the gap to PDG `g_A`
remains structural.  Closing it requires the bound-state observable
master formula `⟨O⟩_T = Σ u_i (G^{-1})_{ij} ⟨O, b_j⟩` on the LP
active set `A*(T)`; see
[`confinement-frobenius-reciprocity.md`](../../content/quantum-observable-universe/particle-interactions/confinement-frobenius-reciprocity.md).
This script remains audit-only because it is still a Markov-trace
probe, not the bound-state observable.
