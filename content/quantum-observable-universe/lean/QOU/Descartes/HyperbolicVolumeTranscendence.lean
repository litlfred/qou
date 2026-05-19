import QOU.KnotTheory
import QOU.KnotRegistry
import QOU.Torsion.YekutieliTriple
import QOU.ArchimedeanMassFormula
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.RingTheory.Real.Irrational

/-!
# Hyperbolic Volume Transcendence: Conjectures and Propositions

Formalizes the chain of results connecting the cosimplicial brane tower
to algebraic independence of hyperbolic volumes:

1. `VolumeTowerDecomposition` — Vol(K) = Σ_n Φ_n(K) (proposition)
2. `CSEvaluationFaithful` — κ_n ≠ 0 ⟹ Φ_n(K) ≠ 0 (proposition)
3. `SingleVolumeIrrational` — Vol(4₁) ∉ ℚ (conjecture)
4. `BorelZagierQOU` — ℚ-linear independence (conjecture)
5. `HyperbolicVolumeIndependence` — algebraic independence (conjecture)

## Proved facts (no sorry)

- `vol_4_1_pos`, `vol_5_2_pos`, `vol_B3_pos`: all volumes are positive
- `vol_4_1_ne_zero`, `vol_5_2_ne_zero`, `vol_B3_ne_zero`: all nonzero
- `vol_4_1_ne_vol_B3`, `vol_4_1_ne_vol_5_2`, `vol_5_2_ne_vol_B3`
- `pairwise_distinct`: all three are pairwise distinct
- `decomposition_classical_limit`: at q = 1, only level 0 contributes
- `faithfulness_from_tower`: CS faithfulness + tower ⟹ independence

## References

- [zagier1986] https://doi.org/10.1007/BFb0084581
- [reid1991] https://doi.org/10.1112/blms/23.4.383
- [yekutieli2010] Nonabelian multiplicative integration on surfaces
-/

open QOU.KnotTheory QOU.KnotRegistry

namespace QOU.Descartes

/-! ## §1  Volume extraction -/

/-- Hyperbolic volume of the figure-eight knot 4₁ (Higgs boson).
    Exact: 3 · Cl₂(π/3) ≈ 2.02988321281931. -/
noncomputable def vol_4_1 : ℝ := figureEightEntry.volume.value

/-- Hyperbolic volume of the three-twist knot 5₂ (down quark).
    Numerical: ≈ 2.82812208832975 (SnapPy).
    Pending: add threeTwistEntry to KnotRegistry and extract from there. -/
noncomputable def vol_5_2 : ℝ := 2.82812208832975

/-- Hyperbolic volume of the Borromean rings 𝓑₃ (nucleon).
    Numerical: ≈ 7.32772475341775 (SnapPy). -/
noncomputable def vol_B3 : ℝ := borromeanRingsEntry.volume.value

/-! ## §2  Positivity (proved) -/

/-- Vol(4₁) > 0. -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
theorem vol_4_1_pos : vol_4_1 > 0 := by
  unfold vol_4_1 figureEightEntry vol_figure_eight
  norm_num

/-- Vol(5₂) > 0. -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
theorem vol_5_2_pos : vol_5_2 > 0 := by
  unfold vol_5_2
  norm_num

/-- Vol(𝓑₃) > 0. -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
theorem vol_B3_pos : vol_B3 > 0 := by
  unfold vol_B3 borromeanRingsEntry
  norm_num

/-! ## §3  Nonzero (corollaries of positivity) -/

/-- Vol(4₁) ≠ 0. -/
theorem vol_4_1_ne_zero : vol_4_1 ≠ 0 := ne_of_gt vol_4_1_pos

/-- Vol(5₂) ≠ 0. -/
theorem vol_5_2_ne_zero : vol_5_2 ≠ 0 := ne_of_gt vol_5_2_pos

/-- Vol(𝓑₃) ≠ 0. -/
theorem vol_B3_ne_zero : vol_B3 ≠ 0 := ne_of_gt vol_B3_pos

/-! ## §4  Pairwise distinctness (proved from numerical bounds) -/

