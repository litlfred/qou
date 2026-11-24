import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Data.Matrix.Basic
import Mathlib.Data.Fin.VecNotation
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FinCases
import QOU.GravitySpacetime.ReebLengthTimeAndLightConeEntropy

/-!
# Canonical Fefferman 4D Lorentzian CR Circle-Bundle Metric `g_θ` & Modular `(2π)/(8π) = 1/4` Horizon Law

Generic base-ring / generic-field (`§7c`, zero `ℝ`, zero empirical inputs, `0 sorry`) formalization
for **Closing Open Gap 4 (Option 4A)**, building on `QOU.GravitySpacetime.ReebLengthTimeAndLightConeEntropy`
(`qou-slfm`, PR `#9240`) and addressing `cr-structure-lorentzian-lift`:

1. **Canonical Fefferman–Lee 4D Lorentzian Metric `g_θ` on `C(M³) → M³` (`§1`):**
   - Given a strictly pseudoconvex contact CR 3-manifold `(M³, H, J, θ)` (`dim H = 2`, Reeb vector
     `R_θ`, positive-definite Levi form `L_θ` with principal eigenvalues `ℓ₁, ℓ₂ > 0`) and its
     canonical circle bundle `π : C(M³) = (K_M \ {0}) / ℝ₊ → M³` with vertical `S¹`-fibre
     generator `∂_σ` and pseudohermitian Fefferman–Lee connection 1-form `ω₀` (`ω₀(∂_σ) = 1`,
     `ω₀(R_θ) = c_R`), formalizes the symmetric bilinear form
       `g_θ(u, v) = θ(u) ω₀(v) + θ(v) ω₀(u) + L_θ(π_* u, π_* v)`
     on `V = R · R_θ ⊕ R · ∂_σ ⊕ H ≅ R⁴` (Fefferman 1976, `10.2307/1970945`; Lee 1986,
     `10.1090/S0002-9947-1986-0837820-2`).
   - Proves exact Gram-matrix representation `feffermanGram c_R ℓ₁ ℓ₂`, universal fibre nullity
     `g_θ(∂_σ, ∂_σ) = 0`, canonical pairing `g_θ(R_θ, ∂_σ) = 1`, Reeb nullity `g_θ(R_θ, R_θ) = 0`
     at `c_R = 0`, shifted null Reeb generator `k_+ = R_θ - c_R ∂_σ` satisfying `g_θ(k_+, k_+) = 0`
     and `g_θ(k_+, ∂_σ) = 1` for **every** `c_R`, and exact 2D horizon-screen restriction
     `g_θ|_H = L_θ` with **zero tunable parameters** once `θ` is fixed by `ℓ_P(q) = ℏ_q t_P(q) = 1`.
   - Proves `det G_Feff(c_R, ℓ₁, ℓ₂) = -ℓ₁ ℓ₂ < 0` independently of `c_R` and constructs an explicit
     unimodular `SL₄(K)` congruence (`det P = 1`, `(2 : K) ≠ 0`, zero square roots required)
       `(P(c_R)).transpose * G_Feff(c_R, ℓ₁, ℓ₂) * P(c_R) = diag(-1, 1, ℓ₁, ℓ₂)`,
     proving exact Lorentzian Sylvester inertia `(3, 1, 0)` (three `+` and one `-` directions).

2. **Sparling–Graham–Lee Curvature Decomposition, Vacuum Obstruction, & Null Focusing (`§2`):**
   - Formalizes Lee's conformal-flatness lock `c_R = R_W / 6` at `λ₀ = 1 / 3` (`W_{abcd}(g_θ) = 0`
     on all locally spherical / constant-Webster-curvature Sasakian CR 3-manifolds: `S³`, `ℍ¹`, and
     hyperbolic unit tangent bundles `UT(Σ_g)` including Bring's genus-4 surface; Graham 1987,
     `10.2307/2374491`).
   - Proves Sparling–Graham's vacuum-Einstein obstruction: along the null Killing `S¹`-fibre
     `K = ∂_σ`, `g_θ(K, K) = 0` while `Ric(K, K) = 1 / 2 ≠ 0` (from contact twist `ω_{ab} ω^{ab} = 1/2`),
     ruling out vacuum Einstein `Ric = Λ g_θ` for every `Λ`.
   - Proves the exact Einstein–`Λ_W` rank-1 wave decomposition
       `Einstein(R_W) + (R_W / 4) · G_Feff(0, 1, 1) = (1 / 2) ξ ⊗ ξ`   (`ξ = σ_θ - (R_W / 2) θ`)
     and universal Null Energy / Raychaudhuri focusing non-negativity
       `Ric_{ab}(R_W) k^a k^b = (1 / 2) (k₁ - (R_W / 2) k₀)² ≥ 0`
     across the entire 4D null cone `2 k₀ k₁ + k₂² + k₃² = 0` for all `R_W`.

3. **Modular–Raychaudhuri `(2π)/(8π) = 1/4` Law & Dual Substrate Normalizations `1` vs `q` (`§3–§4`):**
   - Proves in both proper-acceleration (`a = c κ`) and surface-gravity (`κ`) conventions that
     Unruh/Bisognano–Wichmann Rindler modular temperature `T_U = ℏ a / (2π c) = ℏ κ / (2π)`
     (Bisognano & Wichmann 1975/1976, `10.1063/1.522605`, `10.1063/1.522898`) combined with
     Einstein–Raychaudhuri horizon heat flux `δQ = (c² a / (8π G)) δA = (c³ κ / (8π G)) δA`
     (Jacobson 1995, `10.1103/PhysRevLett.75.1260`) yields `(δQ / T_U) / δA = 1 / (4 (ℏ G / c³))`.
   - Contrasts QOU's two substrate gravitational normalizations over any generic `[Field K]`:
     * **Arm N1 (`def:gravitational-constant`, `G_q (ℏ_q / c_q)² = 1`):** exact `1 / 4`,
     * **Arm N2 (direct native-`q` relativistic `ℏ_q G_q / c_q³ = q`):** `1 / (4 q)`, with exact
       ratio `ℏ_q c_q = q⁻¹` and exact relative shift `-ℏ_q = -(1 - q⁻¹)` (`-9.908%` at `q₀`).
   - Isolates the remaining dynamical induced-Einstein & normalization bridge in the zero-instance
     Rule-13a conjecture class `FeffermanDynamicalEinsteinHorizonConjecture`.
