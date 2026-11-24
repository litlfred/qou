import Mathlib.Tactic

/-!
# Subset cumulants at general `A`: the algebra the binding-gap arc measured

`computations/probes/the_binding_arc_was_measured_in_float64_probe.py` (bean `qou-wx83`)
re-measured, at 200 bits, the identities the `t7qv` binding-gap arc had read off the float64
floor. Every one of them held to `~1e-60`. This file proves the ones that are *algebra* — true
for every set function, every ring, every `q` — so that the probe's role is reduced to what a
numerical check can honestly be: a consistency test on the code, not the warrant for the claim.

The arc's object is a set function `L : Finset ι → R` on subsets of the `A` nucleons —
`L S = log(tr_free / tr_S)` with bonds placed among the nucleons in `S` — and its Möbius
cumulants over the Boolean lattice,

    cum L S = L S − Σ_{T ⊊ S} cum L T .

Three facts carry the arc's cumulant reading:

* **Reconstruction** (`sum_powerset_cum`): `Σ_{T ⊆ S} cum L T = L S`. Immediate from the
  definition; the probe's "reconstruction residual `2.49e-60`" is an instance.
* **The size-only recursion** (`cum_eq_sizeCum`): if `L S` depends only on `#S` — the
  exchangeable, homonuclear case — then so does `cum L S`, and the scalar sequence obeys

      c_k = f_k − Σ_{j<k} C(k,j) · c_j ,

  which is the `c_k`-only recursion the owner asked for. It replaces `2^A − A − 1` traces by
  `A − 1`. The probe's "size-only vs full Möbius `4.98e-60`" is an instance.
* **Cumulants vanish across an additive split** (`cum_eq_zero_of_additive_split`): if the ground
  set splits as `A ⊔ B` and `L S = L (S ∩ A) + L (S ∩ B)`, then `cum L S = 0` for every `S`
  meeting both sides. This is what makes the Möbius coefficients *cumulants* in the standard
  sense — independence kills every mixed cumulant — and it is exactly the additivity the
  Markov trace supplies on a split link. The probe's "additivity residual `4.98e-60`" is an
  instance, and `QOU.Mass.PairwiseCumulantVanishing` (hard-wired to `Fin 4`, orders 3 and 4)
  is the special case where every pair is its own block.

Two smaller facts from the same probe, about the seminormal form and the Hecke relation:

