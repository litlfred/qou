# Tranche evidence — restore `def:hadron` to the blocks that lost it?

Regenerated 2026-08-15 on the **union** editorial graph — `uses[]` *and*
`interprets` (folio-assistant bean `i8ad`) — and after the `extractUses` fix
(#117). Both changes shrink these lists by revealing declared dependencies the
graph previously could not see. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings and
the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.Hadron`
Sources that lost it and still cannot reach it: **6**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `prop:hadron-exists` | proposition | no | hadron | yes | 0 | backward |
| `prop:borromean-hopf-energy-crossover` | proposition | no | no | *n/a — no .lean* | 1 | backward |
| `def:skein-binding-lagrangian` | definition | no | no | no | 1 | backward |
| `prop:eos-borromean-cfl` | proposition | no | hadron | no | 1 | backward |
| `prop:hadron-unique` | proposition | no | hadron | yes | 2 | backward |
| `rem:strangelet-witten-stability` | remark | no | hadron | *n/a — no .lean* | 2 | backward |

**None of the 6 would point forward if restored.**

**0 of 6 searchable blocks link to the target from their prose** (0 of 6 have no `.md` and were not searched at all).
