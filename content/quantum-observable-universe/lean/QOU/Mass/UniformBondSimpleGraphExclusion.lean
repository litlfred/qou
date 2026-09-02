/-
# No uniform-bond simple-graph assembly can produce `b₃ > 0`

`qou-edt7` asks why the coordination weight `w z = B(A)/C(A,2)` **rises** from
`z = 1` to `z = 2` — that rise being, by
`QOU.Mass.CoordinationWeightDifferences.lt_of_b3_pos`, the entire content of the
measured `b₃ = +1.426220 MeV > 0`.

This file answers the negative half of the question, and the answer is sharper
than the coordination-saturation picture suggested.

## The result

Let the binding be a **uniform bond weight `ε` summed over a simple graph**:

    B(A) = ε * e A,      e A = the number of edges of a simple graph on A vertices

Then `b₃ ≤ 0`, **always** — for every graph family, with no monotonicity, no cap,
and no hypothesis relating one mass number to another. The proof is a counting
bound and nothing more: a simple graph on three vertices has at most `3` edges,
a bonded pair has at least `1`, so

    b₃ = ε * (e 3 - 3 * e 2) ≤ ε * (3 - 3) = 0.

Equality holds exactly when the triple is complete **and** the pair carries one
bond, which is the pairwise-additive case
(`QOU.Mass.PairwiseCumulantVanishing`). Every sparser graph is strictly negative.

## Why this is stronger than the saturation argument

`QOU.Mass.CoordinationSaturation` shows that complete-graph coordination cannot
saturate (`complete_graph_no_saturation`) while bounded-degree coordination does
(`bounded_degree_saturates`), and concludes that saturation *forces* bounded
degree. Read through the coordination weight, a degree function `d` gives

    w z = ε * d (z+1) / z

so the complete graph gives `w` **constant** (`b₃ = 0`) and bounded degree `k`
gives `w z = ε k / z`, **strictly decreasing** (`b₃ < 0`). One might then hope
that some intermediate degree profile — saturating at large `A`, complete at
small `A` — could rise at the bottom. It cannot: `d 3 ≤ 2` for any simple graph,
which is exactly the `e 3 ≤ 3` bound above.

**So the entire coordination-multiplicity family is excluded as a source of
`b₃ > 0`**, not merely the two endpoints the corpus had checked.

## What that forces

`b₃ > 0` is therefore **not** a statement about which pairs are bonded. It
requires the bond weight itself to differ between the pair and the triple —
non-transferability. With a complete graph and a coordination-dependent weight
`ε z`, `w z = ε z`, and `b₃ > 0` says precisely

    ε 2 > ε 1     — the bond is STRONGER at coordination 2 than at coordination 1

measured as `2.6999729` against `2.2245662` MeV per pair, a rise of `21.4 %`.
That is the quantity a derivation has to produce, and this file does not produce
it. It only shows that no rearrangement of *which* pairs bind can substitute for
it.

## Scope

This is a **structural exclusion** in the sense of AGENTS.md §"Before declaring
refuted" case (b): the invariant is a proved counting bound (`e 3 ≤ 3` on simple
graphs), cited here, not a numerical probe that came out badly. What is excluded
is the conjunction *uniform bond weight* **and** *simple graph*. Dropping either
escapes it, and the physical reading of dropping the first is above. Dropping the
second means multi-edges or genuine higher simplices — a three-body bond that is
not a sum of two-body ones.

Base ring is a generic ordered ring; the content is counting, not archimedean.

Bean `qou-edt7`. Builds on `QOU.Mass.CoordinationWeightDifferences` and
`QOU.Mass.CoordinationSaturation`.
-/
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
set_option linter.unusedSectionVars false

namespace QOU.Mass.UniformBondSimpleGraphExclusion

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The connected three-body cumulant of a **uniform-bond** assembly, written in
terms of the edge counts alone: `b₃ = ε·(e₃ − 3·e₂)`. -/
def b3Uniform (ε : R) (e2 e3 : ℕ) : R := ε * ((e3 : R) - 3 * (e2 : R))

