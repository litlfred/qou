---
# qou-k4f8
title: 'Dual certificate existence for the operator-selection LP: formalize first, then symbolic'
status: todo
type: task
priority: normal
created_at: 2026-08-16T12:50:00Z
updated_at: 2026-08-16T12:50:00Z
---

Follows `k4ul` (#5216, theorem proved) and `0tjt` (#5231, box shown
non-binding by the paper's own text). Those establish that
`operator_selection_lp` holds **given** a dual certificate. This bean asks
whether one exists.

## The question, stated exactly

`k4ul`'s hypotheses require `s : Fin d → R` with

```
s ≥ 0        and        ∀ j,  t j = y_0_star + Σᵢ sᵢ · G i j
```

`G` is the Frobenius Gram matrix `Gᵢⱼ = tr_M(bᵢbⱼ)`, hence **symmetric**, so in
vector form the second condition is

```
t = y₀ · 𝟙 + G s ,      s ≥ 0
```

— `d` equations in `d + 1` unknowns `(y₀, s)` with a sign constraint. Existence
is **not** automatic: it asks whether `t` lies in the cone `{y₀𝟙 + Gs : s ≥ 0}`,
`y₀ ∈ ℝ`. That is a genuine Farkas-type question about the substrate data.

## Method: formalize first, then compute

Per AGENTS.md. Do not start from numerics.

1. **Lean, statement.** Define
   `DualCertificateExists (t G) : Prop := ∃ y₀ s, (∀ i, 0 ≤ s i) ∧ ∀ j, t j = y₀ + Σᵢ s i * G i j`
   and prove the two reductions that make it checkable:
   - if `G` is invertible, `s = G⁻¹(t − y₀𝟙)`, so existence reduces to
     `∃ y₀, ∀ i, 0 ≤ (G⁻¹(t − y₀𝟙))ᵢ` — a one-parameter sign condition;
   - the certificate, once exhibited, discharges `k4ul`'s fields directly.
   Both are elementary and need no Farkas — Farkas would only be needed for the
   *converse* (non-existence ⇒ something), which is not wanted here.
2. **Symbolic.** For `n = 2` (`d = 2`) and `n = 3` (`d = 6`), build the NF basis
   of `H_n(q)`, compute `tᵢ = tr_M(bᵢ)` and `Gᵢⱼ = tr_M(bᵢbⱼ)` **symbolically in
   `q`**, not at a pinned `q₀`. Then evaluate the sign condition from step 1.
3. **Instantiate.** If a certificate exists for those `n`, supply it as a
   `OperatorSelectionLpContext` instance — that turns `k4ul` from conditional
   into an unconditional statement about the small cases.

## Why symbolic before numeric

A numeric check at `q₀` cannot distinguish "the certificate exists" from "the
certificate exists at this `q₀`". The proposition is stated for general `q`, and
the sign condition can change across `q`. This corpus has a `q-usage` QA axis
precisely because pinning `q` early hides that.

## Starting points

- `computations/aK_via_lp_dual_hecke_basis.py` + its witness
  `a-K-via-lp-dual-hecke-basis.witness.json` — the closest existing artifact,
  and it is **live**, not deprecated. Read before writing anything new.
- `computations/alpha-k-jones-markov-h3.witness.json`,
  `alpha-k-jones-markov-h4.witness.json` — Markov traces for `H₃`, `H₄`
  already computed. These may already contain `t` for `n = 3, 4`.
- `computations/_deprecated/symbolic-lp.py` — deprecated; check what replaced it
  before reusing.

`pyhecke` is **not importable** in this sandbox as of 2026-08-16, so the Hecke
machinery has to come from the checked-in computations or be rebuilt.

## Not started

No work done beyond scoping. Filed so the next session begins with the
formalization rather than with numerics.
