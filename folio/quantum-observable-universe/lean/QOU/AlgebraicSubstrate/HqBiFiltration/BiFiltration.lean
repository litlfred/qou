import Mathlib.Tactic

/-!
# QOU.AlgebraicSubstrate.HqBiFiltration.BiFiltration

**Canonical declaration** for content block at
[`quantum-observable-universe/mass-theory/hq-bi-filtration.ts`](quantum-observable-universe/mass-theory/hq-bi-filtration.ts).

Formalises the manuscript **definition** of the knot-indexed bi-filtration:
for a depth filtration `G^(0) ⊆ G^(1) ⊆ ⋯` on the substrate convolution
algebra and a central primitive idempotent `e = e_{λ_K}`, the
knot-`K`-localised depth-`n` stratum is
`H_q^{(n,K)} = { α ∈ G^(n) : e·α·e = α }`. Pure algebra over a generic ring
(§7c-clean).
-/

namespace QOU.AlgebraicSubstrate.HqBiFiltration

/-- Data for the bi-filtration on a ring `A`.

    A `definition` carrier: the idempotent `e = e_{λ_K}` (`e² = e`), and the
    depth filtration `G : ℕ → Set A` (monotone, the horizontal Goncharov
    axis). -/
structure BiFiltration (A : Type*) [Ring A] where
  /-- The central primitive idempotent `e_{λ_K}`. -/
  e : A
  /-- `e` is idempotent. -/
  e_idem : e * e = e
  /-- The iterated-integral depth filtration `G^(n)`. -/
  G : ℕ → Set A
  /-- The filtration is monotone: `G^(n) ⊆ G^(n+1)`. -/
  G_mono : ∀ n, G n ⊆ G (n + 1)

namespace BiFiltration

variable {A : Type*} [Ring A] (F : BiFiltration A)

/-- The knot-`K` projector `p(α) = e·α·e`. -/
def proj (α : A) : A := F.e * α * F.e

/-- The knot-`K`-localised depth-`n` stratum
    `H_q^{(n,K)} = { α ∈ G^(n) : e·α·e = α }`. -/
def stratum (n : ℕ) : Set A := {α | α ∈ F.G n ∧ F.proj α = α}

/-- `e` absorbs on the left of a projected element. -/
theorem e_mul_proj (α : A) : F.e * F.proj α = F.proj α := by
  unfold proj; rw [← mul_assoc, ← mul_assoc, F.e_idem]

/-- `e` absorbs on the right of a projected element. -/
theorem proj_mul_e (α : A) : F.proj α * F.e = F.proj α := by
  unfold proj; rw [mul_assoc, F.e_idem]

/-- The projector is idempotent: `p(p(α)) = p(α)` (from `e² = e`). -/
theorem proj_idem (α : A) : F.proj (F.proj α) = F.proj α := by
  calc F.proj (F.proj α) = F.e * F.proj α * F.e := rfl
    _ = F.proj α * F.e := by rw [F.e_mul_proj]
    _ = F.proj α := F.proj_mul_e α

/-- `α` lies in some stratum iff it is in the corresponding depth level and is
    `e`-fixed. -/
theorem mem_stratum {n : ℕ} {α : A} :
    α ∈ F.stratum n ↔ α ∈ F.G n ∧ F.proj α = α := Iff.rfl

/-- The stratum is closed under addition (an additive subgroup of `G^(n)`
    modulo the filtration): if `α, β` are both `e`-fixed then so is `α + β`. -/
theorem proj_add_fixed {α β : A} (hα : F.proj α = α) (hβ : F.proj β = β) :
    F.proj (α + β) = α + β := by
  unfold proj at hα hβ ⊢
  rw [mul_add, add_mul, hα, hβ]

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/hq-bi-filtration.ts

end BiFiltration

end QOU.AlgebraicSubstrate.HqBiFiltration
