import Mathlib.Data.Complex.Basic

/-!
# QOU.Observations.CPViolationSpectralForm

CP-violating discriminant `δ_CP` as the imaginary part of the
alternating/symmetric Wedderburn-block trace ratio.

Conditional on `complex_chirality_rotation` — the complexification of
the substrate parameter `q = |q| exp(iθ)`.

LaTeX label: `conj:cp-violation-spectral-form`

## References

- [leitner2026] §6/cp-violation-spectral-form
- [christenson1964] https://doi.org/10.1103/PhysRevLett.13.138
-/

namespace QOU.Observations

/-- Conjectural class: the substrate parameter is complexified, with
    the alternating-block character carrying the residual phase. -/
class ComplexSubstrate where
  q_modulus : ℝ
  q_phase : ℝ                        -- θ_res
  modulus_pos : 0 < q_modulus

/-- Wedderburn-block characters as complex numbers under the
    complexified substrate. -/
structure WedderburnComplexCharacters where
  chiAlt : ℂ                         -- χ_{(1^n)}(β)
  chiSym : ℂ                         -- χ_{(n)}(β)
  sym_nonzero : chiSym ≠ 0

/-- The CP-violating discriminant as the imaginary part of the
    alternating/symmetric ratio. -/
noncomputable def deltaCP (W : WedderburnComplexCharacters) : ℝ :=
  (W.chiAlt / W.chiSym).im

/-! ## What is proved here, and what stays open

**Superseded 2026-09-05.** This file carried

```lean
theorem cp_violation_spectral_form [ComplexSubstrate]
    (W : WedderburnComplexCharacters) :
    ∃ δ : ℝ, δ = (W.chiAlt / W.chiSym).im :=
  ⟨(W.chiAlt / W.chiSym).im, rfl⟩
```

`∃ x, x = e` is provable by `⟨e, rfl⟩` for **any** well-typed `e`, so it
asserted nothing about the ratio — only that a name for it exists, which in a
total type theory is free. It did not mention `deltaCP`, defined immediately
above it, and its `[ComplexSubstrate]` binder was unused. Its docstring called
it a *Conjecture* while its kind was `theorem`.

Found by `scripts/lean-vacuous-existential-audit.py` only after that detector's
bound-variable pattern was widened from ASCII to Unicode — `δ` is not ASCII, so
this had been invisible to the audit written to catch exactly this shape. Bean
`qou-ekga`.

**Replaced by the conjecture's own falsifiability claim, which is provable.**
The `.md` states: *"Amphicheiral or real-`q` configurations have
`Im(χ_λ) = 0` and `δ_CP = 0`"*, and under **Falsifiability**: *"Amphicheiral
knots must yield exactly `δ_CP = 0`. Any amphicheiral hadron exhibiting CP
violation falsifies this characterization."* That direction follows from the
definition — a quotient of two reals is real — so it is stated below as a
theorem with load-bearing hypotheses, not invented for this file.

**What stays open, and is deliberately NOT given a Lean carrier here.** The
conjecture proper is an *identification*: that the physical CP-violating
discriminant of a hadronic braid IS this ratio's imaginary part. That claim
needs an independently-defined `δ_CP` to be set against, and the corpus has
none — `observations/complex-chirality-rotation.lean:44` records the numerical
bound as future work. Writing a class here whose field asserted the
identification against `deltaCP` itself would be a self-assuming projection, so
the open half is left in the narrative where it can be read as open. -/

/-- **Real characters give no CP violation.**

    If both Wedderburn-block characters are real — the amphicheiral and
    real-`q` configurations — then the discriminant vanishes identically.

    This is the falsifiable content the `.md` names: an amphicheiral hadron
    exhibiting CP violation would contradict it. Both hypotheses are used. -/
-- Ref: [leitner2026] §6/cp-violation-spectral-form
-- Ref: [christenson1964] Evidence for the $2\pi$ Decay of the $K_2^0$ Meso — see folio/schema/references.ts
theorem deltaCP_eq_zero_of_real_characters
    (W : WedderburnComplexCharacters)
    (hAlt : W.chiAlt.im = 0) (hSym : W.chiSym.im = 0) :
    deltaCP W = 0 := by
  simp [deltaCP, Complex.div_im, hAlt, hSym]

/-- **Conjecture carrier (§3b): the spectral form of `δ_CP`.**

    The conjecture is an IDENTIFICATION — that the CP-violating discriminant of
    a hadronic braid *is* the imaginary part of the alternating/symmetric
    character ratio. Stating it needs a `δ_CP` on the left that is not already
    *defined* as that ratio, and this file's `deltaCP` is exactly that
    definition. So the physical discriminant enters as a PARAMETER, supplied by
    the caller; asserting the identity against `deltaCP` itself would be a
    self-assuming projection (§3b-cond item 5).

    The field is content-bearing: it is false for any `physicalDeltaCP`
    disagreeing with `deltaCP` at a single `W`, so `⟨True⟩`-style inhabitation
    is impossible.

    **No instance is provided, and that is the honest open state** (§3b-tax).
    Constructing one requires an independently-defined CP-violating
    discriminant, which the corpus does not have —
    `observations/complex-chirality-rotation.lean:44` records the numerical
    bound `δ_CP = O(θ²)` as future work. Per the `.md`, a proof also needs
    `R_ℂ`-enrichment uniqueness and a match of `θ_res` to the Wolfenstein
    parameterisation. -/
-- Ref: [leitner2026] §6/cp-violation-spectral-form
-- Ref: [christenson1964] Evidence for the $2\pi$ Decay of the $K_2^0$ Meso — see folio/schema/references.ts
class CPViolationSpectralForm
    (physicalDeltaCP : WedderburnComplexCharacters → ℝ) : Prop where
  /-- The identification the conjecture asserts. -/
  spectral_form : ∀ W : WedderburnComplexCharacters, physicalDeltaCP W = deltaCP W

/-- The carrier's one consequence, stated so the class is not write-only:
    under the conjecture, real characters give no physical CP violation.
    Composes the carrier with `deltaCP_eq_zero_of_real_characters`. -/
theorem physical_deltaCP_eq_zero_of_real_characters
    (physicalDeltaCP : WedderburnComplexCharacters → ℝ)
    [h : CPViolationSpectralForm physicalDeltaCP]
    (W : WedderburnComplexCharacters)
    (hAlt : W.chiAlt.im = 0) (hSym : W.chiSym.im = 0) :
    physicalDeltaCP W = 0 := by
  rw [h.spectral_form, deltaCP_eq_zero_of_real_characters W hAlt hSym]

end QOU.Observations