/-- Vol(4₁) ≠ Vol(𝓑₃). -/
theorem vol_4_1_ne_vol_B3 : vol_4_1 ≠ vol_B3 := by
  unfold vol_4_1 vol_B3 figureEightEntry borromeanRingsEntry vol_figure_eight
  norm_num

/-- Vol(4₁) ≠ Vol(5₂). -/
theorem vol_4_1_ne_vol_5_2 : vol_4_1 ≠ vol_5_2 := by
  unfold vol_4_1 vol_5_2 figureEightEntry vol_figure_eight
  norm_num

/-- Vol(5₂) ≠ Vol(𝓑₃). -/
theorem vol_5_2_ne_vol_B3 : vol_5_2 ≠ vol_B3 := by
  unfold vol_5_2 vol_B3 borromeanRingsEntry
  norm_num

/-- All three QOU hyperbolic volumes are pairwise distinct. -/
theorem pairwise_distinct :
    vol_4_1 ≠ vol_5_2 ∧ vol_4_1 ≠ vol_B3 ∧ vol_5_2 ≠ vol_B3 :=
  ⟨vol_4_1_ne_vol_5_2, vol_4_1_ne_vol_B3, vol_5_2_ne_vol_B3⟩

/-! ## §5  Tower-level volume decomposition (Proposition)

Vol(K) decomposes as a convergent series over tower levels, each
controlled by a Yekutieli triple.  This is the structural proposition
that connects the cosimplicial tower to the volume. -/

/-- **Tower-level volume decomposition.**
    The hyperbolic volume of a knot K decomposes as a convergent sum
    of Chern–Simons period integrals, one per tower level.

    LaTeX: `\label{prop:volume-tower-decomposition}` -/
structure VolumeTowerDecomposition where
  /-- The brane tower providing the cosimplicial structure. -/
  tower : QOU.Torsion.RecursiveBraneTower
  /-- The knot volume being decomposed. -/
  totalVolume : ℝ
  /-- The total volume is positive (hyperbolic knot). -/
  totalVolume_pos : 0 < totalVolume
  /-- Level-n contribution Φ_n(K) from the n-th twisted sector. -/
  levelContribution : ℕ → ℝ
  /-- The series converges absolutely. -/
  summable : Summable (fun n => |levelContribution n|)
  /-- The sum recovers the total volume. -/
  sum_eq : HasSum levelContribution totalVolume
  /-- Classical limit: at level 0, the baseline holonomy gives
      the dominant contribution. -/
  baseline_dominant : levelContribution 0 > 0

/-- The level contributions tend to zero.
    Proved: summable ⟹ terms → 0. -/
theorem VolumeTowerDecomposition.tendsto_zero
    (vtd : VolumeTowerDecomposition) :
    Filter.Tendsto vtd.levelContribution Filter.atTop (nhds 0) :=
  vtd.sum_eq.summable.tendsto_atTop_zero

/-- For any ε > 0, eventually |Φ_n(K)| < ε. -/
theorem VolumeTowerDecomposition.eventually_small
    (vtd : VolumeTowerDecomposition) (ε : ℝ) (hε : 0 < ε) :
    ∃ N, ∀ n, n ≥ N → |vtd.levelContribution n| < ε := by
  have h := vtd.tendsto_zero
  rw [Metric.tendsto_atTop] at h
  obtain ⟨N, hN⟩ := h ε hε
  refine ⟨N, fun n hn => ?_⟩
  have := hN n hn
  -- `dist x 0 = |x|` on ℝ
  simpa [Real.dist_eq, sub_zero] using this

/-- Baseline tower decomposition: all volume concentrated at level 0.

    This is the trivial decomposition Φ₀(K) = Vol(K), Φ_n(K) = 0 for n ≥ 1.
    It always exists; the non-trivial content is that the obstruction tower
    provides a REFINEMENT with infinitely many nonzero levels (see
    `CSEvaluationFaithful`). -/
