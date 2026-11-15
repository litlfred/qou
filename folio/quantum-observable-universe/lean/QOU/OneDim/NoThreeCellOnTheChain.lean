import QOU.Mass.LinearLayoutNoBulk
import Mathlib.Tactic

/-!
# QOU.OneDim.NoThreeCellOnTheChain — the missing term and the missing dimension are one gap

**What this connects.** Two results in the corpus sit in different arcs and have not been put
side by side. Read together they say something neither says alone.

* `QOU.LiftingDescent.CrossedModuleSurfaceHolonomy` (route D's first prune, bean `qou-20bk`)
  establishes that **no 2-dimensional Yekutieli object carries a non-abelian many-body term
  beyond word ordering**, because the kernel of the crossed-module feedback is central; and it
  names the one candidate that survives, in its own words:

  > "the only 3-body-shaped object in the book is the abelian volume term `∫γ` over a **3-cell**
  > — which is additive over 3-cells (extensive), exactly the *super-pairwise additive extensive
  > object* the Δ_λ audit asks for, **if** `γ ≠ 0` for the framework's connection."

  It records that the condition `γ ≠ 0` "cannot be evaluated: the framework's Step-2 curvature is
  stipulated, not a form."

* `QOU.Mass.LinearLayoutNoBulk` (sorry-free) proves that the coordination graph of **every** word
  the nuclear encoding can produce is a linear layout, and `QOU.Mass.SurfaceExponentIsDimension`
  states flatly that "the production word is one-dimensional, and this is exact".

**The bridge proved here.** A 3-cell needs three mutually incident sites. `no_triangle` shows a
linear layout has none: adjacency forces consecutive indices, and three indices cannot be pairwise
consecutive. So the corpus's one identified candidate for the missing extensive term is
**structurally unavailable on the corpus's own production geometry** — not blocked by the
unevaluated `γ ≠ 0`, but by there being no 3-cell to integrate it over.

The combinatorial fact is stated **once**, as `no_triangle`, and that is deliberate. A first
version of this file also carried a `threeCell_weight_vanishes : ∀ w, … → w a b c = 0`, on the
reasoning that the `∀ w` showed no choice of curvature could evade the obstruction. **That was
wrong and the theorem is deleted.** Its hypotheses are exactly the ones `no_triangle` proves
unsatisfiable, so every instance is vacuously true: the identical hypotheses also prove
`w a b c = r` for arbitrary `r`, and prove `0 = 1` — both mutants compile, and Lean's own
`unused variable 'w'` warning fires on them, because `w` never enters the proof. The conclusion
`= 0` was not distinguished by the theorem; the `∀ w` sat *outside* the vacuity rather than
protecting against it. The intuition it reached for is real and is already carried in full by
`no_triangle`: there is no 3-cell **at all**, independently of any weight. This is AGENTS.md
"Strict Lean Discipline" item 8 — read the statement and ask whether it could be wrong.

That is a second, independent obstruction, and it is the cheaper one to act on: `γ ≠ 0` is a
question about a stipulated curvature, whereas this one is a question about the layout, and
`LinearLayoutNoBulk` already closes its own docstring with *"a bulk needs a non-linear layout,
and the corpus derives no such layout"*. A bulk **is** a 3-cell. The missing extensive term and
the missing dimension are therefore the same gap, reached from two directions.

**Scope.** This is a statement about the encoding, scope-(b), invariant = the linear layout — it
inherits exactly the scope of `LinearLayoutNoBulk` and widens it by nothing. It says nothing
about what layout the physics wants, and nothing about whether `γ ≠ 0`. In particular it is
**not** an argument that the extensive term does not exist; it locates where it cannot be found.

Base ring §7c: none — pure combinatorics over `Fin n`, no `ℝ`, no ordering beyond `ℕ` arithmetic.

-- Ref: [yekutieli2015] https://arxiv.org/abs/1007.1250 — Thm 0.4.2 (2-dim Stokes), Thm 8.6.6
--      (3-dim Stokes: the abelian `∫γ` over a balloon).
-- Ref: [leitner2026] docs/audits/2026-09-14-one-dim-sector-and-the-three-cell-gap.md
-/

namespace QOU.OneDim

open QOU.Mass.LinearLayoutNoBulk

/-- **A linear layout has no triangle.** Adjacency in a linear layout forces the two indices to be
consecutive, and three indices cannot be pairwise consecutive: if `a` and `b` differ by one and
`b` and `c` differ by one, then `a` and `c` differ by zero or two, never by one.

This is the combinatorial content of "the chain has no 3-cell". -/
theorem no_triangle {n : ℕ} {G : SimpleGraph (Fin n)} (hL : LinearLayout G)
    (a b c : Fin n) (hab : G.Adj a b) (hbc : G.Adj b c) (hac : G.Adj a c) : False := by
  have h1 := hL a b hab
  have h2 := hL b c hbc
  have h3 := hL a c hac
  rcases h1 with h1 | h1 <;> rcases h2 with h2 | h2 <;> rcases h3 with h3 | h3 <;> omega

/-- Contrapositive, in the form a consumer wants: a graph carrying three mutually adjacent sites
is **not** a linear layout, so it is not a coordination graph the nuclear encoding can produce. -/
theorem not_linearLayout_of_triangle {n : ℕ} {G : SimpleGraph (Fin n)} (a b c : Fin n)
    (hab : G.Adj a b) (hbc : G.Adj b c) (hac : G.Adj a c) : ¬ LinearLayout G :=
  fun hL => no_triangle hL a b c hab hbc hac

end QOU.OneDim
