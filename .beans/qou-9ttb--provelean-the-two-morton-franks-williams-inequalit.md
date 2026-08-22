---
# qou-9ttb
title: 'PROVE(lean): the two Morton-Franks-Williams inequalities — currently hypotheses on MFWWitness'
status: completed
type: task
priority: normal
created_at: 2026-08-22T02:02:43Z
updated_at: 2026-08-22T19:25:59Z
---

## What is open

`QOU.Knot.MortonFranksWilliams` (PR #5380, bean `qou-dr8m`) carries the two
MFW degree bounds as **hypotheses** on the `MFWWitness` structure:

    mfw_lower : dmin >= e - n + 1
    mfw_upper : dmax <= e + n - 1

Everything downstream of them is derived and sorry-free — `braid_bound`,
`spread_le_two_mul_sub_two`, `selfLinking_le`, `no_representative_of_spread_gt`,
and the two measured instances (`sixOne`, `torusFourFive`). What is NOT proved
is the pair itself.

This is §3b-cond used honestly: the class carries the *inputs* and the theorems
*derive* the conclusions. It is deliberately not a class carrying
`braid index >= ...` as a field. But the inequalities remain assumed.

## Why it is research-scale

Morton's proof needs two ingredients:

1. **Markov invariance of the Ocneanu trace** — that the trace is unchanged by
   stabilization, so the HOMFLY of a closure is a link invariant rather than a
   braid-word invariant.
2. **A degree argument** on the Hecke-algebra representation bounding the
   `v`-degree window by the writhe and strand count.

## Dependency — do NOT duplicate

Ingredient 1 overlaps bean `qou-bhrx` (**in-progress**, F4-opt1: abstract
Ocneanu cyclic-trace lemma on MarkovStabilization). That bean already delivered
`QOU.Machinery.BilinearTraceCyclicity` (sorry-free, all-n) reducing cyclicity to
Gram symmetry, and names the remaining open keystone as the Ocneanu word-length
induction OR the Wedderburn decomposition `tr_M = sum_lambda w_lambda chi_lambda`.

Whoever picks this up should build ON qou-bhrx rather than re-deriving the trace
machinery. Ingredient 2 (the degree argument) appears to be genuinely
independent of it and is the part with no in-corpus precedent I could find.

## Corpus-grep done (2026-08-22)

- `.beans/` for morton / franks / ocneanu / markov-invariance -> **5 files
  matched**, assessed as follows (corrected 2026-08-22; an earlier version of
  this bean said "only qou-bhrx and qou-dr8m", which overstated what had
  actually been checked):
  - `qou-bhrx` — **relevant**, ingredient 1, in-progress. See above.
  - `qou-dr8m` — mine, completed; the *derivation* consuming these as
    hypotheses, not a proof of them.
  - `qou-qb8e`, `46ke`, `qou-b3nk` — matched on the string **"Ocneanu" only**,
    not on Morton / Franks / Markov-invariance. They concern other uses of the
    trace (hh1 carrier magnitude; canonical-watcher CODATA literals; the
    qbeta trace-convention registry). Not MFW; no overlap.
- No `PROVE` bean for the inequalities themselves existed.
- `grep -rli "morton-franks\|morton_franks" content/ computations/ docs/` -> only
  files this PR adds or edits. In particular `computations/homflypt_engine.py`
  matches **only** on a comment added by this PR; `origin/main`'s copy has zero
  mentions of Morton / Franks / braid index. So there was no pre-existing MFW
  machinery in the corpus, which is what #5380's "neither existing source can
  supply a v-degree" rests on.

## Possibly-related downstream consumers

Two open beans want braid-index data and may be served by the producer
`computations/homfly_braid_index_mfw.py` that #5380 adds — worth checking
before either is worked, though neither is blocked on *proving* MFW:

- "production hygiene: add the m <= p (braid index) guard to
  rosso_jones_three_strand_delta_q and alpha_k_per_force_assembly"
- "compute: name the braid index in the isotope writhe comparisons"

Note `computations/knot_braid_database.py` carries 3-strand knots only, which is
why `6_1` had no in-repo braid index before #5380.

## Scope note

Nothing is blocked on this. The braid indices derived in #5380 are correct as
computed facts; MFW is a cited theorem there, exactly as a textbook result would
be. This bean exists so the assumption is visible and attributable rather than
silently inherited.


## CORRECTION (2026-08-22) — my dependency claim above was wrong

The section "Dependency — do NOT duplicate" says ingredient 1 (Markov
invariance / Ocneanu cyclicity) is open under `qou-bhrx`, and calls that bean's
remaining item "the OPEN keystone". **I took that from `qou-bhrx`'s own progress
note, dated 2026-07-19, and did not check the corpus.** That is exactly the
failure this repo documents (PRs #1515/#1532/#1543): trusting a status note over
the corpus. Re-checked today:

- **H₄ cyclicity is PROVED and unconditional** — `QOU.Machinery.MarkovTraceH4`
  carries `trM_cyclic` for `n = 4` off the 576-entry Gram closure, reduced via
  `BilinearTraceCyclicity.cyclic_of_gram_symm`. Six-file cluster, **0 real
  `sorry`**.
- **The H₄ NF basis + `mulNF` table exists** —
  `computations/markov/hecke-regular-nf-h4.witness.json`, GB-NF generated
  (bean `qou-1jrr`), `Fin 24` = 4! normal forms, which is what
  `MarkovTraceOnHecke.lean`'s "open keystone infra" block asked for. That block
  described the work as still-to-do for about a month after it landed; corrected
  in the same commit as this note.

**So ingredient 1 is NOT the blocker for this bean.** What remains, precisely:

1. **The Wedderburn route is still conditional.**
   `HeckeH4RepDecomp.trM4_gram_symm_of_markov_basis` needs `hbasis` (24
   basis-level Markov identities). Tracked as `qou-x64l` step 4 — not here, and
   not needed for MFW.
2. **General-`n`, not just `n = 4`.** MFW's degree argument is over `H_n` for
   arbitrary `n`; H₃ and H₄ are done, the general case is not.
3. **Ingredient 2 of this bean — the degree argument — is untouched and remains
   the part with no in-corpus precedent.** That is the real content of this
   bean, and it was true before this correction and after it.


## PROGRESS (2026-08-22) — ingredient 2 has a second route, and its step is proved

**The scoping in this bean named one route and treated it as the only one.**
It said proving MFW needs Markov invariance of the Ocneanu trace plus a degree
argument. There is a second route that needs **neither**: induct along the
skein recursion itself, on the same well-founded order the corpus's own HOMFLY
engine already descends (`computations/homfly_skein_braid.py`).

Lickorish's relation rearranges to `P₊ = v²·P₋ + v·z·P₀`. On braid words both
children are again `n`-strand closures — switching moves `e ↦ e−2`, smoothing
moves `e ↦ e−1` — so the MFW window propagates by pure interval arithmetic.

**Proved, sorry-free**: `QOU.Knot.MFWSkeinInduction` — `mfw_step`,
`switch_shift` / `smooth_shift` and their converses, `switch_shift_eq` /
`smooth_shift_eq`, `spread_le_of_window`. Axioms on every one:
`propext, Classical.choice, Quot.sound`; no `sorryAx`.

**Measured first**: the window holds for **180/180** random braid words on 2–4
strands under the engine, zero violations.

**Lean corrected me mid-proof, and the correction is the interesting part.** I
wrote the step as an inclusion with slack at the top — two units on the switch
branch, one on the smoothing — and inferred that the upper bound must
therefore be driven by the base case. Both slack lemmas are **false**;
`ring` rejected them. `2 + ((e−2) + n − 1) = e + n − 1`, not `e + n − 3`. Each
shifted child window *equals* the parent window at both edges. The recursion
neither widens nor narrows — it only translates. That is a stronger result
than I set out to prove, and the inference I had drawn from the imagined slack
was unfounded.

An earlier draft also packaged this as an induction "concluding" MFW whose
base-case hypothesis went **unused** — near-circular. Deleted rather than
patched; the file now proves the step and nothing more.

## What remains — narrower than before, and NOT closed

The **base case**: a descending braid diagram closes to an unlink of `c`
components with `P = δ^{c−1}`, `δ = (v⁻¹ − v)/z`, so its degrees span
`[−(c−1), c−1]`. Fitting that inside `[e−n+1, e+n−1]` requires

    |e| ≤ n − c

for descending words. This is **not free**, and I checked rather than assumed:
it is false for arbitrary words — the longest element of `S₃` has Coxeter
length 3 against `n − c = 1` — so it depends on what "descending" actually
supplies, and that is where the remaining content of this route sits.

Also still open, unchanged: HOMFLY's invariance and the termination of the
recursion are built into the engine's construction, not proved in Lean.

So ingredient 2 is **not closed**. What changed is that it no longer requires
the Ocneanu/Markov machinery — the residue is one combinatorial statement
about descending braid words.


## Base case narrowed further (2026-08-22, second pass)

**Mechanism identified.** Descending supplies: *no two strands cross more than
once NET.* Max `|net signed crossings|` over any strand pair = **1**, across
all 1227 descending words. This is the cancellation that keeps `|e|` bounded
while the letter count `m` stays large — and it is what makes the bound
possible at all, since `|e| <= m` runs the wrong way.

**One decomposition REFUTED** — scope-(a), recorded so nobody re-walks it. The
per-pair bound is necessary but **not sufficient**: in **298** of the 1227
words the count of pairs with nonzero net **exceeds** `n - c`. Worked case:
`n = 3`, `w = sigma_1 sigma_2 sigma_1^{-1}` has all three pairs nonzero
against `n - c = 1`; the nets are `+1, +1, -1`, summing to `1`. So
`|e| <= #nonzero pairs` does not give it — the SIGNS must additionally
arrange, and no argument for that is in hand.

Also checked and rejected as the mechanism: `|e| <= rank(G)` where `G` is the
signed graph of nonzero pairs. For the triangle above `rank(G) = 2` while
`n - c = 1`, so `n - c` is strictly stronger than the graph rank — the bound
is not a spanning-forest count.

**Still open.** The residue is exactly: why do the signs arrange so that
`|sum of nets| <= n - c`? `n - c` is the reflection length of the word's
permutation, and the crossings' transpositions generate that permutation, so
the shape of the answer is probably "the word's transposition sequence is a
reduced-ish factorization once cancellation is applied" — but that is a
sketch, not an argument.


## Base case REDUCED to the connected case (2026-08-22, third pass)

The bound decomposes over closure components. Measured over 2592 descending
words, zero failures on both halves:

**(A) Any two closure components have LINKING NUMBER ZERO** — their signed
crossings cancel exactly (0 pairs of components with nonzero sum). This one is
*provable*, not merely measured: descending means every crossing is first met
as an over-crossing, so traversal totally orders the components; every crossing
between two of them is first met while traversing the EARLIER component, hence
the earlier passes entirely OVER the later, lifts off it, and lk = 0. Since
lk = (1/2) * (signed crossings between them), the sum vanishes.

**(C) Each component then satisfies |sum of inner nets| <= L - 1 separately**
(0 violations; tight in 1220 components).

Since sum over components of (L - 1) = n - c exactly, **the whole base case
reduces to the single-component (c = 1) case**: one closure component, L braid
strands forming a single cycle, descending, show |self-writhe| <= L - 1.

Equivalent reformulation, also measured clean (0 failures): the crossing
graph's number of independent cycles is at most twice its number of negative
edges.

**Second decomposition refuted.** "G+ and G- are both forests within a
component" would have finished it (each <= L-1 edges, so |pos - neg| <= L-1).
G- always IS a forest, but G+ carries a cycle in 30 words: n = 4,
w = sigma_1 sigma_2 sigma_1 sigma_3 sigma_2^{-1} has the positive triangle
{1,2}, {1,3}, {2,3}. The bound survives there only because a negative edge
compensates (pos = 4, neg = 1, e = 3 = L - 1, tight).

**Still open**: the connected case. But it is strictly cleaner than the
original -- the multi-component reduction is now understood and is exactly
linking-number-zero.


## RESOLVED as classical (2026-08-22, fourth pass) — it was never open

The `DescendingWrithe` base-case hypothesis is a **corollary of two standard
theorems**. I had been trying to prove from scratch something the literature
already gives.

**1. A descending diagram is an unlink** (`lickorish1997`). Verified in this
codebase's own conventions rather than assumed: over every descending word
tested (n <= 4, length <= 5) the HOMFLY depends only on `c` and never on the
word -- 0 disagreements -- taking the values 1, (v^-1-v)/z, ((v^-1-v)/z)^2,
((v^-1-v)/z)^3, i.e. exactly the c-component unlink polynomial.

**2. Bennequin's inequality** (`bennequin1983`, Asterisque 107-108, 87-161):
`sl(L) <= -chi(L)`. For a closed braid on n strands with exponent sum e the
self-linking number is `sl = e - n`; the c-component unlink has maximal Euler
characteristic `chi = c` (c disjoint disks). Hence `e - n <= -c`, i.e.
`e <= n - c`. Mirroring sends `e -> -e` and fixes the unlink, giving the other
side. Together: `|e| <= n - c` -- exactly `DescendingWrithe`. The measured
tightness is the standard closed braid realising `sl = -c`.

**Not circular**: Bennequin (1983) predates HOMFLY (1985) and MFW (1987), and
its proof is contact-geometric -- it does not use the skein induction it is
invoked in here.

**Status change**: the hypothesis stays a threaded assumption in Lean *only*
because Mathlib has neither HOMFLY nor the Bennequin inequality. Its epistemic
status is **classical-and-cited**, NOT open. Added `bennequin1983` to
references.ts (740 refs, no duplicate ids).

**Retrospective on the three refuted routes** (per-pair counting; G+/G- both
forests; the component decomposition): all three were attempts to reprove from
scratch what Bennequin already gives. The component decomposition (A)+(C) is
still correct and still worth keeping -- linking-number-zero between components
is a genuine structural fact -- but it was not needed. The lesson is the
corpus-grep discipline applied one tier out: I checked this repo for prior
work but not the classical literature, and the literature had it.


## Wiring (2026-08-22, fifth pass) — the induction file was ORPHANED

`MFWSkeinInduction` was imported by nothing. Its window arithmetic fed no
consumer. Meanwhile `MortonFranksWilliams.MFWWitness` carries the two MFW
inequalities as fields `mfw_lower` / `mfw_upper` — which are *exactly* `window`
membership for `dmin` and `dmax`. Same object, two files, no connection.

Wired with three declarations, all `#print axioms` clean (propext /
Classical.choice / Quot.sound only, no sorryAx; `toWitness` depends on none):

- `toWitness` — builds the witness from two window memberships. `mem_window` is
  `Iff.rfl`, so the fields are `hmin.1` / `hmax.2`; definitional, not a re-proof.
- `braid_bound_of_window` — makes the wiring load-bearing: the braid-index bound
  now follows via `MortonFranksWilliams.braid_bound` rather than a second copy.
- `descending_witness` — carries the base case through (unlink v-degrees span
  [-(c-1), c-1]; DescendingWrithe puts both endpoints in the window).

**What this does NOT do.** Neither file touches an actual HOMFLY polynomial or
an actual braid — `MortonFranksWilliams` says so itself ("asserts nothing about
any actual knot"). There is no Lean HOMFLY in this repo, so nothing can produce
an `MFWWitness` from a real link. This connects two arithmetic layers; it does
not close MFW. The remaining Lean work is a formalization of HOMFLY/braid
closures, which is a large separate project, not a residue of this bean.

**Verification hazard recorded**: a stale olean in `.lake/build/lib/lean` took
precedence over a fresh build on LEAN_PATH, making three real declarations
report as "Unknown constant". Harmless in that direction; the same shadowing
would let an axiom check PASS against old code. Put the fresh build first.


## CLOSED (2026-08-22) — mathematical content complete; residue split to `qou-e6db`

Closed on owner authorisation. Both ingredients are settled:

- **Ingredient 1** (Markov invariance of the Ocneanu trace) — was **already
  proved** when this bean claimed it open. That claim came from a month-old
  progress note on `qou-bhrx` that I repeated without a corpus-grep; corrected
  in place earlier in this bean.
- **Ingredient 2** (the degree argument) — closed by the skein-induction route,
  which needs neither the Ocneanu machinery nor Markov invariance:
  - **propagation** proved sorry-free (`mfw_step` + window arithmetic);
  - **base case** `DescendingWrithe` is **classical**, not open — descending ⇒
    unlink (`lickorish1997`) plus Bennequin's inequality (`bennequin1983`);
  - **wired** to `MortonFranksWilliams.MFWWitness`, all `#print axioms` clean.

**What is NOT closed, and why it is not this bean's residue.** No Lean file
here touches an actual knot — there is no HOMFLY in Lean, so nothing can
produce an `MFWWitness` from a real link. That is **infrastructure**, not the
mathematics this bean was about, and it is a formalization project on the scale
of a Mathlib contribution. Tracked as **`qou-e6db`** with the full handoff:
what is already done (do not redo), the four steps needed, and the honest
scoping note that it cannot be drained in a session.

**Retrospective worth keeping.** Three self-contained proof routes for the base
case were tried and refuted before the fourth pass found the classical result:
(a) `|e| ≤ #nonzero pairs` (false, 298 words exceed it); (b) "`G⁺` and `G⁻`
both forests" (`G⁻` always is, `G⁺` has a cycle in 30 words); (c) the component
decomposition (correct, and kept — descending components have linking number
zero — but not needed). All three were attempts to reprove from scratch what
`bennequin1983` already gives. The lesson is the corpus-grep discipline applied
one tier out: this repo was checked for prior work, the classical literature was
not, and the literature had it.
