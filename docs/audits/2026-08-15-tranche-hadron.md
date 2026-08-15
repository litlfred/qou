# Tranche evidence — restore `def:hadron` to the blocks that lost it?

Regenerated 2026-08-15 by `scripts/prune-tranche-sheet.ts def:hadron`, **after** the
`extractUses` fix (folio-assistant #117). Earlier revisions of this sheet
under-reported `declares now` for any block with a comment before its `uses:`
key — 27 blocks corpus-wide had their whole array invisible. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings, the
two-relation caveat and the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.Hadron`
Sources that lost it and still cannot reach it: **10**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `rem:quarks-borromean-picture` | remark | no | hadron | *n/a — no .lean* | 0 | backward |
| `rem:hadron-interpretation` | remark | no | hadron | *n/a — no .lean* | 0 | backward |
| `prop:hadron-exists` | proposition | no | hadron | yes | 0 | backward |
| `prop:borromean-hopf-energy-crossover` | proposition | no | no | *n/a — no .lean* | 1 | backward |
| `ex:hadron-proton` | example | no | hadron | *n/a — no .lean* | 1 | backward |
| `rem:borromean-baryon-interpretation` | remark | no | no | *n/a — no .lean* | 0 | backward |
| `def:skein-binding-lagrangian` | definition | no | no | no | 1 | backward |
| `prop:eos-borromean-cfl` | proposition | no | hadron | no | 1 | backward |
| `prop:hadron-unique` | proposition | no | hadron | yes | 2 | backward |
| `rem:strangelet-witten-stability` | remark | no | hadron | *n/a — no .lean* | 2 | backward |

**None of the 10 would point forward if restored.**

**0 of 10 searchable blocks link to the target from their prose** (0 of 10 have no `.md` and were not searched at all).
