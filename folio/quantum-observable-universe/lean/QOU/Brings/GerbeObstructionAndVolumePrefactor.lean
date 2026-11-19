import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Data.Finset.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.IntervalCases
import Mathlib.Tactic.NormNum
import QOU.BraidKnot.BringFigureEightDepth2Witness
import QOU.BraidKnot.BringTrilogDepth3Witness
import QOU.BraidKnot.BringTrilogImaginaryTateRational
import QOU.BraidKnot.Cl3Zeta5OrbitSum

/-!
# Gerbe Lifting-Obstruction Reconciliation and the `(2, 4, 5)` Hyperbolic Index `40 = |S₅| / 3`

This module formalizes three interconnected families of arithmetic, cohomological, and
hyperbolic-tessellation results on Bring's genus-4 curve `Σ₄` (`qou-vo9t`, `qou-lx8f`,
`qou-2a2o`, `qou-n2aa`, `qou-5lib`, `cj27e`, `cj3fb`):

1. **§1. Reconciliation of `ℤ` vs `ℤ/2` vs `ℤ/n` vs `𝒪^×` Lifting Obstructions (`qou-vo9t`, `qou-lx8f`, `qou-2a2o`, `qou-n2aa`):**
   - For a closed orientable surface `Σ_g` (`H²(Σ_g; ℤ) ≅ ℤ`), the integral Euler/Chern class
     of the tangent `U(1)`-bundle is `e(TΣ_g) = 2 - 2g`, which is non-vanishing in `ℤ` iff
     `g ≠ 1` (`euler_nonvanishing_iff_g_ne_one`), taking the value `-6 ≠ 0` at `g = 4`.
   - Under the spin central extension `1 → ℤ/2 → SU(2) → SO(3) → 1`, the mod-2 reduction
     `w₂(TΣ_g) = (2 - 2g : ZMod 2)` vanishes identically for every genus `g`
     (`stiefel_whitney_mod2_vanishes`), whereas odd-degree circle bundles `2k + 1` have
     non-zero mod-2 class `1 ∈ ZMod 2`.
   - Under the `n`-th root Kummer sequence `1 → μ_n → 𝔾_m → 𝔾_m → 1`, the mod-`n` image
     `(-6 : ZMod n)` vanishes iff `n ∣ 6` (`kummer_mod_n_vanishes_iff_dvd_six`), selecting
     `n ∈ {1, 2, 3, 6}` among positive levels (`bring_admissible_kummer_levels_iff`) and
     matching `QOU.Brings.BringsObstruction`.
   - In `H²(Σ₄; ℤ) ≅ ℤ`, any two non-zero subgroups intersect non-trivially
     (`int_subgroups_non_complementary`), while the holomorphic `n`-jet Atiyah extension
     scalar `n(d + (n - 1)(g - 1))` for `TΣ₄` (`d = -6`, `g = 4`) equals `3n(n - 3)`,
     vanishing uniquely at Bol's third-order level `n = 3` (`bring_tangent_atiyah_jet_bol_zero`).

2. **§2. Spin-Structure Arf Partition and Odd Theta Characteristics at `g = 4` (`qou-2a2o`, `qou-9l0d`):**
   - Because `w₂(TΣ_g) = 0`, a genus-`g` surface (`g ≥ 1`) carries `2^(2g)` spin structures,
     partitioned by the Arf invariant into `2^(g-1)(2^g + 1)` even and `2^(g-1)(2^g - 1)` odd
     theta characteristics (`spin_structure_arf_partition`).
   - At `g = 4`, `N_odd(4) = 2^(4-1)(2^4 - 1) = 8 × 15 = 120 = 5! = |S₅|` and
     `136 + 120 = 2^8 = 256` (`odd_theta_characteristics_genus_four_eq_s5_order`).
   - Across all genera `g ≥ 1`, the equality `N_odd(g) = (g + 1)!` holds iff `g = 2` or `g = 4`
     (`odd_theta_eq_factorial_succ_iff`), making `g = 4` the unique non-hyperelliptic solution.

