import Mathlib.Algebra.Module.End
import Mathlib.Algebra.Module.Submodule.Ker
import Mathlib.Algebra.Module.Submodule.Range
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Categorical Descent Orthogonal Split and `q`-Jackson UV Proper-Time Regulator

Over an arbitrary commutative ring `R` and ordered field `K` (§7c generic base-ring
discipline, no `ℝ`), this module formalizes:

1. **Categorical `lem:descent` Orthogonal Split (`IsometricDescentSplit`):**
   Given `R`-linear maps `l : A0 →ₗ[R] T` and `r : T →ₗ[R] A0` satisfying `r ∘ l = id`,
   the operators `P0 := l ∘ r` and `Ppos := id - P0` form a complete pair of mutually
   orthogonal idempotent projectors (`P0 * P0 = P0`, `Ppos * Ppos = Ppos`,
   `P0 * Ppos = 0`, `Ppos * P0 = 0`, `P0 + Ppos = 1`) with `ker r = range Ppos`
   (`ker_r_eq_range_Ppos`).
2. **Exact Cottingham–Compton Born + Transient Jet Polarizability Decomposition:**
   For every block-diagonal brane propagator `K : T →ₗ[R] T` commuting with `P0`
   (`K ∘ P0 = P0 ∘ K`), incoming current lift `J_psi : A0 →ₗ[R] T`, and outgoing current
   operator `J_bar : T →ₗ[R] T`, the forward Compton/self-energy matrix element splits
   with **zero** cross-terms and **zero** continuum virtual-photon assumptions:
   `r (J_bar (K (J_psi x))) = r (J_bar (P0 (K (P0 (J_psi x))))) + r (J_bar (Ppos (K (Ppos (J_psi x)))))`
   (`cottingham_compton_split`), where the `k = 0` term reduces purely to the descended
   Born current `r (J_psi x)` and descended propagator `r ∘ K ∘ l` (`elastic_born_reduction`),
   while `Ppos (J_psi x) ∈ ker r` carries the transient `k ≥ 1` jet polarizability tower.
3. **Discrete `q`-Jackson Proper-Time Floor & UV Regulator Bound:**
   Over any strict linear ordered field `K`, for `1 < q` and UV proper-time floor `0 < τ0`,
   every Jackson step `τ_j = τ0 * q^(2j)` satisfies `0 < τ0 ≤ τ_j`
   (`jacksonProperTime_ge_floor`), and the geometric UV regulator partial sums satisfy
   `∑_{j < N} (q⁻¹)^j = (1 - (q⁻¹)^N) / (1 - q⁻¹) < (ℏ_q)⁻¹ = q / (q - 1)` uniformly in `N`
   (`uvRegulatorSum_eq_and_lt_inv_hbarQ`), while diverging above any threshold `M > 0` as
   `q → 1⁺` (`inv_hbarQ_gt_of_sub_lt_inv`).

References: W. Noel Cottingham (1963), Ann. Phys. 25, 424–432; Victor Kac & Pokman Cheung (2002),
*Quantum Calculus*, §19.
-- Ref: [manuscript]
-/

namespace QOU.AlgebraicSubstrate

open BigOperators

/-! ## 1. Isometric Descent Split (`P0` Elastic vs `Ppos` Transient Jet Modes) -/

/-- Categorical descent retract (`l : A0 →ₗ[R] T`, `r : T →ₗ[R] A0`) satisfying `r ∘ l = id`. -/
structure IsometricDescentSplit (R A0 T : Type*) [CommRing R]
    [AddCommGroup A0] [Module R A0] [AddCommGroup T] [Module R T] where
  /-- Isometric / section lift `l : A0 →ₗ[R] T` into the `k = 0` brane sector. -/
  l : A0 →ₗ[R] T
  /-- Conditional expectation / descent retraction `r : T →ₗ[R] A0`. -/
  r : T →ₗ[R] A0
  /-- Retraction axiom `r ∘ l = id_{A0}`. -/
  r_comp_l : r.comp l = LinearMap.id

namespace IsometricDescentSplit

variable {R A0 T : Type*} [CommRing R]
  [AddCommGroup A0] [Module R A0] [AddCommGroup T] [Module R T]
  (d : IsometricDescentSplit R A0 T)

@[simp]
theorem r_apply_l (x : A0) : d.r (d.l x) = x :=
  LinearMap.congr_fun d.r_comp_l x

/-- Ground (`k = 0` elastic) projector `P0 := l ∘ r : T →ₗ[R] T`. -/
def P0 : Module.End R T :=
  d.l.comp d.r

/-- Transient (`k ≥ 1` jet) complementary projector `Ppos := id_T - P0 : T →ₗ[R] T`. -/
def Ppos : Module.End R T :=
  LinearMap.id - d.P0

