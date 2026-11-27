/-
Copyright (c) 2026 QOU contributors. All rights reserved.
-/
import Mathlib.Algebra.Polynomial.Degree.Definitions
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Tactic
import BraidKnotOctonion.JimboGl3Singlet
import HeckeTemperleyLieb.QPartitionCombinatorics
import QOU.Nuclear.DeltaLambdaBindingAssembly
import QOU.Nuclear.StokesSymmetryConstant

set_option autoImplicit false

/-!
# Many-Body `6q–12q` Colour-Reconnection Nuclear Carrier & Figure-Eight Stokes Constant `A_ω = 3`

Workstream W4 (`beans` `qou-v2om`, `qou-0c19`, `qou-gpb5`, `qou-3q7t`).
Formalizes two exact mathematical pillars (`0 sorry`, `0 axiom`, §7c generic rings/fields wherever
algebraic):

## Part A — Algebraic Origin of `A_ω = 3` & Cusp Modulus on the `4₁` Eisenstein `ℤ[ω]` Lattice

1. **Eisenstein Cyclotomic & Tetrahedral Cross-Ratio Identities (`eisenstein_minimal_poly`):**
   Over any `[CommRing R]`, a root `ω` of `1 - ω + ω² = 0` satisfies `ω³ = -1`, `ω⁶ = 1`,
   `(2ω - 1)² = -3` (the `ℚ(√-3)` discriminant sourcing `τ = -i√3`), `ω(1 - ω) = 1` (all three
   ideal-tetrahedron edge cross-ratios `(z, 1/(1-z), 1 - 1/z)` coincide on the regular tetrahedron),
   and `1 - (1 - ω) + (1 - ω)² = 0` (`ω̄ = 1 - ω` is the Galois-conjugate saddle).

2. **Two-Tetrahedra Gluing Variety & Three Flat-Connection Saddles
   (`two_tetrahedra_gluing_variety_degree`, `three_flat_connections_card`):**
   - Over `[CommRing R] [Nontrivial R]`, SnapPy's cleared symmetric two-tetrahedra edge equation
     `X⁴ - (1 - X)²` factors as `(X² - X + 1)(X² + X - 1)` where `X² - X + 1` has `natDegree = 2`,
     and adjoining the abelian/trivial flat boundary factor `X + 1` produces `(X + 1)(X² - X + 1) =
     X³ + 1` of `natDegree = 3`.
   - Over `[CommRing R] [IsDomain R]` with `(3 : R) ≠ 0`, any root `ω` of `1 - ω + ω² = 0` yields
     three pairwise-distinct saddle roots `{-1, ω, 1 - ω}` of exact cardinality `3` exhausting all
     solutions of `x³ + 1 = 0`.

3. **Garoufalidis–Kashaev / CCGLS `A`-Polynomial Degree-`3` `L`-Specialization & GGM `A_ω = 3`
   (`aPolyFourOne_degree_and_meridian_one`, `aPoly_nz_cusp_jet`, `ggm_stokes_symmetry_three`):**
   - Both the CCGLS (`L_CCGLS(0) = -1`) and Garoufalidis–Kashaev AJ (`L_AJ(0) = +1`) `A`-polynomials
     of `4₁` are monic of exact `L`-degree `3` for all `(M, M⁻¹)`, specializing at `M = 1` to
     `(L - 1)(L + 1)²` and `(L - 1)³` respectively (matching the rank-`3` state-integral /
     `q`-difference order).
   - Expanding the non-abelian `A`-polynomial relation around `M = 1` (`M² + M⁻² = 2 + δ_X`,
     `-(L + L⁻¹) = 2 + δ_Y`) yields `δ_Y = -3 δ_X - δ_X²`, forcing `τ² = -3` and `3 v₃ = τ`.
   - On the GGM eq. (59a) Wronskian sandwich `2 S⁺(q) = A_GGM W_{-1}(q) B_GGM W_{-1}(q)ᵀ C_GGM`,
     pure bilinear algebra over `[CommRing R]` proves `S̃₀₁(W) + S̃₁₀(W) = 3 · S̃₀₀(W)` and
     `det S̃(W) = (det W)²` for **every** `2 × 2` matrix `W`, specializing at `W_{-1}(0) =
     [[0, -2], [1, 1]]` to `2 · [[1, 3], [0, 1]]` and discharging the `hsym` hypothesis of
     `QOU.QBeta.StokesSymmetryConstant` with `A_ω = 3`.

## Part B — `6q / 9q / 12q` Skew-Howe Colour-Reconnection Multiplicity & Variational Binding Bounds

1. **Exact `SU(3)_c`-Singlet Multiplicity via Hook-Length Formula (`su3SingletDim_light_nuclei`):**
   For `A` nucleons (`3A` quarks in `ℂ³_col`), `Hom_{SU(3)_c}((ℂ³)^{⊗ 3A}, 1)` has basis indexed by
   standard Young tableaux of the rectangular shape `rectThree A = [A, A, A]`. Using
   `QPartitionCombinatorics.Partition.hookLength`, we prove `2 · hookProd [A, A, A] = A! (A+1)! (A+2)!`
   for all `A : ℕ` (3D Catalan numbers), yielding `1` (`3q`), **`5`** (`6q` = `1` factorized `|11⟩`
   + `4` hidden-colour `|88⟩`), **`42`** (`9q` = `1 + 41`), and **`462`** (`12q` = `1 + 461`).

2. **Exact `6q` `U_q(𝔰𝔩₃)` Jimbo Braiding Overlap & `q`-Fierz Casimir Eigenvalues
   (`sixQuark_R23_overlap`, `qFierz_charPoly_roots`):**
   On `(K³)^{⊗ 6}` over any `[Field K]`, pairing the factorized two-nucleon `q`-singlet
   `ε_q ⊗ ε_q` with Jimbo's inter-nucleon braiding `Ř_{2,3}(q)` gives exact overlap ratio
   `q³ / [3]_q` (`1/3` at `q = 1`), hidden-colour leakage norm-squared `[2]_q [4]_q / [3]_q²`
   (`8/9` at `q = 1`), and `q`-Fierz colour-exchange eigenvalues `+[2]_q / (2 [3]_q)` (`+1/3` at
   `q = 1`) and `-[4]_q / (2 [3]_q)` (`-2/3` at `q = 1`, attractive colour reconnection).

3. **Orthogonal Projection / Bloch–Horowitz Schur-Complement Variational Bounds
   (`multiChannel_schur_rayleigh_lt`, `colourReconnection_lowers_ground_energy`):**
   Over any ordered field `K`, coupling `|1^A⟩` across positive hidden-colour gaps `Δ_k > 0` via any
   nonzero braid amplitude `v_k ≠ 0` strictly lowers the Rayleigh–Ritz energy; over `ℝ`, the exact
   2-channel ground eigenvalue `E_-` satisfies `E_- < E₀` and the global `O(v⁴)` sandwich
   `-v² / Δ₈ < E_- - E₀ ≤ -v² / Δ₈ + v⁴ / Δ₈³`.
-/

namespace QOU.Nuclear.ColourReconnectionStokesAssembly

