---
# qou-06h7
title: 'Lean: exchange/Matsumoto general-rank braid relation'
status: completed
type: task
priority: normal
created_at: 2026-07-19T02:57:13Z
updated_at: 2026-09-06T10:49:09Z
---

## Measured 2026-09-05 (branch claude/hecke-cyclicity-markov-2026-09-05, PR #6845)

Re-measured against the pinned Mathlib (v4.24.0, the toolchain in
`lean-toolchain`), because an earlier claim of mine — "zero occurrences of
`exchange`/`deletion` in `Mathlib/GroupTheory/Coxeter/`" — was true but weaker
than what is actually there.

`Mathlib/GroupTheory/Coxeter/` is four files: `Basic.lean`, `Length.lean`,
`Inversion.lean`, `Matrix.lean`. Grepping all four case-insensitively for
`exchange|matsumoto|deletion` returns **exactly one line**, and it is
`Basic.lean:78`, inside Mathlib's own TODO list:

    * State and prove Matsumoto's theorem.

So the status is not "Mathlib might have it under another name" — Mathlib
states, in its own file header, that it does not. There is no exchange
property, no deletion condition, no geometric representation, and nothing in
the tree imports `Inversion.lean`.

## What is and is not blocked by this

The *algebra* half of Matsumoto is already proved in this corpus and is not
waiting on anything:
`QOU/IwahoriHecke/BraidWordInvariance.lean` has `heckeWord_eq_of_braidMove`,
its closure `heckeWord_eq_of_braidEquiv`, and `exists_Tw_of_braidEquiv` — the
conditional theorem that produces a well-defined `T_w` **given** the group
half as a named hypothesis. That is the honest form of the deferral.

The *group* half — any two reduced expressions for `w ∈ W` are related by a
chain of braid moves — is what is open, and it is a fact about the Coxeter
group, not about the Hecke algebra. Proving it is Mathlib-scale work
(exchange property → deletion condition → Matsumoto), not a session's task,
and it should be done as a Mathlib contribution rather than in `QOU/`.

**Do NOT reach for this to fix injectivity of the R-matrix action.** At the
`Fin 2` fibre that action is non-injective *by theorem* for `n ≥ 3` (kernel
`ker(H_n ↠ TL_n)`, dimension `n! − Catalan(n)` = 1, 10, 78, 588, 4611, 38890 at
n = 3…8), so no amount of basis machinery makes it injective. Matsumoto buys
the **rank** of `H_n(q)`, which is worth having for its own sake. Recorded in
`QOU/IwahoriHecke/TensorEmbedding.lean` §"What `heckeActionN` does NOT say".


## 🛑 CORRECTION 2026-09-05, same day, same session — I measured Mathlib and concluded about AVAILABILITY

The entry above says the group half of Matsumoto is *"Mathlib-scale work
(exchange property → deletion condition → Matsumoto)"*. **The first and hardest
of those three is already proved in this corpus, sorry-free, for every Coxeter
system.** I ran the Mathlib half of the check and skipped corpus-grep path 2
(`grep -rln <topic> content/`) entirely — the exact failure the checklist exists
to prevent, made in the very entry where I was correcting a *different*
measurement error.

Measured, on `main`:

* [`QOU/Machinery/CoxeterReflectionCocycle.lean:469`](../content/quantum-observable-universe/lean/QOU/Machinery/CoxeterReflectionCocycle.lean)
  — `theorem rightExchange : RightExchangeProp cs`, whose docstring reads *"The
  right exchange property holds in every Coxeter system … This closes the
  audited Mathlib gap."*
* `:459` — `theorem strong_exchange` (Björner–Brenti Thm 1.4.3): if `t` is a
  right inversion of `π ω` — **any** reflection, **any** word, reducedness not
  required — then `π ω · t` is `π (ω.eraseIdx j)` for some `j`.
* `RightExchangeProp` itself is at `QOU/Machinery/CoxeterParabolicCoset.lean:63`.

Both are **sorry-free**: the three `sorry` string-matches across those two files
are all prose (*"sorry-free"*, *"never as … a `sorry`"*), not tactics. The file's
own header carries `HONESTY (STRICT): sorry-free; no axiom, no class instance,
no True.`

### What that changes

The remaining chain from this corpus's actual starting point is **deletion →
Matsumoto**, not exchange → deletion → Matsumoto. That is a materially smaller
job than "Mathlib-scale", and it is the kind of thing a session could plausibly
carry. It does **not** make Matsumoto proved, and it does not change the other
finding recorded above — Matsumoto is still not the obstruction to injectivity
of the R-matrix action, which is false at the `Fin 2` fibre for `n ≥ 3` by
theorem.

