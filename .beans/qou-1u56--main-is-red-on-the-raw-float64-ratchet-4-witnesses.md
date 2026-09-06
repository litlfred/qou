---
# qou-1u56
title: 'main is RED on the raw-float64 ratchet: 4 witnesses regenerated without a baseline update'
status: todo
type: task
priority: normal
created_at: 2026-09-06T13:28:11Z
updated_at: 2026-09-06T13:28:48Z
---

## Measured on `main`, not on a branch

The raw-float64 ratchet reports **4 REGRESSED** and a net **−38 fields** on a
tree freshly rebased onto `origin/main`. All four are `main`'s:

| baseline | live | witness |
|---|---|---|
| 25 | 55 | `probes/he4-channel-split-categorical-constraint-probe.witness.json` |
| 23 | 34 | `probes/he4-partition-dominance-audit-probe.witness.json` |
| 7 | 18 | `probes/option-a-vol-per-knot-light-series.witness.json` |
| 24 | 26 | `probes/he4-9-3-trace-dominant-correction-probe.witness.json` |

**Attribution is byte-exact, not inferred.** All four files are
`sha256`-identical to `origin/main`, and `origin/main`'s **own**
`raw-float64-baseline.json` still carries the OLD counts (25 / 23 / 7 / 24).
So the witnesses were regenerated and the baseline was not updated in the same
change — the ratchet is red on `main` independently of any branch.

Traced to two commits, both of which regenerate witnesses in bulk:

- `9b009da0e6e` — *"rebase(6854): integrate 485 commits of main, and RE-DERIVE
  the six conflicting witnesses rather than picking a side"*
- `3cc4b2aab10` — *"sweep(qou-92u9): 64 downstream producers run — 50 witnesses
  refreshed, and the new word BREAKS A ROUTE rather than just moving its
  numbers"*

Both did the right thing by the witnesses. Neither re-ran the ratchet.

## Why I did not just fix it

The ratchet is **drain-only**: `--rebaseline` floors every entry at its previous
value and prints `NOT BANKED` for anything that would grow, precisely so an
agent cannot make a red run green by widening the baseline. These four *would*
grow. Banking them is the move AGENTS.md forbids in as many words —
*"NEVER make a red run green by widening a baseline… baselines drain, never
grow."*

So there are exactly two honest resolutions and both need someone who has read
these producers:

1. **The growth is real and wanted** — the regenerated witnesses legitimately
   carry more float64, in which case the four entries need a deliberate,
   reviewed baseline raise with the reason recorded. That is a decision, not a
   sweep.
2. **The growth is a defect** — the regeneration introduced float64 where the
   producer previously serialized through `fmt`, in which case the fix is at
   the producer and the baseline never moves.

`he4-channel-split` more than doubled (25 → 55) and `option-a-vol-per-knot`
more than doubled (7 → 18), which leans toward (2), but I have not read those
producers and am not guessing.

## Note for whoever picks this up

The ratchet currently runs **ADVISORY** here (`exit 0` despite the findings), so
this does not block a merge and will not announce itself. That is why it needed
a bean rather than a comment: nothing else will surface it.
