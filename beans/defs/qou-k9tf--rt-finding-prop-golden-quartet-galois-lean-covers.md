---
# qou-k9tf
title: 'RT finding: prop:golden-quartet-galois — Lean covers 2 of ~5 claims (roots, phi*psi=1); Galois orbits, iota-exchange, regular action, disc=400 unformalised'
status: todo
type: bug
priority: low
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-21T16:00:00Z
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

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Re-checked against main 2ae54ab40: the finding still holds as recorded (B05 `prop:golden-quartet-galois`.).
- Disclosed, not fixed: a dated `caveat` authorNote on the block's `.ts` (commit 24c44167e) says exactly what the Lean proves and what it does not. Kind, prose, `uses[]` and Lean untouched.
- The kind change / restatement / demotion is an owner decision (ask-first rule); framed in the coordinator report. Stays open until the claim is re-derived or restated.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md on main 2ae54ab40; list: L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, single-term trace, trefoil-primary electron, 'c_2 = −1 PROVED', χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean's premises or in the files it names.

## 2026-11-21 (honesty-audits sibling)

Statement restated to what the Lean proves (owner ruling 2026-11-21, PR #8888; record in docs/audits/2026-11-21-roundtrip-blind-audit-pass2.md §3). The `.md` no longer claims more than the `lean.ref` theorem. Left open on purpose: the original, stronger claim is still unproved, and the narrative-proof defects noted above are not yet fixed.
