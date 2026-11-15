import Mathlib.Tactic

/-!
# QOU.Conjectures.ShellTransitionKnot — magic numbers from shell transitions

Conjectural axiomatisation of `conj:shell-transition-knot`
(`folio/quantum-observable-universe/particle-interactions/shell-transition-knot.md`).

The seven stability pairs `{2, 8, 20, 28, 50, 82, 126}` arise from the
3-D harmonic-oscillator shell structure of nucleons in the nuclear mean
field, corrected by the spin–orbit coupling of the Borromean baryon's
three internal crossings.

The harmonic-oscillator content is concrete and **proved** here:
shell sizes `s_N = (N+1)(N+2)`, cumulative closures
`C_N = (N+1)(N+2)(N+3)/3`, and the uncorrected closure sequence
`{2, 8, 20, 40, 70, …}` (which does *not* match observation — the gap
the spin–orbit correction must close).  The conjectural content (that
the spin–orbit threshold set by the three Borromean crossings produces
exactly the observed `{2, 8, 20, 28, 50, 82, 126}`) is carried by the
content-bearing class with **no instance**.

This is a **dependent** conjecture: it is conditional on
`conj:borromean-quark` (the Borromean-baryon model that supplies the
crossing count `3`).  The dependency is threaded through the type by the
`[BorromeanQuark]` instance binder (AGENTS.md §3b-cond / §3b-tax).

LaTeX label: `conj:shell-transition-knot`

## References

- [leitner2026] §"Shell-transition knot"
-/

namespace QOU.Conjectures

/-- 3-D harmonic-oscillator shell size at level `N`: `(N+1)(N+2)`. -/
def hoShellSize (N : ℕ) : ℕ := (N + 1) * (N + 2)

/-- Cumulative HO closure at level `N`:
    `C_N = ∑_{k=0}^{N} (k+1)(k+2) = (N+1)(N+2)(N+3)/3`. -/
def hoClosure (N : ℕ) : ℕ := (N + 1) * (N + 2) * (N + 3) / 3

/-- The cumulative closure equals the explicit running sum of the shell
    sizes across the first seven levels (the standard HO bookkeeping over
    the range that produces the magic-number candidates). -/
theorem hoClosure_eq_sum_first_seven :
    (List.range 7).map hoClosure =
      (List.range 7).map (fun N => (Finset.range (N + 1)).sum hoShellSize) := by
  decide

/-- The first three HO closures are the (uncorrected) values
    `{2, 8, 20}` — these already match the first three magic numbers. -/
theorem hoClosure_first_three :
    hoClosure 0 = 2 ∧ hoClosure 1 = 8 ∧ hoClosure 2 = 20 := by decide

/-- Without spin–orbit coupling the closures continue `{40, 70, 112, …}`,
    which do **not** match the observed `{28, 50, 82, …}` — the gap the
    spin–orbit correction must close. -/
theorem hoClosure_uncorrected_mismatch :
    hoClosure 3 = 40 ∧ hoClosure 4 = 70 ∧ hoClosure 5 = 112 := by decide

/-- The seven observed nuclear stability pairs (magic numbers). -/
def stabilityPairs : List ℕ := [2, 8, 20, 28, 50, 82, 126]

/-- **Borromean-baryon model** (`conj:borromean-quark`), the upstream
    conjecture this block is conditional on.  Its field records the
    crossing count of the Borromean link `B₃` that sets the spin–orbit
    threshold — genuine content, not a bare `True`. -/
class BorromeanQuark where
  /-- Minimum crossing number of the Borromean link `B₃`. -/
  crossingNumber : ℕ
  /-- The Borromean link has exactly three crossings. -/
  crossingNumber_eq : crossingNumber = 3

/-- **Conjecture class** (`conj:shell-transition-knot`), conditional on
    `[BorromeanQuark]`.

An instance supplies the spin–orbit-corrected cumulative closure
function `correctedClosure` and asserts that its first seven values
reproduce the observed stability pairs `{2, 8, 20, 28, 50, 82, 126}` —
with the shell-transition threshold set at `N = 3` matching the three
Borromean crossings (`BorromeanQuark.crossingNumber`).

The field `closures_match` carries the conjecture's genuine content (the
corrected closures equal the observed magic numbers), not a bare `True`.
The `[BorromeanQuark]` binder makes this a **dependent** conjecture. -/
class ShellTransitionKnot [BorromeanQuark] where
  /-- The spin–orbit-corrected cumulative shell closure at level `N`. -/
  correctedClosure : ℕ → ℕ
  /-- **Conjectural shell-transition identity.**  The corrected closures
      at levels `0..6` reproduce the seven observed stability pairs. -/
  closures_match :
    (List.range 7).map correctedClosure = stabilityPairs

-- No instance: both `conj:borromean-quark` (upstream) and
-- `conj:shell-transition-knot` are OPEN (AGENTS.md §3b-tax).  A
-- `mockCorrectedClosure` that hardcodes `{2,8,20,28,50,82,126}` and
-- discharges `closures_match` by `decide` is FITTING the answer into a
-- lookup table, not deriving the spin–orbit correction from the three
-- Borromean crossings — precisely the anti-laundering pattern the rule
-- forbids.  The genuine HO content above (`hoClosure`, the closure
-- theorems) is proved; the corrected-closure identity remains open.

end QOU.Conjectures
