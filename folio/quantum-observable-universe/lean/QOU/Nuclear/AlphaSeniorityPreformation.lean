import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Data.Finset.Powerset
import Mathlib.Data.Fintype.Powerset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
# Racah Seniority-0 Coherent-Pair Overlap Algebra for α-Cluster Preformation

Bean `qou-q0gw` (parent epic `qou-myts` / Stability `qou-s028`).

In a single-`j` nuclear shell of magnetic degeneracy `2j + 1 = 2Ω`, the `Ω`
time-reversed Kramers pair orbitals `α ∈ Fin Ω` generate a `2^Ω`-dimensional
pair Fock module `PairSpace Ω R := Finset (Fin Ω) → R` over any commutative ring
`R`. Rather than postulating the quasispin algebra abstractly, this module
constructs the explicit pair creation and annihilation operators on
`PairSpace Ω R` and proves:

1. **Fermionic pair Fock algebra:**
   - `orbitalCreate_sq_zero`, `orbitalAnnihilate_sq_zero`: Pauli exclusion
     `(b†_α)² = 0` and `(b_α)² = 0` on each Kramers orbital.
   - `fockInner_orbitalCreate_adjoint`, `fockInner_pairCreate_adjoint`: exact
     adjointness of `b†_α` and `b_α` (and of the collective Racah operators
     `A† = ∑_α b†_α` and `A = ∑_α b_α`) under the canonical Fock inner product.
   - `pairAnnihilate_pairCreate_comm`: the Racah `𝔰𝔲(2)` quasispin commutator
     `([A, A†] ψ) J = (Ω - 2 |J|) ψ J` across the entire `2^Ω`-dimensional space.

2. **Racah seniority-0 coherent-pair matrix element (`coherent_pair_overlap_sq_*`):**
   On the seniority-`0` (`v = 0`) symmetric `k`-pair state `symPairVec Ω k`
   (`|j^{2k}, v = 0⟩` prior to unit normalization, with squared norm `Nat.choose Ω k`),
   for `1 ≤ k ≤ Ω`:
   - `coherent_pair_overlap_sq_commRing`:
     `⟨u, A† w⟩² = k (Ω + 1 - k) ⟨u, u⟩ ⟨w, w⟩` over any `CommRing R`;
   - `coherent_pair_overlap_sq_field`:
     `⟨u, A† w⟩² / (⟨u, u⟩ ⟨w, w⟩) = k (Ω - k + 1)` over any characteristic-zero
     field `K`.

3. **Coherent vs localized single-orbital pair pickup (`single_orbital_overlap_sq_field`):**
   For any single Kramers orbital `α₀ : Fin Ω`,
   `Ω · ⟨u, b†_{α₀} w⟩ = ⟨u, A† w⟩`, so
   `⟨u, b†_{α₀} w⟩² / (⟨u, u⟩ ⟨w, w⟩) = k (Ω - k + 1) / Ω²`: coherent pairing
   across `Ω` Kramers orbitals enhances squared two-nucleon pickup by `Ω²` over a
   single localized orbital and by `Ω` over an incoherent orbital sum.

4. **Admissible preformation bound & Polonium shell evaluations:**
   - `four_mul_racahWeight_le_sq`: `4 k (Ω - k + 1) ≤ (Ω + 1)²`, so normalizing
     `W(k, Ω) = k (Ω - k + 1)` by `W_cap(Ω) = ((Ω + 1) / 2)²` yields an admissible
     preformation factor `0 < S ≤ 1` (`AlphaPreformationBound`) for all `1 ≤ k ≤ Ω`.
   - `polonium_coherent_vs_literal_ratios`: contrasts Racah seniority-`0` weights
     for `²¹⁰Po` (`1h_{9/2}² ⊗ 3p_{1/2}⁻²`, `W = 5`), `²¹²Po` (`1h_{9/2}² ⊗ 2g_{9/2}²`,
     `W = 25`), and `²¹⁴Po` (`1h_{9/2}² ⊗ 2g_{9/2}⁴`, `W = 40`, ratio `8 / 5` with
     strict Pauli blocking `8 < 10`) against literal uncorrelated `1 / (2Ω)` counting.

Historical credits:
- Giulio Racah (1943), *Theory of Complex Spectra. III*, Phys. Rev. 63, 367
- Arthur K. Kerman (1961), *Pairing forces and nuclear collective motion*, Ann. Phys. 12, 300
- Hans J. Mang (1960), *Calculation of α-transition probabilities*, Phys. Rev. 119, 1069
- Shiro Yoshida (1962), *Note on the enhancement of the L = 0 α-decay due to pairing correlation*, Nucl. Phys. 38, 380

-- Ref: [mayer1949]
-/

set_option autoImplicit false

namespace QOU.Nuclear.AlphaSeniorityPreformation

open scoped BigOperators

/-! ## 1. Explicit Kramers-Pair Fock Space and Racah Quasispin Operators -/

