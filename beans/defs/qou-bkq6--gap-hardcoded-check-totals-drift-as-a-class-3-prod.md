---
# qou-bkq6
title: 'GAP: hardcoded check totals drift as a class — 3 producers print N/N while N+1 checks execute'
status: in-progress
pr: 8248
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:35:10Z
updated_at: 2026-11-17T07:18:00Z
parent: qou-5vkl
---


Surfaced while draining `qou-srvu` slice E; branch
`claude/srvu-drain-e-2026-08-30`. Reported rather than fixed, because
`checks_total` is a `data` field and silently changing a recorded number
mid-drain is the wrong move.

## Measured — 3 of the 11 check-carrying producers in this slice

| producer | prints / records | checks that actually run |
|---|---|---|
| `computations/qbeta/qbeta_delta_bar_parity_probe.py` | `15/15`, `checks_total: 15` | **16** |
| `computations/qbeta/qbeta_nucleon_selection_rule_probe.py` | `4/4` | **5** |
| `computations/meson/growing_width_cut_shape_exclusion_probe.py` | `7/7 assertions passed` | **9** |

Each computes its tally as a LITERAL minus the failure count, e.g.

    npass = 15 - len(_FAILURES)
    w.add_data("checks_total", 15)

so the literal goes stale the moment a check is added, and nothing notices.

## Why this is worth a bean rather than a one-character fix

1. **It is a class, not three accidents.** Three of eleven, all with the same
   construction. Any producer using this idiom is one added check away from the
   same drift, so the fix worth having is the idiom (`len(_CHECKS)`), not the
   three literals.
2. **It under-reports in the safe direction, which is why it survived.** A
   stale total makes the run look like it ran FEWER checks than it did, so it
   never trips anything — the same "fails quietly in the reassuring direction"
   shape as the vacuous-green defect itself.
3. **The witnesses now disagree with themselves.** After the `qou-srvu` drain
   these witnesses carry 16 / 5 / 9 assertions beside a `checks_total` of
   15 / 4 / 7. A consumer comparing the two gets a contradiction.

## Suggested fix

Replace the literal with a count derived from the same list the checks are
recorded in, and re-run the three producers. Low risk: it changes one `data`
integer per witness and no computed quantity. Default if nobody acts: the three
witnesses keep a self-inconsistent tally, which is cosmetic but is exactly the
kind of small wrongness that gets quoted later.

## Progress (2026-11-17, PR #8248)

- [x] Derive check totals dynamically from `len(_CHECKS)` in `qbeta_delta_bar_parity_probe.py` (16/16), `qbeta_nucleon_selection_rule_probe.py` (5/5), and `growing_width_cut_shape_exclusion_probe.py` (9/9) and regenerate all 3 witnesses (PR #8248, Commit 1 `d3dcd4c4757a988299ad0246ed502bd2358a90e4`, Commit 2 `b4185f1dac70a76b08299e291f3137fb9b60fe3c`).
- [ ] Merge PR #8248 (`claude/round53-trd0-9nnz-fixes`, HEAD `b4185f1dac70a76b08299e291f3137fb9b60fe3c`)
