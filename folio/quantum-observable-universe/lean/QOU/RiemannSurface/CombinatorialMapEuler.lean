import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.GroupTheory.Perm.Cycle.Factors
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# `QOU.RiemannSurface.CombinatorialMapEuler` — the Euler characteristic of a map is even

Bean `qou-m3tr` (Bring milestone M3), step 2, parent `qou-qhcr`.

A combinatorial map on a finite set of darts `D` is a permutation `σ` (vertex rotation) and a
fixed-point-free involution `α` (edges); its faces are the cycles of `σ * α`. Write `c(π)` for
the number of cycles of `π`, fixed points included (`numCycles`). The Euler characteristic is

  `χ = c(σ) − c(α) + c(σ * α)`.

## What is proved (sorry-free)

* `card_cycles`: `c(π) = #(nontrivial cycles) + #(fixed points)`, i.e. `c(π)` agrees with the
  number of parts of `π.partition`.
* `sign_eq_neg_one_pow`: `sign π = (-1)^(|D| + c(π))`.
* `two_mul_numCycles_of_involution`: a fixed-point-free involution has `|D| = 2·c(α)`.
* **`euler_even`**: `χ` is even, so `χ = 2 − 2g` for an integer `g` (`exists_genus`).

The proof is the sign homomorphism: `sign(σα) = sign σ · sign α` gives
`|D| + c(σ) + c(α) + c(σα)` even, and `|D| = 2 c(α)`. Connectivity is not used, and
orientability is built into the encoding by a rotation `σ`.

## What is NOT proved

* `g ≥ 0` (equivalently `χ ≤ 2`) for a **connected** map. This needs the genus inequality
  (e.g. by induction on edge contraction), and is what the capstone's `g : ℕ` presupposes.
* Step 3: a compact Riemann surface with a holomorphic `G`-action carries a `G`-equivariant map
  (triangulation). Mathlib gap.

Ref: [farkas-kra1992] Farkas–Kra, *Riemann Surfaces*, §I.2 (Euler characteristic of a
triangulated surface). The sign-parity argument is standard for permutation encodings of maps.
-/

namespace QOU.RiemannSurface.CombinatorialMapEuler

open Equiv Equiv.Perm

variable {D : Type*} [Fintype D] [DecidableEq D]

/-- The number of cycles of `π`, fixed points included. -/
noncomputable def numCycles (π : Perm D) : ℕ := Nat.card (Quotient (SameCycle.setoid π))

/-- Representative map: a fixed point to itself, a moved dart to its cycle. -/
noncomputable def cycleRep (π : Perm D) (x : D) :
    (Function.fixedPoints π) ⊕ (π.cycleFactorsFinset : Set (Perm D)) :=
  if h : π x = x then Sum.inl ⟨x, h⟩
  else Sum.inr ⟨π.cycleOf x, cycleOf_mem_cycleFactorsFinset_iff.2 (mem_support.2 h)⟩

theorem cycleRep_respects (π : Perm D) {x y : D} (hxy : π.SameCycle x y) :
    cycleRep π x = cycleRep π y := by
  unfold cycleRep
  by_cases hx : π x = x
  · have hy : π y = y := hxy.apply_eq_self_iff.1 hx
    have hxy' : x = y := hxy.eq_of_left hx
    subst hxy'
    rfl
  · have hy : ¬ π y = y := fun hy => hx (hxy.apply_eq_self_iff.2 hy)
    rw [dif_neg hx, dif_neg hy]
    congr 2
    exact hxy.cycleOf_eq

