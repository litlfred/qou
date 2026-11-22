import Mathlib.Data.Real.Basic
import Mathlib.Data.List.Count
import Mathlib.Tactic


/-!
# QOU.Braiding.CrossingEnergy — Crossing energy of a knot composite

The crossing energy of a composite H with braid word β is defined as
the sum over crossings:
  E_cross(H) = Σ (positive crossings) q + Σ (negative crossings) (−q⁻¹)

where q is the substrate parameter and the sign convention follows
the Skein relation q L₊ − q⁻¹ L₋ = (q^{1/2} − q^{−1/2}) L₀.

LaTeX label: `def:crossing-energy`

## References

- [leitner2026] Ch. 4, §10
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2

**Ground ring**: this Lean sibling is the archimedean specialisation
over `ℝ` (AGENTS.md §7c): the energy uses `q⁻¹` and the half-sum
`/2`, both of which require division.  The substrate parameter
`q : ℝ` is `q ↦ q₀` under `ι : ℤ[q, q⁻¹] → ℝ`.  The combinatorial
crossing-count content is generic to any commutative ring.
-/

namespace QOU.Braiding

/-! ## Crossing Energy -/

/-- A braid word: a finite list of signed crossings.
    `true` = positive crossing (L₊), `false` = negative crossing (L₋). -/
abbrev BraidWord := List Bool

/-- Count of positive crossings in a braid word. -/
def BraidWord.numPositive (w : BraidWord) : ℕ :=
  w.filter id |>.length

/-- Count of negative crossings in a braid word. -/
def BraidWord.numNegative (w : BraidWord) : ℕ :=
  w.filter (fun b => !b) |>.length

/-- Total number of crossings in a braid word. -/
def BraidWord.numCrossings (w : BraidWord) : ℕ :=
  w.length

/-- Positive + negative = total crossings. -/
-- Ref: [leitner2026] Ch. 4, §10
theorem BraidWord.pos_plus_neg_eq_total (w : BraidWord) :
    w.numPositive + w.numNegative = w.numCrossings := by
  simp only [numPositive, numNegative, numCrossings]
  induction w with
  | nil => rfl
  | cons b t ih =>
    cases b <;> simp_all <;> omega

/-- **Crossing energy** of a knot composite with braid word β and
    substrate parameter q.

    Each positive crossing contributes `q`, each negative crossing
    `−q⁻¹`, following the Skein sign convention of `def:crossing-energy`:

      E_cross(H) = n₊ · q − n₋ · q⁻¹

    **CORRECTED 2026-08-29 (bean `qou-toul`).** This previously read
    `n₊ · q + n₋ · q⁻¹`, with a docstring stating that the `−q⁻¹` Skein
    sign "governs the L₊/L₋ skein triple, not the energy magnitude" and
    that "with `−q⁻¹` the baseline + Coulomb decomposition would not
    hold, so the energy is the additive `n₊·q + n₋·q⁻¹`".

    That is the defect, stated in its own docstring: the *definition was
    adjusted so that the theorem below would be provable*. The
    decomposition then held by `ring` — of an object the `.md` sibling
    does not define. `def:crossing-energy` says `−q⁻¹` and cites the
    Skein relation; `QOU.Braiding.crossingEnergy` in the Lake tree also
    says `−q⁻¹`. This file was the outlier.

    The decomposition does hold for the Skein sign. What changes is
    *which multiplicity goes with which channel* — see `decomposition`,
    and `prop:crossing-energy-decomposition`, which has carried the
    correct form all along:

      symmetric (strong)   ← (n₊ − n₋)   the writhe; cosh carries the sign
      antisymmetric (Coul) ← (n₊ + n₋)   the count;  sinh is sign-blind

    The two were swapped here and in `def:coulomb-charge`. -/
-- Ref: [leitner2026] Ch. 4, §10
structure CrossingEnergy where
  /-- The braid word representing the linking pattern. -/
  braidWord : BraidWord
  /-- Substrate parameter q. -/
  q : ℝ
  -- Physical constraints `0 < q` (so `q⁻¹` is well-defined) and
  -- `1 < q` (substrate constraint) are omitted: the algebraic
  -- identities below hold for all `q : ℝ`.

