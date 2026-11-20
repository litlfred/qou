---
# qou-x0su
title: 'GAP: CoordinationSaturation''s premise is not instantiated in the channel binding_canonical uses'
status: todo
pr: 8284
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-31T03:09:04Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

## The finding (branch `claude/binding-channel-arity-2026-08-31`)

Following `qou-brng`'s claim that both live bond sets are excluded from opposite
directions. The chain half checks out (measured, merged in #6304). **The
complete-graph half does not apply to the producer it is cited against.**

### The arity gap

`QOU.Mass.CoordinationSaturation.complete_graph_no_saturation` is about

    perNucleonComplete ε A := ε * C(A,2) / A

— binding **ADDITIVE** in the bond count, uniform per-bond `ε`. The live
canonical producer computes something else. `closed_form_tau_M` builds
`tr_M = tr_p^Z · tr_n^N · ∏_bonds f_i` (MULTIPLICATIVE) and
`binding_canonical.py:528-533` reads binding off it as the **observe-early trace
difference** `B = Q_β·|tr_free|·(1 − ∏f)`. It computes the log-like form too and
labels that one **REFUTED**.

`Σ` over bonds is `ε·M`; `1 − ∏` is bounded by 1 whatever `M` is. Different
functions of `M`, so the theorem's premise is instantiated in one and not the
other. Measured (proton pin, 50 dps, `binding_channel_saturation_probe.py`):

| channel | chain | complete graph |
|---|---|---|
| free energy `−log(∏f)/A` | 0.338 → **0.681**, plateaus | 0.338 → **13.40**, grows ≈ 0.344·A |
| observe-early `Q_β·\|tr_free\|·(1−∏f)/A` | — identical to complete from A=12 — | |

**In channel 1 the exclusion reproduces exactly** — `ε = −log f > 0` for all three
factors, so the hypothesis is met and the dichotomy is the corpus's own. Good.

**In channel 2 the bond set is asymptotically invisible.** `1 − ∏f` reaches
1.0 by A=12 (chain) and A=8 (complete); the two bond sets' B/A agree to **10
significant figures** from A=12 on, and are bit-identical by A=40. So
`complete_graph_no_saturation` cannot discriminate them there.

### What actually drives channel 2, with a check that could have failed

`B/A` is set by the constituent factor `|tr_p|^Z|tr_n|^N`, not by coordination.
Falsifiable prediction, no fitting: on the N=Z chain `|tr_free|/A = c^(A/2)/A`
with `c = |tr_p·tr_n| = 1.13171690432`, whose minimum is at `A* = 2/ln c`.

    predicted A* = 16.163   measured argmin over A = 4,6,...,40 : 16   AGREE

### And no bond set rescues it

`(1 − ∏f) ∈ [0,1)` for every bond set, since every `f ∈ (0,1)`. So
`B/A ≤ Q_β|tr_free|/A` universally, and a plateau needs `|tr_free| ~ A` — an
exponential is asymptotically linear only at `c = 1`, where it is constant and
`B/A → 0`. Measured `ln c = 0.1237 ≠ 0`, so `B/A` diverges. Bound, not a search.

### Consequence for `qou-brng`

The saturation constraint driving the bond-set search is, **in the channel the
canonical producer uses**, a constraint on the constituent term `tr_p^Z tr_n^N`
rather than on coordination. Searching bond sets against it cannot succeed there.

Not a refutation of the Lean, which is correct as stated, and not a claim that
channel 2 is the right channel. It is a scope label the citation is missing —
`CoordinationSaturation`'s own docstring says it "excludes the complete-graph
z = A−1", which is true of the additive ansatz and not of `binding_canonical`.

### Limits

Measured on the corpus's own closed-form factorisation, not on the direct Hecke
trace `binding_canonical` evaluates; if those disagree, the channel-2 rows move.
Scope (a) throughout.


## 🛑 CORRECTION to my own entry above (same session, before merge)

Three claims in the entry above were wrong. Corrected in the probe, the PR body
and here. The substantive channel finding survives; the framing did not.

**1. `B_late` is NOT a log channel.** I wrote that `binding_canonical` "computes
the log-like form and labels it REFUTED". Read at `binding_canonical.py:522-539`:
`B_late = Q_β·Σ_λ y_λ(θ_free[λ] − θ_atom[λ])` with `θ = acos(χ/dim)` or
`acosh(|χ|/dim)` — an ANGLE per Wedderburn block, summed over partitions, not
over bonds. Its `# refuted: small/neg/shrinks` note says nothing about the
free-energy channel.

**2. The free-energy channel is LIVE, and my Channel 1 duplicates it.**
`computations/derived_bond_graph_binding.py:170-171` computes
`B_chain = E0*sum(log(1/f[b]) for b in cb)` and `B_complete` over `C(A,2)` — the
same three factors, the same comparison, against AME. I first grepped `mp.log`
and concluded the channel existed "only in `_deprecated/`"; that producer uses
`math.log`, so my grep could not see it. **My Channel 1 is an independent
re-derivation and is now cited as such, not offered as new.** This is a
corpus-grep miss on my part: path 3 (`computations/`) would have caught it with
a less specific pattern.

**3. `binding_canonical` uses the CHAIN, not the complete graph.** It calls
`atom_braid_word_3A(Z, N, include_inter=True)`, which I had myself measured to be
`A−1` bonds. So it is not the producer the complete-graph exclusion is about —
`build_atom_nf` / `build_atom_nf_sym` is. The PR title said "the channel
binding_canonical uses", which conflated channel with bond set.

### What survives, unchanged

* The arity gap itself: `complete_graph_no_saturation` is about additive `ε·M`;
  the trace-difference channel enters through `1 − ∏f`, bounded by 1. Two live
  channels, and the exclusion is a statement about one of them.
* Channel 2's measurements: the bond sets agree to 10 significant figures from
  A=12; `A* = 2/ln c = 16.163` against measured argmin 16; and the bound showing
  no bond set can plateau there.

### Two defects found in `derived_bond_graph_binding` while checking (not fixed)

* **Stale docstring convention.** Line 18 declares `z = 1/(q^½+q^{-½})`
  (convention C); line 78 computes `q0**3/(q0**2+1)` (convention D). The body is
  right. Same defect class as the `markovZc` docstring (bean `qou-961o`).
* **NO-FLOAT64 violation in a live witness-emitting producer.** Line 77 is
  `q0, h, me = float(q0), float(h), float(me)` and the binding is accumulated
  with `math.log` — float64 end to end, and it writes
  `derived-bond-graph-binding.witness.json`. Worth its own bean.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-31 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR #8284 — `status: in-progress`)

- [x] Formalized pure Lean 4.24.0 module(s) (`QOU/MassTheory/PhiQTowerConvexityAndGramRankFive.lean`, `QOU/MassTheory/ChainOrderingSpreadAndOneRowUrsellIdentity.lean`, `QOU/MassTheory/CoordinationChannelAritySeparation.lean`) with `0 sorry` and `0` findings across all 6 static vacuity audits.
- [x] Added 50-dps `mpmath` probe `computations/probes/phi_q_convexity_gram_rank_chain_ursell_arity_probe.py` and 2-commit stamped witness `computations/probes/phi-q-convexity-gram-rank-chain-ursell-arity-probe.witness.json` (`allPassed: true`, `0` raw `float64`).
- [x] Opened and signed [PR #8284](https://github.com/litlfred/qou/pull/8284) (`ready: d9d87101718b841adc62a2d83ad74df6ff4798e4`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8284, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
