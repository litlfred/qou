---
# qou-k9tf
title: 'RT finding: prop:golden-quartet-galois — Lean covers 2 of ~5 claims (roots, phi*psi=1); Galois orbits, iota-exchange, regular action, disc=400 unformalised'
status: todo
type: bug
priority: low
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-20T08:40:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B05).

- The Lean (`folio/quantum-observable-universe/predicted-spectra/golden-quartet-galois.lean`) proves that ±φ and ±φ⁻¹ are roots of x⁴−3x²+1, and that φ·φ⁻¹ = 1.
- The `.md` also claims:
  - the two quadratics are the Gal(ℚ(√5)/ℚ)-orbits, which needs irreducibility; the narrative does not argue it;
  - ι: x ↦ x⁻¹ swaps them;
  - ℤ/2 × ℤ/2 acts simply transitively; the narrative never checks that τ and ι commute;
  - disc = 400.
- The Lean statement is therefore weaker than the paper statement. All of the missing claims are true and cheaply formalisable over ℚ(√5) or ℝ.
