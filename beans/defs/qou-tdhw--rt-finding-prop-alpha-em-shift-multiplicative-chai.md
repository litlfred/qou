---
# qou-tdhw
title: 'RT finding: prop:alpha-em-shift-multiplicative-chain — Lean drops alpha_EM entirely and restates instance data; .md writes ''='' for a quantity 0.213 from CODATA'
status: todo
type: bug
priority: normal
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-20T08:40:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B06).

- The Lean (`folio/quantum-observable-universe/predicted-spectra/alpha-em-shift-multiplicative-chain.lean`) proves only `chainIndices = bareIndices` under `[HasAlphaShiftTorus 2 9] [HasAlphaShiftTorus 3 5]`. `bareIndices` is the literal [9,10], and the values come from the instances via `alpha_shift_torus_knot`. RT-1 leg B also noted the English round trip is unprovable without the class-to-α_shift link.
- The `.md` statement is α_EM⁻¹ = q·[α_shift(T₂,₉)]_q·[α_shift(T₃,₅)]_q. The Lean never mentions α_EM. The narrative is a pure substitution of two upstream propositions.
- The `.md` writes "=" for α_EM⁻¹, while the proof reports a 0.213 gap to CODATA. So "=" holds only for the model quantity q[9][10]. §7ab (≈ for derived values) / the mathematical-model register applies.
- This is photon/α_EM scope (W3; see also qou-aemx).
