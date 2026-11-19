import QOU.StandardModel.ElectroweakBringSchwingerBridge
import QOU.BraidKnot.TorusKnotMass

/-!
# Torus-Knot Mass and All-$m$ Plancherel / Rosso–Jones Laurent Bridge

This module unifies the `TorusKnotMass` carrier (`QOU.BraidKnot.TorusKnotMass`) with the
Plancherel / Rosso–Jones trace polynomial hierarchy of `ElectroweakBringSchwingerBridge`
for arbitrary 2-strand torus links $T(2, 2m)$ ($m \in \mathbb{N}$).

Specifically:
1. **General-$m$ Doubled Plancherel Trace Polynomial `twoMulPm`**:
   Defines `twoMulPm (h : R) : ℕ → R` over any commutative ring `R` via the second-order
   Chebyshev-like recurrence:
   $$P_0^{\text{doubled}}(h) = 1, \quad P_1^{\text{doubled}}(h) = 1 + h^2, \quad
     P_{m+2}^{\text{doubled}}(h) = (h^2 + 2) P_{m+1}^{\text{doubled}}(h) - P_m^{\text{doubled}}(h).$$
2. **Exact Agreement with the $m = 0..4$ Electroweak Polynomials `twoMulP`**:
   Proves that `twoMulPm h m = QOU.StandardModel.twoMulP m h` for
   $m = 0, 1, 2, 3, 4$, and establishes the closed form at $m = 5$ ($T(2,10)$):
   `twoMulPm h 5 = 1 + 15 * h^2 + 35 * h^4 + 28 * h^6 + 9 * h^8 + h^10`.
3. **All-$m$ Rosso–Jones Laurent Identity by Induction**:
   For **every** $m \in \mathbb{N}$ and any invertible pair $q \cdot q^{-1} = 1$ in a
   commutative ring `R`, proves by two-step induction:
   $$(q + q^{-1}) \cdot \mathrm{twoMulPm}(q - q^{-1}, m) = q^{2m+1} + q^{-(2m+1)}.$$
4. **First-Difference, Positivity, Strict Monotonicity, and Unit-Interval Ratios over `ℝ`**:
   Proves the exact first-difference recurrence
   $$\mathrm{twoMulPm}(h, m+2) - \mathrm{twoMulPm}(h, m+1)
     = h^2 \cdot \mathrm{twoMulPm}(h, m+1) + (\mathrm{twoMulPm}(h, m+1) - \mathrm{twoMulPm}(h, m)),$$
   deduces that $1 \le \mathrm{twoMulPm}(h, m)$ for all $h \in \mathbb{R}$ and $m \in \mathbb{N}$,
   proves strict monotonicity $\mathrm{twoMulPm}(h, m) < \mathrm{twoMulPm}(h, m+1)$ for all
   $h \ne 0$, and concludes that every adjacent Plancherel step ratio
   $$\mathrm{plancherelStepRatio}(h, m) := \frac{\mathrm{twoMulPm}(h, m)}{\mathrm{twoMulPm}(h, m+1)}$$
   lies strictly inside the unit interval $(0, 1)$ for all $h \ne 0$.
5. **Bridge to `QOU.BraidKnot.TorusKnotMass`**:
   - Specializing `plancherelStepRatio` to $m = 2$ ($W = T(2,4)$ over $Z = T(2,6)$) proves
     that the bare Plancherel $W/Z$ ratio `plancherelWZRatio h` unconditionally satisfies the
     unit-interval obligation `0 < r ∧ r < 1` of `TorusKnotMass.WZ_mass_ratio_in_unit` for every
     non-zero Hecke parameter $h \ne 0$.
   - Connects `TorusKnotMass.poly_growth_degree` directly to the Seifert genus
     `seifertGenusTorusLink2 m = m - 1` and the Laurent exponent $2m + 1$ of $T(2, 2m)$.
-/

namespace QOU.StandardModel.TorusKnotMassPlancherelBridge

open QOU.StandardModel
open QOU.BraidKnot

-- ============================================================================
-- § 1. General-m Doubled Plancherel Trace Polynomial Recurrence
-- ============================================================================

