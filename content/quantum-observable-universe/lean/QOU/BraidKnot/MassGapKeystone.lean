import QOU.Torsion.MassGap
-- Specific tactic imports (not the `Mathlib` umbrella): the lake-cache
-- restore omits the root `Mathlib.olean`; see
-- lean-environment-setup.md §"Two more gotchas after a lake-cache restore".
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# QOU.BraidKnot.MassGapKeystone — S1a/S1b keystone + the ε³ lemma (Step 2)

Implements the **S1a keystone**, the **Step-2 ε³ lemma**, and the
**S1b spectrum bridge** of the mass-gap three-step program
(`docs/workplans/2026-06-11-mass-gap-three-step-program.md` §1–§2, §4).

**Deduplication note (S1b revision).** The first revision of this
module re-defined `crossingEnergy` / `gapBound` and re-proved their
positivity and `q = 1` vanishing — duplicating
`QOU.Torsion.minCrossingEnergy` / `QOU.Torsion.massGapBound` and the
theorems `massGapBound_pos` / `massGapBound_at_one` already on `main`
in `QOU.Torsion.MassGap` (a corpus-grep miss). This revision deletes
the duplicates and states everything over the `QOU.Torsion`
originals; the workplan-skeleton names survive only in this comment
for provenance.

Contents (all sorry-free):

- **S1a remainder** — `massGapBound_div_hbarSq`: the exact
  physical-units identity `Δ_q/ℏ_q² = ½·q·(q−1)·(q+1)` with
  `ℏ_q = (q−1)/q` (probe-verified by `q1_mass_gap_probe.py`).
  Positivity, vanishing at `q = 1`, and monotonicity are inherited
  from `QOU.Torsion.MassGap`.

