# Tranche evidence — restore `def:motivic-substrate` to the blocks that lost it?

Regenerated 2026-08-15 on the **union** editorial graph — `uses[]` *and*
`interprets` (folio-assistant bean `i8ad`) — and after the `extractUses` fix
(#117). Both changes shrink these lists by revealing declared dependencies the
graph previously could not see. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings and
the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.AlgebraicSubstrate.MotivicSubstrate`
Sources that lost it and still cannot reach it: **8**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `def:classical-limit-functor` | definition | no | no | no | 2 | backward |
| `thm:groebner-shirshov-energy` | theorem | no | no | no | 1 | backward |
| `prop:operator-selection-lp` | proposition | no | no | *n/a — no .lean* | 1 | backward |
| `def:motivic-mass-measure` | definition | no | no | no | 1 | backward |
| `def:archimedean-realization-functor` | definition | no | no | no | 3 | backward |
| `ex:archimedean-yekutieli` | example | no | motivic substrate | *n/a — no .lean* | 4 | backward |
| `rem:kummer-tower` | remark | no | no | *n/a — no .lean* | 2 | **FORWARD** |
| `def:adelic-substrate` | definition | no | no | no | 0 | backward |

**1 of 8 would point FORWARD if restored**.

Each adds a forward reference to a chapter the detangler arc has been untangling. Restoring these needs `foreshadows[]`, a relocation, or a deliberate decision to accept the edge — not a bulk apply:

- `rem:kummer-tower`

**0 of 8 searchable blocks link to the target from their prose** (0 of 8 have no `.md` and were not searched at all).