/-- The crossing energy value: n₊ · q − n₋ · q⁻¹ (Skein sign). -/
noncomputable def CrossingEnergy.value (E : CrossingEnergy) : ℝ :=
  E.braidWord.numPositive * E.q - E.braidWord.numNegative * E.q⁻¹

/-- Baseline (strong) contribution: ½(n₊ − n₋)(q + q⁻¹).

    The multiplicity is the **writhe** `n₊ − n₋`, not the crossing count:
    `cosh` carries the crossing sign, so reversing a crossing negates its
    symmetric part. -/
noncomputable def CrossingEnergy.baseline (E : CrossingEnergy) : ℝ :=
  ((E.braidWord.numPositive : ℝ) - E.braidWord.numNegative) * (E.q + E.q⁻¹) / 2

/-- Coulomb contribution: ½(n₊ + n₋)(q − q⁻¹).

    The multiplicity is the **crossing count** `n₊ + n₋`: `sinh` is blind
    to the crossing sign, contributing `+sinh λ` for a negative crossing
    exactly as for a positive one. -/
noncomputable def CrossingEnergy.coulombContribution (E : CrossingEnergy) : ℝ :=
  ((E.braidWord.numPositive : ℝ) + E.braidWord.numNegative) * (E.q - E.q⁻¹) / 2

/-- The crossing energy decomposes as baseline + Coulomb contribution:

      E_cross = ½(n₊ − n₋)(q + q⁻¹) + ½(n₊ + n₋)(q − q⁻¹) -/
-- Ref: [leitner2026] Ch. 4, §10
theorem CrossingEnergy.decomposition (E : CrossingEnergy) :
    E.value = E.baseline + E.coulombContribution := by
  simp only [value, baseline, coulombContribution]
  ring

/-- **The swapped assignment is not merely unproved — it is false.**

    Stated as a theorem so the defect cannot recur silently: assigning the
    crossing count to the symmetric channel and the writhe to the
    antisymmetric one reconstructs the Skein energy only when there are no
    negative crossings. The discrepancy is exactly `2·n₋·q⁻¹`. -/
theorem CrossingEnergy.swapped_decomposition_off_by (E : CrossingEnergy) :
    ((E.braidWord.numPositive : ℝ) + E.braidWord.numNegative) * (E.q + E.q⁻¹) / 2
      + ((E.braidWord.numPositive : ℝ) - E.braidWord.numNegative)
          * (E.q - E.q⁻¹) / 2
    = E.value + 2 * E.braidWord.numNegative * E.q⁻¹ := by
  simp only [value]
  ring

/-- Corollary: the swapped assignment agrees with the Skein energy exactly
    on positive braids (`n₋ = 0`), which is why the error survived — every
    canonical atomic braid the corpus evaluates is positive. -/
theorem CrossingEnergy.swapped_agrees_iff_positive_braid (E : CrossingEnergy)
    (hq : E.q ≠ 0) :
    (((E.braidWord.numPositive : ℝ) + E.braidWord.numNegative) * (E.q + E.q⁻¹) / 2
      + ((E.braidWord.numPositive : ℝ) - E.braidWord.numNegative)
          * (E.q - E.q⁻¹) / 2 = E.value)
    ↔ E.braidWord.numNegative = 0 := by
  rw [swapped_decomposition_off_by]
  constructor
  · intro h
    have h2 : 2 * (E.braidWord.numNegative : ℝ) * E.q⁻¹ = 0 := by linarith
    rcases mul_eq_zero.mp h2 with h3 | h4
    · rcases mul_eq_zero.mp h3 with h5 | h6
      · norm_num at h5
      · exact_mod_cast h6
    · exact absurd (inv_eq_zero.mp h4) hq
  · intro h; rw [h]; push_cast; ring

end QOU.Braiding
