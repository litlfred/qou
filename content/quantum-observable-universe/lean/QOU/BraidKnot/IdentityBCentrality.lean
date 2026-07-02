import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.Data.Complex.Basic
import QOU.BraidKnot.RegularRepTrace

/-!
# Centrality of the Jucys–Murphy power sum `C₂`, de-abstracted to one combinatorial core

`IdentityBWedderburn.identityB_via_wedderburn_unconditional` reduces Identity (B) for `ℂ[Sₙ]` to a
*single* classical input: the centrality of the second Jucys–Murphy power sum

  `C₂ = ∑ₖ Xₖ² ∈ Z(ℂ[Sₙ])`,   `Xₖ = ∑_{i<k} (i k)`.

This module **proves that centrality outright** — no `sorry` remains. The chain
center ⟸ class-function coefficient ⟸ cycle-type case analysis is machine-checked end to end,
including the combinatorial heart

  `centralC2_apply_threecycle` : for a 3-cycle `σ`, `C₂ σ = 1`

(each 3-cycle arises from exactly one triple `(k,i,j)` with `i,j<k` and `swap(i,k)·swap(j,k)=σ` —
namely `k = max(supp σ)`, `i = σ⁻¹(k)`, `j = σ(k)`; the opposite ordering produces `σ⁻¹`).

Everything below is sorry-free (`[propext, Classical.choice, Quot.sound]`):

* `centralC2_apply` — coefficient of `C₂` at `σ` as `∑ₖ #{(i,j) : i,j<k, swap(i,k)·swap(j,k)=σ}`.
* `swap_prod_classify` — `swap(i,k)·swap(j,k)` is `1` (if `i=j`) or a 3-cycle.
* `centralC2_apply_other` — `σ` neither `1` nor a 3-cycle ⟹ `C₂ σ = 0` (CharZero-free).
* `centralC2_apply_one` — `C₂ 1 = binom(n,2)` (from `RegularRepTrace.centralC2_coeff_one`).
* `centralC2_apply_threecycle` — `C₂ σ = 1` for a 3-cycle `σ` (the `k = max(supp σ)` count:
  the pair set is empty unless `k = max(supp σ)`, and there it is exactly `{(σ⁻¹ k, σ k)}`).
* `isThreeCycle_conj`, `conj_eq_one_iff` — conjugation preserves cycle type / the identity.
* `commute_all_of_commute_single`, `mem_center_of_commute_single`, `commute_single_of_classFun`,
  `mem_center_of_classFun` — general: a class-function coefficient ⟹ central in `MonoidAlgebra`.
* `centralC2_classFun` — the coefficient of `C₂` is a class function (three cycle-type cases).
* `centralC2_mem_center` — `C₂ ∈ Set.center ℂ[Sₙ]`, **sorry-free**: together with
  `IdentityBWedderburn.identityB_via_wedderburn` this closes Identity (B) for `ℂ[Sₙ]` outright.

So `C₂ = binom(n,2)·1 + (class-sum of all 3-cycles)` at the coefficient level — Jucys' theorem
for the `p = 2` power sum — is fully formalised.

Base ring: the coefficient/centrality machinery is generic (`[CommRing R]` / `[CommSemiring S]`);
the final `centralC2_mem_center` is stated at `ℂ` (the ring `IdentityBWedderburn` consumes).

Ref: [vershik-kerov1977] (Okounkov–Vershik / Jucys central elements).
-/

open MonoidAlgebra Finset Equiv

namespace QOU.BraidKnot.IdentityBCentrality

open QOU.BraidKnot.RegularRepTrace

variable {R : Type*} [CommRing R]

