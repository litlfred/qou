/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.FormalGroups.Cartier

/-!
# Thm. 3.7 of arXiv:math/0602138, given the PBW basis

The proof of Thm. 3.7 of F. Leitner, arXiv:math/0602138, has two parts.

1. **PBW** (Thm. 1.9): the ordered monomials `δx^J = δx₁^{J₁} ⋯ δxₙ^{Jₙ}` form a basis of
   `U = T / J`.
2. **The coproduct on that basis**: each `δxⱼ^{(m)}` lies in the distribution algebra of a
   commutative formal subgroup, so `Δ(δxⱼ^{(m)}) = Σ_{a+b=m} δxⱼ^{(a)} ⊗ δxⱼ^{(b)}`. Since `Δ` is
   an algebra map (Prop. 1.13, `CoproductDescent.lean`) it follows that
   `Δ(δx^J) = Σ_{A+B=J} δx^A ⊗ δx^B`, and Cartier's theorem (`Cartier.lean`) gives a formal
   group law whose distribution algebra is `U`.

This file proves part 2. Part 1 enters as a hypothesis: a basis `b` of `U` with
`b J = δx^J`. That is the PBW statement exactly, and nothing else is assumed. The result is
`formalGroupLaw_of_pbw`: if the ordered monomials are a basis, `U` is the distribution algebra
of a formal group law, with its product given by convolution.

The coordinates are ordered by a list `l` that lists each coordinate once (`l.Nodup` and
`∀ j, j ∈ l`); `δx^J` is the product in the order of `l`.

-- Ref: [leitner2006] F. Leitner, arXiv:math/0602138, Thm. 3.7 (proof) and Thm. 1.9.
-/

namespace QOU.FormalGroups

open TensorProduct

noncomputable section

variable {R : Type*} [CommRing R] {ι : Type*} [DecidableEq ι]
  {U : Type*} [Ring U] [Bialgebra R U]

/-- The ordered monomial `δx^J := ∏_{j ∈ l} e j (J j)`, the product taken in the order of
`l`. -/
def orderedMono (e : ι → ℕ → U) (l : List ι) (J : ι →₀ ℕ) : U :=
  (l.map fun j => e j (J j)).prod

theorem orderedMono_nil (e : ι → ℕ → U) (J : ι →₀ ℕ) : orderedMono e [] J = 1 := rfl

theorem orderedMono_cons (e : ι → ℕ → U) (j : ι) (l : List ι) (J : ι →₀ ℕ) :
    orderedMono e (j :: l) J = e j (J j) * orderedMono e l J := by
  simp [orderedMono]

