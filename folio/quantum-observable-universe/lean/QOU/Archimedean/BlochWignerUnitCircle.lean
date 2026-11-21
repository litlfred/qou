/-
  # `BlochWigner_unit_circle` — canonical Lake-tree declaration

  Moves the `BlochWigner_unit_circle : ℝ → ℝ` signature from the
  `axiom` declaration that lived inside
  `folio/quantum-observable-universe/predicted-spectra/em-coupling-bring-zero-mode.lean`
  (merged #1460 Phase 1) into the canonical Lake-built module tree
  under `QOU.Archimedean`.

  **Phase-1 wire-up partial (this commit).**  The function signature
  is now resolvable at its documented namespace
  `QOU.Archimedean.BlochWigner_unit_circle` for any consumer inside
  the `qou` Lake library.  Downstream consumers that live in the
  Lake tree — e.g. future migrations of
  `BringZeroModeBlochClass.bring_zero_mode_realised` and the
  `bring_zero_mode_additive_form` theorem — pick this up via `import
  QOU.Archimedean.BlochWignerUnitCircle`.

  **Note on content-block siblings.**  The current consumer at
  `folio/quantum-observable-universe/predicted-spectra/em-coupling-bring-zero-mode.lean`
  is a content-block sibling (lives **outside** the `qou` Lake
  library `srcDir`), so it cannot `import` Lake modules directly
  and continues to use its inline `axiom BlochWigner_unit_circle`.
  Switching that consumer to the Lake-tree declaration requires a
  prior refactor that migrates the content-block sibling into the
  Lake tree — tracked as a separate follow-up.

  **Phase-3 closure (completed, bean `qou-tc8y`).**  `BlochWigner_unit_circle`
  carries its concrete Clausen-function body `Cl_2 θ` (from
  `ClausenFunctionMathlibFiller.lean`), and `BlochWignerMathlibFiller.lean`
  imports this module instead of redeclaring a duplicate `BlochWigner_unit_circle`
  in `namespace QOU.Archimedean`.

  Ref: [leitner2026] prop:em-coupling-bring-zero-mode
  Ref: [leitner2026] prop:archimedean-functor-uniqueness
  Ref: filler at content/.../predicted-spectra/bloch-wigner-mathlib-filler.lean
  Ref: [suslin1991], [bloch2000] for the Bloch-Suslin K-theory framework
-/
import QOU.Archimedean.ClausenFunctionMathlibFiller

namespace QOU.Archimedean

/-- The Bloch-Wigner dilogarithm on the unit circle:
    `D(e^{iθ}) = Cl_2 θ`, where `Cl_2` is the Clausen function
    (`ClausenFunctionMathlibFiller.lean`).

    **2026-11-15 (owner decision, issue #7942):** this was a
    `noncomputable opaque` with no body, which made every statement
    about its values independent of Lean.  It now carries its documented
    body `Cl_2 θ`.  Consequence: the old `BringZeroModeBlochClass` field
    (*some* real angle) became an intermediate-value fact
    (`BringZeroModeClausenWitness.lean`), so the field was restated over
    algebraic Bloch–Wigner combinations; it has no instance.  The root-of-unity (transcendence-obstructed)
    version is the separate class `BringZeroModeRootOfUnityClass`. -/
noncomputable def BlochWigner_unit_circle (θ : ℝ) : ℝ := Cl_2 θ

end QOU.Archimedean