/-- General-$m$ doubled Plancherel / Rosso–Jones trace polynomial $2 P_m(h)$ for the
2-strand torus link $T(2, 2m)$ in the Hecke difference variable $h = q - q^{-1}$,
defined for all $m \in \mathbb{N}$ by the second-order recurrence
$P_0 = 1$, $P_1 = 1 + h^2$, $P_{m+2} = (h^2 + 2) P_{m+1} - P_m$. -/
def twoMulPm {R : Type*} [CommRing R] (h : R) : ℕ → R
  | 0 => 1
  | 1 => 1 + h ^ 2
  | m + 2 => (h ^ 2 + 2) * twoMulPm h (m + 1) - twoMulPm h m

@[simp]
theorem twoMulPm_zero {R : Type*} [CommRing R] (h : R) :
    twoMulPm h 0 = 1 :=
  rfl

@[simp]
theorem twoMulPm_one {R : Type*} [CommRing R] (h : R) :
    twoMulPm h 1 = 1 + h ^ 2 :=
  rfl

theorem twoMulPm_add_two {R : Type*} [CommRing R] (h : R) (m : ℕ) :
    twoMulPm h (m + 2) = (h ^ 2 + 2) * twoMulPm h (m + 1) - twoMulPm h m :=
  rfl

/-- Closed-form polynomial expansion of `twoMulPm h 2` ($W$-boson torus link $T(2,4)$). -/
theorem twoMulPm_two {R : Type*} [CommRing R] (h : R) :
    twoMulPm h 2 = 1 + 3 * h ^ 2 + h ^ 4 := by
  change (h ^ 2 + 2) * (1 + h ^ 2) - 1 = 1 + 3 * h ^ 2 + h ^ 4
  ring

/-- Closed-form polynomial expansion of `twoMulPm h 3` ($Z$-boson torus link $T(2,6)$). -/
theorem twoMulPm_three {R : Type*} [CommRing R] (h : R) :
    twoMulPm h 3 = 1 + 6 * h ^ 2 + 5 * h ^ 4 + h ^ 6 := by
  rw [twoMulPm_add_two, twoMulPm_two, twoMulPm_one]
  ring

/-- Closed-form polynomial expansion of `twoMulPm h 4` (Higgs torus link $T(2,8)$). -/
theorem twoMulPm_four {R : Type*} [CommRing R] (h : R) :
    twoMulPm h 4 = 1 + 10 * h ^ 2 + 15 * h ^ 4 + 7 * h ^ 6 + h ^ 8 := by
  rw [twoMulPm_add_two, twoMulPm_three, twoMulPm_two]
  ring

/-- Closed-form polynomial expansion of `twoMulPm h 5` (10-crossing torus link $T(2,10)$). -/
theorem twoMulPm_five {R : Type*} [CommRing R] (h : R) :
    twoMulPm h 5 = 1 + 15 * h ^ 2 + 35 * h ^ 4 + 28 * h ^ 6 + 9 * h ^ 8 + h ^ 10 := by
  rw [twoMulPm_add_two, twoMulPm_four, twoMulPm_three]
  ring

/-- Exact agreement between `twoMulPm h m` and `QOU.StandardModel.twoMulP m h`
across the entire electroweak range $m \in \{0, 1, 2, 3, 4\}$. -/
theorem twoMulPm_eq_twoMulP_of_le_four {R : Type*} [CommRing R] (h : R) :
    twoMulPm h 0 = twoMulP 0 h ∧
    twoMulPm h 1 = twoMulP 1 h ∧
    twoMulPm h 2 = twoMulP 2 h ∧
    twoMulPm h 3 = twoMulP 3 h ∧
    twoMulPm h 4 = twoMulP 4 h := by
  refine ⟨rfl, rfl, ?_, ?_, ?_⟩
  · exact twoMulPm_two h
  · exact twoMulPm_three h
  · exact twoMulPm_four h