3. **§3. `(2, 4, 5)` Hyperbolic Tessellation, Coset Index `40 = |S₅|/3`, and Depth-2/3 Witnesses (`qou-5lib`, `cj27e`, `cj3fb`):**
   - One `(2, 4, 5)` Schwarz triangle has normalized Gauss–Bonnet area
     `1 - 1/2 - 1/4 - 1/5 = 1/20` (in units of `π`), so `240` Schwarz triangles (`120`
     orientation-preserving `(2, 4, 5)` rhombi) have normalized area `240 · (1/20) = 12 = 4(4 - 1)`
     (`bring_245_hyperbolic_tessellation`).
   - Grouping by a freely-acting `C₃ < A₅ < S₅` gives coset indices `|S₅| / |C₃| = 120 / 3 = 40`
     and `|A₅| / |C₃| = 60 / 3 = 20`, matching the universal `(2, 4, 5)` Hurwitz ratio
     `|S₅| / (g_B - 1) = 120 / 3 = 40` (`bring_coset_indices_40_and_20`).
   - The `(2, 4, 5)` fundamental hyperbolic rhombus has cross-ratio phase fraction
     `1/2 + 1/4 - 1/5 = 11/20 = 22/40` (`gcd(11, 40) = 1`), placing `1 - z_rhombus` at a
     primitive `40`-th root of unity with `gcd(40, 6) = 2` (`schwarz_rhombus_cyclotomic_order_40`).
   - Landen's golden-ratio trilogarithm cancellation yields `(4/5) ζ(3)` for the single-valued
     clean trilogarithm at `φ⁻²`, standing in exact `5 : 3` ratio against the primitive
     `5`-th-root Clausen pair sum of `BringTrilogDepth3Witness`
     (`bring_depth3_golden_and_pentagon_relation`).
-/

namespace QOU.Brings.GerbeObstructionAndVolumePrefactor

-- ============================================================================
-- §1. Exact Reconciliation of Z vs Z/2 vs Z/n vs O^x Lifting Obstructions
-- ============================================================================

/-- Integral Euler / first Chern class `e(TΣ_g) = 2 - 2g ∈ H²(Σ_g; ℤ) ≅ ℤ` of the
    tangent bundle of a closed orientable genus-`g` surface. -/
def surfaceEulerClass (g : ℤ) : ℤ := 2 - 2 * g

/-- Mod-`n` reduction `ρ_n(e(TΣ_g)) ∈ ZMod n ≅ H²(Σ_g; ℤ/nℤ)` under the Kummer /
    universal-coefficient map `ℤ →+* ZMod n`. -/
def modNObstruction (g : ℤ) (n : ℕ) : ZMod n :=
  (surfaceEulerClass g : ZMod n)

/-- Second Stiefel–Whitney spin-lifting obstruction `w₂(TΣ_g) ∈ ZMod 2` associated with
    `1 → ℤ/2 → SU(2) → SO(3) → 1`. -/
def stiefelWhitneyW2 (g : ℤ) : ZMod 2 :=
  modNObstruction g 2

/-- Sheaf `H²(Σ_g, 𝒪^×) ≅ 0` class (represented in `ZMod 1`), vanishing on every compact
    Riemann surface via `H²(Σ_g, 𝒪) = 0 → H²(Σ_g, 𝒪^×) → H³(Σ_g, ℤ) = 0`. -/
def archimedeanBandH2Obstruction (_g : ℤ) : ZMod 1 := 0

/-- **Integral Euler non-vanishing criterion (`qou-n2aa`):**
    The integral Euler class `2 - 2g ∈ ℤ` is non-zero if and only if `g ≠ 1` (the torus). -/
theorem euler_nonvanishing_iff_g_ne_one (g : ℤ) :
    surfaceEulerClass g ≠ 0 ↔ g ≠ 1 := by
  unfold surfaceEulerClass
  omega

/-- On Bring's curve (`g = 4`), the integral Euler class equals `-6` and is non-zero in `ℤ`. -/
theorem bring_integral_euler_neg_six :
    surfaceEulerClass 4 = -6 ∧ surfaceEulerClass 4 ≠ 0 := by
  unfold surfaceEulerClass
  omega

/-- **Mod-2 Stiefel–Whitney vanishing for all orientable surfaces (`qou-2a2o`):**
    `(2 - 2g : ZMod 2) = 0` holds identically for every `g : ℤ`, so `TΣ_g` always lifts
    across `SU(2) → SO(3)` (`Spin(2) → SO(2)`). -/