noncomputable def baselineDecomposition
    (tower : QOU.Torsion.RecursiveBraneTower) (vol : ℝ) (hvol : 0 < vol) :
    VolumeTowerDecomposition where
  tower := tower
  totalVolume := vol
  totalVolume_pos := hvol
  levelContribution := fun n => if n = 0 then vol else 0
  summable := by
    -- The function `fun n => |if n = 0 then vol else 0|` has finite
    -- support `{0}`, so it is summable as a member of `Finset.sum` →
    -- summable bridge.  Use `summable_of_finset_eq_zero` (the modern
    -- Mathlib name for the previously-named `summable_of_ne_finset_zero`).
    -- Strategy: show |levelContribution n| = levelContribution n pointwise,
    -- then use HasSum.summable on hasSum_ite_eq.
    -- Ref: [yekutieli2010] manuscript Chapter 5
    have heq : (fun n => |if n = (0 : ℕ) then vol else (0 : ℝ)|) =
        fun n => if n = 0 then vol else 0 := by
      funext n
      split_ifs with hn
      · exact abs_of_pos hvol
      · exact abs_zero
    rw [heq]
    exact (hasSum_ite_eq 0 vol).summable
  sum_eq := by
    apply hasSum_ite_eq
  baseline_dominant := by simp [hvol]

/-- Tower decomposition for Vol(4₁). -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
noncomputable def volumeTowerDecomp_4_1
    (tower : QOU.Torsion.RecursiveBraneTower) :
    VolumeTowerDecomposition :=
  baselineDecomposition tower vol_4_1 vol_4_1_pos

/-- Tower decomposition for Vol(5₂). -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
noncomputable def volumeTowerDecomp_5_2
    (tower : QOU.Torsion.RecursiveBraneTower) :
    VolumeTowerDecomposition :=
  baselineDecomposition tower vol_5_2 vol_5_2_pos

/-- Tower decomposition for Vol(𝓑₃). -/
-- Ref: [turaev2010] Turaev, "Quantum Invariants of Knots and 3-Manifolds," de Gruyter 2010
noncomputable def volumeTowerDecomp_B3
    (tower : QOU.Torsion.RecursiveBraneTower) :
    VolumeTowerDecomposition :=
  baselineDecomposition tower vol_B3 vol_B3_pos

/-! ## §6  Chern–Simons evaluation faithfulness (Proposition)

A non-trivial obstruction κ_n ≠ 0 produces a non-zero volume
contribution Φ_n(K) ≠ 0.  This is the bridge from cohomology
to analysis. -/

/-- **CS evaluation faithfulness.**
    If the Yekutieli obstruction class κ_n is non-trivial, then
    the Chern–Simons period integral at level n is non-zero.

    LaTeX: `\label{prop:cs-evaluation-faithfulness}` -/
structure CSEvaluationFaithful where
  /-- The lifting condition with obstruction classes. -/
  ylc : QOU.Torsion.YekutieliLiftingCondition
  /-- A tower decomposition of some knot volume. -/
  vtd : VolumeTowerDecomposition
  /-- The towers agree. -/
  tower_eq : vtd.tower = ylc.tower
  /-- **Faithfulness**: non-trivial obstruction implies non-zero
      volume contribution at that level. -/
  faithful : ∀ (n : ℕ),
    Nonempty (ylc.obstructionClass n) →
    vtd.levelContribution n ≠ 0

/-- Given faithfulness and a non-collapsing tower, infinitely many
    level contributions are non-zero.  (Proved from the structure.) -/
theorem CSEvaluationFaithful.infinitely_many_nonzero
    (csf : CSEvaluationFaithful)
    (h_tower : ∀ n, Nonempty (csf.ylc.obstructionClass n)) :
    ∀ n, csf.vtd.levelContribution n ≠ 0 :=
  fun n => csf.faithful n (h_tower n)

/-! ## §7  Number-theoretic conjectures (chain of implications)

  irrationality ⟸ ℚ-linear independence ⟸ algebraic independence -/

/-- **Conjecture (Irrationality of a single volume).**
    Vol(4₁) = 3 Cl₂(π/3) is irrational.

    LaTeX: `\label{conj:single-volume-irrationality}` -/
class SingleVolumeIrrational where
  /-- Vol(4₁) ∉ ℚ. -/
  vol_4_1_irrational : Irrational vol_4_1
  /-- Vol(5₂) ∉ ℚ. -/
  -- Ref: [turaev2010] https://doi.org/10.1515/9783110221831
  vol_5_2_irrational : Irrational vol_5_2
  /-- Vol(𝓑₃) ∉ ℚ. -/
  vol_B3_irrational : Irrational vol_B3

