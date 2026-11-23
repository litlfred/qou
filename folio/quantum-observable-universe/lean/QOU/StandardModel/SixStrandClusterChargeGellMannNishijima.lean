import Mathlib.Algebra.Module.End
import Mathlib.Algebra.Module.Pi
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Fintype.Pi
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FinCases

/-!
# 6-Strand `(3 + 3)` Cluster Cartan Braiding, Gell-Mann–Nishijima Charge, and Derived Quark Charges

Over an arbitrary commutative ring `R`, characteristic-zero field `K`, and strict ordered
field (§7c generic base-ring discipline, zero `ℝ` and zero fitted constants), this module
formalizes five coupled structural results for two-baryon `(3 + 3)` strand configurations:

1. **6-Strand `U_q(sl₂)` Hecke Braiding & Cluster Cartan Commutant Structure:**
   On the 64-dimensional 6-strand state space `Strand6 = (Fin 6 → Bool)` (`Cluster A = {0,1,2}`,
   `Cluster B = {3,4,5}`), the five adjacent Jimbo–Hecke braid operators `R₀, R₁, R₂, R₃, R₄`
   satisfy the Hecke quadratic (`heckeBraid6_sq`), braid (`heckeBraid6_braid`), and far
   commutation (`heckeBraid6_far_comm`) relations. The single-cluster modular Cartan operator
   `F_A` commutes with internal braids `R₀, R₁, R₃, R₄` (`clusterACartan_comm_internal`), the total
   Cartan `F_A * F_B` commutes with **all five** braids including the inter-cluster crossing
   `R₂` (`clusterABCartan_comm_all_five`), whereas `F_A` **fails to commute** with `R₂` whenever `q² ≠ 1`
   (`clusterACartan_not_comm_intercluster`).
2. **Gell-Mann–Nishijima vs Pure-`T₃` Neutron Neutrality & `q = 1` Vanishing:**
   The pure modular Cartan defect `Δν(q, m) = (q^m - q^(-m)) / 2` vanishes identically at
   `q = 1` (`deltaNu_at_one_vanishes`, closing the `q = 1` static-charge obstruction), but
   its two-body product `Δν_A ⊗ Δν_B` takes the nonzero value `((q⁻¹ - q)^2) / 4 ≠ 0` on
   `|nn⟩` whenever `q² ≠ 1` and equates `|pp⟩` with `|nn⟩` (`pureDeltaNu_nn_ne_zero_and_pp_eq_nn`).
   Adding hypercharge via `Q_EM = T₃ + Y / 2` (and its `q`-deformed modular counterpart
   `qModGMN`) yields `(+1, 0, -1, 0)` on `(p, n, p̄, n̄)`, vanishes on `(n, n)` and `(p, n)`,
   separates `|pp⟩` (`+1`) from `|nn⟩` (`0`), is `C`-odd on single bodies, and makes `Q_A Q_B`
   `CPT`-even (`gmn_charge_properties`, `qModGMN_properties`).
3. **Unique Derived Quark Charges `(q_u, q_d) = (2/3, -1/3)`:**
   For `N_c = 3` colour strands, modular Cartan isospin splitting `q_u - q_d = 1` together
   with either `udd` baryon neutrality `q_u + 2 * q_d = 0` or chiral/mixed anomaly
   cancellation `3 * (q_u + q_d) + (-1) = 0` (`udd_neutral_iff_anomaly_cancel`) has the
   **unique** solution `q_u = 2/3` and `q_d = -1/3` (`derived_quark_charges_unique`).
4. **Unconditional Electrostatic Negative-Sign Obstruction on `m_n - m_p`:**
   At `(q_u, q_d) = (2/3, -1/3)`, composite charge-square (`-1`), constituent quark
   self-squares (`-1/3`), and constituent pairwise products (`0` for `p`, `-1/3` for `n`,
   difference `-1/3`) are **all strictly negative** (`electrostatic_three_functionals_negative`),
   so no non-negative linear combination of repulsive electrostatic functionals can contribute
   positively to `m_n - m_p` (`electrostatic_positive_cone_nogo`).
5. **Normal-Ordered `A`-Cluster Nuclear Coulomb Law (`Z(Z - 1)` & `³H`–`³He` Mirror Split):**
   For any `{0, 1}`-valued nucleon charge assignment `Q : ι → R` with total proton charge
   `Z = ∑ i, Q i`, normal-ordering removes 1-body self-energies identically:
   `(∑ i, Q i)² - ∑ i, (Q i)² = Z * (Z - 1)` (`normalOrderedCoulomb_eq_Z_mul_Z_sub_one`),
   yielding `0` for `Z ∈ {0, 1}` (`nn`, `²H`, `³H`), `2` for `Z = 2` (`³He`, `⁴He`), and
   strict mirror splitting `E_C(³He) - E_C(³H) = 2 * α_C > 0` (`helion_triton_coulomb_split_pos`).

References: Michio Jimbo (1986), Lett. Math. Phys. 11, 247–252; Murray Gell-Mann (1956),
Nuovo Cimento 4, 848–866; Kazuhiko Nishijima (1955).
-- Ref: [jimbo1986]
-/

namespace QOU.StandardModel

open BigOperators

/-! ## 1. 6-Strand `(3 + 3)` Hecke Braiding and Cluster Cartan Commutant Structure -/

/-- Six-strand spinor/isospin configuration space (`true = u`, `false = d`) of cardinality
`2^6 = 64`, partitioned into `Cluster A = {0, 1, 2}` and `Cluster B = {3, 4, 5}`. -/
abbrev Strand6 : Type := Fin 6 → Bool

theorem card_strand6 : Fintype.card Strand6 = 64 := by
  simp

/-- Left strand index `i ∈ {0,1,2,3,4}` of adjacent crossing `i`. -/
def strandL (i : Fin 5) : Fin 6 := ⟨i.val, by omega⟩