/-- The `2^Ω`-dimensional Kramers-pair Fock module for a single-`j` shell of pair
degeneracy `Ω = (2j + 1) / 2`: basis states are subsets `J : Finset (Fin Ω)` of
occupied time-reversed pair orbitals. -/
abbrev PairSpace (Ω : ℕ) (R : Type*) : Type _ := Finset (Fin Ω) → R

section CommRingFock

variable {Ω : ℕ} {R : Type*} [CommRing R]

/-- Canonical orthonormal-basis bilinear form on `PairSpace Ω R`. -/
def fockInner (φ ψ : PairSpace Ω R) : R :=
  ∑ J : Finset (Fin Ω), φ J * ψ J

/-- Creation operator `b†_α` for Kramers pair orbital `α : Fin Ω`, enforcing Pauli
exclusion (`0` if `α` is already occupied). -/
def orbitalCreate (α : Fin Ω) (ψ : PairSpace Ω R) : PairSpace Ω R :=
  fun J => if α ∈ J then ψ (J.erase α) else 0

/-- Annihilation operator `b_α` for Kramers pair orbital `α : Fin Ω`. -/
def orbitalAnnihilate (α : Fin Ω) (ψ : PairSpace Ω R) : PairSpace Ω R :=
  fun J => if α ∉ J then ψ (insert α J) else 0

/-- Collective Racah seniority-`0` pair creation operator `A† = ∑_α b†_α`. -/
def pairCreate (Ω : ℕ) (ψ : PairSpace Ω R) : PairSpace Ω R :=
  fun J => ∑ α : Fin Ω, orbitalCreate α ψ J

/-- Collective Racah seniority-`0` pair annihilation operator `A = ∑_α b_α`. -/
def pairAnnihilate (Ω : ℕ) (ψ : PairSpace Ω R) : PairSpace Ω R :=
  fun J => ∑ α : Fin Ω, orbitalAnnihilate α ψ J

/-- Equal-amplitude `k`-pair seniority-`0` state vector (`|j^{2k}, v = 0⟩` prior to
dividing by `√(Nat.choose Ω k)`). -/
def symPairVec (Ω k : ℕ) : PairSpace Ω R :=
  fun J => if J.card = k then 1 else 0

/-- Pauli exclusion on each Kramers pair orbital: `(b†_α)² = 0`. -/
theorem orbitalCreate_sq_zero (α : Fin Ω) (ψ : PairSpace Ω R) :
    orbitalCreate α (orbitalCreate α ψ) = 0 := by
  funext J
  simp [orbitalCreate]

/-- Nilpotency of single-orbital pair annihilation: `(b_α)² = 0`. -/
theorem orbitalAnnihilate_sq_zero (α : Fin Ω) (ψ : PairSpace Ω R) :
    orbitalAnnihilate α (orbitalAnnihilate α ψ) = 0 := by
  funext J
  simp [orbitalAnnihilate]

/-- `orbitalCreate α` and `orbitalAnnihilate α` are exact adjoints under `fockInner`. -/
theorem fockInner_orbitalCreate_adjoint (α : Fin Ω) (φ ψ : PairSpace Ω R) :
    fockInner φ (orbitalCreate α ψ) = fockInner (orbitalAnnihilate α φ) ψ := by
  unfold fockInner orbitalCreate orbitalAnnihilate
  have hL :
      (∑ J : Finset (Fin Ω), φ J * (if α ∈ J then ψ (J.erase α) else 0)) =
        ∑ J ∈ Finset.univ.filter (fun J : Finset (Fin Ω) => α ∈ J), φ J * ψ (J.erase α) := by
    rw [Finset.sum_filter]
    refine Finset.sum_congr rfl fun J _ => ?_
    split_ifs <;> ring
  have hR :
      (∑ K : Finset (Fin Ω), (if α ∉ K then φ (insert α K) else 0) * ψ K) =
        ∑ K ∈ Finset.univ.filter (fun K : Finset (Fin Ω) => α ∉ K), φ (insert α K) * ψ K := by
    rw [Finset.sum_filter]
    refine Finset.sum_congr rfl fun K _ => ?_
    split_ifs <;> ring
  rw [hL, hR]
  symm
  refine Finset.sum_bij (fun K _ => insert α K) ?_ ?_ ?_ ?_
  · intro K hK
    simp
  · intro K₁ hK₁ K₂ hK₂ hEq
    have h1 : α ∉ K₁ := (Finset.mem_filter.mp hK₁).2
    have h2 : α ∉ K₂ := (Finset.mem_filter.mp hK₂).2
    have hErase := congrArg (fun S => S.erase α) hEq
    simpa [Finset.erase_insert h1, Finset.erase_insert h2] using hErase
  · intro J hJ
    have hαJ : α ∈ J := (Finset.mem_filter.mp hJ).2
    refine ⟨J.erase α, ?_, Finset.insert_erase hαJ⟩
    simp
  · intro K hK
    have h1 : α ∉ K := (Finset.mem_filter.mp hK).2
    rw [Finset.erase_insert h1]

