/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Algebra.Ring.Defs
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import QOU.MassTheory.FigureEightGluingFromMonodromy
import QOU.MassTheory.FiveTwoGluingFromFareyWord

/-!
# Adjoint Reidemeister Torsion Determinants, Euler–Jacobi Saddle Sum Rules, and Sister-Manifold Bridges

This module formalizes over generic commutative rings (`[CommRing R]`, **zero `sorry`**, **zero
custom axioms**, **zero `[Field]` / `field_simp`**, **zero transcendental tokens**, **zero
empirical literals**) the exact Dimofte–Garoufalidis / Neumann–Zagier 1-loop adjoint Reidemeister
torsion determinants, deformed $A$-polynomial factorizations, Euler–Jacobi saddle-weight sum rules,
sister-manifold bridges, and two-variable Alexander torus-link identities across $4_1$, $5_2$, the
$(-2,3,7)$ pretzel (`m016`), and the 2-component lepton / electroweak links:

1. **Section 1 — Figure-Eight ($4_1$) Adjoint Torsion Determinant (`hτ` Discharge), $A_\omega(4_1) = 3$,
   and Deformed $A$-Polynomial Factorization:**
   - Constructs the exact $2 \times 2$ Dimofte–Garoufalidis HNF edge + meridian/longitude matrices
     and Neumann flattening `f' = (1, 1)` over any `[CommRing R]` at a sixth root $\omega^2 - \omega + 1 = 0$
     (grounded in the Stallings monodromy $R \cdot L$ of `FigureEightGluingFromMonodromy`).
   - Proves `(twoTauDgMu41 ω)² = -3` (`|τ_{DG,μ}(4₁)| = √3 / 2`, discharging the sole remaining
     `hτ` hypothesis recorded in `MathlibExt/OneLoopPrefactorInvariance.lean`),
     `twoTauDgLam41 ω = -6` (`|τ_{DG,λ}(4₁)| = 3 = s(1) = A_ω(4₁)`), and the squared cusp-shape
     change-of-curve law `(twoTauDgLam41 ω)² = -12 * (twoTauDgMu41 ω)²`.
   - Proves over `[CommRing R]` for any unit `M : Rˣ` on the $4_1$ $A$-polynomial
     `L + L⁻¹ = M⁴ - M² - 2 - M⁻² + M⁻⁴` the exact four-factor identity
     `4 - (L + L⁻¹)² = (M - M⁻¹)² (M + M⁻¹)² (-M² + 3 - M⁻²) (M² + 1 + M⁻²)`,
     factoring deformed cusp torsion into $[2]_M^2$, the abelian Alexander polynomial
     $\Delta_{4_1}(M^2)$, and GGM's non-abelian Stokes meridian polynomial $s(M^2) = M^2 + 1 + M^{-2}$.

2. **Section 2 — $5_2$ Three-Saddle Adjoint Torsion (`2 τ_{DG,μ} = P'(ξ)/ξ`), Norm `23`, and
   Euler–Jacobi Saddle-Weight Cancellation:**
   - Constructs the exact $3 \times 3$ DG HNF edge + meridian/longitude matrices and Neumann
     flattening `f' = (1, 1, 1)` on the `GeneratedGluing.K52` shape triple `(ξ, ξ² - ξ + 2, ξ)`
     for any root of `P(ξ) = ξ³ - 2ξ² + 3ξ - 1 = 0` over `[CommRing R]`.
   - Proves `twoTauDgMu52 ξ = 3ξ² - 3ξ + 5` with `ξ * twoTauDgMu52 ξ = 3ξ² - 4ξ + 3 = P'(ξ)`
     (promoting the numerical closed form of `one_loop_ohtsuki_5_2_crosscheck_probe.py` to an
     unconditional ring theorem), `twoTauDgLam52 ξ = -26ξ² + 38ξ - 50`, and exact cusp shape
     `-4ξ² + 4ξ - 10`.
   - Along the Vieta locus `(e₁, e₂, e₃) = (2, 3, 1)`, proves the 3-saddle torsion norm
     `∏_{j=0}^2 (2 τ_{DG,μ}(5₂; ξ_j)) = 23 = -disc(P)` and the Vandermonde-cleared Euler–Jacobi
     cancellation of the squared Ohtsuki 1-loop saddle weights (`∑ 1/(2 τ_j) = 0`, `∑ ξ_j/(2 τ_j) = 1`).

3. **Section 3 — $(-2,3,7)$ Pretzel (`m016`) Sister-Manifold Torsion Identity (`τ_λ(-2,3,7) = 2 τ_μ(5₂)`)
   and 6-Block State-Integral Saddle Splitting:**
   - Constructs the exact $3 \times 3$ DG matrices on `m016` (`z = (ξ, ξ² - ξ + 2, ξ² - ξ + 2)`,
     flattening `f = (0,1,0), f' = (1,0,1)`) over `[CommRing R]`, proving
     `twoTauDgMuPretzel ξ = 10ξ² - 16ξ + 20`, `twoTauDgLamPretzel ξ = 6ξ² - 6ξ + 10 = 2 * twoTauDgMu52 ξ`
     (**exact sister-manifold torsion bridge**), and `(1 - ξ) * twoTauDgMuPretzel ξ = twoTauDgLamPretzel ξ`
     (cusp shape `1 - ξ`, whose modulus at the hyperbolic root is the plastic constant $\rho$).
   - Proves that the 1D state-integral saddle polynomial of `PretzelLevelTwoBlockFactorization`
     factors as `(1 - Z)²(1 - Z²)² - Z² = (Z³ - Z² + 1)(Z³ - Z² - 2Z + 1)` with cubic discriminants
     `-23` (3 hyperbolic sister saddles) and `+49 = 7²` (3 abelian $\mathbb{Z}/7$ saddles), giving `3 + 3 = 6`.