@[simp]
theorem P0_apply (y : T) : d.P0 y = d.l (d.r y) := rfl

@[simp]
theorem Ppos_apply (y : T) : d.Ppos y = y - d.l (d.r y) := rfl

/-- Completeness of the descent decomposition: `P0 + Ppos = 1` (`LinearMap.id`). -/
theorem P0_add_Ppos : d.P0 + d.Ppos = (1 : Module.End R T) := by
  ext y
  simp [P0, Ppos]

/-- Idempotency of the elastic projector: `P0 * P0 = P0`. -/
theorem P0_mul_P0 : d.P0 * d.P0 = d.P0 := by
  ext y
  simp [Module.End.mul_apply]

/-- Orthogonality `P0 * Ppos = 0`. -/
theorem P0_mul_Ppos : d.P0 * d.Ppos = 0 := by
  ext y
  simp [Module.End.mul_apply]

/-- Orthogonality `Ppos * P0 = 0`. -/
theorem Ppos_mul_P0 : d.Ppos * d.P0 = 0 := by
  ext y
  simp [Module.End.mul_apply]

/-- Idempotency of the transient jet projector: `Ppos * Ppos = Ppos`. -/
theorem Ppos_mul_Ppos : d.Ppos * d.Ppos = d.Ppos := by
  ext y
  simp [Module.End.mul_apply]

/-- `r` absorbs `P0` (`r ∘ P0 = r`) and annihilates `Ppos` (`r ∘ Ppos = 0`). -/
theorem r_comp_P0_and_Ppos : d.r.comp d.P0 = d.r ∧ d.r.comp d.Ppos = 0 := by
  refine ⟨?_, ?_⟩ <;> ext y <;> simp

/-- `P0` fixes `l` (`P0 ∘ l = l`) and `Ppos` annihilates `l` (`Ppos ∘ l = 0`). -/
theorem P0_and_Ppos_comp_l : d.P0.comp d.l = d.l ∧ d.Ppos.comp d.l = 0 := by
  refine ⟨?_, ?_⟩ <;> ext x <;> simp

/-- **Kernel–Range Identification:** `ker r = range Ppos`.
Every transient jet state has zero `k = 0` observable shadow, and conversely every state
annihilated by `r` lies in the image of `Ppos`. -/
theorem ker_r_eq_range_Ppos : LinearMap.ker d.r = LinearMap.range d.Ppos := by
  ext y
  simp only [LinearMap.mem_ker, LinearMap.mem_range, Ppos_apply]
  constructor
  · intro hy
    exact ⟨y, by rw [hy, map_zero, sub_zero]⟩
  · rintro ⟨z, rfl⟩
    rw [map_sub, d.r_apply_l, sub_self]

/-- Complementary range identification: `range l = range P0`. -/
theorem range_l_eq_range_P0 : LinearMap.range d.l = LinearMap.range d.P0 := by
  ext y
  simp only [LinearMap.mem_range, P0_apply]
  constructor
  · rintro ⟨x, rfl⟩
    exact ⟨d.l x, by rw [d.r_apply_l]⟩
  · rintro ⟨z, rfl⟩
    exact ⟨d.r z, rfl⟩

/-! ## 2. Exact Cottingham–Compton Born + Polarizability Split -/

/-- Any operator `K : T →ₗ[R] T` commuting with `P0` also commutes with `Ppos = id - P0`. -/
theorem comm_Ppos_of_comm_P0 {K : T →ₗ[R] T} (hK : K.comp d.P0 = d.P0.comp K) :
    K.comp d.Ppos = d.Ppos.comp K := by
  ext y
  have hy := LinearMap.congr_fun hK y
  simp only [Ppos, LinearMap.comp_apply, LinearMap.sub_apply, LinearMap.id_apply] at hy ⊢
  rw [map_sub, hy]

/-- Off-diagonal propagator cross-terms vanish identically:
`P0 (K (Ppos y)) = 0` and `Ppos (K (P0 y)) = 0`. -/
theorem propagator_cross_terms_zero {K : T →ₗ[R] T} (hK : K.comp d.P0 = d.P0.comp K) (y : T) :
    d.P0 (K (d.Ppos y)) = 0 ∧ d.Ppos (K (d.P0 y)) = 0 := by
  have hKpos := d.comm_Ppos_of_comm_P0 hK
  refine ⟨?_, ?_⟩
  · have h1 := LinearMap.congr_fun hKpos y
    simp only [LinearMap.comp_apply] at h1
    rw [h1]
    exact LinearMap.congr_fun d.P0_mul_Ppos (K y)
  · have h2 := LinearMap.congr_fun hK y
    simp only [LinearMap.comp_apply] at h2
    rw [h2]
    exact LinearMap.congr_fun d.Ppos_mul_P0 (K y)

