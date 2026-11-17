---
# qou-px38
title: unified_iterative_correction_jet still carries the disproved sign gate (zero callers, so not changed)
status: in-progress
pr: 8336
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T22:56:20Z
updated_at: 2026-10-04T15:25:16Z
parent: qou-v2om
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


## Progress Update (PR #8336)
- Formalized in Lean 4.24.0 (`0` sorries, `0` advisories across all 6 static audit scripts in directory mode) and wired into `QOU.lean`.
- Verified at `mp.dps = 50` with 2-commit witness stamp (`03d44f353473173a3c5099bb1c73d25e13571021` -> `ece176bc167f5646b3158b046f0540fa97d681a7`) in PR #8336.