### Where this came from

A sibling landed `qou-phir` on `main` the same afternoon — `d500c443211` (the
Bruhat/subword order, Mathlib has none) and `ef8826f663d` (`T_w^{-1}` lies in the
Bruhat interval `[e, w^{-1}]`, sorry-free). `d500c443211`'s message names the
same fact: *"Each needs the exchange condition. This repo HAS that —
`CoxeterParabolic.rightExchange`, sorry-free for every Coxeter system — so these
are unfinished, not blocked."* I found it while checking whether my own
"Mathlib has no braid group" claim shared the defect the sibling's other commit
(`2aa451659bf`, *"my 'Mathlib has no Bruhat order' grep was measuring my own
checkout"*) had retracted. Mine survived that check; this one did not.


## 2026-09-06 — the deletion condition is PROVED (PR #6894)

Acting on the retraction above. `QOU/Machinery/CoxeterDeletion.lean`:

* **`exists_deletion`** — the deletion condition (Björner–Brenti Thm 1.4.4):
  a non-reduced word has two positions `a < b` whose deletion leaves the
  product unchanged. One induction along the word from the right, off
  `strong_exchange`. No case analysis on the Coxeter matrix, no rank
  restriction.
* **`exists_reduced_sublist`** — every word contains a **reduced subword**
  with the same product. Strictly stronger than Mathlib's
  `exists_reduced_word'`, which gives *some* reduced word for the element;
  this one is a `List.Sublist` of the word you started with.

Both sorry-free, `[propext, Classical.choice, Quot.sound]`.

**So the chain is now exchange ✓ → deletion ✓ → Matsumoto ✗.** Matsumoto
itself remains open and remains the named hypothesis of
`BraidWordInvariance.exists_Tw_of_braidEquiv`. This bean is NOT closed.

**Cross-arc consumer.** `QOU.Machinery.CoxeterBruhat` (sibling `qou-phir`,
merged to `main` 2026-09-05) defines `u ≤ w` by the subword criterion and
records that transitivity, antisymmetry, the subword property and the lifting
property are unproved there because "each needs the exchange condition".
`exists_reduced_sublist` is the first of those inputs in the shape they
consume.

**Also fixed on `main` in the same PR:** `Tw.lean` and
`BraidWordInvariance.lean` both asserted that *this corpus* has no exchange
property. Both docstrings corrected.


## 🛑 2026-09-06 — `exists_Tw_of_braidEquiv` is VACUOUS at the case it was written for

Found while assessing what Matsumoto would actually buy. The conditional that
this corpus has been offering as "the honest form of the deferral" **cannot be
discharged**, so it reduces nothing.

`BraidWordInvariance.exists_Tw_of_braidEquiv` takes as hypothesis
`∀ u v : List B, π u = π v → BraidEquiv M u v` — over **all** words. Its own
docstring flagged that as "stronger than Matsumoto" and offered the strength as
a feature: *"what a total `Tw : W → H` needs"*.

**It is not merely stronger; at `π := cs.wordProd` it is false.** A braid move
swaps an alternating block of length `M i j` for one of length `M j i`, and a
Coxeter matrix is symmetric, so braid-equivalence **preserves word length**. But
`s_i² = 1` gives `π [i,i] = π []` with lengths `2` and `0`. Proved in
`QOU/IwahoriHecke/TwFromMatsumoto.lean`:

* `braidEquiv_length_eq` — braid-equivalence preserves length (given symmetry);
* **`not_braidEquiv_hypothesis`** — the all-words hypothesis is false for any
  Coxeter system with at least one generator.

The theorem itself is fine as a statement about an abstract `π : List B → W`;
what was wrong is the claim that it made the remaining gap exact. It made a gap
nothing can fill.

### The replacement, same file

* **`exists_Tw_of_matsumoto`** — hypothesis = Matsumoto verbatim (two
  **reduced** words with the same image are braid-equivalent); conclusion = a
  `Tw : W → H(M,q)` agreeing with the word product on every **reduced** word.
  Satisfiable, and it is what a `T_w` basis actually means — a basis is indexed
  through reduced expressions, not arbitrary words. Uses Mathlib's
  `exists_reduced_word'` for the choice (`redWord`).
* `Tw_one_of_matsumoto` — `T_1 = 1`.

Both sorry-free; `braidEquiv_length_eq` needs only `[propext]`.

`BraidWordInvariance.lean`'s two misleading passages are corrected in the same
PR (#6894). **Matsumoto itself is still open** — this changes which conditional
the corpus offers, not whether the input exists.


## 2026-09-06 — antisymmetry of the Bruhat order closes (same PR #6894)

`QOU/Machinery/CoxeterBruhatOrder.lean` spends the deletion consequence on the
sibling's deferred list. `CoxeterBruhat` names four things it does not prove —
transitivity, antisymmetry, the subword property, lifting — saying "each needs
the exchange condition". **One of the four now closes.**

* `bruhatLe_reduced_witness` — the witnessing subword may always be taken
  **reduced** (a subword of a reduced word need not be). This is where
  `exists_reduced_sublist'` is spent.
* `eq_of_bruhatLe_of_length_le` — `u ≤ w` with `ℓ(w) ≤ ℓ(u)` forces `u = w`,
  by a length squeeze: `ℓ(u) ≤ |ω'| ≤ |ω| = ℓ(w) ≤ ℓ(u)`, so the sublist has
  full length and `List.Sublist.eq_of_length` makes it the host.
* **`bruhatLe_antisymm`** — antisymmetry.
* `bruhatLe_one_iff`, `not_bruhatLe_of_length_lt`.

All sorry-free, `[propext, Classical.choice, Quot.sound]`.

**Why the other three do NOT follow, stated in the file.** Transitivity is not
a corollary: from `v ≤ w` you get a reduced word for `w` with a (now reduced)
subword for `v`; from `u ≤ v` you get a reduced word for `v` — but **another
one**, and nothing says two reduced words for the same element are
interchangeable. That is the subword property, equivalent in strength to
Matsumoto. So the four split cleanly: antisymmetry needed only length
bookkeeping; transitivity, subword and lifting all wait on Matsumoto.


## ✅ CLOSED 2026-09-06 — Matsumoto is proved (branch claude/coxeter-deletion-matsumoto-2026-09-06)

**My "Mathlib-scale work, not a session's task, should be done as a Mathlib
contribution rather than in QOU/" was wrong on all three counts**, and the
first correction on this branch is why: the exchange property was ALREADY in
this corpus (`CoxeterReflectionCocycle.rightExchange`, sorry-free, every
Coxeter system) — I had measured Mathlib and concluded about availability,
skipping corpus-grep path 2. With exchange in hand the remaining chain is one
session's work, and it is now done, in four files:

| file | what it adds |
|---|---|
| `Machinery/CoxeterDeletion` | the deletion condition; every word contains a reduced SUBWORD |
| `Machinery/CoxeterRankTwo` | reduced two-letter words are alternating; parabolics embed isometrically; two spellings ⟹ `(sᵢsⱼ)^k = 1` |
| `Machinery/CoxeterDihedralDescent` | the descent lemma; `DihedralExact` discharged for `M i j ≤ 3` |
| `IwahoriHecke/Matsumoto` | Matsumoto, and `exists_Tw_An` |

**Status of the result.** `matsumoto` is conditional on ONE named predicate,
`CoxeterRankTwo.DihedralExact` — that `σᵢσⱼ` has order exactly `M i j`.
`matsumoto_An` and `exists_Tw_An` are **hypothesis-free**: for `M i j ≤ 3` the
predicate follows from `CoxeterGeometricRepresentationFull`'s two unconditional
cell-faithfulness results. That covers type A, hence `H_n(q)` and the symmetric
group — every case this corpus's Hecke/braid arc uses.

`#print axioms` on all five headline results: `[propext, Classical.choice,
Quot.sound]`. No `sorryAx`.

**Non-vacuity checked, not asserted** (`An_le_three` / `An_ne_zero` plus an
`example` exhibiting a Coxeter system of type Aₙ) — this same branch caught a
conditional in this corpus whose hypothesis was FALSE at the case it was
written for.

## What is left, as a NEW item — not this one

`DihedralExact` for `M i j ≥ 4`. That is the order of `σᵢσⱼ` in the reflection
representation, and it is `CoxeterGeometricRepresentationFull`'s own named open
item (its HONESTY note: "What this does NOT prove: ... the order of σᵢσⱼ being
exactly mᵢⱼ"). The trig engine it needs — `periodic_of_two_step`, the
`(fᵢfⱼ)^m = 1` direction — is already in that file; the converse (no smaller
power is the identity) is not. No consumer in this corpus needs it.