/-- Collective Racah operators `pairCreate Ω` (`A†`) and `pairAnnihilate Ω` (`A`) are
exact adjoints under `fockInner`. -/
theorem fockInner_pairCreate_adjoint (φ ψ : PairSpace Ω R) :
    fockInner φ (pairCreate Ω ψ) = fockInner (pairAnnihilate Ω φ) ψ := by
  unfold fockInner pairCreate pairAnnihilate
  simp_rw [Finset.mul_sum, Finset.sum_mul]
  rw [Finset.sum_comm]
  have hStep :
      ∀ α : Fin Ω,
        (∑ x : Finset (Fin Ω), φ x * orbitalCreate α ψ x) =
          ∑ x : Finset (Fin Ω), orbitalAnnihilate α φ x * ψ x :=
    fun α => fockInner_orbitalCreate_adjoint α φ ψ
  simp_rw [hStep]
  rw [Finset.sum_comm]

/-- Distinct Kramers pair orbitals commute: `[b_α, b†_β] = 0` for `α ≠ β`. -/
theorem orbital_comm_of_ne {α β : Fin Ω} (hne : α ≠ β) (ψ : PairSpace Ω R)
    (J : Finset (Fin Ω)) :
    orbitalAnnihilate α (orbitalCreate β ψ) J =
      orbitalCreate β (orbitalAnnihilate α ψ) J := by
  unfold orbitalAnnihilate orbitalCreate
  by_cases hα : α ∈ J <;> by_cases hβ : β ∈ J
  · have hαErase : α ∈ J.erase β := Finset.mem_erase.mpr ⟨hne, hα⟩
    simp [hα, hβ, hαErase]
  · simp [hα, hβ]
  · have hαErase : α ∉ J.erase β := by
      intro hmem
      exact hα (Finset.mem_of_mem_erase hmem)
    have hβIns : β ∈ insert α J := Finset.mem_insert_of_mem hβ
    have hSet : (insert α J).erase β = insert α (J.erase β) := by
      ext x
      simp only [Finset.mem_erase, Finset.mem_insert]
      constructor
      · rintro ⟨hxβ, rfl | hxJ⟩
        · exact Or.inl rfl
        · exact Or.inr ⟨hxβ, hxJ⟩
      · rintro (rfl | ⟨hxβ, hxJ⟩)
        · exact ⟨hne, Or.inl rfl⟩
        · exact ⟨hxβ, Or.inr hxJ⟩
    simp [hα, hβ, hαErase, hβIns, hSet]
  · have hβIns : β ∉ insert α J := by
      simp [Finset.mem_insert, hβ, Ne.symm hne]
    simp [hα, hβ, hβIns]

/-- Diagonal Kramers orbital commutator: `[b_α, b†_α] = 1 - n̂_α`, acting as `-1` when
orbital `α` is occupied and `+1` when `α` is empty. -/
theorem orbital_comm_self (α : Fin Ω) (ψ : PairSpace Ω R) (J : Finset (Fin Ω)) :
    orbitalAnnihilate α (orbitalCreate α ψ) J -
      orbitalCreate α (orbitalAnnihilate α ψ) J =
        (if α ∈ J then (-1 : R) else 1) * ψ J := by
  unfold orbitalAnnihilate orbitalCreate
  by_cases hα : α ∈ J
  · have hNotErase : α ∉ J.erase α := Finset.notMem_erase α J
    simp [hα, hNotErase, Finset.insert_erase hα]
  · simp [hα, Finset.erase_insert hα]

