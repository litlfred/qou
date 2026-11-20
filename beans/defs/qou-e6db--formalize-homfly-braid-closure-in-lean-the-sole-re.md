---
# qou-e6db
title: Formalize HOMFLY + braid closure in Lean — the sole residue of MFW (split from qou-9ttb)
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-22T19:25:24Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-0cyu
---

## Why this bean exists

Split out of `qou-9ttb` (Prove/Lean the two Morton-Franks-Williams inequalities)
when that bean's **mathematical** content was completed on 2026-08-22. Opening
this separately rather than leaving it as an open residue on a bean whose
mathematics is done — owner-authorised.

## What is already DONE (do not redo)

- **Propagation** — `QOU.Knot.MFWSkeinInduction.mfw_step` and the window
  arithmetic (`switch_shift`, `smooth_shift`, `shifts_preserve_width`, the
  surjectivity lemmas). Sorry-free. Lickorish's relation rearranges to
  `P₊ = v²·P₋ + v·z·P₀`; switching moves `e ↦ e−2`, smoothing `e ↦ e−1`, so the
  MFW window propagates by pure interval arithmetic.
- **Base case** — `DescendingWrithe` (`|e| ≤ n − c` for a totally descending
  word) is **classical, not open**: a descending diagram is an unlink
  (`lickorish1997`) and Bennequin's inequality `sl ≤ −χ` (`bennequin1983`) with
  `sl = e − n` and `χ = c` for the c-component unlink gives exactly `e ≤ n − c`;
  mirroring gives the other side. Not circular — Bennequin (1983) predates
  HOMFLY (1985) and MFW (1987) and its proof is contact-geometric. Verified
  empirically at 2592 words: 0 violations, tight, and HOMFLY depends only on `c`.
- **Wiring** — `toWitness` / `braid_bound_of_window` / `descending_witness`
  connect the induction to `QOU.Knot.MortonFranksWilliams.MFWWitness`, whose
  `mfw_lower` / `mfw_upper` fields ARE window membership. All `#print axioms`
  clean (propext / Classical.choice / Quot.sound; `toWitness` none).

## What is ACTUALLY open — and it is infrastructure, not mathematics

**Neither Lean file touches a real knot.** `MortonFranksWilliams` says so
itself: *"the file asserts nothing about any actual knot."* Both files are
arithmetic over `ℤ` with the MFW bounds carried as hypotheses/fields. Nothing
can produce an `MFWWitness` from an actual link because there is no Lean
HOMFLY.

To close MFW in Lean one needs, roughly in order:

1. **Braid words + closure.** A `BraidWord n` type (`QOU/MathlibExt/BraidGroup.lean`
   exists — check what it already gives), the closure permutation, the component
   count `c`, and the exponent sum `e`.
2. **The descending predicate** and the reduction of an arbitrary word to a
   descending one by crossing changes, with a well-founded order. The corpus's
   own engine already descends such an order —
   `computations/homfly_skein_braid.py` (`first_bad` / `traverse`) — so the
   termination argument is available in executable form to port.
3. **HOMFLY itself**, as the skein-recursive invariant, plus its
   well-definedness (the hard part: invariance under Markov moves / Reidemeister
   moves).
4. **`mindeg_v` / `maxdeg_v`** and then the induction assembling `mfw_step` +
   `descending_witness` into MFW for all words.

Step 3 is the large one and is a genuine Mathlib-gap project — Mathlib has
neither HOMFLY nor the Jones polynomial. Consider whether it belongs under the
`08a2` keystone de-abstraction epic.

## Honest scoping

This is **not** a residue that a session can drain. It is a formalization
project on the scale of a Mathlib contribution. Anyone picking it up should
size it accordingly and should NOT represent partial progress as closing MFW.
The mathematics of MFW is settled classically; what is missing is Lean
infrastructure.


## Step 1 landed (2026-08-22) — closure permutation + component count

**The gap was real and specific.** `MFWSkeinInduction` states the window in terms
of `n`, `e`, `c`. `n` and `e` existed (`BraidKnot.BraidWord.writhe`); **`c` did
not exist anywhere in the Lean tree**, so no braid word could be connected to the
window it is supposed to satisfy. Now supplied in
`QOU/Knot/BraidClosure.lean` — sorry-free, zero linter warnings, all six results
axiom-clean (`propext` / `Classical.choice` / `Quot.sound`; `writhe_append` needs
only `propext`).

- `crossingSwap` — the transposition a crossing induces. **The sign is
  irrelevant**, which is the structural reason `c` is invariant under crossing
  changes while `e` moves; that is exactly what the skein induction needs.
- `closurePerm`, `closurePerm_nil/cons/append`
- `writhe_append` — additivity over concatenation
- `components` — orbits of `closurePerm` (nontrivial cycles + fixed points)
- `components_nil = n` — the identity braid closes to the n-component unlink

