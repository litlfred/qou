import QOU.BraidKnot.TableauPerm
import QOU.BraidKnot.RowStandardTableau
import QOU.BraidKnot.SpechtDominanceCore
import QOU.Machinery.CoxeterBruhat
import QOU.Hecke.SymmetricCoxeter

/-!
# Dipper–James: dominance on row-standard tableaux is the Bruhat order

Mathas states this immediately before using it, and the sentence is worth quoting because it
is the reason this file exists at all:

> The partial order `⊵` on `S_n` is the ubiquitous **Bruhat–Chevalley order**.  Perhaps
> surprisingly, it **agrees with the dominance ordering on row standard λ-tableaux** (when
> restricted to `D_λ`).
>
> **3.7 Proposition (Dipper–James).**  Let λ be a composition of `n` and suppose that `s` and
> `t` are row standard λ-tableaux.  Then `s ⊵ t` if and only if `d(s) ⊵ d(t)`.

`TableauPerm.dOf` is a **bijection** onto `Perm (Fin (nOf μ))` (`equivPerm`), so this says the
two orders are **the same order transported along `d`** — not two orders that co-operate.

## Why that matters here

`MurphyInductionMeasure.murphyLex` is `lex-on-shapes × dominance-on-tabloids`.  Under 3.7 its
inner axis **is Bruhat**, which is what makes Mathas' Corollary 3.8 — whose proof opens by
invoking Theorem 1.1.11, that `T_{d(v)} T_w` is supported on **subexpressions** of `d(v)w` —
speak about the same order the induction descends in.

## 🛑 THE ORIENTATION IS REVERSING.  Do not transcribe 3.7 off the page.

The obvious reading of *"`s ⊵ t` iff `d(s) ⊵ d(t)`"* is `d(t) ≤ d(s)` in **standard** Bruhat.
**That is backwards.**  `t^λ` is dominance-MAXIMAL while `d(t^λ) = 1` is Bruhat-MINIMAL
(`TableauPerm.dOf_refTab`), so `d` is order-**reversing** onto standard Bruhat.  Mathas' `⊵`
on `S_n` is standard Bruhat with the order reversed, and the correct correspondence is

    s ⊵ t   ↔   d(s) ≤ d(t)      (standard Bruhat, i.e. `CoxeterBruhat.BruhatLe`)

This was **measured before being stated**, and the wrong-way version is what caught it:
[`dipper_james_dominance_is_bruhat_probe.py`](../../../../../computations/hecke/dipper_james_dominance_is_bruhat_probe.py)
run against `d(t) ≤ d(s)` fails at 30/46, 511/773, 14201/19426, 565748/708062 — *identically
in both directions and under both definitions of Bruhat*.  **Equal forward and converse
counts is the signature of a flipped relation, not of a counterexample**, which is how it was
caught rather than reported as a refutation of a published lemma.  Run the right way round:

| n | ordered pairs | `s ⊵ t → d(s) ≤ d(t)` | converse |
|---|---|---|---|
| 3 | 46 | 46/46 | 46/46 |
| 4 | 773 | 773/773 | 773/773 |
| 5 | 19 426 | 19 426/19 426 | 19 426/19 426 |
| 6 | 708 062 | 708 062/708 062 | 708 062/708 062 |

Sixth instance of the handedness/orientation trap on this arc, and the first caught before
any Lean was written rather than after.

## Which Bruhat, and which `d` — both settled by measurement

**Which Bruhat.**  `CoxeterBruhat.BruhatLe` is the **subword** definition; Mathas' is
**reflection-generated with length increase** (`w = v t₁⋯t_k` with `ℓ(v t₁⋯t_j) = ℓ(v) + j`).
Their equivalence is a theorem, not an unfolding — but the probe compares them permutation by
permutation and finds them **identical** on `S₃`…`S₆` (6/6, 24/24, 120/120, **720/720**).  So
this file states 3.7 against `BruhatLe` without choosing sides.  That is evidence, **not** a
discharge of the subword property as a proof obligation: Corollary 3.8 needs it for arbitrary
`n`.