* `seminormal_diag_product`: the two diagonal entries of a branching `2×2` seminormal block,
  `a = h/(1 − u⁻²)` and `a' = h/(1 − u²)` with `u = q^ρ`, multiply to `−(h/(u − u⁻¹))²`, i.e.
  `−1/[ρ]_q²`. So the off-diagonal radicand `a·a' + 1` is `1 − 1/[ρ]²`, and the `abs` the
  corpus's builder wraps around it (`sqrt(|a a' + 1|)`) is a no-op whenever `|[ρ]| ≥ 1`
  (`seminormal_radicand_nonneg`).
* `hecke_quadratic_factor` / `hecke_root_product`: `x² − h x − 1 = (x − q)(x + q⁻¹)` and
  `q · (−q⁻¹) = −1`. The `det T = −1` the arc leans on is this, read on a block.

Nothing here is numerical. The numbers live in the probe; the *reasons* live here.

Ground ring: any `CommRing` for the cumulant layer, any `Field` for the seminormal layer.
Bean `qou-wx83`.
-/

namespace QOU.Mass.SubsetCumulantRecursion

open Finset

variable {ι : Type*} [DecidableEq ι] {R : Type*} [CommRing R]

/-! ### Möbius cumulants over the Boolean lattice -/

/-- Möbius cumulants of a set function, by the recursion the probes run:
`cum L S = L S − Σ_{T ⊊ S} cum L T`. -/
noncomputable def cum (L : Finset ι → R) (S : Finset ι) : R :=
  L S - ∑ T ∈ (S.powerset.erase S).attach, cum L T.1
termination_by S.card
decreasing_by
  have h := T.2
  rw [Finset.mem_erase, Finset.mem_powerset] at h
  exact Finset.card_lt_card (Finset.ssubset_iff_subset_ne.mpr ⟨h.2, h.1⟩)

theorem cum_eq (L : Finset ι → R) (S : Finset ι) :
    cum L S = L S - ∑ T ∈ S.powerset.erase S, cum L T := by
  rw [cum, Finset.sum_attach]

theorem cum_empty (L : Finset ι → R) : cum L ∅ = L ∅ := by
  rw [cum_eq]; simp

/-- **Reconstruction.** The cumulants of the subsets of `S` sum back to `L S`. -/
theorem sum_powerset_cum (L : Finset ι → R) (S : Finset ι) :
    ∑ T ∈ S.powerset, cum L T = L S := by
  have hS : S ∈ S.powerset := Finset.mem_powerset.mpr (Finset.Subset.refl S)
  rw [← Finset.add_sum_erase _ _ hS, cum_eq]
  ring

/-! ### The size-only (`c_k`) recursion -/

/-- The scalar recursion for an exchangeable system: `c_k = f_k − Σ_{j<k} C(k,j) c_j`. -/
noncomputable def sizeCum (f : ℕ → R) (k : ℕ) : R :=
  f k - ∑ j ∈ (Finset.range k).attach, (k.choose j.1 : R) * sizeCum f j.1
termination_by k
decreasing_by exact Finset.mem_range.mp j.2

theorem sizeCum_eq (f : ℕ → R) (k : ℕ) :
    sizeCum f k = f k - ∑ j ∈ Finset.range k, (k.choose j : R) * sizeCum f j := by
  rw [sizeCum, Finset.sum_attach _ (fun j => (k.choose j : R) * sizeCum f j)]

/-- With no zero- or one-body term the recursion starts at `k = 2`, as the probes write it. -/
theorem sizeCum_zero_one (f : ℕ → R) (h0 : f 0 = 0) (h1 : f 1 = 0) :
    sizeCum f 0 = 0 ∧ sizeCum f 1 = 0 := by
  have hz : sizeCum f 0 = 0 := by rw [sizeCum_eq, h0]; simp
  refine ⟨hz, ?_⟩
  rw [sizeCum_eq, h1, Finset.sum_range_one, hz]; simp

/-- Summing a function of the cardinality over the *proper* subsets of `S`. -/
theorem sum_powerset_erase_apply_card (g : ℕ → R) (S : Finset ι) :
    ∑ T ∈ S.powerset.erase S, g T.card
      = ∑ j ∈ Finset.range S.card, (S.card.choose j : R) * g j := by
  have hS : S ∈ S.powerset := Finset.mem_powerset.mpr (Finset.Subset.refl S)
  have h1 := Finset.sum_powerset_apply_card g (x := S)
  rw [← Finset.add_sum_erase _ _ hS, Finset.sum_range_succ, Nat.choose_self, one_smul] at h1
  simp only [nsmul_eq_mul] at h1
  linear_combination h1

/-- **The size-only collapse.** If `L` depends only on cardinality, so do its cumulants, and
they obey the scalar recursion. -/
theorem cum_eq_sizeCum (L : Finset ι → R) (f : ℕ → R) (hL : ∀ S, L S = f S.card)
    (S : Finset ι) : cum L S = sizeCum f S.card := by
  induction S using Finset.strongInduction with
  | H S ih =>
    rw [cum_eq, hL, sizeCum_eq]
    congr 1
    rw [← sum_powerset_erase_apply_card (sizeCum f) S]
    refine Finset.sum_congr rfl (fun T hT => ?_)
    rw [Finset.mem_erase, Finset.mem_powerset] at hT
    exact ih T (Finset.ssubset_iff_subset_ne.mpr ⟨hT.2, hT.1⟩)

/-! ### Cumulants vanish across an additive split -/

theorem filter_powerset_subset (S A : Finset ι) :
    S.powerset.filter (fun T => T ⊆ A) = (S ∩ A).powerset := by
  ext T
  simp [Finset.mem_filter, Finset.mem_powerset, Finset.subset_inter_iff]

theorem filter_powerset_not_subset_subset (S A B : Finset ι) (hAB : Disjoint A B) :
    S.powerset.filter (fun T => ¬ T ⊆ A ∧ T ⊆ B) = (S ∩ B).powerset.erase ∅ := by
  ext T
  simp only [Finset.mem_filter, Finset.mem_powerset, Finset.mem_erase, Finset.subset_inter_iff]
  constructor
  · rintro ⟨hTS, hTA, hTB⟩
    refine ⟨?_, hTS, hTB⟩
    rintro rfl
    exact hTA (Finset.empty_subset _)
  · rintro ⟨hne, hTS, hTB⟩
    refine ⟨hTS, ?_, hTB⟩
    intro hTA
    apply hne
    exact Finset.eq_empty_of_forall_notMem
      (fun x hx => Finset.disjoint_left.mp hAB (hTA hx) (hTB hx))

/-- **Mixed cumulants of an additive set function vanish.** If the ground set splits as
`A ⊔ B` and `L` is additive across the split, every cumulant straddling it is zero. -/
theorem cum_eq_zero_of_additive_split (L : Finset ι → R) (A B : Finset ι)
    (hAB : Disjoint A B) (h0 : L ∅ = 0)
    (hadd : ∀ S, S ⊆ A ∪ B → L S = L (S ∩ A) + L (S ∩ B)) :
    ∀ S, S ⊆ A ∪ B → (S ∩ A).Nonempty → (S ∩ B).Nonempty → cum L S = 0 := by
  intro S
  induction S using Finset.strongInduction with
  | H S ih =>
    intro hS hA hB
    -- split the powerset by `T ⊆ A`, then the remainder by `T ⊆ B`
    have hsplit1 := Finset.sum_filter_add_sum_filter_not S.powerset (fun T => T ⊆ A) (cum L)
    have hsplit2 := Finset.sum_filter_add_sum_filter_not
      (S.powerset.filter (fun T => ¬ T ⊆ A)) (fun T => T ⊆ B) (cum L)
    rw [Finset.filter_filter, Finset.filter_filter] at hsplit2
    rw [filter_powerset_subset, sum_powerset_cum, sum_powerset_cum] at hsplit1
    rw [filter_powerset_not_subset_subset S A B hAB] at hsplit2
    -- the block that meets both sides contributes only `cum L S`: the rest is the IH
    have hthird :
        ∑ T ∈ S.powerset.filter (fun T => ¬ T ⊆ A ∧ ¬ T ⊆ B), cum L T = cum L S := by
      have hSmem : S ∈ S.powerset.filter (fun T => ¬ T ⊆ A ∧ ¬ T ⊆ B) := by
        simp only [Finset.mem_filter, Finset.mem_powerset]
        refine ⟨Finset.Subset.refl S, ?_, ?_⟩
        · intro hSA
          obtain ⟨x, hx⟩ := hB
          rw [Finset.mem_inter] at hx
          exact Finset.disjoint_left.mp hAB (hSA hx.1) hx.2
        · intro hSB
          obtain ⟨x, hx⟩ := hA
          rw [Finset.mem_inter] at hx
          exact Finset.disjoint_left.mp hAB hx.2 (hSB hx.1)
      rw [← Finset.add_sum_erase _ _ hSmem, Finset.sum_eq_zero, add_zero]
      intro T hT
      rw [Finset.mem_erase, Finset.mem_filter, Finset.mem_powerset] at hT
      obtain ⟨hTS, hTsub, hTA, hTB⟩ := hT
      have hTAB : T ⊆ A ∪ B := hTsub.trans hS
      apply ih T (Finset.ssubset_iff_subset_ne.mpr ⟨hTsub, hTS⟩) hTAB
      · rw [Finset.not_subset] at hTB
        obtain ⟨x, hxT, hxB⟩ := hTB
        have hx := Finset.mem_union.mp (hTAB hxT)
        exact ⟨x, Finset.mem_inter.mpr ⟨hxT, hx.resolve_right hxB⟩⟩
      · rw [Finset.not_subset] at hTA
        obtain ⟨x, hxT, hxA⟩ := hTA
        have hx := Finset.mem_union.mp (hTAB hxT)
        exact ⟨x, Finset.mem_inter.mpr ⟨hxT, hx.resolve_left hxA⟩⟩
    -- the `B`-side block, minus the empty set it shares with the `A`-side
    have hsecond : ∑ T ∈ (S ∩ B).powerset.erase ∅, cum L T = L (S ∩ B) - L ∅ := by
      rw [Finset.sum_erase_eq_sub (Finset.mem_powerset.mpr (Finset.empty_subset _)),
        sum_powerset_cum, cum_empty]
    rw [hsecond, hthird, h0] at hsplit2
    have hL := hadd S hS
    linear_combination hsplit1 + hsplit2 + hL

/-! ### The seminormal radicand and the Hecke roots -/

section Seminormal

variable {K : Type*} [Field K]

/-- The two diagonal entries of a branching seminormal block multiply to `−(h/(u − u⁻¹))²`,
i.e. `−1/[ρ]_q²` once `h = q − q⁻¹` and `u = q^ρ`. -/
theorem seminormal_diag_product (h u : K) (hu : u ≠ 0) (hu2 : u ^ 2 ≠ 1) :
    (h / (1 - (u ^ 2)⁻¹)) * (h / (1 - u ^ 2)) = -(h / (u - u⁻¹)) ^ 2 := by
  have hA : 1 - u ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm hu2)
  have hB : 1 - (u ^ 2)⁻¹ ≠ 0 := by
    intro hc
    apply hu2
    have : (u ^ 2)⁻¹ = 1 := (sub_eq_zero.mp hc).symm
    rw [inv_eq_one] at this
    exact this
  -- the denominators multiply to minus a square: `(1 − u⁻²)(1 − u²) = −(u − u⁻¹)²`
  have key : (1 - (u ^ 2)⁻¹) * (1 - u ^ 2) = -(u - u⁻¹) ^ 2 := by
    have h1 : u * u⁻¹ = 1 := mul_inv_cancel₀ hu
    rw [← inv_pow]
    linear_combination (u * u⁻¹ - 1) * h1
  rw [div_mul_div_comm, key, div_neg, div_pow, ← sq]

/-- Hence the off-diagonal radicand is `1 − (h/(u − u⁻¹))²`. -/
theorem seminormal_radicand (h u : K) (hu : u ≠ 0) (hu2 : u ^ 2 ≠ 1) :
    (h / (1 - (u ^ 2)⁻¹)) * (h / (1 - u ^ 2)) + 1 = 1 - (h / (u - u⁻¹)) ^ 2 := by
  rw [seminormal_diag_product h u hu hu2]; ring

/-- In an ordered field the radicand is non-negative whenever `|h/(u − u⁻¹)| ≤ 1`, i.e.
`|[ρ]_q| ≥ 1` — so the `abs` in `sqrt(|a a' + 1|)` is a no-op there. -/
theorem seminormal_radicand_nonneg {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (h u : K) (hu : u ≠ 0) (hu2 : u ^ 2 ≠ 1) (hb : |h / (u - u⁻¹)| ≤ 1) :
    0 ≤ (h / (1 - (u ^ 2)⁻¹)) * (h / (1 - u ^ 2)) + 1 := by
  rw [seminormal_radicand h u hu hu2, sub_nonneg]
  have := abs_le.mp hb
  nlinarith [this.1, this.2]

/-- The Hecke quadratic `x² − h x − 1` with `h = q − q⁻¹` factors as `(x − q)(x + q⁻¹)`. -/
theorem hecke_quadratic_factor (q x : K) (hq : q ≠ 0) :
    (x - q) * (x + q⁻¹) = x ^ 2 - (q - q⁻¹) * x - 1 := by
  field_simp
  ring

/-- Its two roots multiply to `−1`: the `det T = −1` of the arc, on any block. -/
theorem hecke_root_product (q : K) (hq : q ≠ 0) : q * (-q⁻¹) = -1 := by
  field_simp

end Seminormal

end QOU.Mass.SubsetCumulantRecursion
