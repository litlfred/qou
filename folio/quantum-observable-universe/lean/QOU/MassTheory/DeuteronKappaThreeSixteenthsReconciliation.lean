/-
# Three-way reconciliation of `κ = 3/16` on the deuteron (`²H`, `pn`)

Bean `qou-08xc` (owner ruling `Q-10V9-2 = 1`, parent `qou-10v9`).
Companion probe: `computations/probes/deuteron_kappa_three_sixteenths_reconciliation_probe.py`.

## What this reconciles

Three distinct calculations in the QOU mass and binding program produce the rational constant
`κ = 3/16` (or its deuteron specialization `±1/16`), and conflating them as a single
"Lean-proved `κ = 3/16` correction" hides their distinct algebraic origins, variables (`ℏ_q = 1 - q⁻¹`
vs `ε = q - 1` vs `h = q - q⁻¹`), and normalizations:

1. **Route 1 — Borromean 29-letter Laurent-trace coefficients on `H_{3A}`
   (`QOU.MassTheory.PairwiseChainLeadingOrder`, `QOU.MassTheory.LeadingOrderTraceCoefficient`,
   bean `qou-qqm4`):**
   - At **first order** in `ℏ_q` (equivalently `ε = q - 1`), the Borromean per-nucleon deletion
     weights `(a, b) = (3, -2)` have sum `a + b = 1`, so the three-pair sum is
     `c₁(pp) + c₁(pn) + c₁(nn) = 3(a + b)/16 = 3/16` (`c₁(pp) = 1/8`, `c₁(pn) = 1/16`,
     `c₁(nn) = 0`), making both the `³He` (`pp + pn`) and `⁴He` (`pp + pn + nn`) pairwise chain sums
     equal to `3/16`, while the **deuteron (`pn`, `Z = 1, N = 1`)** has `c₁(pn) = 1/16 = (1/3) · (3/16)`.
   - At **second order** in `ε = q - 1` (`|S| = 2` pair-class decomposition of `Δtr = tr(free) - tr(atom)`,
     bean `qou-qqm4`), the `A = 3` intra-nucleon 3-strand Borromean coefficient is
     `intra(Z, N) = (Z - N) · κ(3)` with `κ(3) = 3/16` (`3p: 9/16`, `T: -3/16`, `³He: 3/16`,
     `3n: -9/16`), which vanishes at `Z = N = 1` (`deuteron_S2_intra = 0`), while the **deuteron
     inter-nucleon cross-term** is `deuteron_S2_cross = -3/16`, partially cancelled by the
     nucleon–interface term `deuteron_S2_nif = +1/8 = +2/16` to give the net `|S| = 2` contribution
     `-3/16 + 1/8 = -1/16` (and total `c₂(pn) = 0 + 27/32 - 1/16 = 25/32`).

