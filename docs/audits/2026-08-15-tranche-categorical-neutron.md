# Tranche evidence — restore `def:categorical-neutron` to the blocks that lost it?

Regenerated 2026-08-15 on the **union** editorial graph — `uses[]` *and*
`interprets` (folio-assistant bean `i8ad`) — and after the `extractUses` fix
(#117). Both changes shrink these lists by revealing declared dependencies the
graph previously could not see. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings and
the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.Torsion.CategoricalNeutron`
Sources that lost it and still cannot reach it: **6**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `rem:nucleon-nf-observability` | remark | no | no | *n/a — no .lean* | 1 | backward |
| `prop:neutron-proton-mass-splitting` | proposition | no | no | no | 1 | backward |
| `prop:torus-hopf-stability` | proposition | no | no | no | 0 | backward |
| `prop:confinement-operator-selection` | proposition | no | no | *n/a — no .lean* | 1 | backward |
| `prop:four-term-pair-nucleon` | proposition | no | no | *n/a — no .lean* | 2 | **FORWARD** |
| `rem:unmapped-torus-knots` | remark | no | no | *n/a — no .lean* | 2 | backward |

**1 of 6 would point FORWARD if restored**.

Each adds a forward reference to a chapter the detangler arc has been untangling. Restoring these needs `foreshadows[]`, a relocation, or a deliberate decision to accept the edge — not a bulk apply:

- `prop:four-term-pair-nucleon`

**0 of 6 searchable blocks link to the target from their prose** (0 of 6 have no `.md` and were not searched at all).
