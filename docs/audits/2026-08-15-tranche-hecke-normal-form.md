# Tranche evidence — restore `def:hecke-normal-form` to the blocks that lost it?

Regenerated 2026-08-15 on the **union** editorial graph — `uses[]` *and*
`interprets` (folio-assistant bean `i8ad`) — and after the `extractUses` fix
(#117). Both changes shrink these lists by revealing declared dependencies the
graph previously could not see. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings and
the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.Braiding.HeckeNormalForm`
Sources that lost it and still cannot reach it: **18**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `prop:level-sufficiency` | proposition | no | normal form | *n/a — no .lean* | 0 | backward |
| `prop:shell-schur-weyl-self-duality` | proposition | no | no | no | 0 | backward |
| `prop:phi-q-categorical-truncation` | proposition | no | no | no | 1 | backward |
| `prop:full-pole-structure-mass-trace` | proposition | no | no | no | 0 | backward |
| `prop:compound-beta-shell-calibration` | proposition | no | no | no | 2 | backward |
| `prop:quantum-dilogarithm-stratified` | proposition | no | no | no | 0 | backward |
| `prop:atom-knot-exists` | proposition | no | no | no | 0 | backward |
| `prop:atom-knot-unique` | proposition | no | normal form | no | 1 | backward |
| `def:confinement-category` | definition | no | no | no | 2 | backward |
| `def:confined-particle` | definition | no | normal form | no | 0 | backward |
| `def:isotope-knot` | definition | no | no | no | 1 | backward |
| `def:q-pochhammer-partial-product` | definition | no | no | no | 1 | backward |
| `def:atom-knot` | definition | no | normal form | no | 1 | backward |
| `prop:confinement-level-exists` | proposition | no | normal form | no | 0 | backward |
| `def:confinement-level` | definition | no | hecke normal form, hecke normal, normal form | no | 0 | backward |
| `def:knot-operator-energy` | definition | no | no | no | 1 | backward |
| `prop:graded-trace-residue-split` | proposition | no | no | no | 1 | backward |
| `def:stable-atom` | definition | no | normal form | no | 1 | backward |

**None of the 18 would point forward if restored.**

**0 of 18 searchable blocks link to the target from their prose** (0 of 18 have no `.md` and were not searched at all).