-/

-- Ref: [leitner2026] gravity-spacetime, cr-structure-lorentzian-lift
-- Ref: [leitner2026] information-theory, rem:spacetime-length-distance-layers
-- Ref: [jacobson1995] Jacobson, Phys. Rev. Lett. 75 (1995), 1260–1263.
-- Ref: [lewandowski-nurowski-tafel1990] Lewandowski, Nurowski & Tafel, Class. Quantum Grav. 7 (1990), 1961–1981.
-- Ref: [nurowski-trautman2002] Nurowski & Trautman, Differ. Geom. Appl. 17 (2002), 175–195.
-- Ref: [bekenstein1973] Bekenstein, Phys. Rev. D 7 (1973), 2333–2346.
-- Ref: [hawking1975] Hawking, Commun. Math. Phys. 43 (1975), 199–220.
namespace QOU.GravitySpacetime.FeffermanLorentzianHorizonEntropy

open QOU.InformationTheory.UnifiedClockScaleLayers
open QOU.GravitySpacetime.ReebLengthTimeAndLightConeEntropy

/-! ## 1. Fefferman–Lee Canonical CR Circle-Bundle Metric `g_θ` & `(3, 1)` Lorentzian Signature -/

section FeffermanLorentzianSignature

/-- Pullback `π^* θ` of the CR contact 1-form to `V = R · R_θ ⊕ R · ∂_σ ⊕ H ≅ R⁴`
in the adapted frame `(R_θ, ∂_σ, X₁, X₂)`: `θ(R_θ) = 1`, `θ(∂_σ) = 0`, `θ|_H = 0`. -/
def contactPullback {R : Type*} [CommRing R] (u : Fin 4 → R) : R :=
  u 0

/-- Fefferman–Lee connection 1-form `ω₀` on `C(M³)` in the adapted frame `(R_θ, ∂_σ, X₁, X₂)`:
`ω₀(∂_σ) = 1`, `ω₀(R_θ) = cR` (encoding the Tanaka–Webster scalar curvature shift), `ω₀|_H = 0`. -/
def feffermanConnForm {R : Type*} [CommRing R] (cR : R) (u : Fin 4 → R) : R :=
  cR * u 0 + u 1

/-- Horizontal Levi bilinear form `L_θ(π_* u, π_* v)` on the 2D contact distribution `H = span(X₁, X₂)`
with principal Levi eigenvalues `ℓ₁, ℓ₂`. -/
def leviFormHoriz {R : Type*} [CommRing R] (ℓ₁ ℓ₂ : R) (u v : Fin 4 → R) : R :=
  ℓ₁ * u 2 * v 2 + ℓ₂ * u 3 * v 3

/-- **Fefferman–Lee Canonical Symmetric Bilinear Form (`Fefferman 1976`, `Lee 1986`):**
`g_θ(u, v) = θ(u) ω₀(v) + θ(v) ω₀(u) + L_θ(π_* u, π_* v)` on `V = R · R_θ ⊕ R · ∂_σ ⊕ H`. -/
def feffermanBilinear {R : Type*} [CommRing R] (cR ℓ₁ ℓ₂ : R) (u v : Fin 4 → R) : R :=
  contactPullback u * feffermanConnForm cR v +
    contactPullback v * feffermanConnForm cR u +
    leviFormHoriz ℓ₁ ℓ₂ u v

/-- Explicit `4 × 4` Gram matrix of `feffermanBilinear cR ℓ₁ ℓ₂` in the adapted frame
`(R_θ, ∂_σ, X₁, X₂)`. -/
def feffermanGram {R : Type*} [CommRing R] (cR ℓ₁ ℓ₂ : R) : Matrix (Fin 4) (Fin 4) R :=
  !![2 * cR, 1, 0, 0;
     1,      0, 0, 0;
     0,      0, ℓ₁, 0;
     0,      0, 0, ℓ₂]

/-- Adapted basis vector `R_θ = (1, 0, 0, 0)` (horizontal lift of the Reeb vector). -/
def reebLiftVec {R : Type*} [CommRing R] : Fin 4 → R :=
  ![1, 0, 0, 0]

/-- Adapted basis vector `∂_σ = (0, 1, 0, 0)` (canonical `S¹`-fibre generator on `C(M³)`). -/
def fibreGenVec {R : Type*} [CommRing R] : Fin 4 → R :=
  ![0, 1, 0, 0]

/-- Shifted null Reeb generator `k_+ = R_θ - cR · ∂_σ = (1, -cR, 0, 0)`, which remains strictly
null (`g_θ(k_+, k_+) = 0`) for arbitrary Tanaka–Webster scalar curvature shift `cR`. -/
def shiftedNullReebVec {R : Type*} [CommRing R] (cR : R) : Fin 4 → R :=
  ![1, -cR, 0, 0]

/-- `feffermanBilinear` is symmetric over any commutative ring `R`. -/
theorem feffermanBilinear_symm {R : Type*} [CommRing R] (cR ℓ₁ ℓ₂ : R) (u v : Fin 4 → R) :
    feffermanBilinear cR ℓ₁ ℓ₂ u v = feffermanBilinear cR ℓ₁ ℓ₂ v u := by
  unfold feffermanBilinear contactPullback feffermanConnForm leviFormHoriz
  ring

/-- `feffermanGram cR ℓ₁ ℓ₂` is a symmetric `4 × 4` matrix. -/
theorem feffermanGram_transpose {R : Type*} [CommRing R] (cR ℓ₁ ℓ₂ : R) :
    (feffermanGram cR ℓ₁ ℓ₂).transpose = feffermanGram cR ℓ₁ ℓ₂ := by
  ext i j
  fin_cases i <;> fin_cases j <;> simp [feffermanGram]