/-- **Racah `𝔰𝔲(2)` Quasispin Commutator on `PairSpace Ω R`:**
`[A, A†] = Ω - 2 K̂`, i.e. `(A (A† ψ) - A† (A ψ)) J = (Ω - 2 |J|) ψ J` for every pair
configuration `J ⊆ Fin Ω`. -/
theorem pairAnnihilate_pairCreate_comm (ψ : PairSpace Ω R) (J : Finset (Fin Ω)) :
    pairAnnihilate Ω (pairCreate Ω ψ) J - pairCreate Ω (pairAnnihilate Ω ψ) J =
      ((Ω : R) - 2 * (J.card : R)) * ψ J := by
  have hExpand1 :
      pairAnnihilate Ω (pairCreate Ω ψ) J =
        ∑ α : Fin Ω, ∑ β : Fin Ω, orbitalAnnihilate α (orbitalCreate β ψ) J := by
    unfold pairAnnihilate pairCreate orbitalAnnihilate
    refine Finset.sum_congr rfl fun α _ => ?_
    split_ifs <;> simp
  have hExpand2 :
      pairCreate Ω (pairAnnihilate Ω ψ) J =
        ∑ β : Fin Ω, ∑ α : Fin Ω, orbitalCreate β (orbitalAnnihilate α ψ) J := by
    unfold pairCreate pairAnnihilate orbitalCreate
    refine Finset.sum_congr rfl fun β _ => ?_
    split_ifs <;> simp
  rw [hExpand1, hExpand2, Finset.sum_comm (f := fun β α => orbitalCreate β (orbitalAnnihilate α ψ) J)]
  rw [← Finset.sum_sub_distrib]
  have hDiag :
      ∀ α : Fin Ω,
        (∑ β : Fin Ω, orbitalAnnihilate α (orbitalCreate β ψ) J) -
            (∑ β : Fin Ω, orbitalCreate β (orbitalAnnihilate α ψ) J) =
          (if α ∈ J then (-1 : R) else 1) * ψ J := by
    intro α
    rw [← Finset.sum_sub_distrib]
    rw [Finset.sum_eq_single α]
    · exact orbital_comm_self α ψ J
    · intro β _ hβα
      rw [orbital_comm_of_ne (Ne.symm hβα), sub_self]
    · intro hAbs
      exact False.elim (hAbs (Finset.mem_univ α))
  simp_rw [hDiag, ← Finset.sum_mul]
  congr 1
  have hRewrite :
      ∀ α : Fin Ω, (if α ∈ J then (-1 : R) else 1) = (1 : R) - 2 * (if α ∈ J then (1 : R) else 0) := by
    intro α
    split_ifs <;> ring
  simp_rw [hRewrite, Finset.sum_sub_distrib, ← Finset.mul_sum]
  have hOnes : (∑ _α : Fin Ω, (1 : R)) = (Ω : R) := by
    simp
  have hCard : (∑ α : Fin Ω, (if α ∈ J then (1 : R) else 0)) = (J.card : R) := by
    rw [← Finset.sum_filter]
    have hFilter : Finset.univ.filter (fun α : Fin Ω => α ∈ J) = J := by
      ext α
      simp
    rw [hFilter]
    simp
  rw [hOnes, hCard]

/-! ## 2. Action on Seniority-0 States and Coherent-Pair Overlap Identity -/

/-- `A†` maps `symPairVec Ω m` to `(m + 1) • symPairVec Ω (m + 1)`. -/
theorem pairCreate_symPairVec (m : ℕ) (J : Finset (Fin Ω)) :
    pairCreate Ω (symPairVec Ω m (R := R)) J =
      ((m + 1 : ℕ) : R) * symPairVec Ω (m + 1) J := by
  unfold pairCreate orbitalCreate symPairVec
  have hFilter :
      (∑ α : Fin Ω, if α ∈ J then (if (J.erase α).card = m then (1 : R) else 0) else 0) =
        ∑ α ∈ J, if (J.erase α).card = m then (1 : R) else 0 := by
    rw [← Finset.sum_filter]
    have hEq : Finset.univ.filter (fun α : Fin Ω => α ∈ J) = J := by
      ext α
      simp
    rw [hEq]
  rw [hFilter]
  by_cases hJ : J.card = m + 1
  · have hEach : ∀ α ∈ J, (if (J.erase α).card = m then (1 : R) else 0) = 1 := by
      intro α hα
      have hCard : (J.erase α).card = m := by
        have := Finset.card_erase_of_mem hα
        omega
      simp [hCard]
    rw [Finset.sum_congr rfl hEach]
    simp [hJ]
  · have hEach : ∀ α ∈ J, (if (J.erase α).card = m then (1 : R) else 0) = 0 := by
      intro α hα
      have hPos : 1 ≤ J.card := Finset.one_le_card.mpr ⟨α, hα⟩
      have hCard : (J.erase α).card ≠ m := by
        have := Finset.card_erase_of_mem hα
        omega
      simp [hCard]
    rw [Finset.sum_congr rfl hEach]
    simp [hJ]

/-- For `1 ≤ k ≤ Ω`, `A` maps `symPairVec Ω k` to `(Ω + 1 - k) • symPairVec Ω (k - 1)`. -/
theorem pairAnnihilate_symPairVec {k : ℕ} (hk1 : 1 ≤ k) (hkΩ : k ≤ Ω)
    (J : Finset (Fin Ω)) :
    pairAnnihilate Ω (symPairVec Ω k (R := R)) J =
      ((Ω + 1 - k : ℕ) : R) * symPairVec Ω (k - 1) J := by
  unfold pairAnnihilate orbitalAnnihilate symPairVec
  rw [← Finset.sum_filter]
  by_cases hJ : J.card = k - 1
  · have hEach :
        ∀ α ∈ Finset.univ.filter (fun α : Fin Ω => α ∉ J),
          (if (insert α J).card = k then (1 : R) else 0) = 1 := by
      intro α hα
      have hNotMem : α ∉ J := (Finset.mem_filter.mp hα).2
      have hIns : (insert α J).card = k := by
        rw [Finset.card_insert_of_notMem hNotMem]
        omega
      simp [hIns]
    rw [Finset.sum_congr rfl hEach]
    have hComp : Finset.univ.filter (fun α : Fin Ω => α ∉ J) = Finset.univ \ J := by
      ext α
      simp
    have hComplCard : (Finset.univ \ J).card = Ω + 1 - k := by
      rw [Finset.card_sdiff, Finset.inter_univ, Finset.card_univ, Fintype.card_fin]
      omega
    simp [hJ, hComp, hComplCard]
  · have hEach :
        ∀ α ∈ Finset.univ.filter (fun α : Fin Ω => α ∉ J),
          (if (insert α J).card = k then (1 : R) else 0) = 0 := by
      intro α hα
      have hNotMem : α ∉ J := (Finset.mem_filter.mp hα).2
      have hIns : (insert α J).card ≠ k := by
        rw [Finset.card_insert_of_notMem hNotMem]
        omega
      simp [hIns]
    rw [Finset.sum_congr rfl hEach]
    simp [hJ]

