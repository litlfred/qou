import QOU.EightfoldWay.NeutralLeptonFixesCharges
import QOU.StandardModel.OddExteriorAnomalyFreedom

/-!
# QOU.EightfoldWay.ChiralitySignIsHyperchargeSign — the two open signs are one sign

Two binary choices are open upstream of one generation:

* which part of `Λ^• K⁵` is matter, even or odd (`prop:even-strand-generation`);
* which root of the neutral-lepton condition, `α = 1/6` or `α = -1/6`
  (`prop:neutral-lepton-fixes-charges`).

This module shows they are the same choice, and locates what can see it.

* `stateCharge_neg_alpha` — `Q(-α)` on a state is `-Q(α)` on the state with the two
  isospin strands swapped.
* `even_neg_alpha_eq_odd` — **the even part at `-α` has the charge spectrum of the odd
  part at `α`.** So (even, `-1/6`) and (odd, `+1/6`) are the same theory; only the
  product of the two signs is physical.
* `stateCharge_toggle` / `electric_spectrum_even_eq_odd` — at `α = 1/6` strand `4` is
  neutral, so adding or removing it is a bijection from the even part to the odd part
  that preserves electric charge and does not move the colour strands. **Colour and
  electric charge cannot see the sign.**
* `hypercharge_count_even` / `hypercharge_count_odd` — the hypercharge direction
  `Y₀ = (-2,-2,-2,3,3)` (`Q(α) = T₃ + α Y₀`) can: six even states have `Y₀ = 1` and no
  odd state does, so no bijection between the parts preserves hypercharge.

So the chirality sign is the sign of hypercharge relative to the matter part. It is not
derived here. Base rings `ℚ` and `ℤ`; no empirical input.
-/

namespace QOU.EightfoldWay.ChiralitySignIsHyperchargeSign

open Finset
open QOU.EightfoldWay.NeutralLeptonFixesCharges
open QOU.StandardModel.Su3Su2U1Z6GroupAndCommutant
open QOU.StandardModel.OddExterior

theorem mem_evenSubsets' (S : Finset (Fin 5)) : S ∈ evenSubsets ↔ Even S.card := by
  simp [evenSubsets]

theorem mem_oddSubsets' (S : Finset (Fin 5)) : S ∈ oddSubsets ↔ Odd S.card := by
  simp [oddSubsets]

/-- `Q(-α)` on `S` is `-Q(α)` on `S` with the isospin strands swapped. -/
theorem stateCharge_neg_alpha (α : ℚ) (S : Finset (Fin 5)) :
    stateCharge (qWeight5 (-α)) S =
      -stateCharge (qWeight5 α) (S.map isoSwap.toEmbedding) := by
  simp only [stateCharge, Finset.sum_map, Equiv.coe_toEmbedding, qWeight5_neg,
    Finset.sum_neg_distrib]