**Which `d`.**  3.7 is stated for a **composition** λ.  This file is for **partition** shapes,
because a partition *is* a composition (so this is a genuine special case, not an analogue);
because `TableauPerm.dOf t = refTab.trans t.symm` with `refTab = t^λ` row-superstandard **is**
Mathas' `d(t)`, the one defined by `t = t^λ · d(t)`; and because `murphyLex` is indexed by
`PartOf n`, so the partition case is exactly what consumes it.  The composition form stays
available in `CompositionCoset*` if 3.9 at basis level turns out to need it.

## Status of what is below

`refTab_dOf_bruhatLe` is **sorry-free** and is the orientation fact in its own right: the
reference tableau sits at the **bottom** of Bruhat while being the **top** of dominance.

`dominance_iff_bruhatLe` is **stated, not proved** — the honest state-and-queue marker of
`AGENTS.md` §1, with its `-- Ref:` citation.  It is a published theorem (Dipper–James, via
Mathas 3.7), not an open problem, and it is confirmed by exhaustive measurement to `n = 6`;
what is missing is the formalisation.

## 🛑 What discharging that `sorry` ACTUALLY needs — measured, not guessed

Mathas' proof is an induction on a transposition `(a,b)` chosen at the first row where `s`
and `t` differ, and needs no Hecke algebra.  **But it does not run against the statement as
written here**, and that is worth knowing before anyone starts:

* the inductive step is *"if `v = t·(a,b)` then `v ▷ t` and `d(v) ▷ d(t)`"* — a **Bruhat
  cover by an arbitrary transposition with length increase**.  That is the **reflection**
  characterisation of Bruhat;
* this file states 3.7 against `CoxeterBruhat.BruhatLe`, the **subword** one.

So the proof route needs the bridge **subword ⟺ reflection**.  Surveyed:

| what | where |
|---|---|
| a reflection Bruhat order | **absent from the corpus** |
| subword ⟺ reflection | **absent from the corpus** |
| length under a **simple** transposition | `Hecke.ParabolicPairing.length_swap_dichotomy`, `length_mul_swap_eq_succ_iff`, `length_swap_cases` — proved, but **simple** reflections only, while Mathas needs arbitrary `(a,b)` |

**The probe's 720/720 does not shortcut this.**  Subword and reflection agreeing on
`S₃`…`S₆` is evidence the bridge is true; it is not the bridge.

### 🟩 CORRECTED WITHIN THE HOUR — #6894 landed and the table above is stale

That survey was written against `main` before **#6894** merged (`6d0cb3a094`), and two of its
three rows are now wrong.  Verified against `main` itself, not against the PR body:

