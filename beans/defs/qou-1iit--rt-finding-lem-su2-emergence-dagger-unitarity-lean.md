---
# qou-1iit
title: 'RT finding: lem:su2-emergence-dagger-unitarity — Lean formalises only the linear-algebra tail; the categorical premise (G preserves a positive Hermitian pairing) is unformalised'
status: todo
type: bug
priority: normal
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-ncxf
---

qou-ncxf pass-1 (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B03).

- Lean (`folio/quantum-observable-universe/lean/QOU/su2_emergence_dagger_unitarity.lean`) proves: a 2×2 complex matrix preserving the standard Hermitian product is unitary. This is correct and genuine.
- The `.md` claims G ⊆ U(2) for the tensor automorphisms of τ. RT-2 and RT-3 found that the narrative does not show:
  - that the Frobenius pairing is sesquilinear/Hermitian (it is defined bilinearly);
  - positive-definiteness (only non-degeneracy f†f = 0 ⇒ f = 0 is stated);
  - that S(f) makes sense on a morphism;
  - that dim τ(V) = 2.
- So the Lean statement is strictly weaker than the `.md` claim. Either formalise the categorical step, or rescope the `.md` to "given a positive Hermitian τ-pairing preserved by g, g is unitary".

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Re-checked against main 2ae54ab40: the finding still holds as recorded (B03 `lem:su2-emergence-dagger-unitarity`.).
- Disclosed, not fixed: a dated `caveat` authorNote on the block's `.ts` (commit 24c44167e) says exactly what the Lean proves and what it does not. Kind, prose, `uses[]` and Lean untouched.
- The kind change / restatement / demotion is an owner decision (ask-first rule); framed in the coordinator report. Stays open until the claim is re-derived or restated.
- Superseded-premise check (owner 2026-11-21, against docs/coordination/owner-rulings.md on main 2ae54ab40; list: L± photon, virtual photons, pre-Nov-15 γγ letters, T(2,n_s), convention C, single-term trace, trefoil-primary electron, 'c_2 = −1 PROVED', χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean's premises or in the files it names.