4. **Section 4 — Division-Free Two-Variable Alexander Lepton-Link Ordering Inversion & Torus-Link
   Quantum Integers:**
   - Proves over strict ordered commutative rings that at `1 < q` and `q - q⁻¹ < 1` (`q₀ ≈ 1.11`),
     the two-variable Alexander polynomials of `(e, μ, τ)` satisfy `0 < Δ_τ(q,q) < Δ_e(q,q) < Δ_μ(q,q)`
     and `Δ_τ(q,q⁻¹) < 0 < Δ_e(q,q⁻¹) < Δ_μ(q,q⁻¹)` (inverting physical mass order $e < \mu < \tau$),
     while diagonal symmetrized Alexander polynomials of `T(2, 2k)` reproduce `[k]_q` (`k = 1..4`).

-- Ref: [dimofte-garoufalidis2013] Dimofte & Garoufalidis, Adv. Theor. Math. Phys. 17 (2013), arXiv:1202.6268
-- Ref: [ohtsuki2016] Ohtsuki, Quantum Topol. 7 (2016) 669-735
-- Ref: [garoufalidis-gu-marino2023peacock] Garoufalidis, Gu & Marino, Commun. Math. Phys. 386 (2021), arXiv:2012.00062
-/

set_option autoImplicit false

namespace QOU.BraidsAndKnots
namespace AdjointTorsionSaddlePrefactors

open QOU.Mass.FigureEightGluingFromMonodromy (R L stallings_monodromy_eq stallings_trace_three)

private lemma det_fin_two_of {A : Type*} [CommRing A] (a b c d : A) :
    (!![a, b; c, d] : Matrix (Fin 2) (Fin 2) A).det = a * d - b * c := by
  rw [Matrix.det_fin_two]
  simp

private lemma det_fin_three_of {A : Type*} [CommRing A]
    (a00 a01 a02 a10 a11 a12 a20 a21 a22 : A) :
    (!![a00, a01, a02; a10, a11, a12; a20, a21, a22] : Matrix (Fin 3) (Fin 3) A).det =
      a00 * (a11 * a22 - a12 * a21) -
      a01 * (a10 * a22 - a12 * a20) +
      a02 * (a10 * a21 - a11 * a20) := by
  rw [Matrix.det_fin_three]
  simp
  ring

/-! ## Section 1: Figure-Eight ($4_1$) Adjoint Torsion, `hτ` Discharge, and Deformed $A$-Polynomial -/

section FigureEightAdjointTorsion

/-- Specialised $2 \times 2$ Dimofte–Garoufalidis meridian matrix `(B ; P_μ)` of $4_1$ at shape
`z₀ = z₁ = ω` (`ζ = 1 - ω`, `ζ' = ω` modulo `ω² - ω + 1 = 0`), with HNF edge row `(2, 2 | 1, 1)`
and meridian row `(1, 1 | 0, 1)`. -/
def dgMuMat41 {A : Type*} [CommRing A] (ω : A) : Matrix (Fin 2) (Fin 2) A :=
  !![2 * (1 - ω) + ω, 2 * (1 - ω) + ω; 1 - ω, (1 - ω) + ω]

/-- Specialised $2 \times 2$ Dimofte–Garoufalidis longitude matrix `(B ; P_λ)` of $4_1$ with
longitude row `(0, 4 | 0, 2)`. -/
def dgLamMat41 {A : Type*} [CommRing A] (ω : A) : Matrix (Fin 2) (Fin 2) A :=
  !![2 * (1 - ω) + ω, 2 * (1 - ω) + ω; 0, 4 * (1 - ω) + 2 * ω]

/-- Doubled meridian DG 1-loop / adjoint torsion `2 τ_{DG,μ}(4₁)` over any `[CommRing A]`,
multiplying `det(dgMuMat41 ω)` by the inverse `-ω` of the Neumann flattening monomial
`ζ'₀ ζ'₁ = ω²` (`f = (0,0), f' = (1,1), f'' = (0,0)`). -/
def twoTauDgMu41 {A : Type*} [CommRing A] (ω : A) : A :=
  (dgMuMat41 ω).det * (-ω)

/-- Doubled longitude DG 1-loop / adjoint torsion `2 τ_{DG,λ}(4₁)` over any `[CommRing A]`. -/
def twoTauDgLam41 {A : Type*} [CommRing A] (ω : A) : A :=
  (dgLamMat41 ω).det * (-ω)

/-- **Exact unit & flattening identities for $4_1$ (`ω² - ω + 1 = 0`) over `[CommRing A]`:**
`ω(1 - ω) = 1`, `ω² · (-ω) = 1`, and `(1 - ω)² = -ω`. -/
theorem fourOne_shape_and_flattening_units {A : Type*} [CommRing A] {ω : A}
    (hω : ω ^ 2 - ω + 1 = 0) :
    ω * (1 - ω) = 1 ∧ ω ^ 2 * (-ω) = 1 ∧ (1 - ω) ^ 2 = -ω := by
  refine ⟨?_, ?_, ?_⟩
  · linear_combination -hω
  · linear_combination -(ω + 1) * hω
  · linear_combination hω

