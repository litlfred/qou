import QOU.BraidKnot.MassGapKeystone

/-!
# QOU.BraidKnot.CrossingGradedModel — S1c, the crossing-graded model tower

Implements the constructive half of **S1c strategy (iii)**
("min-energy-per-crossing counting") of the mass-gap three-step
program: the **crossing-graded model transfer matrix**, whose level-`k`
excitation carries exactly `k` crossings, each contributing the
minimum crossing energy — i.e. the additive energy accounting of
strategy (iii) taken as the *definition* of the spectrum:

  `eigenvalues k = k · E_×(q)`.

**What this module proves (all sorry-free):**

1. The model is a well-formed `CategoricalTransferMatrix`
   (`crossingGradedTM`): vacuum eigenvalue `0`, non-negative,
   monotone.
2. The model satisfies `CrossingFiltration` (`crossingGradedTM_filtration`):
   every non-vacuum excitation dominates one crossing's energy —
   **by construction**, which is exactly the point of strategy (iii).
3. The full reduction pipeline composes end-to-end: the model tower
   has a uniform `SubstrateGap` (`crossingGraded_substrateGap`), each
   level is a `YangMillsMassGap` witness (`crossingGradedYMG`), and
   the millennium-conjecture class `HasYangMillsMassGap` receives its
   first in-framework instance (`instHasYangMillsMassGapCrossingGraded`)
   — for the **model**, on the substrate window `1 < q ≤ 2`.

**What this module does NOT prove (the honest residue of S1c):**
that the *physical* brane-tower transfer matrix on `End(Aₙ)` has a
spectrum dominating the crossing-graded model.  That single
comparison — "every non-vacuum excitation of the physical `𝒯_q`
carries at least one crossing's energy" — is the entire remaining
content of S1c; it enters as the `per_crossing` field of
`CrossingFiltration` for the physical tower (the class is a one-field
constructor, so no further machinery is needed once that spectral
fact is established).  Strategies (i) (Wenzl/Jones-tower positivity
transport) and (ii) (Perron–Frobenius) of the workplan are candidate
routes to it; both are research-grade.

This module therefore converts S1c from "research-grade step" to
"research-grade *single hypothesis* plus a verified pipeline that
consumes it."
-/

namespace QOU.BraidKnot

open QOU.Torsion

/-- **The crossing-graded model transfer matrix**: the `k`-th
    excitation carries exactly `k` crossings, each contributing the
    minimum crossing energy `E_×(q)`.  Parametrized over any direct
    limit algebra and vacuum state (`vacuum_state_exists` supplies one
    for every `dla`).

    This is strategy (iii)'s additive energy accounting taken as the
    *definition* of the spectrum — a MODEL, not the physical
    `End(Aₙ)` spectrum (see module docstring). -/
noncomputable def crossingGradedTM (q : ℝ) (hq : 1 < q)
    (dla : DirectLimitAlgebra) (vac : VacuumState dla) :
    CategoricalTransferMatrix where
  dla := dla
  vacuum := vac
  eigenvalues := fun k => (k : ℝ) * minCrossingEnergy q
  vacuum_eigenvalue := by simp
  eigenvalues_nonneg := fun k =>
    mul_nonneg (Nat.cast_nonneg k) (le_of_lt (minCrossingEnergy_pos hq))
  eigenvalues_mono := fun a b hab =>
    mul_le_mul_of_nonneg_right (Nat.cast_le.mpr hab)
      (le_of_lt (minCrossingEnergy_pos hq))

/-- The model's gap value (first excited eigenvalue) is exactly one
    crossing's energy. -/
theorem crossingGradedTM_gapValue (q : ℝ) (hq : 1 < q)
    (dla : DirectLimitAlgebra) (vac : VacuumState dla) :
    (crossingGradedTM q hq dla vac).gapValue = minCrossingEnergy q := by
  simp [CategoricalTransferMatrix.gapValue, crossingGradedTM]

/-- **The model satisfies the crossing-energy filtration** — by
    construction: a non-vacuum excitation has `k ≥ 1` crossings, and
    `k · E_×(q) ≥ E_×(q)`.  This is the constructive half of S1c
    strategy (iii); the open half is the same statement for the
    physical tower. -/
theorem crossingGradedTM_filtration (q : ℝ) (hq : 1 < q)
    (dla : DirectLimitAlgebra) (vac : VacuumState dla) :
    CrossingFiltration q (fun _ => crossingGradedTM q hq dla vac) where
  per_crossing := by
    intro n k hk
    have hE := minCrossingEnergy_pos hq
    have hk0 : k ≠ 0 := by
      intro h
      apply hk
      simp [crossingGradedTM, h]
    have hk1 : (1 : ℝ) ≤ (k : ℝ) := by
      exact_mod_cast Nat.one_le_iff_ne_zero.mpr hk0
    show minCrossingEnergy q ≤ (k : ℝ) * minCrossingEnergy q
    nlinarith

/-- **The model tower carries the uniform substrate gap** on the
    substrate window `1 < q ≤ 2` — the full S1b/S1c pipeline composed:
    crossing-graded construction ⟹ `CrossingFiltration` ⟹
    `SubstrateGap`. -/
theorem crossingGraded_substrateGap (q : ℝ) (hq : 1 < q) (hq2 : q ≤ 2)
    (dla : DirectLimitAlgebra) (vac : VacuumState dla) :
    SubstrateGap q (towerSpectrum (fun _ => crossingGradedTM q hq dla vac)) :=
  have := crossingGradedTM_filtration q hq dla vac
  substrateGap_of_crossingFiltration hq hq2 _

/-- **Per-level Yang–Mills mass-gap witness for the model**: on
    `1 < q ≤ 2`, the crossing-graded model satisfies the
    `YangMillsMassGap` interface — `massGapBound q ≤ gapValue = E_×(q)`
    (since `(q−1)² ≤ 1` there) and the gap is positive.

    MODEL CAVEAT: this witnesses the *conjecture interface* for the
    crossing-graded model spectrum, not for the physical `End(Aₙ)`
    transfer matrix.  See module docstring. -/
noncomputable def crossingGradedYMG (q : ℝ) (hq : 1 < q) (hq2 : q ≤ 2)
    (dla : DirectLimitAlgebra) (vac : VacuumState dla) :
    YangMillsMassGap where
  q := q
  hq := hq
  transferMatrix := crossingGradedTM q hq dla vac
  mass_gap := by
    rw [crossingGradedTM_gapValue q hq dla vac]
    have hE0 : 0 < minCrossingEnergy q := minCrossingEnergy_pos hq
    have hsq : (q - 1) ^ 2 ≤ 1 := by nlinarith
    unfold massGapBound
    nlinarith
  gap_positive := by
    show 0 < (crossingGradedTM q hq dla vac).gapValue
    rw [crossingGradedTM_gapValue q hq dla vac]
    exact minCrossingEnergy_pos hq

/-- The millennium-conjecture class `HasYangMillsMassGap` is
    **non-vacuous in-framework**: the crossing-graded model
    instantiates it on the substrate window.  (First in-framework
    instance; MODEL caveat per the module docstring.) -/
noncomputable instance instHasYangMillsMassGapCrossingGraded
    (q : ℝ) (hq : 1 < q) (hq2 : q ≤ 2)
    (dla : DirectLimitAlgebra) (vac : VacuumState dla) :
    HasYangMillsMassGap q (crossingGradedTM q hq dla vac) where
  witness := crossingGradedYMG q hq hq2 dla vac
  q_eq := rfl
  tm_eq := rfl

end QOU.BraidKnot