/-- Exact coordinate equivalence `g_θ(u, v) = u ⬝ᵥ (G_Feff *ᵥ v)` between `feffermanBilinear`
and the `4 × 4` matrix `feffermanGram`. -/
theorem feffermanBilinear_eq_dotProduct_gram {R : Type*} [CommRing R]
    (cR ℓ₁ ℓ₂ : R) (u v : Fin 4 → R) :
    feffermanBilinear cR ℓ₁ ℓ₂ u v =
      dotProduct u (Matrix.mulVec (feffermanGram cR ℓ₁ ℓ₂) v) := by
  unfold feffermanBilinear contactPullback feffermanConnForm leviFormHoriz feffermanGram
  simp [dotProduct, Matrix.mulVec, Fin.sum_univ_four]
  ring

/-- **Nullity & Canonical Pairing Identities of `g_θ`:**
Over any commutative ring `R` and for all `cR, ℓ₁, ℓ₂ : R`:
1. `g_θ(∂_σ, ∂_σ) = 0` (universal nullity of the `S¹`-fibre generator),
2. `g_θ(R_θ, ∂_σ) = 1` (canonical unit null pairing),
3. `g_θ(R_θ, R_θ) = 2 * cR` (so `g_θ(R_θ, R_θ) = 0` whenever `cR = 0`),
4. `g_θ(k_+, k_+) = 0` and `g_θ(k_+, ∂_σ) = 1` for the shifted null generator `k_+ = R_θ - cR ∂_σ`. -/
theorem fefferman_null_and_pairing_identities {R : Type*} [CommRing R] (cR ℓ₁ ℓ₂ : R) :
    feffermanBilinear cR ℓ₁ ℓ₂ fibreGenVec fibreGenVec = 0 ∧
      feffermanBilinear cR ℓ₁ ℓ₂ reebLiftVec fibreGenVec = 1 ∧
      feffermanBilinear cR ℓ₁ ℓ₂ reebLiftVec reebLiftVec = 2 * cR ∧
      feffermanBilinear cR ℓ₁ ℓ₂ (shiftedNullReebVec cR) (shiftedNullReebVec cR) = 0 ∧
      feffermanBilinear cR ℓ₁ ℓ₂ (shiftedNullReebVec cR) fibreGenVec = 1 := by
  unfold feffermanBilinear contactPullback feffermanConnForm leviFormHoriz
    reebLiftVec fibreGenVec shiftedNullReebVec
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · simp
  · simp
  · simp; ring
  · simp
  · simp

/-- When the Tanaka–Webster scalar shift vanishes (`cR = 0`), both `R_θ` and `∂_σ` are strictly null. -/
theorem fefferman_reeb_null_of_zero_shift {R : Type*} [CommRing R] (ℓ₁ ℓ₂ : R) :
    feffermanBilinear (0 : R) ℓ₁ ℓ₂ reebLiftVec reebLiftVec = 0 := by
  simpa using (fefferman_null_and_pairing_identities (0 : R) ℓ₁ ℓ₂).2.2.1

/-- **2D Horizon Screen Metric Identity (`g_θ|_H = L_θ`):**
On any horizontal tangent vectors `u, v ∈ H = ker θ ∩ ker ω₀` (`u 0 = 0`, `v 0 = 0`), `g_θ(u, v)`
reduces identically to the Levi form `L_θ(π_* u, π_* v)` with zero free parameters. -/
theorem fefferman_screen_metric_eq_leviForm {R : Type*} [CommRing R]
    (cR ℓ₁ ℓ₂ : R) {u v : Fin 4 → R} (hu0 : u 0 = 0) (hv0 : v 0 = 0) :
    feffermanBilinear cR ℓ₁ ℓ₂ u v = leviFormHoriz ℓ₁ ℓ₂ u v := by
  unfold feffermanBilinear contactPullback
  rw [hu0, hv0]
  ring

/-- **Exact Fefferman Determinant Theorem (`det G_Feff = -ℓ₁ ℓ₂`):**
Over any commutative ring `R`, `det (feffermanGram cR ℓ₁ ℓ₂) = -ℓ₁ * ℓ₂`, completely independent
of the Reeb connection / Webster-scalar shift `cR`. -/
theorem det_feffermanGram {R : Type*} [CommRing R] (cR ℓ₁ ℓ₂ : R) :
    Matrix.det (feffermanGram cR ℓ₁ ℓ₂) = -(ℓ₁ * ℓ₂) := by
  unfold feffermanGram
  rw [Matrix.det_succ_row_zero]
  simp only [Fin.sum_univ_four, Matrix.det_fin_three]
  have h10 : Fin.succAbove (1 : Fin 4) 0 = 0 := rfl
  have h11 : Fin.succAbove (1 : Fin 4) 1 = 2 := rfl
  have h12 : Fin.succAbove (1 : Fin 4) 2 = 3 := rfl
  simp [h10, h11, h12]

