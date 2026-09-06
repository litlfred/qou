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

The `iff` is therefore **split** below into its two implications, so the reachable half is not
held hostage to the blocked one.

## 🛑 THE SOURCE'S INDUCTIVE STEP DOES NOT CLOSE — measured, not suspected

The paragraph above said the forward half was "unblocked" and that what remained was
"purely the tableau combinatorics".  The Coxeter side **is** supplied, and the handedness
trap it warned about **is** closed (`BruhatReflection.LeftReflStep` / `LeftReflLe` /
`bruhatLe_of_leftReflLe_An`, this branch, sorry-free).  What is *not* true is that Mathas'
argument transcribes.

Mathas' proof, from the source verbatim:

> First suppose that `s ▷ t` and choose `r` minimal such that row `r` of `s` and row `r` of
> `t` are different.  Let `a` be the smallest number which is in row `r` of `s` but not in
> row `r` of `t`; similarly, let `b` be the smallest number which is in row `r` of `t` but
> not in row `r` of `s`.  Then `a < b` since `s ▷ t`.  Therefore, if `v = t(a,b)` then
> `v ▷ t` and `d(v) ▷ d(t)`.  Further, if `a` is in row `t` of `t` and `b` is in row `s` of
> `s` then `t > r` and `t ≥ s`; so, either `v = s` or `s ▷ v`.  Therefore, by induction,
> `d(s) ⊵ d(v)`; so `d(s) ⊵ d(t)` as required.

[`dipper_james_forward_step_probe.py`](../../../../../computations/hecke/dipper_james_forward_step_probe.py)
measures each clause of that separately.  At `n = 6`, over all 142 314 ordered pairs of
row-standard tableaux with `s ▷ t` strictly:

| clause | | |
|---|---|---|
| `a < b` | 142314/142314 | ok |
| `v ▷ t` strictly | 142314/142314 | ok |
| `d(v) ≤ d(t)` (subword Bruhat) | 142314/142314 | ok |
| the raw swap is row standard | 129833/142314 | **91.2 %** |
| `v` is one LEFT reflection step below `t` | 129833/142314 | **91.2 %** |
| **`s ⊵ v`** | 112096/142314 | **78.8 %** |
| some transposition does all of it | 142314/142314 | ok |

**`s ⊵ v` is the substantive failure.**  The justification Mathas gives for it is
`ℓ_t(a) ≥ ℓ_s(b)` — `a`'s row in `t` at or below `b`'s row in `s` — and that is the
condition which *produces* the overshoot rather than preventing it: swapping sends `b` to
`a`'s row in `t`, i.e. at or below where `s` puts it.  Smallest instance, verified by hand
and by probe:

    λ = (2,1,1)
    s = ((1,2),(4),(3))      t = ((1,4),(3),(2))      s ▷ t
    r = 0,  a = 2,  b = 4,  a < b
    v = t(2,4) = ((1,2),(3),(4))
    v ▷ t  ✓   but   s ⊵ v  is FALSE — at i = 1, m = 3 the counts are s : 2, v : 3

The two 91.2 % rows fail together and cost less: when the raw swap leaves a row unsorted,
`v` is still the correct *tabloid* but is no longer `(a,b) · t` as a *tableau*, so the
single-step route through `bruhatLe_of_leftReflLe_An` is unavailable for those pairs.  The
relation `d(v) ≤ d(t)` holds throughout regardless.

### This is a repair, not a refutation — and the difference is measured

The last row is why.  For **every** such pair there exists a transposition meeting all of
Mathas' conditions at once — raw swap row standard, `s ⊵ v ▷ t`, `d(v) = (a,b) · d(t)`,
length down.  So the *strategy* is sound and only the *selection rule* is wrong: what a
Lean proof needs is a correct rule, not a different induction.

Nor is this a claim against Mathas.  **3.7 itself is measured true**, in both directions,
708 062/708 062 on the same range.  The source is OCR, and the sentence carrying the failing
clause prints its two **row indices** as `s` and `t` — the same glyphs as the two tableaux —
so a transcription error in either direction is entirely possible.  What is established is
that *the argument as this corpus can read it does not close*, which is a reason not to
write Lean against it.

### Rules already measured — do not re-try these

Hits against the brute-force valid set at `n = 6`, out of 142 314: Mathas' own **102 404**
(71.9 %), `lowrow` 95 044, `deep` 98 448, `a_bmin` 111 474, `bmax_a` **119 640** (84.1 %,
best measured).  Both `b`-side repairs beat both `a`-side ones, which is the one structural
hint the search produced: Mathas' `b` — least in row `r` of `t` but *not* in row `r` of `s` —
is the wrong constraint, and the valid set repeatedly wants a `b` that **is** in row `r` of
`s`, which his definition can never return.  A per-element "do not overshoot" criterion is
ruled out: the valid set contains steps sending a label *below* the row `s` puts it in,
because dominance is a global count comparison.

Tracked as bean **`qou-f3mc`**.  What remains free and is not in doubt: swapping two labels
**is** the group action (`TableauPerm.dOf_smul`, `dOf (Equiv.swap a b • t) = Equiv.swap a b *
dOf t`, verified), the handedness bridge is landed, and
`DominanceWellFounded.domGtOn_wellFounded` supplies the induction's measure.
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

