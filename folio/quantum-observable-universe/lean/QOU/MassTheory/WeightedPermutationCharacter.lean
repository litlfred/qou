import Mathlib.Tactic
import QOU.MassTheory.OrbitQuotientCount

/-!
# The `q`-deformed permutation character: one `q`-factor per orbit

Bean `qou-uyb4`. Continues the `q = 1` arc (`qou-uinl`, `qou-mex9`) into `q ≠ 1`.

## 🛑 Read this first: WHICH `q ≠ 1` this is

"Quantum Schur–Weyl" is **two independent deformations** of the classical picture, and
this file does exactly one of them.

| deformation | what changes | status |
|---|---|---|
| **trace weight** | the flat trace becomes the `K`-weighted (quantum) trace, `K = diag(1, q²)^{⊗n}` | **proved here** |
| **braiding** | the permutation operator `P_σ` becomes the R-matrix `Ř(q)`, and `H_n(q)` replaces `S_n` | **NOT here** |

Full quantum Schur–Weyl — the `U_q(gl_N) × H_n(q)` double centralizer — needs both,
and bean `qou-mpq5` scoped it as a multi-week build. **That assessment stands.**
Measured 2026-09-05, Mathlib has **zero** files matching `QuantumGroup`,
`HeckeAlgebra`, `BraidGroup`, `RMatrix`, `YangBaxter` or `TemperleyLieb` — only
Coxeter groups — so the braiding half is a from-scratch development, not a gap that
can be closed by finding the right lemma.

**Do not cite this file as quantum Schur–Weyl.** It is the weighted character of the
*permutation* action; the braiding is untouched.

## What is proved

    ∑_{f invariant} ∏ᵢ w (f i)  =  ∏_{orbits O} ∑_k w(k) ^ |O|

`weighted_permutation_character`. The deformation lives **entirely in the orbit
sizes**, which the `q = 1` count discards — that is the whole content, and it is why
the undeformed statement could get away with counting orbits rather than measuring
them.

Three checks pin it down:

* `sum_orbitSize` — orbit sizes sum to `card α` (the orbits really do partition).
* `weighted_permutation_character_one` — at `w ≡ 1` the product collapses to
  `(card κ) ^ orbitCount σ`, **the character proved in `OrbitQuotientCount`**. This is
  the check that matters: the deformation is not a new object, it is the same
  character with the sizes retained.
* `weighted_character_two` — at `κ = Fin 2` with `K = diag(1, q²)`, the weight the
  corpus's own Schur–Weyl normalisation uses, the character is

      ∏_{orbits O} (1 + q^{2|O|})

  one `q`-binomial per orbit. At `q = 1` each factor is `2` and this is `2^{c(σ)}`.

-- Ref: [leitner2026] bean qou-uyb4; the weighted permutation character on a tensor
-- power is classical, and the per-orbit product is its standard form.
-/

open Equiv Equiv.Perm Finset

namespace QOU.MassTheory

variable {α : Type*} [Fintype α] [DecidableEq α]
variable {κ : Type*} [Fintype κ] [DecidableEq κ]

/-- The size of an orbit of `σ`. -/
noncomputable def orbitSize (σ : Perm α) (O : Quotient (SameCycle.setoid σ)) : ℕ := by
  classical
  exact #(univ.filter fun i : α => (⟦i⟧ : Quotient (SameCycle.setoid σ)) = O)

