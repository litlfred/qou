# Tranche evidence — restore `def:q-from-epsilon` to the blocks that lost it?

Generated 2026-08-15 by `scripts/prune-tranche-sheet.ts def:q-from-epsilon`. Bean `prn1`.

> **Five of the original ten have been APPLIED** — see "What was applied" below.
> This sheet shows the **remaining five**, which are the ones a reader must decide.

Column meanings, the two-relation caveat, the forward-reference rule, and why a
target-shaped tranche is one question rather than many: see
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.AlgebraicSubstrate.QFromEpsilon`
Sources that lost it and still cannot reach it: **5**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `rem:ns-surreal-bound` | remark | no | no | *n/a — no .lean* | 0 | backward |
| `conj:p-vs-np-qou` | conjecture | no | no | *n/a — no .lean* | 2 | backward |
| `prop:surreal-rate-calculus` | proposition | no | no | *n/a — no .lean* | 1 | backward |
| `rem:adelic-tate-squeeze` | remark | no | no | *n/a — no .lean* | 1 | backward |
| `rem:ns-blowup-physical-evidence` | remark | no | no | *n/a — no .lean* | 3 | backward |

**None of the 5 would point forward if restored.**

**0 of 5 searchable blocks link to the target from their prose** (0 of 5 have no `.md` and were not searched at all).

## What was applied, and on what ground

Five blocks — `rem:millennium-unification`, `rem:bsd-surreal-bound`,
`rem:rh-surreal-bound`, `rem:yang-mills-surreal-bound`,
`rem:p-vs-np-surreal-bound` — now declare `def:q-from-epsilon`.

The ground is structural, not a reading. Each of the five contains the **same
sentence construction**, introducing two definitions together:

> … $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)) …

immediately after linking `def:reeb-epsilon`. **Four of the five already declared
`def:reeb-epsilon` and none declared `def:q-from-epsilon`** — the same sentence,
the same role, one dependency carried and the other not. That is a block's two
halves contradicting each other, which is a defect rather than an editorial
choice, and it is the case the `uses-editorial-review` skill names as not
requiring two readers because nothing is being judged.

(`rem:millennium-unification` declared *neither*, while linking both. Only
`def:q-from-epsilon` was added, since `def:reeb-epsilon` is a different tranche's
question. Recorded rather than folded in silently.)

Verified before applying, not asserted:

- `def:q-from-epsilon` uses only `def:reeb-epsilon` and **cannot reach any of the
  five**, so no cycle is created. The editorial graph is still acyclic — 0
  cycles corpus-wide, preserving the property #4881 established.
- **None of the five points forward.** The restored edges cannot regress
  `detangler-no-forward-ref`.

## What remains

The five below carry **no prose link** to the target. The self-contradicting
subset is fully drained, so what is left is exactly the residue where a reader's
judgement decides something — which is the right place for the two-reader
standard, and where it has not been met.
