import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Ring.GeomSum
import Mathlib.Tactic

/-!
# QOU.BraidKnot.EigenbasisStructuralLemmas — content/twist eigenbasis lemmas

Lean formalization of the structural lemmas of the **content/twist
eigenbasis**, verified exact-symbolic in
`computations/probes/eigenbasis_structural_lemmas_probe.py` (PR #2502) and
flagged there for Lean follow-up (`lean_followup`).

The eigenbasis is organized by the **ribbon-twist eigenvalue**
`θ_λ = q^{2c(λ)}`: the full twist `Δ² ∈ Z(H_n(q))` acts on the Wedderburn
channel `V_λ` by the scalar `θ_λ`, formalized as the class
[`QOU.BraidKnot.ChiralityWritheRibbon.RibbonTwistEigenvalue`].  This file
proves the lemmas **sorry-free** over `ℝ` importing only Mathlib; the
connection of the abstract framing ratio `θ` to the categorical
`q^{2κ_λ}` is `framing_eigenvalue_pow` below.

## Lemmas

- **L3 — framing generating function** (this file): the framing tower
  `Σ_m t^m χ_λ(β·Δ^{2m})` is the single-pole rational `χ_λ(β)/(1 − t·θ_λ)`.

LaTeX / witness: probe `eigenbasis-structural-lemmas`, lemma L3.

## References

- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [jones1987] https://doi.org/10.2307/1971403
- [manuscript] braids-and-knots / eigenbasis structural lemmas (PR #2502)
-/

namespace QOU.BraidKnot.EigenbasisStructuralLemmas

open Finset

/-! ## L3 — framing generating function -/

/-- **Ribbon power law.**  The eigenvalue of the `m`-fold full twist
`Δ^{2m}` on the channel `V_λ` is the `m`-th power of the single-twist
eigenvalue `θ_λ = q^{2κ_λ}`:

  `q^{2mκ} = (q^{2κ})^m`.

This is the algebraic content linking the `m`-fold framing to the ribbon
eigenvalue; it holds for every real base (the `zpow` identity is valid in a
`GroupWithZero`). -/
theorem framing_eigenvalue_pow (q : ℝ) (κ : ℤ) (m : ℕ) :
    q ^ (2 * (m : ℤ) * κ) = (q ^ (2 * κ)) ^ m := by
  rw [show 2 * (m : ℤ) * κ = (2 * κ) * (m : ℤ) by ring, zpow_mul, zpow_natCast]

/-- **L3 — framing generating function (finite closed form).**

Let `c m = χ_λ(β · Δ^{2m})` be the Hecke character of the braid `β` framed
by `m` full twists, in Wedderburn channel `λ`.  Centrality of the full
twist `Δ² ∈ Z(H_n(q))` together with the ribbon eigenvalue
`Δ²|_{V_λ} = θ` (`θ = q^{2c(λ)}`, `framing_eigenvalue_pow`) gives the
one-step scaling `c (m+1) = θ · c m`.  Then the framing generating function
is the **single-pole rational** `c 0 / (1 − t·θ)`: the partial sums satisfy
the finite geometric closed form

  `(1 − t·θ) · Σ_{m<N} t^m · c m = c 0 · (1 − (t·θ)^N)`,

so the only pole is at `t = θ⁻¹ = q^{−2c(λ)}`.  The result is **not**
vacuous: it pins the framing tower as geometric with ratio `t·θ` and
leading coefficient `c 0`, which is the substance of the eigenbasis
reframing (the framing tower separates orders by content). -/
theorem framing_gf_closed_form
    (θ t : ℝ) (c : ℕ → ℝ)
    (hstep : ∀ m, c (m + 1) = θ * c m) (N : ℕ) :
    (1 - t * θ) * (∑ m ∈ range N, t ^ m * c m) = c 0 * (1 - (t * θ) ^ N) := by
  -- The framed characters form a geometric sequence `c m = θ^m · c 0`.
  have hcm : ∀ m, c m = θ ^ m * c 0 := by
    intro m
    induction m with
    | zero => simp
    | succ k ih => rw [hstep, ih]; ring
  -- Pull `c 0` out and collapse `t^m · θ^m = (t·θ)^m`.
  have hsum : (∑ m ∈ range N, t ^ m * c m) = c 0 * ∑ m ∈ range N, (t * θ) ^ m := by
    rw [mul_sum]
    refine sum_congr rfl (fun m _ => ?_)
    rw [hcm, mul_pow]; ring
  -- Geometric-series closed form `(1 − x)·Σ x^m = 1 − x^N` with `x = t·θ`.
  have hgeom : (1 - t * θ) * (∑ m ∈ range N, (t * θ) ^ m) = 1 - (t * θ) ^ N := by
    linear_combination - geom_sum_mul (t * θ) N
  rw [hsum, ← mul_assoc, mul_comm (1 - t * θ) (c 0), mul_assoc, hgeom]

end QOU.BraidKnot.EigenbasisStructuralLemmas