/-- Coefficient expansion of `centralC2` at a permutation `σ`. -/
theorem centralC2_apply (n : ℕ) (σ : Equiv.Perm (Fin n)) :
    (centralC2 (R := R) n) σ =
      (∑ k : Fin n,
        ((((Finset.univ.filter (fun i : Fin n => i.val < k.val)) ×ˢ
          (Finset.univ.filter (fun i : Fin n => i.val < k.val))).filter
            (fun p => Equiv.swap p.1 k * Equiv.swap p.2 k = σ)).card : R)) := by
  unfold centralC2
  rw [Finsupp.finset_sum_apply]
  refine Finset.sum_congr rfl (fun k _ => ?_)
  set F := Finset.univ.filter (fun i : Fin n => i.val < k.val) with hF
  have expand : (∑ i ∈ F, single (Equiv.swap i k) (1 : R)) ^ 2
      = ∑ p ∈ F ×ˢ F, single (Equiv.swap p.1 k * Equiv.swap p.2 k) (1 : R) := by
    rw [pow_two, Finset.sum_mul_sum, Finset.sum_product]
    refine Finset.sum_congr rfl (fun i _ => ?_)
    refine Finset.sum_congr rfl (fun j _ => ?_)
    rw [single_mul_single, mul_one]
  rw [expand, Finsupp.finset_sum_apply]
  simp only [Finsupp.single_apply]
  rw [Finset.sum_boole]

/-- `swap(i,k)·swap(j,k)` is `1` (when `i=j`) or a 3-cycle (when `i,j,k` are distinct). -/
theorem swap_prod_classify {n : ℕ} (i j k : Fin n) (hik : i ≠ k) (hjk : j ≠ k) :
    Equiv.swap i k * Equiv.swap j k = 1 ∨ (Equiv.swap i k * Equiv.swap j k).IsThreeCycle := by
  rcases eq_or_ne i j with hij | hij
  · subst hij; left; exact Equiv.swap_mul_self i k
  · right
    rw [Equiv.swap_comm i k, Equiv.swap_comm j k]
    exact Equiv.Perm.isThreeCycle_swap_mul_swap_same (Ne.symm hik) (Ne.symm hjk) hij

/-- `σ` neither `1` nor a 3-cycle ⟹ `centralC2 σ = 0` (CharZero-free: the card is `0` in `ℕ`). -/
theorem centralC2_apply_other (n : ℕ) (σ : Equiv.Perm (Fin n))
    (h1 : σ ≠ 1) (h3 : ¬ σ.IsThreeCycle) :
    (centralC2 (R := R) n) σ = 0 := by
  rw [centralC2_apply]
  apply Finset.sum_eq_zero
  intro k _
  have hcard : (((Finset.univ.filter (fun i : Fin n => i.val < k.val)) ×ˢ
      (Finset.univ.filter (fun i : Fin n => i.val < k.val))).filter
        (fun p => Equiv.swap p.1 k * Equiv.swap p.2 k = σ)).card = 0 := by
    rw [Finset.card_eq_zero, Finset.filter_eq_empty_iff]
    rintro p hp
    simp only [Finset.mem_product, Finset.mem_filter, Finset.mem_univ, true_and] at hp
    obtain ⟨hi, hj⟩ := hp
    have hik : p.1 ≠ k := fun h => by rw [h] at hi; exact absurd hi (lt_irrefl _)
    have hjk : p.2 ≠ k := fun h => by rw [h] at hj; exact absurd hj (lt_irrefl _)
    intro heq
    rcases swap_prod_classify p.1 p.2 k hik hjk with h | h
    · exact h1 (heq ▸ h)
    · exact h3 (heq ▸ h)
  rw [hcard, Nat.cast_zero]

/-- `centralC2` at the identity permutation is `binom(n,2)`. -/
theorem centralC2_apply_one (n : ℕ) :
    (centralC2 (R := R) n) 1 = (n.choose 2 : R) :=
  centralC2_coeff_one n

/-! #### The 3-cycle count: action and support of `swap(i,k)·swap(j,k)`

Multiplication convention: `(f * g) x = f (g x)`, so `swap(i,k)·swap(j,k)` sends
`i ↦ k ↦ j ↦ i` and fixes everything else. -/

private lemma swapProd_apply_fst {n : ℕ} (i j k : Fin n) (hij : i ≠ j) (hik : i ≠ k) :
    (Equiv.swap i k * Equiv.swap j k) i = k := by
  rw [Equiv.Perm.mul_apply, Equiv.swap_apply_of_ne_of_ne hij hik, Equiv.swap_apply_left]