/-- **Unconditional $4_1$ DG 1-loop / Adjoint Torsion Theorem (`hτ` discharge & `A_ω = 3`):**
For every root `ω` of `ω² - ω + 1 = 0` in any commutative ring `A`:
1. `twoTauDgMu41 ω = 1 - 2ω` and `(twoTauDgMu41 ω)² = -3` (`|τ_{DG,μ}(4₁)|² = 3/4`, discharging
   the `hτ` assumption recorded in `MathlibExt/OneLoopPrefactorInvariance.lean`);
2. `twoTauDgLam41 ω = -6` (`|τ_{DG,λ}(4₁)| = 3 = tr(R · L) = s(1) = A_ω(4₁)`, identifying the
   longitude adjoint torsion of $4_1$ with the Stallings trace and Stokes symmetry constant `3`);
3. `(twoTauDgLam41 ω)² = -12 * (twoTauDgMu41 ω)²` (squared cusp-shape ratio `|τ_λ / τ_μ|² = 12`). -/
theorem fourOne_dg_torsion_mu_lam_and_cusp_shape {A : Type*} [CommRing A] {ω : A}
    (hω : ω ^ 2 - ω + 1 = 0) :
    twoTauDgMu41 ω = 1 - 2 * ω ∧
    (twoTauDgMu41 ω) ^ 2 = -3 ∧
    twoTauDgLam41 ω = -6 ∧
    (R * L).trace = 3 ∧
    (twoTauDgLam41 ω) ^ 2 = -12 * (twoTauDgMu41 ω) ^ 2 := by
  have hmu : twoTauDgMu41 ω = 1 - 2 * ω := by
    unfold twoTauDgMu41 dgMuMat41
    rw [det_fin_two_of]
    linear_combination (ω - 1) * hω
  have hmu_sq : (twoTauDgMu41 ω) ^ 2 = -3 := by
    rw [hmu]
    linear_combination 4 * hω
  have hlam : twoTauDgLam41 ω = -6 := by
    unfold twoTauDgLam41 dgLamMat41
    rw [det_fin_two_of]
    linear_combination (-2 * ω + 6) * hω
  refine ⟨hmu, hmu_sq, hlam, stallings_trace_three, ?_⟩
  rw [hlam, hmu_sq]
  norm_num

/-- **Deformed $4_1$ $A$-Polynomial Cusp-Torsion Factorization over `[CommRing A]` (`0` division):**
Along the $4_1$ $A$-polynomial `L + L⁻¹ = M⁴ - M² - 2 - M⁻² + M⁻⁴` for any unit `M : Aˣ`,
`4 - (L + L⁻¹)²` factors into `(M - M⁻¹)² · [2]_M² · Δ_{4₁}(M²) · s(M²)`, uniting the abelian
Alexander polynomial `Δ_{4₁}(x) = -x + 3 - x⁻¹` and GGM's non-abelian Stokes meridian weight
`s(x) = x + 1 + x⁻¹` inside one ring identity, with specialization `4 · 1 · 3 = 12` at `M = 1`. -/
theorem fourOne_deformed_apoly_disc_factors {A : Type*} [CommRing A] (M : Aˣ) :
    let m : A := M
    let mi : A := ↑M⁻¹
    let lSum : A := m ^ 4 - m ^ 2 - 2 - mi ^ 2 + mi ^ 4
    let delta41 : A := -m ^ 2 + 3 - mi ^ 2
    let stokesS : A := m ^ 2 + 1 + mi ^ 2
    4 - lSum ^ 2 = (m - mi) ^ 2 * (m + mi) ^ 2 * delta41 * stokesS ∧
    ((1 : A) + 1) ^ 2 * (-1 + 3 - 1) * (1 + 1 + 1) = 12 := by
  intro m mi lSum delta41 stokesS
  have hmi : m * mi = 1 := M.val_inv
  refine ⟨?_, by norm_num⟩
  dsimp only [lSum, delta41, stokesS]
  linear_combination
    (-4 * m ^ 3 * mi ^ 3 + 4 * m ^ 3 * mi - 4 * m ^ 2 * mi ^ 2 +
      4 * m ^ 2 + 4 * m * mi ^ 3 + 4 * mi ^ 2) * hmi

end FigureEightAdjointTorsion

/-! ## Section 2: $5_2$ Three-Saddle Adjoint Torsion, Norm `23`, and Euler–Jacobi Cancellation -/

section FiveTwoThreeSaddleTorsion

/-- Exact $3 \times 3$ Dimofte–Garoufalidis meridian matrix `(B ; P_μ)` for $5_2$ (`GeneratedGluing.K52`,
shapes `z = (ξ, ξ² - ξ + 2, ξ)` with integral inverses `ζ = (ξ² - 2ξ + 3, 1 - ξ, ξ² - 2ξ + 3)` and
`ζ' = (ξ² - ξ + 2, -ξ² + 2ξ - 2, ξ² - ξ + 2)` modulo `ξ³ - 2ξ² + 3ξ - 1 = 0`), using HNF edge rows
`(1,2,1 | 0,2,0)`, `(0,1,0 | -1,2,-1)` and meridian row `(-1,-1,0 | 0,-1,0)`. -/
def dgMuMat52 {A : Type*} [CommRing A] (ξ : A) : Matrix (Fin 3) (Fin 3) A :=
  let zt0 := ξ ^ 2 - 2 * ξ + 3
  let zt1 := 1 - ξ
  let ztp0 := ξ ^ 2 - ξ + 2
  let ztp1 := -ξ ^ 2 + 2 * ξ - 2
  !![1 * zt0 + 0 * ztp0, 2 * zt1 + 2 * ztp1, 1 * zt0 + 0 * ztp0;
     0 * zt0 - 1 * ztp0, 1 * zt1 + 2 * ztp1, 0 * zt0 - 1 * ztp0;
     -1 * zt0 + 0 * ztp0, -1 * zt1 - 1 * ztp1, 0]