/-- Squared norm of `symPairVec Ω k` equals `Nat.choose Ω k`. -/
theorem fockInner_symPairVec_self (k : ℕ) :
    fockInner (symPairVec Ω k (R := R)) (symPairVec Ω k) = (Nat.choose Ω k : R) := by
  unfold fockInner symPairVec
  have hSq :
      ∀ J : Finset (Fin Ω),
        (if J.card = k then (1 : R) else 0) * (if J.card = k then 1 else 0) =
          if J.card = k then 1 else 0 := by
    intro J
    split_ifs <;> ring
  simp_rw [hSq, ← Finset.sum_filter]
  have hPow :
      Finset.univ.filter (fun J : Finset (Fin Ω) => J.card = k) =
        (Finset.univ : Finset (Fin Ω)).powersetCard k := by
    ext J
    simp [Finset.mem_powersetCard]
  rw [hPow]
  simp [Finset.card_powersetCard]

/-- **Racah Seniority-0 Coherent-Pair Overlap Identity (`CommRing` cross-multiplied form):**
For `1 ≤ k ≤ Ω`, `u = symPairVec Ω k`, and `w = symPairVec Ω (k - 1)`,
`⟨u, A† w⟩² = k (Ω + 1 - k) ⟨u, u⟩ ⟨w, w⟩`. -/
theorem coherent_pair_overlap_sq_commRing {k : ℕ} (hk1 : 1 ≤ k) (hkΩ : k ≤ Ω) :
    let u := symPairVec Ω k (R := R)
    let w := symPairVec Ω (k - 1) (R := R)
    fockInner u (pairCreate Ω w) ^ 2 =
      (k : R) * ((Ω + 1 - k : ℕ) : R) * (fockInner u u * fockInner w w) := by
  intro u w
  have hkEq : k - 1 + 1 = k := by omega
  have hFwd : fockInner u (pairCreate Ω w) = (k : R) * fockInner u u := by
    unfold fockInner
    have hPoint : ∀ J : Finset (Fin Ω), pairCreate Ω w J = (k : R) * u J := by
      intro J
      have h := pairCreate_symPairVec (Ω := Ω) (R := R) (k - 1) J
      simpa [u, w, hkEq] using h
    simp_rw [hPoint]
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun J _ => ?_
    ring
  have hAdj : fockInner u (pairCreate Ω w) = ((Ω + 1 - k : ℕ) : R) * fockInner w w := by
    rw [fockInner_pairCreate_adjoint]
    unfold fockInner
    have hPoint : ∀ J : Finset (Fin Ω), pairAnnihilate Ω u J = ((Ω + 1 - k : ℕ) : R) * w J :=
      fun J => pairAnnihilate_symPairVec (R := R) hk1 hkΩ J
    simp_rw [hPoint]
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun J _ => ?_
    ring
  calc
    fockInner u (pairCreate Ω w) ^ 2
      = fockInner u (pairCreate Ω w) * fockInner u (pairCreate Ω w) := sq _
    _ = ((k : R) * fockInner u u) * (((Ω + 1 - k : ℕ) : R) * fockInner w w) :=
          congrArg₂ (· * ·) hFwd hAdj
    _ = (k : R) * ((Ω + 1 - k : ℕ) : R) * (fockInner u u * fockInner w w) := by ring