open scoped BigOperators Matrix Polynomial
open Polynomial Matrix
open QOU.Braiding.JimboGl3Singlet
open QOU.MathlibExt.QPartitionCombinatorics
open QOU.Knot.FigureEightComplexVolume
open QOU.QBeta.DeltaLambdaBindingAssembly
open QOU.QBeta.StokesSymmetryConstant

/-! ## §1. Eisenstein `ℤ[ω]` Cusp Lattice, Gluing Degree & Three `4₁` Flat Connections -/

section EisensteinGluingVariety

/-- Evaluation of the 6th cyclotomic / Eisenstein minimal polynomial `1 - w + w²` in `R`. -/
def eisensteinEval {R : Type*} [CommRing R] (w : R) : R :=
  1 - w + w ^ 2

/-- Polynomial `X² - X + 1 ∈ R[X]` cutting out the regular ideal tetrahedron cross-ratio `ω`. -/
noncomputable def eisensteinMinPoly (R : Type*) [CommRing R] : R[X] :=
  X ^ 2 - X + 1

/-- Cubic polynomial `(X + 1)(X² - X + 1) = X³ + 1 ∈ R[X]` uniting the abelian flat boundary
root `-1` with the two Galois-conjugate geometric roots `(ω, 1 - ω)`. -/
noncomputable def flatSaddleCubicPoly (R : Type*) [CommRing R] : R[X] :=
  (X + 1) * eisensteinMinPoly R

/-- SnapPy's cleared symmetric two-tetrahedra edge-gluing polynomial `X⁴ - (1 - X)² ∈ R[X]`
for `4₁` (`z₁ = z₂ = X` in `z₁² z₂² = (1 - z₁)(1 - z₂)`). -/
noncomputable def snappySymEdgePoly (R : Type*) [CommRing R] : R[X] :=
  X ^ 4 - (1 - X) ^ 2

/-- **Exact cyclotomic & tetrahedral cross-ratio identities over `[CommRing R]`.**
Whenever `1 - ω + ω² = 0`:
1. `(ω + 1)(1 - ω + ω²) = ω³ + 1` and `(ω - 1)(ω + 1)(ω² + ω + 1)(1 - ω + ω²) = ω⁶ - 1`;
2. `ω³ = -1` and `ω⁶ = 1`;
3. `(2ω - 1)² = -3` (Eisenstein discriminant `-3`, corresponding to `ℚ(√-3)` and `τ = -i√3`);
4. `ω(1 - ω) = 1` (tetrahedral edge parameters `(ω, (1-ω)⁻¹, 1 - ω⁻¹)` all equal `ω`);
5. `eisensteinEval (1 - ω) = 0` (`ω̄ = 1 - ω` is the conjugate root). -/
theorem eisenstein_minimal_poly {R : Type*} [CommRing R] (ω : R) :
    ((ω + 1) * eisensteinEval ω = ω ^ 3 + 1 ∧
      (ω - 1) * (ω + 1) * (ω ^ 2 + ω + 1) * eisensteinEval ω = ω ^ 6 - 1) ∧
    (eisensteinEval ω = 0 →
      ω ^ 3 = -1 ∧
      ω ^ 6 = 1 ∧
      (2 * ω - 1) ^ 2 = -3 ∧
      ω * (1 - ω) = 1 ∧
      eisensteinEval (1 - ω) = 0) := by
  refine ⟨⟨by unfold eisensteinEval; ring, by unfold eisensteinEval; ring⟩, fun h => ?_⟩
  unfold eisensteinEval at h
  have hcube : ω ^ 3 = -1 := by
    linear_combination (ω + 1) * h
  have hsix : ω ^ 6 = 1 := by
    linear_combination (ω ^ 3 - 1) * (ω + 1) * h
  have hdisc : (2 * ω - 1) ^ 2 = -3 := by
    linear_combination 4 * h
  have htet : ω * (1 - ω) = 1 := by
    linear_combination -h
  have hconj : eisensteinEval (1 - ω) = 0 := by
    unfold eisensteinEval
    linear_combination h
  exact ⟨hcube, hsix, hdisc, htet, hconj⟩

/-- **Factorization and degrees of the `4₁` two-tetrahedra gluing polynomials.**
Over any nontrivial commutative ring `R`:
1. SnapPy's symmetric two-tetrahedra edge polynomial factors as `(X² - X + 1)(X² + X - 1)`;
2. `flatSaddleCubicPoly R = X³ + 1`;
3. `natDegree (eisensteinMinPoly R) = 2` (the two conjugate geometric saddles);
4. `natDegree (flatSaddleCubicPoly R) = 3` (all three `SU(2)/SL₂(ℂ)` flat-connection branches). -/
theorem two_tetrahedra_gluing_variety_degree (R : Type*) [CommRing R] [Nontrivial R] :
    snappySymEdgePoly R = eisensteinMinPoly R * (X ^ 2 + X - 1) ∧
    flatSaddleCubicPoly R = X ^ 3 + 1 ∧
    (eisensteinMinPoly R).natDegree = 2 ∧
    (flatSaddleCubicPoly R).natDegree = 3 := by
  have hsnap : snappySymEdgePoly R = eisensteinMinPoly R * (X ^ 2 + X - 1) := by
    unfold snappySymEdgePoly eisensteinMinPoly
    ring
  have hcubic : flatSaddleCubicPoly R = (X : R[X]) ^ 3 + 1 := by
    unfold flatSaddleCubicPoly eisensteinMinPoly
    ring
  have hdeg2 : (eisensteinMinPoly R).natDegree = 2 := by
    unfold eisensteinMinPoly
    compute_degree!
  have hdeg3 : (flatSaddleCubicPoly R).natDegree = 3 := by
    rw [hcubic]
    compute_degree!
  exact ⟨hsnap, hcubic, hdeg2, hdeg3⟩

/-- Explicit 3-element `Finset` of `x³ + 1 = 0` saddle roots `{-1, ω, 1 - ω}` in `R`, indexing the
abelian/trivial branch `-1` and the conjugate geometric branches `(ω, 1 - ω)`. -/
def flatConnectionRoots {R : Type*} [CommRing R] [DecidableEq R] (ω : R) : Finset R :=
  {-1, ω, 1 - ω}

/-- **Exact `[3 : 1]` saddle cardinality & root completeness (`three_flat_connections_card`).**
Over any integral domain `R` with `(3 : R) ≠ 0`, if `1 - ω + ω² = 0`, then `{-1, ω, 1 - ω}` has
exact cardinality `3` and is the complete solution set of `x³ + 1 = 0` in `R`. -/
theorem three_flat_connections_card {R : Type*} [CommRing R] [IsDomain R] [DecidableEq R]
    {ω : R} (hω : eisensteinEval ω = 0) (h3 : (3 : R) ≠ 0) :
    (flatConnectionRoots ω).card = 3 ∧
    (∀ x : R, x ^ 3 + 1 = 0 ↔ x ∈ flatConnectionRoots ω) := by
  have hne1 : (-1 : R) ≠ ω := by
    intro heq
    apply h3
    unfold eisensteinEval at hω
    rw [← heq] at hω
    linear_combination hω
  have hne2 : (-1 : R) ≠ 1 - ω := by
    intro heq
    have hw2 : ω = 2 := by linear_combination heq
    apply h3
    unfold eisensteinEval at hω
    rw [hw2] at hω
    linear_combination hω
  have hne3 : ω ≠ 1 - ω := by
    intro heq
    have h2w : 2 * ω = 1 := by linear_combination heq
    apply h3
    unfold eisensteinEval at hω
    linear_combination 4 * hω - (2 * ω - 1) * h2w
  have hcard : (flatConnectionRoots ω).card = 3 := by
    unfold flatConnectionRoots
    rw [Finset.card_insert_of_notMem, Finset.card_insert_of_notMem, Finset.card_singleton]
    · simp [hne3]
    · simp [hne1, hne2]
  refine ⟨hcard, fun x => ?_⟩
  unfold flatConnectionRoots
  simp only [Finset.mem_insert, Finset.mem_singleton]
  have hfac : x ^ 3 + 1 = (x + 1) * (x - ω) * (x - (1 - ω)) := by
    unfold eisensteinEval at hω
    linear_combination (x + 1) * hω
  rw [hfac, mul_eq_zero, mul_eq_zero]
  constructor
  · rintro ((hx1 | hx2) | hx3)
    · left; linear_combination hx1
    · right; left; linear_combination hx2
    · right; right; linear_combination hx3
  · rintro (rfl | rfl | rfl)
    · left; left; ring
    · left; right; ring
    · right; ring

