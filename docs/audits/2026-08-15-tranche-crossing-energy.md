# Tranche evidence — restore `def:crossing-energy` to the blocks that lost it?

Regenerated 2026-08-15 by `scripts/prune-tranche-sheet.ts def:crossing-energy`, **after** the
`extractUses` fix (folio-assistant #117). Earlier revisions of this sheet
under-reported `declares now` for any block with a comment before its `uses:`
key — 27 blocks corpus-wide had their whole array invisible. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings, the
two-relation caveat and the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.Braiding.CrossingEnergy`
Sources that lost it and still cannot reach it: **9**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `conj:crossing-graded-mass-expansion` | conjecture | no | no | no | 0 | backward |
| `rem:hecke-algebra-from-braiding` | remark | no | no | *n/a — no .lean* | 0 | backward |
| `rem:braid-fluid` | remark | no | no | *n/a — no .lean* | 4 | backward |
| `prop:hadron-exists` | proposition | no | no | no | 0 | **FORWARD** |
| `prop:borromean-hopf-energy-crossover` | proposition | no | crossing energy, crossing-energy | *n/a — no .lean* | 1 | backward |
| `def:hopf-diquark` | definition | no | no | no | 0 | backward |
| `prop:eos-borromean-cfl` | proposition | no | crossing energy | no | 1 | backward |
| `sec:strangelet-intro` | prose | no | crossing-energy | *n/a — no .lean* | 1 | backward |
| `rem:commutative-crossing-energy` | remark | **YES** | crossing energy, crossing-energy | yes | 3 | backward |

**1 of 9 would point FORWARD if restored**.

Each adds a forward reference to a chapter the detangler arc has been untangling. Restoring these needs `foreshadows[]`, a relocation, or a deliberate decision to accept the edge — not a bulk apply:

- `prop:hadron-exists`

**1 of 9 searchable blocks link to the target from their prose** (0 of 9 have no `.md` and were not searched at all).

For those, the narrative is sending the reader to `def:crossing-energy` while `uses[]` omits it. That is the editorial relation contradicting itself in the same block, not a matter of taste:

- `rem:commutative-crossing-energy`
