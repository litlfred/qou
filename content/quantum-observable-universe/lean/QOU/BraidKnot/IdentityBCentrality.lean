import Mathlib.Algebra.MonoidAlgebra.Basic
import Mathlib.GroupTheory.Perm.Cycle.Type
import Mathlib.Data.Complex.Basic
import QOU.BraidKnot.RegularRepTrace

/-!
# Centrality of the Jucys–Murphy power sum `C₂`, de-abstracted to one combinatorial core

`IdentityBWedderburn.identityB_via_wedderburn_unconditional` reduces Identity (B) for `ℂ[Sₙ]` to a
*single* classical input: the centrality of the second Jucys–Murphy power sum

  `C₂ = ∑ₖ Xₖ² ∈ Z(ℂ[Sₙ])`,   `Xₖ = ∑_{i<k} (i k)`.

This module **de-abstracts that centrality** into sorry-free plumbing plus the smallest honest core.
The whole reduction — center ⟸ class-function coefficient ⟸ cycle-type case analysis — is machine
checked; the *only* remaining `sorry` is the elementary combinatorial count

  `centralC2_apply_threecycle` : for a 3-cycle `σ`, `C₂ σ = 1`

(each 3-cycle arises from exactly one triple `(k,i,j)` with `i,j<k` and `swap(i,k)·swap(j,k)=σ` —
the `k = max(supp σ)`, unique-ordering fact). This is strictly more atomic than the original
opaque `C₂ ∈ Set.center` citation: the centrality *conclusion* is now **proved** from this single
coefficient value.

Sorry-free here (`[propext, Classical.choice, Quot.sound]`):

* `centralC2_apply` — coefficient of `C₂` at `σ` as `∑ₖ #{(i,j) : i,j<k, swap(i,k)·swap(j,k)=σ}`.
* `swap_prod_classify` — `swap(i,k)·swap(j,k)` is `1` (if `i=j`) or a 3-cycle.
* `centralC2_apply_other` — `σ` neither `1` nor a 3-cycle ⟹ `C₂ σ = 0` (CharZero-free).
* `centralC2_apply_one` — `C₂ 1 = binom(n,2)` (from `RegularRepTrace.centralC2_coeff_one`).
* `isThreeCycle_conj`, `conj_eq_one_iff` — conjugation preserves cycle type / the identity.
* `commute_all_of_commute_single`, `mem_center_of_commute_single`, `commute_single_of_classFun`,
  `mem_center_of_classFun` — general: a class-function coefficient ⟹ central in `MonoidAlgebra`.
* `centralC2_classFun` — the coefficient of `C₂` is a class function (via the three cycle-type
  cases; the 3-cycle case cites `centralC2_apply_threecycle`).
* `centralC2_mem_center` — `C₂ ∈ Set.center ℂ[Sₙ]` (discharges the `IdentityBWedderburn` residual).

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

/-- **THE COMBINATORIAL CORE (single remaining `sorry`).** `centralC2 σ = 1` for a 3-cycle `σ`:
exactly one triple `(k,i,j)` with `i,j < k` has `swap(i,k)·swap(j,k) = σ` — namely `k = max(supp σ)`
with the unique ordering of the two smaller support elements (the other ordering gives `σ⁻¹`). -/
theorem centralC2_apply_threecycle (n : ℕ) (σ : Equiv.Perm (Fin n))
    (hσ : σ.IsThreeCycle) :
    (centralC2 (R := R) n) σ = 1 := by
  -- Ref: [vershik-kerov1977] — Jucys' theorem for the p=2 power sum: `C₂ = binom(n,2)·1 +
  --   (class-sum of all 3-cycles)`, i.e. each 3-cycle has coefficient exactly 1 in `∑ₖ Xₖ²`.
  --   The `k = max(supp σ)` + unique-ordering count; elementary but combinatorially involved.
  sorry

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

/-- **`C₂ ∈ Set.center ℂ[Sₙ]`** (via the class-function property) — discharges the residual
centrality hypothesis of `IdentityBWedderburn.identityB_via_wedderburn`, modulo the single
combinatorial `sorry` `centralC2_apply_threecycle`. -/
theorem centralC2_mem_center (n : ℕ) :
    centralC2 (R := ℂ) n ∈ Set.center (MonoidAlgebra ℂ (Equiv.Perm (Fin n))) :=
  mem_center_of_classFun (centralC2 (R := ℂ) n) (centralC2_classFun (R := ℂ) n)

end QOU.BraidKnot.IdentityBCentrality