theorem stiefel_whitney_mod2_vanishes (g : ℤ) :
    ((2 - 2 * g : ℤ) : ZMod 2) = 0 := by
  have h2 : (2 : ℤ) ∣ (2 - 2 * g) := ⟨1 - g, by ring⟩
  exact (ZMod.intCast_zmod_eq_zero_iff_dvd (2 - 2 * g) 2).mpr h2

/-- Corollary in terms of `stiefelWhitneyW2`, contrasted with odd-degree circle bundles
    `d = 2k + 1` (such as the Hopf bundle `d = -1`), whose mod-2 class equals `1 ≠ 0`. -/
theorem stiefelWhitneyW2_zero_and_odd_bundle_nonzero (g k : ℤ) :
    stiefelWhitneyW2 g = 0 ∧
    ((2 * k + 1 : ℤ) : ZMod 2) = 1 ∧
    ((2 * k + 1 : ℤ) : ZMod 2) ≠ 0 := by
  refine ⟨stiefel_whitney_mod2_vanishes g, ?_, ?_⟩
  · push_cast
    have h2z : (2 : ZMod 2) = 0 := by decide
    rw [h2z, zero_mul, zero_add]
  · intro h0
    have hdvd : (2 : ℤ) ∣ (2 * k + 1) :=
      (ZMod.intCast_zmod_eq_zero_iff_dvd (2 * k + 1) 2).mp h0
    omega

/-- **Exact Bockstein / Kummer kernel characterization:**
    Under `ℤ →(·n) ℤ →(ρ_n) ZMod n → 0`, an integral class `e : ℤ` maps to `0 ∈ ZMod n`
    if and only if `(n : ℤ) ∣ e`. -/
theorem bockstein_kummer_kernel_iff_dvd (e : ℤ) (n : ℕ) :
    (e : ZMod n) = 0 ↔ (n : ℤ) ∣ e :=
  ZMod.intCast_zmod_eq_zero_iff_dvd e n

/-- **Kummer mod-`n` vanishing on Bring's curve (`qou-lx8f`, `qou-n2aa`):**
    `(-6 : ZMod n) = 0` holds if and only if `n ∣ 6`. -/
theorem kummer_mod_n_vanishes_iff_dvd_six (n : ℕ) :
    ((-6 : ℤ) : ZMod n) = 0 ↔ n ∣ 6 := by
  rw [ZMod.intCast_zmod_eq_zero_iff_dvd, Int.dvd_neg]
  exact Int.ofNat_dvd

/-- Explicit characterization of positive Kummer levels on `Σ₄`:
    for `n > 0`, `(-6 : ZMod n) = 0` holds if and only if `n ∈ {1, 2, 3, 6}`. -/
theorem bring_admissible_kummer_levels_iff (n : ℕ) (hn : 0 < n) :
    ((-6 : ℤ) : ZMod n) = 0 ↔ n ∈ ({1, 2, 3, 6} : Finset ℕ) := by
  rw [kummer_mod_n_vanishes_iff_dvd_six]
  simp only [Finset.mem_insert, Finset.mem_singleton]
  constructor
  · intro hdvd
    have hle : n ≤ 6 := Nat.le_of_dvd (by decide) hdvd
    interval_cases n <;> simp_all
  · rintro (rfl | rfl | rfl | rfl) <;> norm_num

/-- Kummer degree-condition equivalence on `Σ₄`: any level-indexed sequence `kappa : ℕ → ℤ`
    satisfying `kappa n = 0 ↔ (n : ℤ) ∣ surfaceEulerClass 4` vanishes at `n > 0` iff
    `(-6 : ZMod n) = 0`, i.e. `n ∈ {1, 2, 3, 6}` (with `n = 4, 5` obstructed). -/