/-- Exact $3 \times 3$ Dimofte–Garoufalidis longitude matrix `(B ; P_λ)` for $5_2$, with longitude
row `(5, 3, -1 | 3, 2, -1)`. -/
def dgLamMat52 {A : Type*} [CommRing A] (ξ : A) : Matrix (Fin 3) (Fin 3) A :=
  let zt0 := ξ ^ 2 - 2 * ξ + 3
  let zt1 := 1 - ξ
  let ztp0 := ξ ^ 2 - ξ + 2
  let ztp1 := -ξ ^ 2 + 2 * ξ - 2
  !![1 * zt0 + 0 * ztp0, 2 * zt1 + 2 * ztp1, 1 * zt0 + 0 * ztp0;
     0 * zt0 - 1 * ztp0, 1 * zt1 + 2 * ztp1, 0 * zt0 - 1 * ztp0;
     5 * zt0 + 3 * ztp0, 3 * zt1 + 2 * ztp1, -1 * zt0 - 1 * ztp0]

/-- Doubled meridian DG 1-loop / adjoint torsion `2 τ_{DG,μ}(5₂; ξ)` over `[CommRing A]`,
multiplying `det(dgMuMat52 ξ)` by the inverse `ξ² - ξ` of the Neumann flattening monomial
`ζ'₀ ζ'₁ ζ'₂` (`f = (0,0,0), f' = (1,1,1), f'' = (0,0,0)`). -/
def twoTauDgMu52 {A : Type*} [CommRing A] (ξ : A) : A :=
  (dgMuMat52 ξ).det * (ξ ^ 2 - ξ)

/-- Doubled longitude DG 1-loop / adjoint torsion `2 τ_{DG,λ}(5₂; ξ)` over `[CommRing A]`. -/
def twoTauDgLam52 {A : Type*} [CommRing A] (ξ : A) : A :=
  (dgLamMat52 ξ).det * (ξ ^ 2 - ξ)

/-- **Exact shape-unit & flattening-monomial certificates for $5_2$ (`ξ³ - 2ξ² + 3ξ - 1 = 0`):**
Every `z_j`, `1 - z_j`, and the Neumann flattening monomial `ζ'₀ ζ'₁ ζ'₂` is an explicit unit in `A`. -/
theorem fiveTwo_shape_and_flattening_units {A : Type*} [CommRing A] {ξ : A}
    (hξ : ξ ^ 3 - 2 * ξ ^ 2 + 3 * ξ - 1 = 0) :
    ξ * (ξ ^ 2 - 2 * ξ + 3) = 1 ∧
    (1 - ξ) * (ξ ^ 2 - ξ + 2) = 1 ∧
    (1 - (ξ ^ 2 - ξ + 2)) * (-ξ ^ 2 + 2 * ξ - 2) = 1 ∧
    ((ξ ^ 2 - ξ + 2) * (-ξ ^ 2 + 2 * ξ - 2) * (ξ ^ 2 - ξ + 2)) * (ξ ^ 2 - ξ) = 1 := by
  refine ⟨?_, ?_, ?_, ?_⟩
  · linear_combination hξ
  · linear_combination -hξ
  · linear_combination (ξ - 1) * hξ
  · linear_combination (-ξ ^ 5 + 3 * ξ ^ 4 - 6 * ξ ^ 3 + 7 * ξ ^ 2 - 5 * ξ + 1) * hξ

/-- **Unconditional $5_2$ DG Adjoint Torsion Closed-Form & Cusp-Shape Theorem:**
For every root `ξ` of `P(ξ) = ξ³ - 2ξ² + 3ξ - 1 = 0` in any `[CommRing A]`:
1. `twoTauDgMu52 ξ = 3ξ² - 3ξ + 5`;
2. `ξ * twoTauDgMu52 ξ = 3ξ² - 4ξ + 3 = P'(ξ)` (establishing `2 τ_{DG,μ}(5₂; ξ) = P'(ξ)/ξ = f'(1/ξ)`
   algebraically at all three saddles);
3. `twoTauDgLam52 ξ = -26ξ² + 38ξ - 50` and `twoTauDgMu52 ξ * (-4ξ² + 4ξ - 10) = twoTauDgLam52 ξ`. -/
theorem fiveTwo_dg_torsion_eq_saddle_deriv {A : Type*} [CommRing A] {ξ : A}
    (hξ : ξ ^ 3 - 2 * ξ ^ 2 + 3 * ξ - 1 = 0) :
    twoTauDgMu52 ξ = 3 * ξ ^ 2 - 3 * ξ + 5 ∧
    ξ * twoTauDgMu52 ξ = 3 * ξ ^ 2 - 4 * ξ + 3 ∧
    twoTauDgLam52 ξ = -26 * ξ ^ 2 + 38 * ξ - 50 ∧
    twoTauDgMu52 ξ * (-4 * ξ ^ 2 + 4 * ξ - 10) = twoTauDgLam52 ξ := by
  have hmu : twoTauDgMu52 ξ = 3 * ξ ^ 2 - 3 * ξ + 5 := by
    unfold twoTauDgMu52 dgMuMat52
    rw [det_fin_three_of]
    linear_combination
      (-4 * ξ ^ 5 + 15 * ξ ^ 4 - 34 * ξ ^ 3 + 40 * ξ ^ 2 - 27 * ξ + 5) * hξ
  have hderiv : ξ * twoTauDgMu52 ξ = 3 * ξ ^ 2 - 4 * ξ + 3 := by
    rw [hmu]
    linear_combination 3 * hξ
  have hlam : twoTauDgLam52 ξ = -26 * ξ ^ 2 + 38 * ξ - 50 := by
    unfold twoTauDgLam52 dgLamMat52
    rw [det_fin_three_of]
    linear_combination
      (40 * ξ ^ 5 - 134 * ξ ^ 4 + 296 * ξ ^ 3 - 340 * ξ ^ 2 + 226 * ξ - 50) * hξ
  refine ⟨hmu, hderiv, hlam, ?_⟩
  rw [hmu, hlam]
  linear_combination (-12 * ξ) * hξ

