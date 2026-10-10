/-
# The `SLq(2)` knot label admits the atom word only at even `A`

Finkelstein's `SLq(2)` dictionary (`library/arxiv-0806.3105v3`, held) assigns a
knot the irrep matrix element `D^{N/2}_{w/2,(r+1)/2}`, where `(N, w, r)` are its
crossing number, writhe and rotation number. That is a *derived* knot →
representation map — no volume, no census scan, nothing fitted — and so a
candidate for the nucleus → link map the census route provably cannot supply.

For `D^j_{m m'}` to be a genuine irrep index, `j - m` and `j - m'` must be
integers. The first is automatic (`w ≡ N [2]`, each crossing contributing `±1`).
This file settles the second.

For a coherently-oriented closed braid on `n` strands with `c` crossings,
Seifert's algorithm yields `n` circles and `c` bands, so `χ = n - c`; and for a
genus-`g` surface with `μ` boundary components `χ = 2 - 2g - μ`. Hence

  `c - n = 2g + μ - 2`,

and `seifert_label_parity` below turns that into: the label is consistent
**iff the closure has an odd number of components**. For a knot (`μ = 1`) this
is automatic, which is why the dictionary is stated for knots.

`computations/probes/slq2_label_admits_even_a_only_probe.py` measures the atom
word's closure to have **`μ = A + 1`** components — branch-independent, since a
superposition letter and its `σ` branch project to the same permutation — and
cross-checks the deuteron's `μ = 3` against the 32/32 SnapPy branch measurement
recorded in `docs/audits/2026-08-25-knot-id-is-an-admitted-fit.md`. Feeding that
in gives `label_admits_even_A`: **even `A` yes, odd `A` never**, for every one of
the `2^(2A+1)` branches.

**Scope (a)** for this labelling applied to this word. It does not refute the
`SLq(2)` route; it locates what a generalisation must supply — a *link* version
of the labelling, the parity condition being exactly the knot condition.

No `sorry`. Everything is over `ℤ` with parity written as `% 2`, so `omega`
discharges it and no Mathlib parity API is needed.
-/
import Mathlib.Data.Nat.Basic

namespace QOU.Mass.SLq2Label

/-- The Euler-characteristic relation for a closed braid on `n` strands with `c`
crossings whose closure bounds a genus-`g` Seifert surface with `μ` boundary
components: `χ = n - c` and `χ = 2 - 2g - μ`. Carried as a hypothesis — it is
Seifert's algorithm, not something proved here. -/
def SeifertRelation (c n g mu : ℤ) : Prop := c - n = 2 * g + mu - 2

/-- `D^{N/2}_{w/2,(r+1)/2}` is a genuine irrep index only if `j - m'` is an
integer, i.e. `N - r - 1` is even. -/
def LabelConsistent (c r : ℤ) : Prop := (c - r - 1) % 2 = 0

/-- **The label condition is exactly a component-count parity condition.**
Given Seifert's relation with `r = n`, the label is consistent iff the closure
has an odd number of components. -/
theorem seifert_label_parity {c n g mu : ℤ} (h : SeifertRelation c n g mu) :
    LabelConsistent c n ↔ mu % 2 = 1 := by
  unfold SeifertRelation at h
  unfold LabelConsistent
  omega

/-- A knot has one component, so the label condition is automatic — which is why
the dictionary is stated for knots. -/
theorem knot_label_consistent {c n g : ℤ} (h : SeifertRelation c n g 1) :
    LabelConsistent c n := by
  rw [seifert_label_parity h]; decide

/-- The measured component count of the atom-word closure, `μ = A + 1`, is odd
exactly when `A` is even. -/
theorem components_odd_iff_even_A {A mu : ℤ} (h : mu = A + 1) :
    mu % 2 = 1 ↔ A % 2 = 0 := by omega

/-- **The atom word admits an `SLq(2)` label exactly at even `A`.** Combining
Seifert's relation with the measured `μ = A + 1`. Branch-independent: `μ` does
not depend on how the `2^(2A+1)` superposition letters resolve. -/
theorem label_admits_even_A {c n g A mu : ℤ}
    (hs : SeifertRelation c n g mu) (hmu : mu = A + 1) :
    LabelConsistent c n ↔ A % 2 = 0 := by
  rw [seifert_label_parity hs, components_odd_iff_even_A hmu]

/-- The excluded half is not incidental: the `A = 3` mirror pair, where this
arc's convention systematic lives, carries `μ = 4` and admits no label. -/
example : ¬ ((4 : ℤ) % 2 = 1) := by decide

/-- The deuteron: `μ = 3`, odd, so the label is consistent at `A = 2`. -/
example {c n g : ℤ} (hs : SeifertRelation c n g 3) : LabelConsistent c n := by
  rw [seifert_label_parity hs]; decide

end QOU.Mass.SLq2Label