/-- Right strand index `i + 1 ∈ {1,2,3,4,5}` of adjacent crossing `i`. -/
def strandR (i : Fin 5) : Fin 6 := ⟨i.val + 1, by omega⟩

/-- Overwrite strands `(i, i + 1)` of `s : Strand6` with `(a, b : Bool)`. -/
def set2 (i : Fin 5) (s : Strand6) (a b : Bool) : Strand6 :=
  fun k =>
    if k = strandL i then a
    else if k = strandR i then b
    else s k

/-- Overwrite three consecutive strands `(j, j + 1, j + 2)` of `s : Strand6` with `(a, b, c)`. -/
def set3 (j : Fin 4) (s : Strand6) (a b c : Bool) : Strand6 :=
  fun k =>
    if k = ⟨j.val, by omega⟩ then a
    else if k = ⟨j.val + 1, by omega⟩ then b
    else if k = ⟨j.val + 2, by omega⟩ then c
    else s k

theorem set2_self (i : Fin 5) (s : Strand6) :
    set2 i s (s (strandL i)) (s (strandR i)) = s := by
  ext k
  unfold set2
  by_cases hL : k = strandL i
  · subst hL; simp
  · by_cases hR : k = strandR i
    · subst hR; simp [hL]
    · simp [hL, hR]

theorem set2_idem (i : Fin 5) (s : Strand6) (a b c d : Bool) :
    set2 i (set2 i s a b) c d = set2 i s c d := by
  ext k
  unfold set2
  by_cases hL : k = strandL i
  · simp [hL]
  · by_cases hR : k = strandR i
    · simp [hR]
    · simp [hL, hR]

theorem set2_apply_L (i : Fin 5) (s : Strand6) (a b : Bool) :
    set2 i s a b (strandL i) = a := by
  simp [set2]

theorem set2_apply_R (i : Fin 5) (s : Strand6) (a b : Bool) :
    set2 i s a b (strandR i) = b := by
  have hne : strandR i ≠ strandL i := by
    intro h
    have hv := congr_arg Fin.val h
    simp [strandL, strandR] at hv
  simp [set2, hne]

theorem set3_self (j : Fin 4) (s : Strand6) :
    set3 j s (s ⟨j.val, by omega⟩) (s ⟨j.val + 1, by omega⟩) (s ⟨j.val + 2, by omega⟩) = s := by
  ext k
  fin_cases j <;> fin_cases k <;> rfl

theorem set2_left_set3 (j : Fin 4) (s : Strand6) (a b c a' b' : Bool) :
    set2 ⟨j.val, by omega⟩ (set3 j s a b c) a' b' = set3 j s a' b' c := by
  ext k
  fin_cases j <;> fin_cases k <;> rfl

theorem set2_right_set3 (j : Fin 4) (s : Strand6) (a b c b' c' : Bool) :
    set2 ⟨j.val + 1, by omega⟩ (set3 j s a b c) b' c' = set3 j s a b' c' := by
  ext k
  fin_cases j <;> fin_cases k <;> rfl

section SixStrandOperators

variable {R : Type*} [CommRing R]

/-- Balanced Jimbo `U_q(sl₂)` Hecke braid operator `R_i` (`i : Fin 5`) on the 64-dimensional
6-strand module `Strand6 → R`. -/
def heckeBraid6 (q : Rˣ) (i : Fin 5) : Module.End R (Strand6 → R) where
  toFun ψ s :=
    match s (strandL i), s (strandR i) with
    | true, true => (q : R) * ψ s
    | false, false => (q : R) * ψ s
    | true, false =>
        ψ (set2 i s false true) + ((q : R) - (((q⁻¹ : Rˣ) : R))) * ψ s
    | false, true =>
        ψ (set2 i s true false)
  map_add' ψ₁ ψ₂ := by
    ext s
    simp only [Pi.add_apply]
    cases s (strandL i) <;> cases s (strandR i) <;> simp <;> ring
  map_smul' r ψ := by
    ext s
    simp only [Pi.smul_apply, smul_eq_mul, RingHom.id_apply]
    cases s (strandL i) <;> cases s (strandR i) <;> simp <;> ring

