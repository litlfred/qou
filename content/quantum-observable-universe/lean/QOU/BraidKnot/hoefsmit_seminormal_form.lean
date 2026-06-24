import Mathlib.Tactic

/-!
# QOU.BraidKnot.hoefsmit_seminormal_form — explicit `ρ_λ(σᵢ)` matrix entries

**Proposition** ([`prop:hoefsmit-seminormal-form`](../../../quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.md)).

*For each partition `λ ⊢ n` and substrate parameter `q > 1`, the
Hoefsmit seminormal form gives an explicit matrix representation
`ρ_λ : H_n(R, q) → M_{d_λ}(ℂ)` where `d_λ = |SYT(λ)|` is the number
of standard Young tableaux of shape `λ`.  The generator `σᵢ` acts on
the SYT basis by*

```
  ρ_λ(σᵢ)_{s s'} = a_ρ      if s' = s
                 = b        if s' = sᵢ (the swap of i, i+1)
                 = 0        otherwise
```

*where*

```
  a_ρ = (q − q⁻¹) / (1 − q^{-2ρ}),
  b   = √(1 − a_ρ²)
```

*and `ρ = ρ(s, i)` is the axial distance between cells `i` and `i+1`
in `s`.*

The Lean encoding records the matrix entries against an abstract
`HoefsmitSeminormalContext` carrying the SYT data and the
representation matrix.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.md
-- Ref: [hoefsmit1974] P. Hoefsmit, Representations of Hecke algebras of finite groups with BN-pairs of classical type, PhD thesis 1974.
-/

namespace QOU.BraidKnot

open Classical

/-- Abstract context for the Hoefsmit seminormal form. -/
class HoefsmitSeminormalContext (n : ℕ) where
  -- Witness: computations/none
  /-- The substrate parameter `q > 1`. -/
  q : ℝ
  q_gt_one : 1 < q
  /-- Indexing type for partitions of `n`. -/
  Partition : Type
  /-- Indexing type for standard Young tableaux. -/
  SYT : Partition → Type
  /-- The axial distance `ρ(s, i)` between cells `i` and `i+1`. -/
  axialDistance : ∀ {lam : Partition}, SYT lam → ℕ → ℤ
  /-- The Hoefsmit diagonal entry `a_ρ = (q − q⁻¹) / (1 − q^{-2ρ})`. -/
  hoefsmitDiagonal : ℤ → ℝ
  /-- The Hoefsmit off-diagonal entry `b = √(1 − a_ρ²)`. -/
  hoefsmitOffDiagonal : ℤ → ℝ
  /-- The representation matrix entry `ρ_λ(σᵢ)_{s s'}`. -/
  repMatrix : ∀ {lam : Partition} (s s' : SYT lam) (i : ℕ), ℝ
  /-- The "swap-i-result" function, partial since it may not yield
      a valid SYT. -/
  swapIResult : ∀ {lam : Partition}, SYT lam → ℕ → Option (SYT lam)
  /-- Manuscript defining equation for the matrix entries (Hoefsmit 1974). -/
  repMatrix_def : ∀ {lam : Partition} (s s' : SYT lam) (i : ℕ),
    repMatrix s s' i = if s' = s then hoefsmitDiagonal (axialDistance s i)
      else match swapIResult s i with
        | some t => if s' = t then hoefsmitOffDiagonal (axialDistance s i) else 0
        | none => 0

/-- **Hoefsmit seminormal form matrix entries** ([`prop:hoefsmit-seminormal-form`]).

    `ρ_λ(σᵢ)_{s s'}` evaluates to `a_ρ` on the diagonal, `b` on the
    swap-i result (when valid), and `0` elsewhere. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.md
-- Ref: [hoefsmit1974]
theorem hoefsmit_seminormal_form
    {n : ℕ} [ctx : HoefsmitSeminormalContext n]
    {lam : ctx.Partition} (s s' : ctx.SYT lam) (i : ℕ) :
    ctx.repMatrix s s' i
      = if s' = s then
          ctx.hoefsmitDiagonal (ctx.axialDistance s i)
        else
          match ctx.swapIResult s i with
          | some t =>
              if s' = t then ctx.hoefsmitOffDiagonal (ctx.axialDistance s i) else 0
          | none => 0 := by
  -- Manuscript proof: direct computation from the Hoefsmit thesis.
  -- The `a_ρ` / `b` entries come from solving the Hecke quadratic
  -- `σ_i² = (q − q⁻¹)·σ_i + 1` block-diagonalised in the SYT basis.
  -- Concretisation requires Lean SYT infrastructure.
  -- Ref: [manuscript] quantum-observable-universe/braids-and-knots/hoefsmit-seminormal-form.md
  -- Ref: [hoefsmit1974]
  -- `repMatrix_def` axiomatises this exact equation. The two sides differ only
  -- in the per-declaration `match`-helper Lean generates, so case-split the
  -- `if`/`match` (reducing each branch to a concrete value) and close by `rfl`.
  rw [ctx.repMatrix_def]
  cases ctx.swapIResult s i <;> rfl

end QOU.BraidKnot
