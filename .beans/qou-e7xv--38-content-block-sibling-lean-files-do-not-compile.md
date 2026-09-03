---
# qou-e7xv
title: 38 content-block sibling .lean files do not compile — nothing in the corpus checks them
status: todo
type: task
priority: normal
created_at: 2026-09-03T22:46:23Z
updated_at: 2026-09-03T22:47:07Z
---

Audit: `docs/audits/2026-09-03-sibling-lean-compile-sweep.md`
Data:  `docs/audits/2026-09-03-sibling-lean-compile-sweep.tsv`

## Measured 2026-09-03

`lean`-direct on all 908 `.lean` under `content/quantum-observable-universe/`
outside `lean/`, then EVERY failure re-verified under a widened LEAN_PATH:

    raw failures                                        41
      harness: QOU-only LEAN_PATH, file imports UGB     -1
      harness: `import Mathlib` (aggregator olean absent) -2
    REAL                                                38   (4.2 %)

Both harness classes confirmed by re-running, not by inspection.
`vertex-algebra-relations.lean`: `unknown module prefix 'UGB'` under a
QOU-only path, exit 0 with all three paper packages. `Mathlib.olean` is
genuinely absent from the restore, so two files that `import Mathlib`
wholesale fail for a reason a real `lake build` would not have.

## Why nothing caught them

Siblings sit outside the Lake globs (`globs = ["QOU", "QOU.+"]`,
`srcDir = "."` = the `lean/` dir), so `lake build QOU` never sees them; CI is
`workflow_dispatch`-only; `lean-content-siblings.yml` gates content-block
siblings, not these.

## Largest shared causes

- `Inv GroundRing.R_q` fails to synthesise in **5 files** — ONE missing
  instance on the corpus's own ground ring, not five independent defects.
  Highest-leverage single fix in the list.
- 4 files fail at the PARSER.
- Mathlib drift: `Real.tendsto_log_mul_rpow_nhdsGT_zero`,
  `MonoidalCategory.whiskerRight_comp` -> `comp_whiskerRight`.
- `delta-max-uniform-bound.lean` imports `QOU.MassEndomorphism.JetTower`,
  which does not exist in source, and `QOU.BraidsAndKnots.MarkovTrace` where
  the tree spells the namespace `BraidKnot`. Absent olean AND absent source
  is what distinguishes this from a harness gap.
- Worst single file: `spin-involution-lp-dual-invariance.lean`, 24 errors.

## Scope

A sibling failing to compile is NOT automatically a false claim — most are
stale references and missing instances, not wrong mathematics. It means the
block's `lean.ref` points into a file that does not typecheck, so the
formalisation cannot be relied on as stated. Triage per file; do not read 38
as 38 refuted propositions.

## Already partly done on this branch

- `n-v-bring-action.lean` — was 8 parse errors (`Σ` used as a binder name);
  now exit 0, zero warnings, and its axiom + self-discharging instance removed.
- `braid-action-tensor.lean` — 5 errors -> 2 (bean `qou-8qby`).
