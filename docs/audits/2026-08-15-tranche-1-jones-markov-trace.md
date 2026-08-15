# Tranche evidence — restore `thm:jones-markov-trace` to the blocks that lost it?

Regenerated 2026-08-15 by `scripts/prune-tranche-sheet.ts thm:jones-markov-trace`, **after** the
`extractUses` fix (folio-assistant #117). Earlier revisions of this sheet
under-reported `declares now` for any block with a comment before its `uses:`
key — 27 blocks corpus-wide had their whole array invisible. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings, the
two-relation caveat and the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.Braiding.JonesMarkovTrace`
Sources that lost it and still cannot reach it: **19**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `prop:shell-schur-weyl-self-duality` | proposition | no | no | no | 0 | backward |
| `rem:hecke-algebra-from-braiding` | remark | no | no | *n/a — no .lean* | 0 | backward |
| `prop:wedderburn-as-noncomm-fourier` | proposition | no | no | no | 0 | backward |
| `prop:frobenius-self-duality-forces-lp-dual-extraction` | proposition | no | markov trace | no | 0 | backward |
| `lem:vhat-pair-commutation-trace` | lemma | no | no | no | 0 | backward |
| `prop:atom-knot-unique` | proposition | no | no | no | 1 | backward |
| `lem:degree-one-braid-trivial-volume` | lemma | no | no | no | 0 | backward |
| `prose:pre-archimedean-derivation-chain` | prose | no | markov trace | *n/a — no .lean* | 3 | backward |
| `prop:atom-knot-mass-derivation` | proposition | no | no | no | 2 | backward |
| `def:per-nucleon-channel-decomposition` | definition | no | no | no | 1 | backward |
| `prop:recursive-atom-knot-atlas` | proposition | no | no | no | 4 | backward |
| `prop:pieri-photon-shift` | proposition | no | no | no | 1 | backward |
| `prop:y-lambda-cyclotomic-factorization` | proposition | no | no | no | 1 | backward |
| `prop:y-lambda-recipe-from-partition` | proposition | no | no | no | 1 | backward |
| `prop:qmn-recursive-memoized` | proposition | no | no | *n/a — no .lean* | 1 | backward |
| `prop:demazure-fiber-markov-trace` | proposition | no | no | no | 1 | backward |
| `def:phi-q-piece` | definition | no | no | no | 1 | backward |
| `prop:wenzl-bridge-applicability-qou` | proposition | no | markov trace | no | 1 | backward |
| `prop:wenzl-qmn-synergy` | proposition | no | markov trace | no | 1 | backward |

**None of the 19 would point forward if restored.**

**0 of 19 searchable blocks link to the target from their prose** (0 of 19 have no `.md` and were not searched at all).
