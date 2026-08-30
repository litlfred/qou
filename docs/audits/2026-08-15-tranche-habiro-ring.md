# Tranche evidence — restore `def:habiro-ring` to the blocks that lost it?

Regenerated 2026-08-15 on the **union** editorial graph — `uses[]` *and*
`interprets` (folio-assistant bean `i8ad`) — and after the `extractUses` fix
(#117). Both changes shrink these lists by revealing declared dependencies the
graph previously could not see. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings and
the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
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
| `rem:kashaev-volume-density` | remark | no | no | *n/a — no .lean* | 2 | backward |
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
