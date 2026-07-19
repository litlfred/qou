---
# qou-k4ud
title: 'FRONTIER A: Δ_λ MAGNITUDE assembly — sign done (valuation); is |Δ_λ|=dim_λ closed-form? tr(g_ρ)→B wiring'
status: todo
type: task
created_at: 2026-07-19T03:32:44Z
updated_at: 2026-07-19T03:32:44Z
---


## SCOPING + ATTACK RESULT (2026-07-19)

**The magnitude is SETTLED, not open:** Δ_λ = (−1)^{n(λ)}·dim_λ (sign=valuation, |Δ_λ|=classical q=1 dim). The single-trace form Σ_λ y_λ χ^λ(β_D)(−1)^{n(λ)}dim_λ = −0.7439 → B(D)=0.380 MeV vs AME 2.2246 (−82.9%, under-binds ×5.85). Witnesses: deltalambda-magnitude-graded-trace, binding_energy_categorical_deuteron.

**The real wall = the He4-local ≥4-body cumulant b₄=−ln det(I+mS)**, structure DERIVED (b4_slater_antisymmetrizer_exchange_sign 7/7; Lean SU4SupermultipletGate + ReebPnMagnitude): eig(S)={±√5,±1} ⇒ det=(1−5m²)(1−m²), binding for 0<m<1/√5; SU(4) [1⁴] rank=C(4,A) vanishes A>4 (⁴He-locality structural); pp→+1, nn→−1 derived. OPEN: the scalar m∈(0,1/√5) + the pn sign + E0→MeV dressing.

**ATTACK on the icosahedral-m lead (Vector 2, docs/audits/2026-07-18-deltalambda-attack-vector-map.md):** probe `computations/deltalambda/b4_icosahedral_m_ceiling_probe.py` (2/2, scope-a, NO AME fit). The 1/√5 ceiling is genuinely √5/binary-icosahedral, BUT the primary Σ(2,3,5) objects OVERSHOOT it: S_00=0.526, S_01=0.851, φ⁻¹=0.618 all >1/√5=0.447 (unphysical as m); only secondary powers fall below (φ⁻²=0.382, 1/D²=0.276, sin²π/5=0.345), none structurally forced. So the lead does NOT yet supply a forward parameter-free m; picking by AME is the forbidden fit.

**KEY CROSS-LINK (Frontier A ↔ B):** the Σ(2,3,5) S-matrix lives at the root-of-unity FIBRE (|q|=1, unitary); the physical m (and τ=tr B, Frontier B qou-2v7k) live at real q₀. Both frontiers share the SAME fibre→observable archimedean-continuation wall (AGENTS.md Im(q) table). The continuation is the common bottleneck.

Status: magnitude sign+|Δ_λ| settled; b₄ structure derived; m/pn-sign open; icosahedral lead narrowed to "needs the archimedean continuation". Next = Frontier B (the shared wall).
