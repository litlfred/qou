import QOU.BraidKnot.TableauPerm
import QOU.BraidKnot.RowStandardTableau
import QOU.BraidKnot.SpechtDominanceCore
import QOU.Machinery.CoxeterBruhat
import QOU.Hecke.SymmetricCoxeter
import QOU.BraidKnot.SytRowSuperstandard
import QOU.Machinery.BruhatRankCriterion

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
* **converse** (`d(s) ≤ d(t) → s ⊵ t`) appeared to need **`BruhatLe → ReflLe`** — bean
  **`qou-3k66`**, which #6894's own "left open" section names as *"what a consumer citing
  Mathas' Prop 3.7 needs for an `↔`"*, this file being that consumer.

**Both halves of that assessment turned out to be wrong, in opposite directions**, and the
sections below are the record: the forward half is *not* unblocked (its tableau step does not
close), and the converse *is* — by a route through rank matrices that never mentions the
reflection order.  **`bruhatLe_to_dominance` is proved.**

The `iff` is nonetheless still **split** below into its two implications, because only one of
them is closed.

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
| the raw swap is row standard | 129833/142314 | **91.2 %** — but see below |
| `v` is one LEFT reflection step below `t` | 129833/142314 | **91.2 %** — likewise |
| **`s ⊵ v`** | 112096/142314 | **78.8 %** |
| some transposition does all of it | 142314/142314 | ok |
| `d(rowsort(τ·t)) ≤ d(τ·t)`, over **every** τ | 2134710/2134710 | ok |

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

### The two 91.2 % rows **dissolve** — and the lemma that dissolves them is proved

When the raw swap leaves a row unsorted, `v` is still the correct *tabloid* but is no
longer `(a,b) · t` as a *tableau*, so the single-step route through
`bruhatLe_of_leftReflLe_An` is unavailable there.  That looked like a second obstruction.
It is not: `d(v)` is the **distinguished** (minimal-length) representative of the coset
`S_λ · d((a,b)·t)`, so `ℓ` is additive across that factorisation and a reduced word for
`d(v)` is a *prefix* of one for `d((a,b)·t)` — hence a subword.

That is `CoxeterBruhat.bruhatLe_of_length_add`, **proved sorry-free** alongside this file,
and the corpus's own unconditional Bourbaki lifting lemma
`CoxeterReflectionCocycle.length_minRep_mul_wordProd'` supplies its hypothesis.  Measured
first, over **every** transposition of every row-standard tableau rather than only the
chosen one: **2 134 710/2 134 710** at `n = 6`.

So the raw swap need not be row standard, and under the relaxed valid set that drops the
requirement, **`s ⊵ v` is the ONE remaining failing clause** — Mathas' rule then scores
exactly the `s ⊵ v` count, 112 096/142 314.

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

Hits against the **relaxed** valid set at `n = 6`, out of 142 314 — seven rules, the last
four written after the coset bound retired the row-standardness requirement:

| rule | | |
|---|---|---|
| Mathas | 112 096 | 78.8 % (= the `s ⊵ v` count exactly) |
| `lowrow` | 107 740 | 75.7 % |
| `deep` | 109 684 | 77.1 % |
| `a_bmin` | 113 374 | 79.7 % |
| `minlift` | 118 814 | 83.5 % |
| `lift1b` | 123 121 | 86.5 % |
| **`bmax_a`** | **124 391** | **87.4 %** — best measured, still not a rule |

Two structural hints, both negative.  **Mathas' `b` is the wrong constraint** — least in row
`r` of `t` but *not* in row `r` of `s`, while the valid set repeatedly wants a `b` that
**is** in row `r` of `s`, which his definition can never return; both `b`-side repairs beat
both `a`-side ones.  And **a per-element "do not overshoot" criterion is ruled out in both
directions**: `minlift` lifts the least misplaced label as high as it can go and overshoots,
`lift1b` lifts it one row and undershoots, the valid set contains steps sending a label
*below* the row `s` puts it in, and some pairs' only valid steps do not move the least
misplaced label at all.  Dominance is a global count comparison, not a per-label one.

Tracked as bean **`qou-f3mc`**.

## 🟩 THE TRANSPOSITION INDUCTION IS THE WRONG ROUTE — and the converse half is unblocked