**Non-vacuity checked, not assumed.** A definition that type-checks can still
compute the wrong number, so `components` is pinned to known answers:
`components_two_one_crossing = 1` (one crossing on two strands closes to the
UNKNOT, not two circles — the smallest case where an off-by-one would hide) and
`components_two_two_crossings = 2`.

## FINDING — `BraidWord` is defined NINE times; this blocks the bean

Before adding anything I grepped, and the tree already defines `BraidWord` in
nine places across six namespaces: `PhotonThreading` (structure), four separate
`StandardModel` files (`WritheLevelParity`, `QuarkBraidChargeObstruction`,
`WritheMarkovInvariance`, `ChiralFermionBraidWords` — each `abbrev List ℤ`),
`Archimedean/NuclearGroebnerReduction` (`List ℕ`), `Archimedean/HeckeRep`
(`List (Fin (n-1) × Bool)`), `BraidKnot/BraidGroupNStrand`
(`List (BraidCrossing n)`), `BraidKnot/BraidWordBasisGram` (`List ℕ`), and
`KnotTheory` (structure). **`writhe` is defined at least five times, four of them
character-identical** (`(β.map Int.sign).sum`).

I built on `BraidKnot.BraidGroupNStrand.BraidWord` rather than adding a tenth: it
is the only one indexed by strand count AND carrying the crossing sign, which is
what MFW needs.

**This is a genuine obstacle to the bean, not a tidiness complaint.** HOMFLY must
be defined on ONE braid-word type or it cannot be connected to the MFW window,
the Markov trace (`MathlibExt/MarkovTrace` uses yet another), or the Hecke
representation. Consolidation should be scoped before step 3.

## Also checked, so it is not re-checked

`Knot/HomflySkeinReference.lean` exists but is **only the 2-strand skein value**
settling a mirror-convention dispute (bean `qou-7ue5`) — a numeric recursion
`skein : ℕ → R`, not a general HOMFLY. It does not advance steps 2-4.

## Next

Step 2 (the descending predicate + reduction to a descending word by crossing
changes, with a well-founded order). `computations/homfly_skein_braid.py`
(`first_bad` / `traverse`) already descends that order in executable form.


## Step 2 (partial) — the skein moves, proved on actual braid words

`MFWSkeinInduction.mfw_step` takes the window shifts as *arithmetic hypotheses*:
switching moves `e ↦ e-2`, smoothing `e ↦ e-1`, both keeping `n`. Nothing proved
a braid word actually **realises** those shifts. Now proved, sorry-free, zero
warnings, axiom-clean (`writhe_smooth` needs only `propext`):

- `crossingSwap_flipSign` / `closurePerm_switch` / `components_switch` —
  **switching a crossing does not move the permutation, hence not `c`.** This is
  the structural reason the induction works: `e` slides while `c` and `n` stay
  fixed, so the window translates without changing width.
- `writhe_switch` — switching moves the writhe by exactly `2`, signed by the
  crossing's original sign.
- `closurePerm_smooth` — smoothing removes exactly that transposition from the
  permutation, which is where `c` moves.
- `writhe_smooth` — smoothing moves the writhe by exactly `1`.

**What is still missing for step 2**: that multiplying by a transposition
changes the orbit count by exactly `±1` (so smoothing moves `c` by one), plus
the descending predicate itself and the well-founded reduction. The `±1` fact is
the next concrete target and is a standard permutation-combinatorics lemma —
check Mathlib for it before proving it by hand (`#check` against the oleans; the
cache carries no `.lean` source and the LSP is down, so name-grep does not work
in this container).


## Parity layer proved (2026-08-22)

The base-case measurement behind `MFWSkeinInduction` found `|e|` and `n - c`
always sharing a parity, with the bound tight whenever they agree. That is now
**proved**, not observed, and it is the structure that makes `|e| <= n - c` a
*same-parity, smaller-magnitude* statement rather than a bare inequality:

- `sign_closurePerm` — the closure permutation's sign is `(-1)^(crossing count)`.
  Each crossing is one transposition **whatever its sign**, the same
  sign-blindness that makes `c` invariant under switching.
- `length_parity_cycleType` — read through `Equiv.Perm.sign_of_cycleType`.
- `writhe_sub_length_even` — the writhe has the parity of the crossing count.
- `writhe_parity_cycleType` — the writhe's parity is fixed by the closure
  permutation's cycle data.

All sorry-free, zero warnings, axiom-clean. 23 results in the file now.

**Deliberate weakening, stated so it is not mistaken for the full result.** The
last theorem is phrased against `cycleType.sum + cycleType.card` rather than
`n - c`. Getting to the `n - c` form needs two pieces of `ℕ`-subtraction
bookkeeping I did not do: `support.card ≤ n` (easy — `Finset.card_le_univ` plus
`Fintype.card_fin`) and `cycleType.card ≤ support.card` (each cycle has length
≥ 2 and they are disjoint; **`Equiv.Perm.card_cycleType_le_card_support` does
NOT exist in Mathlib** — checked by `#check` — so it needs proving by hand).
Without the second, `components ≤ n` is not available and `(n : ℤ) - components`
cannot be formed cleanly. That is the next concrete target.

