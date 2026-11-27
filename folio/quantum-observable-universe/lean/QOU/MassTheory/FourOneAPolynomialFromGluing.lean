import Mathlib.Tactic
import QOU.Nuclear.RouteANewtonPolygonDT
import QOU.Nuclear.StokesMatrixProvenance
import QOU.Nuclear.FiveTwoDTSpectrumSplit
import BraidKnotOctonion.AJFigureEight
import QOU.MassTheory.FiveTwoAPolynomialFromFareyWord

/-!
# QOU.Mass.FourOneAPolynomialFromGluing — `4₁` A-polynomial derived from Neumann–Zagier gluing and cross-checked against all corpus carriers (`qou-m1tr`)

Closes the remaining open items of bean `qou-m1tr` (*Transcription audit: verify the hand-typed GGM
Stokes matrices / A-polynomial / `5₂` slopes against the source PDFs*):

1. **First-principles algebraic derivation of `A_{4₁}(L, M)` from the Neumann–Zagier gluing equations
   of `S³ ∖ 4₁` (no hand-transcription).**
   From the derived two-tetrahedron triangulation of `S³ ∖ 4₁` (Farey word `R`, witness
   `nz-gluing-from-braid-monodromy.witness.json`), the edge and cusp holonomy equations in `(z₀, z₁)` are
   * edge gluing: `z₀ · z₁ · (1 − z₀) · (1 − z₁) = 1`,
   * meridian: `M² · z₀ · (1 − z₁) = 1`,
   * longitude: `L² · z₁ · (1 − z₁) = z₀ · (1 − z₀)` (with complete-point lift `z₀(1 − z₀) = −L` at
     `z₀ = z₁ = (1 + i√3)/2`, `(L, M) = (−1, 1)`).
   We prove by an explicit division-free Bezout polynomial certificate over `ℤ[z₀, z₁, L, M]`
   (`A41_bezout_certificate`, `A41_vanishes_of_nz_gluing_lift`, `A41_pm_vanishes_of_nz_gluing`) that
   every solution satisfies `A41(L, M) = 0` on the `L = −1` branch and `A41(L, M) · A41(−L, M) = 0`
   unconditionally.

2. **Exact four-way agreement across all held references and Lean carriers:**
   * `A41` = Culler's census `library/A_census.tgz:apolys/K2_1.apoly` (`A41_eq_census`),
   * `A41` = `AJFigureEight.aPolyFigureEight`, the sorry-free `q = 1` specialization of the `4₁`
     colored-Jones q-difference operator (`A41_eq_AJ`),
   * `A41_routeA = −A41`, whose explicit 7-term nonzero monomial support equals
     `RouteANewtonPolygonDT.a41Monomials` (`a41TermTable_eval`,
     `a41TermTable_support_eq_a41Monomials`, `a41TermTable_all_coeffs_nonzero`),
   * Property-P meridian specialization `A41(L, ±1) = (L + 1)²`, boundary-orientation involution
     `L² M⁸ A41(L⁻¹, M⁻¹) = A41(L, M)`, and amphichiral mirror symmetry `L² A41(L⁻¹, M) = A41(L, M)`.

3. **Direct cross-module GGM Stokes provenance bridge (`FiveTwoDTSpectrumSplit` ↔
   `StokesMatrixProvenance` + GGM eq (60) `4₁` inversion):**
   Connects `FiveTwoDTSpectrumSplit.Splus0 / Sminus0` directly to
   `StokesMatrixProvenance.SplusRecon / SminusRecon` reconstructed from GGM `2012.00062v3` eq (98),
   and checks GGM eq (17)/(60) `S⁺(0)ᵀ S⁻(0) = I₂` for `4₁`.

## Base ring (§7c)
Purely algebraic (`[CommRing K]`, `[IsDomain K]`, `[Field F]`, `Int`); no `ℝ`, no archimedean order.
-/

namespace QOU.Mass.FourOneAPolynomialFromGluing

section CommRing

variable {K : Type*} [CommRing K]

/-- The geometric A-polynomial of the figure-eight knot `4₁`:
`A_{4₁}(L, M) = M⁴ L² − (M⁸ − M⁶ − 2 M⁴ − M² + 1) L + M⁴`. -/
def A41 (L M : K) : K :=
  M ^ 4 * L ^ 2 - (M ^ 8 - M ^ 6 - 2 * M ^ 4 - M ^ 2 + 1) * L + M ^ 4