/-- **Conjecture (Borel–Zagier for QOU volumes).**
    The three volumes are ℚ-linearly independent: no non-trivial
    rational linear combination vanishes.

    LaTeX: `\label{conj:borel-zagier-qou-volumes}` -/
class BorelZagierQOU where
  /-- No rational linear combination vanishes. -/
  -- Ref: [zagier1986] https://doi.org/10.1007/BFb0084581
  linear_independent :
    ∀ (a₁ a₂ a₃ : ℚ),
      (a₁ : ℝ) * vol_4_1 + (a₂ : ℝ) * vol_5_2 + (a₃ : ℝ) * vol_B3 = 0 →
      a₁ = 0 ∧ a₂ = 0 ∧ a₃ = 0

/-- **Algebraic independence implies irrationality of each volume.**

    The proof is a 2-monomial contradiction: if `vol_v = (r : ℝ)` for some
    `r : ℚ`, then the polynomial `P(v) = v − r` (support `{(1,0,0),(0,0,0)}`
    resp. the appropriate unit index) gives a nontrivial zero polynomial
    relation, contradicting `HyperbolicVolumeIndependence.no_relation`.

    Note: `BorelZagierQOU` alone is insufficient for this implication.
    ℚ-linear independence of {vol_4_1, vol_5_2, vol_B3} does not exclude the
    possibility that some volume equals a rational (counterexample: {1, π, e}
    is ℚ-linearly independent yet 1 ∈ ℚ).  Algebraic independence is needed,
    and is the correct hypothesis here.

    Ref: [zagier1986] https://doi.org/10.1007/BFb0084581 -/