**Still missing for step 2 overall**: that a transposition changes the orbit
count by exactly `±1` (the magnitude half — this parity work is only the parity
half), the descending predicate, and the well-founded reduction.


## The `n - c` form landed — and the Mathlib gap was fillable

The previous entry recorded the parity theorem as deliberately weakened to
`cycleType` form, blocked on `cycleType.card ≤ support.card`, which Mathlib
does not have. **That gap is now filled, in a stronger form than needed:**

- `two_mul_card_cycleType_le_card_support` — **`2 * cycleType.card ≤
  support.card`**, i.e. every nontrivial cycle costs at least two points. Proved
  from `Multiset.card_nsmul_le_sum` + `Equiv.Perm.two_le_of_mem_cycleType`. This
  is a general permutation fact with nothing braid-specific in it; if it is
  wanted upstream it would go in `Mathlib.GroupTheory.Perm.Cycle.Type`.
- `card_cycleType_le_card_support`, `card_support_le`, `components_le`
  (`c ≤ n` — a closure has at most one component per strand), `n_sub_components`.
- **`writhe_parity`** — `Even (e - (n - c))`, the parity constraint in exactly
  the form the MFW window uses.

So the base-case bound `|e| ≤ n - c` is now known to be a *same-parity,
smaller-magnitude* statement, with the parity half **proved** rather than
measured. The tightness the probe found at `|e| = n - c` is the case where the
parities coincide.

All sorry-free, zero warnings, axiom-clean. 29 results in the file.

**One tactic note worth keeping** (cost a failed proof): in `writhe_parity`,
`Equiv.Perm.sum_cycleType` must be rewritten while still in `ℕ`. Running
`push_cast` first drives the cast inside the `Multiset.sum`
(`(Multiset.map Nat.cast cycleType).sum`) and severs the link to
`support.card`, after which `linarith` cannot close it.

**Still open for step 2**: the magnitude half — that a transposition changes the
orbit count by exactly `±1` — plus the descending predicate and the well-founded
reduction. This is the parity half only.


## CORRECTION — the ±1 orbit-count lemma is NOT needed

An earlier entry in this bean listed "a transposition changes the orbit count by
exactly ±1" as the next target and as a gap in step 2. **That was wrong, and I
am recording it rather than quietly dropping it**, because it would have cost
the next agent a session on a lemma the argument never uses.

Checked against the actual statement: `mfw_step` is quantified over `n`, `e`,
`d` only — **`c` never appears in the propagation step**. `c` enters solely in
`base_window_of_descending`, applied to the descending word *itself*. And the
descending word is reached from the original by **sign changes alone**, so it
carries the same `n` and the same `c`; only `e` moves. Nothing ever needs to
know how `c` responds to smoothing.

## What that does need, now proved

`components_switch` covered one crossing change. The reduction changes many, so
the load-bearing statement is that `c` is a function of the **generator sequence
alone**, blind to every sign at once:

- `gens` — the generator sequence, signs forgotten.
- `closurePerm_eq_of_gens_eq` — same generator sequence ⇒ same closure
  permutation, whatever the signs.
- `components_eq_of_gens_eq` — hence the same `c`.
- `length_eq_of_gens_eq` — and the same crossing count, leaving `e` as the only
  quantity the reduction moves.

Sorry-free, zero warnings, axiom-clean (`length_eq_of_gens_eq` needs only
`propext`). 33 results in the file.

## Remaining for step 2 — now a single item

The **descending predicate and the well-founded reduction**. That is genuinely
the hard part: it needs the closure traversal (which strand-position follows
which), and the termination argument that switching the first
first-met-as-under crossing makes progress. `computations/homfly_skein_braid.py`
(`first_bad` / `traverse`) already implements exactly this and terminates, so
the measure exists in executable form and is worth porting rather than
reinventing.


## Orientation pinned against the reference engine

Reading `homfly_skein_braid.py::traverse` to prepare the descending predicate
surfaced a convention mismatch worth settling **before** building on it, not
after.

`traverse` counts components by walking each strand around the closure — its
`comps` is the orbit count of the strand map, the same quantity `components`
defines. **But it composes crossings in the opposite order**: it applies
`word[0], word[1], …` in turn, whereas Lean's `f * g` is `f ∘ g`, so
`closurePerm` applies the *last* letter first.

The two differ by an inversion, not by an error — and inversion preserves cycle
type and support, so the component counts agree. Proved rather than asserted:

- `closurePerm_reverse` — reversing a word inverts its closure permutation (each
  crossing is an involution, so reversal *is* inversion).
