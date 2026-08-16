# Tranche evidence — restore `def:crossing-energy` to the blocks that lost it?

Regenerated 2026-08-15 on the **union** editorial graph — `uses[]` *and*
`interprets` (folio-assistant bean `i8ad`) — and after the `extractUses` fix
(#117). Both changes shrink these lists by revealing declared dependencies the
graph previously could not see. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings and
the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.Braiding.CrossingEnergy`
Sources that lost it and still cannot reach it: **8**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `conj:crossing-graded-mass-expansion` | conjecture | no | no | no | 0 | backward |
| `rem:hecke-algebra-from-braiding` | remark | no | no | *n/a — no .lean* | 1 | backward |
| `rem:braid-fluid` | remark | no | no | *n/a — no .lean* | 5 | backward |
| `prop:hadron-exists` | proposition | no | no | no | 0 | **FORWARD** |
| `prop:borromean-hopf-energy-crossover` | proposition | no | crossing energy, crossing-energy | *n/a — no .lean* | 1 | backward |
| `def:hopf-diquark` | definition | no | no | no | 0 | backward |
| `prop:eos-borromean-cfl` | proposition | no | crossing energy | no | 1 | backward |
| `sec:strangelet-intro` | prose | no | crossing-energy | *n/a — no .lean* | 1 | backward |

**1 of 8 would point FORWARD if restored**.

Each adds a forward reference to a chapter the detangler arc has been untangling. Restoring these needs `foreshadows[]`, a relocation, or a deliberate decision to accept the edge — not a bulk apply:

- `prop:hadron-exists`

**0 of 8 searchable blocks link to the target from their prose** (0 of 8 have no `.md` and were not searched at all).
