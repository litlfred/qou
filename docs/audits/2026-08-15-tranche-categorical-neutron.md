# Tranche evidence — restore `def:categorical-neutron` to the blocks that lost it?

Generated 2026-08-15 by `scripts/prune-tranche-sheet.ts def:categorical-neutron`. Bean `prn1`.
**Nothing is restored by this document.**

Column meanings, the two-relation caveat, the forward-reference rule, and why a
target-shaped tranche is one question rather than many: see
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md) and
[`2026-08-15-tranche-1-jones-markov-trace.md`](2026-08-15-tranche-1-jones-markov-trace.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.Torsion.CategoricalNeutron`
Sources that lost it and still cannot reach it: **10**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `rem:nucleon-nf-observability` | remark | no | no | *n/a — no .lean* | 0 | backward |
| `prop:neutron-proton-mass-splitting` | proposition | no | no | no | 1 | backward |
| `prop:torus-hopf-stability` | proposition | no | no | no | 0 | backward |
| `prop:confinement-operator-selection` | proposition | no | no | *n/a — no .lean* | 1 | backward |
| `ex:helium4-derived-nf` | example | no | no | *n/a — no .lean* | 2 | backward |
| `prop:four-term-pair-nucleon` | proposition | no | no | *n/a — no .lean* | 2 | **FORWARD** |
| `def:stable-nucleus` | definition | **YES** | categorical neutron, categorical-neutron | no | 1 | backward |
| `prop:categorical-neutron-exists` | proposition | **YES** | categorical neutron, categorical-neutron | yes | 1 | backward |
| `rem:unmapped-torus-knots` | remark | no | no | *n/a — no .lean* | 2 | backward |
| `prop:categorical-neutron-unique` | proposition | **YES** | categorical neutron, categorical-neutron | yes | 2 | backward |

**1 of 10 would point FORWARD if restored**.

Each adds a forward reference to a chapter the detangler arc has been untangling. Restoring these needs `foreshadows[]`, a relocation, or a deliberate decision to accept the edge — not a bulk apply:

- `prop:four-term-pair-nucleon`

**3 of 10 searchable blocks link to the target from their prose** (0 of 10 have no `.md` and were not searched at all).

For those, the narrative is sending the reader to `def:categorical-neutron` while `uses[]` omits it. That is the editorial relation contradicting itself in the same block, not a matter of taste:

- `def:stable-nucleus`
- `prop:categorical-neutron-exists`
- `prop:categorical-neutron-unique`
