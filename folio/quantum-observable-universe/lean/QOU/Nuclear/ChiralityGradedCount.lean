import Init.Data.Int.Basic
import Init.Omega

/-!
# QOU.QBeta.ChiralityGradedCount — a fully proved, input-independent obstruction: no symmetric scalar recovers a chirality-split count

## Why this file exists (the transcription problem)

`FiveTwoDTSpectrumSplit` and `RouteANewtonPolygonDT` prove sharp statements, but
each takes **hand-transcribed literature data** as `def`s (the GGM eq-(96)/(97)
Stokes matrices; the `A_{4₁}` monomials; the `5₂` boundary slopes). Lean cannot
verify a transcription from a PDF, so those results are *conditional on the
transcription being faithful* — the `sorry-free ≠ derived` boundary. Their inputs
are cross-validated (`det S± = 1`, `S⁺ᵀS⁻ = 1`, the reciprocal symmetry of the
Newton polygon), which is strong evidence, but evidence is not proof.

This file isolates the part of the argument that needs **no input at all**. Every
theorem below is a statement about *arbitrary* integers, proved outright. The
knot-specific numbers `(4, 3)` then appear only as an *instance*, never as a
hypothesis of the general result.

## The mathematical content

A chirality-split count is an **ordered pair** `(a, b)` (the `S⁺` and `S⁻`
constants). The mirror involution `τ` swaps them. Then:

* `barGrading_faithful_general` — the `ℤ/2` decomposition into
  `even = a + b` (τ-fixed) and `odd = a − b` (τ-negated) loses no information:
  `2a = even + odd`, `2b = even − odd`.
* `symmetric_scalar_cannot_separate` — **the obstruction.** *Any* symmetric
  function `g : ℤ → ℤ → ℤ` takes the same value on `(a,b)` and on its mirror
  `(b,a)`. So if a count is genuinely chiral (`a ≠ b`, equivalently `odd ≠ 0`),
  no symmetric scalar reading distinguishes the two chiralities: the scalar is
  precisely the `τ`-trivial shadow of the graded object.
* `chiral_iff_odd_ne_zero` — "genuinely chiral" and "nonzero bar-odd part" are
  the same condition.
* `amphichiral_collapse` — when `a = b` (the amphichiral case) the bar-odd part
  vanishes and the pair degenerates to a single number, which is exactly why a
  single knot with `a = b` can never exhibit the obstruction.

The last point is the methodological payload: it is a *proof* that testing on an
amphichiral knot alone (e.g. `4₁`) is structurally incapable of separating
"scalar" from "graded" — the cross-knot gate is not a stylistic preference but a
logical necessity.

None of this derives `A_ω`, and none of it depends on any literature value.

-- Ref: [leitner2026] docs/audits/2026-08-11-route-c-bps-cohomology-scoping.md (Route C, M0)
-/

namespace QOU.QBeta.ChiralityGradedCount

/-- A chirality-split count: the ordered pair of `S⁺` and `S⁻` constants. -/
abbrev Split := Int × Int

/-- The mirror involution `τ` exchanging the two chiralities. -/
def mirror (p : Split) : Split := (p.2, p.1)

/-- `τ` is an involution. -/
theorem mirror_involutive (p : Split) : mirror (mirror p) = p := by
  cases p; rfl

/-- The `τ`-fixed (bar-even) part. -/
def barEven (p : Split) : Int := p.1 + p.2

/-- The `τ`-negated (bar-odd) part. -/
def barOdd (p : Split) : Int := p.1 - p.2

/-- `τ` fixes the bar-even part: it is the `+1` eigenvector. -/
theorem barEven_mirror (p : Split) : barEven (mirror p) = barEven p := by
  cases p; unfold barEven mirror; omega

/-- `τ` negates the bar-odd part: it is the `−1` eigenvector. -/
theorem barOdd_mirror (p : Split) : barOdd (mirror p) = - barOdd p := by
  cases p; unfold barOdd mirror; omega

/-- **The `ℤ/2` grading is faithful** — no information is lost in passing to the
bar-even/bar-odd parts. -/
theorem barGrading_faithful_general (p : Split) :
    2 * p.1 = barEven p + barOdd p ∧ 2 * p.2 = barEven p - barOdd p := by
  cases p; unfold barEven barOdd; constructor <;> omega

/-- A split is **genuinely chiral** when its two constants differ. -/
def IsChiral (p : Split) : Prop := p.1 ≠ p.2

instance (p : Split) : Decidable (IsChiral p) := by
  unfold IsChiral; infer_instance