/-- **Three-Saddle Torsion Norm `23` and Vandermonde-Cleared Euler–Jacobi Saddle-Weight Sum Rules:**
Over any `[CommRing A]`, for any triple `(ξ₀, ξ₁, ξ₂)` satisfying the $5_2$ Vieta relations
`ξ₀ + ξ₁ + ξ₂ = 2`, `ξ₀ξ₁ + ξ₀ξ₂ + ξ₁ξ₂ = 3`, `ξ₀ξ₁ξ₂ = 1`, with Vandermonde product
`V = (ξ₀ - ξ₁)(ξ₀ - ξ₂)(ξ₁ - ξ₂)`:
1. **3-Saddle Norm = `23 = |disc(K_{5₂})|`:**
   `(3ξ₀² - 3ξ₀ + 5)(3ξ₁² - 3ξ₁ + 5)(3ξ₂² - 3ξ₂ + 5) = 23` (so `∏_{j=0}^2 τ_{DG,μ}(5₂; ξ_j) = 23/8`);
2. **Derivative Factorization:** `3ξ₀² - 4ξ₀ + 3 = (ξ₀ - ξ₁)(ξ₀ - ξ₂)`;
3. **Cleared Euler–Jacobi `k = 0` (`∑ 1 / P'(ξ_j) = 0`):** `(ξ₁ - ξ₂) + (ξ₂ - ξ₀) + (ξ₀ - ξ₁) = 0`;
4. **Cleared Euler–Jacobi `k = 1` (`∑ 1 / (2 τ_{DG,μ}(5₂; ξ_j)) = ∑ ξ_j / P'(ξ_j) = 0`):**
   `ξ₀(ξ₁ - ξ₂) + ξ₁(ξ₂ - ξ₀) + ξ₂(ξ₀ - ξ₁) = 0` (exact cancellation of the three squared
   Ohtsuki 1-loop saddle weights `ω_j²`);
5. **Cleared Euler–Jacobi `k = 2` (`∑ ξ_j / (2 τ_{DG,μ}(5₂; ξ_j)) = 1`):**
   `ξ₀²(ξ₁ - ξ₂) + ξ₁²(ξ₂ - ξ₀) + ξ₂²(ξ₀ - ξ₁) = V`. -/
theorem fiveTwo_three_saddle_norm_and_euler_jacobi {A : Type*} [CommRing A]
    {ξ₀ ξ₁ ξ₂ : A}
    (e1 : ξ₀ + ξ₁ + ξ₂ = 2)
    (e2 : ξ₀ * ξ₁ + ξ₀ * ξ₂ + ξ₁ * ξ₂ = 3)
    (e3 : ξ₀ * ξ₁ * ξ₂ = 1) :
    (3 * ξ₀ ^ 2 - 3 * ξ₀ + 5) * (3 * ξ₁ ^ 2 - 3 * ξ₁ + 5) * (3 * ξ₂ ^ 2 - 3 * ξ₂ + 5) = 23 ∧
    3 * ξ₀ ^ 2 - 4 * ξ₀ + 3 = (ξ₀ - ξ₁) * (ξ₀ - ξ₂) ∧
    (ξ₁ - ξ₂) + (ξ₂ - ξ₀) + (ξ₀ - ξ₁) = 0 ∧
    ξ₀ * (ξ₁ - ξ₂) + ξ₁ * (ξ₂ - ξ₀) + ξ₂ * (ξ₀ - ξ₁) = 0 ∧
    ξ₀ ^ 2 * (ξ₁ - ξ₂) + ξ₁ ^ 2 * (ξ₂ - ξ₀) + ξ₂ ^ 2 * (ξ₀ - ξ₁) =
      (ξ₀ - ξ₁) * (ξ₀ - ξ₂) * (ξ₁ - ξ₂) := by
  have hsym :
      (3 * ξ₀ ^ 2 - 3 * ξ₀ + 5) * (3 * ξ₁ ^ 2 - 3 * ξ₁ + 5) * (3 * ξ₂ ^ 2 - 3 * ξ₂ + 5) =
        75 * (ξ₀ + ξ₁ + ξ₂) ^ 2
        - 45 * (ξ₀ + ξ₁ + ξ₂) * (ξ₀ * ξ₁ + ξ₀ * ξ₂ + ξ₁ * ξ₂)
        - 63 * (ξ₀ + ξ₁ + ξ₂) * (ξ₀ * ξ₁ * ξ₂)
        - 75 * (ξ₀ + ξ₁ + ξ₂)
        + 45 * (ξ₀ * ξ₁ + ξ₀ * ξ₂ + ξ₁ * ξ₂) ^ 2
        - 27 * (ξ₀ * ξ₁ + ξ₀ * ξ₂ + ξ₁ * ξ₂) * (ξ₀ * ξ₁ * ξ₂)
        - 105 * (ξ₀ * ξ₁ + ξ₀ * ξ₂ + ξ₁ * ξ₂)
        + 27 * (ξ₀ * ξ₁ * ξ₂) ^ 2
        + 108 * (ξ₀ * ξ₁ * ξ₂) + 125 := by ring
  refine ⟨?_, ?_, by ring, by ring, by ring⟩
  · rw [hsym, e1, e2, e3]; norm_num
  · linear_combination 2 * ξ₀ * e1 - e2

