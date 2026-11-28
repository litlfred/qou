import QOU.StandardModel.StrandsAreBringEllipticQuotients

/-!
# Every subgroup of order 24 in `S₅` is a point stabiliser

Bean `qou-h0zz` (owner, 2026-11-28: "Links to lit so can prove gaps?"). This closes the
cited step in `StrandsAreBringEllipticQuotients.lean`: "every index-five subgroup of `S₅` is a
point stabiliser". Since `|S₅| = 120`, index five means order `24`.

## Proof

Let `H ≤ S₅` have order `24` and let `O` be the orbit of `0`.

1. Orbit–stabiliser: `|O|` divides `24`, so `|O| ≠ 5`. `H` is not transitive.
2. `H` maps `O` and its complement to themselves.
3. If `|O|` is `2` or `3`, the permutations preserving `O` number `|O|! (5 − |O|)! = 12`
   (`setStab_card_two_three`), so `|H| ≤ 12`, a contradiction.
4. If `|O|` is `1` or `4`, either `O` or its complement is a single point, and every
   permutation preserving `O` fixes it (`setStab_fixes_point`).

So `H` fixes a point `i`, and `H = Stab(i)` because both have `24` elements.

## Consequence

A transitive `S₅`-set of size five has point stabilisers of order `24`, so (by this result) each
is some `Stab(i)`; such a set `X` is therefore `S₅ / Stab(i)`, which is `Fin 5` with the natural
action. In particular the strands, the five elliptic quotients `B/A₄`, and
any other five-point `S₅`-set from Bring's surface carry stabilisers from the same list of five.

Finite group theory only. No empirical value enters.
-/

namespace QOU.StandardModel.IndexFive

open Equiv Finset QOU.StandardModel.StrandQuotients

/-- Permutations preserving a set `s` of strands. -/
def setStab (s : Finset (Fin 5)) : Finset (Perm (Fin 5)) :=
  univ.filter (fun g => ∀ j, j ∈ s ↔ g j ∈ s)

theorem setStab_card_two_three :
    ∀ s : Finset (Fin 5), s.card = 2 ∨ s.card = 3 → (setStab s).card = 12 := by
  decide +kernel

theorem setStab_fixes_point :
    ∀ s : Finset (Fin 5), s.card = 1 ∨ s.card = 4 →
      ∃ i : Fin 5, ∀ g ∈ setStab s, g i = i := by
  decide +kernel

/-- **Every subgroup of order 24 in `S₅` fixes a point.** -/
theorem fixes_point_of_card (H : Subgroup (Perm (Fin 5))) (hH : Nat.card H = 24) :
    ∃ i : Fin 5, ∀ g ∈ H, g i = i := by
  classical
  set O : Finset (Fin 5) := univ.filter (fun j => ∃ g ∈ H, g 0 = j) with hO
  -- the Mathlib orbit is `O`
  have horb : MulAction.orbit H (0 : Fin 5) = (O : Set (Fin 5)) := by
    ext j
    simp only [MulAction.mem_orbit_iff, Subgroup.smul_def, Perm.smul_def, hO, coe_filter,
      mem_univ, true_and, Set.mem_setOf_eq, Subtype.exists, exists_prop]
  -- (1) |O| divides 24
  have hdvd : O.card ∣ 24 := by
    have h1 := MulAction.index_stabilizer H (0 : Fin 5)
    rw [horb, Set.ncard_coe_finset] at h1
    rw [← h1, ← hH]
    exact Subgroup.index_dvd_card _
  -- (2) H preserves O
  have hpres : ∀ g ∈ H, ∀ j, j ∈ O ↔ g j ∈ O := by
    intro g hg j
    simp only [hO, mem_filter, mem_univ, true_and]
    constructor
    · rintro ⟨k, hk, rfl⟩
      exact ⟨g * k, H.mul_mem hg hk, rfl⟩
    · rintro ⟨k, hk, hkj⟩
      refine ⟨g⁻¹ * k, H.mul_mem (H.inv_mem hg) hk, ?_⟩
      rw [Perm.mul_apply, hkj, Perm.inv_apply_self]
  have hsub : ∀ g ∈ H, g ∈ setStab O := fun g hg => by
    simp only [setStab, mem_filter, mem_univ, true_and]; exact hpres g hg
  have h0 : (0 : Fin 5) ∈ O := by
    simp only [hO, mem_filter, mem_univ, true_and]; exact ⟨1, H.one_mem, rfl⟩
  have hpos : 1 ≤ O.card := card_pos.mpr ⟨0, h0⟩
  have hle : O.card ≤ 5 := by simpa using card_le_univ O
  -- card of H as a finset
  have hHcard : (univ.filter (fun g => g ∈ H)).card = 24 := by
    rw [← hH, Nat.card_eq_fintype_card, Fintype.card_subtype]
  have hcases : O.card = 1 ∨ O.card = 2 ∨ O.card = 3 ∨ O.card = 4 := by
    have : O.card ≠ 5 := by intro h; rw [h] at hdvd; norm_num at hdvd
    omega
  rcases hcases with h | h | h | h
  · obtain ⟨i, hi⟩ := setStab_fixes_point O (Or.inl h)
    exact ⟨i, fun g hg => hi g (hsub g hg)⟩
  · exfalso
    have := card_le_card (show univ.filter (fun g => g ∈ H) ⊆ setStab O from
      fun g hg => hsub g (by simpa using hg))
    rw [hHcard, setStab_card_two_three O (Or.inl h)] at this; omega
  · exfalso
    have := card_le_card (show univ.filter (fun g => g ∈ H) ⊆ setStab O from
      fun g hg => hsub g (by simpa using hg))
    rw [hHcard, setStab_card_two_three O (Or.inr h)] at this; omega
  · obtain ⟨i, hi⟩ := setStab_fixes_point O (Or.inr h)
    exact ⟨i, fun g hg => hi g (hsub g hg)⟩

/-- **Every subgroup of order 24 in `S₅` is a point stabiliser `Stab(i)`.** -/
theorem eq_stab_of_card (H : Subgroup (Perm (Fin 5))) (hH : Nat.card H = 24) :
    ∃ i : Fin 5, ∀ g, g ∈ H ↔ g ∈ stab i := by
  classical
  obtain ⟨i, hi⟩ := fixes_point_of_card H hH
  have hsub : univ.filter (fun g => g ∈ H) ⊆ stab i := fun g hg => by
    replace hg : g ∈ H := by simpa using hg
    simp only [stab, mem_filter, mem_univ, true_and]; exact hi g hg
  have heq : univ.filter (fun g => g ∈ H) = stab i := eq_of_subset_of_card_le hsub (by
    rw [stab_card i, ← hH, Nat.card_eq_fintype_card, Fintype.card_subtype])
  refine ⟨i, fun g => ?_⟩
  rw [← heq]; simp

/-- Index five in `S₅` is order 24. -/
theorem card_of_index_five (H : Subgroup (Perm (Fin 5))) (h : H.index = 5) :
    Nat.card H = 24 := by
  have := H.card_mul_index
  rw [h, Nat.card_eq_fintype_card (α := Perm (Fin 5)), Fintype.card_perm, Fintype.card_fin] at this
  norm_num [Nat.factorial] at this; omega

/-- **Every index-five subgroup of `S₅` is a point stabiliser.** -/
theorem eq_stab_of_index_five (H : Subgroup (Perm (Fin 5))) (h : H.index = 5) :
    ∃ i : Fin 5, ∀ g, g ∈ H ↔ g ∈ stab i :=
  eq_stab_of_card H (card_of_index_five H h)

end QOU.StandardModel.IndexFive
