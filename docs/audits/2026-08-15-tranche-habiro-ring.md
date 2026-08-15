# Tranche evidence — restore `def:habiro-ring` to the blocks that lost it?

Generated 2026-08-15 by `scripts/prune-tranche-sheet.ts def:habiro-ring`. Bean `prn1`.
**Nothing is restored by this document.**

Column meanings, the two-relation caveat, the forward-reference rule, and why a
target-shaped tranche is one question rather than many: see
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md) and
[`2026-08-15-tranche-1-jones-markov-trace.md`](2026-08-15-tranche-1-jones-markov-trace.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.HabiroRing.HabiroElement`
Sources that lost it and still cannot reach it: **11**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `prop:full-pole-structure-mass-trace` | proposition | no | habiro ring | no | 0 | backward |
| `prop:full-pole-structure-mass-trace` | proposition | no | habiro ring | no | 0 | backward |
| `thm:groebner-shirshov-energy` | theorem | no | no | no | 1 | backward |
| `prop:operator-selection-lp` | proposition | no | no | *n/a — no .lean* | 1 | **FORWARD** |
| `rem:kashaev-volume-density` | remark | no | no | *n/a — no .lean* | 1 | backward |
| `prop:habiro-residue-sum-equivalence` | proposition | no | no | no | 1 | backward |
| `def:z-habiro-ring` | definition | no | habiro ring | yes | 1 | backward |
| `def:qz-bicompletion` | definition | no | habiro ring | yes | 1 | backward |
| `def:qou-motivic-galois-instance` | definition | no | no | no | 1 | backward |
| `prop:terms-2-6-higher-operations` | proposition | no | no | *n/a — no .lean* | 1 | backward |
| `thm:six-term-mass-formula-complete` | theorem | no | no | *n/a — no .lean* | 2 | backward |

**1 of 11 would point FORWARD if restored**.

Each adds a forward reference to a chapter the detangler arc has been untangling. Restoring these needs `foreshadows[]`, a relocation, or a deliberate decision to accept the edge — not a bulk apply:

- `prop:operator-selection-lp`

**0 of 11 searchable blocks link to the target from their prose** (0 of 11 have no `.md` and were not searched at all).
