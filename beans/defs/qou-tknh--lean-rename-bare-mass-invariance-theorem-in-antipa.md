---
# qou-tknh
title: 'Lean: rename bare_mass_invariance theorem in antiparticle_crossing_reversal.lean'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-04T19:09:26Z
updated_at: 2026-11-16T19:07:00Z
parent: qou-wp3h
---

## Progress Update (2026-11-16 — PR #8160)
- **PR:** [`litlfred/qou#8160`](https://github.com/litlfred/qou/pull/8160) (`c0fb591249c67f13f6a77b40075589852babb011`)
- **Resolution:**
  - Verified that the Lake module `folio/quantum-observable-universe/lean/QOU/Torsion/antiparticle_crossing_reversal.lean` was already updated to `m_topological` / `impl_topological_mass_invariance`, whereas the content-block sibling `folio/quantum-observable-universe/predicted-spectra/antiparticle-crossing-reversal.lean` still defined `theorem bare_mass_invariance`.
  - Renamed `bare_mass_invariance` in `folio/quantum-observable-universe/predicted-spectra/antiparticle-crossing-reversal.lean` to `topological_mass_invariance` (matching Claim 4 in `antiparticle-crossing-reversal.md`), updated `antiparticle_crossing_reversal` to invoke `topological_mass_invariance`, updated docstrings from "bare mass" to "topological (relational) mass", and kept `@[deprecated topological_mass_invariance (since := "2026-11-16")] abbrev bare_mass_invariance` for backwards compatibility (`0` `sorry`, `0` self-assuming audit hits).
  - Status kept at `in-progress` pending PR #8160 merge and owner verification.