theorem kummer_degree_condition_iff_admissible (kappa : ℕ → ℤ)
    (hkummer : ∀ m : ℕ, 0 < m → (kappa m = 0 ↔ (m : ℤ) ∣ surfaceEulerClass 4))
    (n : ℕ) (hn : 0 < n) :
    (kappa n = 0 ↔ ((-6 : ℤ) : ZMod n) = 0) ∧
    (kappa n = 0 ↔ n ∈ ({1, 2, 3, 6} : Finset ℕ)) := by
  have hk := hkummer n hn
  unfold surfaceEulerClass at hk
  have h6 : (2 : ℤ) - 2 * 4 = -6 := by norm_num
  rw [h6, ← ZMod.intCast_zmod_eq_zero_iff_dvd (-6) n] at hk
  exact ⟨hk, hk.trans (bring_admissible_kummer_levels_iff n hn)⟩

/-- **Indecomposability of `H²(Σ₄; ℤ) ≅ ℤ` (`qou-lx8f` §3):**
    No two non-zero cyclic subgroups `aℤ` and `bℤ` of `ℤ` can have trivial intersection,
    since `a · b ≠ 0` lies in both. -/
theorem int_subgroups_non_complementary (a b : ℤ) (ha : a ≠ 0) (hb : b ≠ 0) :
    ∃ m : ℤ, m ≠ 0 ∧ a ∣ m ∧ b ∣ m :=
  ⟨a * b, mul_ne_zero ha hb, ⟨b, rfl⟩, ⟨a, mul_comm a b⟩⟩

/-- Holomorphic `n`-jet extension scalar `e_n(L) ∝ n(d + (n - 1)(g - 1))` in
    `Ext¹(J^{n-1}L, K^n ⊗ L) ≅ H¹(Σ_g, K) ≅ ℂ` (`qou-lx8f` §Atiyah). -/
def atiyahJetExtensionScalar (n d g : ℤ) : ℤ :=
  n * (d + (n - 1) * (g - 1))

