---
# qou-x09d
title: 'GAP: derive the exterior-quotient antisymmetry (sign on Λ²V, Hecke relation, Λ²W ≅ Wᘁ)'
status: todo
type: task
priority: high
tags:
    - 8f-decide
created_at: 2026-11-27T20:00:00Z
updated_at: 2026-11-27T20:00:00Z
parent: qou-x08k
---

Owner 2026-11-27: "What is the justification for these axioms physically? Where are they coming from?" / "Are these something derivable as we derived q?" — tapped "Yes, derive it".

Done (branch claude/derive-exterior-antisymmetry-2026-11-27, QOU/Core/ExteriorAntisymmetryDerivation.lean, sorry-free; audit docs/audits/2026-11-27-deriving-exterior-antisymmetry.md):
- balancing fixes c on Λ²V ≅ 1 only up to sign (s²c² = 1);
- Hecke value −q⁻¹ forces θ_V = ±q (not q^½);
- a Z/3 grading or grouplikes cannot move c²t (rebraid invariance);
- Λ²W ≅ Wᘁ + ribbon gives c²t = 1.

Open (keep this bean open until the math closes):
1. The sign c = −s⁻¹ on Λ²V is not derived (symmetric quotient satisfies the axioms).
2. The Hecke relation on all of V⊗V does not follow (spin-1 Rep_q(SL2) counterexample, paper level). Try the pivotal partial-trace route θ_V = λ₊(d − 1/d) + λ₋/d.
3. Λ²W ≅ Wᘁ is a hypothesis; would follow from a perfect wedge pairing.
4. Multi-fibre groupoid not examined as a source of the Z/3.
5. Corpus defect: braiding-eigenvalue-extraction asserts λ₊λ₋ = −1, which is the GL_q normalisation, inconsistent with Λ²V ≅ 1 in Rep_q(SL2). Not edited.
