import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# QOU.StandardModel.OddStrandsForceChirality — odd strand count is the same as chiral matter

`OddExteriorAnomalyFreedom.lean` takes matter to be the even part
`Λ⁰ ⊕ Λ² ⊕ Λ⁴ …` of `n = 5` strands, and uses that `n` is odd. This module shows
that oddness is not a separate input: it is equivalent to the matter part being
chiral.

Label a state of `n` strands by the subset `S ⊆ Fin n` it carries. Its conjugate is the
complement `Sᶜ`, which carries charge `-y_S` for any traceless diagonal charge `y`.

* `even_card_compl_iff` — `|Sᶜ|` is even iff `|S|` and `n` have the same parity.
* `evenPart_dichotomy` — **either every matter state's conjugate is matter (n even), or
  none is (n odd).** There is no mixed case.
* `evenPart_image_compl_eq_iff` — the matter part is closed under conjugation exactly
  when `n` is even.
* `evenPart_vectorlike_of_even` — for `n` even every function of the charges summed over
  matter is unchanged by `y ↦ -y`: every odd moment (in particular the cubic anomaly)
  vanishes identically, without cancellation. That is the vector-like case.

So "matter is chiral" (no matter state has its conjugate in matter) is equivalent to
"the strand count is odd". Chirality is the observed input; oddness follows.

What this does not settle: why chirality, i.e. why the matter part is the even part and
not the odd part (the sign, bean `qou-h0zz`), and why `n = 5` rather than another odd
number. Note that a single `U(1)` charge (e.g. electric charge) can still have a
symmetric spectrum on chiral matter; chirality here is at the level of states (weights),
not of one charge.

Base ring: any commutative ring `K`; no empirical input.
-/

namespace QOU.StandardModel.OddStrands

open Finset

variable {n : ℕ}

/-- The even part of the exterior algebra on `n` strands (matter). -/
def evenPart (n : ℕ) : Finset (Finset (Fin n)) :=
  (univ : Finset (Fin n)).powerset.filter (fun S => Even S.card)

theorem mem_evenPart {S : Finset (Fin n)} : S ∈ evenPart n ↔ Even S.card := by
  simp [evenPart]

/-- `|Sᶜ| = n - |S|`, so `|Sᶜ|` is even iff `|S|` and `n` have the same parity. -/
theorem even_card_compl_iff (S : Finset (Fin n)) :
    Even Sᶜ.card ↔ (Even n ↔ Even S.card) := by
  rw [card_compl, Fintype.card_fin]
  exact Nat.even_sub (by simpa using S.card_le_univ)

/-- **Dichotomy.** For `n` even every matter state's conjugate is matter; for `n` odd
no matter state's conjugate is matter. -/
theorem evenPart_dichotomy :
    (Even n → ∀ S ∈ evenPart n, Sᶜ ∈ evenPart n) ∧
      (¬ Even n → ∀ S ∈ evenPart n, Sᶜ ∉ evenPart n) := by
  constructor
  · intro hn S hS
    rw [mem_evenPart] at hS ⊢
    exact (even_card_compl_iff S).2 (iff_of_true hn hS)
  · intro hn S hS h
    rw [mem_evenPart] at hS h
    exact hn ((even_card_compl_iff S).1 h |>.2 hS)

/-- The conjugate of the matter part is the matter part exactly when `n` is even. -/
theorem evenPart_image_compl_eq_iff :
    (evenPart n).image compl = evenPart n ↔ Even n := by
  constructor
  · intro h
    by_contra hn
    have h0 : (∅ : Finset (Fin n)) ∈ evenPart n := by simp [mem_evenPart]
    have : (∅ : Finset (Fin n))ᶜ ∈ evenPart n := by
      rw [← h]; exact mem_image_of_mem _ h0
    exact evenPart_dichotomy.2 hn _ h0 this
  · intro hn
    ext S
    constructor
    · rintro hS
      obtain ⟨T, hT, rfl⟩ := mem_image.1 hS
      exact evenPart_dichotomy.1 hn T hT
    · intro hS
      exact mem_image.2 ⟨Sᶜ, evenPart_dichotomy.1 hn S hS, compl_compl S⟩

variable {K : Type*} [CommRing K]

/-- The charge of the state `S`. -/
def stateCharge (y : Fin n → K) (S : Finset (Fin n)) : K := ∑ i ∈ S, y i

theorem stateCharge_compl (y : Fin n → K) (htr : ∑ i, y i = 0) (S : Finset (Fin n)) :
    stateCharge y Sᶜ = -stateCharge y S := by
  unfold stateCharge
  have h := Finset.sum_add_sum_compl S y
  rw [htr] at h
  linear_combination h

/-- **Even `n` is vector-like.** Every function of the charges summed over matter is
invariant under charge conjugation. -/
theorem evenPart_vectorlike_of_even (hn : Even n) (y : Fin n → K) (htr : ∑ i, y i = 0)
    (f : K → K) :
    ∑ S ∈ evenPart n, f (stateCharge y S) = ∑ S ∈ evenPart n, f (-stateCharge y S) := by
  conv_lhs => rw [← evenPart_image_compl_eq_iff.2 hn]
  rw [Finset.sum_image (fun a _ b _ h => compl_injective h)]
  refine Finset.sum_congr rfl fun S _ => ?_
  rw [stateCharge_compl y htr]

/-- For even `n` every odd moment of the matter charges vanishes, with no cancellation
condition: the cubic anomaly is identically zero. -/
theorem evenPart_odd_moment_zero (hn : Even n) (y : Fin n → K) (htr : ∑ i, y i = 0)
    (k : ℕ) (hk : Odd k) [NoZeroSMulDivisors ℕ K] :
    ∑ S ∈ evenPart n, stateCharge y S ^ k = 0 := by
  have h := evenPart_vectorlike_of_even hn y htr (fun x => x ^ k)
  simp only [hk.neg_pow, Finset.sum_neg_distrib] at h
  have h2 : (2 : ℕ) • ∑ S ∈ evenPart n, stateCharge y S ^ k = 0 := by
    rw [two_nsmul]; nth_rewrite 1 [h]; ring
  exact (smul_eq_zero.1 h2).resolve_left (by norm_num)

end QOU.StandardModel.OddStrands
