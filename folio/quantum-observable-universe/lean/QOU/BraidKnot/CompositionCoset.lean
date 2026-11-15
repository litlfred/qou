import QOU.BraidKnot.CompositionMinimal

/-!
# Mathas' `D_μ` is a transversal — the uniqueness half of Proposition 3.3

> `D_μ = { d ∈ S_n | t^μ d is row standard }`.  Then `D_μ` is a **complete set of right
> coset representatives** of `S_μ` in `S_n`.  Moreover, if `w ∈ S_μ` and `d ∈ D_μ` then
> `ℓ(wd) = ℓ(w) + ℓ(d)` and `T_{wd} = T_w T_d`.  *(Mathas, Proposition 3.3)*

`CompositionMinimal.length_mul_eq_add_of_isDistinguished` is the length half.  This
file is the **uniqueness** half: a right coset of `S_μ` contains **at most one**
distinguished element.

## The proof is the length half, applied twice

If `d₁` and `d₂` are both distinguished and lie in one coset, then `d₂ = v · d₁` with
`v ∈ S_μ`, and also `d₁ = v⁻¹ · d₂` with `v⁻¹ ∈ S_μ`.  Length additivity applies to
each, so

    ℓ(d₂) = ℓ(v) + ℓ(d₁)   and   ℓ(d₁) = ℓ(v⁻¹) + ℓ(d₂),

and adding them forces `ℓ(v) + ℓ(v⁻¹) = 0`.  Since `ℓ(v⁻¹) = ℓ(v)`, that gives
`ℓ(v) = 0`, hence `v = 1`.

No exchange condition, no reflection cocycle, no `IsReduced` residue — it is two
applications of a lemma this arc already proved by inversion sets.

## What is still open

**Existence** — that every coset contains a distinguished element.  That is the other
half of Prop 3.3 and is not proved here; the natural route is that the minimal-length
element of a coset must be distinguished (a non-distinguished `d` admits a same-block
transposition `v ∈ S_μ` with `ℓ(v·d) < ℓ(d)`), which is an inversion-count argument
rather than a corollary of the above.
-/

namespace QOU.BraidKnot.CompositionCoset

open QOU.BraidKnot.CompositionYoung QOU.BraidKnot.CompositionMinimal
open QOU.Hecke.SymmetricCoxeter Equiv

variable {n : ℕ}

/-- **Uniqueness in Proposition 3.3**: a right coset of `S_μ` contains at most one
distinguished element.

Stated with the coset condition as `d₂ * d₁⁻¹ ∈ S_μ`, which is membership of `d₂` in
the right coset `S_μ d₁`. -/
theorem isDistinguished_unique {c : Composition (n + 1)} {d₁ d₂ : Perm (Fin (n + 1))}
    (h₁ : IsDistinguished c d₁) (h₂ : IsDistinguished c d₂)
    (hcoset : d₂ * d₁⁻¹ ∈ youngOfComp c) : d₁ = d₂ := by
  set v := d₂ * d₁⁻¹ with hv
  have hvd₁ : v * d₁ = d₂ := by rw [hv]; group
  have hv'd₂ : v⁻¹ * d₂ = d₁ := by rw [← hvd₁]; group
  -- length additivity in both directions
  have e₁ : (permCoxeterSystem n).length d₂
      = (permCoxeterSystem n).length v + (permCoxeterSystem n).length d₁ := by
    rw [← hvd₁]; exact length_mul_eq_add_of_isDistinguished h₁ hcoset
  have e₂ : (permCoxeterSystem n).length d₁
      = (permCoxeterSystem n).length v⁻¹ + (permCoxeterSystem n).length d₂ := by
    rw [← hv'd₂]
    exact length_mul_eq_add_of_isDistinguished h₂ (inv_mem hcoset)
  -- adding them forces `ℓ(v) = 0`
  have hlen : (permCoxeterSystem n).length v = 0 := by
    have hinv := (permCoxeterSystem n).length_inv v
    omega
  have : v = 1 := ((permCoxeterSystem n).length_eq_zero_iff).mp hlen
  rw [this, one_mul] at hvd₁
  exact hvd₁

/-- The same, phrased as injectivity of `d ↦ S_μ d` on the distinguished elements. -/
theorem isDistinguished_eq_of_mul_inv_mem {c : Composition (n + 1)}
    {d₁ d₂ : Perm (Fin (n + 1))} (h₁ : IsDistinguished c d₁) (h₂ : IsDistinguished c d₂)
    (h : ∃ v ∈ youngOfComp c, d₂ = v * d₁) : d₁ = d₂ := by
  obtain ⟨v, hv, rfl⟩ := h
  refine isDistinguished_unique h₁ h₂ ?_
  simpa using hv

end QOU.BraidKnot.CompositionCoset