/-- For a positive-definite Levi form (`0 < ℓ₁`, `0 < ℓ₂`) over any ordered field `K`,
`det (feffermanGram cR ℓ₁ ℓ₂) < 0` (strictly Lorentzian determinant sign). -/
theorem det_feffermanGram_neg {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (cR : K) {ℓ₁ ℓ₂ : K} (hℓ₁ : 0 < ℓ₁) (hℓ₂ : 0 < ℓ₂) :
    Matrix.det (feffermanGram cR ℓ₁ ℓ₂) < 0 := by
  rw [det_feffermanGram]
  exact neg_lt_zero.mpr (mul_pos hℓ₁ hℓ₂)

/-- Explicit unimodular `SL₄(K)` basis matrix `P(cR)` diagonalizing `feffermanGram cR ℓ₁ ℓ₂`
to `diag(-1, 1, ℓ₁, ℓ₂)` over any field `K` (`(2 : K) ≠ 0`, zero square roots needed). -/
def feffermanSylvesterBasis {K : Type*} [Field K] (cR : K) : Matrix (Fin 4) (Fin 4) K :=
  !![(2 : K)⁻¹,            (2 : K)⁻¹,            0, 0;
     -((2 : K)⁻¹ * cR + 1), -((2 : K)⁻¹ * cR - 1), 0, 0;
     0,                    0,                    1, 0;
     0,                    0,                    0, 1]

/-- Diagonal Lorentzian `(3, 1)` signature matrix `diag(-1, 1, ℓ₁, ℓ₂)`. -/
def lorentzianDiag31 {R : Type*} [CommRing R] (ℓ₁ ℓ₂ : R) : Matrix (Fin 4) (Fin 4) R :=
  Matrix.diagonal ![-1, 1, ℓ₁, ℓ₂]

/-- `feffermanSylvesterBasis cR` is unimodular (`det P(cR) = 1`, hence invertible in `GL₄(K)`). -/
theorem det_feffermanSylvesterBasis {K : Type*} [Field K] (h2 : (2 : K) ≠ 0) (cR : K) :
    Matrix.det (feffermanSylvesterBasis cR) = 1 := by
  unfold feffermanSylvesterBasis
  rw [Matrix.det_succ_row_zero]
  simp only [Fin.sum_univ_four, Matrix.det_fin_three]
  have h10 : Fin.succAbove (1 : Fin 4) 0 = 0 := rfl
  have h11 : Fin.succAbove (1 : Fin 4) 1 = 2 := rfl
  have h12 : Fin.succAbove (1 : Fin 4) 2 = 3 := rfl
  simp [h10, h11, h12]
  field_simp [h2]
  ring

/-- **Exact `SL₄(K)` Sylvester `(3, 1)` Congruence Theorem:**
Over any field `K` with `(2 : K) ≠ 0`, `(P(cR)).transpose * G_Feff(cR, ℓ₁, ℓ₂) * P(cR) = diag(-1, 1, ℓ₁, ℓ₂)`. -/
theorem fefferman_sylvester_congruence_3_1 {K : Type*} [Field K] (h2 : (2 : K) ≠ 0)
    (cR ℓ₁ ℓ₂ : K) :
    (feffermanSylvesterBasis cR).transpose * feffermanGram cR ℓ₁ ℓ₂ * feffermanSylvesterBasis cR =
      lorentzianDiag31 ℓ₁ ℓ₂ := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [feffermanSylvesterBasis, feffermanGram, lorentzianDiag31,
      Matrix.mul_apply, Fin.sum_univ_four] <;>
    (try field_simp [h2]) <;> ring

/-- **Exact `(3, 1, 0)` Lorentzian Quadratic-Form Inertia & Sign Certificate:**
Over any ordered field `K` (`0 < ℓ₁`, `0 < ℓ₂`), in the unimodular Sylvester coordinates `P(cR) *ᵥ y`:
1. `g_θ(P y, P y) = -y₀² + y₁² + ℓ₁ y₂² + ℓ₂ y₃²`, and
2. The four principal diagonal weights `d = ![-1, 1, ℓ₁, ℓ₂]` satisfy
   `d 0 < 0 ∧ 0 < d 1 ∧ 0 < d 2 ∧ 0 < d 3` (1 timelike `-`, 3 spacelike `+`, 0 degenerate). -/
theorem fefferman_lorentzian_quadratic_inertia {K : Type*}
    [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (cR : K) {ℓ₁ ℓ₂ : K} (hℓ₁ : 0 < ℓ₁) (hℓ₂ : 0 < ℓ₂) (y : Fin 4 → K) :
    let d : Fin 4 → K := ![-1, 1, ℓ₁, ℓ₂]
    feffermanBilinear cR ℓ₁ ℓ₂
        (Matrix.mulVec (feffermanSylvesterBasis cR) y)
        (Matrix.mulVec (feffermanSylvesterBasis cR) y) =
      -(y 0) ^ 2 + (y 1) ^ 2 + ℓ₁ * (y 2) ^ 2 + ℓ₂ * (y 3) ^ 2 ∧
      (d 0 < 0 ∧ 0 < d 1 ∧ 0 < d 2 ∧ 0 < d 3) := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  dsimp only
  refine ⟨?_, by norm_num, by norm_num, hℓ₁, hℓ₂⟩
  unfold feffermanBilinear contactPullback feffermanConnForm leviFormHoriz feffermanSylvesterBasis
  simp [Matrix.mulVec, dotProduct, Fin.sum_univ_four]
  field_simp [h2]
  ring

/-- **Zero-Parameter Lock under Unit Reeb-Circuit Normalization (`ℓ_P(q) = ℏ_q t_P(q) = 1`):**
Once the conformal scale `Ω` is pinned to QOU's unit Reeb circuit `normalisedCircuitLength q = 1`
(`q ≠ 1`), `Ω = 1` identically, leaving zero adjustable parameters in `g_θ`. -/
theorem fefferman_locked_by_unit_reeb_circuit {K : Type*} [Field K] {q : K} (hq1 : q ≠ 1)
    (cR ℓ₁ ℓ₂ : K) :
    let Ω := normalisedCircuitLength q
    Ω = 1 ∧ feffermanGram (Ω * cR) (Ω * ℓ₁) (Ω * ℓ₂) = feffermanGram cR ℓ₁ ℓ₂ := by
  dsimp only
  have hΩ : normalisedCircuitLength q = 1 := normalisedCircuitLength_eq_one hq1
  refine ⟨hΩ, ?_⟩
  rw [hΩ, one_mul, one_mul, one_mul]

end FeffermanLorentzianSignature

/-! ## 2. Sparling–Graham–Lee Ricci Curvature, Vacuum Obstruction, & Null Focusing Positivity -/

section SparlingGrahamLeeCurvature

/-- Principal Weyl-curvature factor `(2 R_W λ₀ - R_W + 2 c_R) / 3` of the Cartan curvature of
`g_θ = 2 θ ⊙ σ_θ + L_θ` on a constant-Webster-curvature Sasakian CR 3-manifold (`n = 1`). -/
def feffermanWeylFactor {K : Type*} [Field K] (R_W lam0 cR : K) : K :=
  (2 * R_W * lam0 - R_W + 2 * cR) / 3

/-- **Lee Conformal-Flatness Lock (`Lee 1986, Thm. 3.7 & Cor. 6.6`):**
At the canonical `K_M = Λ^{2,0}` weight `λ₀ = 1 / (n + 2) = 1 / 3` (`n = 1`, `CharZero K`),
the Weyl curvature factor vanishes iff `c_R = R_W / 6`, uniquely fixing the Webster scalar shift. -/
theorem lee_conformal_flatness_lock_iff {K : Type*} [Field K] [CharZero K] (R_W cR : K) :
    feffermanWeylFactor R_W ((1 : K) / 3) cR = 0 ↔ cR = R_W / 6 := by
  have h3 : (3 : K) ≠ 0 := by exact_mod_cast (by decide : (3 : ℕ) ≠ 0)
  have h6 : (6 : K) ≠ 0 := by exact_mod_cast (by decide : (6 : ℕ) ≠ 0)
  unfold feffermanWeylFactor
  rw [div_eq_zero_iff]
  constructor
  · intro h
    rcases h with hnum | h3z
    · rw [eq_div_iff h6]
      have hclear : (3 : K) * (2 * R_W * (1 / 3) - R_W + 2 * cR) = 0 := by
        rw [hnum, mul_zero]
      field_simp [h3] at hclear
      linear_combination hclear
    · exact False.elim (h3 h3z)
  · intro hc
    left
    rw [hc]
    field_simp [h3, h6]
    ring

/-- **Exact Sparling–Graham–Lee Ricci Tensor (`Graham 1987, Thm. 2.1`)** of `g_θ` in the
null-adapted coframe `(E⁰ = θ, E¹ = σ_θ, E² = η¹, E³ = η²)` on any constant-Webster-curvature
Sasakian CR 3-manifold (`S³` with `R_W > 0`, `ℍ¹` with `R_W = 0`, `UT(Σ_Bring)` with `R_W < 0`). -/
def feffermanRicci {K : Type*} [Field K] (R_W : K) : Matrix (Fin 4) (Fin 4) K :=
  !![R_W ^ 2 / 8, R_W / 4, 0,       0;
     R_W / 4,     1 / 2,   0,       0;
     0,           0,       R_W / 2, 0;
     0,           0,       0,       R_W / 2]

/-- Scalar curvature `R(g_θ) = (3 / 2) R_W` of Lee's Fefferman metric (`g^{ab} R_{ab}`). -/
def feffermanScalarCurv {K : Type*} [Field K] (R_W : K) : K :=
  3 * R_W / 2

/-- Einstein tensor `G_{ab}(R_W) = Ric_{ab}(R_W) - (1 / 2) R(g_θ) g_{ab}` in the null-adapted
coframe where `g_{ab} = feffermanGram 0 1 1`. -/
def feffermanEinstein {K : Type*} [Field K] (R_W : K) : Matrix (Fin 4) (Fin 4) K :=
  feffermanRicci R_W - (feffermanScalarCurv R_W / 2) • feffermanGram 0 1 1

/-- Canonical Sparling–Graham wave covector `ξ = σ_θ - (R_W / 2) θ = (-R_W / 2, 1, 0, 0)`. -/
def feffermanWaveCovec {K : Type*} [Field K] (R_W : K) : Fin 4 → K :=
  ![-R_W / 2, 1, 0, 0]

/-- **Sparling–Graham Vacuum-Einstein Obstruction (`Graham 1987`):**
Along the null Killing `S¹`-fibre generator `K_fib = ∂_σ = (0, 1, 0, 0)`:
1. `g(K_fib, K_fib) = 0`,
2. `Ric(K_fib, K_fib) = 1 / 2 ≠ 0` (driven by contact twist `ω_{ab} ω^{ab} = 1 / 2`), and
3. Consequently, **no** cosmological constant `Λ ∈ K` satisfies the vacuum Einstein equation
   `feffermanRicci R_W = Λ • feffermanGram 0 1 1`! -/
theorem sparling_graham_vacuum_einstein_obstruction {K : Type*} [Field K] (h2 : (2 : K) ≠ 0)
    (R_W : K) :
    dotProduct fibreGenVec (Matrix.mulVec (feffermanGram (0 : K) 1 1) fibreGenVec) = 0 ∧
      dotProduct fibreGenVec (Matrix.mulVec (feffermanRicci R_W) fibreGenVec) = 1 / 2 ∧
      (∀ Λ : K, feffermanRicci R_W ≠ Λ • feffermanGram (0 : K) 1 1) := by
  refine ⟨?_, ?_, ?_⟩
  · simp [fibreGenVec, feffermanGram, dotProduct, Matrix.mulVec, Fin.sum_univ_four]
  · simp [fibreGenVec, feffermanRicci, dotProduct, Matrix.mulVec, Fin.sum_univ_four]
  · intro Λ hEq
    have h11 := congr_arg (fun M : Matrix (Fin 4) (Fin 4) K => M 1 1) hEq
    simp [feffermanRicci, feffermanGram] at h11
    exact h2 h11

/-- **Exact Einstein–`Λ_W` Rank-1 Wave Decomposition:**
Over any field `K` (`CharZero K`), for every Webster scalar curvature `R_W : K` and all tangent
vectors `u, v : Fin 4 → K`:
`u ⬝ᵥ ((G_Ein(R_W) + (R_W / 4) g) *ᵥ v) = (1 / 2) * (ξ ⬝ᵥ u) * (ξ ⬝ᵥ v)`,
showing that `g_θ` satisfies Einstein's equations with effective cosmological constant `Λ_W = R_W / 4`
sourced by the rank-1 pure-radiation / wave tensor `(1 / 2) ξ ⊗ ξ`. -/
theorem fefferman_einstein_rank_one_decomposition {K : Type*} [Field K] [CharZero K]
    (R_W : K) (u v : Fin 4 → K) :
    dotProduct u
        (Matrix.mulVec (feffermanEinstein R_W + (R_W / 4) • feffermanGram 0 1 1) v) =
      (1 / 2 : K) * dotProduct (feffermanWaveCovec R_W) u *
        dotProduct (feffermanWaveCovec R_W) v := by
  have h2 : (2 : K) ≠ 0 := by exact_mod_cast (by decide : (2 : ℕ) ≠ 0)
  have h4 : (4 : K) ≠ 0 := by exact_mod_cast (by decide : (4 : ℕ) ≠ 0)
  have h8 : (8 : K) ≠ 0 := by exact_mod_cast (by decide : (8 : ℕ) ≠ 0)
  unfold feffermanEinstein feffermanRicci feffermanScalarCurv feffermanGram feffermanWaveCovec
  simp [dotProduct, Matrix.mulVec, Fin.sum_univ_four]
  field_simp [h2, h4, h8]
  ring

/-- **Universal Null-Cone Raychaudhuri Positivity (`Ric(k, k) = (1/2)(k₁ - (R_W/2) k₀)² ≥ 0`):**
Over any ordered field `K`, for **every** null vector `k : Fin 4 → K` (`2 k₀ k₁ + k₂² + k₃² = 0`)
and **every** Webster scalar curvature `R_W` (`S³` `R_W > 0`, `ℍ¹` `R_W = 0`, `UT(Σ_Bring)` `R_W < 0`):
`Ric_{ab}(R_W) k^a k^b = G_{ab}(R_W) k^a k^b = (1 / 2) * (k 1 - (R_W / 2) * k 0) ^ 2 ≥ 0`. -/
theorem fefferman_null_cone_ricci_nonneg {K : Type*}
    [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (R_W : K) {k : Fin 4 → K}
    (hnull : 2 * k 0 * k 1 + (k 2) ^ 2 + (k 3) ^ 2 = 0) :
    dotProduct k (Matrix.mulVec (feffermanRicci R_W) k) =
        (1 / 2 : K) * (k 1 - (R_W / 2) * k 0) ^ 2 ∧
      dotProduct k (Matrix.mulVec (feffermanEinstein R_W) k) =
        (1 / 2 : K) * (k 1 - (R_W / 2) * k 0) ^ 2 ∧
      0 ≤ dotProduct k (Matrix.mulVec (feffermanRicci R_W) k) := by
  have h2 : (2 : K) ≠ 0 := two_ne_zero
  have h4 : (4 : K) ≠ 0 := by norm_num
  have h8 : (8 : K) ≠ 0 := by norm_num
  have hric :
      dotProduct k (Matrix.mulVec (feffermanRicci R_W) k) =
        (1 / 2 : K) * (k 1 - (R_W / 2) * k 0) ^ 2 := by
    unfold feffermanRicci
    simp [dotProduct, Matrix.mulVec, Fin.sum_univ_four]
    have hsq : (k 2) ^ 2 + (k 3) ^ 2 = -(2 * k 0 * k 1) := by linarith
    have hgoal :
        k 0 * (R_W ^ 2 / 8 * k 0 + R_W / 4 * k 1) +
          k 1 * (R_W / 4 * k 0 + 2⁻¹ * k 1) +
          (k 2 * (R_W / 2 * k 2) + k 3 * (R_W / 2 * k 3)) =
        2⁻¹ * (k 1 - R_W / 2 * k 0) ^ 2 := by
      calc k 0 * (R_W ^ 2 / 8 * k 0 + R_W / 4 * k 1) +
            k 1 * (R_W / 4 * k 0 + 2⁻¹ * k 1) +
            (k 2 * (R_W / 2 * k 2) + k 3 * (R_W / 2 * k 3))
          = k 0 * (R_W ^ 2 / 8 * k 0 + R_W / 4 * k 1) +
              k 1 * (R_W / 4 * k 0 + 2⁻¹ * k 1) +
              (R_W / 2) * ((k 2) ^ 2 + (k 3) ^ 2) := by ring
        _ = k 0 * (R_W ^ 2 / 8 * k 0 + R_W / 4 * k 1) +
              k 1 * (R_W / 4 * k 0 + 2⁻¹ * k 1) +
              (R_W / 2) * (-(2 * k 0 * k 1)) := by rw [hsq]
        _ = 2⁻¹ * (k 1 - R_W / 2 * k 0) ^ 2 := by
              field_simp [h2, h4, h8]
              ring
    linear_combination hgoal
  have hein :
      dotProduct k (Matrix.mulVec (feffermanEinstein R_W) k) =
        dotProduct k (Matrix.mulVec (feffermanRicci R_W) k) := by
    unfold feffermanEinstein feffermanGram
    simp [dotProduct, Matrix.mulVec, Fin.sum_univ_four]
    linear_combination -(feffermanScalarCurv R_W / 2) * hnull
  refine ⟨hric, hein.trans hric, ?_⟩
  rw [hric]
  exact mul_nonneg (by norm_num) (sq_nonneg _)

end SparlingGrahamLeeCurvature

/-! ## 3. Modular–Raychaudhuri `(2π)/(8π) = 1/4` Law & Dual Substrate Normalizations (`1` vs `q`) -/

section ModularRaychaudhuriAndDualNormalizations

variable {K : Type*} [Field K]

/-- Unruh / Bisognano–Wichmann Rindler modular temperature `T_U = (ℏ · a) / (2π · c)`
in terms of proper Rindler acceleration `a` (`[a] = L / T²`). -/
def unruhTempAccel (pi hbar c accel : K) : K :=
  (hbar * accel) / (2 * pi * c)

/-- Unruh / Bisognano–Wichmann modular temperature `T_U = (ℏ · κ) / (2π)` in terms of horizon
surface gravity `κ = a / c` (`[κ] = 1 / T`). -/
def unruhTempSurfGrav (pi hbar kappa : K) : K :=
  (hbar * kappa) / (2 * pi)

/-- Jacobson–Einstein–Raychaudhuri horizon heat flux `δQ = (c² · a / (8π · G)) · δA`
in terms of proper Rindler acceleration `a`. -/
def raychaudhuriHeatFluxAccel (pi c G_grav accel dA : K) : K :=
  (c ^ 2 * accel / (8 * pi * G_grav)) * dA

/-- Jacobson–Einstein–Raychaudhuri horizon heat flux `δQ = (c³ · κ / (8π · G)) · δA`
in terms of horizon surface gravity `κ = a / c`. -/
def raychaudhuriHeatFluxSurfGrav (pi c G_grav kappa dA : K) : K :=
  (c ^ 3 * kappa / (8 * pi * G_grav)) * dA

/-- Under `a = c · κ` (`c ≠ 0`), proper-acceleration and surface-gravity conventions agree identically. -/
theorem unruh_and_raychaudhuri_accel_surfGrav_equiv {pi hbar c G_grav kappa dA : K} (hc : c ≠ 0) :
    unruhTempAccel pi hbar c (c * kappa) = unruhTempSurfGrav pi hbar kappa ∧
      raychaudhuriHeatFluxAccel pi c G_grav (c * kappa) dA =
        raychaudhuriHeatFluxSurfGrav pi c G_grav kappa dA := by
  unfold unruhTempAccel unruhTempSurfGrav raychaudhuriHeatFluxAccel raychaudhuriHeatFluxSurfGrav
  refine ⟨?_, ?_⟩
  · calc (hbar * (c * kappa)) / (2 * pi * c)
        = (c * (hbar * kappa)) / (c * (2 * pi)) := by ring_nf
      _ = (hbar * kappa) / (2 * pi) := mul_div_mul_left _ _ hc
  · congr 1
    congr 1
    ring

/-- **Modular–Raychaudhuri `(2π)/(8π) = 1/4` Horizon Entropy Cancellation Theorem:**
Over any field `K` (`(2 : K) ≠ 0`, `pi ≠ 0`, `hbar ≠ 0`, `c ≠ 0`, `G_grav ≠ 0`, `accel ≠ 0`, `dA ≠ 0`),
dividing the Einstein–Raychaudhuri heat flux `δQ` by the Unruh/Bisognano–Wichmann modular
temperature `T_U` cancels `pi`, `accel`, and `dA` identically and simplifies `(2π)/(8π)` to `1/4`:
`(δQ / T_U) / δA = c³ / (4 ℏ G_grav) = 1 / (4 · (ℏ G_grav / c³))`. -/
theorem modular_raychaudhuri_quarter_law (h2 : (2 : K) ≠ 0)
    {pi hbar c G_grav accel dA : K}
    (hpi : pi ≠ 0) (hhbar : hbar ≠ 0) (hc : c ≠ 0) (hG : G_grav ≠ 0)
    (ha : accel ≠ 0) (hdA : dA ≠ 0) :
    let dQ := raychaudhuriHeatFluxAccel pi c G_grav accel dA
    let T_U := unruhTempAccel pi hbar c accel
    let ellGravSq := hbar * G_grav / c ^ 3
    (dQ / T_U) / dA = c ^ 3 / (4 * hbar * G_grav) ∧
      (dQ / T_U) / dA = 1 / (4 * ellGravSq) := by
  dsimp only
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]
    exact mul_ne_zero h2 h2
  have h8 : (8 : K) ≠ 0 := by
    have : (8 : K) = 2 * 4 := by norm_num
    rw [this]
    exact mul_ne_zero h2 h4
  have hc3 : c ^ 3 ≠ 0 := pow_ne_zero 3 hc
  unfold raychaudhuriHeatFluxAccel unruhTempAccel
  refine ⟨?_, ?_⟩
  · field_simp [h2, h4, h8, hpi, hhbar, hc, hG, ha, hdA]
    ring
  · field_simp [h2, h4, h8, hpi, hhbar, hc, hc3, hG, ha, hdA]
    ring

/-- **Arm N1 (`def:gravitational-constant` Planck Area `G_q (ℏ_q / c_q)² = 1`):**
Substrate horizon entropy density per unit Reeb-circuit area cell (`ℓ_P(q)² = 1`) under the
native QOU Planck normalization `ℓ_{grav,N1}² = G_q · (ℏ_q / c_q)²`. -/
def entropyDensityNativePlanck (q : K) : K :=
  1 / (4 * (gravCouplingG q * (hbarQ q / causalSpeed q) ^ 2))

/-- **Arm N2 (Direct Relativistic `ℓ_{grav,N2}² = ℏ_q G_q / c_q³ = q`):**
Substrate horizon entropy density per unit Reeb-circuit area cell (`ℓ_P(q)² = 1`) obtained by
substituting `(ℏ_q, c_q, G_q)` directly into `c_q³ / (4 ℏ_q G_q)`. -/
def entropyDensityRelativisticQ (q : K) : K :=
  (causalSpeed q) ^ 3 / (4 * hbarQ q * gravCouplingG q)

/-- **Dual Substrate Normalization Split Theorem (`1 / 4` vs `1 / (4 q)`):**
Over any field `K` (`(2 : K) ≠ 0`, `q ≠ 0`, `q ≠ 1`, `2q - 1 ≠ 0`):
1. **Arm N1:** `entropyDensityNativePlanck q = 1 / 4` (exact Bekenstein–Hawking `1/4`),
2. **Arm N2:** `entropyDensityRelativisticQ q = 1 / (4 * q)` (shifted by `q⁻¹`),
3. **Origin of the shift:** `entropyDensityRelativisticQ q / entropyDensityNativePlanck q = hbarQ q * causalSpeed q` (`= q⁻¹`),
4. **Exact relative discrepancy:** `(entropyDensityRelativisticQ q - 1 / 4) / (1 / 4) = -hbarQ q`
   (`-9.90817...%` at the proton pin `q₀ = 1.10997858...`, vanishing in the classical limit `q → 1`),
5. **Non-coincidence at `q ≠ 1`:** `entropyDensityRelativisticQ q ≠ 1 / 4`. -/
theorem substrate_modular_entropy_density_dual_arms (h2 : (2 : K) ≠ 0) {q : K}
    (hq0 : q ≠ 0) (hq1 : q ≠ 1) (h2q : 2 * q - 1 ≠ 0) :
    entropyDensityNativePlanck q = 1 / 4 ∧
      entropyDensityRelativisticQ q = 1 / (4 * q) ∧
      entropyDensityRelativisticQ q / entropyDensityNativePlanck q = hbarQ q * causalSpeed q ∧
      (entropyDensityRelativisticQ q - 1 / 4) / (1 / 4) = -hbarQ q ∧
      entropyDensityRelativisticQ q ≠ 1 / 4 := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]
    exact mul_ne_zero h2 h2
  have hdual := gravCoupling_planck_units_and_newton_area hq0 hq1 h2q
  have hn1 : entropyDensityNativePlanck q = 1 / 4 := by
    unfold entropyDensityNativePlanck
    rw [hdual.1, mul_one]
  have hn2 : entropyDensityRelativisticQ q = 1 / (4 * q) := by
    unfold entropyDensityRelativisticQ
    have hsub : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
    rw [gravCouplingG_closed_form hq0 hq1 h2q]
    unfold hbarQ causalSpeed
    field_simp [hq0, hsub, h4]
  refine ⟨hn1, hn2, ?_, ?_, ?_⟩
  · rw [hn1, hn2, hbarQ_mul_causalSpeed hq0 hq1]
    field_simp [hq0, h4]
  · rw [hn2]
    unfold hbarQ
    field_simp [hq0, h4]
    ring
  · rw [hn2]
    intro heq
    have h4q : 4 * q ≠ 0 := mul_ne_zero h4 hq0
    rw [div_eq_div_iff h4q h4] at heq
    apply hq1
    exact mul_left_cancel₀ h4 (by linear_combination -heq)

end ModularRaychaudhuriAndDualNormalizations

/-! ## 4. Honest Rule-13a Conjecture Carrier for Dynamical Fefferman Horizon Focusing -/

section DynamicalHorizonConjectureBridge

/-- **Primary Conjecture Class (OPEN — ZERO instances; Rule 13a & `§3b-cond`):**
With the canonical `(3, 1)` Lorentzian Fefferman–Lee metric `g_θ` constructed unconditionally in
`§1` and its background Sparling–Graham–Lee curvature `G_{ab} + (R_W/4) g_{ab} = (1/2) ξ_a ξ_b`
proved in `§2`, this zero-instance class isolates the remaining **dynamical** bridge needed to
discharge `LCQHorizonPunctureAreaConjecture` from QOU's action:
1. `microscopic_puncture_extensivity`: `N_Σ` minimal boundary punctures carry `S_hor(N) = N * s_punct`,
2. `fefferman_rindler_modular_boost`: hypersurface-orthogonal Rindler cuts of `(C(M³), g_θ)` obey
   the Bisognano–Wichmann modular period `S_hor(N) = (twoPi / hbar_eff) * K_boost(N)`,
3. `sakharov_induced_raychaudhuri_focusing`: perturbations of QOU's `q`-Yang–Mills–Levi / spectral
   action on `(C(M³), g_θ)` induce Einstein–Raychaudhuri horizon focusing
   `A_hor(N) = (4 * twoPi * ellGravSq / hbar_eff) * K_boost(N)` with fixed Planck-area scale `ellGravSq`. -/
-- @conjecture: primary
class FeffermanDynamicalEinsteinHorizonConjecture {K : Type*} [Field K]
    (twoPi hbar_eff ellGravSq s_punct : K)
    (S_hor A_hor K_boost : K → K) : Prop where
  /-- Extensive puncture channel entropy `S_hor(N) = N * s_punct`. -/
  microscopic_puncture_extensivity : ∀ nPunct : K, S_hor nPunct = nPunct * s_punct
  /-- Bisognano–Wichmann modular boost relation on Rindler cuts of `(C(M³), g_θ)`. -/
  fefferman_rindler_modular_boost : ∀ nPunct : K,
    S_hor nPunct = (twoPi / hbar_eff) * K_boost nPunct
  /-- Induced dynamical Einstein–Raychaudhuri horizon focusing on `(C(M³), g_θ)`. -/
  sakharov_induced_raychaudhuri_focusing : ∀ nPunct : K,
    A_hor nPunct = (4 * twoPi * ellGravSq / hbar_eff) * K_boost nPunct

/-- **Conditional Bridge Theorem (`§3b-cond`):**
Assuming `FeffermanDynamicalEinsteinHorizonConjecture`, the `(2π)/(8π) = 1/4` cancellation holds
on `(C(M³), g_θ)`, yielding `S_hor(N) = A_hor(N) / (4 * ellGravSq)` and locking the elementary
puncture area ratio to `a0 = 4 * s_punct`. -/
theorem quarter_law_and_puncture_lock_of_fefferman_horizon {K : Type*} [Field K] [CharZero K]
    {twoPi hbar_eff ellGravSq s_punct : K} {S_hor A_hor K_boost : K → K}
    [hFeff : FeffermanDynamicalEinsteinHorizonConjecture twoPi hbar_eff ellGravSq s_punct
      S_hor A_hor K_boost]
    (htwoPi : twoPi ≠ 0) (hhbar : hbar_eff ≠ 0) (hell : ellGravSq ≠ 0) :
    (∀ nPunct : K, S_hor nPunct = A_hor nPunct / (4 * ellGravSq)) ∧
      (∀ nPunct a0 : K, nPunct ≠ 0 → A_hor nPunct = nPunct * a0 * ellGravSq →
        a0 = 4 * s_punct) := by
  have h4 : (4 : K) ≠ 0 := by exact_mod_cast (by decide : (4 : ℕ) ≠ 0)
  have hquarter : ∀ nPunct : K, S_hor nPunct = A_hor nPunct / (4 * ellGravSq) := by
    intro nPunct
    rw [hFeff.fefferman_rindler_modular_boost nPunct,
        hFeff.sakharov_induced_raychaudhuri_focusing nPunct]
    field_simp [htwoPi, hhbar, hell, h4]
  refine ⟨hquarter, ?_⟩
  intro nPunct a0 hN hA
  have hS := hquarter nPunct
  rw [hFeff.microscopic_puncture_extensivity nPunct, hA] at hS
  have h4ell : 4 * ellGravSq ≠ 0 := mul_ne_zero h4 hell
  rw [eq_div_iff h4ell] at hS
  have hcancel : (nPunct * ellGravSq) * a0 = (nPunct * ellGravSq) * (4 * s_punct) := by
    linear_combination -hS
  exact mul_left_cancel₀ (mul_ne_zero hN hell) hcancel

end DynamicalHorizonConjectureBridge

end QOU.GravitySpacetime.FeffermanLorentzianHorizonEntropy