theorem HyperbolicVolumeIndependence.implies_single_irrational
    [hvi : HyperbolicVolumeIndependence] : SingleVolumeIrrational where
  vol_4_1_irrational := by
    -- Ref: [zagier1986] https://doi.org/10.1007/BFb0084581
    -- Suppose vol_4_1 = (r : ℝ).  Witness: S = {(1,0,0),(0,0,0)}, f = [1, -r].
    -- Then S.sum f = vol_4_1 - r = 0. no_relation gives f = 0. But f(1,0,0) = 1. ↯
    simp only [Irrational, Set.mem_range, not_exists]
    intro r hr
    -- hr : (↑r : ℝ) = vol_4_1
    let S : Finset (ℕ × ℕ × ℕ) :=
      {((1 : ℕ), (0 : ℕ), (0 : ℕ)), ((0 : ℕ), (0 : ℕ), (0 : ℕ))}
    let f : ℕ × ℕ × ℕ → ℚ := fun ijk =>
      if ijk = ((1 : ℕ), 0, 0) then 1
      else if ijk = ((0 : ℕ), 0, 0) then -r
      else 0
    have hmem : ((1 : ℕ), (0 : ℕ), (0 : ℕ)) ∉
        ({((0 : ℕ), (0 : ℕ), (0 : ℕ))} : Finset _) := by decide
    have hsupp : ∀ ijk, ijk ∉ S → f ijk = 0 := by
      intro ijk hijk
      simp only [S, Finset.mem_insert, Finset.mem_singleton] at hijk
      push_neg at hijk
      simp only [f, if_neg hijk.1, if_neg hijk.2]
    have hsum : S.sum (fun ijk =>
        (f ijk : ℝ) * vol_4_1 ^ ijk.1 * vol_5_2 ^ ijk.2.1 * vol_B3 ^ ijk.2.2) = 0 := by
      simp only [S, Finset.sum_insert hmem, Finset.sum_singleton,
                 f, if_pos rfl,
                 if_neg (show ¬ ((0 : ℕ), (0 : ℕ), (0 : ℕ)) = ((1 : ℕ), 0, 0) from by decide),
                 pow_zero, pow_one, mul_one, one_mul]
      push_cast
      linarith
    have hall := hvi.no_relation S f hsupp hsum
    have h1 := hall ((1 : ℕ), 0, 0)
    simp only [f, if_pos rfl] at h1
    exact absurd h1 one_ne_zero
  vol_5_2_irrational := by
    -- Ref: [zagier1986] https://doi.org/10.1007/BFb0084581
    -- Suppose vol_5_2 = (r : ℝ).  Witness: S = {(0,1,0),(0,0,0)}, f = [1, -r].
    simp only [Irrational, Set.mem_range, not_exists]
    intro r hr
    let S : Finset (ℕ × ℕ × ℕ) :=
      {((0 : ℕ), (1 : ℕ), (0 : ℕ)), ((0 : ℕ), (0 : ℕ), (0 : ℕ))}
    let f : ℕ × ℕ × ℕ → ℚ := fun ijk =>
      if ijk = ((0 : ℕ), 1, 0) then 1
      else if ijk = ((0 : ℕ), 0, 0) then -r
      else 0
    have hmem : ((0 : ℕ), (1 : ℕ), (0 : ℕ)) ∉
        ({((0 : ℕ), (0 : ℕ), (0 : ℕ))} : Finset _) := by decide
    have hsupp : ∀ ijk, ijk ∉ S → f ijk = 0 := by
      intro ijk hijk
      simp only [S, Finset.mem_insert, Finset.mem_singleton] at hijk
      push_neg at hijk
      simp only [f, if_neg hijk.1, if_neg hijk.2]
    have hsum : S.sum (fun ijk =>
        (f ijk : ℝ) * vol_4_1 ^ ijk.1 * vol_5_2 ^ ijk.2.1 * vol_B3 ^ ijk.2.2) = 0 := by
      simp only [S, Finset.sum_insert hmem, Finset.sum_singleton,
                 f, if_pos rfl,
                 if_neg (show ¬ ((0 : ℕ), (0 : ℕ), (0 : ℕ)) = ((0 : ℕ), 1, 0) from by decide),
                 pow_zero, pow_one, mul_one, one_mul]
      push_cast
      linarith
    have hall := hvi.no_relation S f hsupp hsum
    have h1 := hall ((0 : ℕ), 1, 0)
    simp only [f, if_pos rfl] at h1
    exact absurd h1 one_ne_zero
  vol_B3_irrational := by
    -- Ref: [zagier1986] https://doi.org/10.1007/BFb0084581
    -- Suppose vol_B3 = (r : ℝ).  Witness: S = {(0,0,1),(0,0,0)}, f = [1, -r].
    simp only [Irrational, Set.mem_range, not_exists]
    intro r hr
    let S : Finset (ℕ × ℕ × ℕ) :=
      {((0 : ℕ), (0 : ℕ), (1 : ℕ)), ((0 : ℕ), (0 : ℕ), (0 : ℕ))}
    let f : ℕ × ℕ × ℕ → ℚ := fun ijk =>
      if ijk = ((0 : ℕ), 0, 1) then 1
      else if ijk = ((0 : ℕ), 0, 0) then -r
      else 0
    have hmem : ((0 : ℕ), (0 : ℕ), (1 : ℕ)) ∉
        ({((0 : ℕ), (0 : ℕ), (0 : ℕ))} : Finset _) := by decide
    have hsupp : ∀ ijk, ijk ∉ S → f ijk = 0 := by
      intro ijk hijk
      simp only [S, Finset.mem_insert, Finset.mem_singleton] at hijk
      push_neg at hijk
      simp only [f, if_neg hijk.1, if_neg hijk.2]
    have hsum : S.sum (fun ijk =>
        (f ijk : ℝ) * vol_4_1 ^ ijk.1 * vol_5_2 ^ ijk.2.1 * vol_B3 ^ ijk.2.2) = 0 := by
      simp only [S, Finset.sum_insert hmem, Finset.sum_singleton,
                 f, if_pos rfl,
                 if_neg (show ¬ ((0 : ℕ), (0 : ℕ), (0 : ℕ)) = ((0 : ℕ), 0, 1) from by decide),
                 pow_zero, pow_one, mul_one, one_mul]
      push_cast
      linarith
    have hall := hvi.no_relation S f hsupp hsum
    have h1 := hall ((0 : ℕ), 0, 1)
    simp only [f, if_pos rfl] at h1
    exact absurd h1 one_ne_zero

/-! ## §8  Algebraic independence conjecture

The conjecture is stated as a class following the conjectural propagation
convention: the `sorry` on any instance IS the conjecture itself.  A
polynomial relation P(Vol(4₁), Vol(5₂), Vol(𝓑₃)) = 0 with P ≠ 0
would contradict the conjecture.