/-- **Holomorphic `n`-jet behavior on `Σ₄` (`g = 4`):**
    1. Tangent bundle `TΣ₄` (`d = -6`): `e_n = 3n(n - 3)`, vanishing among `n ≥ 1`
       uniquely at `n = 3` (Bol's third-order operator).
    2. Spin bundle `K^{-1/2}` (`d = -3`): `e_n = 3n(n - 2)`, vanishing among `n ≥ 1`
       uniquely at `n = 2` (Gunning's projective structures).
    3. Canonical bundle `K` (`d = 6`): `e_n = 3n(n + 1) > 0` for every `n ≥ 1`. -/
theorem bring_tangent_atiyah_jet_bol_zero (n : ℤ) (hn : 1 ≤ n) :
    atiyahJetExtensionScalar n (-6) 4 = 3 * n * (n - 3) ∧
    (atiyahJetExtensionScalar n (-6) 4 = 0 ↔ n = 3) ∧
    (atiyahJetExtensionScalar n (-3) 4 = 0 ↔ n = 2) ∧
    0 < atiyahJetExtensionScalar n 6 4 := by
  have hT : atiyahJetExtensionScalar n (-6) 4 = 3 * n * (n - 3) := by
    unfold atiyahJetExtensionScalar; ring
  have hS : atiyahJetExtensionScalar n (-3) 4 = 3 * n * (n - 2) := by
    unfold atiyahJetExtensionScalar; ring
  have hK : atiyahJetExtensionScalar n 6 4 = 3 * n * (n + 1) := by
    unfold atiyahJetExtensionScalar; ring
  refine ⟨hT, ?_, ?_, ?_⟩
  · rw [hT]
    constructor
    · intro hz
      rcases mul_eq_zero.mp hz with h3n | hn3
      · omega
      · omega
    · rintro rfl; ring
  · rw [hS]
    constructor
    · intro hz
      rcases mul_eq_zero.mp hz with h3n | hn2
      · omega
      · omega
    · rintro rfl; ring
  · rw [hK]; nlinarith

/-- **Four-band coefficient reconciliation on `Σ₄` (`qou-vo9t`, `qou-lx8f`):**
    Simultaneously records the integral persistence (`-6 ≠ 0` in `ℤ`), mod-2 spin
    vanishing (`0` in `ZMod 2`), mod-`n` Kummer divisibility (`n ∈ {1, 2, 3, 6}`), and
    `𝒪^×`-band vanishing (`0` in `ZMod 1`) of the same geometric class `e(TΣ₄) = -6`. -/
theorem bring_four_band_reconciliation :
    surfaceEulerClass 4 = -6 ∧
    surfaceEulerClass 4 ≠ 0 ∧
    stiefelWhitneyW2 4 = 0 ∧
    (∀ n : ℕ, 0 < n → (modNObstruction 4 n = 0 ↔ n ∈ ({1, 2, 3, 6} : Finset ℕ))) ∧
    archimedeanBandH2Obstruction 4 = 0 := by
  refine ⟨bring_integral_euler_neg_six.1, bring_integral_euler_neg_six.2,
    stiefel_whitney_mod2_vanishes 4, ?_, Subsingleton.elim _ _⟩
  intro n hn
  unfold modNObstruction surfaceEulerClass
  simpa using bring_admissible_kummer_levels_iff n hn

-- ============================================================================
-- §2. Spin Structures, Arf Partition, and 120 = |S₅| Odd Theta Characteristics
-- ============================================================================

/-- Total number of spin structures `|H¹(Σ_g; ℤ/2ℤ)| = 2^(2g)` on an orientable genus-`g` surface. -/
def totalSpinStructures (g : ℕ) : ℕ := 2 ^ (2 * g)

/-- Number of even theta characteristics (Arf invariant `0`): `2^(g-1) · (2^g + 1)`. -/
def evenThetaCount (g : ℕ) : ℕ := 2 ^ (g - 1) * (2 ^ g + 1)

/-- Number of odd theta characteristics (Arf invariant `1`): `2^(g-1) · (2^g - 1)`. -/
def oddThetaCount (g : ℕ) : ℕ := 2 ^ (g - 1) * (2 ^ g - 1)

/-- **All-genus Arf-invariant spin-structure partition:**
    For every `g ≥ 1`, `N_even(g) + N_odd(g) = 2^(2g)` and `N_even(g) - N_odd(g) = 2^g`. -/
theorem spin_structure_arf_partition (g : ℕ) (hg : 1 ≤ g) :
    evenThetaCount g + oddThetaCount g = totalSpinStructures g ∧
    evenThetaCount g - oddThetaCount g = 2 ^ g := by
  obtain ⟨k, rfl⟩ : ∃ k, g = k + 1 := ⟨g - 1, by omega⟩
  unfold evenThetaCount oddThetaCount totalSpinStructures
  simp only [Nat.add_sub_cancel]
  have hpow : 1 ≤ 2 ^ (k + 1) := Nat.one_le_pow _ _ (by decide)
  have hsum : (2 ^ (k + 1) + 1) + (2 ^ (k + 1) - 1) = 2 * 2 ^ (k + 1) := by omega
  have hdiff : (2 ^ (k + 1) + 1) - (2 ^ (k + 1) - 1) = 2 := by omega
  constructor
  · calc
      2 ^ k * (2 ^ (k + 1) + 1) + 2 ^ k * (2 ^ (k + 1) - 1)
          = 2 ^ k * ((2 ^ (k + 1) + 1) + (2 ^ (k + 1) - 1)) := (Nat.mul_add _ _ _).symm
      _ = 2 ^ k * (2 * 2 ^ (k + 1)) := by rw [hsum]
      _ = 2 ^ (2 * (k + 1)) := by ring
  · calc
      2 ^ k * (2 ^ (k + 1) + 1) - 2 ^ k * (2 ^ (k + 1) - 1)
          = 2 ^ k * ((2 ^ (k + 1) + 1) - (2 ^ (k + 1) - 1)) := (Nat.mul_sub_left_distrib _ _ _).symm
      _ = 2 ^ k * 2 := by rw [hdiff]
      _ = 2 ^ (k + 1) := by ring

/-- **Genus-4 odd theta characteristics match `|S₅| = 5! = 120` (`qou-2a2o`, `qou-9l0d`):**
    At `g = 4`, `2^(4-1)(2^4 - 1) = 8 × 15 = 120 = 5!`, `N_even(4) = 136`, and
    `136 + 120 = 2^8 = 256` (contrasting with `N_odd(3) = 28` bitangents on a genus-3 quartic). -/
theorem odd_theta_characteristics_genus_four_eq_s5_order :
    2 ^ (4 - 1) * (2 ^ 4 - 1) = 120 ∧
    120 = Nat.factorial 5 ∧
    oddThetaCount 4 = 120 ∧
    evenThetaCount 4 = 136 ∧
    evenThetaCount 4 + oddThetaCount 4 = 2 ^ 8 ∧
    2 ^ 8 = 256 ∧
    oddThetaCount 3 = 28 := by
  decide

/-- Growth bound `2^(2g - 1) < (g + 1)!` for all `g ≥ 5`, separating `N_odd(g)` from `(g + 1)!`. -/
theorem two_pow_two_g_sub_one_lt_factorial_succ (g : ℕ) (hg : 5 ≤ g) :
    2 ^ (2 * g - 1) < Nat.factorial (g + 1) := by
  obtain ⟨d, rfl⟩ : ∃ d, g = 5 + d := ⟨g - 5, by omega⟩
  induction d with
  | zero => decide
  | succ d ih =>
    have ih' := ih (by omega)
    have hexp : 2 * (5 + (d + 1)) - 1 = (2 * (5 + d) - 1) + 2 := by omega
    rw [hexp, pow_add]
    have hstep : 5 + (d + 1) + 1 = (5 + d + 1) + 1 := by omega
    rw [hstep, Nat.factorial_succ]
    have hmul : 4 < (5 + d + 1) + 1 := by omega
    calc
      2 ^ (2 * (5 + d) - 1) * 2 ^ 2
          = 4 * 2 ^ (2 * (5 + d) - 1) := by ring
      _ < ((5 + d + 1) + 1) * Nat.factorial (5 + d + 1) :=
          Nat.mul_lt_mul_of_lt_of_lt hmul ih'

/-- **All-genus classification of `N_odd(g) = (g + 1)!`:**
    Across all `g ≥ 1`, `oddThetaCount g = (g + 1)!` holds if and only if `g = 2`
    (`N_odd(2) = 6 = 3!`) or `g = 4` (`N_odd(4) = 120 = 5!`), so `g = 4` is the unique
    non-hyperelliptic genus (`g ≥ 3`) with `N_odd(g) = (g + 1)!`. -/
theorem odd_theta_eq_factorial_succ_iff (g : ℕ) (hg : 1 ≤ g) :
    oddThetaCount g = Nat.factorial (g + 1) ↔ g = 2 ∨ g = 4 := by
  constructor
  · intro heq
    by_cases hle4 : g ≤ 4
    · interval_cases g <;> revert heq <;> decide
    · push_neg at hle4
      have hlt := two_pow_two_g_sub_one_lt_factorial_succ g hle4
      have hle : oddThetaCount g ≤ 2 ^ (2 * g - 1) := by
        unfold oddThetaCount
        have hsub : 2 ^ g - 1 ≤ 2 ^ g := Nat.sub_le _ _
        calc
          2 ^ (g - 1) * (2 ^ g - 1) ≤ 2 ^ (g - 1) * 2 ^ g := Nat.mul_le_mul_left _ hsub
          _ = 2 ^ ((g - 1) + g) := (pow_add 2 (g - 1) g).symm
          _ = 2 ^ (2 * g - 1) := by congr 1; omega
      omega
  · rintro (rfl | rfl) <;> decide

/-- Arithmetic `S₅`-orbit structure of theta characteristics on `Σ₄` (`qou-9l0d`,
    Braden–Disney-Hogg 2024): `136 ≡ 1 (mod 5)` forces at least one `C₅`-fixed even
    theta characteristic (`136 = 1 + 15 + 60 + 60`), while `120 = 60 + 60`. -/
theorem bring_theta_s5_orbit_arithmetic :
    evenThetaCount 4 % 5 = 1 ∧
    1 + 15 + 60 + 60 = evenThetaCount 4 ∧
    60 + 60 = oddThetaCount 4 := by
  decide

-- ============================================================================
-- §3. (2, 4, 5) Hyperbolic Tessellation, Coset Index 40 = |S₅|/3, and Periods
-- ============================================================================

/-- Normalized Gauss–Bonnet hyperbolic area `(Area / π) = 1 - 1/p - 1/q - 1/r` of a
    `(p, q, r)` Schwarz reflection triangle in `ℍ²`. -/
def schwarzTriangleNormArea (p q r : ℚ) : ℚ :=
  1 - 1 / p - 1 / q - 1 / r

/-- Normalized Gauss–Bonnet hyperbolic area `(Area(Σ_g) / π) = 4(g - 1) = -2χ(Σ_g)` of a
    closed orientable hyperbolic surface of genus `g`. -/
def surfaceNormArea (g : ℚ) : ℚ :=
  4 * (g - 1)

/-- Normalized phase fraction `θ / π = 1/2 + 1/q - 1/p` of `1 - z_rhombus(2, q, p)` for the
    fundamental `(2, q, p)` hyperbolic rhombus `(0, v_q⁺, v_2, v_q⁻)` in the Poincaré disk. -/
def schwarzRhombusPhaseRatio (q p : ℚ) : ℚ :=
  1 / 2 + 1 / q - 1 / p

/-- **Exact `(2, 4, 5)` hyperbolic tessellation identities on `Σ₄` (`qou-5lib`):**
    1. One `(2, 4, 5)` Schwarz triangle has normalized area `1 / 20` (`Area = π / 20`).
    2. `240` Schwarz triangles (`120` orientation-preserving `(2, 4, 5)` rhombi of area
       `π / 10`) have total normalized area `240 · (1 / 20) = 12 = 4(4 - 1)` (`Area(Σ₄) = 12π`).
    3. Grouping into dual regular maps yields `30` `{5, 4}` quadrilaterals (`30 × 8 = 240`),
       `24` `{4, 5}` right-angled pentagons (`24 × 10 = 240`), and `40` free `C₃`-orbits of
       rhombi covering the genus-2 quotient `Σ₄ / C₃ = 𝒞₂` (`40 × (2 / 20) = 4 = 4(2 - 1)`). -/
theorem bring_245_hyperbolic_tessellation :
    schwarzTriangleNormArea 2 4 5 = 1 / 20 ∧
    240 * schwarzTriangleNormArea 2 4 5 = 12 ∧
    surfaceNormArea 4 = 12 ∧
    120 * (2 * schwarzTriangleNormArea 2 4 5) = surfaceNormArea 4 ∧
    2 / schwarzTriangleNormArea 2 4 5 = 40 ∧
    40 * (2 * schwarzTriangleNormArea 2 4 5) = surfaceNormArea 2 ∧
    30 * 8 = 240 ∧
    24 * 10 = 240 := by
  unfold schwarzTriangleNormArea surfaceNormArea
  norm_num

/-- **Coset indices `40 = |S₅| / |C₃|` and `20 = |A₅| / |C₃|` (`qou-5lib`):**
    Records `|S₅| = 5! = 120`, `|A₅| = 60`, the free-`C₃` coset indices `[S₅ : C₃] = 40` and
    `[A₅ : C₃] = 20`, the `(2, 4, 5)` Riemann–Hurwitz identity `40 · (4 - 1) = 120`, and the
    tower-exponent factorizations `90 = 2 × 45 = 3 × 30 = 5 × 18 = 6 × 15`. -/
theorem bring_coset_indices_40_and_20 :
    Nat.factorial 5 = 120 ∧
    Nat.factorial 5 / 2 = 60 ∧
    Nat.factorial 5 / 3 = 40 ∧
    (Nat.factorial 5 / 2) / 3 = 20 ∧
    40 * (4 - 1) = Nat.factorial 5 ∧
    2 * 45 = 90 ∧ 3 * 30 = 90 ∧ 5 * 18 = 90 ∧ 6 * 15 = 90 := by
  decide

/-- **Primitive `40`-th root-of-unity phase of Bring's `(2, 4, 5)` rhombus (`qou-5lib`, `cj27e`):**
    1. `schwarzRhombusPhaseRatio 4 5 = 11 / 20 = 22 / 40` with `gcd(11, 40) = 1`, so
       `1 - z_rhombus(2, 4, 5) = exp(-2πi · 11 / 40)` is a primitive `40`-th root of unity.
    2. `gcd(40, 6) = 2` and `gcd(20, 6) = 2`, reflecting `ℚ(ζ₄₀) ∩ ℚ(ζ₆) = ℚ(ζ₂) = ℚ`
       between Bring's `(2, 4, 5)` cyclotomic field and the figure-8 Eisenstein field `ℚ(ζ₆)`. -/
theorem schwarz_rhombus_cyclotomic_order_40 :
    schwarzRhombusPhaseRatio 4 5 = 11 / 20 ∧
    (11 / 20 : ℚ) = (11 : ℚ) / (40 / 2) ∧
    Nat.Coprime 11 40 ∧
    Nat.gcd 40 6 = 2 ∧
    Nat.gcd 20 6 = 2 := by
  unfold schwarzRhombusPhaseRatio
  refine ⟨by norm_num, by norm_num, by decide, by decide, by decide⟩

/-- **Algebraic cancellation in Zagier's clean single-valued trilogarithm at `φ⁻²`:**
    Substituting Landen's golden-ratio identities `L₃ = (4/5) Z₃ + (2/3) ℓ³ - (2/15) P₂ ℓ`,
    `L₂ = (1/15) P₂ - ℓ²`, `L₁ = ℓ`, and `λ = -2 ℓ` (`ℓ = log φ`, `P₂ = π²`, `Z₃ = ζ(3)`) into
    `L₃ - λ L₂ + (1/3) λ² L₁` cancels every `ℓ³` and `P₂ ℓ` term, leaving `(4/5) Z₃`. -/
theorem landen_clean_trilog_golden_cancellation (Z₃ P₂ ℓ : ℝ) :
    ((4 / 5 : ℝ) * Z₃ + (2 / 3 : ℝ) * ℓ ^ 3 - (2 / 15 : ℝ) * P₂ * ℓ)
      - (-2 * ℓ) * ((1 / 15 : ℝ) * P₂ - ℓ ^ 2)
      + (1 / 3 : ℝ) * (-2 * ℓ) ^ 2 * ℓ
      = (4 / 5 : ℝ) * Z₃ := by
  ring

/-- **Depth-3 golden-ratio vs `ζ₅` Clausen relation (`cj3fb`, `BringTrilogDepth3Witness`):**
    Conditional on `[W : QOU.BraidKnot.BringTrilogDepth3Witness]`, the primitive `5`-th-root
    real trilog pair sum `Cl₃(2π/5) + Cl₃(4π/5) = -(12/25) ζ(3)` and the golden-ratio clean
    trilogarithm value `ℒ₃(φ⁻²) = (4/5) ζ(3)` satisfy
    `5 · (Cl₃(2π/5) + Cl₃(4π/5)) + 3 · ((4/5) ζ(3)) = 0`, while `imLi3ZetaPredicted 5`
    evaluates to `(4/125) π³`. -/
theorem bring_depth3_golden_and_pentagon_relation
    [W : QOU.BraidKnot.BringTrilogDepth3Witness] :
    5 * (W.cl3_2pi5 + W.cl3_4pi5) + 3 * ((4 / 5 : ℝ) * W.zeta3) = 0 ∧
    QOU.Infra.Polylogarithm.imLi3ZetaPredicted 5 =
      QOU.BraidKnot.BringTrilogImaginaryTateRational.imLi3Zeta5Value := by
  refine ⟨?_, QOU.BraidKnot.BringTrilogImaginaryTateRational.im_li3_zeta5_closed_form⟩
  have hp := QOU.BraidKnot.BringTrilogDepth3Witness.pair_sum_eq (W := W)
  linarith

/-- **Depth-2 witness composition (`cj27e`, `BringFigureEightDepth2Witness`):**
    Composes `QOU.BraidKnot.BringFigureEightDepth2Witness.evaluates_to` with the two-tetrahedra
    factor `Vol(4₁) = 2 · D₂(e^{iπ/3})`. -/
theorem bring_depth2_two_tetrahedra_eval {vol41 grouplikeStd d2Zeta6 : ℝ}
    [h : QOU.BraidKnot.BringFigureEightDepth2Witness vol41 grouplikeStd]
    (hD2 : grouplikeStd = 2 * d2Zeta6) :
    vol41 = 2 * d2Zeta6 :=
  QOU.BraidKnot.BringFigureEightDepth2Witness.evaluates_to (h := h) hD2

end QOU.Brings.GerbeObstructionAndVolumePrefactor
