---
# qou-tdhw
title: 'RT finding: prop:alpha-em-shift-multiplicative-chain — Lean drops alpha_EM entirely and restates instance data; .md writes ''='' for a quantity 0.213 from CODATA'
status: todo
type: bug
priority: normal
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-21T16:00:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B06).

- The Lean (`folio/quantum-observable-universe/predicted-spectra/alpha-em-shift-multiplicative-chain.lean`) proves only `chainIndices = bareIndices` under `[HasAlphaShiftTorus 2 9] [HasAlphaShiftTorus 3 5]`. `bareIndices` is the literal [9,10], and the values come from the instances via `alpha_shift_torus_knot`. RT-1 leg B also noted the English round trip is unprovable without the class-to-α_shift link.
- The `.md` statement is α_EM⁻¹ = q·[α_shift(T₂,₉)]_q·[α_shift(T₃,₅)]_q. The Lean never mentions α_EM. The narrative is a pure substitution of two upstream propositions.
- The `.md` writes "=" for α_EM⁻¹, while the proof reports a 0.213 gap to CODATA. So "=" holds only for the model quantity q[9][10]. §7ab (≈ for derived values) / the mathematical-model register applies.
- This is photon/α_EM scope (W3; see also qou-aemx).

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Re-checked against main 2ae54ab40: the finding still holds as recorded (B06 `prop:alpha-em-shift-multiplicative-chain`.).
- Disclosed, not fixed: a dated `caveat` authorNote on the block's `.ts` (commit 24c44167e) says exactly what the Lean proves and what it does not. Kind, prose, `uses[]` and Lean untouched.
- The kind change / restatement / demotion is an owner decision (ask-first rule); framed in the coordinator report. Stays open until the claim is re-derived or restated.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md on main 2ae54ab40; list: L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, single-term trace, trefoil-primary electron, 'c_2 = −1 PROVED', χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none in the proof; CODATA appears only as the comparison (`|chain − CODATA| ≈ 0.213`, proof .md line 46), which is the permitted comparison boundary, not inside a proof.

## 2026-11-21 (honesty-audits sibling)

Statement restated to what the Lean proves (owner ruling 2026-11-21, PR #8888; record in docs/audits/2026-11-21-roundtrip-blind-audit-pass2.md §3). The `.md` no longer claims more than the `lean.ref` theorem. Left open on purpose: the original, stronger claim is still unproved, and the narrative-proof defects noted above are not yet fixed.
