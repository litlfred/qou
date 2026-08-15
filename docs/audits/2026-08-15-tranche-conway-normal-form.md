# Tranche evidence — restore `rem:conway-normal-form` to the blocks that lost it?

Regenerated 2026-08-15 by `scripts/prune-tranche-sheet.ts rem:conway-normal-form`, **after** the
`extractUses` fix (folio-assistant #117). Earlier revisions of this sheet
under-reported `declares now` for any block with a comment before its `uses:`
key — 27 blocks corpus-wide had their whole array invisible. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings, the
two-relation caveat and the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Sources that lost it and still cannot reach it: **10**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `rem:ns-surreal-bound` | remark | no | no | *n/a — target has no lean.ref* | 0 | backward |
| `conj:p-vs-np-qou` | conjecture | no | no | *n/a — target has no lean.ref* | 2 | backward |
| `prop:surreal-rate-calculus` | proposition | no | no | *n/a — target has no lean.ref* | 1 | backward |
| `rem:adelic-tate-squeeze` | remark | no | no | *n/a — target has no lean.ref* | 1 | backward |
| `prop:jet-tower-convergence` | proposition | no | no | *n/a — target has no lean.ref* | 1 | backward |
| `rem:body-asymptotics-catalog` | remark | **YES** | conway-normal-form | *n/a — target has no lean.ref* | 7 | backward |
| `prop:unified-iterative-correction` | proposition | no | no | *n/a — target has no lean.ref* | 2 | backward |
| `prop:hecke-convergence-bound` | proposition | no | no | *n/a — target has no lean.ref* | 0 | backward |
| `prop:universal-braid-branching` | proposition | no | normal form | *n/a — target has no lean.ref* | 2 | backward |
| `prop:ns-obstruction-computation` | proposition | no | no | *n/a — target has no lean.ref* | 2 | backward |

**None of the 10 would point forward if restored.**

**1 of 10 searchable blocks link to the target from their prose** (0 of 10 have no `.md` and were not searched at all).

For those, the narrative is sending the reader to `rem:conway-normal-form` while `uses[]` omits it. That is the editorial relation contradicting itself in the same block, not a matter of taste:

- `rem:body-asymptotics-catalog`