end EisensteinGluingVariety

/-! ## §2. `4₁` `A`-Polynomial Degree-`3` `L`-Specialization, NZ Cusp Jet & GGM `A_ω = 3` -/

section APolynomialAndGGMStokesThree

/-- Laurent trace polynomial `B(M, M⁻¹) = M⁴ - M² - 2 - M⁻² + M⁻⁴` of the `4₁` `A`-polynomial. -/
def bCoeffFourOne {R : Type*} [CommRing R] (M Minv : R) : R :=
  M ^ 4 - M ^ 2 - 2 - Minv ^ 2 + Minv ^ 4

/-- CCGLS `4₁` `A`-polynomial in `L` (`L_CCGLS(0) = -1` on the geometric branch, `+1` on abelian):
`(L - 1)(L² - B(M, M⁻¹) L + 1) ∈ R[L]`. -/
noncomputable def aPolyCCGLS {R : Type*} [CommRing R] (M Minv : R) : R[X] :=
  (X - 1) * (X ^ 2 - C (bCoeffFourOne M Minv) * X + 1)

/-- Garoufalidis–Kashaev AJ `4₁` `A`-polynomial in `L` (`L_AJ = -L_CCGLS` on the non-abelian
factor, so all 3 branches coalesce at `L_AJ = 1` when `M = 1`):
`(L - 1)(L² + B(M, M⁻¹) L + 1) ∈ R[L]`. -/
noncomputable def aPolyAJ {R : Type*} [CommRing R] (M Minv : R) : R[X] :=
  (X - 1) * (X ^ 2 + C (bCoeffFourOne M Minv) * X + 1)

/-- **Degree-`3` `L`-span and `M = 1` specialization of the `4₁` `A`-polynomial.**
Over `[CommRing R] [Nontrivial R]`:
1. Both `aPolyCCGLS M Minv` and `aPolyAJ M Minv` have exact `natDegree = 3` in `L` for all
   `(M, Minv)` (matching the order-`3` Garoufalidis–Kashaev `q`-difference equation);
2. At `M = Minv = 1`, `bCoeffFourOne 1 1 = -2`, so `aPolyAJ 1 1 = (X - 1)³` (`L + L⁻¹ - 2 =
   L⁻¹(L - 1)²` times the abelian branch `L - 1`) and `aPolyCCGLS 1 1 = (X - 1)(X + 1)²`;
3. Cleared Laurent form: when `L * Linv = 1`, `(M² - 1)(L + Linv + bCoeffFourOne M Minv) * L`
   equals `(M² - 1)((L - 1)² + (2 + bCoeffFourOne M Minv) * L)`. -/
theorem aPolyFourOne_degree_and_meridian_one {R : Type*} [CommRing R] [Nontrivial R]
    (M Minv : R) :
    (aPolyCCGLS M Minv).natDegree = 3 ∧
    (aPolyAJ M Minv).natDegree = 3 ∧
    aPolyAJ (1 : R) 1 = (X - 1) ^ 3 ∧
    aPolyCCGLS (1 : R) 1 = (X - 1) * (X + 1) ^ 2 ∧
    (∀ L Linv : R, L * Linv = 1 →
      (M ^ 2 - 1) * (L + Linv + bCoeffFourOne M Minv) * L =
        (M ^ 2 - 1) * ((L - 1) ^ 2 + (2 + bCoeffFourOne M Minv) * L)) := by
  have hdegC : (aPolyCCGLS M Minv).natDegree = 3 := by
    have hexp : aPolyCCGLS M Minv =
        X ^ 3 - C (bCoeffFourOne M Minv + 1) * X ^ 2 +
          C (bCoeffFourOne M Minv + 1) * X - 1 := by
      unfold aPolyCCGLS; simp only [map_add, map_one]; ring
    rw [hexp]
    compute_degree!
  have hdegA : (aPolyAJ M Minv).natDegree = 3 := by
    have hexp : aPolyAJ M Minv =
        X ^ 3 + C (bCoeffFourOne M Minv - 1) * X ^ 2 -
          C (bCoeffFourOne M Minv - 1) * X - 1 := by
      unfold aPolyAJ; simp only [map_sub, map_one]; ring
    rw [hexp]
    compute_degree!
  have hb1 : bCoeffFourOne (1 : R) 1 = -2 := by
    unfold bCoeffFourOne; norm_num
  have hAJ1 : aPolyAJ (1 : R) 1 = (X - 1) ^ 3 := by
    unfold aPolyAJ; rw [hb1]; simp only [map_neg, map_ofNat]; ring
  have hCC1 : aPolyCCGLS (1 : R) 1 = (X - 1) * (X + 1) ^ 2 := by
    unfold aPolyCCGLS; rw [hb1]; simp only [map_neg, map_ofNat]; ring
  refine ⟨hdegC, hdegA, hAJ1, hCC1, fun L Linv hL => ?_⟩
  linear_combination (M ^ 2 - 1) * hL

/-- **Exact Neumann–Zagier cusp-modulus & quartic-jet relation from `bCoeffFourOne`.**
Setting `M² + M⁻² = 2 + δ_X` (with `M * Minv = 1`), the non-abelian `A`-polynomial trace satisfies
`-bCoeffFourOne M Minv = 2 - 3 δ_X - δ_X²` (`δ_Y = -3 δ_X - δ_X²`). Matching `2 cosh u - 2 =
u² + u⁴/12 + …` and `2 cosh(τ u + v₃ u³ + …) - 2 = τ² u² + (2 τ v₃ + τ⁴/12) u⁴ + …` (cleared by
`12`) pins `τ² = -3` and `24 τ v₃ + τ⁴ = -15`, which algebraically forces `τ * v₃ = -1` and
`3 * v₃ = τ` (deriving the `τ = -i√3`, `v₃ = -i√3/3` relation of `FigureEightQuarticCoefficient`). -/
theorem aPoly_nz_cusp_jet {R : Type*} [CommRing R] :
    (∀ M Minv δ_X : R, M * Minv = 1 → M ^ 2 + Minv ^ 2 = 2 + δ_X →
      -bCoeffFourOne M Minv = 2 - 3 * δ_X - δ_X ^ 2) ∧
    (∀ τ v₃ : R, τ ^ 2 = -3 → 24 * τ * v₃ + τ ^ 4 = -15 →
      24 * (τ * v₃ + 1) = 0 ∧ 24 * (3 * v₃ - τ) = 0) := by
  refine ⟨fun M Minv δ_X hM hX => ?_, fun τ v₃ hτ hv => ?_⟩
  · unfold bCoeffFourOne
    linear_combination -(M ^ 2 + Minv ^ 2 + 2 + δ_X) * hX + hX + 2 * (M * Minv + 1) * hM
  · have hτ4 : τ ^ 4 = 9 := by linear_combination (τ ^ 2 - 3) * hτ
    have h1 : 24 * (τ * v₃ + 1) = 0 := by linear_combination hv - hτ4
    have h2 : 24 * (3 * v₃ - τ) = 0 := by linear_combination -τ * h1 + 24 * v₃ * hτ
    exact ⟨h1, h2⟩