- `components_reverse` — hence the same component count.

Worth the effort because this is exactly the class of mismatch that silently
produces a mirror: `qou-7ue5` is a case in this very repo where two places in
`computations/` disagreed about a HOMFLY by `v ↦ v⁻¹`. Harmless for `c`, but the
**order** is load-bearing once the traversal itself is formalised, so it is now
recorded in the file rather than waiting to be rediscovered.

35 results in the file, all sorry-free, zero warnings, axiom-clean.

## Remaining for step 2 — unchanged, and it is the hard part

The descending predicate and the well-founded reduction. Formalising `traverse`
means encoding: components taken in increasing order of least start position,
each walked around its cycle, with the global encounter order recorded so that
"first met as an under-crossing" is well defined. That is a substantial piece —
larger than any single increment landed so far — and should be scoped as such
rather than attempted as a quick follow-on.


## `stepOver` — the over/under atom of the traversal

The descending predicate is about which strand is met **over** and which
**under**. `closurePerm` already carried *where* a strand goes; this carries
*which of the two passes over*. Together they are the Lean analogue of the
reference engine's `_step`.

The convention is now **stated in the Lean rather than left implicit**: for
`σ_i` (positive) the strand entering at the lower position passes OVER. Sign
conventions here are not free — `qou-7ue5` is a case in this repo of two
`computations/` sites disagreeing about a HOMFLY by a mirror, and sections 2-3
of PR #5440 are its cleanup — so the two defining properties are proved:

- `stepOver_lo_ne_hi` — **the two strands of a crossing get opposite verdicts.**
  This is the defining property of a crossing and the reason each crossing
  contributes exactly one `over` and one `under` to the traversal, which is what
  makes "first met as an under-crossing" well posed.
- `stepOver_isSome_iff` — **a strand is involved exactly when the crossing moves
  it** (`crossingSwap c p ≠ p`). This ties the over/under data to `closurePerm`:
  encounters are recorded precisely at the positions the permutation does not
  fix.
- `stepOver_flipSign` — switching flips both verdicts. The counterpart of
  `closurePerm_switch`, which said the *positions* are untouched; together, a
  crossing change is exactly an exchange of over for under.

39 results in the file, sorry-free, zero warnings, axiom-clean.

## What remains, unchanged in size

The traversal proper: components taken in increasing order of least start
position, each walked around its cycle, with the **global encounter order**
recorded so "first met as an under-crossing" is well defined — then the
well-founded reduction. `stepOver` and `closurePerm` are its two atoms and are
now in place; the ordering and the termination argument are not, and that is
still the substantial piece.


## The lap layer — one strand's pass through the whole word

The traversal walks a strand around the closure; one *lap* is one pass through
the word. Both halves now exist:

- `lapStep` — where the strand ends up.
- `lapVerdicts` — what it met, as `List (Option Bool)` **indexed by crossing
  position** rather than a list of `(index, verdict)` pairs. The crossing index
  is then the list index, so no index arithmetic is needed anywhere; `none`
  means this strand was not one of the two at that crossing.
- `lapVerdicts_length` — exactly one verdict slot per crossing, which is what
  makes "the first crossing met as an under-crossing" expressible without
  separate bookkeeping.
- `lapStep_eq` — **a lap is the INVERSE of `closurePerm`**, since a lap applies
  the first letter first while `closurePerm`, being a product, applies the last
  first. This is the orientation `closurePerm_reverse` pinned earlier, now
  restated as an equation so it does not have to be re-derived at the use site.
- `lapStep_eq_self_iff` — a lap returns to its start exactly on the fixed points
  of the closure permutation (the strands that close up alone).
- `lapStep_flipSign_cons` — switching leaves the itinerary untouched.

44 results in the file, sorry-free, zero warnings, axiom-clean.

## What remains — the multi-lap ordering, and it is still the hard part

A lap is one trip around. The traversal needs **many** laps per component
(walking the whole cycle), components taken in increasing order of least start
position, with a **global** encounter order across all of it. That ordering is
what "first met as an under-crossing" quantifies over, and it is the piece with
the real difficulty: it needs a termination argument for the per-component walk
(the cycle is finite, so it terminates, but Lean needs that argument) and then
the well-founded reduction on top.

Nothing landed so far shrinks that. The atoms (`stepOver`, `closurePerm`) and
now the lap are in place; the ordering is not.


## Walking a component — the termination worry is avoidable

A lap is one trip through the word; a component is walked by taking laps until
the strand returns. Rather than loop-until-return, which would need its own
termination argument, **the lap count is supplied explicitly as the cycle
length** and closing up becomes a theorem:

- `cycleLen f p = orderOf (f.cycleOf p)` — and `orderOf f` would be **wrong**
  here, not merely suboptimal: it is the lcm over all cycles, so it walks short
  components round and round instead of once.