private lemma swapProd_apply_top {n : ℕ} (i j k : Fin n) (hij : i ≠ j) (hjk : j ≠ k) :
    (Equiv.swap i k * Equiv.swap j k) k = j := by
  rw [Equiv.Perm.mul_apply, Equiv.swap_apply_right,
    Equiv.swap_apply_of_ne_of_ne (Ne.symm hij) hjk]

private lemma swapProd_apply_snd {n : ℕ} (i j k : Fin n) :
    (Equiv.swap i k * Equiv.swap j k) j = i := by
  rw [Equiv.Perm.mul_apply, Equiv.swap_apply_left, Equiv.swap_apply_right]

private lemma swapProd_support {n : ℕ} (i j k : Fin n)
    (hik : i ≠ k) (hjk : j ≠ k) (hij : i ≠ j) :
    (Equiv.swap i k * Equiv.swap j k).support = {i, k, j} := by
  have hnodup : [i, k, j].Nodup := by
    simp only [List.nodup_cons, List.mem_cons, List.not_mem_nil, List.nodup_nil,
      not_false_eq_true, and_true, not_or]
    exact ⟨⟨hik, hij⟩, fun h => hjk h.symm⟩
  rw [Equiv.swap_comm j k]
  exact Equiv.Perm.support_swap_mul_swap hnodup

