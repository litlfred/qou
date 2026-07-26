# Δ_λ residual is a two-operator (binding − saturation) object — capstone formalization

**Date:** 2026-07-26
**PR:** #4379 (`claude/deltalambda-two-operator-split-2026-07-26`)
**Lean:** [`content/quantum-observable-universe/lean/QOU/MassTheory/TwoOperatorResidualSplit.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/TwoOperatorResidualSplit.lean)
**Verification:** `lean`-direct exit 0, sorry-free, no warnings.

## Summary

The three just-merged cluster-sign walls established, in isolation, three signed facts:

| PR | file | proved fact |
|----|------|-------------|
| #4360 | `BorromeanThreeBodyCluster.lean` | Brunnian/Borromean binding cluster `c₃ = E₀·(1 − τ_Borr) ≥ 0` (`borromean_cluster_nonneg`) — supplies the `μ₃ > 0` sign |
| #4354 | `Mu4RhoFCluster.lean` | multiplicative interface cluster `1 − ∏ fᵢ` beyond-pairwise content `≤ 0` (`pairwise_3body_content_nonpos`, mirror of `productModel_3body_nonpos`) |
| #4376 | `HeliumFourBodyCluster.lean` | A=4 residual `μ₄ = −4.591 < 0` (`mu4Residual_neg`); Brunnian A=4 deficit still `≥ 0` (`brunnian4Cluster_nonneg`); the two are sign-incompatible (`sign_swap_a3_a4`) |

This file reads those three **together as a single decomposition**: the per-isotope
binding residual moment sequence `{μₖ}` (forward AME−model, 0-fit: `μ₂ = 0`,
`μ₃ = +0.4708`, `μ₄ = −4.591`) is **not one closing coefficient** but a **signed
sum of two operators of opposite sign**:

```
μₖ = Bₖ − Sₖ,   Bₖ ≥ 0 (binding, Brunnian/Borromean deficit),   Sₖ ≥ 0 (saturation magnitude)
```

## The derived content

Composed purely from the merged sign lemmas (reused, not reproved):

1. **Sign selection.** `residual_pos_iff` / `residual_neg_iff`:
   `0 < B − S ⟺ S < B` (binding-dominated) and `B − S < 0 ⟺ B < S`
   (saturation-dominated). So the sign of `μₖ` picks the dominant operator:
   - `μ₃ > 0` ⟹ `S₃ < B₃`: the positive odd moment is carried by the non-negative
     Brunnian/Borromean operator (`borromean_cluster_nonneg`, #4360).
   - `μ₄ < 0` (`mu4Residual_neg`, #4376) ⟹ `B₄ < S₄`: the negative even moment is
     carried by the non-positive multiplicative operator
     (`pairwise_3body_content_nonpos`, #4354).

2. **Single-sign bounds.** `pure_binding_nonneg` (a `S = 0` model is `≥ 0`
   everywhere) and `pure_saturation_nonpos` (a `B = 0` model is `≤ 0` everywhere).

3. **Two-operator necessity.** `binding_alone_ne_mu4` (a binding-only model can
   never equal `μ₄ < 0`) and `saturation_alone_ne_mu3` (a saturation-only model
   can never equal `μ₃ > 0`). Hence two operators of opposite sign are
   *structurally* required — no single-sign operator spans both moments. This is
   `sign_swap_a3_a4` (#4376) re-read as a decomposition.

4. **Concrete split from the proved lemmas.** `borromeanMinusSaturation` builds a
   `SignedResidualSplit` whose binding half `B = E₀·(1 − τ_Borr) ≥ 0` is
   `borromean_cluster_nonneg` and whose saturation half
   `S = 2 − f_a − f_b − f_c + f_a f_b f_c ≥ 0` is `saturationMagnitude_nonneg`
   (which reuses `pairwise_3body_content_nonpos`). Both signs come from the merged
   proofs. `brunnian4MinusSaturation` is the A=4 analogue via
   `brunnian4Cluster_nonneg`.

5. **Capstone.** `residual_is_two_operator` packages (1)+(2)+(3): binding-dominated
   at A=3, saturation-dominated at A=4, and the two-operator necessity.

## Scope — honest (anti-fit / anti-laundering)

- **DERIVED:** the sign of each operator (`B ≥ 0`, `S ≥ 0`), the sign of `μ₄`
  (`< 0`), and the sign-selection / necessity logic. All by composition of the
  existing sorry-free lemmas — no new class field assumes the conclusion.
- **NOT claimed:** that the *concrete operator magnitudes* sum to the exact AME
  `μₖ`. The per-λ magnitude closure is the **OPEN Δ_λ gate**; the bare-`H₃`
  Borromean scale (`~0.006 MeV`, #4360; lifted to `~0.30 MeV = 0.63× μ₃` at H₉,
  #4364) is not the target coefficient, and any magnitude tuned to `μₖ` would be a
  FIT and is not made. The identity `μ = B − S` enters the domination theorems as
  a modeling **hypothesis** (`hmodel`), never a fitted equation.
  `signed_split_exists` records only the *trivial* weak existence (`B = max μ 0`,
  `S = max (−μ) 0`) and explicitly flags the strong (magnitude) form as open.
- **0 free parameters.** No `μₖ` is inverted to fix any coefficient; `μ₃`'s numeric
  value enters no proof; nothing is wired to production.

Per AGENTS.md §"Before declaring 'refuted' / 'ruled out'": the two-operator
necessity is a **scope-(b) structural exclusion** — it cites a proved invariant
(a single non-negative operator cannot produce a negative value, and vice versa),
so "no single-sign operator reproduces both signs" is a legitimate structural
claim, not an over-narrowing scope-(a) negative.

## Verification method

`lake build` intentionally NOT used (rebuilds Mathlib from source, wipes the
restored olean cache). Instead: the three sibling modules were compiled to oleans
with `lean`-direct (each imports only `Mathlib.Tactic`, ~6 s against the restored
Mathlib cone), then `TwoOperatorResidualSplit.lean` was checked with `LEAN_PATH`
pointing at the restored Mathlib packages + the freshly-built sibling oleans:
exit 0, sorry-free, no warnings.

Base ring §7c: `ℝ`, because every statement is an archimedean ordering/sign fact
(`0 ≤`, `<`, `≠` against a signed numeric target) — matching the three sibling
wall files.
