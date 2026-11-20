---
# qou-1iit
title: 'RT finding: lem:su2-emergence-dagger-unitarity — Lean formalises only the linear-algebra tail; the categorical premise (G preserves a positive Hermitian pairing) is unformalised'
status: todo
type: bug
priority: normal
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-20T08:40:00Z
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