/-- **THE COMBINATORIAL CORE (now proved).** `centralC2 σ = 1` for a 3-cycle `σ`:
exactly one triple `(k,i,j)` with `i,j < k` has `swap(i,k)·swap(j,k) = σ` — namely `k = max(supp σ)`
with `i = σ⁻¹(k)`, `j = σ(k)` (the other ordering gives `σ⁻¹`). -/
theorem centralC2_apply_threecycle (n : ℕ) (σ : Equiv.Perm (Fin n))
    (hσ : σ.IsThreeCycle) :
    (centralC2 (R := R) n) σ = 1 := by
  classical
  -- basic support data: card 3, the max element m, σ⁻¹ m and σ m in support
  have hcard : σ.support.card = 3 := hσ.card_support
  have hne : σ.support.Nonempty := Finset.card_pos.mp (by rw [hcard]; norm_num)
  set m := σ.support.max' hne with hm
  have hmmem : m ∈ σ.support := Finset.max'_mem _ hne
  have hjm : σ m ≠ m := Equiv.Perm.mem_support.mp hmmem
  have hjmem : σ m ∈ σ.support := Equiv.Perm.apply_mem_support.mpr hmmem
  have himem : σ⁻¹ m ∈ σ.support := by
    rw [← Equiv.Perm.support_inv σ]
    exact Equiv.Perm.apply_mem_support.mpr (by rw [Equiv.Perm.support_inv]; exact hmmem)
  have him : σ⁻¹ m ≠ m := by
    intro h
    apply hjm
    conv_lhs => rw [← h]
    exact σ.apply_inv_self m
  -- σ has order 3, so σ³(m) = m
  have hpow : σ ^ 3 = 1 := by rw [← hσ.orderOf]; exact pow_orderOf_eq_one σ
  have hcube : σ (σ (σ m)) = m := by
    have h3 : (σ ^ 3) m = m := by rw [hpow]; rfl
    rw [pow_succ, pow_succ, pow_one] at h3
    simpa only [Equiv.Perm.mul_apply] using h3
  -- σ⁻¹ m ≠ σ m (else σ² fixes m, so σ³ = 1 forces σ m = m)
  have hij : σ⁻¹ m ≠ σ m := by
    intro h
    apply hjm
    have h2 : σ (σ m) = m := by
      conv_lhs => rw [← h]
      exact σ.apply_inv_self m
    have h4 : σ (σ (σ m)) = σ m := by rw [h2]
    exact h4.symm.trans hcube
  -- strict val-inequalities against the max
  have hilt : (σ⁻¹ m).val < m.val :=
    Fin.lt_def.mp (lt_of_le_of_ne (Finset.le_max' _ _ himem) him)
  have hjlt : (σ m).val < m.val :=
    Fin.lt_def.mp (lt_of_le_of_ne (Finset.le_max' _ _ hjmem) hjm)
  -- the support is exactly {σ⁻¹ m, m, σ m}
  have hsub : ({σ⁻¹ m, m, σ m} : Finset (Fin n)) ⊆ σ.support := by
    intro x hx
    simp only [Finset.mem_insert, Finset.mem_singleton] at hx
    rcases hx with rfl | rfl | rfl
    exacts [himem, hmmem, hjmem]
  have hcard3 : ({σ⁻¹ m, m, σ m} : Finset (Fin n)).card = 3 := by
    have h1 : σ⁻¹ m ∉ ({m, σ m} : Finset (Fin n)) := by
      simp only [Finset.mem_insert, Finset.mem_singleton, not_or]
      exact ⟨him, hij⟩
    have h2 : m ∉ ({σ m} : Finset (Fin n)) := by
      simp only [Finset.mem_singleton]
      exact fun h => hjm h.symm
    rw [Finset.card_insert_of_notMem h1, Finset.card_insert_of_notMem h2,
      Finset.card_singleton]
  have hsupp : σ.support = {σ⁻¹ m, m, σ m} :=
    (Finset.eq_of_subset_of_card_le hsub (by rw [hcard, hcard3])).symm
  -- the product identity: σ = swap(σ⁻¹ m, m) · swap(σ m, m)
  have hprod : Equiv.swap (σ⁻¹ m) m * Equiv.swap (σ m) m = σ := by
    apply Equiv.ext
    intro x
    by_cases hx : x ∈ σ.support
    · rw [hsupp] at hx
      simp only [Finset.mem_insert, Finset.mem_singleton] at hx
      rcases hx with rfl | rfl | rfl
      · rw [swapProd_apply_fst _ _ _ hij him, σ.apply_inv_self]
      · rw [swapProd_apply_top _ _ _ hij hjm]
      · rw [swapProd_apply_snd]
        conv_lhs => rw [← hcube]
        rw [Equiv.Perm.inv_apply_self]
    · have hfix : σ x = x := Equiv.Perm.notMem_support.mp hx
      have hx1 : x ≠ σ m := fun h => hx (h ▸ hjmem)
      have hx2 : x ≠ m := fun h => hx (h ▸ hmmem)
      have hx3 : x ≠ σ⁻¹ m := fun h => hx (h ▸ himem)
      rw [Equiv.Perm.mul_apply, Equiv.swap_apply_of_ne_of_ne hx1 hx2,
        Equiv.swap_apply_of_ne_of_ne hx3 hx2, hfix]
  -- assemble: only k = m contributes, and there it contributes exactly 1
  rw [centralC2_apply]
  refine (Finset.sum_eq_single m ?_ ?_).trans ?_
  · -- k ≠ m ⟹ the pair set is empty (else k would be the max of the support)
    intro k _ hk
    have hzero : (((Finset.univ.filter (fun i : Fin n => i.val < k.val)) ×ˢ
        (Finset.univ.filter (fun i : Fin n => i.val < k.val))).filter
          (fun p => Equiv.swap p.1 k * Equiv.swap p.2 k = σ)).card = 0 := by
      rw [Finset.card_eq_zero, Finset.filter_eq_empty_iff]
      rintro ⟨i', j'⟩ hp
      simp only [Finset.mem_product, Finset.mem_filter, Finset.mem_univ, true_and] at hp
      obtain ⟨hi', hj'⟩ := hp
      intro heq
      have hi'k : i' ≠ k := fun h => by rw [h] at hi'; exact absurd hi' (lt_irrefl _)
      have hj'k : j' ≠ k := fun h => by rw [h] at hj'; exact absurd hj' (lt_irrefl _)
      have hij' : i' ≠ j' := by
        rintro rfl
        rw [Equiv.swap_mul_self] at heq
        have h0 : σ.support.card = 0 := by
          rw [← heq, Equiv.Perm.support_one, Finset.card_empty]
        rw [hcard] at h0
        norm_num at h0
      have hsupp' : σ.support = {i', k, j'} := by
        rw [← heq]; exact swapProd_support i' j' k hi'k hj'k hij'
      have hkm : k ≤ m := Finset.le_max' _ _ (by rw [hsupp']; simp)
      have hmk : m ≤ k := Finset.max'_le _ hne _ (fun x hx => by
        rw [hsupp'] at hx
        simp only [Finset.mem_insert, Finset.mem_singleton] at hx
        rcases hx with rfl | rfl | rfl
        · exact le_of_lt (Fin.lt_def.mpr hi')
        · exact le_refl _
        · exact le_of_lt (Fin.lt_def.mpr hj'))
      exact hk (le_antisymm hkm hmk)
    rw [hzero, Nat.cast_zero]
  · intro h; exact absurd (Finset.mem_univ m) h
  · -- at k = m the pair set is the singleton {(σ⁻¹ m, σ m)}
    have hone : (((Finset.univ.filter (fun i : Fin n => i.val < m.val)) ×ˢ
        (Finset.univ.filter (fun i : Fin n => i.val < m.val))).filter
          (fun p => Equiv.swap p.1 m * Equiv.swap p.2 m = σ)).card = 1 := by
      rw [Finset.card_eq_one]
      refine ⟨(σ⁻¹ m, σ m), ?_⟩
      rw [Finset.eq_singleton_iff_unique_mem]
      refine ⟨?_, ?_⟩
      · simp only [Finset.mem_product, Finset.mem_filter, Finset.mem_univ, true_and]
        exact ⟨⟨hilt, hjlt⟩, hprod⟩
      · rintro ⟨i', j'⟩ hp
        simp only [Finset.mem_product, Finset.mem_filter, Finset.mem_univ, true_and] at hp
        obtain ⟨⟨hi', hj'⟩, heq⟩ := hp
        have hi'm : i' ≠ m := fun h => by rw [h] at hi'; exact absurd hi' (lt_irrefl _)
        have hj'm : j' ≠ m := fun h => by rw [h] at hj'; exact absurd hj' (lt_irrefl _)
        have hij' : i' ≠ j' := by
          rintro rfl
          rw [Equiv.swap_mul_self] at heq
          have h0 : σ.support.card = 0 := by
            rw [← heq, Equiv.Perm.support_one, Finset.card_empty]
          rw [hcard] at h0
          norm_num at h0
        have e1 : σ i' = m := by rw [← heq]; exact swapProd_apply_fst _ _ _ hij' hi'm
        have e2 : σ m = j' := by rw [← heq]; exact swapProd_apply_top _ _ _ hij' hj'm
        have ei : i' = σ⁻¹ m := by rw [← e1, Equiv.Perm.inv_apply_self]
        exact Prod.ext ei e2.symm
    rw [hone, Nat.cast_one]

/-- `IsThreeCycle` is conjugation-invariant. -/
theorem isThreeCycle_conj {n : ℕ} (g σ : Equiv.Perm (Fin n)) :
    (g⁻¹ * σ * g).IsThreeCycle ↔ σ.IsThreeCycle := by
  unfold Equiv.Perm.IsThreeCycle
  rw [show g⁻¹ * σ * g = g⁻¹ * σ * (g⁻¹)⁻¹ by rw [inv_inv], Equiv.Perm.cycleType_conj]

/-- Conjugation preserves being the identity. -/
theorem conj_eq_one_iff {n : ℕ} (g σ : Equiv.Perm (Fin n)) :
    g⁻¹ * σ * g = 1 ↔ σ = 1 := by
  constructor
  · intro h
    have : σ = g * (g⁻¹ * σ * g) * g⁻¹ := by group
    rw [h] at this; simpa using this
  · rintro rfl; group

/-- **THE CLASS-FUNCTION PROPERTY.** The coefficient of `centralC2` is constant on conjugacy
classes, assembled from the three cycle-type cases (`1` / 3-cycle / other). -/
theorem centralC2_classFun (n : ℕ) (g σ : Equiv.Perm (Fin n)) :
    (centralC2 (R := R) n) (g⁻¹ * σ * g) = (centralC2 (R := R) n) σ := by
  by_cases h1 : σ = 1
  · subst h1
    rw [show g⁻¹ * (1 : Equiv.Perm (Fin n)) * g = 1 by group]
  · by_cases h3 : σ.IsThreeCycle
    · rw [centralC2_apply_threecycle n _ ((isThreeCycle_conj g σ).mpr h3),
          centralC2_apply_threecycle n σ h3]
    · rw [centralC2_apply_other n _ (by rwa [Ne, conj_eq_one_iff]) (by rwa [isThreeCycle_conj]),
          centralC2_apply_other n σ h1 h3]

/-! ### Center-reduction helpers (general, sorry-free) -/

/-- Commuting with every `single g 1` ⟹ commuting with everything (linearity). -/
theorem commute_all_of_commute_single {G : Type*} [Monoid G] {S : Type*} [CommSemiring S]
    (z : MonoidAlgebra S G)
    (h : ∀ g : G, z * single g 1 = single g 1 * z) : ∀ x, z * x = x * z := by
  intro x
  induction x using MonoidAlgebra.induction_on with
  | hM g => simpa using h g
  | hadd f₁ f₂ hf₁ hf₂ => rw [mul_add, add_mul, hf₁, hf₂]
  | hsmul r f hf => rw [mul_smul_comm, hf, smul_mul_assoc]

/-- Commuting with every `single g 1` ⟹ in the center. -/
theorem mem_center_of_commute_single {G : Type*} [Monoid G] {S : Type*} [CommSemiring S]
    (z : MonoidAlgebra S G)
    (h : ∀ g : G, z * single g 1 = single g 1 * z) :
    z ∈ Set.center (MonoidAlgebra S G) := by
  rw [Set.mem_center_iff]
  exact ⟨fun a => commute_all_of_commute_single z h a, fun b c => (mul_assoc z b c).symm,
    fun a b => mul_assoc a b z⟩

/-- A class-function coefficient ⟹ commutes with every `single g 1`. -/
theorem commute_single_of_classFun {G : Type*} [Group G] {S : Type*} [CommSemiring S]
    (z : MonoidAlgebra S G)
    (hcf : ∀ g σ : G, z (g⁻¹ * σ * g) = z σ) :
    ∀ g : G, z * single g 1 = single g 1 * z := by
  intro g
  have hconj : single g (1:S) * z * single g⁻¹ (1:S) = z := by
    apply MonoidAlgebra.ext
    intro σ
    rw [mul_single_apply, single_mul_apply, one_mul, mul_one]
    have key : z (g⁻¹ * (σ * g⁻¹⁻¹)) = z (g⁻¹ * σ * g) := by congr 1; group
    rw [key, hcf]
  have hu : single g⁻¹ (1:S) * single g (1:S) = 1 := by
    rw [single_mul_single, inv_mul_cancel, one_mul]; rfl
  calc z * single g (1:S)
      = (single g (1:S) * z * single g⁻¹ (1:S)) * single g (1:S) := by rw [hconj]
    _ = single g (1:S) * z * (single g⁻¹ (1:S) * single g (1:S)) := by rw [mul_assoc, mul_assoc]
    _ = single g (1:S) * z * 1 := by rw [hu]
    _ = single g (1:S) * z := mul_one _

/-- A class-function coefficient ⟹ in the center. -/
theorem mem_center_of_classFun {G : Type*} [Group G] {S : Type*} [CommSemiring S]
    (z : MonoidAlgebra S G)
    (hcf : ∀ g σ : G, z (g⁻¹ * σ * g) = z σ) :
    z ∈ Set.center (MonoidAlgebra S G) :=
  mem_center_of_commute_single z (commute_single_of_classFun z hcf)

/-- **`C₂ ∈ Set.center ℂ[Sₙ]`** (via the class-function property), **sorry-free** — discharges
the centrality hypothesis of `IdentityBWedderburn.identityB_via_wedderburn` outright. -/
theorem centralC2_mem_center (n : ℕ) :
    centralC2 (R := ℂ) n ∈ Set.center (MonoidAlgebra ℂ (Equiv.Perm (Fin n))) :=
  mem_center_of_classFun (centralC2 (R := ℂ) n) (centralC2_classFun (R := ℂ) n)

end QOU.BraidKnot.IdentityBCentrality