/-- Invariant functions are exactly functions on the orbit set. -/
def invariantEquivOrbit (σ : Perm α) (κ : Type*) :
    {f : α → κ // ∀ x, f (σ x) = f x} ≃ (Quotient (SameCycle.setoid σ) → κ) where
  toFun f := Quotient.lift f.1 (fun _ _ h => eq_of_sameCycle_of_invariant f.2 h)
  invFun g := ⟨fun x => g ⟦x⟧, fun x => congrArg g (Quotient.sound ⟨-1, by simp⟩)⟩
  left_inv _ := rfl
  right_inv g := funext (Quotient.ind fun _ => rfl)

variable {R : Type*} [CommRing R]

omit [DecidableEq α] [Fintype κ] [DecidableEq κ] in
/-- A weight assigned per tensor slot factors over the orbits: an invariant `f` is
constant on each orbit, so its slot-weights collect into one power per orbit. -/
theorem prod_weight_eq_prod_orbits (σ : Perm α) (w : κ → R)
    (f : {f : α → κ // ∀ x, f (σ x) = f x}) :
    (∏ i, w (f.1 i)) = ∏ O, w (invariantEquivOrbit σ κ f O) ^ orbitSize σ O := by
  classical
  rw [← Finset.prod_fiberwise univ (fun i : α => (⟦i⟧ : Quotient (SameCycle.setoid σ)))
        (fun i => w (f.1 i))]
  refine Finset.prod_congr rfl fun O _ => ?_
  rw [orbitSize, ← Finset.prod_const]
  refine Finset.prod_congr rfl fun i hi => ?_
  have : (⟦i⟧ : Quotient (SameCycle.setoid σ)) = O := (Finset.mem_filter.mp hi).2
  rw [← this]
  rfl

/-- **The `q`-deformed permutation character.** With a weight `w` on the fibre basis,
the weighted trace of `σ` permuting the factors of `V^{⊗α}` is a product of one factor
per **orbit**, each factor a weight-sum raised to that orbit's size:

    ∑_{f invariant} ∏ᵢ w (f i)  =  ∏_{orbits O} ∑_k w(k) ^ |O|

At `w ≡ 1` every factor is `card κ` and this collapses to `(card κ)^{orbitCount σ}` —
the `q = 1` character. The deformation lives entirely in the orbit SIZES, which the
undeformed count discards. -/
theorem weighted_permutation_character (σ : Perm α) (w : κ → R) :
    (∑ f : {f : α → κ // ∀ x, f (σ x) = f x}, ∏ i, w (f.1 i))
      = ∏ O : Quotient (SameCycle.setoid σ), ∑ k : κ, w k ^ orbitSize σ O := by
  classical
  rw [Fintype.prod_sum (fun O (k : κ) => w k ^ orbitSize σ O),
    ← Equiv.sum_comp (invariantEquivOrbit σ κ) (fun g => ∏ O, w (g O) ^ orbitSize σ O)]
  exact Finset.sum_congr rfl fun f _ => prod_weight_eq_prod_orbits σ w f

/-! ### Consistency with the `q = 1` character, and the physical weight -/

omit [DecidableEq α] in
/-- **The orbits partition the slots.** Structural sanity: orbit sizes sum to `card α`. -/
theorem sum_orbitSize (σ : Perm α) :
    (∑ O : Quotient (SameCycle.setoid σ), orbitSize σ O) = Fintype.card α := by
  classical
  simp only [orbitSize]
  rw [← Finset.card_eq_sum_card_fiberwise
    (f := fun i : α => (⟦i⟧ : Quotient (SameCycle.setoid σ))) (fun i _ => mem_univ _)]
  simp

omit [DecidableEq κ] in
/-- **The undeformed limit.** At `w ≡ 1` every orbit factor is `card κ`, and the
`q`-deformed character collapses to `(card κ) ^ orbitCount σ` — the character proved in
`OrbitQuotientCount`.

This is the check that the deformation is the RIGHT one: it is not a new object, it is
the same character with the orbit SIZES retained instead of discarded. -/
theorem weighted_permutation_character_one (σ : Perm α) :
    (∏ O : Quotient (SameCycle.setoid σ), ∑ _k : κ, (1 : R) ^ orbitSize σ O)
      = (Fintype.card κ : R) ^ orbitCount σ := by
  classical
  simp only [one_pow, Finset.sum_const, Finset.card_univ, nsmul_eq_mul, mul_one]
  rw [Finset.prod_const, Finset.card_univ, card_quotient_sameCycle]

/-- **The physical weight.** With the fibre `κ = Fin 2` carrying `K = diag(1, q²)` —
the weight the corpus's Schur–Weyl normalisation uses — the character is

    ∏_{orbits O} (1 + q^{2|O|})

a product of one `q`-binomial per orbit, indexed by orbit size. At `q = 1` each factor
is `2` and this is `2^{c(σ)}`. -/
theorem weighted_character_two (σ : Perm α) (q : R) :
    (∑ f : {f : α → Fin 2 // ∀ x, f (σ x) = f x},
        ∏ i, (![1, q ^ 2] : Fin 2 → R) (f.1 i))
      = ∏ O : Quotient (SameCycle.setoid σ), (1 + q ^ (2 * orbitSize σ O)) := by
  rw [weighted_permutation_character]
  refine Finset.prod_congr rfl fun O _ => ?_
  simp [Fin.sum_univ_two, pow_mul]

end QOU.MassTheory
