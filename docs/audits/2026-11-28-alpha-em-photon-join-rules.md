# α_EM two-loop: four candidate rules for joining two photon vertices (2026-11-28)

Bean `qou-l4t2`. Carl chose "Compare candidate rules" (2026-11-28): evaluate the
candidates, adopt none. Mathematics only. Lean:
[`QOU/MassTheory/EmPhotonJoinRules.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/EmPhotonJoinRules.lean)
(lean-direct exit 0 with `-DautoImplicit=false`; standard axioms only; no `sorry`).
Follows [the pair-weights note](2026-11-28-alpha-em-photon-pair-weights.md).

## Comparison

Vertices `v`, `w` are convention-D generators `σ`, `τ` with bar images `σ⁻¹`, `τ⁻¹`.

| rule | join | one position | two positions | reading it matches |
|---|---|---|---|---|
| plain product | `v w` | `hσ + 1` | `στ` | none |
| bar-Hermitian | `v̄ w` | `1` | `σ⁻¹τ` | the photon form's own `σ₀σ₁⁻¹` term |
| bar-even | `(v + v̄)(w + w̄)` | `[2]_q² = 4 + h²` | `4στ − 2h(σ + τ) + h²` | θ-graph, after removing the singlet |
| bar-odd, signed | `−(v − v̄)(w − w̄)` | `−h²` | `−h²` | Form B |

## What the comparison shows

- **Only the bar-odd rule is position-blind** (`barOdd_eq`). The other three give
  elements that depend on where the two vertices sit. Their moments then need the
  moment data `m(σ)`, `m(τ)`, `m(στ)`, which the corpus does not fix. The skein chain
  and its moment independence exist only for the bar-odd rule.
- **Only the bar-even rule reproduces the θ-graph**, and only at one position. At two
  positions `barEven_expand` is not a scalar, so the θ-graph's `[3]_q` is a
  same-position statement.
- The plain-product and bar-Hermitian rules match neither reading.

## Scope

This is a comparison, not a choice. Position-blindness is a structural property of the
bar-odd rule (cited invariant `skein_scalar`). It does not show that the bar-odd rule
is the physical one. Adopting a rule is a definition and needs Carl's call. Both
readings stay as labelled fallbacks.