- `pow_cycleLen_apply` — **the walk closes up**, via
  `Equiv.Perm.cycleOf_pow_apply_self` + `pow_orderOf_eq_one`.
- `walk` / `walk_length` / `walk_zero` — the positions visited.
- `walk_sameCycle` — the walk stays inside its component, which is what makes it
  a *component* walk rather than an arbitrary itinerary.
- `walkVerdicts` / `walkVerdicts_length` — `k` laps of `m` crossings each; the
  encounter count is exactly `k * m`, the arithmetic the global ordering rests
  on.

49 results in the file, sorry-free, zero warnings, axiom-clean.

## What is left

Concatenating the component walks in the engine's order (components taken in
increasing order of least start position), then reading off, per crossing, which
of its **two** encounters comes first — that is the descending predicate. Then
the well-founded reduction.

The per-component termination worry is now **gone** (the count is explicit and
`pow_cycleLen_apply` closes it). What remains is the cross-component ordering
and the reduction's own well-foundedness — genuinely smaller than the piece
described two entries ago, but not small.


## Component ordering — the mutable `seen_start` set is not needed

The reference engine takes components "in increasing order of their smallest
starting position", implemented with a mutable `seen_start` set. That set has a
**stateless characterisation**: a position starts a component exactly when it is
the least position in its own cycle. Modelling it that way removes the state
entirely — the traversal becomes a filter over `Fin n` in the natural order,
which is both closer to a specification and far easier to reason about than a
fold carrying a visited-set.

- `IsLeader f p` — `p` is the least position in its cycle.
- `exists_leader` — **every position has a leader in its cycle**, so no
  component is skipped. (Least element of a nonempty finite set.)
- `leader_unique` — a cycle has **exactly one** leader, so no component is
  walked twice. Together these two are precisely what `seen_start` was doing,
  and they are theorems rather than an invariant of a loop.
- `traversalVerdicts` — the full traversal: every component, in increasing order
  of least position, each walked once.

53 results in the file, sorry-free, zero warnings, axiom-clean.

## What is left

The descending predicate itself: per crossing, which of its **two** encounters
in `traversalVerdicts` comes first. The list is now defined and ordered
correctly; what is missing is the indexing lemma — that each crossing index
appears exactly twice in `traversalVerdicts` — and then `Descending w` as "for
every crossing, the earlier of its two entries is `over`". After that, the
well-founded reduction, which is a separate argument.

The "exactly twice" lemma is the natural next target: it is what makes "first
of the two" well posed, and it is the traversal-level counterpart of
`stepOver_lo_ne_hi` (which gave opposite verdicts at a single crossing).


## "Exactly two strands meet each crossing" — PROVED

This was named as the next target last entry, and it is the fact that makes *the
first of a crossing's two encounters* well posed, hence what makes the
descending predicate definable at all.

- `lapVerdicts_getElem` — the indexing step: the `k`-th entry of a lap is the
  `k`-th crossing's verdict, evaluated at wherever the strand had reached after
  the first `k` crossings.
- `stepOver_isSome_iff_mem` — a strand is involved exactly when it sits at one
  of the two positions the crossing acts on.
- **`card_involved`** — for each crossing, exactly **2** starting positions are
  involved. The argument: the position a strand occupies just before crossing
  `k` is a *permutation* of its start (`lapStep_eq`), so the involved starts are
  the preimage of a two-element set, and injectivity plus `loIdx_ne_hiIdx` gives
  the two are distinct.

It is the traversal-level counterpart of `stepOver_lo_ne_hi`, which gave the two
strands *opposite* verdicts at a single crossing. Together: each crossing
contributes exactly one `over` and one `under` to the whole traversal.

56 results in the file, sorry-free, zero warnings, axiom-clean.

## What is left

`Descending w` itself — "for every crossing, the earlier of its two entries in
`traversalVerdicts` is `over`" — which is now a *definition* rather than a
research question, since both the ordering and the exactly-two fact are in
place. Then the well-founded reduction, which remains a separate argument and is
the last genuinely open piece of step 2.


## `Descending` is now a definition

- `lapsOf` — the traversal as a **list of laps** rather than pre-flattened.
  Every lap has one slot per crossing, so crossing `k`'s verdicts are the `k`-th
  *column*; flattening first would turn that projection into modular arithmetic
  on a global index for no gain.
- `length_of_mem_lapsOf` — every lap has length `w.length`, which is what makes
  the column well defined.
- `verdictsFor w k` — the `k`-th column with uninvolved strands dropped.
- **`Descending w`** — every crossing is first met as an over-crossing. This is
  the hypothesis the MFW base case is about, now a definition.
- `descending_nil` — the identity braid is descending (vacuously); the extreme
  case of the reduction.

58 results, sorry-free, zero warnings, axiom-clean.

## HONEST LIMIT — the two-entry structure is not yet discharged