- **Step 2, the ε³ lemma** — at `q = 1 + ε` the gap has *exact*
  closed forms (no `O(·)` machinery):

  * `massGapBound (1+ε) = ε³(2+ε) / (2(1+ε))`;
  * `massGapBound (1+ε) / ℏ_q² = ε + (3/2)ε² + (1/2)ε³` (exact
    cubic — the workplan's `O(ε³)` tail pinned to exactly `ε³/2`);
  * the two-sided pinch `ε³/2 ≤ massGapBound (1+ε) ≤ ε³` for
    `0 < ε`, the quantitative form of `Δ_q = ε³(1 + O(ε))` making
    the standard-part-zero statement immediate.

- **S1b, the spectrum bridge** — pins the uniform-in-`n` gap to the
  *existing* spectral interface `QOU.Torsion.CategoricalTransferMatrix`
  (`def:categorical-transfer-matrix`), so "gap" has one meaning
  across the corpus:

  * `towerSpectrum tms n = Set.range (tms n).eigenvalues` — the
    level-`n` excitation spectrum of a brane-tower family of
    transfer matrices;
  * `SubstrateGap q spectrum` — the conditional uniform-in-`n` gap
    class (§3b-cond pattern), now stated over
    `QOU.Torsion.massGapBound`;
  * `substrateGap_of_uniform_gapValue` — if every tower level's
    `gapValue` (first excited eigenvalue) is ≥ `massGapBound q`,
    the substrate gap holds (uses `vacuum_eigenvalue` +
    `eigenvalues_mono`);
  * `CrossingFiltration` + `substrateGap_of_crossingFiltration` —
    S1c strategy (iii) "min-energy-per-crossing" reduced to a single
    named hypothesis: if every non-vacuum eigenvalue carries at least
    one crossing's energy `E_×(q)`, then for `1 < q ≤ 2` the
    substrate gap follows (since `Δ_q = E_×(q)·(q−1)² ≤ E_×(q)`
    there). What remains for S1c is *establishing* the filtration
    for the concrete tower — the research-grade step.

Relation to `QOU.AlgebraicSubstrate.SurrealRateCalculus`: the abstract
`massGap_order` rate (`massGap = ε³`, positive scalar absorbed per the
class docstring) is realised concretely with the scalar
`(2+ε)/(2(1+ε))` displayed and pinched in `[1/2, 1]`.

Per AGENTS.md §7c the ordering hypothesis `1 < q` forces the
archimedean carrier `ℝ` — no generic-`R` version exists.
-/

namespace QOU.BraidKnot

open QOU.Torsion

/-! ## S1a remainder — the exact physical-units identity -/

/-- **Exact physical-units identity**
    `Δ_q / ℏ_q² = ½·q·(q−1)·(q+1)` with `ℏ_q = (q−1)/q`.
    Probe-verified at 50 dps by `q1_mass_gap_probe.py`
    (`q1-mass-gap-probe.witness.json`, field `exact_identities`).

    Positivity (`massGapBound_pos`), vanishing at the classical point
    (`massGapBound_at_one`), and monotonicity (`massGapBound_mono`)
    live upstream in `QOU.Torsion.MassGap`. -/
-- Ref: [manuscript] q1-mass-gap-probe.witness.json exact_identities
theorem massGapBound_div_hbarSq {q : ℝ} (h0 : q ≠ 0) (h1 : q ≠ 1) :
    massGapBound q / ((q - 1) / q) ^ 2 = q * (q - 1) * (q + 1) / 2 := by
  have hq1 : q - 1 ≠ 0 := sub_ne_zero.mpr h1
  unfold massGapBound minCrossingEnergy
  field_simp
  ring

/-! ## Step 2 — the ε³ lemma (exact forms at `q = 1 + ε`) -/

/-- **ε³ lemma, categorical form (exact).** At `q = 1 + ε`:

    `Δ_{1+ε} = ε³ · (2 + ε) / (2(1 + ε))`.

    The factor `(2+ε)/(2(1+ε))` tends to `1` as `ε → 0`, so this is
    the exact form of the workplan target `Δ_q = ε³(1 + O(ε))`; the
    quantitative pinch is `massGapBound_one_add_eps_bounds` below. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §2
theorem massGapBound_one_add_eps (ε : ℝ) (hm : (1 : ℝ) + ε ≠ 0) :
    massGapBound (1 + ε) = ε ^ 3 * (2 + ε) / (2 * (1 + ε)) := by
  unfold massGapBound minCrossingEnergy
  field_simp
  ring

/-- **ε³ lemma, physical-units form (exact cubic).** At `q = 1 + ε`,
    with `ℏ_q = (q−1)/q = ε/(1+ε)`:

    `Δ_{1+ε} / ℏ_{1+ε}² = ε + (3/2)·ε² + (1/2)·ε³`.

    This is an exact polynomial — the workplan's
    `Δ_q/ℏ_q² = ε + 3⁄2·ε² + O(ε³)` with the `O(ε³)` term pinned to
    exactly `ε³/2`.  The physical-units gap dies *linearly* in `ε`;
    its standard part at the classical point is `0`. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §2
theorem massGapBound_one_add_eps_div_hbarSq (ε : ℝ) (h0 : ε ≠ 0)
    (hm : (1 : ℝ) + ε ≠ 0) :
    massGapBound (1 + ε) / ((1 + ε - 1) / (1 + ε)) ^ 2
      = ε + 3 / 2 * ε ^ 2 + ε ^ 3 / 2 := by
  have h2 : (1 : ℝ) + ε - 1 = ε := by ring
  rw [h2, massGapBound_one_add_eps ε hm]
  field_simp
  ring

/-- **Two-sided ε³ pinch**: for every `0 < ε`,

    `ε³/2 ≤ Δ_{1+ε} ≤ ε³`.

    (The lower bound uses `1 + ε ≤ 2 + ε`; the upper uses
    `2 + ε ≤ 2(1 + ε)`, i.e. `0 ≤ ε` — neither needs `ε ≤ 1`.)
    This is the quantitative content of `Δ_q = ε³(1 + O(ε))` and makes
    the standard-part-zero claim of the workplan immediate: the gap is
    squeezed between two infinitesimals of order exactly 3. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §2
theorem massGapBound_one_add_eps_bounds {ε : ℝ} (h0 : 0 < ε) :
    ε ^ 3 / 2 ≤ massGapBound (1 + ε) ∧ massGapBound (1 + ε) ≤ ε ^ 3 := by
  have hm : (1 : ℝ) + ε ≠ 0 := ne_of_gt (by linarith)
  rw [massGapBound_one_add_eps ε hm]
  have hden : (0 : ℝ) < 2 * (1 + ε) := by linarith
  constructor
  · -- lower bound: the difference is exactly ε³ / (2(1+ε)) ≥ 0
    have key : ε ^ 3 * (2 + ε) / (2 * (1 + ε)) - ε ^ 3 / 2
        = ε ^ 3 / (2 * (1 + ε)) := by
      field_simp
      ring
    have hpos : 0 ≤ ε ^ 3 / (2 * (1 + ε)) :=
      le_of_lt (div_pos (pow_pos h0 3) hden)
    linarith
  · -- upper bound: the difference is exactly ε⁴ / (2(1+ε)) ≥ 0
    have key : ε ^ 3 - ε ^ 3 * (2 + ε) / (2 * (1 + ε))
        = ε ^ 4 / (2 * (1 + ε)) := by
      field_simp
      ring
    have hpos : 0 ≤ ε ^ 4 / (2 * (1 + ε)) :=
      le_of_lt (div_pos (pow_pos h0 4) hden)
    linarith

/-! ## S1b — the spectrum bridge to `def:categorical-transfer-matrix` -/

/-- The level-indexed excitation spectrum of a brane-tower family of
    categorical transfer matrices: at level `n`, the set of
    eigenvalues of `tms n`.  This pins the `spectrum` parameter of
    `SubstrateGap` to the corpus-canonical spectral interface
    `QOU.Torsion.CategoricalTransferMatrix`
    (`def:categorical-transfer-matrix`). -/
def towerSpectrum (tms : ℕ → CategoricalTransferMatrix) : ℕ → Set ℝ :=
  fun n => Set.range (tms n).eigenvalues

/-- Uniform-in-`n` substrate gap, conditional form (§3b-cond
    conditional-class pattern), parametrized by the level-`n`
    excitation spectrum.  Downstream consumers take this class as an
    explicit `[Instance]` hypothesis per the conditional-class
    discipline; `substrateGap_of_uniform_gapValue` and
    `substrateGap_of_crossingFiltration` below provide the two
    instantiation routes. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §4
class SubstrateGap (q : ℝ) (spectrum : ℕ → Set ℝ) : Prop where
  one_lt : 1 < q
  gap_uniform : ∀ n : ℕ, ∀ E ∈ spectrum n, E ≠ 0 → massGapBound q ≤ E

/-- **S1b bridge theorem.** If every level of a brane-tower family of
    transfer matrices has its first excited eigenvalue (`gapValue`)
    bounded below by `massGapBound q` — i.e. the per-level
    `YangMillsMassGap.mass_gap` inequality holds uniformly — then the
    uniform-in-`n` substrate gap holds on the tower spectrum.

    The proof uses exactly the spectral interface of
    `def:categorical-transfer-matrix`: the vacuum eigenvalue is `0`
    (`vacuum_eigenvalue`) and eigenvalues are monotone
    (`eigenvalues_mono`), so every non-vacuum eigenvalue dominates
    `gapValue = eigenvalues 1`. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §1 S1b
theorem substrateGap_of_uniform_gapValue
    {q : ℝ} (hq : 1 < q) (tms : ℕ → CategoricalTransferMatrix)
    (huniform : ∀ n, massGapBound q ≤ (tms n).gapValue) :
    SubstrateGap q (towerSpectrum tms) where
  one_lt := hq
  gap_uniform := by
    intro n E hE hne
    obtain ⟨k, rfl⟩ := hE
    match k with
    | 0 => exact absurd (tms n).vacuum_eigenvalue hne
    | k + 1 =>
      have h1 : (tms n).eigenvalues 1 ≤ (tms n).eigenvalues (k + 1) :=
        (tms n).eigenvalues_mono (by omega)
      exact le_trans (huniform n) h1

/-- **Crossing-energy filtration** (S1c strategy (iii) as a named
    hypothesis): every non-vacuum eigenvalue of every tower level
    carries at least one crossing's worth of energy `E_×(q)`.

    This is the "min-energy-per-crossing counting" mechanism of the
    workplan — every non-trivial excitation contains ≥ 1 crossing and
    crossings contribute additively ≥ `minCrossingEnergy q`.
    Establishing this for the concrete brane tower is the
    research-grade content of S1c; here it is the named interface. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §1 S1c(iii)
class CrossingFiltration (q : ℝ) (tms : ℕ → CategoricalTransferMatrix) : Prop where
  per_crossing : ∀ n k, (tms n).eigenvalues k ≠ 0 →
    minCrossingEnergy q ≤ (tms n).eigenvalues k

/-- **S1c-(iii) reduction.** In the substrate window `1 < q ≤ 2`
    (which contains the physical `q₀ ≈ 1.11`), the crossing-energy
    filtration implies the uniform substrate gap: there
    `(q − 1)² ≤ 1`, so `Δ_q = E_×(q)·(q−1)² ≤ E_×(q)`, and any
    eigenvalue dominating one crossing's energy dominates the gap
    bound.

    This reduces S1c to establishing `CrossingFiltration` for the
    concrete tower — a single named hypothesis replacing the informal
    "min-energy-per-crossing" argument. -/
-- Ref: [manuscript] docs/workplans/2026-06-11-mass-gap-three-step-program.md §1 S1c(iii)
theorem substrateGap_of_crossingFiltration
    {q : ℝ} (hq : 1 < q) (hq2 : q ≤ 2)
    (tms : ℕ → CategoricalTransferMatrix) [cf : CrossingFiltration q tms] :
    SubstrateGap q (towerSpectrum tms) where
  one_lt := hq
  gap_uniform := by
    intro n E hE hne
    obtain ⟨k, rfl⟩ := hE
    have hcf := cf.per_crossing n k hne
    have hE0 : 0 < minCrossingEnergy q := minCrossingEnergy_pos hq
    -- In the window 1 < q ≤ 2 we have (q − 1)² ≤ 1, hence
    -- Δ_q = E_×(q)·(q−1)² ≤ E_×(q).
    have hsq : (q - 1) ^ 2 ≤ 1 := by nlinarith
    have hbound : massGapBound q ≤ minCrossingEnergy q := by
      unfold massGapBound
      nlinarith
    linarith

end QOU.BraidKnot
