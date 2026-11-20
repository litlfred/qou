---
# qou-9xla
title: 'PRODUCER (missing): prf:interface-knot-markov-z''s 4-atom table has no producer -- write one, regenerate under D'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T22:49:46Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---


## What this bean found instead

The task was: write the missing producer for `prf:interface-knot-markov-z`'s
4-atom table. The producer to build on is `computations/mass_at_3A_proper.py`
(`atom_braid_word_3A`, `markov_trace_3A`). Line 76 of that file:

```python
Z_MARKOV = 1.0 / (Q0 ** 0.5 + QI ** 0.5)
```

**Convention C.** The producer needed to regenerate the convention-C table is
itself convention C, and it is not in the 13-file list this branch has been
working from.

## THIRD measurement of the producer surface, and the first trustworthy one

| when | method | answer |
|---|---|---|
| first | grep with a bare `0.5 + ` alternative | **70** — false positives, matched unrelated arithmetic |
| second | "tight" grep, hand-listed spellings | **13** — missed most spellings |
| **third** | **AST walk, `scripts/convention-c-producer-audit.py`** | **178 actionable sites** |

Both earlier numbers were wrong, in opposite directions, and I reported both.

**Why grep could never work here.** The corpus spells this at least fifteen
ways — `mp.sqrt` / `sp.sqrt` / `np.sqrt` / `**0.5` / `**(-0.5)` /
`**mpf('0.5')` / `**mpmath.mpf('0.5')`, with the reciprocal named `q0`, `qi`,
`qi0`, `QI`, `Q_INV`, `_QI0`, `sqrt_q`, `q_val` or inlined, bound to `z`,
`z_mark`, `z_markov`, `Z_MARKOV`, `z_sym`, `zmkv`, `ZS`, `z_q`, `_z`, `z0`, `Z`.
Any regex tuned to a subset misses the rest; a looser one matches noise. Both
happened, in that order. Only shape-matching on the AST catches all of them.

### Stratified (AST-verified)

```
 119 sites / 104 files   computations — live producers
  56 sites /  49 files   probes / exploratory
   4 sites /   2 files   tools/pyhecke — BLOCKED on C by design (registry)
   2 sites /   2 files   qou-mass — SHIPPED PACKAGE          <-- priority
   1 site                sweeps
   6 sites               deliberately C-named (z_C, z_c) — labelled, not defects
```

**`qou-mass` is the shipped package** and is the sharpest item:
- `qou-mass/src/qou_mass/_internal/hecke_characters.py:36`
- `qou-mass/src/qou_mass/_internal/markov_trace_recursive.py:54`

`tools/pyhecke` (4 sites) is the registry's declared `blocked_migrations`
exception — R9 asserts it rather than leaving it undetected — so it is excluded
from the actionable count, not overlooked.

## The instrument is committed

`scripts/convention-c-producer-audit.py`, with a `--selftest` (15/15) whose
fixtures are the real corpus spellings plus the convention-D forms that must NOT
match. It found a genuine bug in itself on first run: `ast.unparse` emits
`q ** 3`, so the `"**3"` guard never fired and `1/(q**3 + q**0.5)` was wrongly
matched. Fixed by whitespace-normalising.

This is the producer-layer counterpart to
`content/pipeline/trace-convention-audit.ts`, which walks `content/**` only.
Nothing walked the producers, which is why this went unmeasured for so long.

## NEEDS OWNER — scope

178 actionable sites is not the "13 files, reviewable" change reported earlier,
and it is not something to start unilaterally. The layers differ in risk and
should probably be sequenced, not swept:

1. **`qou-mass` (2 sites)** — shipped; highest consequence; do first.
2. **`computations` live producers (119)** — each drags its witnesses. Many may
   be convention-scoped anyway and need auditing individually, not substituting.
3. **`probes` (56)** — exploratory; a C-era probe computing a C-era number for
   its own consumption may be legitimate history. Cheapest to leave, but they
   should at least be labelled so they stop reading as production.

The blast-radius question from `qou-emyt` stands and is now much larger: the
registry records 195.8 ppm on β_Bor and −197 ppm on m_p for the channels already
migrated.

## Not done

The atom-table producer itself. It cannot be written honestly on top of
`mass_at_3A_proper.py` while that file's `Z_MARKOV` is convention C — the output
would be C numbers wearing a fresh witness. Blocked on item 1/2 above, or on a
decision to parameterise that producer by `z` explicitly.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-09 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8313, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
