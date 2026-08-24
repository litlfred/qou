---
# qou-goc9
title: 'GAP: which nucleon NF is canonical for the Q_beta counit chain? single-wrap vs typed 6-term differ by 0.579%, 3.6x the phase'
status: todo
type: task
priority: normal
created_at: 2026-08-23T00:54:05Z
updated_at: 2026-08-23T00:54:35Z
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