/-- At $h = 0$ (the classical specialization $q = 1$), `twoMulPm 0 m = 1` for all $m \in \mathbb{N}$. -/
theorem twoMulPm_at_zero {R : Type*} [CommRing R] :
    ∀ m : ℕ, twoMulPm (0 : R) m = 1
  | 0 => rfl
  | 1 => by
    change (1 : R) + 0 ^ 2 = 1
    ring
  | m + 2 => by
    rw [twoMulPm_add_two, twoMulPm_at_zero (m + 1), twoMulPm_at_zero m]
    ring

/-- Even parity of `twoMulPm`: `twoMulPm (-h) m = twoMulPm h m` for all $m \in \mathbb{N}$. -/
theorem twoMulPm_neg {R : Type*} [CommRing R] (h : R) :
    ∀ m : ℕ, twoMulPm (-h) m = twoMulPm h m
  | 0 => rfl
  | 1 => by
    dsimp [twoMulPm]
    ring
  | m + 2 => by
    rw [twoMulPm_add_two, twoMulPm_add_two, twoMulPm_neg h (m + 1), twoMulPm_neg h m]
    ring

-- ============================================================================
-- § 2. All-m Rosso–Jones Laurent Identity by Induction
-- ============================================================================

/-- Key Laurent step identity: for any $q \cdot q^{-1} = 1$ in a commutative ring `R`,
$$((q - q^{-1})^2 + 2)(q^{2m+3} + q^{-(2m+3)}) - (q^{2m+1} + q^{-(2m+1)})
  = q^{2m+5} + q^{-(2m+5)}.$$ -/
theorem laurent_chebyshev_step {R : Type*} [CommRing R] (q qi : R) (hinv : q * qi = 1) (m : ℕ) :
    ((q - qi) ^ 2 + 2) * (q ^ (2 * m + 3) + qi ^ (2 * m + 3)) -
        (q ^ (2 * m + 1) + qi ^ (2 * m + 1)) =
      q ^ (2 * m + 5) + qi ^ (2 * m + 5) := by
  have hq2 : (q - qi) ^ 2 + 2 = q ^ 2 + qi ^ 2 := by
    calc
      (q - qi) ^ 2 + 2 = q ^ 2 + qi ^ 2 - 2 * (q * qi) + 2 := by ring
      _ = q ^ 2 + qi ^ 2 - 2 * 1 + 2 := by rw [hinv]
      _ = q ^ 2 + qi ^ 2 := by ring
  have hexp3 : 2 * m + 3 = (2 * m + 1) + 2 := by omega
  have hexp5 : 2 * m + 5 = (2 * m + 1) + 4 := by omega
  rw [hq2, hexp3, hexp5, pow_add q (2 * m + 1) 2, pow_add qi (2 * m + 1) 2,
    pow_add q (2 * m + 1) 4, pow_add qi (2 * m + 1) 4]
  calc
    (q ^ 2 + qi ^ 2) * (q ^ (2 * m + 1) * q ^ 2 + qi ^ (2 * m + 1) * qi ^ 2) -
        (q ^ (2 * m + 1) + qi ^ (2 * m + 1))
      = (q ^ (2 * m + 1) * q ^ 4 + qi ^ (2 * m + 1) * qi ^ 4) +
          ((q * qi) ^ 2 - 1) * (q ^ (2 * m + 1) + qi ^ (2 * m + 1)) := by ring
    _ = (q ^ (2 * m + 1) * q ^ 4 + qi ^ (2 * m + 1) * qi ^ 4) +
          (1 ^ 2 - 1) * (q ^ (2 * m + 1) + qi ^ (2 * m + 1)) := by rw [hinv]
    _ = q ^ (2 * m + 1) * q ^ 4 + qi ^ (2 * m + 1) * qi ^ 4 := by ring

