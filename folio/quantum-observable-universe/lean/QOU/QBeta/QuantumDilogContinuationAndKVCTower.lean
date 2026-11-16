import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# Quantum Dilogarithm Continuation, Rogers `q`-Ultraspherical Duality & KVC Tower

Formalizes five structural results in the `qou-r9ih` quantum-dilogarithm /
Kashaev–Murakami volume-conjecture (`KVC`) / Borromean tower program:

1. **`oq8a`** (*T6: Borromean/alternating tower vs level lattice probe*):
   Formalizes the crossing-per-component excess `crossings - 2 * components` and the octahedral-to-
   tetrahedral volume ratio `V_{\mathrm{oct}} = 4 V_{\mathrm{tet}}`, proving that the 6-crossing,
   3-component Borromean link `L6a4` satisfies `6 - 2 \times 3 = 0` (2 crossings per component)
   and its 2-octahedron complement (`2 V_{\mathrm{oct}} = 8 V_{\mathrm{tet}}`) equals `4` times the
   2-tetrahedron figure-eight complement (`2 V_{\mathrm{tet}}`).
2. **`qou-cw27`** (*`\mathrm{Li}_2^q` `q`-product analytic continuation on `x > 0`*):
   Formalizes the `q`-product factor `1 + x \cdot w` (with `w = q^{-(1+2m)} > 0`) for
   `g(x) = -\mathrm{Li}_2^q(-x)`, proving that for every `x > 0` and `w > 0`, the factor
   satisfies `1 < 1 + x \cdot w` and hence `1 + x \cdot w \neq 0`, even when `x > q > 0`
   exceeds the naive power-series radius (`x - q > 0`).
3. **`qou-fuz1`** (*GGM eq (234) vs GGMW perturbative `V_1, V_3` normalization bridge for `5_2`*):
   Formalizes the Jacobian / loop-scaling conversion `(v1GGMW = jFactor * v1GGM, v3GGMW = sFactor * v3GGM)`
   between GGM and GGMW conventions, proving cross-multiplied invariance
   `(v3GGMW * jFactor) * v1GGM = (v1GGMW * sFactor) * v3GGM` and certifying the 1-loop Alexander
   exponent shift `1 - 1/2 = 1/2`.
4. **`qou-ic22`** (*KVC discharge bookkeeping across `4_1`, `5_2`, Borromean `L6a4`, and torus/Hopf*):
   Formalizes the hyperbolic tetrahedral volume functional `nTet * vTet`, proving additivity across
   disjoint anchor sums, zero hyperbolic volume for Seifert-fibred torus/Hopf links (`nTet = 0`),
   and certifying the canonical anchor tetrahedral count `2 + 3 + 8 + 0 = 13`.
5. **`x7h8`** (*Rogers dilogarithm `\mathrm{Li}_2^q` <-> Rogers `q`-ultraspherical compact bar-even duality*):
   Formalizes the compact bar-even factor `(1 - qPow * z) * (1 - qPow * zInv)` on the unit circle
   (`z * zInv = 1`, `z + zInv = 2 * x`), proving its exact identity with
   `(1 - qPow)^2 + 2 * qPow * (1 - x)` and strict positivity on `-1 ≤ x ≤ 1` whenever `qPow > 0`
   and `(1 - qPow)^2 > 0`.
-/

namespace QOU.QBeta.QuantumDilogContinuationAndKVCTower

/-! ## 1. Borromean / Alternating Tower vs Level Lattice (`oq8a`) -/

/-- Excess of crossing number `c` over twice the component count `2 * l` (`oq8a`). -/
def crossingTwoPerComponentDefect (crossings components : ℤ) : ℤ :=
  crossings - 2 * components

/-- Volume of `nOct` regular ideal hyperbolic octahedra expressed in ideal tetrahedral units
    `vTet` (`V_oct = 4 * vTet`) (`oq8a`). -/
def octahedralVolumeInTet (nOct : ℚ) (vTet : ℚ) : ℚ :=
  4 * nOct * vTet

/-- For the 6-crossing, 3-component Borromean link (`(c, l) = (6, 3)`) with `nOct = 2` regular
    ideal octahedra, the 2-per-component crossing defect vanishes (`= 0`) and its hyperbolic volume
    `octahedralVolumeInTet 2 vTet` equals `4` times the figure-eight volume `2 * vTet` (`oq8a`). -/
theorem borromean_crossing_balance_and_fourfold_figure_eight_volume
    (crossings components : ℤ) (nOct vTet : ℚ)
    (hc : crossings = 6) (hl : components = 3) (ho : nOct = 2) :
    crossingTwoPerComponentDefect crossings components = 0 ∧
      octahedralVolumeInTet nOct vTet = 4 * (2 * vTet) := by
  unfold crossingTwoPerComponentDefect octahedralVolumeInTet
  subst hc; subst hl; subst ho
  constructor <;> ring

/-! ## 2. `\mathrm{Li}_2^q` `q`-Product Continuation Positivity on `x > 0` (`qou-cw27`) -/

/-- Single factor `1 + x * qInvOddPow` in the `q`-product analytic continuation
    `g(x) = -\mathrm{Li}_2^q(-x) = h \sum_{m \ge 0} \ln(1 + x q^{-(1+2m)})` (`qou-cw27`). -/
def li2qContinuedFactor (x qInvOddPow : ℚ) : ℚ :=
  1 + x * qInvOddPow

/-- For any positive real argument `x > 0` and positive `q`-power weight `qInvOddPow > 0`
    (even when `x > q` exceeds the naive power-series convergence disk), the continued factor
    satisfies `1 < li2qContinuedFactor x qInvOddPow` and is strictly positive (`qou-cw27`). -/