/-- GGM eq. (59a) constant cusp-gluing matrix `A_GGM = [[0, 1], [1, 1]]`. -/
def ggmMatA (R : Type*) [CommRing R] : Matrix (Fin 2) (Fin 2) R :=
  !![0, 1; 1, 1]

/-- GGM eq. (59a) constant intersection matrix `B_GGM = [[0, 1], [1, 0]]`. -/
def ggmMatB (R : Type*) [CommRing R] : Matrix (Fin 2) (Fin 2) R :=
  !![0, 1; 1, 0]

/-- GGM eq. (59a) constant cusp-gluing matrix `C_GGM = [[0, -1], [1, 2]]`. -/
def ggmMatC (R : Type*) [CommRing R] : Matrix (Fin 2) (Fin 2) R :=
  !![0, -1; 1, 2]

/-- Twice the GGM Stokes matrix: `S̃(W) = A_GGM · W · B_GGM · Wᵀ · C_GGM` (GGM 2012.00062 eq. 59a). -/
def ggmSandwich2 {R : Type*} [CommRing R] (W : Matrix (Fin 2) (Fin 2) R) :
    Matrix (Fin 2) (Fin 2) R :=
  ggmMatA R * W * ggmMatB R * W.transpose * ggmMatC R

/-- Base-point Wronskian `W_{-1}(0) = [[0, -2], [1, 1]]` at `q = 0` from GGM eqs. (51a)/(51b). -/
def ggmWronskianAtZero (R : Type*) [CommRing R] : Matrix (Fin 2) (Fin 2) R :=
  !![0, -2; 1, 1]

/-- **Algebraic proof of GGM eq. (65) `A_ω = 3` symmetry, unimodularity, and `q → 0` base matrix.**
Over any `[CommRing R]`, for **every** `2 × 2` Wronskian matrix `W`:
1. `S̃₀₁(W) + S̃₁₀(W) = 3 · S̃₀₀(W)` (`S⁺₁₂(q) + S⁺₂₁(q) = 3 · S⁺₁₁(q)` holds identically as a
   bilinear identity of the two-tetrahedra cusp matrices `(A_GGM, B_GGM, C_GGM)`, where `3 = 2 + 1`);