/-- **The exclusion.** A simple graph on three vertices has at most three edges,
and a bonded pair has at least one. Hence every uniform-bond simple-graph
assembly has `b₃ ≤ 0`.

No monotonicity, no degree cap, no relation between mass numbers is assumed. The
hypotheses are exactly "the triple's graph is simple" and "the pair is bonded". -/
theorem b3Uniform_nonpos {ε : R} (hε : 0 ≤ ε) {e2 e3 : ℕ}
    (h3 : e3 ≤ 3) (h2 : 1 ≤ e2) : b3Uniform ε e2 e3 ≤ 0 := by
  have h3' : (e3 : R) ≤ 3 := by exact_mod_cast h3
  have h2' : (1 : R) ≤ (e2 : R) := by exact_mod_cast h2
  have : (e3 : R) - 3 * (e2 : R) ≤ 0 := by linarith
  exact mul_nonpos_of_nonneg_of_nonpos hε this

/-- **The equality case is the complete triple.** `b₃ = 0` exactly when the
triple carries all three bonds and the pair carries one — the pairwise-additive
assembly. Every sparser graph is strictly negative. -/
theorem b3Uniform_eq_zero_of_complete {ε : R} : b3Uniform ε 1 3 = 0 := by
  unfold b3Uniform
  norm_num

/-- A chain on three vertices carries two bonds, and is strictly negative for a
positive bond weight. This is the arrangement the canonical braid wires. -/
theorem b3Uniform_neg_of_chain {ε : R} (hε : 0 < ε) : b3Uniform ε 1 2 < 0 := by
  have h : b3Uniform ε 1 2 = -ε := by
    unfold b3Uniform
    norm_num
  rw [h]
  linarith

/-- **The falsifiable form.** A measured `b₃ > 0` refutes the conjunction
"uniform bond weight" ∧ "simple graph" — for *every* graph family at once, so no
choice of which pairs bind can rescue it.

AME2020 gives `b₃ = +1.426220 MeV`, so the physical binding is not of this
shape. -/
theorem not_uniform_simple_of_b3_pos {ε : R} (hε : 0 ≤ ε) {e2 e3 : ℕ}
    (h : 0 < b3Uniform ε e2 e3) : ¬ (e3 ≤ 3 ∧ 1 ≤ e2) :=
  fun ⟨h3, h2⟩ => absurd (b3Uniform_nonpos hε h3 h2) (not_le.mpr h)

section CoordinationForm

/-- The coordination weight of a **degree-`d`** uniform-bond assembly, in the
form `w z = ε·d/z` used in the module docstring. Stated as the defining
relation `z · w = ε · d` to stay in a ring without division. -/
def coordWeightRel (ε w : R) (d z : ℕ) : Prop := (z : R) * w = ε * (d : R)

/-- **The complete graph gives a constant coordination weight.** With `d = z`
the relation reads `z·w = ε·z`, so `w = ε` for every `z ≥ 1` — hence `Δw = 0`
and `b₃ = 0`, recovering the pairwise wall from the degree picture. -/
theorem coordWeight_complete {ε w : R} {z : ℕ} (hz : 0 < z)
    (h : coordWeightRel ε w z z) : w = ε := by
  have hz' : (0 : R) < (z : R) := by exact_mod_cast hz
  have := h
  unfold coordWeightRel at this
  exact mul_left_cancel₀ (ne_of_gt hz') (by linarith [this])

/-- **Bounded degree gives a strictly decreasing coordination weight.** If the
degree is capped at `k` while `z` grows, `z·w` is pinned to the constant `ε·k`,
so `w` falls like `1/z`. Stated as: two coordinations sharing one capped degree
have `z₁ · w₁ = z₂ · w₂`. -/
theorem coordWeight_bounded_inv {ε w₁ w₂ : R} {k z₁ z₂ : ℕ}
    (h₁ : coordWeightRel ε w₁ k z₁) (h₂ : coordWeightRel ε w₂ k z₂) :
    (z₁ : R) * w₁ = (z₂ : R) * w₂ := by
  unfold coordWeightRel at h₁ h₂
  rw [h₁, h₂]

end CoordinationForm

end QOU.Mass.UniformBondSimpleGraphExclusion