| what | then | **now** |
|---|---|---|
| a reflection Bruhat order | absent | **`IwahoriHecke.BruhatReflection.ReflLe`** — `ReflStep v w := ∃ t, IsReflection t ∧ w = v*t ∧ ℓ v < ℓ w`, then `ReflTransGen`.  That is *exactly* Mathas' step. |
| subword ⟺ reflection | absent | **one direction proved**: `bruhatLe_of_reflLe`, and `bruhatLe_of_reflLe_An` is the **hypothesis-free type-A** corollary — i.e. it applies to `Sₙ` with nothing to discharge |
| Bruhat antisymmetry / subword property / transitivity / lifting | all four deferred in `CoxeterBruhat` | **all four proved** (#6894, via Matsumoto) |

So the two routes above collapse: **route 2 is unnecessary** (the reflection order exists),
and **route 1 is half done**.

### What that makes provable, and what it does not

Mathas' proof constructs precisely `ReflStep`s — multiply by a transposition, length goes up.
Composing with `bruhatLe_of_reflLe_An` therefore reaches `BruhatLe`.  So:

* **forward** (`s ⊵ t → d(s) ≤ d(t)`) is **unblocked**: the Coxeter side is now supplied and
  what remains is the tableau combinatorics — the induction on a transposition at the first
  differing row;
* **converse** (`d(s) ≤ d(t) → s ⊵ t`) still needs **`BruhatLe → ReflLe`**, which is open and
  tracked as bean **`qou-3k66`**.  #6894's own "left open" section names it as *"what a
  consumer citing Mathas' Prop 3.7 needs for an `↔`"* — this file is that consumer.

The `iff` below should therefore be **split** into the two implications, so the reachable half
is not held hostage to the blocked one.  Left as an `iff` for now only because splitting it is
a statement change and the forward proof is the next commit, not this one.
-/

open Equiv
open QOU.Hecke.SymmetricCoxeter

namespace QOU.BraidKnot.DominanceIsBruhat

open QOU.BraidKnot.TableauPerm QOU.BraidKnot.SpechtDominanceCore

variable {μ : YoungDiagram} {n : ℕ}

/-! ### The orientation, proved

`dOf_refTab` puts the reference tableau at `1`, and `1` is below everything in Bruhat.  So
`t^λ` — which is the **maximum** of the dominance order — maps to the **minimum** of Bruhat.
That is the whole content of "the correspondence reverses", and it is why writing 3.7 as
`d(t) ≤ d(s)` produces a statement that fails on half its instances. -/

/-- **The reference tableau maps to the bottom of the Bruhat order.**

Sorry-free, and it pins the orientation of `dominance_iff_bruhatLe` below: `refTab` is
dominance-maximal, so under 3.7 it must be Bruhat-*minimal*, which is exactly what this says.
Anyone tempted to state 3.7 the other way round should read this first. -/
theorem refTab_dOf_bruhatLe (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (t : QOU.BraidKnot.Specht.Tableau μ) :
    QOU.Machinery.CoxeterBruhat.BruhatLe (permCoxeterSystem n)
      (toFinSucc hn (dOf (refTab μ))) (toFinSucc hn (dOf t)) := by
  rw [dOf_refTab]
  have : toFinSucc hn (1 : Perm (Fin (QOU.BraidKnot.Specht.nOf μ))) = 1 := by
    refine Equiv.ext fun x => ?_
    simp [toFinSucc]
  rw [this]
  exact QOU.Machinery.CoxeterBruhat.one_bruhatLe _ _

/-! ### Dipper–James 3.7 itself -/

/-- **Dipper–James (Mathas 3.7): dominance on row-standard tableaux is the Bruhat order.**

`domRel a b` reads "`a` is dominated by `b`", so `domRel ⟦t⟧ ⟦s⟧` is "`s` dominates `t`".
The Bruhat side is `d(s) ≤ d(t)` — **reversing**; see the module docstring, and
`refTab_dOf_bruhatLe` for the fact that forces it.

Measured exhaustively over every ordered pair of row-standard tableaux of every partition of
`n ≤ 6`: **708 062/708 062 in both directions at `n = 6`**, under both definitions of the
Bruhat order.  What is missing is the formalisation, not the mathematics; Mathas' proof is an
induction on a transposition chosen at the first row where `s` and `t` differ. -/
-- Ref: [dipper-james1986] Dipper & James, *Blocks and idempotents of Hecke algebras of
-- general linear groups*, Proc. LMS (3) 54 (1987) 57-82; and [mathas1999] Mathas,
-- *Iwahori-Hecke algebras and Schur algebras of the symmetric group*, Proposition 3.7.
theorem dominance_iff_bruhatLe (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    {s t : QOU.BraidKnot.Specht.Tableau μ}
    (_hs : QOU.BraidKnot.RowStandardTableau.IsRowStandard s)
    (_ht : QOU.BraidKnot.RowStandardTableau.IsRowStandard t) :
    domRel (QOU.BraidKnot.Specht.Tabloid.mk t) (QOU.BraidKnot.Specht.Tabloid.mk s)
      ↔ QOU.Machinery.CoxeterBruhat.BruhatLe (permCoxeterSystem n)
          (toFinSucc hn (dOf s)) (toFinSucc hn (dOf t)) :=
  sorry

end QOU.BraidKnot.DominanceIsBruhat