2. **Route 2 — Yekutieli / Family-A Borromean `h²` extraction (`κ_Yek = 3/16`) vs standard
   Kauffman–Jones Markov trace (`κ_std = 0`)
   (`QOU.BraidsAndKnots.BorromeanMarkovTrace`, `lambda-scale-substrate-form.lean`, bean `qou-pi4m`):**
   - The Borromean Jones numerator in `h = q - q⁻¹` is `4 + h² - 3h⁴ - h⁶ = 4(1 + (1/4)h² + O(h⁴))`.
   - Under the **standard Kauffman–Jones normalization** `[2]_q² = (q + q⁻¹)² = 4 + h² = 4(1 + (1/4)h²)`,
     the `1 + (1/4)h²` factor cancels identically (`h2_coefficient_cancellation`), so the `h²`
     coefficient of `tr_M(β_Bor, h)` is **`κ_std = 0`** and the leading topological correction is
     `-(3/4)h⁴`.
   - Under the **half-power / `[2]_q + 2` normalization** `(√q + 1/√q)² = q + 2 + q⁻¹ = w² + 4`
     (with `w = q^{1/2} - q^{-1/2}` and `h² = w²(w² + 4) = 4w² + w⁴`, so `w² = (1/4)h² + O(h⁴)` and
     `w² + 4 = 4(1 + (1/16)h² + O(h⁴))`), dividing `4 + h² - 3h⁴ - h⁶` by `w² + 4` produces the
     non-zero `h²` coefficient
     `κ_Yek = 1/4 - 1/16 = 3/16` (and `4 · κ_Yek = 3/4`, matching Family A's `λ_A(h) = 5/2 + (3/4)h²`).
   - Theorem `route2_yekutieli_h2_is_three_sixteenths` (over `ℚ`) and `route2_yekutieli_h2_mul`
     (division-free over any `[CommRing R]`) prove as an exact polynomial identity in `w` that
     `(4 + h²) - (w² + 4)(1 + (3/16)h²)` factors through `w⁴`, uniquely pinning `κ_Yek = 3/16`.

3. **Route 3 — Discretized Yekutieli surface 2-form on the deuteron `pn` trefoil Seifert surface
   (`QOU.QBeta.YekutieliTrefoilDiscretization`, bean `qou-prjo`):**
   - The deuteron `pn` 2-strand closure is the right-handed trefoil `σ₁³` (genus `g = 1`) with
     Seifert matrix `V = [[-1, 1], [0, -1]]`.
   - Because `σ₁³` is a single-generator (abelian) braid word, all 1D path/Magnus commutators vanish,
     and the discretized Yekutieli surface 2-form `∑_{i,j} V_{ij} ⁅A_i, A_j⁆` collapses to its
     skew intersection part `(V_{01} - V_{10}) ⁅A_0, A_1⁆ = 1 · ⁅A_0, A_1⁆` (`surface2Form_trefoil`),
     invariant under scalar color-dressing shifts (`surface2Form_trefoil_dressing_invariant`).
   - Thus Route 3 supplies the **operator carrier** `⁅A_0, A_1⁆` with unit topological intersection
     weight `V_{01} - V_{10} = 1` on the deuteron trefoil Seifert surface, not an independent proof
     of the scalar `3/16`; the scalar `3/16` comes from Route 1 (pairwise chain / `|S| = 2` cross-term)
     or Route 2 (`[2]_q + 2` denominator shift).

-- Ref: [leitner2026] beans qou-08xc, qou-qqm4, qou-pi4m, qou-prjo;
-- computations/probes/deuteron_kappa_three_sixteenths_reconciliation_probe.py
-/
import Mathlib.Tactic
import QOU.MassTheory.PairwiseChainLeadingOrder
import QOU.MassTheory.LeadingOrderTraceCoefficient
import QOU.BraidsAndKnots.BorromeanMarkovTrace
import QOU.QBeta.YekutieliTrefoilDiscretization

namespace QOU.MassTheory.DeuteronKappaReconciliation

/-- The rational constant `κ = 3/16` shared across the Borromean pairwise chain sum,
the `A = 3` intra-nucleon / deuteron cross-nucleon `|S| = 2` expansion, and the
Yekutieli `(√q + 1/√q)²` Borromean `h²` extraction. -/
def kappa_borromean : ℚ := 3 / 16

/-! ## 1. Route 1 — Borromean 29-letter Laurent-trace coefficients on `H_{3A}` -/

/-- At first order in `ℏ_q`, the `³He` (`pp + pn`) pairwise chain sum equals `κ = 3/16`. -/
theorem route1_chain_He3_eq_kappa :
    QOU.MassTheory.c1_pp + QOU.MassTheory.c1_pn = kappa_borromean := by
  unfold QOU.MassTheory.c1_pp QOU.MassTheory.c1_pn kappa_borromean
  norm_num

/-- At first order in `ℏ_q`, the `⁴He` (`pp + pn + nn`) pairwise chain sum also equals `κ = 3/16`
because `c₁(nn) = 0` under the Borromean intra-nucleon ordering. -/
theorem route1_chain_He4_eq_kappa :
    QOU.MassTheory.c1_pp + QOU.MassTheory.c1_pn + QOU.MassTheory.c1_nn = kappa_borromean := by
  unfold QOU.MassTheory.c1_pp QOU.MassTheory.c1_pn QOU.MassTheory.c1_nn kappa_borromean
  norm_num

/-- For the deuteron (`²H`, `pn`, `Z = 1, N = 1`), the first-order trace difference coefficient
derived from the 18-letter star sums `star_pnFree (1/8) - star_pnAtom (1/16)` is `c₁(pn) = 1/16`,
which is exactly one-third of `κ = 3/16` (`c₁(pp) = 2/16` carries the other two-thirds). -/
theorem route1_deuteron_c1_reconciliation :
    QOU.MassTheory.c1_pn =
      QOU.MassTheory.starSum 6 QOU.MassTheory.letters_pnFree -
        QOU.MassTheory.starSum 6 QOU.MassTheory.letters_pnAtom ∧
    QOU.MassTheory.c1_pn = 1 / 16 ∧
    QOU.MassTheory.c1_pn = (1 / 3) * kappa_borromean ∧
    QOU.MassTheory.c1_pp = (2 / 3) * kappa_borromean := by
  refine ⟨QOU.MassTheory.c1_from_letters.2.1, ?_, ?_, ?_⟩ <;>
    · norm_num [QOU.MassTheory.c1_pn, QOU.MassTheory.c1_pp, kappa_borromean]

/-- Why `3/16` appears in the Borromean pairwise sum: for arbitrary per-nucleon letter weights
`(a, b)`, the three `A = 2` pair coefficients sum to `3(a + b)/16` (`pairSum_of_letters`); at the
Borromean weights `(a, b) = (3, -2)` we have `a + b = 1`, pinning the pair sum to `3/16`. -/
theorem route1_borromean_letter_weights_sum_to_kappa :
    QOU.MassTheory.c1Closed 3 (-2) 2 0 +
      QOU.MassTheory.c1Closed 3 (-2) 1 1 +
      QOU.MassTheory.c1Closed 3 (-2) 0 2 = kappa_borromean := by
  rw [QOU.MassTheory.pairSum_of_letters]
  unfold kappa_borromean
  norm_num

/-- At second order in `ε = q - 1` (bean `qou-qqm4`), the `A = 3` intra-nucleon `|S| = 2` pair-class
contribution is `(Z - N) · κ` with `κ(3) = 3/16`. -/
def intraA3 (Z N : ℤ) : ℚ := (Z - N : ℚ) * kappa_borromean

/-- The affine law `intra(Z, N) = (Z - N) · (3/16)` reproduces all four `A = 3` species
(`3p`, `T`, `³He`, `3n`) and vanishes identically at `Z = N = 1` (deuteron isospin singlet/triplet
symmetric content `Z = N`). -/
theorem route1_intraA3_values :
    intraA3 3 0 = 9 / 16 ∧
    intraA3 1 2 = -3 / 16 ∧
    intraA3 2 1 = 3 / 16 ∧
    intraA3 0 3 = -9 / 16 ∧
    intraA3 1 1 = 0 := by
  unfold intraA3 kappa_borromean
  norm_num

/-- Deuteron (`pn`, `Z = 1, N = 1`) second-order `|S| = 2` pair-class components from the exact
diagonal-insertion expansion (`c2_pair_class_decomposition_probe.py`, bean `qou-qqm4`):
- `intra = 0` (`Z = N = 1`)
- `cross = -3/16 = -κ` (inter-nucleon letter pairs)
- `n-if = +1/8 = +2/16` (nucleon–interface letter pairs)
- `if-if = 0` (only one interface letter at `A = 2`). -/
def deuteron_S2_intra : ℚ := 0
def deuteron_S2_cross : ℚ := -3 / 16
def deuteron_S2_nif : ℚ := 1 / 8
def deuteron_S2_ifif : ℚ := 0
def deuteron_S2_total : ℚ := -1 / 16

/-- On the deuteron (`pn`), the `|S| = 2` cross-nucleon term is `-κ = -3/16`, and adding the
nucleon–interface term `+1/8 = +2/16` yields the net `|S| = 2` contribution `-1/16 = -c₁(pn)`,
which combines with `|S| = 0` (`0`) and `|S| = 1` (`27/32`) to give `c₂(pn) = 25/32`. -/
theorem route1_deuteron_S2_reconciliation :
    deuteron_S2_cross = -kappa_borromean ∧
    deuteron_S2_intra + deuteron_S2_cross + deuteron_S2_nif + deuteron_S2_ifif =
      deuteron_S2_total ∧
    deuteron_S2_total = -QOU.MassTheory.c1_pn ∧
    (0 : ℚ) + 27 / 32 + deuteron_S2_total = 25 / 32 := by
  unfold deuteron_S2_intra deuteron_S2_cross deuteron_S2_nif deuteron_S2_ifif
    deuteron_S2_total kappa_borromean QOU.MassTheory.c1_pn
  norm_num

/-! ## 2. Route 2 — Yekutieli `(√q + 1/√q)²` vs standard Kauffman–Jones `[2]_q²` on `β_Bor` -/

section Route2CommRing

variable {R : Type*} [CommRing R]

/-- In terms of the half-step parameter `w = q^{1/2} - q^{-1/2}`, the full Hecke parameter
`h = q - q⁻¹ = (q^{1/2} - q^{-1/2})(q^{1/2} + q^{-1/2})` satisfies `h² = w²(w² + 4)`. -/
def hSqOfW (w : R) : R := w ^ 2 * (w ^ 2 + 4)

/-- The Borromean Jones numerator `4 + h² - 3h⁴ - h⁶` written as a polynomial in `hSq = h²`. -/
def borromeanNumOfHSq (hSq : R) : R := 4 + hSq - 3 * hSq ^ 2 - hSq ^ 3

/-- The Yekutieli / `_li_2_q_util` denominator `(√q + 1/√q)² = q + 2 + q⁻¹ = [2]_q + 2 = w² + 4`. -/
def yekutieliDen (w : R) : R := w ^ 2 + 4

/-- Compatibility with `QOU.BraidsAndKnots.trM_borromean_num`. -/
theorem borromeanNumOfHSq_eq_trM_num (h : R) :
    borromeanNumOfHSq (h ^ 2) = QOU.BraidsAndKnots.trM_borromean_num h := by
  unfold borromeanNumOfHSq QOU.BraidsAndKnots.trM_borromean_num
  ring

/-- **Standard Kauffman–Jones normalization (`[2]_q² = h² + 4`):** the `h²` coefficient of
`tr_M(β_Bor, h)` is `0` (`trM_borromean_num h - trM_borromean_den h · 1` is purely `O(h⁴)`). -/
theorem route2_standard_h2_vanishes (h : R) :
    QOU.BraidsAndKnots.trM_borromean_num h - QOU.BraidsAndKnots.trM_borromean_den h * 1 =
      h ^ 4 * (-3 - h ^ 2) := by
  unfold QOU.BraidsAndKnots.trM_borromean_num QOU.BraidsAndKnots.trM_borromean_den
  ring

/-- **Yekutieli / `[2]_q + 2` normalization (`w² + 4`), division-free over `R[w]`:**
clearing `16`, the remainder `16 · V(𝓑₃) - (w² + 4) · (16 + 3 h²)` factors through `w⁴` (no `w⁰` or
`w²` term). This is the exact algebraic reason dividing `V(𝓑₃)` by `(√q + 1/√q)² = w² + 4`
produces `h²` coefficient `κ_Yek = 3/16` instead of `0`. -/
theorem route2_yekutieli_h2_mul (w : R) :
    16 * borromeanNumOfHSq (hSqOfW w) - yekutieliDen w * (16 + 3 * hSqOfW w) =
      w ^ 4 * (-8 - 3 * w ^ 2 - 48 * (w ^ 2 + 4) ^ 2 - 16 * w ^ 2 * (w ^ 2 + 4) ^ 3) := by
  unfold borromeanNumOfHSq hSqOfW yekutieliDen
  ring

end Route2CommRing

/-- **Over `ℚ`:** dividing the Borromean numerator by `(√q + 1/√q)² = w² + 4` gives the quadratic
approximation `1 + (3/16) h²` with an exact `O(w⁴) = O(h⁴)` remainder. -/
theorem route2_yekutieli_h2_is_three_sixteenths (w : ℚ) :
    borromeanNumOfHSq (hSqOfW w) - yekutieliDen w * (1 + kappa_borromean * hSqOfW w) =
      w ^ 4 * (-1 / 2 - (3 / 16) * w ^ 2 - 3 * (w ^ 2 + 4) ^ 2 - w ^ 2 * (w ^ 2 + 4) ^ 3) := by
  unfold borromeanNumOfHSq hSqOfW yekutieliDen kappa_borromean
  ring

/-- **Uniqueness of `κ_Yek = 3/16`:** for an arbitrary candidate coefficient `κ : ℚ`, the
`w²` term of `borromeanNumOfHSq (hSqOfW w) - yekutieliDen w * (1 + κ * hSqOfW w)` is
`(3 - 16 κ) w²`, which vanishes iff `κ = 3/16`. -/
theorem route2_yekutieli_kappa_unique (κ : ℚ) :
    (∀ w : ℚ,
      borromeanNumOfHSq (hSqOfW w) - yekutieliDen w * (1 + κ * hSqOfW w) =
        (3 - 16 * κ) * w ^ 2 +
          w ^ 4 * (1 - 8 * κ - κ * w ^ 2 - 3 * (w ^ 2 + 4) ^ 2 - w ^ 2 * (w ^ 2 + 4) ^ 3)) ∧
    (3 - 16 * κ = 0 ↔ κ = kappa_borromean) := by
  refine ⟨fun w => ?_, ?_⟩
  · unfold borromeanNumOfHSq hSqOfW yekutieliDen
    ring
  · unfold kappa_borromean
    constructor <;> intro h <;> linarith

/-- **Origin of `3/16` as a denominator shift, and the Family-A `4 · (3/16) = 3/4` bridge:**
- The numerator `4 + h² = 4(1 + (1/4)h²)` contributes `+1/4` at `h²`.
- The standard denominator `4 + h² = 4(1 + (1/4)h²)` subtracts `1/4`, leaving `1/4 - 1/4 = 0`.
- The Yekutieli denominator `4 + w² = 4(1 + (1/16)h² + O(h⁴))` subtracts `1/16`, leaving
  `1/4 - 1/16 = 3/16 = κ_borromean`.
- Multiplying by the `q = 1` loop factor `4` gives `4 · (3/16) = 3/4`, the `h²` slope of
  Family A's `linking_weight_family_a_h(h) = 5/2 + (3/4)h²`. -/
theorem route2_denominator_shift_and_family_a (h : ℚ) :
    (1 : ℚ) / 4 - 1 / 4 = 0 ∧
    (1 : ℚ) / 4 - 1 / 16 = kappa_borromean ∧
    4 * kappa_borromean = 3 / 4 ∧
    QOU.BraidsAndKnots.linking_weight_family_a_h h =
      5 / 2 + (4 * kappa_borromean) * h ^ 2 := by
  refine ⟨by norm_num, ?_, ?_, ?_⟩
  · unfold kappa_borromean; norm_num
  · unfold kappa_borromean; norm_num
  · unfold QOU.BraidsAndKnots.linking_weight_family_a_h kappa_borromean; ring

/-! ## 3. Route 3 — Trefoil Seifert surface 2-form on the deuteron `pn` braid `σ₁³` -/

/-- On the genus-1 right-handed trefoil Seifert surface (`pn` 2-strand braid `σ₁³`), the
skew intersection coefficient `V_{01} - V_{10}` is `+1`, whereas the symmetric self-linking
diagonal entries `V_{00} = V_{11} = -1` cancel out of `surface2Form`. -/
theorem route3_trefoil_seifert_skew_unit :
    QOU.QBeta.YekutieliTrefoilDiscretization.seifertTrefoil 0 1 -
      QOU.QBeta.YekutieliTrefoilDiscretization.seifertTrefoil 1 0 = 1 ∧
    QOU.QBeta.YekutieliTrefoilDiscretization.seifertTrefoil 0 0 = -1 ∧
    QOU.QBeta.YekutieliTrefoilDiscretization.seifertTrefoil 1 1 = -1 := by
  decide

/-- The discretized Yekutieli surface 2-form on the deuteron trefoil Seifert surface equals
the single handle-holonomy commutator `⁅A_0, A_1⁆` with coefficient `1`, and is invariant under
central color/flavor scalar dressings `s_0, s_1`. -/
theorem route3_trefoil_operator_carrier {R : Type*} [Ring R] (A s : Fin 2 → R)
    (h0 : ∀ x, s 0 * x = x * s 0) (h1 : ∀ x, s 1 * x = x * s 1) :
    QOU.QBeta.YekutieliTrefoilDiscretization.surface2Form
        QOU.QBeta.YekutieliTrefoilDiscretization.seifertTrefoil A =
      QOU.QBeta.YekutieliTrefoilDiscretization.bracket (A 0) (A 1) ∧
    QOU.QBeta.YekutieliTrefoilDiscretization.surface2Form
        QOU.QBeta.YekutieliTrefoilDiscretization.seifertTrefoil (fun i => A i + s i) =
      QOU.QBeta.YekutieliTrefoilDiscretization.bracket (A 0) (A 1) := by
  refine ⟨QOU.QBeta.YekutieliTrefoilDiscretization.surface2Form_trefoil A, ?_⟩
  rw [QOU.QBeta.YekutieliTrefoilDiscretization.surface2Form_trefoil_dressing_invariant A s h0 h1,
    QOU.QBeta.YekutieliTrefoilDiscretization.surface2Form_trefoil]

/-! ## 4. Master three-way reconciliation theorem (`qou-08xc`) -/

/-- **Master reconciliation of `κ = 3/16` across all three deuteron / Borromean routes:**
1. **Route 1 (first-order `ℏ_q` chain vs deuteron):** `c₁(pp) + c₁(pn) = 3/16 = κ`, while the
   deuteron (`pn`) alone has `c₁(pn) = 1/16 = κ/3`.
2. **Route 1 (second-order `ε²` `|S| = 2` pair classes):** the `A = 3` intra-nucleon slope is
   `κ = 3/16`, the deuteron cross-nucleon term is `-κ = -3/16`, and adding the nucleon–interface
   term `+1/8` gives the net deuteron `|S| = 2` coefficient `-1/16 = -c₁(pn)`.
3. **Route 2 (`h²` Borromean trace normalization):** standard `[2]_q² = h² + 4` gives `h²`
   coefficient `0`, while `(√q + 1/√q)² = w² + 4` shifts the denominator from `1 + h²/4` to
   `1 + h²/16 + O(h⁴)` and produces `κ = 1/4 - 1/16 = 3/16` (`4κ = 3/4` in Family A).
4. **Route 3 (trefoil Seifert 2-form on `σ₁³`):** provides the framing- and dressing-invariant
   non-abelian commutator carrier `1 · ⁅A_0, A_1⁆` (`V_{01} - V_{10} = 1`). -/
theorem deuteron_kappa_three_way_reconciliation :
    (QOU.MassTheory.c1_pp + QOU.MassTheory.c1_pn = kappa_borromean) ∧
    (QOU.MassTheory.c1_pn = (1 / 3) * kappa_borromean) ∧
    (deuteron_S2_cross = -kappa_borromean) ∧
    (deuteron_S2_cross + deuteron_S2_nif = -QOU.MassTheory.c1_pn) ∧
    ((1 : ℚ) / 4 - 1 / 16 = kappa_borromean) ∧
    (4 * kappa_borromean = 3 / 4) ∧
    (QOU.QBeta.YekutieliTrefoilDiscretization.seifertTrefoil 0 1 -
      QOU.QBeta.YekutieliTrefoilDiscretization.seifertTrefoil 1 0 = 1) := by
  refine ⟨route1_chain_He3_eq_kappa,
    route1_deuteron_c1_reconciliation.2.2.1,
    route1_deuteron_S2_reconciliation.1,
    ?_, ?_, ?_,
    route3_trefoil_seifert_skew_unit.1⟩
  · unfold deuteron_S2_cross deuteron_S2_nif QOU.MassTheory.c1_pn; norm_num
  · unfold kappa_borromean; norm_num
  · unfold kappa_borromean; norm_num

end QOU.MassTheory.DeuteronKappaReconciliation