/-- **All-$m$ Rosso–Jones / Plancherel Laurent Identity**:
For **every** $m \in \mathbb{N}$ and any invertible pair $q \cdot q^{-1} = 1$ in a
commutative ring `R`,
$$(q + q^{-1}) \cdot \mathrm{twoMulPm}(q - q^{-1}, m) = q^{2m+1} + q^{-(2m+1)}.$$ -/
theorem twoMulPm_laurent {R : Type*} [CommRing R] (q qi : R) (hinv : q * qi = 1) :
    ∀ m : ℕ, (q + qi) * twoMulPm (q - qi) m = q ^ (2 * m + 1) + qi ^ (2 * m + 1)
  | 0 => by
    dsimp [twoMulPm]
    ring
  | 1 => twoMulP1_laurent q qi hinv
  | m + 2 => by
    have ih1 := twoMulPm_laurent q qi hinv (m + 1)
    have ih0 := twoMulPm_laurent q qi hinv m
    have hexp1 : 2 * (m + 1) + 1 = 2 * m + 3 := by omega
    have hexp2 : 2 * (m + 2) + 1 = 2 * m + 5 := by omega
    rw [hexp1] at ih1
    rw [hexp2, twoMulPm_add_two]
    calc
      (q + qi) * (((q - qi) ^ 2 + 2) * twoMulPm (q - qi) (m + 1) - twoMulPm (q - qi) m)
        = ((q - qi) ^ 2 + 2) * ((q + qi) * twoMulPm (q - qi) (m + 1)) -
            (q + qi) * twoMulPm (q - qi) m := by ring
      _ = ((q - qi) ^ 2 + 2) * (q ^ (2 * m + 3) + qi ^ (2 * m + 3)) -
            (q ^ (2 * m + 1) + qi ^ (2 * m + 1)) := by rw [ih1, ih0]
      _ = q ^ (2 * m + 5) + qi ^ (2 * m + 5) := laurent_chebyshev_step q qi hinv m

-- ============================================================================
-- § 3. First-Difference Recurrence, Positivity, and Strict Monotonicity on ℝ
-- ============================================================================

/-- Exact first-difference recurrence for `twoMulPm`:
$$P_{m+2}(h) - P_{m+1}(h) = h^2 P_{m+1}(h) + (P_{m+1}(h) - P_m(h)).$$ -/
theorem twoMulPm_diff_step {R : Type*} [CommRing R] (h : R) (m : ℕ) :
    twoMulPm h (m + 2) - twoMulPm h (m + 1) =
      h ^ 2 * twoMulPm h (m + 1) + (twoMulPm h (m + 1) - twoMulPm h m) := by
  rw [twoMulPm_add_two]
  ring

/-- Joint lower bound and non-decreasing step inequality over `ℝ`:
for all $h \in \mathbb{R}$ and $m \in \mathbb{N}$,
$$1 \le \mathrm{twoMulPm}(h, m) \quad \text{and} \quad
  h^2 \le \mathrm{twoMulPm}(h, m + 1) - \mathrm{twoMulPm}(h, m).$$ -/
theorem twoMulPm_ge_one_and_diff_ge_sq (h : ℝ) :
    ∀ m : ℕ, 1 ≤ twoMulPm h m ∧ h ^ 2 ≤ twoMulPm h (m + 1) - twoMulPm h m
  | 0 => by
    refine ⟨le_rfl, ?_⟩
    dsimp [twoMulPm]
    linarith
  | m + 1 => by
    obtain ⟨hm1, hdiff⟩ := twoMulPm_ge_one_and_diff_ge_sq h m
    have hsq : 0 ≤ h ^ 2 := sq_nonneg h
    have hm2 : 1 ≤ twoMulPm h (m + 1) := by linarith
    refine ⟨hm2, ?_⟩
    rw [twoMulPm_diff_step]
    have hmul : 0 ≤ h ^ 2 * twoMulPm h (m + 1) := mul_nonneg hsq (by linarith)
    linarith

/-- For every real $h \in \mathbb{R}$ and $m \in \mathbb{N}$, `1 ≤ twoMulPm h m`. -/
theorem one_le_twoMulPm (h : ℝ) (m : ℕ) : (1 : ℝ) ≤ twoMulPm h m :=
  (twoMulPm_ge_one_and_diff_ge_sq h m).1

/-- For every real $h \in \mathbb{R}$ and $m \in \mathbb{N}$, `0 < twoMulPm h m`. -/
theorem twoMulPm_pos (h : ℝ) (m : ℕ) : (0 : ℝ) < twoMulPm h m :=
  lt_of_lt_of_le zero_lt_one (one_le_twoMulPm h m)