/-- Culler's census `A_{K2_1}` (`4₁ = m004`), transcribed verbatim from
`library/A_census.tgz:apolys/K2_1.apoly`:
`(1*M^4) + (L^1)*(-1 + 1*M^2 + 2*M^4 + 1*M^6 - 1*M^8) + (L^2)*(1*M^4)`. -/
def A41_census (L M : K) : K :=
  1 * M ^ 4 + L * (-1 + 1 * M ^ 2 + 2 * M ^ 4 + 1 * M ^ 6 - 1 * M ^ 8) + L ^ 2 * (1 * M ^ 4)

/-- The sign convention stated in `RouteANewtonPolygonDT`:
`−M⁴ + L(1 − M² − 2 M⁴ − M⁶ + M⁸) − L² M⁴`. -/
def A41_routeA (L M : K) : K :=
  -M ^ 4 + L * (1 - M ^ 2 - 2 * M ^ 4 - M ^ 6 + M ^ 8) - L ^ 2 * M ^ 4

/-- `A41` agrees identically with Culler's census `A_{K2_1}`. -/
theorem A41_eq_census (L M : K) : A41 L M = A41_census L M := by
  unfold A41 A41_census; ring

/-- `RouteANewtonPolygonDT`'s convention is the exact negative `-A41` (identical zero locus and
Newton polygon). -/
theorem A41_routeA_eq_neg (L M : K) : A41_routeA L M = -A41 L M := by
  unfold A41 A41_routeA; ring

/-- Over `M = 1` the curve has only the parabolic point `L = −1`, with multiplicity two
(Property-P meridian filling consistency, parallel to `FiveTwoAPolynomialFromFareyWord.A_at_M_one`). -/
theorem A41_at_M_one (L : K) : A41 L 1 = (L + 1) ^ 2 := by
  unfold A41; ring

/-- Likewise over `M = −1` (the second lift of the trivial meridian holonomy `M² = 1`). -/
theorem A41_at_M_neg_one (L : K) : A41 L (-1) = (L + 1) ^ 2 := by
  unfold A41; ring

/-- The complete hyperbolic structure `(L, M) = (−1, 1)` lies on the curve. -/
theorem A41_complete_point : A41 (-1 : K) 1 = 0 := by
  rw [A41_at_M_one]; ring

/-! ## 1. Exact division-free elimination from the Neumann–Zagier gluing equations of `S³ ∖ 4₁` -/

/-- Step 1 (eliminating `z₁`): from `-L · z₁(1 − z₁) − 1` and `M² z₀(1 − z₁) − 1`, an explicit
polynomial combination yields the second quadratic `-L(M² z₀ − 1) − M⁴ z₀²`. -/
theorem nz_eliminate_z1_identity (z0 z1 L M : K) :
    M ^ 4 * z0 ^ 2 * (-L * z1 * (1 - z1) - 1)
      + L * (M ^ 2 * z0 * z1 - 1) * (M ^ 2 * z0 * (1 - z1) - 1)
      = -L * (M ^ 2 * z0 - 1) - M ^ 4 * z0 ^ 2 := by
  ring

/-- Step 2 (eliminating `z₀`): explicit Bezout polynomial combination over `ℤ[z₀, L, M]`
producing `-L · A41(L, M)` from `z₀² − z₀ − L` and `-L(M² z₀ − 1) − M⁴ z₀²`. -/
theorem A41_bezout_certificate (z0 L M : K) :
    (L ^ 2 * M ^ 4 - L * M ^ 8 + L * M ^ 6 + L * M ^ 4 + (L * M ^ 6 + M ^ 8) * z0) *
      (z0 ^ 2 - z0 - L)
    + (-L * M ^ 4 - L * M ^ 2 + L - M ^ 4 + (L * M ^ 2 + M ^ 4) * z0) *
      (-L * (M ^ 2 * z0 - 1) - M ^ 4 * z0 ^ 2)
    = -L * A41 L M := by
  unfold A41; ring

