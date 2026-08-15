# Tranche evidence — restore `def:motivic-substrate` to the blocks that lost it?

Generated 2026-08-15 by `scripts/prune-tranche-sheet.ts def:motivic-substrate`. Bean `prn1`.
**Nothing is restored by this document.**

Column meanings, the two-relation caveat, the forward-reference rule, and why a
target-shaped tranche is one question rather than many: see
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md) and
[`2026-08-15-tranche-1-jones-markov-trace.md`](2026-08-15-tranche-1-jones-markov-trace.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.AlgebraicSubstrate.MotivicSubstrate`
Sources that lost it and still cannot reach it: **11**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `def:classical-limit-functor` | definition | no | no | no | 2 | backward |
| `thm:groebner-shirshov-energy` | theorem | no | no | no | 1 | backward |
| `prop:operator-selection-lp` | proposition | no | no | *n/a — no .lean* | 1 | backward |
| `def:motivic-mass-measure` | definition | no | no | no | 1 | backward |
| `def:archimedean-realization-functor` | definition | no | no | no | 3 | backward |
| `def:qou-motivic-galois-instance` | definition | no | no | no | 1 | backward |
| `ex:chi-minus-six-derivation` | example | **YES** | motivic substrate, motivic-substrate | *n/a — no .lean* | 3 | backward |
| `ex:archimedean-yekutieli` | example | no | motivic substrate | *n/a — no .lean* | 3 | backward |
| `def:motivic-galois-character` | definition | **YES** | motivic substrate, motivic-substrate | yes | 1 | backward |
| `rem:kummer-tower` | remark | no | no | *n/a — no .lean* | 1 | **FORWARD** |
| `def:adelic-substrate` | definition | no | no | no | 0 | backward |

**1 of 11 would point FORWARD if restored**.

Each adds a forward reference to a chapter the detangler arc has been untangling. Restoring these needs `foreshadows[]`, a relocation, or a deliberate decision to accept the edge — not a bulk apply:

- `rem:kummer-tower`

**2 of 11 searchable blocks link to the target from their prose** (0 of 11 have no `.md` and were not searched at all).

For those, the narrative is sending the reader to `def:motivic-substrate` while `uses[]` omits it. That is the editorial relation contradicting itself in the same block, not a matter of taste:

- `ex:chi-minus-six-derivation`
- `def:motivic-galois-character`