/-- **The even part at `-α` is the odd part at `α`.** -/
theorem even_neg_alpha_eq_odd (α : ℚ) (f : ℚ → ℚ) :
    ∑ S ∈ evenSubsets, f (stateCharge (qWeight5 (-α)) S) =
      ∑ S ∈ oddSubsets, f (stateCharge (qWeight5 α) S) := by
  have hswap : ∑ S ∈ evenSubsets, f (stateCharge (qWeight5 (-α)) S) =
      ∑ S ∈ evenSubsets, f (-stateCharge (qWeight5 α) S) := by
    refine Finset.sum_equiv (Equiv.finsetCongr isoSwap) (fun S => ?_) (fun S _ => ?_)
    · simp [mem_evenSubsets', Equiv.finsetCongr_apply]
    · rw [stateCharge_neg_alpha, Equiv.finsetCongr_apply]
  rw [hswap]
  have h := sum_evenSubsets_eq_neg_odd (qWeight5 α) (sum_qWeight5 α) (fun x => f (-x))
  simpa using h

/-- Adding or removing a neutral strand does not change the charge. -/
theorem stateCharge_toggle {K : Type*} [CommRing K] (y : Fin 5 → K) (a : Fin 5)
    (ha : y a = 0) (S : Finset (Fin 5)) :
    stateCharge y (symmDiff S {a}) = stateCharge y S := by
  unfold stateCharge
  by_cases h : a ∈ S
  · have : symmDiff S {a} = S.erase a := by
      ext x; by_cases hx : x = a <;> simp [mem_symmDiff, hx, h]
    rw [this, Finset.sum_erase _ ha]
  · have : symmDiff S {a} = insert a S := by
      ext x; by_cases hx : x = a <;> simp [mem_symmDiff, hx, h]
    rw [this, Finset.sum_insert h, ha, zero_add]

theorem toggle_even_iff_odd :
    ∀ S : Finset (Fin 5), S ∈ evenSubsets ↔ symmDiff S {4} ∈ oddSubsets := by
  decide +kernel

/-- **Colour and electric charge cannot see the sign.** At `α = 1/6` the even and odd
parts have the same electric-charge spectrum, via the toggle of the neutral strand `4`,
which fixes the colour strands. -/
theorem electric_spectrum_even_eq_odd (f : ℚ → ℚ) :
    ∑ S ∈ evenSubsets, f (stateCharge (qWeight5 (1 / 6)) S) =
      ∑ S ∈ oddSubsets, f (stateCharge (qWeight5 (1 / 6)) S) := by
  have h4 : qWeight5 (1 / 6 : ℚ) 4 = 0 := by
    obtain ⟨-, -, -, -, q4⟩ := qWeight5_apply (1 / 6 : ℚ); rw [q4]; norm_num
  have hinv : Function.Involutive (fun S : Finset (Fin 5) => symmDiff S {4}) :=
    fun S => symmDiff_symmDiff_cancel_right _ _
  refine Finset.sum_equiv (Function.Involutive.toPerm _ hinv) (fun S => ?_) (fun S _ => ?_)
  · simpa using toggle_even_iff_odd S
  · simp only [Function.Involutive.coe_toPerm]; rw [stateCharge_toggle _ 4 h4]

/-- The hypercharge direction `Y₀ = Q(1) - Q(0)`, in integers. -/
def hyper : Fin 5 → ℤ := ![-2, -2, -2, 3, 3]

theorem hyper_eq (i : Fin 5) : (hyper i : ℚ) = qWeight5 (1 : ℚ) i - qWeight5 0 i := by
  fin_cases i <;> simp [hyper, qWeight5, Q5, T3, Y0, Matrix.add_apply]

/-- Six even states have `Y₀ = 1` (`Q`, the left-handed quarks). -/
theorem hypercharge_count_even :
    (evenSubsets.filter (fun S => stateCharge hyper S = 1)).card = 6 := by
  decide +kernel

/-- No odd state has `Y₀ = 1`. -/
theorem hypercharge_count_odd :
    (oddSubsets.filter (fun S => stateCharge hyper S = 1)).card = 0 := by
  decide +kernel

/-- **Hypercharge sees the sign:** no bijection from the even part to the odd part
preserves `Y₀`. -/
theorem no_hypercharge_bijection :
    ¬ ∃ e : Finset (Fin 5) ≃ Finset (Fin 5), (∀ S, S ∈ evenSubsets ↔ e S ∈ oddSubsets) ∧
      ∀ S, stateCharge hyper (e S) = stateCharge hyper S := by
  rintro ⟨e, hmem, hch⟩
  have h : (evenSubsets.filter (fun S => stateCharge hyper S = 1)).card =
      (oddSubsets.filter (fun S => stateCharge hyper S = 1)).card := by
    refine Finset.card_bij' (fun S _ => e S) (fun S _ => e.symm S) ?_ ?_ ?_ ?_
    · intro S hS; simp only [mem_filter] at hS ⊢; exact ⟨(hmem S).1 hS.1, (hch S).trans hS.2⟩
    · intro S hS
      simp only [mem_filter] at hS ⊢
      refine ⟨(hmem _).2 (by simpa using hS.1), ?_⟩
      rw [← hch, Equiv.apply_symm_apply]; exact hS.2
    · intro S _; simp
    · intro S _; simp
  rw [hypercharge_count_even, hypercharge_count_odd] at h
  exact absurd h (by norm_num)

end QOU.EightfoldWay.ChiralitySignIsHyperchargeSign