/-- Single-orbital matrix element on `symPairVec`: for any fixed Kramers orbital
`α₀ : Fin Ω` and `1 ≤ k`, `⟨u, b†_{α₀} w⟩ = Nat.choose (Ω - 1) (k - 1)`, which is
independent of `α₀`, so `Ω · ⟨u, b†_{α₀} w⟩ = ⟨u, A† w⟩`. -/
theorem omega_mul_orbitalCreate_eq_pairCreate {k : ℕ} (hk1 : 1 ≤ k) (α₀ : Fin Ω) :
    let u := symPairVec Ω k (R := R)
    let w := symPairVec Ω (k - 1) (R := R)
    (Ω : R) * fockInner u (orbitalCreate α₀ w) = fockInner u (pairCreate Ω w) := by
  intro u w
  have hOrb :
      ∀ α : Fin Ω, fockInner u (orbitalCreate α w) = (Nat.choose (Ω - 1) (k - 1) : R) := by
    intro α
    unfold fockInner orbitalCreate u w symPairVec
    have hTerm :
        ∀ J : Finset (Fin Ω),
          (if J.card = k then (1 : R) else 0) *
              (if α ∈ J then (if (J.erase α).card = k - 1 then 1 else 0) else 0) =
            if α ∈ J ∧ (J.erase α).card = k - 1 then 1 else 0 := by
      intro J
      by_cases hα : α ∈ J
      · have hPos : 1 ≤ J.card := Finset.one_le_card.mpr ⟨α, hα⟩
        have hCard := Finset.card_erase_of_mem hα
        by_cases hE : (J.erase α).card = k - 1
        · have hJ : J.card = k := by omega
          simp [hα, hCard, hJ]
        · have hJ : J.card ≠ k := by omega
          have hSubNe : J.card - 1 ≠ k - 1 := by omega
          simp [hα, hSubNe, hJ]
      · simp [hα]
    simp_rw [hTerm, ← Finset.sum_filter]
    have hBij :
        (Finset.univ.filter (fun J : Finset (Fin Ω) => α ∈ J ∧ (J.erase α).card = k - 1)).card =
          ((Finset.univ.erase α).powersetCard (k - 1)).card := by
      refine Finset.card_bij (fun J _ => J.erase α) ?_ ?_ ?_
      · intro J hJ
        have h := (Finset.mem_filter.mp hJ).2
        rw [Finset.mem_powersetCard]
        refine ⟨?_, h.2⟩
        intro x hx
        exact Finset.mem_erase.mpr ⟨(Finset.mem_erase.mp hx).1, Finset.mem_univ x⟩
      · intro J₁ hJ₁ J₂ hJ₂ hEq
        dsimp at hEq
        have h1 := ((Finset.mem_filter.mp hJ₁).2).1
        have h2 := ((Finset.mem_filter.mp hJ₂).2).1
        calc
          J₁ = insert α (J₁.erase α) := (Finset.insert_erase h1).symm
          _ = insert α (J₂.erase α) := by rw [hEq]
          _ = J₂ := Finset.insert_erase h2
      · intro K hK
        rw [Finset.mem_powersetCard] at hK
        have hNot : α ∉ K := fun hmem => (Finset.mem_erase.mp (hK.1 hmem)).1 rfl
        refine ⟨insert α K, ?_, Finset.erase_insert hNot⟩
        simp [Finset.erase_insert hNot, hK.2]
    have hEraseCard : (Finset.univ.erase α : Finset (Fin Ω)).card = Ω - 1 := by
      rw [Finset.card_erase_of_mem (Finset.mem_univ α), Finset.card_univ, Fintype.card_fin]
    simp [hBij, Finset.card_powersetCard, hEraseCard]
  have hSumPair :
      fockInner u (pairCreate Ω w) = ∑ α : Fin Ω, fockInner u (orbitalCreate α w) := by
    unfold fockInner pairCreate
    simp_rw [Finset.mul_sum]
    rw [Finset.sum_comm]
  rw [hSumPair]
  simp_rw [hOrb]
  simp

/-- Pure ring form of the Racah seniority-`0` coherent-pair weight `W(k, Ω) = k (Ω - k + 1)`. -/
def racahCoherentWeight (k Ω : R) : R :=
  k * (Ω - k + 1)

/-- Completion of the square showing `4 W(k, Ω) = (Ω + 1)² - (2 k - (Ω + 1))²` over any
`CommRing R`. -/
theorem four_mul_racahCoherentWeight_eq (k Ω : R) :
    4 * racahCoherentWeight k Ω = (Ω + 1) ^ 2 - (2 * k - (Ω + 1)) ^ 2 := by
  unfold racahCoherentWeight
  ring

end CommRingFock

/-! ## 3. Exact Normalized Overlaps Over Commutative Rings (`Rˣ` Units), `ℚ`, & Ordered Bounds -/

section FieldOverlaps

variable {K : Type*} [CommRing K]

private lemma mul_unit_inv {x : K} (hx : IsUnit x) : x * (↑hx.unit⁻¹ : K) = 1 :=
  calc
    x * (↑hx.unit⁻¹ : K) = (hx.unit : K) * (↑hx.unit⁻¹ : K) :=
      congrArg (· * (↑hx.unit⁻¹ : K)) hx.unit_spec.symm
    _ = 1 := Units.mul_inv hx.unit

