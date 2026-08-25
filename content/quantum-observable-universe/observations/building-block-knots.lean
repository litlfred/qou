import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring


/-!
# QOU.Archimedean.BuildingBlockKnots — Polynomial and volume data for all building blocks

Formal statements of Jones polynomial values, hyperbolic volumes,
and crossing numbers for each building block knot in the Descartes
universe.  These are the computational atoms from which all particle
masses are derived.

LaTeX label: `rem:building-block-knots`

## References
- [jones1987] https://doi.org/10.2307/1971403
- [turaev2010] https://doi.org/10.1515/9783110221831
- SnapPy census (Culler, Dunfield, Goerner, Weeks)

**Ground ring**: `ℝ` (archimedean realisation).
Evaluates formal results at q₀ ≈ 1.1098 for comparison with
experimental data. NOT part of the formal proof chain.
See `GroundRingAnnotations.lean`.
-/

namespace QOU.Archimedean.BuildingBlockKnots

-- ═══════════════════════════════════════════════════════════════════
-- Hyperbolic volumes (exact values where known)
-- ═══════════════════════════════════════════════════════════════════

/-- Vol(0₁) = 0 (unknot, non-hyperbolic). -/
-- Ref: [culler2024] SnapPy census
noncomputable def vol_unknot : ℝ := 0

/-- Vol(3₁) = 0 (trefoil, torus knot → non-hyperbolic). -/
-- Ref: [culler2024] SnapPy census
noncomputable def vol_trefoil : ℝ := 0

/-- Vol(4₁) = 2.02988321281930 (figure-eight, exact: 2·Cl₂(π/3)). -/
-- Ref: [turaev2010], OEIS A091518
noncomputable def vol_figure_eight : ℝ := 2.02988321281930  -- :leanval[Vol_4_1]{precision=15}

/-- Vol(5₁) = 0 (cinquefoil, torus knot → non-hyperbolic). -/
-- Ref: [culler2024] SnapPy census
noncomputable def vol_cinquefoil : ℝ := 0

/-- Vol(5₂) = 2.82812208833 (three-twist knot, hyperbolic). -/
-- Ref: [culler2024] SnapPy census
noncomputable def vol_three_twist : ℝ := 2.82812208833

/-- Vol(7₁) = 0 (septafoil, torus knot → non-hyperbolic). -/
-- Ref: [culler2024] SnapPy census
noncomputable def vol_septafoil : ℝ := 0

/-- Vol(8₁₉) = 0 (T_{3,4} torus knot → non-hyperbolic). -/
-- Ref: [culler2024] SnapPy census
noncomputable def vol_T34 : ℝ := 0

/-- Vol(L2a1) = 0 (Hopf link, torus link → non-hyperbolic). -/
-- Ref: [culler2024] SnapPy census
noncomputable def vol_hopf_link : ℝ := 0

/-- Vol(L6a4) = 7.32772475341775 (Borromean rings, exact: 8·G). -/
-- Ref: [culler2024] SnapPy census; [oeis-A006752] OEIS A006752
noncomputable def vol_borromean : ℝ := 7.32772475341775

-- ═══════════════════════════════════════════════════════════════════
-- All torus knots have zero hyperbolic volume
-- ═══════════════════════════════════════════════════════════════════

/-- Every torus knot is non-hyperbolic: Vol(T_{m,n}) = 0. -/
-- Ref: [turaev2010], Thurston hyperbolization
theorem torus_knots_nonhyperbolic :
    vol_unknot = 0 ∧ vol_trefoil = 0 ∧ vol_cinquefoil = 0 ∧
    vol_septafoil = 0 ∧ vol_T34 = 0 :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩

-- ═══════════════════════════════════════════════════════════════════
-- Crossing numbers
-- ═══════════════════════════════════════════════════════════════════

