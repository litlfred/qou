# Tranche evidence — restore `def:borromean-baryon` to the blocks that lost it?

Regenerated 2026-08-15 on the **union** editorial graph — `uses[]` *and*
`interprets` (folio-assistant bean `i8ad`) — and after the `extractUses` fix
(#117). Both changes shrink these lists by revealing declared dependencies the
graph previously could not see. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings and
the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.Braiding.BorromeanBaryon`
Sources that lost it and still cannot reach it: **15**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `prop:atom-knot-exists` | proposition | no | no | no | 0 | backward |
| `def:typed-crossing-operator` | definition | no | borromean baryon | no | 1 | backward |
| `rem:quarks-borromean-picture` | remark | no | no | *n/a — no .lean* | 1 | backward |
| `rem:down-quark-properties` | remark | no | no | *n/a — no .lean* | 1 | **FORWARD** |
| `rem:binding-knots-visual-inventory` | remark | no | borromean baryon | *n/a — no .lean* | 1 | **FORWARD** |
| `sim:knot-periodic-table` | simulator | no | borromean baryon | *n/a — no .lean* | 2 | backward |
| `rem:knot-particle-dictionary` | remark | no | no | *n/a — no .lean* | 4 | **FORWARD** |
| `ex:hadron-proton` | example | no | no | *n/a — no .lean* | 2 | backward |
| `rem:up-quark-properties` | remark | no | no | *n/a — no .lean* | 1 | **FORWARD** |
| `def:per-nucleon-channel-decomposition` | definition | no | no | no | 1 | backward |
| `def:nucleon-hecke-element` | definition | no | borromean baryon | no | 1 | backward |
| `rem:shell-transition-knot-interpretation` | remark | no | no | *n/a — no .lean* | 1 | backward |
| `conj:borromean-quark` | conjecture | no | no | yes | 2 | backward |
| `rem:knot-atom-diagrams` | remark | no | no | *n/a — no .lean* | 2 | backward |
| `prop:atomic-lp-stability` | proposition | no | no | *n/a — no .lean* | 1 | backward |

**4 of 15 would point FORWARD if restored**.

Each adds a forward reference to a chapter the detangler arc has been untangling. Restoring these needs `foreshadows[]`, a relocation, or a deliberate decision to accept the edge — not a bulk apply:

- `rem:down-quark-properties`
- `rem:binding-knots-visual-inventory`
- `rem:knot-particle-dictionary`
- `rem:up-quark-properties`

**0 of 15 searchable blocks link to the target from their prose** (0 of 15 have no `.md` and were not searched at all).