/-- Diagonal block decomposition of a `P0`-commuting propagator `K`:
`K y = P0 (K (P0 y)) + Ppos (K (Ppos y))`. -/
theorem propagator_block_split {K : T →ₗ[R] T} (hK : K.comp d.P0 = d.P0.comp K) (y : T) :
    K y = d.P0 (K (d.P0 y)) + d.Ppos (K (d.Ppos y)) := by
  obtain ⟨hc1, hc2⟩ := d.propagator_cross_terms_zero hK y
  have hy : y = d.P0 y + d.Ppos y := by
    simp [P0, Ppos]
  calc
    K y = K (d.P0 y + d.Ppos y) := congr_arg K hy
    _ = K (d.P0 y) + K (d.Ppos y) := map_add K _ _
    _ = (d.P0 (K (d.P0 y)) + d.Ppos (K (d.P0 y))) +
          (d.P0 (K (d.Ppos y)) + d.Ppos (K (d.Ppos y))) := by
          have hA : K (d.P0 y) = d.P0 (K (d.P0 y)) + d.Ppos (K (d.P0 y)) := by
            simp [P0, Ppos]
          have hB : K (d.Ppos y) = d.P0 (K (d.Ppos y)) + d.Ppos (K (d.Ppos y)) := by
            simp [P0, Ppos]
          rw [← hA, ← hB]
    _ = d.P0 (K (d.P0 y)) + d.Ppos (K (d.Ppos y)) := by
          rw [hc1, hc2, add_zero, zero_add]

/-- **Exact Cottingham–Compton Orthogonal Split:**
For any `P0`-commuting brane propagator `K : T →ₗ[R] T`, incoming current lift
`J_psi : A0 →ₗ[R] T`, and outgoing current operator `J_bar : T →ₗ[R] T`, the descended
amplitude decomposes cleanly into the `k = 0` elastic Born channel plus the `k ≥ 1`
transient jet polarizability channel:
`r (J_bar (K (J_psi x))) = r (J_bar (P0 (K (P0 (J_psi x))))) + r (J_bar (Ppos (K (Ppos (J_psi x)))))`. -/
theorem cottingham_compton_split {K : T →ₗ[R] T} (hK : K.comp d.P0 = d.P0.comp K)
    (J_bar : T →ₗ[R] T) (J_psi : A0 →ₗ[R] T) (x : A0) :
    d.r (J_bar (K (J_psi x))) =
      d.r (J_bar (d.P0 (K (d.P0 (J_psi x))))) +
        d.r (J_bar (d.Ppos (K (d.Ppos (J_psi x))))) := by
  rw [d.propagator_block_split hK (J_psi x), map_add, map_add]

/-- **Elastic Born Reduction (`k = 0` Channel):**
The `k = 0` intermediate state `P0 (K (P0 (J_psi x)))` depends **solely** on the descended
observable current `r (J_psi x) ∈ A0` and descended propagator `r ∘ K ∘ l`, while the
complementary transient current `Ppos (J_psi x)` lies in `ker r`. -/
theorem elastic_born_reduction (K : T →ₗ[R] T) (J_psi : A0 →ₗ[R] T) (x : A0) :
    d.P0 (K (d.P0 (J_psi x))) = d.l (d.r (K (d.l (d.r (J_psi x))))) ∧
      d.Ppos (J_psi x) ∈ LinearMap.ker d.r := by
  refine ⟨rfl, ?_⟩
  rw [d.ker_r_eq_range_Ppos]
  exact ⟨J_psi x, rfl⟩

end IsometricDescentSplit

/-! ## 3. Discrete `q`-Jackson UV Proper-Time Floor & Geometric Regulator Bound -/

section JacksonUVRegulator

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Discrete `q`-Jackson proper-time grid step `τ_j = τ0 * q^(2 * j)` (`j : ℕ`). -/
def jacksonProperTime (τ0 q : K) (j : ℕ) : K :=
  τ0 * q ^ (2 * j)

/-- Substrate quantum-calculus grain `ℏ_q = 1 - q⁻¹`. -/
def hbarQ (q : K) : K :=
  1 - q⁻¹

/-- Geometric UV regulator partial sum `∑_{j=0}^{N-1} (q⁻¹)^j`. -/
def uvRegulatorSum (q : K) (N : ℕ) : K :=
  ∑ j ∈ Finset.range N, (q⁻¹) ^ j

