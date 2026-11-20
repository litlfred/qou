---
# qou-q8vl
title: 'b_3''s three-way wrong sign has ONE root: every derived bond scalar is confined to (0,1), and uniform attraction does not escape it'
status: todo
pr: 8278
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T12:28:23Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

## Resolved as far as it goes: ONE root, and the stated escape is insufficient

Branch `claude/b3-sign-one-root-2026-09-12`, PR #7226.
Lean `QOU/MassTheory/B3SignOneRoot.lean` (13 decls, sorry-free, `lake build` exit 0).
Probe `computations/probes/b3_sign_one_root_probe.py` (10/10, exit 0, 60 dps).
Audit `docs/audits/2026-09-12-b3-sign-one-root-and-the-insufficient-escape.md`.

### The finding

The three wrong-sign routes (#7193 count channel, #7198 Ursell, #7200 dominant
summand) are ONE failure. Every production interface letter is `σ + d·1` with
`d ≤ 0` — `pp = (1,0)` bare σ, `nn = (1,−h)` which IS σ⁻¹ (`μ_nn = 1/(q(q²+1))`,
`|dev| 0.0` at 50 dps), `pn` colour-weighted between them — so every bond factor
is confined to `(0,1)`, and that decides the sign in all three settings.

### 🛑 The correction to the escape hatch

The Ursell audit §4 and the AGENTS.md extensive-term bullet say a positive term
"needs a bond factor above 1". **Necessary, not sufficient.** The production
`A=3` word is a CHAIN, so `φᵀ₃ = g₀₁·g₁₂` — a PRODUCT — whose sign is invariant
under flipping BOTH bonds. Measured: reflecting every live bond to attractive
leaves `b₃` byte-identical (`−0.293278112721` ³H, `−0.190468485549` ³He).
A two-bond chain needs **exactly one** bond above 1.

Also: the chain is covered by NEITHER standing theorem. `b3corpus_neg` needs all
three bonds strictly inside `(0,1)` and the absent bond sits at exactly 1;
`wMult_b3_nonpos` is the equal-bond case and the chain bonds differ by ~0.105.

### The required pattern is the two-nucleon spectrum

Exactly the two SIGN-MIXED assignments make both chains positive: `g_pn` opposite
to both like-pair bonds. Since `B = −α·log μ > 0` iff `μ < 1`, that is "unlike
pair binds, like pairs do not" — deuteron bound, diproton and dineutron unbound.
The live model binds all three, dineutron most. **`b₃ > 0` and the correct
two-body isospin structure are ONE condition.**

Both derived families excluded: production letters by `d ≤ 0`; isospin projectors
by an IDENTITY, `μ₊ + μ₋ = 1` (symbolic residual 0, any `z`, any `q`), so an
attractive channel forces its partner to `μ < 0` where the log is not real.

### Two claims of mine the probe refuted

* **"even powers attract, odd repel" is FALSE.** Measured `m = −2…+8`: `μ > 1` at
  `m = 2,4,5,6,7,8` — **+5 and +7 are odd**. A two-data-point extrapolation from
  `μ(σ²) > 1 > μ(σ³)`. Reproduces the corpus's stacked-bond table independently.
* **"a bond above 1 is the only escape" is FALSE.** `b3Agg_nonneg_of_convexOn`
  (`qou-82mc`) gives `b₃ ≥ 0` with every bond still inside `(0,1)`.

### Status: this bean stays OPEN, and `qou-brng` is untouched

σ² is NOT proposed — `qou-kj4v` records that the topological argument selecting it
runs backwards (binds the diproton, unbinds the deuteron), and adopting it because
it yields `b₃ > 0` is selection against the target. Magnitude is untouched. What
is open: a THIRD bond family that supplies the sign-mixed pattern by derivation,
and the convexity route, which is unanalysed here.


## 2026-09-12 (session stalled-agent-takeover, PR pending) — the open "third bond family" item is NARROWED at the structure level

This bean excludes the two derived families at the VALUE level (production letters
by `d <= 0`; isospin projectors by `mu_+ + mu_- = 1`) and records as open: *"a THIRD
bond family that supplies the sign-mixed pattern by derivation"*.

