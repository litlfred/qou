---
# qou-zxuy
title: 'RT finding: prop:crossed-module-euler-characteristic — ''−12 = dim V·χ(Σ₄)'' is a decide-checked coincidence presented as an identity; Φ₀ direction reversed in statement'
status: todo
type: bug
priority: normal
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B09).

- The Lean (`folio/quantum-observable-universe/lean/QOU/BraidKnot/CrossedModuleEulerCharacteristic.lean`) is `by decide` on a concrete Gaussian-integer computation. Its right-hand side is the named constant `dim_V * euler_bring`. Nothing links the matrix sum to the topology. All three independent legs (RT-1A, RT-2B, RT-3) flagged the identification as numerical only.
- In the `.md` statement, Φ₀: Q₈ → H₃(q) is written with domain Q₈ but defined on σ's, mapping to Q₈ units. The direction is reversed.
- The narrative asserts the intermediate matrix [[−6,3i],[3i,−6]] without computing it. The "Bring bridge" table (−8G, 3/16) is unproved.
- Rescope to "trace = −12, which numerically equals dim V·χ(Σ₄)", or supply a structural argument. See also qou-zmuu, qou-vfy1.

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Re-checked against main 2ae54ab40: the finding still holds as recorded (B09 `prop:crossed-module-euler-characteristic`.).
- Disclosed, not fixed: a dated `caveat` authorNote on the block's `.ts` (commit 24c44167e) says exactly what the Lean proves and what it does not. Kind, prose, `uses[]` and Lean untouched.
- The kind change / restatement / demotion is an owner decision (ask-first rule); framed in the coordinator report. Stays open until the claim is re-derived or restated.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md on main 2ae54ab40; list: L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, single-term trace, trefoil-primary electron, 'c_2 = −1 PROVED', χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean's premises or in the files it names.