`card_involved` counts the **starting positions** involved in crossing `k`:
exactly two. `verdictsFor` collects verdicts from the laps in `lapsOf`. To get
`(verdictsFor w k).length = 2` — which is what actually pins down "the first of
the two" — those must be identified: the laps in `lapsOf w` are exactly the `n`
laps `lapVerdicts w p`, one per `p : Fin n`.

That is the **partition fact**: the cycles of `closurePerm w`, each represented
once by its leader and walked its full length, cover `Fin n` exactly. True, and
the natural next lemma, but **not proved**. So `Descending` is at present a
well-formed definition whose two-entry structure rests on a fact still to be
discharged, and the file says so rather than leaving it implicit.

Next: the partition fact, then `(verdictsFor w k).length = 2`, then the
well-founded reduction.


## `cycleLen` validated as the component size

`cycleLen` was *defined* as `orderOf (f.cycleOf p)` because that is what makes
`pow_cycleLen_apply` come out. These confirm it is the **intended** quantity —
the number of strands in the component — rather than merely a number that
happens to close the walk:

- `cycleLen_of_fixed` — a strand that closes up alone needs one lap.
- `cycleLen_eq_card_support` — otherwise `cycleLen` is exactly the size of the
  component (`Equiv.Perm.isCycle_cycleOf` + `IsCycle.orderOf`). So the walk
  takes one lap per strand of the component, no more and no fewer.

That distinction matters: a definition chosen to make one lemma work is not
automatically the right object, and this is the check that it is.

60 results in the file, sorry-free, zero warnings, axiom-clean.

## Toward the partition fact

With `cycleLen` = component size, the partition fact reduces to: the components
(one leader each, by `exists_leader` + `leader_unique`) have sizes summing to
`n`. Mathlib ingredients located for the next step:
`Equiv.Perm.mem_support_cycleOf_iff`, `Equiv.Perm.SameCycle.exists_pow_eq`.

Also worth recording for whoever picks this up: **`exact?` works in this
container** (verified — it produced `(Equiv.Perm.cycleOf_eq_one_iff f).mpr h`).
Since the cache carries no Mathlib `.lean` source and the LSP is down,
`#check` and `exact?` against the oleans are the only name-discovery tools
available here, and both are worth reaching for before hand-proving anything.


## The PARTITION FACT is proved

Named as the blocker two entries ago; now discharged.

- `leaderOf` + `leaderOf_isLeader` / `leaderOf_sameCycle` — the leader
  assignment as a *function*, which is what turns "each cycle has one leader"
  into something summable.
- `leaderOf_eq_iff` — two positions share a leader exactly when they share a
  cycle, so **the fibres of `leaderOf` are precisely the components**.
- `card_fiber_leader` — a leader's fibre is its component, of size `cycleLen`.
  Two cases, the two shapes a component can have: a lone fixed strand, or a
  genuine cycle.
- **`sum_cycleLen_leaders`** — summing each leader's component size gives `n`.
  The components cover `Fin n` exactly.

66 results, sorry-free, zero warnings, axiom-clean.

## What is still missing, precisely

`sum_cycleLen_leaders` is the **Finset** statement. `lapsOf` is built from
`(List.finRange n).filter …`, so converting it into `(lapsOf w).length = n`
needs a **List/Finset bridge** — relating a `List.sum` over filtered `finRange`
to a `Finset.sum` over filtered `univ`. That is bookkeeping rather than
mathematics, but it is not done, and until it is, `(verdictsFor w k).length = 2`
is still not available.

**I removed a scaffold rather than commit it.** An intermediate version of
`lapsOf_length` carried a `sorry`; per the zero-sorry discipline it was deleted,
not left in place with a citation. The file has 0 occurrences of `sorry`.

Next: the List/Finset bridge → `lapsOf_length` → `(verdictsFor w k).length = 2`
→ the well-founded reduction.


## `lapsOf_length` — and the List/Finset "bridge" was `rfl`

Last entry called this bookkeeping and flagged it as a needed transfer lemma.
**It needed no lemma at all**: for `Fin n`, a `Finset.sum` over a filtered `univ`
and a `List.sum` over a filtered `finRange` are the *same term*. Found with
`exact?`, which returned `rfl` — a good argument for reaching for the search
tactics before writing transfer infrastructure by hand.

- `lapsOf_length` — **the traversal takes exactly `n` laps**, one per strand.

The one wrinkle worth noting: `rw [← sum_cycleLen_leaders]` fails with "motive
is not type correct", because the rewrite needs a *syntactic* match while the
two forms agree only up to defeq. `exact sum_cycleLen_leaders _` after the
`simp only` works, since `exact` checks up to defeq.

67 results, sorry-free, zero warnings, axiom-clean.

## What is left for `(verdictsFor w k).length = 2`