end FiveTwoThreeSaddleTorsion

/-! ## Section 3: $(-2,3,7)$ Pretzel (`m016`) Sister-Manifold Bridge & 6-Block Saddle Split -/

section PretzelSisterTorsionAndBlocks

/-- Exact $3 \times 3$ Dimofte–Garoufalidis meridian matrix `(B ; P_μ)` for the $(-2,3,7)$ pretzel
(`m016`, shapes `z = (ξ, ξ² - ξ + 2, ξ² - ξ + 2)`), using HNF edge rows `(1,0,1 | 1,-1,0)`,
`(0,1,-1 | 1,0,-2)` and meridian row `(-2,0,-1 | -2,0,0)`. -/
def dgMuMatPretzel {A : Type*} [CommRing A] (ξ : A) : Matrix (Fin 3) (Fin 3) A :=
  let zt0 := ξ ^ 2 - 2 * ξ + 3
  let zt1 := 1 - ξ
  let ztp0 := ξ ^ 2 - ξ + 2
  let ztp1 := -ξ ^ 2 + 2 * ξ - 2
  !![1 * zt0 + 1 * ztp0, 0 * zt1 - 1 * ztp1, 1 * zt1 + 0 * ztp1;
     0 * zt0 + 1 * ztp0, 1 * zt1 + 0 * ztp1, -1 * zt1 - 2 * ztp1;
     -2 * zt0 - 2 * ztp0, 0, -1 * zt1 + 0 * ztp1]

/-- Exact $3 \times 3$ Dimofte–Garoufalidis longitude matrix `(B ; P_λ)` for `m016`, with longitude
row `(0, 0, 0 | 2, -2, -2)`. -/
def dgLamMatPretzel {A : Type*} [CommRing A] (ξ : A) : Matrix (Fin 3) (Fin 3) A :=
  let zt0 := ξ ^ 2 - 2 * ξ + 3
  let zt1 := 1 - ξ
  let ztp0 := ξ ^ 2 - ξ + 2
  let ztp1 := -ξ ^ 2 + 2 * ξ - 2
  !![1 * zt0 + 1 * ztp0, 0 * zt1 - 1 * ztp1, 1 * zt1 + 0 * ztp1;
     0 * zt0 + 1 * ztp0, 1 * zt1 + 0 * ztp1, -1 * zt1 - 2 * ztp1;
     2 * ztp0, -2 * ztp1, -2 * ztp1]

/-- Doubled meridian DG 1-loop / adjoint torsion `2 τ_{DG,μ}(-2,3,7)` over `[CommRing A]`,
multiplying `det(dgMuMatPretzel ξ)` by the inverse `-ξ² + ξ - 1` of the Neumann flattening monomial
`ζ'₀ ζ₁ ζ'₂` (`f = (0,1,0), f' = (1,0,1), f'' = (0,0,0)`). -/
def twoTauDgMuPretzel {A : Type*} [CommRing A] (ξ : A) : A :=
  (dgMuMatPretzel ξ).det * (-ξ ^ 2 + ξ - 1)

/-- Doubled longitude DG 1-loop / adjoint torsion `2 τ_{DG,λ}(-2,3,7)` over `[CommRing A]`. -/
def twoTauDgLamPretzel {A : Type*} [CommRing A] (ξ : A) : A :=
  (dgLamMatPretzel ξ).det * (-ξ ^ 2 + ξ - 1)

/-- **Sister-Manifold Adjoint Torsion Theorem (`5_2` ↔ `(-2,3,7)` Pretzel `m016`):**
For every root `ξ` of `ξ³ - 2ξ² + 3ξ - 1 = 0` in any `[CommRing A]`:
1. The Neumann flattening monomial `ζ'₀ ζ₁ ζ'₂` has exact inverse `-ξ² + ξ - 1`;
2. `twoTauDgMuPretzel ξ = 10ξ² - 16ξ + 20` and `twoTauDgLamPretzel ξ = 6ξ² - 6ξ + 10`;
3. **Exact Sister Identity:** `twoTauDgLamPretzel ξ = 2 * twoTauDgMu52 ξ`
   (`τ_{DG,λ}(-2,3,7) = 2 · τ_{DG,μ}(5₂)` identically over `A`!);
4. **Plastic-Constant Cusp Shape:** `(1 - ξ) * twoTauDgMuPretzel ξ = twoTauDgLamPretzel ξ`, where
   `t = 1 - ξ` satisfies `t³ - t² + 2t - 1 = 0` (`|1 - ξ₀| = ρ = 1.3247179572…` at the geometric saddle). -/