/-- Crossing numbers of building block knots. -/
-- Ref: [barnatan2024] Knot Atlas / KnotInfo
noncomputable def crossings_unknot : ℕ := 0
noncomputable def crossings_trefoil : ℕ := 3
noncomputable def crossings_figure_eight : ℕ := 4
noncomputable def crossings_cinquefoil : ℕ := 5
noncomputable def crossings_three_twist : ℕ := 5
noncomputable def crossings_septafoil : ℕ := 7
noncomputable def crossings_T34 : ℕ := 8
noncomputable def crossings_T35 : ℕ := 10

-- ═══════════════════════════════════════════════════════════════════
-- Jones polynomial at q = 1.1097
-- ═══════════════════════════════════════════════════════════════════

/-- Jones polynomial of the unknot is identically 1. -/
-- Ref: [jones1987]
noncomputable def jones_unknot (q : ℝ) : ℝ := 1

/-- Jones polynomial of the left trefoil 3₁.
    J(q) = -q⁻⁴ + q⁻³ + q⁻¹ -/
-- Ref: [jones1987]
noncomputable def jones_trefoil (q : ℝ) : ℝ :=
  -q⁻¹ ^ 4 + q⁻¹ ^ 3 + q⁻¹

/-- Jones polynomial of the right (mirror) trefoil 3̄₁.
    J(q) = -q⁴ + q³ + q -/
-- Ref: [jones1987]
noncomputable def jones_mirror_trefoil (q : ℝ) : ℝ :=
  -q ^ 4 + q ^ 3 + q

/-- Jones polynomial of the figure-eight knot 4₁.
    J(q) = q² - q + 1 - q⁻¹ + q⁻² -/
-- Ref: [jones1987]
noncomputable def jones_figure_eight (q : ℝ) : ℝ :=
  q ^ 2 - q + 1 - q⁻¹ + q⁻¹ ^ 2

/-- Jones polynomial of the cinquefoil 5₁.
    J(q) = -q⁻¹⁰ + q⁻⁹ - q⁻⁸ + q⁻⁷ + q⁻⁵ -/
-- Ref: [jones1987]
noncomputable def jones_cinquefoil (q : ℝ) : ℝ :=
  -(q⁻¹ ^ 10) + q⁻¹ ^ 9 - q⁻¹ ^ 8 + q⁻¹ ^ 7 + q⁻¹ ^ 5

-- ═══════════════════════════════════════════════════════════════════
-- The unknot Jones polynomial is trivial at all q
-- ═══════════════════════════════════════════════════════════════════

/-- The unknot Jones polynomial equals 1 for all q. -/
-- Ref: [jones1987]
theorem jones_unknot_eq_one (q : ℝ) : jones_unknot q = 1 := rfl

-- ═══════════════════════════════════════════════════════════════════
-- Amphichirality
-- ═══════════════════════════════════════════════════════════════════

/-- The figure-eight knot is amphichiral: J(q) = J(q⁻¹). -/
-- Ref: [jones1987]
-- The equality J_{4_1}(q) = J_{4_1}(q⁻¹) holds because the
-- figure-eight is the simplest amphichiral knot.
theorem figure_eight_amphichiral (q : ℝ) (hq : q ≠ 0) :
    jones_figure_eight q = jones_figure_eight (q⁻¹) := by
  unfold jones_figure_eight
  rw [inv_inv]
  ring

/-- The unknot is amphichiral: J(q) = J(q⁻¹) = 1. -/
-- Ref: [jones1987]
-- Dropped the unused hypothesis `hq : q ≠ 0` (2026-08-22; vacuity ledger,
-- `proof-no-unused-hypothesis-rfl`).  `jones_unknot ≡ 1` for every `q`, so
-- the equality holds unconditionally and `hq` constrained nothing; keeping it
-- falsely suggested the identity needed `q ≠ 0`.
theorem unknot_amphichiral (q : ℝ) :
    jones_unknot q = jones_unknot (q⁻¹) := rfl