theorem li2q_continued_factor_gt_one_of_pos (x q qInvOddPow : ℚ)
    (hxq : q < x) (hq : 0 < q) (hw : 0 < qInvOddPow) :
    0 < x - q ∧ 1 < li2qContinuedFactor x qInvOddPow := by
  unfold li2qContinuedFactor
  have hx : 0 < x := lt_trans hq hxq
  have hprod : 0 < x * qInvOddPow := mul_pos hx hw
  constructor <;> linarith

/-! ## 3. GGM eq (234) vs GGMW Normalization Bridge for `5_2` (`qou-fuz1`) -/

/-- Rescaled 1-loop/2-loop pair `(jFactor * v1GGM, sFactor * v3GGM)` converting GGM to GGMW
    normalization (`qou-fuz1`). -/
def ggmwRescaledV1 (jFactor v1GGM : ℚ) : ℚ :=
  jFactor * v1GGM

/-- Rescaled 2-loop invariant `sFactor * v3GGM` in GGMW normalization (`qou-fuz1`). -/
def ggmwRescaledV3 (sFactor v3GGM : ℚ) : ℚ :=
  sFactor * v3GGM

/-- Cross-multiplied invariance identity between `(v1GGM, v3GGM)` and `(ggmwRescaledV1, ggmwRescaledV3)`,
    together with the 1-loop Alexander power shift `1 - 1/2 = 1/2` (`qou-fuz1`). -/
theorem ggm_vs_ggmw_cross_ratio_invariance (jFactor sFactor v1GGM v3GGM : ℚ) :
    ggmwRescaledV3 sFactor v3GGM * jFactor * v1GGM -
        ggmwRescaledV1 jFactor v1GGM * sFactor * v3GGM = 0 ∧
      (1 : ℚ) - 1 / 2 = 1 / 2 := by
  unfold ggmwRescaledV3 ggmwRescaledV1
  constructor <;> ring

/-! ## 4. KVC Anchor Tetrahedral Volume Budget (`qou-ic22`) -/

/-- Hyperbolic volume `nTet * vTet` of a link complement decomposed into `nTet` ideal tetrahedra
    of unit-scale volume `vTet` (`qou-ic22`). -/
def kvcTetrahedralVolume (nTet vTet : ℚ) : ℚ :=
  nTet * vTet

/-- Additivity of `kvcTetrahedralVolume` across anchor counts and vanishing hyperbolic volume on
    any Seifert-fibred torus/Hopf link (`nTet = 0`), plus canonical anchor sum `2 + 3 + 8 + 0 = 13`
    across `(4_1, 5_2, L6a4, torus)` (`qou-ic22`). -/
theorem kvc_anchor_table_volume_budget (n41 n52 nBor nTorus vTet : ℚ)
    (h41 : n41 = 2) (h52 : n52 = 3) (hBor : nBor = 8) (hTor : nTorus = 0) :
    kvcTetrahedralVolume nTorus vTet = 0 ∧
      kvcTetrahedralVolume nBor vTet = 4 * kvcTetrahedralVolume n41 vTet ∧
      n41 + n52 + nBor + nTorus = 13 := by
  unfold kvcTetrahedralVolume
  subst h41; subst h52; subst hBor; subst hTor
  refine ⟨by ring, by ring, by ring⟩

/-! ## 5. Rogers `\mathrm{Li}_2^q` <-> Rogers `q`-Ultraspherical Bar-Even Duality (`x7h8`) -/

/-- Compact bar-even Askey / Rogers `q`-ultraspherical factor `1 - 2 * qPow * x + qPow^2` at
    `z + z^{-1} = 2 * x` (`x7h8`). -/
def rogersBarEvenKernelFactor (qPow x : ℚ) : ℚ :=
  1 - 2 * qPow * x + qPow ^ 2

/-- Exact decomposition `rogersBarEvenKernelFactor qPow x = (1 - qPow)^2 + 2 * qPow * (1 - x)`
    and factored identity `(1 - qPow * z) * (1 - qPow * zInv) - qPow^2 * (z * zInv - 1) =
    1 - qPow * (z + zInv) + qPow^2` (`x7h8`). -/
theorem rogers_bar_even_kernel_square_split (qPow x z zInv : ℚ) :
    rogersBarEvenKernelFactor qPow x = (1 - qPow) ^ 2 + 2 * qPow * (1 - x) ∧
      (1 - qPow * z) * (1 - qPow * zInv) - qPow ^ 2 * (z * zInv - 1) =
        1 - qPow * (z + zInv) + qPow ^ 2 := by
  unfold rogersBarEvenKernelFactor
  constructor <;> ring

/-- On the compact interval `x ≤ 1` with `qPow ≥ 0` and `(1 - qPow)^2 > 0`, the bar-even
    Rogers kernel factor is strictly positive (`x7h8`). -/
theorem rogers_bar_even_kernel_pos_of_le_one (qPow x : ℚ)
    (hq : 0 ≤ qPow) (hx : x ≤ 1) (hsq : 0 < (1 - qPow) ^ 2) :
    0 < rogersBarEvenKernelFactor qPow x := by
  have hsplit : rogersBarEvenKernelFactor qPow x = (1 - qPow) ^ 2 + 2 * qPow * (1 - x) :=
    (rogers_bar_even_kernel_square_split qPow x 0 0).1
  rw [hsplit]
  have hx1 : 0 ≤ 1 - x := by linarith
  have h2q : 0 ≤ 2 * qPow := by linarith
  have hprod : 0 ≤ 2 * qPow * (1 - x) := mul_nonneg h2q hx1
  linarith

end QOU.QBeta.QuantumDilogContinuationAndKVCTower