/-- For every real $h \in \mathbb{R}$ and $m \in \mathbb{N}$,
`twoMulPm h m + h ^ 2 ≤ twoMulPm h (m + 1)`. -/
theorem twoMulPm_add_sq_le_succ (h : ℝ) (m : ℕ) :
    twoMulPm h m + h ^ 2 ≤ twoMulPm h (m + 1) := by
  have hdiff := (twoMulPm_ge_one_and_diff_ge_sq h m).2
  linarith

/-- For every non-zero Hecke difference $h \ne 0$, the Plancherel trace sequence
`m ↦ twoMulPm h m` is strictly increasing: `twoMulPm h m < twoMulPm h (m + 1)`. -/
theorem twoMulPm_lt_succ (h : ℝ) (hh : h ≠ 0) (m : ℕ) :
    twoMulPm h m < twoMulPm h (m + 1) := by
  have hpos : 0 < h ^ 2 := sq_pos_of_ne_zero hh
  have hle := twoMulPm_add_sq_le_succ h m
  linarith

/-- The sequence `m ↦ twoMulPm h m` is strictly monotone on `ℕ` whenever $h \ne 0$. -/
theorem twoMulPm_strictMono (h : ℝ) (hh : h ≠ 0) :
    StrictMono (twoMulPm h) :=
  strictMono_nat_of_lt_succ (twoMulPm_lt_succ h hh)

-- ============================================================================
-- § 4. Plancherel Step Ratios and Bridge to `QOU.BraidKnot.TorusKnotMass`
-- ============================================================================

/-- Adjacent Plancherel trace ratio for 2-strand torus links $T(2, 2m)$ over $T(2, 2(m+1))$:
$$\mathrm{plancherelStepRatio}(h, m) := \frac{P_m(h)}{P_{m+1}(h)}
  = \frac{\mathrm{twoMulPm}(h, m)}{\mathrm{twoMulPm}(h, m+1)}.$$ -/
noncomputable def plancherelStepRatio (h : ℝ) (m : ℕ) : ℝ :=
  twoMulPm h m / twoMulPm h (m + 1)

/-- For every $h \ne 0$ and every $m \in \mathbb{N}$, the adjacent Plancherel step ratio
lies strictly in the open unit interval $(0, 1)$. -/
theorem plancherelStepRatio_in_unit (h : ℝ) (hh : h ≠ 0) (m : ℕ) :
    0 < plancherelStepRatio h m ∧ plancherelStepRatio h m < 1 := by
  unfold plancherelStepRatio
  have hnum : 0 < twoMulPm h m := twoMulPm_pos h m
  have hden : 0 < twoMulPm h (m + 1) := twoMulPm_pos h (m + 1)
  have hlt : twoMulPm h m < twoMulPm h (m + 1) := twoMulPm_lt_succ h hh m
  exact ⟨div_pos hnum hden, (div_lt_one hden).mpr hlt⟩

/-- Bare Plancherel $W/Z$ trace ratio $P_2(h) / P_3(h)$ ($T(2,4)$ over $T(2,6)$). -/
noncomputable def plancherelWZRatio (h : ℝ) : ℝ :=
  plancherelStepRatio h 2

/-- Explicit rational-function form of `plancherelWZRatio h` in terms of $h^2$. -/
theorem plancherelWZRatio_eq (h : ℝ) :
    plancherelWZRatio h =
      (1 + 3 * h ^ 2 + h ^ 4) / (1 + 6 * h ^ 2 + 5 * h ^ 4 + h ^ 6) := by
  unfold plancherelWZRatio plancherelStepRatio
  rw [twoMulPm_two, twoMulPm_three]

/-- For every $h \ne 0$, the bare Plancherel $W/Z$ ratio `plancherelWZRatio h` satisfies
the unit-interval bound `0 < r ∧ r < 1` required by `TorusKnotMass.WZ_mass_ratio_in_unit`. -/
theorem plancherelWZRatio_in_unit (h : ℝ) (hh : h ≠ 0) :
    0 < plancherelWZRatio h ∧ plancherelWZRatio h < 1 :=
  plancherelStepRatio_in_unit h hh 2

