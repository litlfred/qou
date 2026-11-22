/-
  Nuclear knot classification: braid closure type determines binding scale.

  The closure of the nuclear braid 𝒩(Z,N) falls into one of four knot
  types. Each type determines the geometric invariant (Vol or CS) that
  sets the binding scale.

  Ref: [leitner2026] §5.8, conj:nuclear-knot-classification
-/

import QOU.Torsion.HeckeMassElement
import QOU.Torsion.TopologicalMass

namespace QOU.BraidKnot

/-- Classification of nuclear braid closures by knot type. -/
inductive NuclearKnotType where
  | unknot      : NuclearKnotType   -- A = 1, trivial
  | satellite   : NuclearKnotType   -- A = 2, mixed topology
  | figureEight : NuclearKnotType   -- A = 3, Vol(4₁) = 2.030
  | borromean   : NuclearKnotType   -- A ≥ 4, Vol(B₃) = 7.328
  deriving DecidableEq, Repr

/-- The binding scale α depends on the knot type through its volume.

    ⚠ **CORRECTED 2026-08-30 (bean `qou-f8lit`).** Both Borromean entries read
    `7.327724753846269`, which is **wrong from digit 11** against
    `Vol(B₃) = 8·G = 7.327724753417752120…` (abs err `4.3e-10`). Every other Lean
    carrier in the corpus — `building-block-knots.vol_borromean`,
    `categorical-neutron`, `categorical-proton` — already used `7.32772475341775`,
    so this file was the outlier, not an alternative convention.

    The corpus had already IDENTIFIED this value as bad:
    `computations/snappy_borromean_volume.py` tabulates it as "**wrong** at digit 11".
    But `docs/audits/2026-06-21-constant-consistency-axis2-clean.md` declared the axis
    CLEAN on the ground that it "survives only as a *comment* in
    `experimental_constants.py`" — while it was live here, in executable Lean, inside a
    mass formula, at two sites. That audit was evidently scoped to `computations/` and
    never looked at `content/**/*.lean`.

    Found by `scripts/known-constant-literal-audit.py`, which compares literals to
    computed constants by VALUE rather than grepping for known-bad digit strings. -/
noncomputable def bindingScale (K : NuclearKnotType) (m_e : ℝ) : ℝ :=
  match K with
  | .unknot      => 0
  | .satellite   => m_e * 7.32772475341775  -- default Borromean
  | .figureEight => m_e * 2.029883212819307  -- Vol(4₁)
  | .borromean   => m_e * 7.32772475341775  -- Vol(B₃) = 8G

/-- Classify a nuclear braid closure by mass number `A = Z + N`:
    `A ≤ 1` unknot, `A = 2` satellite, `A = 3` figure-eight, `A ≥ 4` Borromean. -/
def classifyByMassNumber (A : ℕ) : NuclearKnotType :=
  if A ≤ 1 then .unknot
  else if A = 2 then .satellite
  else if A = 3 then .figureEight
  else .borromean

/-- For `A = Z + N ≥ 4`, the nuclear braid closure is Borromean-like:
    `classifyByMassNumber (Z + N) = .borromean`.

    Derived from `hA` (the mass number selects the else-branch of
    `classifyByMassNumber`) — no longer the vacuous
    `∃ K, K = .borromean := ⟨.borromean, rfl⟩`, which held for any `A` and used
    none of its hypotheses. -/
theorem nuclear_knot_classification (Z N : ℕ) (hA : Z + N ≥ 4) :
    classifyByMassNumber (Z + N) = .borromean := by
  unfold classifyByMassNumber
  rw [if_neg (by omega : ¬ Z + N ≤ 1), if_neg (by omega : Z + N ≠ 2),
    if_neg (by omega : Z + N ≠ 3)]

end QOU.BraidKnot
