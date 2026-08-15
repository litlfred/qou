# Tranche evidence — restore `def:crossing-energy` to the blocks that lost it?

Generated 2026-08-15 by `scripts/prune-tranche-sheet.ts def:crossing-energy`. Bean `prn1`.
**Nothing is restored by this document.**

Column meanings, the two-relation caveat, and why a target-shaped tranche is
one question rather than many: see
[`2026-08-15-tranche-1-jones-markov-trace.md`](2026-08-15-tranche-1-jones-markov-trace.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.Braiding.CrossingEnergy`
Sources that lost it and still cannot reach it: **12**

| source | kind | prose link | prose mention | lean | declares now |
|---|---|---|---|---|---|
| `conj:crossing-graded-mass-expansion` | conjecture | no | no | no | 0 |
| `rem:hecke-algebra-from-braiding` | remark | no | no | *n/a — no .lean* | 0 |
| `rem:braid-fluid` | remark | no | no | *n/a — no .lean* | 4 |
| `rem:hecke-charge-mass-duality` | remark | **YES** | crossing energy, crossing-energy | *n/a — no .lean* | 2 |
| `prop:hadron-exists` | proposition | no | no | no | 0 |
| `prop:borromean-hopf-energy-crossover` | proposition | no | crossing energy, crossing-energy | *n/a — no .lean* | 1 |
| `prop:strangelet-crossing-energy` | proposition | **YES** | crossing energy, crossing-energy | *n/a — no .lean* | 0 |
| `def:hopf-diquark` | definition | no | no | no | 0 |
| `prop:eos-borromean-cfl` | proposition | no | crossing energy | no | 1 |
| `sec:strangelet-intro` | prose | no | crossing-energy | *n/a — no .lean* | 1 |
| `prop:strangelet-double-beta` | proposition | no | crossing energy, crossing-energy | no | 1 |
| `rem:commutative-crossing-energy` | remark | **YES** | crossing energy, crossing-energy | yes | 3 |

**3 of 12 searchable blocks link to the target from their prose** (0 of 12 have no `.md` and were not searched at all).

For those, the narrative is sending the reader to `def:crossing-energy` while `uses[]` omits it. That is the editorial relation contradicting itself in the same block, not a matter of taste:

- `rem:hecke-charge-mass-duality`
- `prop:strangelet-crossing-energy`
- `rem:commutative-crossing-energy`
Target exists: yes
Target Lean decl: `QOU.Braiding.CrossingEnergy`
Sources that lost it and still cannot reach it: **12**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `conj:crossing-graded-mass-expansion` | conjecture | no | no | no | 0 | backward |
| `rem:hecke-algebra-from-braiding` | remark | no | no | *n/a — no .lean* | 0 | backward |
| `rem:braid-fluid` | remark | no | no | *n/a — no .lean* | 4 | backward |
| `rem:hecke-charge-mass-duality` | remark | **YES** | crossing energy, crossing-energy | *n/a — no .lean* | 2 | backward |
| `prop:hadron-exists` | proposition | no | no | no | 0 | **FORWARD** |
| `prop:borromean-hopf-energy-crossover` | proposition | no | crossing energy, crossing-energy | *n/a — no .lean* | 1 | backward |
| `prop:strangelet-crossing-energy` | proposition | **YES** | crossing energy, crossing-energy | *n/a — no .lean* | 0 | backward |
| `def:hopf-diquark` | definition | no | no | no | 0 | backward |
| `prop:eos-borromean-cfl` | proposition | no | crossing energy | no | 1 | backward |
| `sec:strangelet-intro` | prose | no | crossing-energy | *n/a — no .lean* | 1 | backward |
| `prop:strangelet-double-beta` | proposition | no | crossing energy, crossing-energy | no | 1 | backward |
| `rem:commutative-crossing-energy` | remark | **YES** | crossing energy, crossing-energy | yes | 3 | backward |

**1 of 12 would point FORWARD if restored**.

Each adds a forward reference to a chapter the detangler arc has been untangling. Restoring these needs `foreshadows[]`, a relocation, or a deliberate decision to accept the edge — not a bulk apply:

- `prop:hadron-exists`

**3 of 12 searchable blocks link to the target from their prose** (0 of 12 have no `.md` and were not searched at all).

For those, the narrative is sending the reader to `def:crossing-energy` while `uses[]` omits it. That is the editorial relation contradicting itself in the same block, not a matter of taste:

- `rem:hecke-charge-mass-duality`
- `prop:strangelet-crossing-energy`
- `rem:commutative-crossing-energy`