/-- Cycles of `π` are fixed points plus nontrivial cycle factors. -/
noncomputable def cyclesEquiv (π : Perm D) :
    Quotient (SameCycle.setoid π) ≃
      (Function.fixedPoints π) ⊕ (π.cycleFactorsFinset : Set (Perm D)) := by
  refine Equiv.ofBijective (Quotient.lift (cycleRep π) fun _ _ h => cycleRep_respects π h) ⟨?_, ?_⟩
  · intro a b hab
    induction a using Quotient.inductionOn with
    | h x =>
    induction b using Quotient.inductionOn with
    | h y =>
    simp only [Quotient.lift_mk] at hab
    apply Quotient.sound
    show π.SameCycle x y
    unfold cycleRep at hab
    by_cases hx : π x = x <;> by_cases hy : π y = y
    · rw [dif_pos hx, dif_pos hy] at hab
      have : x = y := congrArg Subtype.val (Sum.inl_injective hab)
      subst this; exact SameCycle.refl _ _
    · rw [dif_pos hx, dif_neg hy] at hab; cases hab
    · rw [dif_neg hx, dif_pos hy] at hab; cases hab
    · rw [dif_neg hx, dif_neg hy] at hab
      have hc : π.cycleOf x = π.cycleOf y := congrArg Subtype.val (Sum.inr_injective hab)
      have hyy : y ∈ (π.cycleOf y).support :=
        mem_support_cycleOf_iff.2 ⟨SameCycle.refl _ _, mem_support.2 hy⟩
      rw [← hc] at hyy
      exact (mem_support_cycleOf_iff.1 hyy).1
  · rintro (⟨x, hx⟩ | ⟨c, hc⟩)
    · refine ⟨Quotient.mk _ x, ?_⟩
      simp only [Quotient.lift_mk, cycleRep, dif_pos (show π x = x from hx)]
    · have hc' : c ∈ π.cycleFactorsFinset := hc
      have hcyc : c.IsCycle := (mem_cycleFactorsFinset_iff.1 hc').1
      obtain ⟨a, ha⟩ : c.support.Nonempty := by
        rw [Finset.nonempty_iff_ne_empty, Ne, support_eq_empty_iff]; exact hcyc.ne_one
      have hca : c = π.cycleOf a := cycle_is_cycleOf ha hc'
      have haπ : a ∈ π.support := mem_cycleFactorsFinset_support_le hc' ha
      refine ⟨Quotient.mk _ a, ?_⟩
      simp only [Quotient.lift_mk, cycleRep, dif_neg (mem_support.1 haπ)]
      congr 2
      exact hca.symm

theorem card_cycles (π : Perm D) :
    numCycles π = Fintype.card (Function.fixedPoints π) + π.cycleType.card := by
  unfold numCycles
  rw [Nat.card_congr (cyclesEquiv π), Nat.card_sum, Nat.card_eq_fintype_card]
  congr 1
  rw [Nat.card_eq_card_toFinset, Finset.toFinset_coe, cycleType_def, Multiset.card_map]
  rfl

/-- `sign π = (-1)^(|D| + c(π))`. -/
theorem sign_eq_neg_one_pow (π : Perm D) :
    sign π = (-1) ^ (Fintype.card D + numCycles π) := by
  rw [sign_of_cycleType, card_cycles, card_fixedPoints]
  have hle : π.cycleType.sum ≤ Fintype.card D := by
    rw [sum_cycleType]; exact Finset.card_le_univ _
  have : Fintype.card D + (Fintype.card D - π.cycleType.sum + π.cycleType.card) =
      (π.cycleType.sum + π.cycleType.card) + 2 * (Fintype.card D - π.cycleType.sum) := by
    omega
  rw [this, pow_add _ (_ + _), pow_mul, neg_one_sq, one_pow, mul_one]

/-- A fixed-point-free involution has `|D| = 2·c(α)`. -/
theorem two_mul_numCycles_of_involution (α : Perm D) (hinv : α * α = 1) (hfix : ∀ x, α x ≠ x) :
    Fintype.card D = 2 * numCycles α := by
  have hfp : Fintype.card (Function.fixedPoints α) = 0 := by
    rw [Fintype.card_eq_zero_iff]; exact ⟨fun ⟨x, hx⟩ => hfix x hx⟩
  have h2 : ∀ n ∈ α.cycleType, n = 2 := by
    intro n hn
    have hd : n ∣ orderOf α := dvd_of_mem_cycleType hn
    have ho : orderOf α ∣ 2 := orderOf_dvd_of_pow_eq_one (by rw [sq]; exact hinv)
    have := Nat.le_of_dvd (by norm_num) (hd.trans ho)
    have := two_le_of_mem_cycleType hn
    omega
  have hsum : α.cycleType.sum = 2 * α.cycleType.card := by
    rw [Multiset.eq_replicate_of_mem h2, Multiset.sum_replicate, Multiset.card_replicate,
      smul_eq_mul, mul_comm]
  have hcard := card_fixedPoints α
  rw [hfp] at hcard
  have hle : α.cycleType.sum ≤ Fintype.card D := by
    rw [sum_cycleType]; exact Finset.card_le_univ _
  rw [card_cycles, hfp]
  omega

/-- **The Euler characteristic of a combinatorial map is even.** -/
theorem euler_even (σ α : Perm D) (hinv : α * α = 1) (hfix : ∀ x, α x ≠ x) :
    Even ((numCycles σ : ℤ) - numCycles α + numCycles (σ * α)) := by
  have hs := sign_mul σ α
  rw [sign_eq_neg_one_pow, sign_eq_neg_one_pow, sign_eq_neg_one_pow, ← pow_add] at hs
  have hD := two_mul_numCycles_of_involution α hinv hfix
  -- `(-1)^a = (-1)^b` forces `a ≡ b (mod 2)`.
  have hpar : Even (Fintype.card D + numCycles (σ * α) +
      (Fintype.card D + numCycles σ + (Fintype.card D + numCycles α))) := by
    have h1 : ((-1 : ℤˣ)) ^ (Fintype.card D + numCycles (σ * α) +
        (Fintype.card D + numCycles σ + (Fintype.card D + numCycles α))) = 1 := by
      rw [pow_add, hs, ← pow_add, ← two_mul, pow_mul, neg_one_sq, one_pow]
    exact (neg_one_pow_eq_one_iff_even (by decide)).1 h1
  obtain ⟨k, hk⟩ := hpar
  refine ⟨(k : ℤ) - 2 * (numCycles α : ℤ) - (Fintype.card D : ℤ), ?_⟩
  have hk' : ((Fintype.card D + numCycles (σ * α) +
      (Fintype.card D + numCycles σ + (Fintype.card D + numCycles α)) : ℕ) : ℤ) = k + k := by
    exact_mod_cast hk
  push_cast at hk'
  have hD' : (Fintype.card D : ℤ) = 2 * numCycles α := by exact_mod_cast hD
  linarith

/-- So `χ = 2 − 2g` for an integer `g` (`g ≥ 0` for connected maps is not proved here). -/
theorem exists_genus (σ α : Perm D) (hinv : α * α = 1) (hfix : ∀ x, α x ≠ x) :
    ∃ g : ℤ, (numCycles σ : ℤ) - numCycles α + numCycles (σ * α) = 2 - 2 * g := by
  obtain ⟨k, hk⟩ := euler_even σ α hinv hfix
  exact ⟨1 - k, by rw [hk]; ring⟩

end QOU.RiemannSurface.CombinatorialMapEuler
