---
# qou-x0su
title: 'GAP: CoordinationSaturation''s premise is not instantiated in the channel binding_canonical uses'
status: in-progress
type: task
priority: normal
created_at: 2026-08-31T03:09:04Z
updated_at: 2026-08-31T03:09:43Z
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
