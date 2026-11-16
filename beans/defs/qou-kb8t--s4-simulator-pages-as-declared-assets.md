---
# qou-kb8t
title: S4 Simulator pages as declared assets
status: in-progress
type: feature
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:10:16Z
updated_at: 2026-11-16T19:28:00Z
parent: qou-n4r9
---

Size S. Declare the 11 simulator HTML files; report the 3 missing pages, do not invent them.

Owner hard rule: no math or physics content is changed. Every story ends with a parity check: block, chapter and .lean counts unchanged, statements byte-identical by hash, witnesses unchanged.


## Progress 2026-11-16 (PR #8167, `656614697372bd8008f27a4328b66e10d7e1263c` — kept `in-progress` per owner closure rule)

- **Declared the 9 live simulator HTML pages in `qou.json` under `"assets"` (`role: "simulator"`):**
  - `simulators/beta_decay_braid.html` (`sim-beta-decay-braid`), `simulators/beta_decay_halflife.html` (`sim-beta-decay-halflife`), `simulators/brings_surface.html` (`sim-brings-surface`), `simulators/double_slit_simulator.html` (`sim-double-slit-simulator`), `simulators/knot_atom_diagrams.html` (`sim-knot-atom-diagrams`), `simulators/knot_periodic_table.html` (`sim-knot-periodic-table`), `simulators/q_double_slit.html` (`sim-q-double-slit`), `simulators/quantum_brings_surface.html` (`sim-quantum-brings-surface`), `simulators/valley_stability.html` (`sim-valley-stability`).
  - Verified via `bun .../cat-harness-tools/scripts/check-declared-assets.ts` -> `9 declared asset(s) across 1 instance(s) (qou); 0 finding(s)`.
- **Accounting of the missing/parked pages (reported, not invented):**
  - 2 `simulator({...})` blocks in `folio/quantum-observable-universe/mass-theory/` carry `todo-html` (`sim:descent-rate-probe` -> `simulators/descent_rate_probe.html`, `sim:multi-level-jet-sum` -> `simulators/multi_level_jet_sum.html`); their HTML pages were never authored and are not invented per S4.
  - 2 unreferenced HTML files (`fsh-guts/deprecated/simulators/double_slit.html`, `fsh-guts/deprecated/simulators/empty.html`, plus `fsh-guts/deprecated/ruby-3d-viewer.html`) remain parked on `cat/cat-harness/fsh-guts`.
