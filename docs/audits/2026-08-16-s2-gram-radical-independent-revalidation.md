# S2 — the Markov–Gram radical under convention D: independent re-validation

**Branch** `claude/s2-gram-radical-quotient-2026-08-16` · **Status** IN PROGRESS

## Why this doc exists

The owner asked (2026-08-16) to **re-validate the convention-D Gram
singularity from scratch**, treating every relayed figure as unverified:

> *"can we revalidate singularity...maybe probes wrong/old. what
> implications? resolution options?"*

and to test a specific structural framing — that a corank-1 Gram
degeneration at a special parameter is the Graham–Lehrer signature of a
**cell module becoming reducible**, in which case quotient-by-radical is
the standard construction rather than a repair hack.

## Relayed claims under test (NONE assumed true)

| # | Relayed claim | Source | Verdict |
|---|---|---|---|
| R1 | D-frame Markov–Gram has corank 1 | prior probe | TBD |
| R2 | corank n=4: 10, n=5: 78 | prior probe | TBD |
| R3 | `np.linalg.inv` returns entries to 7.6e15, ‖G·G_INV − I‖ = 1.64 | prior probe | TBD |
| R4 | `G_INV` computed at import; 13 modules re-export `z`, 13 consumers | prior probe | TBD |
| R5 | sibling `qou-nr8y`: the C in `pyhecke.gram` is load-bearing | branch `claude/conv-c-shared-root-2026-08-16` | TBD |

## Method

Exact/symbolic first (sympy over ℚ(q)), float64 never load-bearing.

(sections filled in as the work lands)
