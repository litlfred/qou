# Tranche evidence — restore `def:archimedean-realization-functor` to the blocks that lost it?

Regenerated 2026-08-15 by `scripts/prune-tranche-sheet.ts def:archimedean-realization-functor`, **after** the
`extractUses` fix (folio-assistant #117). Earlier revisions of this sheet
under-reported `declares now` for any block with a comment before its `uses:`
key — 27 blocks corpus-wide had their whole array invisible. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings, the
two-relation caveat and the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.BraidsKnots.ArchimedeanRealizationFunctor`
Sources that lost it and still cannot reach it: **10**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `thm:groebner-shirshov-energy` | theorem | no | no | no | 1 | backward |
| `lem:degree-one-braid-trivial-volume` | lemma | no | archimedean realization functor, archimedean realization, realization functor | no | 0 | backward |
| `prose:pre-archimedean-derivation-chain` | prose | no | no | *n/a — no .lean* | 3 | backward |
| `prop:operator-selection-lp` | proposition | no | no | *n/a — no .lean* | 1 | backward |
| `prop:atom-knot-mass-derivation` | proposition | no | archimedean realization functor, archimedean realization, realization functor | no | 2 | backward |
| `rem:archimedean-image-table` | remark | **YES** | archimedean-realization-functor, archimedean realization | *n/a — no .lean* | 1 | backward |
| `rem:generating-functions-solve-reeb-flow` | remark | no | no | *n/a — no .lean* | 5 | backward |
| `rem:kashaev-as-archimedean-realization` | remark | no | archimedean realization functor, archimedean realization, realization functor | *n/a — no .lean* | 1 | backward |
| `rem:vol-as-motivic-period` | remark | no | archimedean realization functor, archimedean realization, realization functor | *n/a — no .lean* | 1 | backward |
| `prop:markov-trace-ratio-exact` | proposition | no | no | no | 1 | backward |

**None of the 10 would point forward if restored.**

**1 of 10 searchable blocks link to the target from their prose** (0 of 10 have no `.md` and were not searched at all).

For those, the narrative is sending the reader to `def:archimedean-realization-functor` while `uses[]` omits it. That is the editorial relation contradicting itself in the same block, not a matter of taste:

- `rem:archimedean-image-table`