theorem pretzel_sister_torsion_bridge {A : Type*} [CommRing A] {ξ : A}
    (hξ : ξ ^ 3 - 2 * ξ ^ 2 + 3 * ξ - 1 = 0) :
    ((ξ ^ 2 - ξ + 2) * (1 - ξ) * (-ξ ^ 2 + 2 * ξ - 2)) * (-ξ ^ 2 + ξ - 1) = 1 ∧
    twoTauDgMuPretzel ξ = 10 * ξ ^ 2 - 16 * ξ + 20 ∧
    twoTauDgLamPretzel ξ = 6 * ξ ^ 2 - 6 * ξ + 10 ∧
    twoTauDgLamPretzel ξ = 2 * twoTauDgMu52 ξ ∧
    (1 - ξ) * twoTauDgMuPretzel ξ = twoTauDgLamPretzel ξ ∧
    (1 - ξ) ^ 3 - (1 - ξ) ^ 2 + 2 * (1 - ξ) - 1 = 0 := by
  have hflat :
      ((ξ ^ 2 - ξ + 2) * (1 - ξ) * (-ξ ^ 2 + 2 * ξ - 2)) * (-ξ ^ 2 + ξ - 1) = 1 := by
    linear_combination (-ξ ^ 4 + 3 * ξ ^ 3 - 5 * ξ ^ 2 + 5 * ξ - 3) * hξ
  have hmu : twoTauDgMuPretzel ξ = 10 * ξ ^ 2 - 16 * ξ + 20 := by
    unfold twoTauDgMuPretzel dgMuMatPretzel
    rw [det_fin_three_of]
    linear_combination
      (8 * ξ ^ 5 - 31 * ξ ^ 4 + 69 * ξ ^ 3 - 88 * ξ ^ 2 + 75 * ξ - 31) * hξ
  have hlam : twoTauDgLamPretzel ξ = 6 * ξ ^ 2 - 6 * ξ + 10 := by
    unfold twoTauDgLamPretzel dgLamMatPretzel
    rw [det_fin_three_of]
    linear_combination
      (6 * ξ ^ 5 - 20 * ξ ^ 4 + 44 * ξ ^ 3 - 52 * ξ ^ 2 + 42 * ξ - 18) * hξ
  have hmu52 : twoTauDgMu52 ξ = 3 * ξ ^ 2 - 3 * ξ + 5 :=
    (fiveTwo_dg_torsion_eq_saddle_deriv hξ).1
  refine ⟨hflat, hmu, hlam, ?_, ?_, ?_⟩
  · rw [hlam, hmu52]; ring
  · rw [hmu, hlam]; linear_combination -10 * hξ
  · linear_combination -hξ

/-- **Stepwise 1D State-Integral Saddle Splitting for the $(-2,3,7)$ Pretzel (`3 + 3 = 6` blocks):**
Over any `[CommRing A]`, the $q \to 1$ classical limit `(1 - Z)²(1 - Z²)² - Z²` of the degree-6
descendant operator (`PretzelLevelTwoBlockFactorization`, charge vector `(1, 1, 2)`, Gaussian `A = 2`)
splits into `(Z³ - Z² + 1)` (`disc = -23`, the 3 hyperbolic sister saddles) times
`(Z³ - Z² - 2Z + 1)` (`disc = +49 = 7²`, the 3 totally real $\mathbb{Z}/7$ dihedral saddles). -/
theorem pretzel_state_integral_saddle_splits {A : Type*} [CommRing A] (Z : A) :
    (1 - Z) ^ 2 * (1 - Z ^ 2) ^ 2 - Z ^ 2 =
      (Z ^ 3 - Z ^ 2 + 1) * (Z ^ 3 - Z ^ 2 - 2 * Z + 1) ∧
    (18 * (1 : ℤ) * (-1) * 0 * 1 - 4 * (-1) ^ 3 * 1 + (-1) ^ 2 * 0 ^ 2 - 4 * 1 * 0 ^ 3 - 27 * 1 ^ 2 * 1 ^ 2) = -23 ∧
    (18 * (1 : ℤ) * (-1) * (-2) * 1 - 4 * (-1) ^ 3 * 1 + (-1) ^ 2 * (-2) ^ 2 - 4 * 1 * (-2) ^ 3 - 27 * 1 ^ 2 * 1 ^ 2) = 49 := by
  refine ⟨by ring, by norm_num, by norm_num⟩

end PretzelSisterTorsionAndBlocks

/-! ## Section 4: Lepton-Link Two-Variable Alexander Ordering Inversion & Torus-Link `[k]_q` -/

section LeptonAndTorusLinkAlexander

/-- Division-free two-variable Alexander polynomial of the electron Hopf link `Δ_e(t₁, t₂) = 1`. -/
def alexE {A : Type*} [CommRing A] (_ _ : A) : A := 1

/-- Division-free two-variable Alexander polynomial of the muon `T(2,4)` link `Δ_μ(t₁, t₂) = 1 + t₁ t₂`. -/
def alexMu {A : Type*} [CommRing A] (t₁ t₂ : A) : A := 1 + t₁ * t₂

/-- Division-free two-variable Alexander polynomial of the tau Whitehead link `Δ_τ(t₁, t₂) = (t₁ - 1)(t₂ - 1)`. -/
def alexTau {A : Type*} [CommRing A] (t₁ t₂ : A) : A := (t₁ - 1) * (t₂ - 1)

/-- **Lepton-Link Two-Variable Alexander Ordering Inversion (`|Δ_τ| < |Δ_e| < |Δ_μ|` at `q₀`):**
Over any strict ordered commutative ring `K` and unit `q : Kˣ` with `1 < q` and `(q : K) - 1 < 1`
(satisfied at `q₀ ≈ 1.10998`, where `q₀ - 1 ≈ 0.11 < 1`):
1. On the parallel locus `(q, q)`: `0 < alexTau q q < alexE q q < alexMu q q`;
2. On the antiparallel/bar locus `(q, q⁻¹)`: `alexTau q q⁻¹ = -((q : K) + ↑q⁻¹ - 2) < 0`,
   `alexE q q⁻¹ = 1`, `alexMu q q⁻¹ = 2`, and `|alexTau q q⁻¹| < alexE q q⁻¹ < alexMu q q⁻¹`.
