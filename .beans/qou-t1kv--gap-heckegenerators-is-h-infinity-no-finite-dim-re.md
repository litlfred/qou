---
# qou-t1kv
title: 'GAP: HeckeGenerators is H_infinity — no finite-dim rep can instantiate it, so IsJMWeight cannot be discharged at dim > 1'
status: todo
type: task
priority: normal
created_at: 2026-08-25T10:48:07Z
updated_at: 2026-08-25T10:48:07Z
---

## The defect

`QOU.BraidKnot.Hecke.HeckeGenerators` (HeckeJucysMurphyElements.lean:63) quantifies its
relations over **all** `i : ℕ`:

    hecke : ∀ i, σ i * σ i = algebraMap R A (q - q⁻¹) * σ i + 1
    braid : ∀ i, σ i * σ (i+1) * σ i = σ (i+1) * σ i * σ (i+1)
    far   : ∀ i j, i + 1 < j → σ i * σ j = σ j * σ i

That is the STABLE algebra H_∞(q). H_∞ has no nontrivial finite-dimensional
representations, so **no finite-dimensional rep can be an instance** — and therefore
`IsJMWeight` (HeckeSeminormalWeight.lean) cannot be discharged at `dim V_λ > 1`.

This is why the non-vacuity witness that shipped with #5746 is the ONE-DIMENSIONAL
`scalarGenerators`. That was not a choice of convenience; it is the only shape the class
admits.

## Padding does not work — checked, not assumed

The obvious workaround is to embed H_3 ⊂ H_∞ by padding σ_i for i ≥ 2 with a scalar `s`.
It fails at the boundary. Braid at i = 1 with σ_2 = s:

    LHS = σ_1 · s · σ_1 = s·σ_1²        RHS = s · σ_1 · s = s²·σ_1

so it needs `σ_1² = s·σ_1`. With the Hecke relation `σ_1² = (q−q⁻¹)σ_1 + 1` that becomes
`1 = (s − q + q⁻¹)·σ_1`, i.e. **σ_1 must be a scalar**. False in any rep of dim > 1.
So padding is not merely inelegant; it is inconsistent.

## What is already sitting there unused

`QOU/Archimedean/HeckeH3.lean` has **`stdRep3 : HeckeRep 3 2`** — the (2,1) representation
of H_3(q), dimension 2, with `stdRep3_hecke0`, `stdRep3_hecke1`, `stdRep3_braid` all PROVED
and packaged with `hecke_rel` / `braid_adj` / `braid_far`. It is exactly the multi-dimensional
instance needed, and it cannot be used because of the arity above.

Expected eigenvalues for λ = [2,1] at n = 3 (contents of (0,0),(0,1),(1,0) are 0, 1, −1;
two SYT): `L_0 = 1`; `L_1 = σ_0²` with the two Hecke roots squared, `q²` and `q⁻²`, matching
`q^{2·(+1)}` and `q^{2·(−1)}`. So the check is concrete and falsifiable.

## The fix

A bounded-index variant — relations required only for indices `< n−1`. `jmRaw H k` for
`k < n` touches only `σ_0 … σ_{n−2}`, so every theorem in the chain (`jmRaw_comm`,
`jmProd_eq_delta_pow`, `IsJMWeight`, `fullTwist_smul_eq_theta_sq`) goes through unchanged
on the bounded class. Then `stdRep3` instantiates it directly and the `dim > 1` gap closes
at n = 3 without any seminormal construction.

Estimated small: a class variant plus re-parameterising the existing proofs by the bound.

## Do NOT start a parallel Hecke seminormal form

See bean `sv8b` (priority HIGH) and `QOU/BraidKnot/JucysMurphy.lean` (830 lines, "brick 5
of the Okounkov–Vershik tower"): the corpus already has the CLASSICAL (q = 1) seminormal /
Gelfand–Zetlin construction with Specht modules, SYT adjacent-swap and entry-monotonicity
infrastructure, and three honestly-stubbed `sorry` + `-- Ref:` cores. `sv8b` has a
division of labour agreed on PR #4702. Building a second one from scratch would duplicate
mechanical, settled work — which the AGENTS.md overlap rule permits only for open-outcome
research, not for this.