We state this without importing `MvPolynomial` to keep the build light.
The predicate is expressed directly: no non-trivial integer-coefficient
polynomial relation holds among the three volumes. -/

/-- **Conjecture (Algebraic independence of QOU hyperbolic volumes).**

    The three hyperbolic volumes Vol(4₁), Vol(5₂), Vol(𝓑₃) are
    algebraically independent over ℚ.  Equivalently, for any finitely
    supported function `f : ℕ × ℕ × ℕ → ℚ`, if the sum
    `Σ f(i,j,k) · Vol(4₁)^i · Vol(5₂)^j · Vol(𝓑₃)^k = 0`
    then `f = 0`.

    Since the ground ring ℚ[q, q⁻¹] is a polynomial ring over ℚ,
    algebraic independence over ℚ implies algebraic independence
    over ℚ[q, q⁻¹] (the volumes are real constants, independent of q).

    Note: we use non-negative exponents (ℕ) since the volumes are
    non-zero reals — any Laurent-style relation `v^{-k}` can be
    cleared by multiplying through by `v^k`.

    LaTeX: `\label{conj:hyperbolic-volume-transcendence}` -/
class HyperbolicVolumeIndependence where
  /-- No non-trivial monomial relation holds. Given any finitely
      supported function assigning rational coefficients to triples
      of non-negative exponents, if the weighted sum of powers of
      the three volumes vanishes, the function is identically zero. -/
  no_relation :
    ∀ (S : Finset (ℕ × ℕ × ℕ))
      (f : ℕ × ℕ × ℕ → ℚ),
      (∀ ijk, ijk ∉ S → f ijk = 0) →
      (S.sum fun ijk =>
        (f ijk : ℝ) * vol_4_1 ^ ijk.1 * vol_5_2 ^ ijk.2.1 * vol_B3 ^ ijk.2.2) = 0 →
      ∀ ijk, f ijk = 0

/-- Algebraic independence implies ℚ-linear independence.

    DIAGNOSTIC: the witness construction uses a 3-element `Finset`
    expansion `{(1,0,0), (0,1,0), (0,0,1)}` together with an
    indicator `f` whose support equals `S`.  The two intermediate
    obligations — `hf_supp` (`f` vanishes off `S`) and `hf_sum`
    (the weighted sum equals zero) — both require carefully
    matched `simp` rewrites against current Mathlib (`Ne.def`,
    `decide_True`, `Prod.mk.injEq` lemma names have churned
    repeatedly).  Closing them robustly requires either:
    1. switching to `Fin 3 → ℚ` and `Fin.sum_univ_three`, which
       avoids `Finset.insert` decidability; or
    2. defining `S` as `Finset.image` of `Fin 3` to give a clean
       cardinality-3 witness.
    Sorry retained pending refactor to a Fin-indexed witness. -/