/-- `δx^J` reads only the coordinates in `l`. -/
theorem orderedMono_congr (e : ι → ℕ → U) (l : List ι) {J J' : ι →₀ ℕ}
    (h : ∀ x ∈ l, J x = J' x) : orderedMono e l J = orderedMono e l J' := by
  unfold orderedMono
  congr 1
  exact List.map_congr_left fun x hx => by rw [h x hx]

theorem orderedMono_zero (e : ι → ℕ → U) (he0 : ∀ j, e j 0 = 1) (l : List ι) :
    orderedMono e l 0 = 1 := by
  induction l with
  | nil => rfl
  | cons j l ih => rw [orderedMono_cons, Finsupp.zero_apply, he0, ih, one_mul]

section Coproduct

variable (e : ι → ℕ → U)
  (heΔ : ∀ j m, Coalgebra.comul (R := R) (e j m) =
    ∑ p ∈ Finset.antidiagonal m, e j p.1 ⊗ₜ[R] e j p.2)

/-- The splitting of an antidiagonal at one coordinate: pairs `(q₁, q₂)` with `q₁ + q₂ = J`
correspond to a split of `J j` together with a split of `J.erase j`. -/
theorem sum_antidiagonal_split {M : Type*} [AddCommMonoid M] (j : ι) (J : ι →₀ ℕ)
    (f : (ι →₀ ℕ) × (ι →₀ ℕ) → M) :
    ∑ q ∈ Finset.antidiagonal J, f q =
      ∑ x ∈ Finset.antidiagonal (J j) ×ˢ Finset.antidiagonal (J.erase j),
        f (Finsupp.single j x.1.1 + x.2.1, Finsupp.single j x.1.2 + x.2.2) := by
  symm
  refine Finset.sum_nbij' (fun x => (Finsupp.single j x.1.1 + x.2.1,
      Finsupp.single j x.1.2 + x.2.2))
    (fun q => ((q.1 j, q.2 j), (q.1.erase j, q.2.erase j))) ?_ ?_ ?_ ?_ ?_
  · rintro ⟨⟨a, b⟩, p₁, p₂⟩ hx
    simp only [Finset.mem_product, Finset.mem_antidiagonal] at hx ⊢
    obtain ⟨hab, hp⟩ := hx
    ext x
    by_cases hx : x = j
    · subst hx
      have := congrArg (fun F => F x) hp
      simp only [Finsupp.add_apply, Finsupp.erase_same] at this
      simp [Finsupp.single_apply, ← hab, this]
      omega
    · have := congrArg (fun F => F x) hp
      simp only [Finsupp.add_apply, Finsupp.erase_ne hx] at this
      simp [Finsupp.single_apply, Ne.symm hx, this]
  · rintro ⟨q₁, q₂⟩ hq
    simp only [Finset.mem_product, Finset.mem_antidiagonal] at hq ⊢
    refine ⟨by rw [← hq]; rfl, ?_⟩
    rw [← hq]; ext x
    by_cases hx : x = j
    · subst hx; simp
    · simp [Finsupp.erase_ne hx]
  · rintro ⟨⟨a, b⟩, p₁, p₂⟩ hx
    simp only [Finset.mem_product, Finset.mem_antidiagonal] at hx
    obtain ⟨hab, hp⟩ := hx
    have h1 : p₁ j = 0 := by
      have := congrArg (fun F => F j) hp
      simp only [Finsupp.add_apply, Finsupp.erase_same] at this; omega
    have h2 : p₂ j = 0 := by
      have := congrArg (fun F => F j) hp
      simp only [Finsupp.add_apply, Finsupp.erase_same] at this; omega
    simp only [Finsupp.add_apply, Finsupp.single_eq_same, h1, h2, add_zero, Prod.mk.injEq,
      true_and]
    constructor <;> ext x <;> by_cases hx : x = j
    · subst hx; simp [h1]
    · simp [Finsupp.erase_ne hx, Finsupp.single_apply, Ne.symm hx]
    · subst hx; simp [h2]
    · simp [Finsupp.erase_ne hx, Finsupp.single_apply, Ne.symm hx]
  · rintro ⟨q₁, q₂⟩ _
    simp only [Prod.mk.injEq]
    constructor <;> ext x <;> by_cases hx : x = j
    · subst hx; simp
    · simp [Finsupp.erase_ne hx, Finsupp.single_apply, Ne.symm hx]
    · subst hx; simp
    · simp [Finsupp.erase_ne hx, Finsupp.single_apply, Ne.symm hx]
  · intros; rfl