/-- **Derivation of `A_{4₁}` on the complete-structure lift:** any solution `(z₀, z₁, L, M)` in an
integral domain (`L ≠ 0`) of the Neumann–Zagier edge and meridian equations together with the
`L = −1` longitude lift `z₀(1 − z₀) = −L` satisfies `A41(L, M) = 0`. -/
theorem A41_vanishes_of_nz_gluing_lift [IsDomain K] {z0 z1 L M : K} (hL : L ≠ 0)
    (he : z0 * z1 * (1 - z0) * (1 - z1) = 1)
    (hm : M ^ 2 * z0 * (1 - z1) = 1)
    (hl : z0 * (1 - z0) = -L) :
    A41 L M = 0 := by
  have hf : z0 ^ 2 - z0 - L = 0 := by
    calc z0 ^ 2 - z0 - L = -(z0 * (1 - z0) - (-L)) := by ring
      _ = 0 := by rw [hl, sub_self, neg_zero]
  have hzz1 : -L * z1 * (1 - z1) - 1 = 0 := by
    calc -L * z1 * (1 - z1) - 1
        = (z0 * z1 * (1 - z0) * (1 - z1) - 1) - z1 * (1 - z1) * (z0 * (1 - z0) + L) := by ring
      _ = (1 - 1) - z1 * (1 - z1) * (-L + L) := by rw [he, hl]
      _ = 0 := by ring
  have hm0 : M ^ 2 * z0 * (1 - z1) - 1 = 0 := sub_eq_zero.mpr hm
  have hq : -L * (M ^ 2 * z0 - 1) - M ^ 4 * z0 ^ 2 = 0 := by
    rw [← nz_eliminate_z1_identity z0 z1 L M, hzz1, hm0]; ring
  have hLA : -L * A41 L M = 0 := by
    rw [← A41_bezout_certificate z0 L M, hf, hq]; ring
  rcases mul_eq_zero.mp hLA with hnegL | hA
  · exact absurd (neg_eq_zero.mp hnegL) hL
  · exact hA

/-- **Unconditional derivation of `A_{4₁}` from the un-lifted Neumann–Zagier equations:**
from `z₀ z₁(1 − z₀)(1 − z₁) = 1`, `M² z₀(1 − z₁) = 1`, and `L² z₁(1 − z₁) = z₀(1 − z₀)` in any
integral domain (`L ≠ 0`), `(z₀(1 − z₀))² = L²` splits into the two sign lifts `±L`, yielding
`A41(L, M) · A41(−L, M) = 0`. -/
theorem A41_pm_vanishes_of_nz_gluing [IsDomain K] {z0 z1 L M : K} (hL : L ≠ 0)
    (he : z0 * z1 * (1 - z0) * (1 - z1) = 1)
    (hm : M ^ 2 * z0 * (1 - z1) = 1)
    (hl2 : L ^ 2 * z1 * (1 - z1) = z0 * (1 - z0)) :
    A41 L M * A41 (-L) M = 0 := by
  have hsq : (z0 * (1 - z0) + L) * (z0 * (1 - z0) - L) = 0 := by
    calc (z0 * (1 - z0) + L) * (z0 * (1 - z0) - L)
        = z0 * (1 - z0) * (z0 * (1 - z0) - L ^ 2 * z1 * (1 - z1))
          + L ^ 2 * (z0 * z1 * (1 - z0) * (1 - z1) - 1) := by ring
      _ = z0 * (1 - z0) * (z0 * (1 - z0) - z0 * (1 - z0)) + L ^ 2 * (1 - 1) := by rw [hl2, he]
      _ = 0 := by ring
  rcases mul_eq_zero.mp hsq with hplus | hminus
  · have hl_neg : z0 * (1 - z0) = -L := eq_neg_of_add_eq_zero_left hplus
    rw [A41_vanishes_of_nz_gluing_lift hL he hm hl_neg, zero_mul]
  · have hl_pos : z0 * (1 - z0) = -(-L) := by
      rw [neg_neg]; exact sub_eq_zero.mp hminus
    rw [A41_vanishes_of_nz_gluing_lift (neg_ne_zero.mpr hL) he hm hl_pos, mul_zero]

end CommRing

/-! ## 2. Field-level symmetries and AJ colored-Jones bridge -/

section Field

variable {F : Type*} [Field F]

/-- Exact agreement with `AJFigureEight.aPolyFigureEight` (the `q = 1` specialization of the
sorry-free `4₁` colored-Jones operator). -/
theorem A41_eq_AJ (L M : F) :
    A41 L M = QOU.BraidKnot.AJFigureEight.aPolyFigureEight L M := rfl