`lapsOf_length` gives the lap **count**. The two-entry lemma additionally needs
the lap **starting positions** to be exactly `Fin n` — i.e. the concatenated
walks form a list that is a permutation of `List.finRange n`. That needs:
walks are `Nodup` within a component (the orbit does not repeat before
`cycleLen`) and disjoint across components (`leaderOf_eq_iff`), giving a `Nodup`
list of length `n` over `Fin n`, which is therefore a permutation of `finRange`.

With that, `card_involved` transfers to `verdictsFor` and the two-entry lemma
follows. Then the well-founded reduction, still the last open piece of step 2.


## Both halves of the Nodup argument

- `walk_disjoint_of_ne_leader` — **walks from distinct leaders never meet**, so
  no strand is walked twice. Note the direction wrinkle: the walk runs under
  `f⁻¹` (a lap applies the first letter first) while leadership is stated for
  `f`; `Equiv.Perm.sameCycle_inv` reconciles them, a permutation and its inverse
  having the same cycles.
- `walk_nodup` — **a component walk does not repeat.** Via
  `Equiv.Perm.IsCycle.pow_eq_one_iff`: if `s^(b-a)` fixes a point the cycle
  moves, then `s^(b-a) = 1`, so `orderOf s ∣ (b-a)`, and `b - a < orderOf s`
  forces `a = b`. Two cases, fixed point and genuine cycle.

69 results, sorry-free, zero warnings, axiom-clean.

## One lemma DROPPED rather than forced

`cycleLen_inv` (`cycleLen f⁻¹ p = cycleLen f p`) is **true and not proved
here**. `Equiv.Perm.cycleOf_inv` and `orderOf_inv` are exactly the ingredients,
but every route tried (`rw` both directions, `congr 1`) fails on an instance
mismatch: `cycleOf` carries a `DecidableRel f.SameCycle` argument, and the
instance `open scoped Classical` supplies for `f⁻¹.cycleOf p` is not the one
`cycleOf_inv` produces. Since nothing yet consumes it, it was **removed rather
than left half-proved or worked around**. It will be needed when the walk (under
`f⁻¹`) is matched to a lap count stated for `f`; the fix is probably to thread
one explicit `DecidableRel` instance through this section instead of relying on
`open scoped Classical` per-declaration.

## Remaining chain to `(verdictsFor w k).length = 2`

1. ✅ disjoint across components — `walk_disjoint_of_ne_leader`
2. ✅ nodup within a component — `walk_nodup`
3. ⬜ the concatenated walks are `Nodup` (combine 1 + 2 over `List.flatMap`)
4. ⬜ a `Nodup` list of length `n` over `Fin n` is a permutation of `finRange n`
   (`exact?` does not find this in one step; needs a `toFinset`/card route)
5. ⬜ transfer `card_involved` across that permutation

Then the well-founded reduction.


## `cycleLen_inv` — an instance-plumbing wall, now diagnosed (not guessed)

Last entry attributed the failure to `open scoped Classical`. **That was only
half right.** Removing the `Classical` decoration from the `cycleLen` family was
a real fix for a *different* mismatch — a standalone probe of exactly the same
statement compiles fine without it, and the file is simpler for the removal
(kept). But `cycleLen_inv` still fails, and the cause is one level deeper.

Measured, so the next attempt need not repeat it:

* `∀ g, cycleLen g p = orderOf (g.cycleOf p) := fun _ => rfl` **holds** — the
  definition is transparent, so `cycleLen` is *not* the obstruction.
* `show orderOf (f⁻¹.cycleOf p) = orderOf (f.cycleOf p)` is rejected as **not
  definitionally equal** to `cycleLen f⁻¹ p = cycleLen f p`. That is only
  possible if the two `DecidableRel f.SameCycle` arguments differ.
* `orderOf (f⁻¹.cycleOf p) = orderOf ((f.cycleOf p)⁻¹)` **is provable** via
  `congr 1` + `cycleOf_inv` — and *still* will not `rw` into the goal. Same
  divergence, one level out.

So it is instance plumbing, not mathematics: fix **one** `DecidableRel` instance
for the section and pass it explicitly, or bridge with `Subsingleton.elim`. The
diagnosis is now in the Lean file so it is not re-derived.

**This blocks `lapStarts_nodup`** (step 3), because the walk runs under `f⁻¹`
while the lap count is stated for `f`. Steps 1-2 remain proved.

## Also this pass

The Lean LSP MCP server reconnected, but **its Mathlib search tools are
unusable here** — `leansearch` and `loogle` both return
`403 Forbidden` through the agent proxy, and `lean_goal` timed out at 60 s on
this file. Local `#check` / `exact?` probes remain the only working
name-discovery route in this container. Lemma names confirmed this way for the
next steps: `List.nodup_flatMap`, `List.map_flatMap`,
`List.perm_of_nodup_nodup_toFinset_eq`, `List.nodup_finRange`.


## The instance wall was ROUTED AROUND, not fought — and the code is better for it