include heΔ in
/-- **The coproduct of an ordered monomial** (proof of Thm. 3.7): for `J` supported on `l`,
`Δ(δx^J) = Σ_{A+B=J} δx^A ⊗ δx^B`. -/
theorem comul_orderedMono (l : List ι) (hl : l.Nodup) (J : ι →₀ ℕ)
    (hJ : ∀ x, x ∉ l → J x = 0) :
    Coalgebra.comul (R := R) (orderedMono e l J) =
      ∑ p ∈ Finset.antidiagonal J, orderedMono e l p.1 ⊗ₜ[R] orderedMono e l p.2 := by
  induction l generalizing J with
  | nil =>
    have hJ0 : J = 0 := by ext x; exact hJ x (List.not_mem_nil)
    subst hJ0
    rw [Finset.antidiagonal_zero, Finset.sum_singleton]
    show Coalgebra.comul (R := R) (1 : U) = (1 : U) ⊗ₜ[R] (1 : U)
    rw [Bialgebra.comul_one]; rfl
  | cons j l ih =>
    have hjl : j ∉ l := (List.nodup_cons.1 hl).1
    have hJ' : ∀ x, x ∉ l → J.erase j x = 0 := by
      intro x hx
      by_cases hxj : x = j
      · subst hxj; simp
      · rw [Finsupp.erase_ne hxj]; exact hJ x (by simp [hxj, hx])
    have hrest : orderedMono e l J = orderedMono e l (J.erase j) :=
      orderedMono_congr e l fun x hx => by
        rw [Finsupp.erase_ne (fun h => hjl (by rw [← h]; exact hx))]
    rw [orderedMono_cons, Bialgebra.comul_mul, heΔ, hrest, ih (List.nodup_cons.1 hl).2 _ hJ',
      Finset.sum_mul_sum, ← Finset.sum_product', sum_antidiagonal_split j J]
    refine Finset.sum_congr rfl fun x hx => ?_
    simp only [Finset.mem_product, Finset.mem_antidiagonal] at hx
    have hp : ∀ (a : ℕ) (p : ι →₀ ℕ), p j = 0 →
        orderedMono e (j :: l) (Finsupp.single j a + p) = e j a * orderedMono e l p := by
      intro a p hpj
      rw [orderedMono_cons]
      simp only [Finsupp.add_apply, Finsupp.single_eq_same, hpj, add_zero]
      congr 1
      exact orderedMono_congr e l fun y hy => by
        rw [Finsupp.add_apply, Finsupp.single_eq_of_ne (fun h => hjl (by rw [← h]; exact hy)), zero_add]
    have h1 : x.2.1 j = 0 := by
      have := congrArg (fun F => F j) hx.2
      simp only [Finsupp.add_apply, Finsupp.erase_same] at this; omega
    have h2 : x.2.2 j = 0 := by
      have := congrArg (fun F => F j) hx.2
      simp only [Finsupp.add_apply, Finsupp.erase_same] at this; omega
    rw [hp _ _ h1, hp _ _ h2, Algebra.TensorProduct.tmul_mul_tmul]

end Coproduct

/-- **Thm. 3.7 of arXiv:math/0602138, given PBW (Thm. 1.9).** Let `U` be a bialgebra and
`e j m` (`m ≥ 0`) elements with `e j 0 = 1` and
`Δ(e j m) = Σ_{a+b=m} e j a ⊗ e j b` (the divided powers of the coordinate `xⱼ` in the
distribution algebra of its commutative formal subgroup). If the ordered monomials
`δx^J = ∏_{j ∈ l} e j (J j)` form a basis `b` of `U`, then `U` is the distribution algebra of a
formal group law `G`: `b.repr` turns the product of `U` into the convolution of `G`. -/
theorem formalGroupLaw_of_pbw [Finite ι] (e : ι → ℕ → U) (he0 : ∀ j, e j 0 = 1)
    (heΔ : ∀ j m, Coalgebra.comul (R := R) (e j m) =
      ∑ p ∈ Finset.antidiagonal m, e j p.1 ⊗ₜ[R] e j p.2)
    (l : List ι) (hl : l.Nodup) (hall : ∀ j, j ∈ l)
    (b : Module.Basis (ι →₀ ℕ) R U) (hb : ∀ J, b J = orderedMono e l J) :
    ∃ G : FormalGroupLaw R ι, G.F = cartierF b ∧
      (∀ u v : U, b.repr (u * v) = conv G (b.repr u) (b.repr v)) ∧ b.repr 1 = one := by
  refine cartier b (fun J => ?_) ?_
  · rw [hb, comul_orderedMono e heΔ l hl J (fun x hx => absurd (hall x) hx)]
    simp only [hb]
  · rw [hb, orderedMono_zero e he0]

end

end QOU.FormalGroups
