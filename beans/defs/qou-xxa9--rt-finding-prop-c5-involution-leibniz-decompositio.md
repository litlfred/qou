---
# qou-xxa9
title: 'RT finding: prop:c5-involution-leibniz-decomposition — Lean takes c5 := -b^2 - 1/2 as a definition (rung-5 identification not derived); narrative errors; R-specialised without need'
status: todo
type: bug
priority: normal
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-21T16:00:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B01).

- The Lean (`folio/quantum-observable-universe/stochastic-mechanics/c5-involution-leibniz-decomposition.lean`) proves c5Decomposition q = −3/2 + 1/[2]_q² over ℝ with q ≠ 0. This is a correct rational-function identity. RT-1 round-trips faithfully.
- The statement needs no archimedean structure. Per §7c it should be over a generic field (char ≠ 2, q ≠ 0, q²+1 ≠ 0).
- The `.md` claims this is THE ladder coefficient c_5. Both RT-2 and RT-3 found that the narrative never derives c_5 = −b² − 1/2 from the ladder; the c_k table is asserted.
- Internal errors in the narrative proof:
  - Step 2 uses h/2 = 1/2 (that is, h = 1); at the silver ratio, h = 2.
  - B_n is called "two averaged crossings", but its second factor is σ₁ − h = σ₁⁻¹.
  - tr_M(B_n − B_p) = h²/2 − h is asserted, not computed.
- Checked: b² = 7/8 at q = 1+√2 is correct. The ladder is convention-C-frame (qou-cds1).

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Re-checked against main 2ae54ab40: the finding still holds as recorded (B01 `prop:c5-involution-leibniz-decomposition`.).
- Disclosed, not fixed: a dated `caveat` authorNote on the block's `.ts` (commit 24c44167e) says exactly what the Lean proves and what it does not. Kind, prose, `uses[]` and Lean untouched.
- The kind change / restatement / demotion is an owner decision (ask-first rule); framed in the coordinator report. Stays open until the claim is re-derived or restated.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md on main 2ae54ab40; list: L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, single-term trace, trefoil-primary electron, 'c_2 = −1 PROVED', χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): the block's .md/.lean use none of these terms, but c₅ is a rung of the Q_β precision ladder (`prop:q-beta-categorical-precision-ladder`), whose c_k values and convention are being reworked in the c_k ladder D arc (qou-cds1) and on the two-term trace. Any restatement must use the current ladder; do not re-derive c₅ on the old basis. The disclosure itself (Lean scope) does not depend on the ladder values.

## 2026-11-21 (honesty-audits sibling)

Statement restated to what the Lean proves (owner ruling 2026-11-21, PR #8888; record in docs/audits/2026-11-21-roundtrip-blind-audit-pass2.md §3). The `.md` no longer claims more than the `lean.ref` theorem. Left open on purpose: the original, stronger claim is still unproved, and the narrative-proof defects noted above are not yet fixed.