Last entry ended blocked on `cycleLen_inv`, needed because the walk ran under
`(closurePerm w)⁻¹` while the lap count was stated for `closurePerm w`. The fix
was not to force the bridge but to notice that **the two permutations should
never have both appeared**:

- `stepPerm w := (closurePerm w)⁻¹` — by `lapStep_eq` this *is* the map one lap
  applies, so it, not `closurePerm`, is the permutation the traversal walks.
  `lapsOf` now phrases the leader filter, the lap count and the walk all in
  `stepPerm w`.

Consequences, all of them simplifications:

- **`cycleLen_inv` is no longer needed at all.** The blocked lemma was an
  artifact of mixing two permutations; one permutation, no bridge. The
  diagnosis stays in the file for whoever hits the same `DecidableRel`
  divergence elsewhere.
- **`walk_disjoint_of_ne_leader` lost a hypothesis-level step**: restated in a
  single permutation, it no longer needs `Equiv.Perm.sameCycle_inv` to
  reconcile `f` with `f⁻¹`.
- **Step 3 is proved**: `lapStarts`, `lapsOf_eq_map`, and **`lapStarts_nodup`**
  — no strand is walked twice — combining `walk_nodup` and
  `walk_disjoint_of_ne_leader` over the concatenation via `List.nodup_flatMap`
  and `List.Pairwise.imp_of_mem`.

73 results, sorry-free, zero warnings, axiom-clean.

## Remaining chain

1. ✅ disjoint across components
2. ✅ nodup within a component
3. ✅ concatenated walks `Nodup` — `lapStarts_nodup`
4. ⬜ `lapStarts w ~ List.finRange n` — a `Nodup` list of length `n` over
   `Fin n` is a permutation of `finRange`. Both inputs are now in hand
   (`lapStarts_nodup`, and `lapsOf_length` gives the length via
   `lapsOf_eq_map`); the route is `List.perm_of_nodup_nodup_toFinset_eq` plus a
   `toFinset = univ` card argument.
5. ⬜ transfer `card_involved` across that permutation ⇒
   `(verdictsFor w k).length = 2`

Then the well-founded reduction.

## 2026-08-29 — the diagnosed-blocked `cycleLen_inv` is CLOSED (PR #5976)

`BraidClosure.lean` carried three paragraphs headed "Blocked lemma,
diagnosed" for `cycleLen f⁻¹ p = cycleLen f p`, ending "the fix is instance
plumbing, not mathematics". Every particular of that diagnosis was correct.
The plumbing is **one `congr!`** — `Decidable` is a subsingleton, so
`DecidableRel` is one pointwise:

    unfold cycleLen
    rw [← orderOf_inv (f.cycleOf p), Equiv.Perm.cycleOf_inv f p]
    congr!

Two routes that do NOT work, measured and now recorded in the file so the
next reader does not retry them:

- `simp only [cycleLen, h]` with `h : f⁻¹.cycleOf p = (f.cycleOf p)⁻¹`
  proved separately reports `h` **unused** — the instance a tactic block
  synthesizes is not the one `cycleLen`'s body carries.
- `show orderOf (f⁻¹.cycleOf p) = orderOf (f.cycleOf p)` fails with a
  **pattern error**, so the two instances are not definitionally equal
  either. Restating the goal cannot bridge them.

Scope note: the lemma is no longer *needed*. The `stepPerm` refactor phrases
the walk and the lap count in one permutation, which removes the bridge from
the critical path rather than paying for it. The `stepPerm` docstring still
pointed at "the diagnosis above" as though the bridge were unavailable; that
is corrected.

**Still open on this bean** (unchanged): the partition fact — that the cycles
of `closurePerm w`, each represented once by its leader and walked for its
full length, cover `Fin n` exactly. Until that lands,
`(verdictsFor w k).length = 2` is unavailable and `Descending` is a
well-formed definition whose two-entry structure rests on an undischarged
fact. That is real mathematics, not plumbing.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-29 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 71 Update (lane-e667)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Foundations/RigidGapBraidedThreeStrandClosureWindowCumulativeCommutantBilinearCyclicity.lean`
- 80-dps mpmath probe: `computations/probes/rigid_gap_braided_three_strand_closure_window_cumulative_commutant_bilinear_cyclicity_probe.py`
- Witness: `computations/probes/rigid-gap-braided-three-strand-closure-window-cumulative-commutant-bilinear-cyclicity.witness.json` (`scriptHash = bb0e9e32b9629d9789227d338ed551e0d79651afa39f07ae980772f540b2ef6a`, `scriptCommitSha = b704b4dd3d9c5480efb9471bb8860000327215d9`)
- PR: https://github.com/litlfred/qou/pull/8385 (`7154445b1b227674fa957c8eed34f505f5e0eeae`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8385, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-29: "chore(beans): qou-m7nj block-factorisation join; qou-e6db cycleLen_inv closed"). The work may be partly or fully done. Read the bean before you close it.