2. `det S̃(W) = (det W)²` (so `det W = 2` from GGM Theorem 9 forces `det(2 S⁺) = 4`, i.e. `det S⁺ = 1`);
3. At `W_{-1}(0) = [[0, -2], [1, 1]]`, `det W_{-1}(0) = 2` and `S̃(W_{-1}(0)) = [[2, 6], [0, 2]] =
   2 · [[1, 3], [0, 1]]` (reproducing GGM eq. 60's Stokes integer `3`!). -/
theorem ggm_stokes_symmetry_three {R : Type*} [CommRing R] (W : Matrix (Fin 2) (Fin 2) R) :
    ggmSandwich2 W 0 1 + ggmSandwich2 W 1 0 = 3 * ggmSandwich2 W 0 0 ∧
    (ggmSandwich2 W).det = W.det ^ 2 ∧
    (ggmWronskianAtZero R).det = 2 ∧
    ggmSandwich2 (ggmWronskianAtZero R) = !![(2 : R), 6; 0, 2] := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp only [ggmSandwich2, ggmMatA, ggmMatB, ggmMatC, Matrix.mul_apply, Fin.sum_univ_two,
      Matrix.transpose_apply, Matrix.of_apply, Matrix.cons_val_zero, Matrix.cons_val_one]
    ring
  · simp only [ggmSandwich2, Matrix.det_mul, Matrix.det_transpose, ggmMatA, ggmMatB, ggmMatC,
      Matrix.det_fin_two_of]
    ring
  · simp [ggmWronskianAtZero, Matrix.det_fin_two_of]
  · ext i j
    fin_cases i <;> fin_cases j <;>
      · simp only [ggmSandwich2, ggmWronskianAtZero, ggmMatA, ggmMatB, ggmMatC, Matrix.mul_apply,
          Fin.sum_univ_two, Matrix.transpose_apply, Matrix.of_apply, Matrix.cons_val_zero,
          Matrix.cons_val_one]
        norm_num

/-- **Wiring into `QOU.QBeta.StokesSymmetryConstant` & `DeltaLambdaBindingAssembly`.**
Over any field `K`, `S⁺(i) = 2⁻¹ • ggmSandwich2 (W i)` satisfies
`symmetryConstant S⁺₀₀ S⁺₀₁ S⁺₁₀ i = 3` at every index `i` with `S⁺₀₀ i ≠ 0`, and specializing
`DeltaLambdaBindingAssembly.binding_formula_of_imV₄₁` to `A_ω = 3` yields
`3 * Im 𝔙₄₁(𝔲) = (3 * √3 / 4) * (Re²𝔲 - Im²𝔲)`. -/
theorem ggm_discharges_symmetryConstant_and_imV41
    {K : Type*} [Field K] {ι : Type*}
    (W : ι → Matrix (Fin 2) (Fin 2) K)
    (hne : ∀ i, ((2 : K)⁻¹ * ggmSandwich2 (W i) 0 0) ≠ 0) :
    (∀ i, symmetryConstant
      (fun j => (2 : K)⁻¹ * ggmSandwich2 (W j) 0 0)
      (fun j => (2 : K)⁻¹ * ggmSandwich2 (W j) 0 1)
      (fun j => (2 : K)⁻¹ * ggmSandwich2 (W j) 1 0) i = 3) ∧
    (∀ 𝔲 : ℂ, (3 : ℝ) * (V₄₁ 𝔲).im = 3 * cuspModulus * (𝔲.re ^ 2 - 𝔲.im ^ 2)) := by
  refine ⟨symmetryConstant_const (fun i => ?_) hne, fun 𝔲 => binding_formula_of_imV₄₁ 3 𝔲⟩
  have hsym := (ggm_stokes_symmetry_three (W i)).1
  calc (2 : K)⁻¹ * ggmSandwich2 (W i) 0 1 + (2 : K)⁻¹ * ggmSandwich2 (W i) 1 0
      = (2 : K)⁻¹ * (ggmSandwich2 (W i) 0 1 + ggmSandwich2 (W i) 1 0) := by ring
    _ = (2 : K)⁻¹ * (3 * ggmSandwich2 (W i) 0 0) := by rw [hsym]
    _ = 3 * ((2 : K)⁻¹ * ggmSandwich2 (W i) 0 0) := by ring

end APolynomialAndGGMStokesThree

/-! ## §3. `6q / 9q / 12q` `SU(3)_c`-Singlet Multiplicity via Hook-Length Formula -/

section SkewHoweSingletMultiplicity

/-- Rectangular 3-row partition `[A, A, A] ⊢ 3A` cutting out `Hom_{SU(3)_c}((ℂ³)^{⊗ 3A}, 1)`. -/
def rectThree (A : ℕ) : Partition := [A, A, A]

/-- **Exact hook-length formula on `rectThree A = [A, A, A]` for all `A : ℕ`.**
Every cell `(i, j)` (`i < 3`, `j < A`) has hook length `(A - j) + (2 - i)`. -/
theorem hookLength_rectThree (A i j : ℕ) (hi : i < 3) (hj : j < A) :
    Partition.hookLength (rectThree A) i j = A - j + (2 - i) := by
  rcases i with _ | _ | _ | i
  · simp [Partition.hookLength, rectThree, hj]
    omega
  · simp [Partition.hookLength, rectThree, hj]
    omega
  · simp [Partition.hookLength, rectThree, hj]
    omega
  · omega

/-- Product of all hook lengths of `rectThree A` across its `3 × A` cells. -/
def hookProdRectThree (A : ℕ) : ℕ :=
  ∏ i ∈ Finset.range 3, ∏ j ∈ Finset.range A, Partition.hookLength (rectThree A) i j

private theorem row_hook_prod_eq_factorial (A k : ℕ) :
    k.factorial * (∏ j ∈ Finset.range A, (A - j + k)) = (A + k).factorial := by
  induction A with
  | zero => simp
  | succ A ih =>
    rw [Finset.prod_range_succ']
    have hshift : (∏ j ∈ Finset.range A, (A + 1 - (j + 1) + k)) =
        ∏ j ∈ Finset.range A, (A - j + k) := by
      refine Finset.prod_congr rfl fun j _ => ?_
      omega
    rw [hshift, ← mul_assoc, ih]
    have hsucc : A + 1 - 0 + k = A + k + 1 := by omega
    rw [hsucc, mul_comm ((A + k).factorial), ← Nat.factorial_succ]
    congr 1
    omega

/-- **General-`A` hook-product identity (`3D` Catalan denominator):**
`2 * hookProdRectThree A = A! * (A + 1)! * (A + 2)!` for every `A : ℕ`. -/
theorem two_mul_hookProdRectThree (A : ℕ) :
    2 * hookProdRectThree A = A.factorial * (A + 1).factorial * (A + 2).factorial := by
  unfold hookProdRectThree
  simp only [Finset.prod_range_succ, Finset.prod_range_zero, one_mul]
  have hrow0 : (∏ j ∈ Finset.range A, Partition.hookLength (rectThree A) 0 j) =
      ∏ j ∈ Finset.range A, (A - j + 2) :=
    Finset.prod_congr rfl fun j hj => hookLength_rectThree A 0 j (by omega) (Finset.mem_range.mp hj)
  have hrow1 : (∏ j ∈ Finset.range A, Partition.hookLength (rectThree A) 1 j) =
      ∏ j ∈ Finset.range A, (A - j + 1) :=
    Finset.prod_congr rfl fun j hj => hookLength_rectThree A 1 j (by omega) (Finset.mem_range.mp hj)
  have hrow2 : (∏ j ∈ Finset.range A, Partition.hookLength (rectThree A) 2 j) =
      ∏ j ∈ Finset.range A, (A - j + 0) :=
    Finset.prod_congr rfl fun j hj => hookLength_rectThree A 2 j (by omega) (Finset.mem_range.mp hj)
  rw [hrow0, hrow1, hrow2]
  have r0 := row_hook_prod_eq_factorial A 2
  have r1 := row_hook_prod_eq_factorial A 1
  have r2 := row_hook_prod_eq_factorial A 0
  simp only [Nat.factorial_zero, Nat.factorial_one, Nat.factorial_two, one_mul, add_zero]
    at r0 r1 r2 ⊢
  calc 2 * ((∏ j ∈ Finset.range A, (A - j + 2)) *
          (∏ j ∈ Finset.range A, (A - j + 1)) *
          (∏ j ∈ Finset.range A, (A - j)))
      = (2 * ∏ j ∈ Finset.range A, (A - j + 2)) *
          (∏ j ∈ Finset.range A, (A - j + 1)) *
          (∏ j ∈ Finset.range A, (A - j)) := by ring
    _ = (A + 2).factorial * (A + 1).factorial * A.factorial := by rw [r0, r1, r2]
    _ = A.factorial * (A + 1).factorial * (A + 2).factorial := by ring

/-- `SU(3)_c`-singlet subspace dimension `dim Hom_{SU(3)_c}((ℂ³)^{⊗ 3A}, 1) = (3A)! / hookProd`
given by the hook-length formula on `rectThree A = [A, A, A]`. -/
def su3SingletDim (A : ℕ) : ℕ :=
  (3 * A).factorial / hookProdRectThree A

/-- Number of hidden-colour reconnection channels `su3SingletDim A - 1` orthogonal to the unique
factorized `A`-nucleon colour-singlet channel `|1^A⟩`. -/
def hiddenColourDim (A : ℕ) : ℕ :=
  su3SingletDim A - 1

/-- **Exact `SU(3)_c`-singlet & hidden-colour multiplicities for `A = 1, 2, 3, 4` (`3q–12q`):**
- `A = 1` (`3q` nucleon): `1` singlet, `0` hidden-colour channels;
- `A = 2` (`6q` deuteron): **`5` singlets** = `1` factorized `|11⟩` + **`4` hidden-colour** `8_c ⊗ 8_c → 1_c` channels (`2 × 2 = 4`);
- `A = 3` (`9q` triton / `³He`): **`42` singlets** = `1` factorized + **`41` hidden-colour** channels;
- `A = 4` (`12q` `α`-particle `⁴He`): **`462` singlets** = `1` factorized + **`461` hidden-colour** channels. -/
theorem su3SingletDim_light_nuclei :
    (su3SingletDim 1 = 1 ∧ hiddenColourDim 1 = 0) ∧
    (su3SingletDim 2 = 5 ∧ hiddenColourDim 2 = 4 ∧ hiddenColourDim 2 = 2 * 2) ∧
    (su3SingletDim 3 = 42 ∧ hiddenColourDim 3 = 41) ∧
    (su3SingletDim 4 = 462 ∧ hiddenColourDim 4 = 461) := by
  decide

end SkewHoweSingletMultiplicity

/-! ## §4. Exact `6q` `U_q(𝔰𝔩₃)` Jimbo Braiding Overlap & `q`-Fierz Casimir Spectrum -/

section JimboSixQuarkOverlapAndCasimir

variable {K : Type*} [Field K]

/-- Six-fold colour tensor `(K³)^{⊗ 6}`. -/
abbrev T6 (K : Type*) := Fin 3 → Fin 3 → Fin 3 → Fin 3 → Fin 3 → Fin 3 → K

/-- Factorized `6q` two-nucleon `U_q(𝔰𝔩₃)` colour-singlet state `|Ψ₁₁(q)⟩ = ε_q ⊗ ε_q`. -/
def eps6 (q : K) : T6 K :=
  fun a b c d e f => eps q a b c * eps q d e f

/-- Inter-nucleon Jimbo braiding `Ř_{2,3}(q)` exchanging quark `2` (last quark of nucleon `0`)
and quark `3` (first quark of nucleon `1`) on `(K³)^{⊗ 6}`. -/
def R23_six (q : K) (w : T6 K) : T6 K :=
  fun a b c d e f => R q (fun x y => w a b x y e f) c d

/-- Partial norm-squared of `eps q` fixing the third colour index `c`. -/
def epsRightSq (q : K) (c : Fin 3) : K :=
  ∑ a : Fin 3, ∑ b : Fin 3, eps q a b c * eps q a b c

/-- Partial norm-squared of `eps q` fixing the first colour index `d`. -/
def epsLeftSq (q : K) (d : Fin 3) : K :=
  ∑ e : Fin 3, ∑ f : Fin 3, eps q d e f * eps q d e f

private theorem epsRight_orthog (q : K) {c c' : Fin 3} (hne : c ≠ c') :
    (∑ a : Fin 3, ∑ b : Fin 3, eps q a b c * eps q a b c') = 0 := by
  fin_cases c <;> fin_cases c' <;> try contradiction
  all_goals
    simp [eps, Fin.sum_univ_three]

private theorem epsLeft_orthog (q : K) {d d' : Fin 3} (hne : d ≠ d') :
    (∑ e : Fin 3, ∑ f : Fin 3, eps q d e f * eps q d' e f) = 0 := by
  fin_cases d <;> fin_cases d' <;> try contradiction
  all_goals
    simp [eps, Fin.sum_univ_three]

/-- Full norm-squared of the 3-quark `q`-singlet `eps q` equals `(1 + q⁻²)(1 + q⁻² + q⁻⁴) = [3]_q!/q³`. -/
theorem eps_norm_sq (q : K) :
    (∑ c : Fin 3, epsRightSq q c) = (1 + q⁻¹ ^ 2) * (1 + q⁻¹ ^ 2 + q⁻¹ ^ 4) := by
  simp [epsRightSq, eps, Fin.sum_univ_three]
  ring

/-- **Exact `6q` `U_q(𝔰𝔩₃)` inter-nucleon braiding overlap (`sixQuark_R23_overlap`).**
Pairing `eps6 q` with `R23_six q (eps6 q)` over all `3⁶ = 729` colour configurations equals
`(q³ / (q² + 1 + q⁻²))` times `‖eps q‖⁴` (`= 1/3` at `q = 1`). -/
theorem sixQuark_R23_overlap (q : K) (hq : q ≠ 0) (hq3 : q ^ 2 + 1 + q⁻¹ ^ 2 ≠ 0) :
    (∑ a : Fin 3, ∑ b : Fin 3, ∑ c : Fin 3, ∑ d : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
        eps6 q a b c d e f * R23_six q (eps6 q) a b c d e f) =
      (q ^ 3 / (q ^ 2 + 1 + q⁻¹ ^ 2)) * (∑ c : Fin 3, epsRightSq q c) ^ 2 := by
  have hred : ∀ c d : Fin 3,
      (∑ a : Fin 3, ∑ b : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
          eps6 q a b c d e f * R23_six q (eps6 q) a b c d e f) =
        if c = d then q * epsRightSq q c * epsLeftSq q c
        else if d < c then (q - q⁻¹) * epsRightSq q c * epsLeftSq q d
        else 0 := by
    intro c d
    by_cases hcd : c = d
    · subst hcd
      simp only [eps6, R23_six, R, ↓reduceIte]
      calc (∑ a : Fin 3, ∑ b : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
              (eps q a b c * eps q c e f) * (q * (eps q a b c * eps q c e f)))
          = q * (∑ a : Fin 3, ∑ b : Fin 3, eps q a b c * eps q a b c *
              (∑ e : Fin 3, ∑ f : Fin 3, eps q c e f * eps q c e f)) := by
              simp_rw [Finset.mul_sum]
              refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
                Finset.sum_congr rfl fun e _ => Finset.sum_congr rfl fun f _ => ?_
              ring
        _ = q * epsRightSq q c * epsLeftSq q c := by
              unfold epsRightSq epsLeftSq
              simp_rw [← Finset.sum_mul]
              ring
    · simp only [eps6, R23_six, R, hcd, ↓reduceIte]
      have hswap : (∑ a : Fin 3, ∑ b : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
            (eps q a b c * eps q d e f) * (eps q a b d * eps q c e f)) = 0 := by
        calc (∑ a : Fin 3, ∑ b : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
                (eps q a b c * eps q d e f) * (eps q a b d * eps q c e f))
            = (∑ a : Fin 3, ∑ b : Fin 3, eps q a b c * eps q a b d) *
                (∑ e : Fin 3, ∑ f : Fin 3, eps q d e f * eps q c e f) := by
                simp_rw [Finset.sum_mul, Finset.mul_sum]
                refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
                  Finset.sum_congr rfl fun e _ => Finset.sum_congr rfl fun f _ => ?_
                ring
          _ = 0 := by rw [epsRight_orthog q hcd, zero_mul]
      by_cases hdc : d < c
      · simp_rw [if_pos hdc]
        have hsplit : (∑ a : Fin 3, ∑ b : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
              (eps q a b c * eps q d e f) *
                (eps q a b d * eps q c e f + (q - q⁻¹) * (eps q a b c * eps q d e f))) =
            (∑ a : Fin 3, ∑ b : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
              (eps q a b c * eps q d e f) * (eps q a b d * eps q c e f)) +
            (q - q⁻¹) * epsRightSq q c * epsLeftSq q d := by
          unfold epsRightSq epsLeftSq
          rw [mul_assoc]
          simp_rw [mul_add, Finset.sum_add_distrib]
          congr 1
          simp_rw [Finset.sum_mul, Finset.mul_sum]
          refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ =>
            Finset.sum_congr rfl fun e _ => Finset.sum_congr rfl fun f _ => ?_
          ring
        rw [hsplit, hswap, zero_add]
      · simp_rw [if_neg hdc, add_zero]
        exact hswap
  have hcomm : (∑ a : Fin 3, ∑ b : Fin 3, ∑ c : Fin 3, ∑ d : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
        eps6 q a b c d e f * R23_six q (eps6 q) a b c d e f) =
      ∑ c : Fin 3, ∑ d : Fin 3,
        (∑ a : Fin 3, ∑ b : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
          eps6 q a b c d e f * R23_six q (eps6 q) a b c d e f) := by
    have s1 : (∑ a : Fin 3, ∑ b : Fin 3, ∑ c : Fin 3, ∑ d : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
          eps6 q a b c d e f * R23_six q (eps6 q) a b c d e f) =
        ∑ a : Fin 3, ∑ c : Fin 3, ∑ b : Fin 3, ∑ d : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
          eps6 q a b c d e f * R23_six q (eps6 q) a b c d e f :=
      Finset.sum_congr rfl fun a _ => Finset.sum_comm
    have s2 : (∑ a : Fin 3, ∑ c : Fin 3, ∑ b : Fin 3, ∑ d : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
          eps6 q a b c d e f * R23_six q (eps6 q) a b c d e f) =
        ∑ c : Fin 3, ∑ a : Fin 3, ∑ b : Fin 3, ∑ d : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
          eps6 q a b c d e f * R23_six q (eps6 q) a b c d e f :=
      Finset.sum_comm
    have s3 : (∑ c : Fin 3, ∑ a : Fin 3, ∑ b : Fin 3, ∑ d : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
          eps6 q a b c d e f * R23_six q (eps6 q) a b c d e f) =
        ∑ c : Fin 3, ∑ a : Fin 3, ∑ d : Fin 3, ∑ b : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
          eps6 q a b c d e f * R23_six q (eps6 q) a b c d e f :=
      Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun a _ => Finset.sum_comm
    have s4 : (∑ c : Fin 3, ∑ a : Fin 3, ∑ d : Fin 3, ∑ b : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
          eps6 q a b c d e f * R23_six q (eps6 q) a b c d e f) =
        ∑ c : Fin 3, ∑ d : Fin 3, ∑ a : Fin 3, ∑ b : Fin 3, ∑ e : Fin 3, ∑ f : Fin 3,
          eps6 q a b c d e f * R23_six q (eps6 q) a b c d e f :=
      Finset.sum_congr rfl fun c _ => Finset.sum_comm
    exact s1.trans (s2.trans (s3.trans s4))
  rw [hcomm]
  simp_rw [hred]
  rw [eps_norm_sq]
  simp [epsRightSq, epsLeftSq, eps, Fin.sum_univ_three]
  have hq3_mul : q ^ 2 * (q ^ 2 + 1 + q⁻¹ ^ 2) = q ^ 4 + q ^ 2 + 1 := by
    field_simp
  have hq4_ne : q ^ 4 + q ^ 2 + 1 ≠ 0 := by
    intro hz
    exact mul_ne_zero (pow_ne_zero 2 hq) hq3 (hq3_mul.trans hz)
  field_simp [hq, hq3, hq4_ne]
  try ring

/-- **Exact hidden-colour transition norm-squared & `q`-Fierz Casimir characteristic polynomial.**
On the `2`-state `{|11⟩_q, |88⟩_q}` subspace:
1. Using `Ř² = (q - q⁻¹)Ř + 1`, the squared off-diagonal coupling out of `|11⟩_q` under `Ř_{2,3}(q)`
   is `v_q² = 1 + (q - q⁻¹)(q³/[3]_q) - (q³/[3]_q)² = [2]_q [4]_q / [3]_q²` (`8/9` at `q = 1`);
2. The `q`-Fierz colour-exchange operator `𝓕_q = ½(Ř_{2,3}(q) - (q³/[3]_q) I)` has diagonal `(0, -(q³ + q⁻³)/(2[3]_q))`
   and off-diagonal squared `v_q² / 4`, with characteristic polynomial factoring into exact roots
   `+[2]_q / (2 [3]_q)` (`+1/3` at `q = 1`) and `-[4]_q / (2 [3]_q)` (`-2/3` at `q = 1`, attractive!). -/
theorem qFierz_charPoly_roots (q μ : K) (h2 : (2 : K) ≠ 0) (hq : q ≠ 0)
    (hq3 : q ^ 2 + 1 + q⁻¹ ^ 2 ≠ 0) :
    let q2 := q + q⁻¹
    let q3 := q ^ 2 + 1 + q⁻¹ ^ 2
    let q4 := q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3
    (1 + (q - q⁻¹) * (q ^ 3 / q3) - (q ^ 3 / q3) ^ 2 = (q2 * q4) / q3 ^ 2) ∧
    ((0 - μ) * (-(q ^ 3 + q⁻¹ ^ 3) / (2 * q3) - μ) - (q2 * q4) / (4 * q3 ^ 2) =
      (μ - q2 / (2 * q3)) * (μ + q4 / (2 * q3))) := by
  dsimp only
  set q3 := q ^ 2 + 1 + q⁻¹ ^ 2 with hq3_def
  have h2q3 : 2 * q3 ≠ 0 := mul_ne_zero h2 hq3
  have h4q3sq : 4 * q3 ^ 2 ≠ 0 := by
    have h4 : (4 : K) = 2 * 2 := by norm_num
    rw [h4]
    exact mul_ne_zero (mul_ne_zero h2 h2) (pow_ne_zero 2 hq3)
  have hident1 : q3 ^ 2 + (q - q⁻¹) * q ^ 3 * q3 - q ^ 6 =
      (q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) := by
    rw [hq3_def]
    field_simp [hq]
    try ring
  constructor
  · apply mul_right_cancel₀ (pow_ne_zero 2 hq3)
    calc (1 + (q - q⁻¹) * (q ^ 3 / q3) - (q ^ 3 / q3) ^ 2) * q3 ^ 2
        = q3 ^ 2 + (q - q⁻¹) * (q ^ 3 / q3 * q3) * q3 - (q ^ 3 / q3 * q3) ^ 2 := by ring
      _ = q3 ^ 2 + (q - q⁻¹) * q ^ 3 * q3 - q ^ 6 := by rw [div_mul_cancel₀ _ hq3]; ring
      _ = (q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) := hident1
      _ = (q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) / q3 ^ 2 * q3 ^ 2 := by
            rw [div_mul_cancel₀ _ (pow_ne_zero 2 hq3)]
  · apply mul_right_cancel₀ h4q3sq
    have hc1 : (-(q ^ 3 + q⁻¹ ^ 3) / (2 * q3)) * (2 * q3) = -(q ^ 3 + q⁻¹ ^ 3) :=
      div_mul_cancel₀ _ h2q3
    have hc2 : ((q + q⁻¹) / (2 * q3)) * (2 * q3) = q + q⁻¹ := div_mul_cancel₀ _ h2q3
    have hc3 : ((q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) / (2 * q3)) * (2 * q3) =
        q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3 := div_mul_cancel₀ _ h2q3
    have hc4 : ((q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) / (4 * q3 ^ 2)) * (4 * q3 ^ 2) =
        (q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) := div_mul_cancel₀ _ h4q3sq
    calc ((0 - μ) * (-(q ^ 3 + q⁻¹ ^ 3) / (2 * q3) - μ) -
            (q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) / (4 * q3 ^ 2)) * (4 * q3 ^ 2)
        = (0 - μ * (2 * q3)) * ((-(q ^ 3 + q⁻¹ ^ 3) / (2 * q3)) * (2 * q3) - μ * (2 * q3)) -
            ((q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) / (4 * q3 ^ 2)) * (4 * q3 ^ 2) := by ring
      _ = (0 - μ * (2 * q3)) * (-(q ^ 3 + q⁻¹ ^ 3) - μ * (2 * q3)) -
            (q + q⁻¹) * (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) := by rw [hc1, hc4]
      _ = (μ * (2 * q3) - (q + q⁻¹)) * (μ * (2 * q3) + (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3)) := by ring
      _ = (μ * (2 * q3) - ((q + q⁻¹) / (2 * q3)) * (2 * q3)) *
            (μ * (2 * q3) + ((q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) / (2 * q3)) * (2 * q3)) := by
            rw [hc2, hc3]
      _ = (μ - (q + q⁻¹) / (2 * q3)) * (μ + (q ^ 3 + q + q⁻¹ + q⁻¹ ^ 3) / (2 * q3)) *
            (4 * q3 ^ 2) := by ring

end JimboSixQuarkOverlapAndCasimir

/-! ## §5. Orthogonal Projection / Bloch–Horowitz Schur-Complement Variational Bounds -/

section VariationalAndSchurComplementBounds

/-- Multi-channel Rayleigh–Ritz energy of the Schur-complement trial state
`ψ = (1, -v₀/Δ₀, …, -v_{M-1}/Δ_{M-1})` coupling a factorized ground channel at energy `E₀` to `M`
hidden-colour channels (`M ∈ {4, 41, 461}` for `6q, 9q, 12q`) at gaps `Δ k > 0`. -/
def schurTrialRayleigh {K : Type*} [Field K] {M : ℕ} (E₀ : K) (Δ v : Fin M → K) : K :=
  (E₀ + 2 * (∑ k : Fin M, v k * (-(v k / Δ k))) +
      ∑ k : Fin M, (E₀ + Δ k) * (-(v k / Δ k)) ^ 2) /
    (1 + ∑ k : Fin M, (-(v k / Δ k)) ^ 2)

/-- **Exact multi-channel Rayleigh–Ritz closed form & strict ground-state lowering (§7c).**
Over any `[Field K] [LinearOrder K] [IsStrictOrderedRing K]`, if all hidden-colour gaps satisfy
`0 < Δ k` and at least one inter-nucleon braid coupling `v k₀ ≠ 0`, then:
1. `schurTrialRayleigh E₀ Δ v = E₀ - (∑ k, v k ^ 2 / Δ k) / (1 + ∑ k, (v k / Δ k) ^ 2)`;
2. `schurTrialRayleigh E₀ Δ v < E₀` (hidden-colour reconnection strictly lowers the ground state). -/
theorem multiChannel_schur_rayleigh_lt
    {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] {M : ℕ}
    (E₀ : K) (Δ v : Fin M → K) (hΔ : ∀ k, 0 < Δ k) (hv : ∃ k, v k ≠ 0) :
    schurTrialRayleigh E₀ Δ v =
      E₀ - (∑ k : Fin M, v k ^ 2 / Δ k) / (1 + ∑ k : Fin M, (v k / Δ k) ^ 2) ∧
    schurTrialRayleigh E₀ Δ v < E₀ := by
  have hsum_sq_nonneg : 0 ≤ ∑ k : Fin M, (v k / Δ k) ^ 2 :=
    Finset.sum_nonneg fun k _ => sq_nonneg _
  have hden_pos : 0 < 1 + ∑ k : Fin M, (v k / Δ k) ^ 2 := by linarith
  have hden_ne : 1 + ∑ k : Fin M, (v k / Δ k) ^ 2 ≠ 0 := ne_of_gt hden_pos
  have hterm1 : ∀ k : Fin M, (-(v k / Δ k)) ^ 2 = (v k / Δ k) ^ 2 := fun k => neg_sq _
  have hnum_id : E₀ + 2 * (∑ k : Fin M, v k * (-(v k / Δ k))) +
        (∑ k : Fin M, (E₀ + Δ k) * (v k / Δ k) ^ 2) =
      E₀ * (1 + ∑ k : Fin M, (v k / Δ k) ^ 2) - ∑ k : Fin M, v k ^ 2 / Δ k := by
    have hstep : ∀ k : Fin M,
        2 * (v k * (-(v k / Δ k))) + (E₀ + Δ k) * (v k / Δ k) ^ 2 =
          E₀ * (v k / Δ k) ^ 2 - v k ^ 2 / Δ k := by
      intro k
      have hk_ne : Δ k ≠ 0 := ne_of_gt (hΔ k)
      field_simp
      ring
    calc E₀ + 2 * (∑ k : Fin M, v k * (-(v k / Δ k))) +
            (∑ k : Fin M, (E₀ + Δ k) * (v k / Δ k) ^ 2)
        = E₀ + ((∑ k : Fin M, 2 * (v k * (-(v k / Δ k)))) +
            ∑ k : Fin M, (E₀ + Δ k) * (v k / Δ k) ^ 2) := by
            rw [Finset.mul_sum, add_assoc]
      _ = E₀ + ∑ k : Fin M, (2 * (v k * (-(v k / Δ k))) + (E₀ + Δ k) * (v k / Δ k) ^ 2) := by
            rw [← Finset.sum_add_distrib]
      _ = E₀ + ∑ k : Fin M, (E₀ * (v k / Δ k) ^ 2 - v k ^ 2 / Δ k) := by
            simp_rw [hstep]
      _ = E₀ * (1 + ∑ k : Fin M, (v k / Δ k) ^ 2) - ∑ k : Fin M, v k ^ 2 / Δ k := by
            rw [Finset.sum_sub_distrib, ← Finset.mul_sum]
            ring
  have heq : schurTrialRayleigh E₀ Δ v =
      E₀ - (∑ k : Fin M, v k ^ 2 / Δ k) / (1 + ∑ k : Fin M, (v k / Δ k) ^ 2) := by
    unfold schurTrialRayleigh
    simp_rw [hterm1]
    rw [hnum_id, sub_div, mul_div_cancel_right₀ E₀ hden_ne]
  refine ⟨heq, ?_⟩
  obtain ⟨k₀, hk₀⟩ := hv
  have hk₀_pos : 0 < v k₀ ^ 2 / Δ k₀ := div_pos (sq_pos_of_ne_zero hk₀) (hΔ k₀)
  have hnum_pos : 0 < ∑ k : Fin M, v k ^ 2 / Δ k := by
    refine lt_of_lt_of_le hk₀_pos ?_
    exact Finset.single_le_sum (fun k _ => div_nonneg (sq_nonneg _) (le_of_lt (hΔ k)))
      (Finset.mem_univ k₀)
  have hquot_pos : 0 < (∑ k : Fin M, v k ^ 2 / Δ k) / (1 + ∑ k : Fin M, (v k / Δ k) ^ 2) :=
    div_pos hnum_pos hden_pos
  linarith [heq]

/-- Archimedean `ℝ` specialisation of `multiChannel_schur_rayleigh_lt` (prescribed `§7c` `_real` bridge). -/
theorem multiChannel_schur_rayleigh_lt_real {M : ℕ}
    (E₀ : ℝ) (Δ v : Fin M → ℝ) (hΔ : ∀ k, 0 < Δ k) (hv : ∃ k, v k ≠ 0) :
    schurTrialRayleigh E₀ Δ v =
      E₀ - (∑ k : Fin M, v k ^ 2 / Δ k) / (1 + ∑ k : Fin M, (v k / Δ k) ^ 2) ∧
    schurTrialRayleigh E₀ Δ v < E₀ :=
  multiChannel_schur_rayleigh_lt (K := ℝ) E₀ Δ v hΔ hv

/- The exact 2-channel ground energy `reconnGroundEnergy` (it takes a real square root) and
`colourReconnection_lowers_ground_energy` live behind the transcendental boundary in
`QOU.Transcendental.Nuclear.ColourReconnectionGroundEnergy`, in this namespace. -/

end VariationalAndSchurComplementBounds

end QOU.Nuclear.ColourReconnectionStokesAssembly