The negative above ("no rule that names a label can be right") points somewhere specific,
and the destination is measured in
[`dipper_james_rank_criterion_probe.py`](../../../../../computations/hecke/dipper_james_rank_criterion_probe.py).
Write `rank(u, i, m) = #{x < i : u(x) < m}` and let `N_i = μ₀ + ⋯ + μ_i` be the **row
boundaries**.  Then, at `n ≤ 6`, all four of:

| | | |
|---|---|---|
| `s ⊵ t` ⟺ the rank inequality at the **boundaries** `N_i` | 708062/708062 | ok |
| `u ≤ w` ⟺ the rank inequality at **every** `i` (Ehresmann) | 708062/708062 | ok |
| boundary ⟹ full, for `d`-images | 143916/143916 | ok |
| full ⟹ boundary (specialisation) | 143916/143916 | ok |

The first is an **identity**, not a coincidence.  `d(t)` sends a reference label to `t`'s
label at the same cell and `refTab` is row-superstandard, so the row of `y` in `t` is the
block of `d(t)⁻¹(y)`, whence

    domCount (rowPattern t) i m = #{x < N_i : d(t) x < m} = rank (d t) N_i m.

**Dominance on tabloids IS a rank comparison on permutations, read only at the row
boundaries.**  So 3.7 carries no tableau content at all: both sides compare the rank
matrices of the *same two permutations*, and the entire difference is *"at the boundaries"*
versus *"at every index"* — reconciled by `d` being a **minimal coset representative**,
which is increasing within each block and therefore has its rank function determined by
interpolation.

### What that changes for each half

* **Converse — no longer blocked on `qou-3k66`.**
  `d(s) ≤ d(t)` ⟹ full rank (the **easy** direction of Ehresmann: a subword can only raise
  the rank matrix, an induction on deletions from the subword *definition*) ⟹ boundary rank
  **by specialisation** ⟹ `s ⊵ t`.  No reflection order appears anywhere in that chain, so
  `bruhatLe_to_dominance`'s recorded blocker is not a blocker on this route.  Its docstring
  It is now **proved** on exactly this route: `rk_le_of_bruhatLe` (easy Ehresmann,
  `Machinery/BruhatRankCriterion`), then `rankAt_eq_rk` to specialise to the row cuts, then
  `domRel_iff_rankAt`.  `qou-3k66` stays open on its own merits.
* **Forward — re-scoped, not unblocked.**  It still needs the **hard** direction of
  Ehresmann (rank criterion ⟹ subword), plus the interpolation bridge.  But that is a named
  classical theorem with a known proof (Björner–Brenti Thm 2.1.5) in place of a tableau
  selection rule that seven attempts failed to find, which is a better place to be stuck.

What remains free and is not in doubt: swapping two labels **is** the group action
(`TableauPerm.dOf_smul`, verified), the handedness bridge is landed, the coset-minimality
bridge is proved (`CoxeterBruhat.bruhatLe_of_length_add`), and
`DominanceWellFounded.domGtOn_wellFounded` supplies a measure should any induction still be
wanted.
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

/-! ### Dominance is a rank comparison — the tableaux come out of the statement

The measured reduction in the module docstring, made precise.  `rowPattern_dOf` is the whole
of it; everything below is reindexing along the bijection `dOf t`. -/

/-- **The key identity**: `d(t)` transports `t`'s row pattern back to the *reference*
tableau's.

`dOf t x = t⁻¹(refTab x)`, so `t` sends `dOf t x` to the cell `refTab` assigns to `x`, and
the row of that cell does not mention `t` at all.  Two lines, and it is the reason 3.7 has
no tableau content: the row of a label in `t` is the row of its `d(t)`-preimage in the
reference tableau. -/
theorem rowPattern_dOf (t : QOU.BraidKnot.Specht.Tableau μ)
    (x : Fin (QOU.BraidKnot.Specht.nOf μ)) :
    QOU.BraidKnot.Specht.rowPattern t (dOf t x)
      = QOU.BraidKnot.Specht.rowPattern (refTab μ) x := by
  simp [QOU.BraidKnot.Specht.rowPattern, dOf_apply]

/-- **The rank matrix of `d(t)`**, cut by the reference tableau's rows: the number of labels
`x` that `refTab` puts in row `≤ i` and `d(t)` sends below `m`.

