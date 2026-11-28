import QOU.StandardModel.OddExteriorAnomalyFreedom

/-!
# Chirality is an orientation of `G_m`: complement swaps the halves of `Λ K⁵`

Bean `qou-qvpl` (hypercharge / chirality). `OddExteriorAnomalyFreedom.lean` takes matter to be
the even half `Λ⁰ ⊕ Λ² ⊕ Λ⁴` by convention (PR #9811) and leaves deriving that choice open. This
file shows what any derivation has to break.

`G_m` acts on `Λᵏ K⁵` with weight `k`. The complement `S ↦ Sᶜ` (the Hodge star on basis states)

* swaps the odd and even halves (`mem_oddSubsets_iff_compl_mem_evenSubsets`),
* sends weight `k` to `5 − k` (`card_compl_five`), i.e. turns the `G_m`-action `λ` into
  `det · λ⁻¹`, the formal inverse of `G_m` twisted by the determinant,
* negates every traceless charge (`stateCharge_compl`).

So (`sum_odd_eq_sum_even_of_symmetric`): **any functional of (charge, weight) that is invariant
under `(y, k) ↦ (−y, 5 − k)` takes the same value on both halves.** No such functional can
select the chirality. A derivation of which half is matter must use an input that is *not*
invariant under the bar involution `q ↦ q⁻¹` together with charge conjugation: an orientation of
`G_m` (a choice of generator `q` rather than `q⁻¹` of its character group), such as the sign of a
linking number or of a twist exponent.

This is a structural statement (scope (b) in the sense of AGENTS.md): the invariant is the
complement bijection. It does not derive the chirality. No measured values.
-/

namespace QOU.StandardModel.ChiralityOrientation

open Finset QOU.StandardModel.OddExterior

/-- The `G_m`-weight of `S` is `|S|`; the complement has weight `5 − |S|`. -/
theorem card_compl_five (S : Finset (Fin 5)) : Sᶜ.card = 5 - S.card := by
  rw [card_compl, Fintype.card_fin]

/-- **Complement swaps the halves.** -/
theorem mem_oddSubsets_iff_compl_mem_evenSubsets (S : Finset (Fin 5)) :
    S ∈ oddSubsets ↔ Sᶜ ∈ evenSubsets := by
  revert S; decide

theorem mem_evenSubsets_iff_compl_mem_oddSubsets (S : Finset (Fin 5)) :
    S ∈ evenSubsets ↔ Sᶜ ∈ oddSubsets := by
  revert S; decide

variable {K : Type*} [CommRing K]

/-- **Complement negates a traceless charge.** -/
theorem stateCharge_compl (y : Fin 5 → K) (htr : ∑ i, y i = 0) (S : Finset (Fin 5)) :
    stateCharge y Sᶜ = -stateCharge y S := by
  unfold stateCharge
  have h := Finset.sum_add_sum_compl S y
  rw [htr] at h
  linear_combination h

/-- `oddSubsets` is the image of `evenSubsets` under complement. -/
theorem oddSubsets_eq_image_compl : oddSubsets = evenSubsets.image (fun S => Sᶜ) := by
  decide

/-- **No (charge, weight)-functional symmetric under `(y, k) ↦ (−y, 5 − k)` separates the
halves.** -/
theorem sum_odd_eq_sum_even_of_symmetric (y : Fin 5 → K) (htr : ∑ i, y i = 0)
    (f : K → ℕ → K) (hf : ∀ c k, k ≤ 5 → f (-c) (5 - k) = f c k) :
    ∑ S ∈ oddSubsets, f (stateCharge y S) S.card =
      ∑ S ∈ evenSubsets, f (stateCharge y S) S.card := by
  rw [oddSubsets_eq_image_compl, Finset.sum_image (fun a _ b _ h => compl_injective h)]
  refine Finset.sum_congr rfl (fun S _ => ?_)
  rw [stateCharge_compl y htr, card_compl_five]
  exact hf _ _ (by simpa using S.card_le_univ)

end QOU.StandardModel.ChiralityOrientation
