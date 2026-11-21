---
# qou-pwo1
title: 'RT finding: lem:staircase-corner-hook — Lean defines hCorner as the arithmetic (k-1)+(k-1)+1; no partition is formalised; rho_k convention unstated in .md'
status: todo
type: bug
priority: low
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B10).

- The Lean (`folio/quantum-observable-universe/lean/QOU/StaircaseCornerHook.lean`) has `hCorner k := (k-1)+(k-1)+1` and proves `= 2k−1` by omega. The statement is pure ℕ arithmetic. The staircase partition, arm and leg never appear, so the Lean does not formalise "the hook of cell (0,0) of ρ_k".
- The `.md` does not fix ρ_k = (k, …, 1). With (k−1, …, 1) the hook would be 2k−3.
- The narrative does prove exactly the stated claim under the (k, …, 1) convention. The fix is cheap: define ρ_k and the hook via Mathlib `YoungDiagram`, or state the convention.

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Re-checked against main 2ae54ab40: the finding still holds as recorded (B10 `lem:staircase-corner-hook`.).
- Disclosed, not fixed: a dated `caveat` authorNote on the block's `.ts` (commit 24c44167e) says exactly what the Lean proves and what it does not. Kind, prose, `uses[]` and Lean untouched.
- The kind change / restatement / demotion is an owner decision (ask-first rule); framed in the coordinator report. Stays open until the claim is re-derived or restated.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md on main 2ae54ab40; list: L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, single-term trace, trefoil-primary electron, 'c_2 = −1 PROVED', χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean's premises or in the files it names.