/-- **Racah Seniority-0 Coherent-Pair Overlap Theorem:**
On the seniority-`0` states `|j^{2k}, v = 0⟩` (`1 ≤ k ≤ Ω`) over any commutative ring `K` in
which the squared-norm product `⟨u, u⟩ · ⟨w, w⟩` is a unit,
`⟨u, A† w⟩² · (⟨u, u⟩ · ⟨w, w⟩)⁻¹ = k (Ω - k + 1)`. -/
theorem coherent_pair_overlap_sq_field {Ω k : ℕ} (hk1 : 1 ≤ k) (hkΩ : k ≤ Ω)
    (hNorm :
      IsUnit
        (fockInner (symPairVec Ω k (R := K)) (symPairVec Ω k) *
          fockInner (symPairVec Ω (k - 1) (R := K)) (symPairVec Ω (k - 1)))) :
    let u := symPairVec Ω k (R := K)
    let w := symPairVec Ω (k - 1) (R := K)
    fockInner u (pairCreate Ω w) ^ 2 * (↑hNorm.unit⁻¹ : K) =
      racahCoherentWeight (k : K) (Ω : K) := by
  intro u w
  rw [coherent_pair_overlap_sq_commRing hk1 hkΩ, mul_assoc, mul_unit_inv hNorm, mul_one]
  unfold racahCoherentWeight
  have hCast : ((Ω + 1 - k : ℕ) : K) = (Ω : K) - (k : K) + 1 := by
    have hkLe : k ≤ Ω + 1 := by omega
    rw [Nat.cast_sub hkLe, Nat.cast_add, Nat.cast_one]
    ring
  rw [hCast]

/-- **Single-Orbital vs Coherent-Shell Pickup Theorem:**
For any single Kramers orbital `α₀ : Fin Ω` (`1 ≤ k ≤ Ω`), when `⟨u, u⟩ · ⟨w, w⟩` and `Ω` are
units in `K`, the normalized squared pickup matrix element equals `k (Ω - k + 1) · (Ω⁻¹)²`,
smaller than the collective Racah coherent overlap `k (Ω - k + 1)` by exact factor `Ω²`. -/
theorem single_orbital_overlap_sq_field {Ω k : ℕ} (hk1 : 1 ≤ k) (hkΩ : k ≤ Ω)
    (α₀ : Fin Ω)
    (hNorm :
      IsUnit
        (fockInner (symPairVec Ω k (R := K)) (symPairVec Ω k) *
          fockInner (symPairVec Ω (k - 1) (R := K)) (symPairVec Ω (k - 1))))
    (hΩ : IsUnit (Ω : K)) :
    let u := symPairVec Ω k (R := K)
    let w := symPairVec Ω (k - 1) (R := K)
    fockInner u (orbitalCreate α₀ w) ^ 2 * (↑hNorm.unit⁻¹ : K) =
      racahCoherentWeight (k : K) (Ω : K) * (↑hΩ.unit⁻¹ : K) ^ 2 := by
  intro u w
  have hRel := omega_mul_orbitalCreate_eq_pairCreate (Ω := Ω) (R := K) hk1 α₀
  have hMulSq : (Ω : K) ^ 2 * fockInner u (orbitalCreate α₀ w) ^ 2 =
      fockInner u (pairCreate Ω w) ^ 2 := by
    calc
      (Ω : K) ^ 2 * fockInner u (orbitalCreate α₀ w) ^ 2
        = ((Ω : K) * fockInner u (orbitalCreate α₀ w)) ^ 2 := by ring
      _ = fockInner u (pairCreate Ω w) ^ 2 := by rw [hRel]
  have hSq : fockInner u (orbitalCreate α₀ w) ^ 2 =
      fockInner u (pairCreate Ω w) ^ 2 * (↑hΩ.unit⁻¹ : K) ^ 2 := by
    calc
      fockInner u (orbitalCreate α₀ w) ^ 2
        = fockInner u (orbitalCreate α₀ w) ^ 2 * (((Ω : K) * (↑hΩ.unit⁻¹ : K)) ^ 2) := by
            rw [mul_unit_inv hΩ, one_pow, mul_one]
      _ = ((Ω : K) ^ 2 * fockInner u (orbitalCreate α₀ w) ^ 2) * (↑hΩ.unit⁻¹ : K) ^ 2 := by
            rw [mul_pow]; ring
      _ = fockInner u (pairCreate Ω w) ^ 2 * (↑hΩ.unit⁻¹ : K) ^ 2 := by rw [hMulSq]
  calc
    fockInner u (orbitalCreate α₀ w) ^ 2 * (↑hNorm.unit⁻¹ : K)
      = (fockInner u (pairCreate Ω w) ^ 2 * (↑hNorm.unit⁻¹ : K)) * (↑hΩ.unit⁻¹ : K) ^ 2 := by
          rw [hSq]; ring
    _ = racahCoherentWeight (k : K) (Ω : K) * (↑hΩ.unit⁻¹ : K) ^ 2 := by
          rw [coherent_pair_overlap_sq_field hk1 hkΩ hNorm]

/-- Rational half-filling capacity `W_cap(Ω) = ((Ω + 1) / 2)²` bounding `racahCoherentWeight`. -/
def racahCapacity (Ω : ℚ) : ℚ :=
  ((Ω + 1) / 2) ^ 2

/-- Cleared-denominator ring capacity `4 · W_cap(Ω) = (Ω + 1)²` over any commutative ring. -/
def fourRacahCapacity (Ω : K) : K :=
  (Ω + 1) ^ 2