**The forward half of 3.7** — dominance implies Bruhat.

`domRel a b` reads "`a` is dominated by `b`", so `domRel ⟦t⟧ ⟦s⟧` is "`s` dominates `t`".
The Bruhat side is `d(s) ≤ d(t)` — **reversing**; see the module docstring, and
`refTab_dOf_bruhatLe` for the fact that forces it.

**Stated, not proved — and NOT for want of Coxeter machinery.**  The Coxeter side is
supplied (`BruhatReflection.bruhatLe_of_leftReflLe_An`, hypothesis-free in type A, with the
left/right handedness bridge landed alongside it).  What blocks this is the **tableau**
side: Mathas' selection rule for the inductive step's transposition is wrong, measured at
**78.8 %** on its `s ⊵ v` clause over 142 314 pairs at `n = 6`.  A correct rule exists —
some transposition works for **every** pair, 142 314/142 314 — but none of the five rules
tried finds it.  See the module docstring for the per-clause table and the smallest
counterexample; tracked as bean `qou-f3mc`.

The **statement** is not in doubt: measured exhaustively over every ordered pair of
row-standard tableaux of every partition of `n ≤ 6`, **708 062/708 062**, under both
definitions of the Bruhat order. -/
-- Ref: [dipper-james1986] Dipper & James, *Blocks and idempotents of Hecke algebras of
-- general linear groups*, Proc. LMS (3) 54 (1987) 57-82; and [mathas1999] Mathas,
-- *Iwahori-Hecke algebras and Schur algebras of the symmetric group*, Proposition 3.7.
theorem dominance_to_bruhatLe (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    {s t : QOU.BraidKnot.Specht.Tableau μ}
    (_hs : QOU.BraidKnot.RowStandardTableau.IsRowStandard s)
    (_ht : QOU.BraidKnot.RowStandardTableau.IsRowStandard t)
    (_hdom : domRel (QOU.BraidKnot.Specht.Tabloid.mk t)
      (QOU.BraidKnot.Specht.Tabloid.mk s)) :
    QOU.Machinery.CoxeterBruhat.BruhatLe (permCoxeterSystem n)
      (toFinSucc hn (dOf s)) (toFinSucc hn (dOf t)) :=
  sorry

/-- **The converse half of 3.7** — Bruhat implies dominance.

**Blocked on a named, tracked Coxeter obligation, not on the tableau side.**  Mathas' argument
here goes through the *reflection* order (`d(t) = d(s)·τ` with `ℓ` up by one, then read off
`s ▷ t` from the definitions), so it needs **`BruhatLe → ReflLe`** — the direction #6894 left
open as bean **`qou-3k66`**, whose own summary names it as *"what a consumer citing Mathas'
Prop 3.7 needs for an `↔`"*.  This is that consumer.

`IwahoriHecke.BruhatReflection` proves the other direction (`bruhatLe_of_reflLe`, and
`bruhatLe_of_reflLe_An` hypothesis-free for type A), which is why
`dominance_to_bruhatLe` above is unblocked and this one is not. -/
-- Ref: [dipper-james1986]; [mathas1999] Proposition 3.7.  Blocked on `qou-3k66`
-- (`BruhatLe → ReflLe`), open in `QOU/IwahoriHecke/BruhatReflection.lean`.
theorem bruhatLe_to_dominance (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    {s t : QOU.BraidKnot.Specht.Tableau μ}
    (_hs : QOU.BraidKnot.RowStandardTableau.IsRowStandard s)
    (_ht : QOU.BraidKnot.RowStandardTableau.IsRowStandard t)
    (_hbr : QOU.Machinery.CoxeterBruhat.BruhatLe (permCoxeterSystem n)
      (toFinSucc hn (dOf s)) (toFinSucc hn (dOf t))) :
    domRel (QOU.BraidKnot.Specht.Tabloid.mk t)
      (QOU.BraidKnot.Specht.Tabloid.mk s) :=
  sorry

/-- **Dipper–James 3.7**, assembled from its two halves.

This declaration itself contains **no `sorry`** — it is the conjunction of
`dominance_to_bruhatLe` and `bruhatLe_to_dominance`, and inherits exactly their status.  It is
stated separately so that a consumer needing only one implication is not made to depend on
the blocked one: the forward half is unblocked (see its docstring), the converse waits on
`qou-3k66`. -/
theorem dominance_iff_bruhatLe (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    {s t : QOU.BraidKnot.Specht.Tableau μ}
    (hs : QOU.BraidKnot.RowStandardTableau.IsRowStandard s)
    (ht : QOU.BraidKnot.RowStandardTableau.IsRowStandard t) :
    domRel (QOU.BraidKnot.Specht.Tabloid.mk t) (QOU.BraidKnot.Specht.Tabloid.mk s)
      ↔ QOU.Machinery.CoxeterBruhat.BruhatLe (permCoxeterSystem n)
          (toFinSucc hn (dOf s)) (toFinSucc hn (dOf t)) :=
  ⟨dominance_to_bruhatLe hn hs ht, bruhatLe_to_dominance hn hs ht⟩

end QOU.BraidKnot.DominanceIsBruhat
