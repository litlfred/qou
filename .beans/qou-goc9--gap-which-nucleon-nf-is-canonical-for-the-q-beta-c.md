---
# qou-goc9
title: 'GAP: which nucleon NF is canonical for the Q_beta counit chain? single-wrap vs typed 6-term differ by 0.579%, 3.6x the phase'
status: in-progress
type: task
priority: normal
created_at: 2026-08-23T00:54:05Z
updated_at: 2026-08-28T15:36:52Z
---

Surfaced from `qou-pdix` (PR #5448). Probe:
`computations/qbeta/qbeta_nf_single_wrap_vs_typed_probe.py` (8/8, exact Q(h)
symbolic, validated against the live PROTON_NF/NEUTRON_NF to float64 eps).

## The two objects

| NF | (n-p) support | deg_z E | |eps(n-p)| |
|---|---|---|---|
| single-wrap | {gamma, sigma_0, sigma_1} = crossing-nos {0,1} | 1 | 0.187207 |
| typed 6-term (live `build_nucleon_nf`) | all six = crossing-nos {0,1,2,3} | 3 | 0.188291 |

Both numbers are the ones `docs/audits/2026-05-11-q-beta-residual-decomposition.md`
§1 already quotes (0.18721 / 0.18829), and their ratio is that audit's
**1.00579** "basis-change typed-vs-single-wrap" factor — recomputed here from
scratch rather than transcribed.

## Why it gates

- `docs/audits/2026-06-16-q-beta-net-ansatz-path-a-counit-vs-trace.md`, the Lean
  `epsNP`/`trMNP` defs, and `CrossingWeightAffine.evalMap` all encode the
  **single-wrap** vector. Every affineness / abelian-period conclusion built on
  `evalMap` is scoped to that object and is FALSE for the typed one.
- The live mass compute (`PROTON_NF`, `NEUTRON_NF`) uses the **typed** one.
- The ladder's N=1 factor is a **0.160%** correction; the ambiguity between the
  two NFs is **0.579%** — 3.6x larger. So the phase cannot be derived at all
  until the NF is settled: settling it moves the target by more than the target.

## What would close it

A derivation (not a preference) of which NF the Q_beta counit chain must use —
i.e. why the transition amplitude pairs against a single-wrap rather than a
typed-crossings normal form, or vice versa. The 2026-05-11 audit leaves the
1.00579 as a factor still to be EXPLAINED (it pairs it with the N=0 brane-tower
1.00168 to make the full 1.00744), so the corpus has not chosen.

Scope-(a) throughout: nothing is refuted, neither NF is declared canonical.


## 2026-08-28 — the question is REFRAMED by qou-avt5, and the fork is asymmetric

Corpus-grep (the STRICT checklist) found `qou-avt5` — COMPLETED, and it changes
what this bean is asking.

`qbeta_single_wrap_element_cannot_exist_probe.py` proves scope-(b): NO difference
of typed-crossing words has counit `epsNPq = h(h-2)/2`. Route: eps of any typed
word is `q^m([2]_q/2)^c`; `epsNPq` carries `(q^2-2q-1)` so it vanishes at the
silver ratio; absolute norms in Z[sqrt2] force the difference identically zero
there, which epsNPq is not. Verified here 10/10.

**So goc9's original framing was subtly wrong.** I asked "which of two valid NFs
is canonical". It is not a choice between two admissible objects: the corpus's
DESCRIPTION of Delta (a typed-crossing word difference) and its ASSERTED value
(epsNPq) are mutually inconsistent. qou-avt5 states the fork — prose wrong, or
value wrong — and explicitly declines to adjudicate.

## Independent convergence

My 0.579% gap between the single-wrap and typed counits (PR #5448) is the
NUMERICAL shadow of their STRUCTURAL exclusion. Two routes, same fact, neither
derived from the other.

## New datum, and the limit of it

eps(typed n-p) = 86 at h = 2, where epsNPq = 0. So the live construction SURVIVES
the invariant that kills the asserted value: the horns are not symmetric.
Probe: computations/qbeta/qbeta_counit_silver_ratio_adjudication_probe.py (7/7),
PR #5893.

Necessary, NOT sufficient — this does not prove epsNPq wrong and does not select
horn (b). BEAN STAYS OPEN.

What it buys: horn (a) is now falsifiable. If epsNPq is retained, the real Delta
must have a counit vanishing at h = 2 while not being a typed-word difference.

Also worth recording: h = q - 1/q is EXACTLY 2 at the silver ratio, so epsNPq
vanishes there because it is built with a root at h = 2. The content is the norm
argument; the constant is a red herring.

NEXT: the fork needs the owner of the counit block, or a derivation of epsNPq
from something. Its current status is a bare Lean `def` with no theorem.