/-- **UV Proper-Time Floor:** For `1 < q` and `0 < τ0`, every discrete Jackson step satisfies
`0 < τ0 ≤ τ_j = τ0 * q^(2j)` (eliminating the `τ → 0⁺` continuum coincidence singularity). -/
theorem jacksonProperTime_ge_floor {τ0 q : K} (hτ0 : 0 < τ0) (hq : 1 < q) (j : ℕ) :
    τ0 ≤ jacksonProperTime τ0 q j ∧ 0 < jacksonProperTime τ0 q j := by
  unfold jacksonProperTime
  have hpow : (1 : K) ≤ q ^ (2 * j) := one_le_pow₀ (le_of_lt hq)
  have hge : τ0 ≤ τ0 * q ^ (2 * j) := le_mul_of_one_le_right (le_of_lt hτ0) hpow
  exact ⟨hge, lt_of_lt_of_le hτ0 hge⟩

/-- Positivity and reciprocal closed form of `ℏ_q = 1 - q⁻¹` for `1 < q`:
`0 < ℏ_q` and `(ℏ_q)⁻¹ = q / (q - 1)`. -/
theorem hbarQ_pos_and_inv {q : K} (hq : 1 < q) :
    0 < hbarQ q ∧ (hbarQ q)⁻¹ = q / (q - 1) := by
  unfold hbarQ
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hqne : q ≠ 0 := ne_of_gt hq0
  have hsub : 0 < q - 1 := sub_pos.mpr hq
  have hsubne : q - 1 ≠ 0 := ne_of_gt hsub
  have heq : 1 - q⁻¹ = (q - 1) / q := by
    rw [sub_div, div_self hqne, one_div]
  refine ⟨?_, ?_⟩
  · rw [heq]
    exact div_pos hsub hq0
  · rw [heq, inv_div]

/-- Telescoping identity `(1 - x) * ∑_{j < N} x^j = 1 - x^N` over any commutative ring. -/
theorem one_sub_mul_geom_sum {R : Type*} [CommRing R] (x : R) (N : ℕ) :
    (1 - x) * (∑ j ∈ Finset.range N, x ^ j) = 1 - x ^ N := by
  induction N with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, mul_add, ih, pow_succ]
    ring

/-- **Exact Closed Form & Uniform `1 / ℏ_q` UV Bound:**
For `1 < q` and every `N : ℕ`:
1. `uvRegulatorSum q N = (1 - (q⁻¹)^N) / hbarQ q`,
2. `uvRegulatorSum q N < (hbarQ q)⁻¹ = q / (q - 1)`. -/
theorem uvRegulatorSum_eq_and_lt_inv_hbarQ {q : K} (hq : 1 < q) (N : ℕ) :
    uvRegulatorSum q N = (1 - (q⁻¹) ^ N) / hbarQ q ∧
      uvRegulatorSum q N < (hbarQ q)⁻¹ := by
  obtain ⟨hhbar_pos, _⟩ := hbarQ_pos_and_inv hq
  have hhbar_ne : hbarQ q ≠ 0 := ne_of_gt hhbar_pos
  have htele : hbarQ q * uvRegulatorSum q N = 1 - (q⁻¹) ^ N :=
    one_sub_mul_geom_sum q⁻¹ N
  have hclosed : uvRegulatorSum q N = (1 - (q⁻¹) ^ N) / hbarQ q := by
    rw [← htele, mul_div_cancel_left₀ _ hhbar_ne]
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have hqinv_pos : 0 < q⁻¹ := inv_pos.mpr hq0
  have hpow_pos : 0 < (q⁻¹) ^ N := pow_pos hqinv_pos N
  have hnum_lt : 1 - (q⁻¹) ^ N < 1 := sub_lt_self 1 hpow_pos
  have hlt : (1 - (q⁻¹) ^ N) / hbarQ q < 1 / hbarQ q :=
    div_lt_div_of_pos_right hnum_lt hhbar_pos
  rw [one_div] at hlt
  exact ⟨hclosed, hclosed.symm ▸ hlt⟩

/-- **Continuum `q → 1⁺` (`ℏ_q → 0⁺`) Divergence:**
For every positive threshold `0 < M`, whenever `1 < q` and `q - 1 < M⁻¹`, the UV regulator
ceiling `(ℏ_q)⁻¹ = q / (q - 1)` strictly exceeds `M`. -/
theorem inv_hbarQ_gt_of_sub_lt_inv {q M : K} (hM : 0 < M) (hq : 1 < q)
    (hclose : q - 1 < M⁻¹) :
    M < (hbarQ q)⁻¹ := by
  obtain ⟨_, hinv⟩ := hbarQ_pos_and_inv hq
  rw [hinv]
  have hsub_pos : 0 < q - 1 := sub_pos.mpr hq
  have hmul : (q - 1) * M < M⁻¹ * M := mul_lt_mul_of_pos_right hclose hM
  rw [inv_mul_cancel₀ (ne_of_gt hM)] at hmul
  have hlt_q : (q - 1) * M < q := lt_trans hmul hq
  exact (lt_div_iff₀' hsub_pos).mpr hlt_q

end JacksonUVRegulator

end QOU.AlgebraicSubstrate