/-- Bare Plancherel $H/Z$ trace ratio $P_4(h) / P_3(h)$ ($T(2,8)$ over $T(2,6)$),
which is the reciprocal of `plancherelStepRatio h 3` and therefore strictly exceeds $1$
for all $h \ne 0$. -/
noncomputable def plancherelHZRatio (h : ℝ) : ℝ :=
  twoMulPm h 4 / twoMulPm h 3

/-- Explicit rational-function form of `plancherelHZRatio h` in terms of $h^2$. -/
theorem plancherelHZRatio_eq (h : ℝ) :
    plancherelHZRatio h =
      (1 + 10 * h ^ 2 + 15 * h ^ 4 + 7 * h ^ 6 + h ^ 8) /
        (1 + 6 * h ^ 2 + 5 * h ^ 4 + h ^ 6) := by
  unfold plancherelHZRatio
  rw [twoMulPm_four, twoMulPm_three]

/-- For every $h \ne 0$, the bare Plancherel $H/Z$ ratio strictly exceeds $1$
($m_H > m_Z$ at the bare Plancherel trace level before Bring-radical dressing). -/
theorem one_lt_plancherelHZRatio (h : ℝ) (hh : h ≠ 0) :
    1 < plancherelHZRatio h := by
  unfold plancherelHZRatio
  have hden : 0 < twoMulPm h 3 := twoMulPm_pos h 3
  have hlt : twoMulPm h 3 < twoMulPm h 4 := twoMulPm_lt_succ h hh 3
  exact (one_lt_div hden).mpr hlt

/-- **Bridge Theorem to `QOU.BraidKnot.TorusKnotMass`**:
In any `[TorusKnotMass]` model, for every $m \ge 1$ (corresponding to the $2m$-crossing
2-strand torus link $T(2, 2m)$ with Seifert genus $g = m - 1$),
`TorusKnotMass.poly_growth_degree (2 * m)` equals $2 g + 1 = 2m - 1$, and adding $2$
recovers the Laurent exponent $2m + 1$ of `twoMulPm_laurent`. -/
theorem torusKnotMass_poly_growth_degree_eq_seifert_and_laurent
    [TorusKnotMass] (m : ℕ) (hm : 1 ≤ m) :
    TorusKnotMass.poly_growth_degree (2 * m) = 2 * seifertGenusTorusLink2 m + 1 ∧
    TorusKnotMass.poly_growth_degree (2 * m) + 2 = 2 * m + 1 := by
  rw [TorusKnotMass.poly_growth_degree_eq (2 * m)]
  unfold seifertGenusTorusLink2
  omega

/-- Specializing `torusKnotMass_poly_growth_degree_eq_seifert_and_laurent` to the three
electroweak torus links $W = T(2,4)$ ($m = 2$), $Z = T(2,6)$ ($m = 3$), and
$H = T(2,8)$ ($m = 4$) simultaneously relates `TorusKnotMass.poly_growth_degree`
to the Laurent exponents $5, 7, 9$ of `twoMulPm_laurent`. -/
theorem torusKnotMass_electroweak_laurent_exponents [TorusKnotMass] :
    TorusKnotMass.poly_growth_degree 4 + 2 = 2 * 2 + 1 ∧
    TorusKnotMass.poly_growth_degree 6 + 2 = 2 * 3 + 1 ∧
    TorusKnotMass.poly_growth_degree 8 + 2 = 2 * 4 + 1 := by
  refine ⟨?_, ?_, ?_⟩
  · exact (torusKnotMass_poly_growth_degree_eq_seifert_and_laurent 2 (by decide)).2
  · exact (torusKnotMass_poly_growth_degree_eq_seifert_and_laurent 3 (by decide)).2
  · exact (torusKnotMass_poly_growth_degree_eq_seifert_and_laurent 4 (by decide)).2

end QOU.StandardModel.TorusKnotMassPlancherelBridge