Hence abelian two-variable Alexander / Milnor torsion strictly inverts $\tau$ below $e$ and $\mu$. -/
theorem lepton_two_var_alexander_inverts_tau_order
    {K : Type*} [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    (q : Kˣ) (hq1 : (1 : K) < (q : K)) (hq2 : (q : K) - 1 < 1) :
    let qv : K := q
    let qi : K := ↑q⁻¹
    (0 < alexTau qv qv ∧ alexTau qv qv < alexE qv qv ∧ alexE qv qv < alexMu qv qv) ∧
    (alexTau qv qi = -(qv + qi - 2) ∧ alexE qv qi = 1 ∧ alexMu qv qi = 2 ∧
      alexTau qv qi < 0 ∧ -alexTau qv qi < alexE qv qi) := by
  intro qv qi
  have hmul : qv * qi = 1 := q.val_inv
  have hsub_pos : 0 < qv - 1 := sub_pos.mpr hq1
  have hqv_pos : 0 < qv := by linarith
  have hqi_pos : 0 < qi := by
    by_contra hle
    push_neg at hle
    have hprod_nonpos : qv * qi ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hqv_pos.le hle
    linarith
  have htau_par_pos : 0 < (qv - 1) * (qv - 1) := mul_pos hsub_pos hsub_pos
  have htau_par_lt1 : (qv - 1) * (qv - 1) < 1 := by
    have hlt : (qv - 1) * (qv - 1) < 1 * (qv - 1) := mul_lt_mul_of_pos_right hq2 hsub_pos
    linarith
  have hq_sq_gt1 : 1 < qv * qv := by
    have h1 : 1 * qv < qv * qv := mul_lt_mul_of_pos_right hq1 hqv_pos
    linarith
  have htau_bar_id : (qv - 1) * (qi - 1) = -(qv + qi - 2) := by
    linear_combination hmul
  have hqi_lt1 : qi < 1 := by
    have h1 : 1 * qi < qv * qi := mul_lt_mul_of_pos_right hq1 hqi_pos
    linarith
  have htau_bar_neg : (qv - 1) * (qi - 1) < 0 :=
    mul_neg_of_pos_of_neg hsub_pos (sub_neg.mpr hqi_lt1)
  have hneg_tau_lt : -((qv - 1) * (qi - 1)) < 1 := by
    have hpos1 : 0 < 1 - qi := sub_pos.mpr hqi_lt1
    have h1 : 1 - qi < 1 := by linarith
    have h2 : (qv - 1) * (1 - qi) < 1 * (1 - qi) := mul_lt_mul_of_pos_right hq2 hpos1
    linarith
  refine ⟨⟨htau_par_pos, ?_, ?_⟩, ⟨htau_bar_id, rfl, ?_, htau_bar_neg, ?_⟩⟩
  · unfold alexTau alexE; exact htau_par_lt1
  · unfold alexE alexMu; linarith
  · unfold alexMu; linear_combination hmul
  · unfold alexTau alexE; exact hneg_tau_lt

/-- Diagonal symmetrized two-variable Conway–Alexander potential of the 2-component torus link
`T(2, 2k)` (`k = 1, 2, 3, 4`) at `t₁ = t₂ = q²` (or `√(t₁ t₂) = q`), defined division-free over
any `[CommRing A]` with unit `q : Aˣ`. -/
def symTorusLinkAlex {A : Type*} [CommRing A] (q : Aˣ) : Fin 4 → A
  | 0 => 1
  | 1 => (q : A) + (↑q⁻¹ : A)
  | 2 => (q : A) ^ 2 + 1 + (↑q⁻¹ : A) ^ 2
  | 3 => (q : A) ^ 3 + (q : A) + (↑q⁻¹ : A) + (↑q⁻¹ : A) ^ 3

/-- **Torus-Link Symmetrized Alexander = Quantum Integer `[k]_q` (`k = 1, 2, 3, 4`):**
Over every `[CommRing A]` and unit `q : Aˣ`, `(q - q⁻¹) · symTorusLinkAlex q (k - 1) = q^k - q⁻ᵏ`,
identifying the electroweak carrier quantum integers `[2]_q, [3]_q, [4]_q` with the diagonal
symmetrized Alexander/Reidemeister torsions of `{T(2,4), T(2,6), T(2,8)}`. -/
theorem symTorusLinkAlex_telescopes_to_qInt {A : Type*} [CommRing A] (q : Aˣ) :
    let qv : A := q
    let qi : A := ↑q⁻¹
    (qv - qi) * symTorusLinkAlex q 0 = qv ^ 1 - qi ^ 1 ∧
    (qv - qi) * symTorusLinkAlex q 1 = qv ^ 2 - qi ^ 2 ∧
    (qv - qi) * symTorusLinkAlex q 2 = qv ^ 3 - qi ^ 3 ∧
    (qv - qi) * symTorusLinkAlex q 3 = qv ^ 4 - qi ^ 4 := by
  intro qv qi
  have hmul : qv * qi = 1 := q.val_inv
  refine ⟨?_, ?_, ?_, ?_⟩
  · unfold symTorusLinkAlex; ring
  · unfold symTorusLinkAlex; ring
  · unfold symTorusLinkAlex; linear_combination -(qv - qi) * hmul
  · unfold symTorusLinkAlex; linear_combination -(qv ^ 2 - qi ^ 2) * hmul

end LeptonAndTorusLinkAlexander

end AdjointTorsionSaddlePrefactors
end QOU.BraidsAndKnots
