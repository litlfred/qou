---
# qou-h0zz
title: 'V6: braid words per chiral fermion -- the actual blocker for T(t)'
status: todo
type: task
priority: normal
tags:
    - 8f-gen
    - reorg-2026-10-04
    - 8f-open
created_at: 2026-08-10T18:34:14Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---

sm-open-problems.md names this itself: hypercharge Y open, 'framework braid words
per chiral fermion STILL MISSING'.

This is the real blocker, upstream of everything else on the T(t) front. Without a
braid word per chiral fermion there is nothing to read t off, so T(t) is a free
label BY CONSTRUCTION -- which is exactly why the published battery returns a
tautology (TwistBatteryVacuity.lean: the battery collapses to sum(t) = 3Q, and
4 = 1x2x2x1 is multiset counting).

WHAT EXISTS: braid words for the HADRON sector --
  gluon unit        sigma_0 sigma_1^-1      (writhe 0)
  Borromean baryon  B_3 = (sigma_0 sigma_1^-1)^3  (writhe 0)
  Hopf link L_H     from the L+/L- terms
  lepton carriers   e- = T(2,3) trefoil, nu = unknot (KNOT types, not braid words)
WHAT IS MISSING: a braid word per CHIRAL fermion (u_L, d_L, e_L, nu_L and the RH
singlets). The lepton rows are given as knot types only, and chirality is not
represented at all.

NOTE the chirality problem is now sharp (LeptonNumberCarrierChirality.lean): the
carrier cannot be an unframed knot type, so 'e- = trefoil' is not enough -- a
braid word (or framed object) is required for the mirror to act freely.
BLOCKED-BY: V5 (which framing) determines what t even means.


RESULT 2026-08-10 — the braid words are NOT missing; the corpus already fixes them.

chi=-6 constraint: 'T(2,n) with odd n<=7 exhaust the fermion spectrum; electron
T(2,3), neutrino T(2,1)'. And T(2,n) IS the closure of sigma_1^n in B_2. So:
  nu_e = sigma_1^1   (w=+1)      nubar_e = sigma_1^-1 (w=-1)
  e-   = sigma_1^3   (w=+3)      e+      = sigma_1^-3 (w=-3)
  gen2 = T(2,5) = sigma_1^5      gen3 = T(2,7) = sigma_1^7
  baryon B_3 = (sigma_0 sigma_1^-1)^3 (w=0);  gluon unit (w=0)

This RESOLVES the chirality obstruction (LeptonNumberCarrierChirality.lean):
nu and nubar are DIFFERENT BRAID WORDS (w=+1 vs -1) though both close to the
unknot. The mirror acts freely at braid level exactly as predicted.

CANDIDATE FOUND: L(beta) = sign(writhe(beta)), parameter-free, matches 6/6
corpus rows (both leptons, both antileptons, baryon, gluon unit). Consequence:
Y = B - L closes all four LH rows (u,d = 1/3; nu,e = -1).
computations/chiral_fermion_braid_words_probe.py

NOT A CLOSURE -- three caveats:
 1. sign() is a CHOICE of function, not derived from the framework.
 2. The QUARK braid word is still NOT in the corpus; w=0 is ASSUMED (motivated by
    the gluon unit being writhe-balanced). Every quark row rests on it.
 3. Chirality L vs R is still unrepresented -- no distinct word for u_L vs u_R.

KEY CONSEQUENCE for the writhe-independence tension: L = sign(w) is
writhe-DEPENDENT, and that is FINE. Y = B - L still does not factor through w
because B varies at fixed w. So the 'second invariant independent of the writhe'
is B (mu-bar_123), NOT L. The apparent L-needs-framing vs Y-needs-independence
collision dissolves: L needs the BRAID WORD (which carries writhe), not a free
framing datum.


---

## 🛑 SCOPE CORRECTION — the LEPTON half of this is already derived, sorry-free, and verified (2026-10-10)

This bean's title calls braid words per chiral fermion *"the actual blocker for
T(t)"*. That is **half true as of 2026-08-17** and the other half is on a
**`scrapped`** bean, which is why it keeps being reported as wholly open — I did
exactly that in four places today before reading it.

**The carrier is `htw2`** (`beans/defs/htw2--gap-per-chiral-fermion-framed-braid-words-for-strand-twist-total.md`,
294 lines, status **`scrapped`** as a duplicate of `qou-kebu` in the 2026-10-04
reorg). Its *content* was never retracted — only the work item was closed — and
the §path-6 rule about reading `scrapped` beans is exactly what finds it.

