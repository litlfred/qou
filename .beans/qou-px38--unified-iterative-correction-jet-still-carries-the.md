---
# qou-px38
title: unified_iterative_correction_jet still carries the disproved sign gate (zero callers, so not changed)
status: todo
type: task
created_at: 2026-09-12T22:56:20Z
updated_at: 2026-09-12T22:56:20Z
---


## The finding

`hecke_core_legacy.unified_iterative_correction_jet` still applies the sign gate
that #7253 removed from `unified_iterative_correction`, in two places:

- the linear terms — `tight = (tr_sign <= 0)`, `gated = cumul if tight else 0.0`;
- the conjugate-pair cross terms — `if tight` / `if tight_either`, gating both
  the self-conjugate `h/2` coupling and the pair-sum `h` coupling.

Its own docstring states the mechanism as *"complementary slackness gate on
final trace sign"*. That justification is **refuted sorry-free** in
`QOU.MassTheory.UICGateNotFromComplementarySlackness` (PR #7251) — four
mismatches plus a scope-(b) invariant; see bean `qou-21oc`.

## Why it was NOT changed

**Zero code callers tree-wide.** Measured 2026-09-12 across the whole repo
(excluding sibling agent worktrees): the only occurrences of the name outside
its own definition are in `.beans/`, one audit doc, and
`docs/audits/2026-05-24-hecke-core-canonical-audit.md`, which classifies it at
row 63 as **EXPLORATORY** with *"no canonical caller"* (rows 8, 59 and 61 name
`partition_jet_depth`, `_jet_witness_path` and `_contrib_single_partition` as
utilities of it, all likewise EXPLORATORY).

So changing it would move no published number while costing a re-run nobody
consumes. A docstring banner was added instead, naming the refutation and this
bean, so the gate's survival there is not read as evidence it is justified.

## What would close this

Either (a) a caller appears, in which case the gate must go before any number it
produces is published; or (b) the function is retired outright, which is the
likelier disposition given the 2026-05-24 audit's classification. **Do not close
this by deleting the function without checking (a) first.**

Related: `qou-ai7v` (the q-Gaussian tier, same argument, also unchanged),
`qou-21oc` (the gate drop).