**The pn letter is not an independent third value — it is an AVERAGE, and an average
is never an extremum.** The required pattern `mu_pn > 1 > mu_pp, mu_nn` makes `mu_pn`
the strict MAXIMUM of the three. But `d_pn = (1/2 + delta/4) d_pp + (1/2 - delta/4) d_nn`
with both weights strictly positive for `delta in (-2,2)`, and the interface law
`mu = z + d` is affine, so `mu_pn` is a strict convex combination of `mu_pp` and
`mu_nn` — strictly between them, for EVERY `q`, EVERY admissible `delta`, and every
pair of like-pair offsets, whatever their values.

**Consequence for the open item:** a third bond family cannot rescue the pattern by
moving letters above 1. It must break the AVERAGING of the pn letter, or break
AFFINENESS of the interface law. Those are the only two hypotheses used, and neither
mentions a numerical value.

Lean `QOU/MassTheory/PnBetweennessBlocksSignMixed.lean` (6 decls, sorry-free,
lean-direct `-DautoImplicit=false -s 65536` exit 0, zero warnings, axioms
propext/Classical.choice/Quot.sound only). Probe
`computations/probes/pn_betweenness_blocks_sign_mixed_probe.py` 8/8, 70 dps, proton
pin, convention D, no float64 — including a CONTROL row showing the pattern becomes
satisfiable the moment `mu_pn` is unpinned from the average, which is what
establishes that the hypothesis and not the values carries the exclusion. Audit
`docs/audits/2026-09-12-pn-betweenness-blocks-sign-mixed.md`.

Scope (b); invariant = strict convexity + affineness. NOT claimed: that no third
family exists. Magnitude untouched. Composes with the existing
`the_pn_bond_is_an_average_and_cannot_be_extremal_probe`, which established the
ordering `L_pp < L_pn < L_nn`; this adds what it means for the `b_3 > 0` requirement
specifically, which that probe predates.


## 2026-09-13 — the escape wording here is now WRONG, and a sibling PR is building on it

This bean records the escape as *"It must break the AVERAGING of the pn letter,
or break AFFINENESS of the interface law."* Both halves are superseded by
`QOU/MassTheory/InterfaceMonotoneBlocksSignMixed.lean` (on `main`, merge
`3cb26d4b9f8`):

- **Affineness is the wrong invariant — MONOTONICITY is.**
  `pn_not_strict_max_of_monotone` holds for **any monotone interface law, affine
  or not**; `signMixed_impossible_of_monotone` is the corollary against this
  bean's own `signMixedPattern`. So abandoning affineness buys **nothing**.
- **Averaging is not separately breakable.** `between_iff_combo` — over an
  ordered field, "`d_pn` strictly between `d_pp` and `d_nn`" and "`d_pn` is a
  convex combination" are the **same** condition, weight `w = (b−c)/(b−a)`.

So the disjunction is one-and-a-half hypotheses, not two, and the live statement
is: **a third bond family must put `d_pn` OUTSIDE the interval spanned by
`d_pp` and `d_nn`, or use a NON-MONOTONE interface law.** The narrowing is sharp
— `nonmonotone_escape_exists` exhibits `f d = 1 − (d−1)²` — so this is a real
door, not a disguised impossibility.

**Urgency:** PR #7287 (`qou-ix0x` Option 1, γγ junction) quotes the old wording
and rests its escape on *"a length-6 word is not `σ + d·1`, so it breaks
affineness."* That step does not escape. Flagged on that PR
(`#7287` comment, 2026-09-13).

**Still OPEN and NOT closeable** (§13a): the third bond family is an open
derivation. Only the *escape question* is closed, as a question.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-13 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Progress Update (PR #8278 — `status: in-progress`)

- [x] Formalized pure Lean 4.24.0 module(s) (`QOU/MassTheory/IsospinChannelReachabilityAndB3ChainSign.lean`, `QOU/MassTheory/PeeledMarkovDefectAndHigherInterleaving.lean`, `QOU/MassTheory/GradedLogPairCancellationAndH3TowerCollapse.lean`) with `0 sorry` and `0` findings across all 6 static vacuity audits.
- [x] Added 50-dps `mpmath` probe `computations/probes/isospin_b3chain_markov_defect_logjet_h3tower_probe.py` and 2-commit stamped witness `computations/probes/isospin-b3chain-markov-defect-logjet-h3tower-probe.witness.json` (`allPassed: true`, `0` raw `float64`).
- [x] Opened and signed [PR #8278](https://github.com/litlfred/qou/pull/8278) (`ready: b3288da132ea8d0d185d184a5e18432c89e4858e`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8278, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
