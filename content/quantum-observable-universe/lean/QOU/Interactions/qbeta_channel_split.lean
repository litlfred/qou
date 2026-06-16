import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring

/-!
# Q_β counit — internal bar-parity decomposition (NOT a binding double-count)

> **Correction (2026-06-16).** An earlier version of this file claimed the
> bar-even part of the counit was "the channel #2346 books as binding," i.e.
> a binding/Q_β **double-count**. That was wrong. The #2346 witness
> `habiro-exact-qbeta` reports `Q_A = Im 𝔙 = 0.78364580… MeV`, which equals
> the **full** counit `|ε(Δ)|·𝔈₀` to `2·10⁻¹⁶` (branch A): their `Im 𝔙` is
> the *whole* counit value, **not** the bar-odd part alone. So there is **no
> double-count** — the two framings agree, and the split below is an
> *internal* decomposition of the counit, distinct from #2346's
> binding/Q_β (Re/Im of the single-knot confinement defect) split.

The counit on the nucleon difference, `ε(Δ) = h²/2 − h` (`h = q − q⁻¹`),
decomposes under the bar-involution `h ↦ −h` into a bar-even `h²/2` and a
bar-odd `−h` part. These lemmas record that algebra. They do **not** assign
the bar-even part to any other observable.

Generic field; `h` free (CLAUDE.md §7c).
-/

namespace QOU.Interactions.QBetaChannelSplit

variable {R : Type*} [Field R]

/-- Bar-even part of the counit on the nucleon difference, `h²/2`. -/
def barEven (h : R) : R := h ^ 2 / 2

/-- Bar-odd part of the counit on the nucleon difference, `−h`. -/
def barOdd (h : R) : R := -h

/-- The counit `ε(Δ) = h²/2 − h` is the sum of its bar-even and bar-odd
    parts. (Internal decomposition; both parts belong to the counit / `Q_β`,
    per the branch-A resolution — see file header.) -/
theorem counit_split (h : R) : h ^ 2 / 2 - h = barEven h + barOdd h := by
  unfold barEven barOdd; ring

/-- `barEven` is invariant under the bar-involution `h ↦ −h`. -/
theorem barEven_invariant (h : R) : barEven (-h) = barEven h := by
  unfold barEven; ring

/-- `barOdd` is negated under the bar-involution `h ↦ −h`. -/
theorem barOdd_anti (h : R) : barOdd (-h) = - barOdd h := by
  unfold barOdd; ring

/-- The bar-even remainder: `ε(Δ) − barOdd = barEven`. This is the internal
    `h²/2` term; it is part of the counit `Q_β`, **not** a separate binding
    contribution (the earlier "double-count" reading is refuted by the #2346
    `Im 𝔙 = ` full-counit witness — see file header). -/
theorem barEven_remainder (h : R) :
    (h ^ 2 / 2 - h) - barOdd h = barEven h := by
  unfold barEven barOdd; ring

end QOU.Interactions.QBetaChannelSplit