### What is DERIVED (not enumerated), verified on `main` `3c0351a40da` today

A framed braid word **does** exist for the leptons, from the corpus's own
`knot-particle-dictionary.md:4` (*"Fermions (n odd) are KNOTS (1 component) …
Quarks are Borromean-linked unknots"*):

    beta_nu = sigma1 sigma2  in B_3,  framing t = (0,0,0)

its closure is the unknot — one component, transitive permutation — so
component-constancy forces a **constant** framing and the pinned total fixes the
value.

| decl | file | gives |
|---|---|---|
| `lepton_framing_determined` | `ComponentFraming.lean` | transitive π + total 3Q ⟹ `t ≡ Q` |
| `nu_framing_is_zero` | same | `Q = 0` ⟹ ν = `{0,0,0}` |
| `nu_distinct_multiset_excluded` | same | a knot closure cannot carry an injective framing ⟹ `{-1,0,1}` **refuted**, and this needs no total at all |
| `e_framing_is_neg_one` | same | e = `{-1,-1,-1}`, derived |
| `d_multiset_forced` | `SignCoherentTwist.lean` | range + total −1 + coherence ⟹ `{-1,0,0}` |
| `coherent_iff_all_same_sign` | same | coherent ⟺ all ≥ 0 or all ≤ 0 |
| `cancel_preserves_total` | same | the reduction step fixes the total |

**Verified rather than taken on trust**, since a bean is not a primary source:
`lean -DautoImplicit=false -s 65536` on both files → **rc=0, 0 diagnostic
lines** (status captured directly, not through a pipe); `ComponentFraming.lean`
304 lines, `SignCoherentTwist.lean` 226 lines, and **0 `sorry` / 0 `axiom` /
0 `native_decide`** in each. All 7 declarations above resolve by name.

**And sign-coherence is no longer an import.** `htw2`'s own later section
upgrades it: because the twist axiom forces `θ_V = q^{1/2}·id_V` on the defining
representation, `θ_V ⊗ θ_V⁻¹ = id` **as morphisms**, so a `(+1,−1)` strand pair
is *ribbon-invisible* and cancelling it rewrites the same state rather than
choosing a different one. The two survivors sign-coherence excludes are the
**un-reduced spellings** of the two it keeps (`d {-1,-1,1} → {-1,0,0}`,
`ν {-1,0,1} → {0,0,0}`). So the residual went **1·2·2·1 → 1·1·1·1**.

### What is STILL OPEN — and this is what this bean should carry

1. **The TOTAL twist is pinned by the SM target**, `T = 3Q`, not computed. `htw2`
   item 1 says so explicitly and nothing above changes it. Deriving `Q(f)` for an
   individual chiral fermion is the real open object; the framework's derived
   `Q = w/2` is a **hadron-level** result and assigns no writhe to a single
   chiral fermion.
2. **The quark side is CONSISTENT, not derived.** Identity-π on the 3-component
   Borromean braid *leaves* `{0,1,1}` available — a transitive π would have
   killed it — which is a real cross-check that passes, and is not a derivation.
3. **Chirality is untouched** — that is `qou-wqto`, and no braid word
   distinguishes `u_L` from `u_R`.
4. **The `1/3` normalisation** (`Q_twist = T/3`) is still the Bilson-Thompson
   helon precedent, not derived.
5. `conj:sm-hypercharge-invariant` stays **open**, and per rule 13a nothing here
   closes it.

### The reusable lesson, because it is the epic's own rule unapplied

The epic `qou-8lxd` records: *"before working a bean, read the beans it cites AND
the beans that cite it."* I wrote that rule after measuring that 5 of 13 bodies
across two fronts were stale against a sibling bean — and then recommended
`htw2` as "the root blocker, highest leverage" **without opening it**, four times,
on the strength of its title. A `scrapped` bean with 294 lines of verified
sorry-free Lean is the sharpest form of that trap: the status says "ignore me"
and the body holds the answer.


---

## The quark side, measured: `u` is forced WITHOUT the interpretive step — and coherence is load-bearing at only two of the four fermions (2026-10-11)

Working item (c) of this bean's open set — derive the quark framing the way the
lepton one was derived. The result is a **negative about where the framework
does work**, and it is more useful than the derivation would have been.

### What the corpus did not have

Corpus-grepped before writing anything: `u_multiset_forced`, any
positive-total mirror of `no_positive_of_negative_total`, and any bean mentioning
a forced `u` multiset are **all absent** — 0 hits across `folio/**/*.lean`
(excluding `.lake`) and 0 across `beans/defs/`. So this is new Lean, not a
re-derivation.

### Measured, by exhaustive enumeration over `{-1,0,1}³` (exact integers)

| `T` | multisets, no coherence | with coherence | any mixed-sign assignment reaches `T`? |
|---:|---|---|---|
| −3 (**e**) | `(-1,-1,-1)` | same | no |
| −2 | `(-1,-1,0)` | same | no |
| −1 (**d**) | `(-1,-1,1)`, `(-1,0,0)` | `(-1,0,0)` | **yes** |
| 0 (**ν**) | `(-1,0,1)`, `(0,0,0)` | `(0,0,0)` | **yes** |
| +1 | `(-1,1,1)`, `(0,0,1)` | `(0,0,1)` | **yes** |
| +2 (**u**) | `(0,1,1)` | same | no |
| +3 | `(1,1,1)` | same | no |

**Sign-coherence — the one interpretive step in this whole arc — is load-bearing
only at `T ∈ {−1, 0, +1}`.** Of the four first-generation fermions, exactly two
sit in that window: `d` (`T = −1`) and `ν` (`T = 0`). **`u` (`T = +2`) and `e`
(`T = −3`) are forced by range and total alone.** The arc's earlier write-up
credits all four to coherence-or-component-constancy; that over-attributes two
of them.

### Lean added (additive — no existing declaration touched)

In `QOU/StandardModel/SignCoherentTwist.lean`:

| decl | hypotheses | gives |
|---|---|---|
| `u_multiset_forced` | `hrange`, `hsum = 2` — **no `SignCoherent`** | `u = {0,1,1}` in one of three orderings |
| `no_mixed_sign_at_total_two` | `hrange`, `hsum = 2` | `∀ i, 0 ≤ t i` — the alternative coherence would exclude does not exist |
| `coherent_of_total_two` | `hrange`, `hsum = 2` | `SignCoherent t` — at `T = 2` coherence is a **consequence**, not an assumption |
| `no_negative_of_positive_total` | `hsum > 0`, `hcoh` | the mirror of `no_positive_of_negative_total`, for the general positive case |

Contrast with the existing `d_multiset_forced`, which **does** take
`SignCoherent` and provably needs it (`d_mixed_sign_not_coherent`).

### The finding, stated as a negative

**For `u` the framework's component structure does no work.** Leptons differ in
kind: there "a closure is a knot" ⟹ transitive π ⟹ constant framing *forces*
the answer (`ComponentFraming.lepton_framing_determined`). For quarks the
Borromean identity-π makes component-constancy **vacuous**, and what determines
the multiset is integer arithmetic on a range the framework did not derive.

So an agent looking for a framework mechanism that picks `u`'s multiset is
looking for something `hrange` and `hsum` have already settled. This closes
item (c) as a question — not by deriving it, but by showing there is nothing
there to derive.

### What this does NOT change — do not read it as progress on the conjecture

- **The TOTAL is still pinned by the SM target**, `T = 3Q`. Item 1 of this bean
  is untouched, `Q(f)` for a single chiral fermion is still underived, and the
  framework's `Q = w/2` is still hadron-level.
- **`hrange` — entries in `{-1,0,1}` — is itself an input**, not derived here.
  If the range were wider, `T = 2` would not be unique, so the `u` result is
  conditional on it exactly as everything else in this arc is.
- **Chirality is untouched** (`qou-wqto`): no braid word separates `u_L` from
  `u_R`, and nothing above addresses it.
- **The `1/3` normalisation** is still the Bilson-Thompson helon precedent.
- `conj:sm-hypercharge-invariant` stays **open**. Per rule 13a nothing is closed.

### The corpus already had the CONVERSE, and the two run in opposite directions

`ComponentFraming.u_multiset_forces_nontransitive` (line 147) proves
**multiset ⟹ braid**: `{0,1,1}` is non-constant, so a transitive π would kill
it, hence `u`'s closure must be non-transitive — multi-component, consistent
with Borromean. That is the cross-check this arc records as "passing".

`u_multiset_forced` is the **other direction**: **range + total ⟹ multiset**.
Neither implies the other, and having both is what makes the accounting
complete — the braid constrains the multiset's *shape* (non-constant), and the
arithmetic pins the multiset *exactly*. What neither supplies is the total.

Declaration names verified against the live files rather than carried from the
predecessor bean: `ComponentFraming.lean` lines 97-300 (14 declarations,
including `lepton_framing_determined` : 246, `nu_framing_is_zero` : 261,
`nu_distinct_multiset_excluded` : 276, `e_framing_is_neg_one` : 287,
`u_multiset_available_at_identity` : 300).

Main's last 200 commits touched **nothing** under
`folio/quantum-observable-universe/lean/QOU/StandardModel/`, so this is not
racing a sibling.

### Verification record, including the red run

The first `lean`-direct run of these four was **rc=1, RED** — one error, in
`coherent_of_total_two`:

    error: omega could not prove the goal: a possible counterexample may
    satisfy  c <= -1,  -1 <= b <= 1,  -1 <= a <= 1,  1 <= a + b <= 3
    where a := t 1, b := t 2, c := t i

The *claim* was fine; the **proof** was wrong — and **my first diagnosis of it
was also wrong**, which is the part worth recording.

I read the error as being in `coherent_of_total_two` and blamed a
pattern-`intro` on a `Prop`-valued `def`. Rewriting that proof changed nothing:
the second run returned the **identical** error. Line 300 is not in
`coherent_of_total_two` at all (that starts at 303) — it is the closing `omega`
of **`no_mixed_sign_at_total_two`**, which begins at 293.

The actual bug: that theorem concludes `∀ i, 0 ≤ t i`, over an **arbitrary**
`i : Fin 3`, while I supplied only `hrange 0`, `hrange 1`, `hrange 2`. So omega
had no constraint on `t i` and the counterexample it printed says exactly that
(`c := t i`, `c ≤ -1`, with only `t 1` and `t 2` bounded). I had copied the
hypothesis pattern from `d_multiset_forced`, whose conclusion is about `t 0`,
`t 1`, `t 2` *specifically* — where three `have`s are sufficient. Fixed with
`intro i` + `fin_cases i <;> omega`.

Two reusable lessons, the second more expensive than the first:

1. **A `∀ i` conclusion over `Fin n` needs case analysis, not three `have`s.**
   The sufficient-for-a-concrete-index pattern looks identical and is not.
2. **Read the error's line number against the declaration boundaries before
   theorising.** I attributed an error to the declaration *after* the one that
   raised it, rewrote a correct proof, and spent a second four-minute
   verification confirming nothing. Lean reports the first error only, so a
   later declaration's status was never in evidence either way.


---

## Lean GREEN on the fourth run — three declarations, one dropped (2026-10-11)

`folio/quantum-observable-universe/lean/QOU/StandardModel/SignCoherentTwist.lean`,
`lean -DautoImplicit=false -s 65536`, exit status captured directly:

    rc=0   0 diagnostic lines   0 sorry   0 axiom   0 native_decide   0 ': True'

| decl | hypotheses | gives |
|---|---|---|
| `u_multiset_forced` | `hrange`, `hsum = 2` — **no `SignCoherent`** | `u = {0,1,1}` in one of three orderings |
| `no_mixed_sign_at_total_two` | `hrange`, `hsum = 2` | `0 ≤ t 0 ∧ 0 ≤ t 1 ∧ 0 ≤ t 2` |
| `no_negative_of_positive_total` | `hsum > 0`, `hcoh` | mirror of `no_positive_of_negative_total`, general positive case |

Contrast the existing `d_multiset_forced`, which **does** take `SignCoherent`
and provably needs it (`d_mixed_sign_not_coherent`).

### `coherent_of_total_two` — DROPPED, and why that is the honest disposition

`SignCoherent t` at total `2` is **true** and follows from
`no_mixed_sign_at_total_two`. Stating it needs `0 ≤ t j` at the existential's
**arbitrary** index, i.e. the `∀ i, 0 ≤ t i` form, and that form is not cheaply
available: `fin_cases i` leaves goals mentioning `t ((fun i => i) ⟨0, ⋯⟩)`, a
beta-redex `omega` will not identify with the `t 0` of `hrange 0`. The proof
fails on `Fin` normalisation, not on mathematics.

Per the three honest dispositions (prove / state-with-`sorry`+`-- Ref:` / drop),
**drop** was correct here because nothing consumes it and the finding does not
rest on it. A docstring in its place records the obstruction so the next agent
does not rediscover it.

### Four rounds, three of them my own error — the reusable part

| run | result | what I believed | what was true |
|---|---|---|---|
| 1 | `rc=1`, 1 error `:300` | the error was in `coherent_of_total_two` | **wrong declaration** — `:300` is the closing `omega` of `no_mixed_sign_at_total_two` (begins `:293`); `coherent_of_total_two` begins `:303` |
| 2 | `rc=1`, **identical** | fixed by rewriting that proof | confirmed nothing; four minutes spent rewriting a proof that was never the problem |
| 3 | `rc=1`, 2 errors `:301` | real bug: `∀ i` over an arbitrary index supplied with only `hrange 0/1/2` | correct, and the fix exposed a *second* layer — the `fin_cases` beta-redex |
| 4 | `rc=0` | — | restated concretely + dropped the corollary |

Three lessons, in order of how much they cost:

1. **Check the error's line number against the declaration boundaries before
   theorising.** Lean reports the **first** error only, so a later
   declaration's status is not in evidence either way — I read silence about
   `coherent_of_total_two` as information about it.
2. **A `∀ i` conclusion over `Fin n` needs case analysis, not three `have`s.**
   The sufficient-for-concrete-indices pattern (`d_multiset_forced`) looks
   identical and is not. I copied it across that boundary.
3. **`fin_cases` is not the end of it.** It discharges the quantifier and
   leaves terms `omega` cannot match. On `Fin 3`, prefer stating the concrete
   conjunction, which is what every consumer wants anyway.

### A grep gate this file would have failed forever

After the drop, `grep -c '\bsorry\b'` on this file returned **1** — matching my
own docstring sentence *"Dropped rather than left as a `sorry`"*. No real
`sorry` existed: the match sat inside a `/-! … -/` block, and `rc=0` with
**zero** diagnostic lines is independent proof, since Lean warns
`declaration uses 'sorry'` for every real one.

This is the trap the corpus already records elsewhere — *"every `sorry` match
in them is a docstring saying 'no `sorry`'"*. Reworded to *"left unproved"* so a
word-grep gate reads 0, rather than leaving a permanent false positive for
whoever runs one next. Re-verified after the reword: the edit is inside a
module docstring and cannot change elaboration, but it was re-run rather than
assumed.


---

## 🛑 CORRECTION to this bean's own open-set list: "chirality is untouched" is WRONG (2026-10-11)

The appends above list, among what stays open:

> **Chirality is untouched** (`qou-wqto`): no braid word separates `u_L` from
> `u_R`, and nothing above addresses it.

That is `qou-wqto`'s **title**, which is stale against `qou-wqto`'s **body**.
Measured: the grading is **constructed** (V10, 2026-08-16,
`ChiralityGradingConstruction.lean`, `rc=0`, 16 declarations) and reproduces the
corpus's own chirality bit pointwise on all eight gen-1 states; Type-B folding
is **excluded** from supplying the involution (V11,
`TypeBFoldingChiralityObstruction.lean`, `rc=0`), because V10 needs the
involution fixed-point free while the folding conjecture fixes stable matter by
construction.

What is actually open on `qou-wqto` is narrower: **the geometric identification
of the Reeb involution on the physical state space** (CR geometry), whose only
corpus statement is a one-paragraph content block that asserts it.

**This is the same error as the `htw2` correction above, one bean over** — and I
made it in the same append that recorded the `htw2` lesson. The common cause is
reading a title out of a bean **listing**, where no body is visible; it is not
about `scrapped` status, since `htw2` is scrapped and `wqto` is `todo` and both
failed identically. Full record on `qou-wqto`.

Nothing else in this bean's open set changes: the total is still pinned by
`T = 3Q`, `hrange` is still an input, the `1/3` normalisation is still the helon
precedent, and `conj:sm-hypercharge-invariant` stays open.

## Progress (2026-11-16, PR #8200)
- [x] Formalized `writheSignLeptonNumber`, `scaledLeftHypercharge`, `carrier_writhe_sign_and_hypercharge_cancellation`, and `writheSignLeptonNumber_neg` in `folio/quantum-observable-universe/lean/QOU/Eightfold/TauAnchoredRatioChiralBraidWritheAndSpectralCubicPowerSums.lean` + 50-dps mpmath witness (`qou_h0zz_chiral_carrier_writhe_and_hypercharge_cancellation`) in PR #8200 (`ec7070e7f1b47f4548cd7f98fc2a7948b28854b0`).



## 2026-11-17 sibling sweep
2 of 4 chiral-fermion words still to scope. PR #7712, branch claude/chiral-fermion-word-scope-2026-10-10. Left: the last two words, then PR review.
Recorded 2026-11-17 from the stale-sibling-session sweep (table: /mnt/project-files/qou-sibling-consolidation/table.md). Source session archived; work not lost.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8200, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-10-12: "qou-h0zz: the lepton half of the braid-word blocker is already derived"). The work may be partly or fully done. Read the bean before you close it.