/-- **6-Strand Hecke Quadratic Relation:**
`R_i² = (q - q⁻¹) • R_i + 1` for all `i ∈ {0, 1, 2, 3, 4}`. -/
theorem heckeBraid6_sq (q : Rˣ) (i : Fin 5) :
    heckeBraid6 (R := R) q i * heckeBraid6 q i =
      ((q : R) - (((q⁻¹ : Rˣ) : R))) • heckeBraid6 q i + 1 := by
  apply LinearMap.ext
  intro ψ
  funext s
  have hs := (set2_self i s).symm
  generalize s (strandL i) = a, s (strandR i) = b at hs
  rw [hs]
  have hqi : (q : R) * (((q⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv q
  cases a <;> cases b <;>
    simp only [Module.End.mul_apply, LinearMap.add_apply, LinearMap.smul_apply,
      Module.End.one_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul, heckeBraid6,
      LinearMap.coe_mk, AddHom.coe_mk, set2_apply_L, set2_apply_R, set2_idem]
  · linear_combination ψ (set2 i s false false) * hqi
  · ring
  · ring
  · linear_combination ψ (set2 i s true true) * hqi

/-- **6-Strand Braid Relation (`R_j R_{j+1} R_j = R_{j+1} R_j R_{j+1}`):**
Holds for all four adjacent generator pairs `(0,1), (1,2), (2,3), (3,4)`. -/
theorem heckeBraid6_braid (q : Rˣ) (j : Fin 4) :
    let i₁ : Fin 5 := ⟨j.val, by omega⟩
    let i₂ : Fin 5 := ⟨j.val + 1, by omega⟩
    heckeBraid6 (R := R) q i₁ * heckeBraid6 q i₂ * heckeBraid6 q i₁ =
      heckeBraid6 q i₂ * heckeBraid6 q i₁ * heckeBraid6 q i₂ := by
  intro i₁ i₂
  apply LinearMap.ext
  intro ψ
  funext s
  have hs := (set3_self j s).symm
  generalize s ⟨j.val, by omega⟩ = a, s ⟨j.val + 1, by omega⟩ = b,
    s ⟨j.val + 2, by omega⟩ = c at hs
  rw [hs]
  have hL1 : ∀ x y z : Bool, set3 j s x y z (strandL i₁) = x := by
    intro x y z; fin_cases j <;> rfl
  have hR1 : ∀ x y z : Bool, set3 j s x y z (strandR i₁) = y := by
    intro x y z; fin_cases j <;> rfl
  have hL2 : ∀ x y z : Bool, set3 j s x y z (strandL i₂) = y := by
    intro x y z; fin_cases j <;> rfl
  have hR2 : ∀ x y z : Bool, set3 j s x y z (strandR i₂) = z := by
    intro x y z; fin_cases j <;> rfl
  have hqi : (q : R) * (((q⁻¹ : Rˣ) : R)) = 1 := Units.mul_inv q
  have hqi2 : (q : R) * (((q⁻¹ : Rˣ) : R)) ^ 2 = (((q⁻¹ : Rˣ) : R)) := by
    rw [sq, ← mul_assoc, Units.mul_inv, one_mul]
  have hq2i : (q : R) ^ 2 * (((q⁻¹ : Rˣ) : R)) = (q : R) := by
    rw [sq, mul_assoc, Units.mul_inv, mul_one]
  cases a <;> cases b <;> cases c <;>
    ((simp only [Module.End.mul_apply, heckeBraid6, LinearMap.coe_mk, AddHom.coe_mk,
      i₁, i₂, hL1, hR1, hL2, hR2, set2_left_set3, set2_right_set3]);
      (try ring_nf);
      (try simp only [hqi, hqi2, hq2i]);
      (try ring))

/-- **6-Strand Far Commutation (`R_i R_j = R_j R_i` for `j ≥ i + 2`):** -/
theorem heckeBraid6_far_comm (q : Rˣ) (i j : Fin 5) (hij : i.val + 2 ≤ j.val) :
    heckeBraid6 (R := R) q i * heckeBraid6 q j =
      heckeBraid6 q j * heckeBraid6 q i := by
  have hcomm_set2 : ∀ (s : Strand6) (a b c d : Bool),
      set2 i (set2 j s c d) a b = set2 j (set2 i s a b) c d := by
    intro s a b c d
    ext k
    fin_cases i <;> fin_cases j <;> simp at hij <;> fin_cases k <;> rfl
  have hj_on_i : ∀ (s : Strand6) (c d : Bool),
      set2 j s c d (strandL i) = s (strandL i) ∧
        set2 j s c d (strandR i) = s (strandR i) := by
    intro s c d
    fin_cases i <;> fin_cases j <;> simp at hij <;> exact ⟨rfl, rfl⟩
  have hi_on_j : ∀ (s : Strand6) (a b : Bool),
      set2 i s a b (strandL j) = s (strandL j) ∧
        set2 i s a b (strandR j) = s (strandR j) := by
    intro s a b
    fin_cases i <;> fin_cases j <;> simp at hij <;> exact ⟨rfl, rfl⟩
  apply LinearMap.ext
  intro ψ
  funext s
  simp only [Module.End.mul_apply, heckeBraid6, LinearMap.coe_mk, AddHom.coe_mk]
  obtain ⟨hjiL, hjiR⟩ := hj_on_i s false true
  obtain ⟨hjiL', hjiR'⟩ := hj_on_i s true false
  obtain ⟨hijL, hijR⟩ := hi_on_j s false true
  obtain ⟨hijL', hijR'⟩ := hi_on_j s true false
  cases hiL : s (strandL i) <;> cases hiR : s (strandR i) <;>
    cases hjL : s (strandL j) <;> cases hjR : s (strandR j) <;>
    ((try simp only [hjiL, hjiR, hjiL', hjiR', hijL, hijR, hijL', hijR', hcomm_set2]);
      (try simp only [hiL, hiR, hjL, hjR]);
      try ring)

/-- Single-strand `2 T₃` weight (`true ↦ +1`, `false ↦ -1`). -/
def strandTwoT3 (b : Bool) : ℤ :=
  if b then 1 else -1

/-- Cluster-`A` (`{0, 1, 2}`) additive `2 T₃` weight. -/
def clusterATwoT3 (s : Strand6) : ℤ :=
  strandTwoT3 (s 0) + strandTwoT3 (s 1) + strandTwoT3 (s 2)

/-- Cluster-`B` (`{3, 4, 5}`) additive `2 T₃` weight. -/
def clusterBTwoT3 (s : Strand6) : ℤ :=
  strandTwoT3 (s 3) + strandTwoT3 (s 4) + strandTwoT3 (s 5)

/-- Diagonal operator `(D_w ψ)(s) = q^(w s) * ψ(s)` for any integer weight `w : Strand6 → ℤ`. -/
def diagQWeight (q : Rˣ) (w : Strand6 → ℤ) : Module.End R (Strand6 → R) where
  toFun ψ s := ((q ^ w s : Rˣ) : R) * ψ s
  map_add' ψ₁ ψ₂ := by ext s; simp [mul_add]
  map_smul' r ψ := by ext s; simp [mul_left_comm]

/-- Cluster-`A` modular Cartan operator `F_A = diag(q^(2 T₃^{(A)}))`. -/
def clusterACartan (q : Rˣ) : Module.End R (Strand6 → R) :=
  diagQWeight q clusterATwoT3

/-- Cluster-`B` modular Cartan operator `F_B = diag(q^(2 T₃^{(B)}))`. -/
def clusterBCartan (q : Rˣ) : Module.End R (Strand6 → R) :=
  diagQWeight q clusterBTwoT3

/-- General criterion: `diagQWeight q w` commutes with `heckeBraid6 q i` whenever swapping
opposite booleans at `(i, i + 1)` preserves `w`. -/
theorem diagQWeight_comm_heckeBraid6 (q : Rˣ) (w : Strand6 → ℤ) (i : Fin 5)
    (hw : ∀ s : Strand6, w (set2 i s false true) = w (set2 i s true false)) :
    diagQWeight (R := R) q w * heckeBraid6 q i =
      heckeBraid6 q i * diagQWeight q w := by
  apply LinearMap.ext
  intro ψ
  funext s
  have hw_tf : s (strandL i) = true → s (strandR i) = false →
      w (set2 i s false true) = w s := by
    intro hL hR
    calc
      w (set2 i s false true) = w (set2 i s true false) := hw s
      _ = w (set2 i s (s (strandL i)) (s (strandR i))) := by rw [hL, hR]
      _ = w s := by rw [set2_self]
  have hw_ft : s (strandL i) = false → s (strandR i) = true →
      w (set2 i s true false) = w s := by
    intro hL hR
    calc
      w (set2 i s true false) = w (set2 i s false true) := (hw s).symm
      _ = w (set2 i s (s (strandL i)) (s (strandR i))) := by rw [hL, hR]
      _ = w s := by rw [set2_self]
  simp only [Module.End.mul_apply, diagQWeight, heckeBraid6, LinearMap.coe_mk, AddHom.coe_mk]
  cases hL : s (strandL i) <;> cases hR : s (strandR i)
  · simp [mul_left_comm]
  · simp [hw_ft hL hR]
  · simp [hw_tf hL hR]; ring
  · simp [mul_left_comm]

/-- **1. `F_A` and `F_B` Commute with All Intra-Cluster Braids (`R₀, R₁, R₃, R₄`):** -/
theorem clusterACartan_comm_internal (q : Rˣ) :
    clusterACartan (R := R) q * heckeBraid6 q 0 = heckeBraid6 q 0 * clusterACartan q ∧
    clusterACartan (R := R) q * heckeBraid6 q 1 = heckeBraid6 q 1 * clusterACartan q ∧
    clusterACartan (R := R) q * heckeBraid6 q 3 = heckeBraid6 q 3 * clusterACartan q ∧
    clusterACartan (R := R) q * heckeBraid6 q 4 = heckeBraid6 q 4 * clusterACartan q := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    (apply diagQWeight_comm_heckeBraid6;
      intro s;
      simp [clusterATwoT3, set2, strandL, strandR, strandTwoT3];
      try omega)

theorem clusterBCartan_comm_internal (q : Rˣ) :
    clusterBCartan (R := R) q * heckeBraid6 q 0 = heckeBraid6 q 0 * clusterBCartan q ∧
    clusterBCartan (R := R) q * heckeBraid6 q 1 = heckeBraid6 q 1 * clusterBCartan q ∧
    clusterBCartan (R := R) q * heckeBraid6 q 3 = heckeBraid6 q 3 * clusterBCartan q ∧
    clusterBCartan (R := R) q * heckeBraid6 q 4 = heckeBraid6 q 4 * clusterBCartan q := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    (apply diagQWeight_comm_heckeBraid6;
      intro s;
      simp [clusterBTwoT3, set2, strandL, strandR, strandTwoT3];
      try omega)

/-- Product of `F_A` and `F_B` equals the total 6-strand Cartan `diagQWeight q (w_A + w_B)`. -/
theorem clusterACartan_mul_clusterBCartan (q : Rˣ) :
    clusterACartan (R := R) q * clusterBCartan q =
      diagQWeight q (fun s => clusterATwoT3 s + clusterBTwoT3 s) := by
  apply LinearMap.ext
  intro ψ
  funext s
  simp only [Module.End.mul_apply, clusterACartan, clusterBCartan, diagQWeight,
    LinearMap.coe_mk, AddHom.coe_mk, zpow_add, Units.val_mul, mul_assoc]

/-- **2. Total `F_A * F_B` Commutes with ALL FIVE 6-Strand Braids (`R₀, R₁, R₂, R₃, R₄`):**
Includes the inter-cluster quark-exchange crossing `R₂` between strand 2 and strand 3. -/
theorem clusterABCartan_comm_all_five (q : Rˣ) (i : Fin 5) :
    (clusterACartan (R := R) q * clusterBCartan q) * heckeBraid6 q i =
      heckeBraid6 q i * (clusterACartan q * clusterBCartan q) := by
  rw [clusterACartan_mul_clusterBCartan]
  apply diagQWeight_comm_heckeBraid6
  intro s
  fin_cases i <;>
    (simp [clusterATwoT3, clusterBTwoT3, set2, strandL, strandR, strandTwoT3];
      try omega)

/-- **3. Single-Cluster `F_A` Does NOT Commute with Inter-Cluster Crossing `R₂` (`q² ≠ 1`):**
Quark exchange across the `(2, 3)` cluster boundary transfers `Δ(2 T₃^{(A)}) = ±2` between
Cluster `A` and Cluster `B`, breaking single-cluster Cartan invariance whenever `q² ≠ 1`. -/
theorem clusterACartan_not_comm_intercluster [Nontrivial R] {q : Rˣ}
    (hq2 : (q : R) ^ 2 ≠ 1) :
    clusterACartan (R := R) q * heckeBraid6 q 2 ≠
      heckeBraid6 q 2 * clusterACartan q := by
  intro heq
  let s₀ : Strand6 := ![true, true, true, false, false, false]
  let t₀ : Strand6 := set2 2 s₀ false true
  let ψ₀ : Strand6 → R := fun s => if s = t₀ then 1 else 0
  have heval := congr_fun (LinearMap.congr_fun heq ψ₀) s₀
  have hs0_ne_t0 : s₀ ≠ t₀ := by
    intro h
    have h2 := congr_fun h 2
    simp [s₀, t₀, set2, strandL] at h2
  have hsL : s₀ (strandL 2) = true := rfl
  have hsR : s₀ (strandR 2) = false := rfl
  have hw_s0 : clusterATwoT3 s₀ = 3 := rfl
  have hw_t0 : clusterATwoT3 t₀ = 1 := rfl
  simp only [Module.End.mul_apply, clusterACartan, diagQWeight, heckeBraid6,
    LinearMap.coe_mk, AddHom.coe_mk, hsL, hsR, hw_s0, hw_t0, ψ₀,
    show set2 2 s₀ false true = t₀ from rfl, ↓reduceIte, hs0_ne_t0,
    mul_zero, add_zero, mul_one, zpow_one] at heval
  have hq3 : ((q ^ (3 : ℤ) : Rˣ) : R) = (q : R) ^ 2 * (q : R) := by
    change ((q ^ (3 : ℕ) : Rˣ) : R) = (q : R) ^ 2 * (q : R)
    rw [Units.val_pow_eq_pow_val]
    ring
  rw [hq3] at heval
  apply hq2
  calc
    (q : R) ^ 2 = ((q : R) ^ 2 * (q : R)) * (((q⁻¹ : Rˣ) : R)) := by
      rw [mul_assoc, Units.mul_inv, mul_one]
    _ = (q : R) * (((q⁻¹ : Rˣ) : R)) := by rw [heval]
    _ = 1 := Units.mul_inv q

end SixStrandOperators

/-! ## 2. Gell-Mann–Nishijima vs Pure-`T₃` Neutron Neutrality and `q = 1` Vanishing -/

/-- Nucleon / antinucleon quartet `(p, n, p̄, n̄)`. -/
inductive BaryonState : Type
  | proton
  | neutron
  | antiproton
  | antineutron
  deriving DecidableEq

/-- Charge conjugation `C` on the nucleon/antinucleon quartet. -/
def BaryonState.cConj : BaryonState → BaryonState
  | .proton => .antiproton
  | .neutron => .antineutron
  | .antiproton => .proton
  | .antineutron => .neutron

/-- Twice the third component of isospin `2 T₃ ∈ {+1, -1}`. -/
def BaryonState.twoT3 : BaryonState → ℤ
  | .proton => 1
  | .neutron => -1
  | .antiproton => -1
  | .antineutron => 1

/-- Baryon hypercharge `Y = B ∈ {+1, -1}` on the nucleon/antinucleon quartet. -/
def BaryonState.hypercharge : BaryonState → ℤ
  | .proton => 1
  | .neutron => 1
  | .antiproton => -1
  | .antineutron => -1

section GellMannNishijima

variable {K : Type*} [Field K] [CharZero K]

/-- Modular Cartan defect `Δν(q, m) = (q^m - q^(-m)) / 2` (`m : ℤ`). -/
def deltaNu (q : Kˣ) (m : ℤ) : K :=
  (((q ^ m : Kˣ) : K) - (((q ^ (-m) : Kˣ) : K))) / 2

omit [CharZero K] in
/-- **Modular Defect Vanishes Identically at `q = 1` (`qou-az9l` `m_p = m_n` at `q = 1`):**
At `q = 1`, `Δν(1, m) = 0`, `(Δν(1, m))² = 0`, and `Δν(1, m₁) * Δν(1, m₂) = 0` for all `m`. -/
theorem deltaNu_at_one_vanishes (m m₁ m₂ : ℤ) :
    deltaNu (1 : Kˣ) m = 0 ∧
    (deltaNu (1 : Kˣ) m) ^ 2 = 0 ∧
    deltaNu (1 : Kˣ) m₁ * deltaNu (1 : Kˣ) m₂ = 0 := by
  have h0 : ∀ k : ℤ, deltaNu (1 : Kˣ) k = 0 := by
    intro k
    simp [deltaNu]
  simp [h0]

/-- **Pure-`T₃` / `Δν_A ⊗ Δν_B` Refutation on Two Neutrons (`|nn⟩ ≠ 0` & `pp = nn`):**
1. On `(n, n)`, `Δν(q, -1) * Δν(q, -1) = ((q⁻¹ - q)²) / 4`, which is **nonzero** whenever
   `(q : K)² ≠ 1` (falsifying pure-`T₃` as electric charge!).
2. Pure `Δν_A ⊗ Δν_B` gives identical eigenvalues on `(p, p)` and `(n, n)` (`pp = nn`
   pure-`H_6(q)` charge blindness). -/
theorem pureDeltaNu_nn_ne_zero_and_pp_eq_nn {q : Kˣ} (hq2 : (q : K) ^ 2 ≠ 1) :
    deltaNu q (BaryonState.neutron.twoT3) * deltaNu q (BaryonState.neutron.twoT3) =
      (((((q⁻¹ : Kˣ) : K) - (q : K)) ^ 2) / 4) ∧
    deltaNu q (BaryonState.neutron.twoT3) * deltaNu q (BaryonState.neutron.twoT3) ≠ 0 ∧
    deltaNu q (BaryonState.proton.twoT3) * deltaNu q (BaryonState.proton.twoT3) =
      deltaNu q (BaryonState.neutron.twoT3) * deltaNu q (BaryonState.neutron.twoT3) := by
  have hval_n : deltaNu q BaryonState.neutron.twoT3 =
      ((((q⁻¹ : Kˣ) : K) - (q : K)) / 2) := by
    simp [deltaNu, BaryonState.twoT3]
  have hval_p : deltaNu q BaryonState.proton.twoT3 =
      (((q : K) - (((q⁻¹ : Kˣ) : K))) / 2) := by
    simp [deltaNu, BaryonState.twoT3]
  have hnn : deltaNu q BaryonState.neutron.twoT3 * deltaNu q BaryonState.neutron.twoT3 =
      (((((q⁻¹ : Kˣ) : K) - (q : K)) ^ 2) / 4) := by
    rw [hval_n]
    ring
  refine ⟨hnn, ?_, ?_⟩
  · rw [hnn]
    intro hzero
    have hdiff_ne : (((q⁻¹ : Kˣ) : K) - (q : K)) ≠ 0 := by
      intro hd
      apply hq2
      have hqi : (q : K) * (((q⁻¹ : Kˣ) : K)) = 1 := Units.mul_inv q
      linear_combination -(q : K) * hd + hqi
    have hsq_ne : ((((q⁻¹ : Kˣ) : K) - (q : K)) ^ 2) ≠ 0 := pow_ne_zero 2 hdiff_ne
    have h4_ne : (4 : K) ≠ 0 := by norm_num
    exact div_ne_zero hsq_ne h4_ne hzero
  · rw [hval_p, hval_n]
    ring

/-- **Gell-Mann–Nishijima Electric Charge Operator** `Q_EM(b) = T₃(b) + Y(b) / 2` over `K`. -/
def qEM (b : BaryonState) : K :=
  (b.twoT3 : K) / 2 + (b.hypercharge : K) / 2

/-- **Gell-Mann–Nishijima Charge Theorem (`(+1, 0, -1, 0)`, Neutron Neutrality, `pp ≠ nn`,
`C`-Oddness, and Two-Body `CPT`-Evenness):** -/
theorem gmn_charge_properties :
    (qEM (K := K) .proton = 1 ∧ qEM (K := K) .neutron = 0 ∧
      qEM (K := K) .antiproton = -1 ∧ qEM (K := K) .antineutron = 0) ∧
    (qEM (K := K) .neutron * qEM .neutron = 0 ∧
      qEM (K := K) .proton * qEM .neutron = 0) ∧
    (qEM (K := K) .proton * qEM .proton = 1 ∧
      qEM (K := K) .proton * qEM .proton ≠ qEM (K := K) .neutron * qEM .neutron) ∧
    (∀ b : BaryonState, qEM (K := K) b.cConj = -qEM b) ∧
    (∀ b₁ b₂ : BaryonState,
      qEM (K := K) b₁.cConj * qEM b₂.cConj = qEM b₁ * qEM b₂) := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · simp only [qEM, BaryonState.twoT3, BaryonState.hypercharge]
    norm_num
  · simp only [qEM, BaryonState.twoT3, BaryonState.hypercharge]
    norm_num
  · simp only [qEM, BaryonState.twoT3, BaryonState.hypercharge]
    norm_num
  · intro b
    cases b <;> simp only [qEM, BaryonState.cConj, BaryonState.twoT3, BaryonState.hypercharge] <;>
      norm_num
  · intro b₁ b₂
    cases b₁ <;> cases b₂ <;>
      simp only [qEM, BaryonState.cConj, BaryonState.twoT3, BaryonState.hypercharge] <;>
      norm_num

/-- `q`-deformed modular Gell-Mann–Nishijima operator combining the modular Cartan defect
`Δν(q, 2 T₃) / 2` with the modular-scaled hypercharge `((q - q⁻¹) / 4) * Y`. -/
def qModGMN (q : Kˣ) (b : BaryonState) : K :=
  deltaNu q b.twoT3 / 2 + (((q : K) - (((q⁻¹ : Kˣ) : K))) / 4) * (b.hypercharge : K)

/-- **`q`-Deformed Modular GMN Theorem:**
1. Exact factorization `qModGMN q b = ((q - q⁻¹) / 2) * qEM b` on all 4 states,
2. Vanishes identically at `q = 1` (`qou-az9l`),
3. Vanishes identically on `neutron` and `antineutron` for **all** `q`,
4. Separates `(p, p)` from `(n, n)` whenever `(q : K)² ≠ 1`,
5. Exact joint `(q ↦ q⁻¹, b ↦ cConj b)` `CPT`-invariance (`qModGMN q⁻¹ b.cConj = qModGMN q b`). -/
theorem qModGMN_properties (q : Kˣ) :
    (∀ b : BaryonState,
      qModGMN q b = (((q : K) - (((q⁻¹ : Kˣ) : K))) / 2) * qEM b) ∧
    (∀ b : BaryonState, qModGMN (1 : Kˣ) b = 0) ∧
    (qModGMN q .neutron = 0 ∧ qModGMN q .antineutron = 0) ∧
    ((q : K) ^ 2 ≠ 1 →
      qModGMN q .proton * qModGMN q .proton ≠ qModGMN q .neutron * qModGMN q .neutron) ∧
    (∀ b : BaryonState, qModGMN q⁻¹ b.cConj = qModGMN q b) := by
  have hfac : ∀ b : BaryonState,
      qModGMN q b = (((q : K) - (((q⁻¹ : Kˣ) : K))) / 2) * qEM b := by
    intro b
    cases b <;>
      simp only [qModGMN, deltaNu, qEM, BaryonState.twoT3, BaryonState.hypercharge,
        neg_neg, zpow_one, zpow_neg_one, Int.cast_one, Int.cast_neg] <;>
      ring
  refine ⟨hfac, ?_, ?_, ?_, ?_⟩
  · intro b
    simp [qModGMN, deltaNu]
  · rw [hfac .neutron, hfac .antineutron]
    simp only [qEM, BaryonState.twoT3, BaryonState.hypercharge]
    norm_num
  · intro hq2
    rw [hfac .proton, hfac .neutron]
    have hp : qEM (K := K) .proton = 1 := by
      simp only [qEM, BaryonState.twoT3, BaryonState.hypercharge]; norm_num
    have hn : qEM (K := K) .neutron = 0 := by
      simp only [qEM, BaryonState.twoT3, BaryonState.hypercharge]; norm_num
    rw [hp, hn, mul_one, mul_zero, zero_mul]
    intro h0
    have hdiff_ne : ((q : K) - (((q⁻¹ : Kˣ) : K))) ≠ 0 := by
      intro hd
      apply hq2
      have hqi : (q : K) * (((q⁻¹ : Kˣ) : K)) = 1 := Units.mul_inv q
      linear_combination (q : K) * hd + hqi
    have h2 : (2 : K) ≠ 0 := by norm_num
    have hhalf_ne : (((q : K) - (((q⁻¹ : Kˣ) : K))) / 2) ≠ 0 := div_ne_zero hdiff_ne h2
    exact mul_ne_zero hhalf_ne hhalf_ne h0
  · intro b
    cases b <;>
      simp only [qModGMN, deltaNu, BaryonState.cConj, BaryonState.twoT3,
        BaryonState.hypercharge, neg_neg, zpow_one, zpow_neg_one, inv_inv,
        Int.cast_one, Int.cast_neg] <;>
      ring

/-! ## 3. Unique Derivation of Quark Charges `(q_u, q_d) = (2/3, -1/3)` -/

/-- Under modular Cartan isospin splitting `q_u - q_d = 1`, neutral `udd` baryon charge
`q_u + 2 * q_d = 0` is equivalent to `N_c = 3` chiral/electric anomaly cancellation
`3 * (q_u + q_d) + (-1) = 0` (with electron charge `-1`). -/
theorem udd_neutral_iff_anomaly_cancel {q_u q_d : K} (hiso : q_u - q_d = 1) :
    q_u + 2 * q_d = 0 ↔ 3 * (q_u + q_d) + (-1) = 0 := by
  have hrel : (3 * (q_u + q_d) + (-1)) = 2 * (q_u + 2 * q_d) + (q_u - q_d - 1) := by ring
  have hiso0 : q_u - q_d - 1 = 0 := sub_eq_zero.mpr hiso
  rw [hrel, hiso0, add_zero]
  constructor
  · intro h; rw [h, mul_zero]
  · intro h
    have h2 : (2 : K) ≠ 0 := by norm_num
    exact (mul_eq_zero.mp h).resolve_left h2

/-- **Unique Derived Quark Charges Theorem (`owner-rulings.md` "Needs to derive the q_i"):**
Over any characteristic-zero field `K`, the linear system
`(i) q_u - q_d = 1` (modular Cartan `ν_q ∘ S² = q^(4 T₃)` isospin splitting) and
`(ii) q_u + 2 * q_d = 0` (`udd` baryon neutrality) has the **unique** solution
`q_u = 2 / 3` and `q_d = -1 / 3`. -/
theorem derived_quark_charges_unique (q_u q_d : K) :
    (q_u - q_d = 1 ∧ q_u + 2 * q_d = 0) ↔ (q_u = 2 / 3 ∧ q_d = -1 / 3) := by
  constructor
  · rintro ⟨hiso, hudd⟩
    have h3 : (3 : K) ≠ 0 := by norm_num
    have hqu3 : 3 * q_u = 2 := by linear_combination 2 * hiso + hudd
    have hqd3 : 3 * q_d = -1 := by linear_combination hudd - hiso
    refine ⟨?_, ?_⟩
    · calc
        q_u = (3 * q_u) / 3 := by rw [mul_div_cancel_left₀ q_u h3]
        _ = 2 / 3 := by rw [hqu3]
    · calc
        q_d = (3 * q_d) / 3 := by rw [mul_div_cancel_left₀ q_d h3]
        _ = -1 / 3 := by rw [hqd3]
  · rintro ⟨rfl, rfl⟩
    constructor <;> norm_num

/-- Equivalent unique derivation from `(i) q_u - q_d = 1` and `(ii') 3 * (q_u + q_d) + (-1) = 0`
(chiral/gauge anomaly cancellation for `N_c = 3` colours). -/
theorem derived_quark_charges_from_anomaly_unique (q_u q_d : K) :
    (q_u - q_d = 1 ∧ 3 * (q_u + q_d) + (-1) = 0) ↔ (q_u = 2 / 3 ∧ q_d = -1 / 3) := by
  constructor
  · rintro ⟨hiso, hanom⟩
    exact (derived_quark_charges_unique q_u q_d).mp
      ⟨hiso, (udd_neutral_iff_anomaly_cancel hiso).mpr hanom⟩
  · rintro ⟨rfl, rfl⟩
    constructor <;> norm_num

end GellMannNishijima

/-! ## 4. Unconditional Electrostatic Negative-Sign Obstruction on `m_n - m_p` -/

section ElectrostaticSignObstruction

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Derived up-quark charge `2 / 3`. -/
def qUp : K := 2 / 3

/-- Derived down-quark charge `-1 / 3`. -/
def qDown : K := -1 / 3

/-- Composite `(Q_n² - Q_p²)`, constituent self-square, and constituent pairwise-product
neutron-minus-proton electrostatic differences at `(q_u, q_d) = (2/3, -1/3)`. -/
theorem electrostatic_three_functionals_negative :
    let Q_p : K := 2 * qUp + qDown
    let Q_n : K := qUp + 2 * qDown
    let self_p : K := 2 * qUp ^ 2 + qDown ^ 2
    let self_n : K := qUp ^ 2 + 2 * qDown ^ 2
    let pair_p : K := qUp * qUp + 2 * qUp * qDown
    let pair_n : K := 2 * qUp * qDown + qDown * qDown
    (Q_n ^ 2 - Q_p ^ 2 = -1 ∧ Q_n ^ 2 - Q_p ^ 2 < 0) ∧
    (self_n - self_p = -1 / 3 ∧ self_n - self_p < 0) ∧
    (pair_p = 0 ∧ pair_n = -1 / 3 ∧ pair_n - pair_p = -1 / 3 ∧ pair_n - pair_p < 0) := by
  dsimp only [qUp, qDown]
  refine ⟨⟨by norm_num, by norm_num⟩, ⟨by norm_num, by norm_num⟩,
    ⟨by norm_num, by norm_num, by norm_num, by norm_num⟩⟩

/-- **Positive-Cone Electrostatic No-Go Theorem for `m_n - m_p > 0`:**
For **every** choice of non-negative positive-kernel weights `w_comp, w_self, w_pair ≥ 0`
not all zero (`0 < w_comp + w_self + w_pair`), each individual electrostatic channel is
non-positive and the total pure electrostatic contribution to `m_n - m_p` is **strictly negative**. -/
theorem electrostatic_positive_cone_nogo {w_comp w_self w_pair : K}
    (hc : 0 ≤ w_comp) (hs : 0 ≤ w_self) (hp : 0 ≤ w_pair)
    (hpos : 0 < w_comp + w_self + w_pair) :
    let Q_p : K := 2 * qUp + qDown
    let Q_n : K := qUp + 2 * qDown
    let self_p : K := 2 * qUp ^ 2 + qDown ^ 2
    let self_n : K := qUp ^ 2 + 2 * qDown ^ 2
    let pair_p : K := qUp * qUp + 2 * qUp * qDown
    let pair_n : K := 2 * qUp * qDown + qDown * qDown
    (w_comp * (Q_n ^ 2 - Q_p ^ 2) ≤ 0 ∧
      w_self * (self_n - self_p) ≤ 0 ∧
      w_pair * (pair_n - pair_p) ≤ 0) ∧
    w_comp * (Q_n ^ 2 - Q_p ^ 2) + w_self * (self_n - self_p) +
      w_pair * (pair_n - pair_p) < 0 := by
  obtain ⟨⟨h1, _⟩, ⟨h2, _⟩, ⟨_, _, h3, _⟩⟩ :=
    electrostatic_three_functionals_negative (K := K)
  dsimp only
  rw [h1, h2, h3]
  refine ⟨⟨by linarith [hc], by linarith [hs], by linarith [hp]⟩, by linarith [hc, hpos]⟩

end ElectrostaticSignObstruction

/-! ## 5. Normal-Ordered `A`-Cluster Nuclear Coulomb Law (`Z(Z - 1)` & `³H`–`³He` Split) -/

section NormalOrderedNuclearCoulomb

/-- Any `{0, 1}`-valued charge assignment (`Q i = 0 ∨ Q i = 1`, e.g. neutrons and protons)
is pointwise idempotent (`(Q i)² = Q i`). -/
theorem sq_eq_self_of_zero_or_one {R : Type*} [CommRing R] {x : R} (hx : x = 0 ∨ x = 1) :
    x ^ 2 = x := by
  rcases hx with rfl | rfl <;> ring

/-- **Normal-Ordered `A`-Cluster Nuclear Coulomb Law (`Z(Z - 1)`):**
For any finite `A`-nucleon system with `{0, 1}`-valued nucleon charges `Q : ι → R` and total
proton number `Z = ∑ i, Q i`, subtracting the 1-body proton self-energies yields
`(∑ i, Q i)² - ∑ i, (Q i)² = Z * (Z - 1)`. -/
theorem normalOrderedCoulomb_eq_Z_mul_Z_sub_one {R : Type*} [CommRing R]
    {ι : Type*} [Fintype ι] (Q : ι → R) (hQ : ∀ i : ι, Q i = 0 ∨ Q i = 1) :
    (∑ i, Q i) ^ 2 - ∑ i, (Q i) ^ 2 = (∑ i, Q i) * ((∑ i, Q i) - 1) := by
  have hsum_sq : ∑ i, (Q i) ^ 2 = ∑ i, Q i := by
    refine Finset.sum_congr rfl fun i _ => sq_eq_self_of_zero_or_one (hQ i)
  rw [hsum_sq]
  ring

/-- Concrete nuclear evaluations: normal-ordered Coulomb pair count `Z * (Z - 1)` vanishes
at `Z = 0` (`nn`) and `Z = 1` (deuteron `²H`, triton `³H`), and equals `2` at `Z = 2`
(helion `³He`, alpha `⁴He`; ordered pairs `i ≠ j`, corresponding to `Z * (Z - 1) / 2 = 1`
unordered proton–proton pair). -/
theorem normalOrderedCoulomb_light_nuclei_values :
    let pairCount : ℤ → ℤ := fun Z => Z * (Z - 1)
    pairCount 0 = 0 ∧ pairCount 1 = 0 ∧ pairCount 2 = 2 := by
  decide

/-- **`³He`–`³H` Mirror Coulomb Splitting:**
Over any strict ordered ring `R`, for any positive Coulomb coupling `0 < α_C`, the normal-ordered
`A = 3` Coulomb energy difference between `³He` (`Z = 2`, `Q = ![1, 1, 0]`) and `³H` (`Z = 1`,
`Q = ![1, 0, 0]`) equals `2 * α_C > 0`, breaking `A = 3` isospin mirror degeneracy. -/
theorem helion_triton_coulomb_split_pos {R : Type*} [CommRing R] [LinearOrder R]
    [IsStrictOrderedRing R] {α_C : R} (hα : 0 < α_C) :
    let Q_He3 : Fin 3 → R := ![1, 1, 0]
    let Q_H3 : Fin 3 → R := ![1, 0, 0]
    let E_He3 : R := α_C * ((∑ i, Q_He3 i) ^ 2 - ∑ i, (Q_He3 i) ^ 2)
    let E_H3 : R := α_C * ((∑ i, Q_H3 i) ^ 2 - ∑ i, (Q_H3 i) ^ 2)
    E_He3 - E_H3 = 2 * α_C ∧ 0 < E_He3 - E_H3 := by
  dsimp only
  have hdiff :
      α_C * ((∑ i : Fin 3, (![1, 1, 0] : Fin 3 → R) i) ^ 2 -
          ∑ i : Fin 3, ((![1, 1, 0] : Fin 3 → R) i) ^ 2) -
        α_C * ((∑ i : Fin 3, (![1, 0, 0] : Fin 3 → R) i) ^ 2 -
          ∑ i : Fin 3, ((![1, 0, 0] : Fin 3 → R) i) ^ 2) = 2 * α_C := by
    simp [Fin.sum_univ_three]
    ring
  refine ⟨hdiff, ?_⟩
  rw [hdiff]
  linarith

end NormalOrderedNuclearCoulomb

end QOU.StandardModel