/-- **Chirality is exactly nonvanishing of the bar-odd part.** -/
theorem chiral_iff_odd_ne_zero (p : Split) : IsChiral p ↔ barOdd p ≠ 0 := by
  cases p; unfold IsChiral barOdd; omega

/-- Not-chiral is exactly equality of the two constants. -/
theorem not_chiral_iff_eq (p : Split) : ¬ IsChiral p ↔ p.1 = p.2 := by
  cases p; unfold IsChiral; omega

/-- **Amphichiral collapse.** If the two constants agree, the bar-odd part is
zero and the pair is its own mirror — the degenerate case in which a single
scalar *does* carry the whole datum. -/
theorem amphichiral_collapse (p : Split) (h : p.1 = p.2) :
    barOdd p = 0 ∧ mirror p = p := by
  cases p
  unfold barOdd mirror at *
  simp_all

/-- **The obstruction, in full generality.** Any symmetric integer reading `g`
assigns the same value to a split and to its mirror. Hence for a genuinely chiral
split, `g` cannot depend on the chirality at all: every symmetric scalar is blind
to the `−1` eigenspace, which for a chiral count is nonzero.

This is the input-free form of
`FiveTwoDTSpectrumSplit.symmetric_scalar_blind_to_chirality`; the knot numbers
enter only in the instance below. -/
theorem symmetric_scalar_cannot_separate
    (g : Int → Int → Int) (hsym : ∀ a b, g a b = g b a) (p : Split) :
    g p.1 p.2 = g (mirror p).1 (mirror p).2 := by
  cases p; exact hsym _ _

/-- **Consequence.** For a chiral split, a symmetric scalar takes one value while
the datum it is meant to represent has a nonzero bar-odd part — so the scalar
cannot determine the ordered pair. -/
theorem symmetric_scalar_loses_chirality
    (g : Int → Int → Int) (hsym : ∀ a b, g a b = g b a)
    (p : Split) (hchi : IsChiral p) :
    g p.1 p.2 = g p.2 p.1 ∧ barOdd p ≠ 0 :=
  ⟨hsym _ _, (chiral_iff_odd_ne_zero p).mp hchi⟩

/-- **A single amphichiral knot cannot exhibit the obstruction.** If the split is
amphichiral, it equals its own mirror, so *every* reading — symmetric or not —
agrees on it and on its mirror. The cross-knot (chiral) test is therefore a
logical necessity, not a methodological preference. -/
theorem amphichiral_cannot_witness_obstruction
    (f : Int → Int → Int) (p : Split) (h : p.1 = p.2) :
    f p.1 p.2 = f (mirror p).1 (mirror p).2 := by
  have hm : mirror p = p := (amphichiral_collapse p h).2
  rw [hm]

/-! ## The knot instance — literature values enter ONLY here

The `5₂` DT constants `(S⁺, S⁻) = (4, 3)` (GGM eq 96/97, transcribed in
`FiveTwoDTSpectrumSplit`) and the amphichiral `4₁` value `(3, 3)`. Everything
above is independent of these; they are supplied as an instance to show the
general theorems are non-vacuous and correctly aimed. -/

/-- The `5₂` chirality split (literature instance). -/
def dtSplit52 : Split := (4, 3)

/-- The `4₁` split: amphichirality forces the two constants to coincide. -/
def dtSplit41 : Split := (3, 3)

/-- `5₂` is chiral, with bar-grading `(even, odd) = (7, 1)`. -/
theorem dtSplit52_chiral_grading :
    IsChiral dtSplit52 ∧ barEven dtSplit52 = 7 ∧ barOdd dtSplit52 = 1 := by
  refine ⟨by decide, by decide, by decide⟩

/-- `4₁` is amphichiral: its bar-odd part vanishes. -/
theorem dtSplit41_amphichiral : ¬ IsChiral dtSplit41 ∧ barOdd dtSplit41 = 0 := by
  refine ⟨by decide, by decide⟩

/-- The `4₁` split satisfies the amphichiral collapse hypothesis. -/
theorem dtSplit41_eq : dtSplit41.1 = dtSplit41.2 := by decide

/-- **The instance of the obstruction**: no symmetric scalar separates the `5₂`
chiralities, and the datum it must represent is chiral. -/
theorem dtSplit52_obstruction
    (g : Int → Int → Int) (hsym : ∀ a b, g a b = g b a) :
    g 4 3 = g 3 4 ∧ barOdd dtSplit52 ≠ 0 :=
  symmetric_scalar_loses_chirality g hsym dtSplit52 (by decide)

end QOU.QBeta.ChiralityGradedCount