Stated against `rowPattern (refTab μ) x ≤ i` rather than against a numeric row boundary
`x < μ₀ + ⋯ + μ_i`.  The two agree — `refTab` is row-superstandard — but that equality is a
separate fact about the reference tableau, and nothing below needs it. -/
noncomputable def rankAt (t : QOU.BraidKnot.Specht.Tableau μ) (i m : ℕ) : ℕ :=
  (Finset.univ.filter fun x : Fin (QOU.BraidKnot.Specht.nOf μ) =>
    QOU.BraidKnot.Specht.rowPattern (refTab μ) x ≤ i
      ∧ ((dOf t x : Fin (QOU.BraidKnot.Specht.nOf μ)) : ℕ) < m).card

/-- **The dominance count IS the rank matrix.**  Reindexing the `domCount` filter along the
bijection `dOf t` and applying `rowPattern_dOf`. -/
theorem domCount_eq_rankAt (t : QOU.BraidKnot.Specht.Tableau μ) (i m : ℕ) :
    domCount (tabloidRowPattern (QOU.BraidKnot.Specht.Tabloid.mk t)) i m = rankAt t i m := by
  rw [tabloidRowPattern_mk, domCount, rankAt]
  refine (Finset.card_equiv (dOf t) ?_).symm
  intro x
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  rw [rowPattern_dOf]
  exact and_comm

/-- **Dominance restated with no tableaux in it**: `s ⊵ t` is exactly the rank inequality
between `d(s)` and `d(t)`, read at the reference tableau's row cuts.

This is the left-hand column of 3.7.  The right-hand column — the Bruhat order — is the
*same* inequality read at **every** index rather than only at the row cuts (Ehresmann's
criterion), and the two are reconciled by `d` being a minimal coset representative.  See the
module docstring for the measurement and for what each half of 3.7 then needs. -/
theorem domRel_iff_rankAt (s t : QOU.BraidKnot.Specht.Tableau μ) :
    domRel (QOU.BraidKnot.Specht.Tabloid.mk t) (QOU.BraidKnot.Specht.Tabloid.mk s)
      ↔ ∀ i m : ℕ, rankAt t i m ≤ rankAt s i m := by
  constructor
  · intro h i m
    rw [← domCount_eq_rankAt, ← domCount_eq_rankAt]
    exact h i m
  · intro h i m
    rw [domCount_eq_rankAt, domCount_eq_rankAt]
    exact h i m

/-! ### The two bridges to `Machinery.BruhatRankCriterion`

`rankAt` cuts by the reference tableau's ROW PATTERN and lives on `Fin (nOf μ)`;
`BruhatRank.rk` cuts by a NUMERIC index and lives on `Fin (n+1)`.  Two lemmas reconcile
them, and both are bookkeeping: the reference tableau is row-superstandard, so its row cut
is the initial segment ending at `rowPrefix μ (i+1)`; and `toFinSucc` is a value-preserving
relabelling. -/

/-- **The row cut is an initial segment.**  `refTab` is row-superstandard, so a label lies
in row `≤ i` exactly when it is below the cumulative row length `rowPrefix μ (i + 1)`.

This is the fact `rankAt` was deliberately stated *without*, so that everything up to here
stayed independent of the reference tableau's shape. -/
theorem rowPattern_refTab_le_iff (i : ℕ) (x : Fin (QOU.BraidKnot.Specht.nOf μ)) :
    QOU.BraidKnot.Specht.rowPattern (refTab μ) x ≤ i
      ↔ (x : ℕ) < QOU.BraidKnot.rowPrefix μ (i + 1) := by
  set c : μ.cells := refTab μ x with hc
  have hmem : (((c : ℕ × ℕ).1, (c : ℕ × ℕ).2) : ℕ × ℕ) ∈ μ := by simp
  have hcell :
      (⟨((c : ℕ × ℕ).1, (c : ℕ × ℕ).2), (YoungDiagram.mem_cells _).2 hmem⟩ : μ.cells) = c := by
    apply Subtype.ext; simp
  have hx : (x : ℕ)
      = QOU.BraidKnot.rowPrefix μ (c : ℕ × ℕ).1 + (c : ℕ × ℕ).2 := by
    have h := refTab_symm_apply (μ := μ) hmem
    rw [hcell, hc, Equiv.symm_apply_apply] at h
    rw [hc]
    exact h
  have hj : (c : ℕ × ℕ).2 < μ.rowLen (c : ℕ × ℕ).1 := YoungDiagram.mem_iff_lt_rowLen.mp hmem
  have hrow : QOU.BraidKnot.Specht.rowPattern (refTab μ) x = (c : ℕ × ℕ).1 := rfl
  rw [hrow]
  constructor
  · intro hle
    have h1 : QOU.BraidKnot.rowPrefix μ ((c : ℕ × ℕ).1 + 1)
        ≤ QOU.BraidKnot.rowPrefix μ (i + 1) := QOU.BraidKnot.rowPrefix_mono μ (by omega)
    rw [QOU.BraidKnot.rowPrefix_succ] at h1
    omega
  · intro hlt
    by_contra hgt
    have hle : i + 1 ≤ (c : ℕ × ℕ).1 := by omega
    have h2 := QOU.BraidKnot.rowPrefix_mono μ hle
    omega

