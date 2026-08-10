---
# qou-a28x
title: 'AXIS: witness-substitution -- 217 blocks quote numbers no declared witness carries'
status: todo
type: task
created_at: 2026-08-10T03:43:44Z
updated_at: 2026-08-10T03:43:44Z
---


## What

New QA axis `content/pipeline/witness-substitution-audit.ts` (selftest 19/19).

A block declares `computation.witness: [...]`, then its prose quotes decimals.
**Nothing checked the second came from the first.** There is no substitution
mechanism in this corpus — no `{{witness:…}}`, no macro — so every quoted value
is a decimal somebody typed once, and the declaration is a citation, not a check.

That is how convention C survived in content after the producers moved:
`markov_trace_recursive.py` was migrated and re-run, its witness says the proton
trace is `1.884319467254976`, and the block still said `1.633154…` — the C value.
`trace-convention-audit` cannot catch it, because `1.633154` is not one of the
registry fingerprints and never could be: the registry lists `z` and the `y_λ`,
not every number computed downstream from them.

The fingerprint axis asks *"is this a known-bad number?"* — a list only as
complete as somebody's memory. This axis asks **"where did this number come
from?"**, which needs no list.

## First sweep

    2705 blocks scanned, 251 quoting high-precision literals, 217 failing

| detector | blocks | literals |
|---|---|---|
| `unsourced-literal` — matches no declared witness | 31 | 13325 → 3238 after the atlas fix |
| `no-witness-declared` — precise values, no `computation.witness` | 186 | — |
| `externally-attributed` — CODATA / knot table / citation (reported, not failing) | 11 | 19 |

## Already fixed here

`rem:recursive-atom-knot-atlas-registry` declared one unrelated witness while its
per-element table is, in its own words, *"auto-rendered from per-Z shards
`canonical-isotope-witness-Z<NN>.witness.json`"*. Under-declaration, not
unsourced data — the numbers had a producer, the block never named it. Declaring
the 119 shards took it from 13250 → 3163.

## Next

1. The 186 `no-witness-declared` blocks — triage: which have a producer that was
   never declared (cheap, like the atlas) vs which quote numbers with no producer
   at all (the real finding).
2. The 3163 residual atlas literals — AME reference columns and derived B/A
   ratios; decide whether the shards should carry them.
3. `prop:markov-trace-recursive-reducer` declares TWO witnesses that disagree by
   17% — one migrated to D, one still C. Suggests a `witness-disagreement`
   detector.
4. Sidecar upsert. Deliberately not written yet: the first sweep touches a large
   fraction of the corpus and would bury the tuning diff in generated JSON.