/-- Boundary-orientation involution: `L² M⁸ · A41(L⁻¹, M⁻¹) = A41(L, M)`. -/
theorem A41_involution (L M : F) (hL : L ≠ 0) (hM : M ≠ 0) :
    L ^ 2 * M ^ 8 * A41 L⁻¹ M⁻¹ = A41 L M := by
  unfold A41; field_simp; ring

/-- **Amphichirality of `4₁`** (contrasting `FiveTwoAPolynomialFromFareyWord.A_ne_A_census`):
under the mirror transformation `L ↦ L⁻¹`, `L² · A41(L⁻¹, M) = A41(L, M)` identically. -/
theorem A41_amphichiral_L (L M : F) (hL : L ≠ 0) :
    L ^ 2 * A41 L⁻¹ M = A41 L M := by
  unfold A41; field_simp; ring

/-- Mirror invariance in `M` as well: `M⁸ · A41(L, M⁻¹) = A41(L, M)`. -/
theorem A41_amphichiral_M (L M : F) (hM : M ≠ 0) :
    M ^ 8 * A41 L M⁻¹ = A41 L M := by
  unfold A41; field_simp; ring

end Field

/-! ## 3. Exact monomial-support bridge to `RouteANewtonPolygonDT` and GGM Stokes cross-checks -/

/-- Explicit `(deg_M, deg_L, coeff)` table of `A41_routeA`. -/
def a41TermTable : List (Int × Int × Int) :=
  [ (4, 0, -1)
  , (0, 1,  1)
  , (2, 1, -1)
  , (4, 1, -2)
  , (6, 1, -1)
  , (8, 1,  1)
  , (4, 2, -1) ]

/-- Summing `a41TermTable` reproduces `A41_routeA` identically over `Int`. -/
theorem a41TermTable_eval (L M : Int) :
    (a41TermTable.foldl (fun acc t => acc + t.2.2 * M ^ t.1.toNat * L ^ t.2.1.toNat) 0)
      = A41_routeA L M := by
  simp only [a41TermTable, List.foldl, Int.toNat]
  unfold A41_routeA
  ring

/-- Every entry of `a41TermTable` carries a nonzero coefficient, and its exponent list is
definitionally equal to `RouteANewtonPolygonDT.a41Monomials` — certifying that `a41Monomials` is
the exact support of `A41_routeA = −A41`. -/
theorem a41TermTable_support_eq_a41Monomials :
    a41TermTable.map (fun t => (t.1, t.2.1)) = QOU.QBeta.RouteANewtonPolygonDT.a41Monomials ∧
      (∀ t ∈ a41TermTable, t.2.2 ≠ 0) := by
  decide

/-- Cross-module provenance theorem: `FiveTwoDTSpectrumSplit.Splus0` and `Sminus0` equal
`StokesMatrixProvenance.SplusRecon` and `SminusRecon` reconstructed from GGM `2012.00062v3` eq (98). -/
theorem fiveTwo_stokes_split_eq_provenance_recon :
    (∀ i j, QOU.QBeta.FiveTwoDTSpectrumSplit.Splus0 i j =
      QOU.QBeta.StokesMatrixProvenance.SplusRecon i j) ∧
    (∀ i j, QOU.QBeta.FiveTwoDTSpectrumSplit.Sminus0 i j =
      QOU.QBeta.StokesMatrixProvenance.SminusRecon i j) := by
  decide

/-- GGM `2012.00062v3` eq (60) (`\label{eq:S0u041}`) negative-chirality leading Stokes matrix
`S⁻(0) = [[1, 0], [−3, 1]]` for `4₁`. -/
def Sminus0_41 : Fin 2 → Fin 2 → Int
  | 0, 0 =>  1 | 0, 1 => 0
  | 1, 0 => -3 | 1, 1 => 1

/-- GGM eq (17) (`S⁺(0)ᵀ · S⁻(0) = I₂`) verified for `4₁`'s leading Stokes pair eq (60). -/
theorem fourOne_stokes_inversion_eq17 :
    ∀ i j : Fin 2,
      (QOU.QBeta.FiveTwoDTSpectrumSplit.Splus0_41 0 i * Sminus0_41 0 j +
       QOU.QBeta.FiveTwoDTSpectrumSplit.Splus0_41 1 i * Sminus0_41 1 j)
        = (if i = j then 1 else 0) := by
  decide

end QOU.Mass.FourOneAPolynomialFromGluing
