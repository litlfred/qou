---
# qou-w3ju
title: simulators/ is duplicated byte-identically inside the platform clone
status: todo
type: bug
priority: low
tags:
    - simulators
created_at: 2026-09-26T10:39:24Z
updated_at: 2026-09-26T10:48:09Z
parent: qou-p7z5
---

**Measured 2026-09-26.** `simulators/` exists in both trees with overlapping
filenames, and the shared ones are byte-identical.

- `qou/simulators/` — 11 files
- `/home/user/folio-assistant/simulators/` — 11 files
- 8 names shared: `beta_decay_braid`, `beta_decay_halflife`, `brings_surface`,
  `double_slit`, `double_slit_simulator`, `empty`, `knot_atom_diagrams`,
  `knot_periodic_table`

Spot-checked with `cmp`: `beta_decay_braid`, `brings_surface`,
`knot_periodic_table` are all **IDENTICAL**. (Only 3 of 8 were compared — the
other 5 are unmeasured.)

## Why this is low priority but worth a bean

`harness.config.json` already states the intended rule — *"simulators are subject
matter, so this path is relative to the qou root, not the platform"* — and
`folio.config.json` sets `simulators.dir: "simulators"`. So qou's copy is the
authoritative one and the platform's is a fork-point duplicate.

It costs nothing today because **nothing at the pinned platform reads
`config.simulators`** (sibling `qou-f50c`). It costs something the moment one
copy is edited: two identical trees with no declared owner is how a fix lands in
the copy nobody serves.

## Not proposed

Deleting the platform's copy is a change to **another repository** and is not
qou's call. The useful qou-side action is to make sure the config points at qou's
tree and that the README's `folio:simulators` section renders from it — which it
does: that section lists qou's 11.