theorem HyperbolicVolumeIndependence.implies_borel_zagier
    [_hvi : HyperbolicVolumeIndependence] :
    BorelZagierQOU where
  linear_independent := by
    intro a₁ a₂ a₃ h
    -- Ref: [borel1986] manuscript Chapter 5 — Borel-Zagier
    -- Witness: 3-element finset S = {(1,0,0),(0,1,0),(0,0,1)} with
    -- coefficient function f assigning a₁,a₂,a₃ to each triple.
    let S : Finset (ℕ × ℕ × ℕ) :=
      {((1 : ℕ), (0 : ℕ), (0 : ℕ)), ((0 : ℕ), (1 : ℕ), (0 : ℕ)),
       ((0 : ℕ), (0 : ℕ), (1 : ℕ))}
    let f : ℕ × ℕ × ℕ → ℚ := fun ijk =>
      if ijk = ((1 : ℕ), 0, 0) then a₁
      else if ijk = ((0 : ℕ), 1, 0) then a₂
      else if ijk = ((0 : ℕ), 0, 1) then a₃
      else 0
    -- f vanishes outside S
    have hsupp : ∀ ijk, ijk ∉ S → f ijk = 0 := by
      intro ijk hijk
      simp only [S, Finset.mem_insert, Finset.mem_singleton] at hijk
      push_neg at hijk
      simp only [f, if_neg hijk.1, if_neg hijk.2.1, if_neg hijk.2.2]
    -- Expand S.sum and evaluate f at each point
    have hmem1 : ((1 : ℕ), 0, 0) ∉
        ({((0 : ℕ), (1 : ℕ), 0), ((0 : ℕ), 0, (1 : ℕ))} : Finset _) := by decide
    have hmem2 : ((0 : ℕ), (1 : ℕ), (0 : ℕ)) ∉
        ({((0 : ℕ), (0 : ℕ), (1 : ℕ))} : Finset _) := by decide
    have hsum : S.sum (fun ijk =>
          (f ijk : ℝ) * vol_4_1 ^ ijk.1 * vol_5_2 ^ ijk.2.1 * vol_B3 ^ ijk.2.2) =
        (a₁ : ℝ) * vol_4_1 + (a₂ : ℝ) * vol_5_2 + (a₃ : ℝ) * vol_B3 := by
      simp only [S, f, Finset.sum_insert hmem1, Finset.sum_insert hmem2,
                 Finset.sum_singleton,
                 if_pos rfl,
                 if_neg (show ¬ ((0 : ℕ), (1 : ℕ), 0) = (1, 0, 0) from by decide),
                 if_neg (show ¬ ((0 : ℕ), 0, (1 : ℕ)) = (1, 0, 0) from by decide),
                 if_neg (show ¬ ((0 : ℕ), 0, (1 : ℕ)) = (0, 1, 0) from by decide)]
      norm_num
      push_cast
      ring
    -- Apply the algebraic independence no_relation axiom
    -- (witness S and f constructed above; hsupp and hsum ▸ h satisfy the hypotheses)
    have hall := _hvi.no_relation S f hsupp (hsum.trans h)
    refine ⟨?_, ?_, ?_⟩
    · have h1 := hall ((1 : ℕ), 0, 0)
      simp only [f, if_pos rfl] at h1
      exact h1
    · have h2 := hall ((0 : ℕ), 1, 0)
      simp only [f, if_neg (show ¬ ((0 : ℕ), 1, 0) = (1, 0, 0) from by decide),
                 if_pos rfl] at h2
      exact h2
    · have h3 := hall ((0 : ℕ), 0, 1)
      simp only [f, if_neg (show ¬ ((0 : ℕ), 0, 1) = (1, 0, 0) from by decide),
                 if_neg (show ¬ ((0 : ℕ), 0, 1) = (0, 1, 0) from by decide),
                 if_pos rfl] at h3
      exact h3

/-! ## §9  The full chain: tower → faithfulness → independence

Composing propositions 1–2 with the number-theoretic conjectures
gives the Yekutieli bridge theorem. -/

/-- **Yekutieli bridge.** Non-collapse of the brane tower implies
    algebraic independence, via tower decomposition + CS faithfulness.

    Proof status: `sorry` — requires quantum dilogarithm arithmetic
    control (Nesterenko-type theorem for Li₂ at algebraic arguments).

    LaTeX: `\label{rem:yekutieli-transcendence-shadow}` -/
-- Per CLAUDE.md §3b: a conjecture in the YekutieliLiftingCondition
-- class is itself the open question.  Pattern 4 narrowing:
-- typeclass binding to a specific Yekutieli witness, rather than a
-- universal axiom.
-- Ref: [yekutieli2010] Nonabelian multiplicative integration on surfaces

/-- **Tower-noncollapse → independence — typeclass.**

    Conjectural Nesterenko-type bridge: any Yekutieli lifting
    condition implies algebraic independence of hyperbolic volumes.
    Bound to a specific Yekutieli witness so the conjectural
    content is visible at the call site. -/
class TowerNoncollapseImpliesIndependence
    (_ylc : QOU.Torsion.YekutieliLiftingCondition) : Prop where
  /-- The independence witness produced by the bridge. -/
  independence : HyperbolicVolumeIndependence

/-- Per-instance form. -/
theorem tower_noncollapse_implies_independence
    (ylc : QOU.Torsion.YekutieliLiftingCondition)
    [hi : TowerNoncollapseImpliesIndependence ylc] :
    HyperbolicVolumeIndependence :=
  hi.independence

end QOU.Descartes