/-- **`rankAt` IS `BruhatRank.rk`**, at the cut `rowPrefix μ (i + 1)` and after the
value-preserving relabelling `toFinSucc`. -/
theorem rankAt_eq_rk (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    (t : QOU.BraidKnot.Specht.Tableau μ) (i m : ℕ) :
    rankAt t i m
      = QOU.Machinery.BruhatRank.rk (toFinSucc hn (dOf t))
          (QOU.BraidKnot.rowPrefix μ (i + 1)) m := by
  rw [rankAt, QOU.Machinery.BruhatRank.rk_eq_card]
  refine Finset.card_equiv (finCongr hn) ?_
  intro x
  simp only [Finset.mem_filter, Finset.mem_univ, true_and, rowPattern_refTab_le_iff]
  constructor
  · rintro ⟨h1, h2⟩
    refine ⟨by simpa using h1, ?_⟩
    simpa [toFinSucc, Equiv.permCongr_apply] using h2
  · rintro ⟨h1, h2⟩
    refine ⟨by simpa using h1, ?_⟩
    simpa [toFinSucc, Equiv.permCongr_apply] using h2

/-! ### Row-standardness enters: `d(t)` increases across each row block

`rk_le_of_endpoints` (in `Machinery/BruhatRankCriterion`) turns a rank inequality at the two
ENDPOINTS of a window into one at every index inside it, provided the dominated permutation
increases across the window.  This section supplies that hypothesis for `dOf t`.

**This is where row-standardness finally does work.**  It is unused in
`bruhatLe_to_dominance` above -- the converse holds for arbitrary tableaux -- and
`dOf_increasingOn_block` is the lemma that needs it: `dOf t x = t.symm (refTab x)` is the
label `t` puts in the cell `refTab` assigns to `x`, and within one row those labels increase
exactly when `t` is row standard.

Measured first, over every row-standard tableau of every partition of `n <= 6`: 1602/1602 at
`n = 6` (`run_c` in `computations/hecke/dipper_james_rank_criterion_probe.py`). -/

theorem colPattern_dOf (t : QOU.BraidKnot.Specht.Tableau μ) (x : Fin (QOU.BraidKnot.Specht.nOf μ)) :
    QOU.BraidKnot.Specht.colPattern t (dOf t x) = QOU.BraidKnot.Specht.colPattern (refTab μ) x := by
  simp [QOU.BraidKnot.Specht.colPattern, dOf_apply]

theorem refTab_val_eq (x : Fin (QOU.BraidKnot.Specht.nOf μ)) :
    (x : ℕ) = QOU.BraidKnot.rowPrefix μ (QOU.BraidKnot.Specht.rowPattern (refTab μ) x)
        + QOU.BraidKnot.Specht.colPattern (refTab μ) x := by
  set c : μ.cells := refTab μ x with hc
  have hmem : (((c : ℕ × ℕ).1, (c : ℕ × ℕ).2) : ℕ × ℕ) ∈ μ := by simp
  have hcell :
      (⟨((c : ℕ × ℕ).1, (c : ℕ × ℕ).2), (YoungDiagram.mem_cells _).2 hmem⟩ : μ.cells) = c := by
    apply Subtype.ext; simp
  have h := refTab_symm_apply (μ := μ) hmem
  rw [hcell, hc, Equiv.symm_apply_apply] at h
  exact h

theorem colPattern_refTab_lt (x : Fin (QOU.BraidKnot.Specht.nOf μ)) :
    QOU.BraidKnot.Specht.colPattern (refTab μ) x < μ.rowLen (QOU.BraidKnot.Specht.rowPattern (refTab μ) x) := by
  set c : μ.cells := refTab μ x with hc
  have hmem : (((c : ℕ × ℕ).1, (c : ℕ × ℕ).2) : ℕ × ℕ) ∈ μ := by simp
  exact YoungDiagram.mem_iff_lt_rowLen.mp hmem

theorem rowPattern_refTab_eq_of_block {r : ℕ} (x : Fin (QOU.BraidKnot.Specht.nOf μ))
    (h1 : QOU.BraidKnot.rowPrefix μ r ≤ (x : ℕ)) (h2 : (x : ℕ) < QOU.BraidKnot.rowPrefix μ (r + 1)) :
    QOU.BraidKnot.Specht.rowPattern (refTab μ) x = r := by
  have hle : QOU.BraidKnot.Specht.rowPattern (refTab μ) x ≤ r := (rowPattern_refTab_le_iff r x).mpr h2
  by_contra hne
  have hlt : QOU.BraidKnot.Specht.rowPattern (refTab μ) x < r := lt_of_le_of_ne hle hne
  have hv := refTab_val_eq x
  have hc := colPattern_refTab_lt x
  have hmono : QOU.BraidKnot.rowPrefix μ (QOU.BraidKnot.Specht.rowPattern (refTab μ) x + 1) ≤ QOU.BraidKnot.rowPrefix μ r :=
    QOU.BraidKnot.rowPrefix_mono μ (by omega)
  rw [QOU.BraidKnot.rowPrefix_succ] at hmono
  omega

theorem colPattern_refTab_eq_of_block {r : ℕ} (x : Fin (QOU.BraidKnot.Specht.nOf μ))
    (h1 : QOU.BraidKnot.rowPrefix μ r ≤ (x : ℕ)) (h2 : (x : ℕ) < QOU.BraidKnot.rowPrefix μ (r + 1)) :
    QOU.BraidKnot.Specht.colPattern (refTab μ) x = (x : ℕ) - QOU.BraidKnot.rowPrefix μ r := by
  have hr := rowPattern_refTab_eq_of_block x h1 h2
  have hv := refTab_val_eq x
  rw [hr] at hv
  omega

theorem dOf_increasingOn_block {t : QOU.BraidKnot.Specht.Tableau μ}
    (ht : QOU.BraidKnot.RowStandardTableau.IsRowStandard t)
    (hn : QOU.BraidKnot.Specht.nOf μ = n + 1) (r : ℕ) :
    QOU.Machinery.BruhatRank.IncreasingOn (toFinSucc hn (dOf t)) (QOU.BraidKnot.rowPrefix μ r) (QOU.BraidKnot.rowPrefix μ (r + 1)) := by
  intro X Y haX hXY hYb
  have hx1 : QOU.BraidKnot.rowPrefix μ r ≤ ((finCongr hn).symm X : ℕ) := by simpa using haX
  have hy2 : (((finCongr hn).symm Y : Fin (QOU.BraidKnot.Specht.nOf μ)) : ℕ) < QOU.BraidKnot.rowPrefix μ (r + 1) := by
    simpa using hYb
  have hx2 : (((finCongr hn).symm X : Fin (QOU.BraidKnot.Specht.nOf μ)) : ℕ) < QOU.BraidKnot.rowPrefix μ (r + 1) := by
    have : (((finCongr hn).symm X : Fin (QOU.BraidKnot.Specht.nOf μ)) : ℕ)
        < (((finCongr hn).symm Y : Fin (QOU.BraidKnot.Specht.nOf μ)) : ℕ) := by simpa using hXY
    omega
  have hy1 : QOU.BraidKnot.rowPrefix μ r ≤ (((finCongr hn).symm Y : Fin (QOU.BraidKnot.Specht.nOf μ)) : ℕ) := by
    have : (((finCongr hn).symm X : Fin (QOU.BraidKnot.Specht.nOf μ)) : ℕ)
        < (((finCongr hn).symm Y : Fin (QOU.BraidKnot.Specht.nOf μ)) : ℕ) := by simpa using hXY
    omega
  set x : Fin (QOU.BraidKnot.Specht.nOf μ) := (finCongr hn).symm X with hxd
  set y : Fin (QOU.BraidKnot.Specht.nOf μ) := (finCongr hn).symm Y with hyd
  have hrow : QOU.BraidKnot.Specht.rowPattern t (dOf t x) = QOU.BraidKnot.Specht.rowPattern t (dOf t y) := by
    rw [rowPattern_dOf, rowPattern_dOf,
      rowPattern_refTab_eq_of_block x hx1 hx2, rowPattern_refTab_eq_of_block y hy1 hy2]
  have hcol : QOU.BraidKnot.Specht.colPattern t (dOf t x) < QOU.BraidKnot.Specht.colPattern t (dOf t y) := by
    rw [colPattern_dOf, colPattern_dOf,
      colPattern_refTab_eq_of_block x hx1 hx2, colPattern_refTab_eq_of_block y hy1 hy2]
    have : (x : ℕ) < (y : ℕ) := by simpa [hxd, hyd] using hXY
    omega
  have hlt : dOf t x < dOf t y := ht _ _ hrow hcol
  simpa [toFinSucc, Equiv.permCongr_apply, hxd, hyd] using hlt

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

/-- **The converse half of 3.7 — PROVED, and it never needed `qou-3k66`.**

Mathas' own argument for this direction goes through the *reflection* order (`d(t) = d(s)·τ`
with `ℓ` up by one), which is why the corpus recorded it as blocked on **`BruhatLe → ReflLe`**
— bean `qou-3k66`, whose own summary names it as *"what a consumer citing Mathas' Prop 3.7
needs for an `↔`"*.  **That route is not the only one.**  The chain used here is

    d(s) ≤ d(t)  →  rank inequality      (`BruhatRank.rk_le_of_bruhatLe`, the EASY half of
                                          Ehresmann's criterion, proved straight from the
                                          SUBWORD definition — no reflection order at all)
                 →  at the row cuts      (specialisation, `rankAt_eq_rk`)
                 →  s ⊵ t                (`domRel_iff_rankAt`)