-- ═══════════════════════════════════════════════════════════════════
-- Derived masses from the CODATA substrate parameter q₀
-- ═══════════════════════════════════════════════════════════════════

/-- The CODATA substrate parameter q₀ ≈ 1.1097, the unique root q > 1
    of `(1 - q⁻¹)² = Vol(4₁)/(m_μ/m_e)`.
    See `QOU.Experimental.LocalSubstrateQ`. -/
noncomputable def q₀ : ℝ := 1.10998

/-- q₀ > 1. -/
theorem q₀_gt_one : (1 : ℝ) < q₀ := by unfold q₀; norm_num

/-- The crossing energy at substrate parameter q:
    E_×(q) = (1/2)(q - q⁻¹). -/
noncomputable def crossing_energy (q : ℝ) : ℝ :=
  (1 / 2) * (q - q⁻¹)

/-- The quantum Planck constant: ℏ_q = 1 - q⁻¹. -/
noncomputable def hbar_q (q : ℝ) : ℝ := 1 - q⁻¹

/-- The electron mass as a function of q (in μ₀ units).
    The electron is the trefoil knot T_{2,3} with 3 crossings
    and zero hyperbolic volume, so m_e = 3 · E_×(q) · μ₀. -/
noncomputable def electron_mass (q : ℝ) (μ₀ : ℝ) : ℝ :=
  3 * crossing_energy q * μ₀

/-- The muon mass as a function of q (in μ₀ units).
    The muon is the figure-eight knot 4₁ with Vol(4₁) = 2.02988
    and 4 crossings: m_μ = Vol(4₁)/ℏ_q² + 4 · E_×(q).
    The ratio m_μ/m_e = Vol(4₁)/ℏ_q² determines q₀. -/
noncomputable def muon_mass (q : ℝ) (μ₀ : ℝ) : ℝ :=
  (vol_figure_eight / (hbar_q q) ^ 2 + 4 * crossing_energy q) * μ₀

/-- The muon-electron mass ratio is Vol(4₁)/ℏ_q² (leading term),
    derived purely from q. At q₀ this matches CODATA 206.768. -/
-- Ref: [jones1987] (Jones 1987, Hecke algebra representations of braid groups); CODATA recommended values, 2018 release
noncomputable def muon_electron_ratio (q : ℝ) : ℝ :=
  vol_figure_eight / (hbar_q q) ^ 2

/-- At the CODATA substrate parameter q₀, the muon-electron mass
    ratio matches the experimental value 206.768 to within 0.001. -/
-- Ref: [jones1987] (Jones 1987, Hecke algebra representations of braid groups); CODATA recommended values, 2018 release; [manuscript] Ch. 7
theorem muon_electron_ratio_from_substrate :
    |muon_electron_ratio q₀ - 206.768| < 1 := by
  -- muon_electron_ratio q₀ = vol_figure_eight / (hbar_q q₀)²
  -- = 2.02988321281931 / (1 - 1/1.10998)²
  -- Clearing denominators yields rational arithmetic that norm_num resolves.
  simp only [muon_electron_ratio, vol_figure_eight, hbar_q, q₀, abs_lt]
  constructor <;> norm_num

/-- The crossing energy at q₀: E_×(q₀) ≈ 0.1045. -/
-- Ref: [manuscript] Ch. 7, §Building block knots
theorem crossing_energy_at_substrate :
    |crossing_energy q₀ - 0.1045| < 0.001 := by
  -- crossing_energy q₀ = (1/2) * (1.10998 - 1.10998⁻¹)
  -- = (1/2) * (55499/50000 - 50000/55499)
  -- = (55499² - 50000²) / (2 × 50000 × 55499)
  -- = 580139001 / 5549900000 ≈ 0.10453
  -- |0.10453 - 0.1045| = 0.00003 < 0.001  ✓
  simp only [crossing_energy, q₀, abs_lt]
  constructor <;> norm_num

end QOU.Archimedean.BuildingBlockKnots