/-- Uncorrelated single-state Mayer–Jensen denominator `1 / (2 Ω) = 1 / (2j + 1)` over `ℚ`. -/
def uncorrelatedSinglePair (Ω : ℚ) : ℚ :=
  1 / (2 * Ω)

/-- **Polonium Chain (`Z = 84`, `N = 126, 128, 130`) Seniority-0 vs Uncorrelated Identities:**
- `1h_{9/2}` (`Ω_p = 5`, `k_p = 1`): `W = 5`;
- `²¹⁰Po` (`N = 126`, `3p_{1/2}` closed `Ω_n = 1, k_n = 1`): `W_p W_n = 5`, uncorrelated `1/20`;
- `²¹²Po` (`N = 128`, `2g_{9/2}²` open `Ω_n = 5, k_n = 1`): `W_p W_n = 25`, uncorrelated `1/100`;
- `²¹⁴Po` (`N = 130`, `2g_{9/2}⁴` open `Ω_n = 5, k_n = 2`): `W_p W_n = 40` (with Pauli
  blocking `W_n = 8 ≠ 2 * 5 = 10`), uncorrelated `1/100`;
- Coherent open-shell pair-addition ratio `W(²¹⁴Po) / W(²¹²Po) = 8 / 5` (vs `1` uncorrelated),
  and `N = 126` jump `W(²¹²Po) / W(²¹⁰Po) = 5` (vs `1 / 5` inverted under literal uncorrelated
  counting). -/
theorem polonium_coherent_vs_literal_ratios :
    let W210 := racahCoherentWeight (1 : ℚ) 5 * racahCoherentWeight (1 : ℚ) 1
    let W212 := racahCoherentWeight (1 : ℚ) 5 * racahCoherentWeight (1 : ℚ) 5
    let W214 := racahCoherentWeight (1 : ℚ) 5 * racahCoherentWeight (2 : ℚ) 5
    let U210 := uncorrelatedSinglePair 5 * uncorrelatedSinglePair 1
    let U212 := uncorrelatedSinglePair 5 * uncorrelatedSinglePair 5
    let U214 := uncorrelatedSinglePair 5 * uncorrelatedSinglePair 5
    W210 = 5 ∧ W212 = 25 ∧ W214 = 40 ∧
      racahCoherentWeight (2 : ℚ) 5 = 8 ∧
      W214 / W212 = 8 / 5 ∧
      W212 / W210 = 5 ∧
      U210 = 1 / 20 ∧ U212 = 1 / 100 ∧ U214 = 1 / 100 ∧
      U214 / U212 = 1 ∧ U212 / U210 = 1 / 5 := by
  unfold racahCoherentWeight uncorrelatedSinglePair
  norm_num

end FieldOverlaps

section OrderedBounds

variable {F : Type*} [CommRing F] [LinearOrder F] [IsStrictOrderedRing F]

/-- Over any strict ordered commutative ring `F`, cleared of the factor `4`,
`0 < 4 · W(k, Ω) ≤ (Ω + 1)²` whenever `0 < k` and `k ≤ Ω`, compatible with
`QOU.Nuclear.AlphaPreformationBound`. -/
theorem racah_normalized_preformation_admissible {k Ω : F} (hk : 0 < k) (hkΩ : k ≤ Ω) :
    0 < 4 * racahCoherentWeight k Ω ∧
      4 * racahCoherentWeight k Ω ≤ fourRacahCapacity Ω := by
  have hWPos : 0 < racahCoherentWeight k Ω := by
    unfold racahCoherentWeight
    have hFactor : 0 < Ω - k + 1 := by linarith
    exact mul_pos hk hFactor
  have h4 : (0 : F) < 4 := by norm_num
  refine ⟨mul_pos h4 hWPos, ?_⟩
  have hFour := four_mul_racahCoherentWeight_eq k Ω
  have hSqNonneg : 0 ≤ (2 * k - (Ω + 1)) ^ 2 := sq_nonneg _
  unfold fourRacahCapacity
  linarith

/-- Note on the naive `W(k, Ω) / (2 Ω)` scaling: at `Ω = 7` (`1i_{13/2}`) and `k = 4`
pairs, `W(4, 7) = 16 > 14 = 2 · 7` over any strict ordered commutative ring (and
`W(4, 7) / (2 · 7) = 16 / 14 > 1` over `ℚ`), proving that `1 / (2 Ω)` is NOT a universal
probability normalization once `Ω ≥ 7`. -/
theorem single_state_racah_exceeds_one_at_omega_seven :
    (2 * 7 : F) < racahCoherentWeight (4 : F) 7 ∧
      (1 : ℚ) < racahCoherentWeight (4 : ℚ) 7 / (2 * 7) := by
  unfold racahCoherentWeight
  constructor <;> norm_num

end OrderedBounds

end QOU.Nuclear.AlphaSeniorityPreformation