so `qou-3k66` stays open on its own merits and 3.7 is no longer a reason to prioritise it.

**The row-standardness hypotheses are not used**, and that is a real observation rather than
an oversight: `domRel` is a relation on *tabloids* and `dOf` is a bijection on *all*
tableaux, so this implication holds for arbitrary `μ`-tableaux.  They are kept in the
signature because 3.7 as stated in the source quantifies over row-standard tableaux and the
forward half does need them. -/
-- Ref: [dipper-james1986]; [mathas1999] Proposition 3.7.
theorem bruhatLe_to_dominance (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    {s t : QOU.BraidKnot.Specht.Tableau μ}
    (_hs : QOU.BraidKnot.RowStandardTableau.IsRowStandard s)
    (_ht : QOU.BraidKnot.RowStandardTableau.IsRowStandard t)
    (hbr : QOU.Machinery.CoxeterBruhat.BruhatLe (permCoxeterSystem n)
      (toFinSucc hn (dOf s)) (toFinSucc hn (dOf t))) :
    domRel (QOU.BraidKnot.Specht.Tabloid.mk t)
      (QOU.BraidKnot.Specht.Tabloid.mk s) := by
  rw [domRel_iff_rankAt]
  intro i m
  rw [rankAt_eq_rk hn, rankAt_eq_rk hn]
  exact QOU.Machinery.BruhatRank.rk_le_of_bruhatLe hbr _ m

/-- **Dipper–James 3.7**, assembled from its two halves.

This declaration itself contains **no `sorry`** — it is the conjunction of
`dominance_to_bruhatLe` and `bruhatLe_to_dominance`, and inherits exactly their status.
**The converse half is proved; the forward half is not**, so a consumer that needs only
`d(s) ≤ d(t) → s ⊵ t` should cite `bruhatLe_to_dominance` directly rather than this `iff`,
which is `sorry`-carrying through its other half.  See each half's own docstring. -/
theorem dominance_iff_bruhatLe (hn : QOU.BraidKnot.Specht.nOf μ = n + 1)
    {s t : QOU.BraidKnot.Specht.Tableau μ}
    (hs : QOU.BraidKnot.RowStandardTableau.IsRowStandard s)
    (ht : QOU.BraidKnot.RowStandardTableau.IsRowStandard t) :
    domRel (QOU.BraidKnot.Specht.Tabloid.mk t) (QOU.BraidKnot.Specht.Tabloid.mk s)
      ↔ QOU.Machinery.CoxeterBruhat.BruhatLe (permCoxeterSystem n)
          (toFinSucc hn (dOf s)) (toFinSucc hn (dOf t)) :=
  ⟨dominance_to_bruhatLe hn hs ht, bruhatLe_to_dominance hn hs ht⟩

end QOU.BraidKnot.DominanceIsBruhat
