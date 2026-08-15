# Tranche evidence — restore `def:borromean-baryon` to the blocks that lost it?

Regenerated 2026-08-15 by `scripts/prune-tranche-sheet.ts def:borromean-baryon`, **after** the
`extractUses` fix (folio-assistant #117). Earlier revisions of this sheet
under-reported `declares now` for any block with a comment before its `uses:`
key — 27 blocks corpus-wide had their whole array invisible. Bean `prn1`.

Sources already restored under this bean no longer appear. Column meanings, the
two-relation caveat and the forward-reference rule:
[`2026-08-15-tranche-index.md`](2026-08-15-tranche-index.md).
`n/a` means the file does not exist, so nothing was searched — it is not `no`.


Target exists: yes
Target Lean decl: `QOU.Braiding.BorromeanBaryon`
Sources that lost it and still cannot reach it: **16**

| source | kind | prose link | prose mention | lean | declares now | restoring points |
|---|---|---|---|---|---|---|
| `prop:atom-knot-exists` | proposition | no | no | no | 0 | backward |
| `def:typed-crossing-operator` | definition | no | borromean baryon | no | 1 | backward |
| `rem:quarks-borromean-picture` | remark | no | no | *n/a — no .lean* | 0 | backward |
| `rem:down-quark-properties` | remark | no | no | *n/a — no .lean* | 0 | **FORWARD** |
| `rem:binding-knots-visual-inventory` | remark | no | borromean baryon | *n/a — no .lean* | 0 | **FORWARD** |
| `sim:knot-periodic-table` | simulator | no | borromean baryon | *n/a — no .lean* | 2 | backward |
| `rem:knot-particle-dictionary` | remark | no | no | *n/a — no .lean* | 3 | **FORWARD** |
| `ex:hadron-proton` | example | no | no | *n/a — no .lean* | 1 | backward |
| `rem:borromean-baryon-interpretation` | remark | no | no | *n/a — no .lean* | 0 | backward |
| `rem:up-quark-properties` | remark | no | no | *n/a — no .lean* | 0 | **FORWARD** |
| `def:per-nucleon-channel-decomposition` | definition | no | no | no | 1 | backward |
| `def:nucleon-hecke-element` | definition | no | borromean baryon | no | 1 | backward |
| `rem:shell-transition-knot-interpretation` | remark | no | no | *n/a — no .lean* | 1 | backward |
| `conj:borromean-quark` | conjecture | no | no | yes | 2 | backward |
| `rem:knot-atom-diagrams` | remark | no | no | *n/a — no .lean* | 1 | backward |
| `prop:atomic-lp-stability` | proposition | no | no | *n/a — no .lean* | 1 | backward |

**4 of 16 would point FORWARD if restored**.

Each adds a forward reference to a chapter the detangler arc has been untangling. Restoring these needs `foreshadows[]`, a relocation, or a deliberate decision to accept the edge — not a bulk apply:

- `rem:down-quark-properties`
- `rem:binding-knots-visual-inventory`
- `rem:knot-particle-dictionary`
- `rem:up-quark-properties`

**0 of 16 searchable blocks link to the target from their prose** (0 of 16 have no `.md` and were not searched at all).
