---
# qou-pymd
title: 'SW-7-4x4: close the diagonal 4×4 (c₁=c₂=c₄=c₆=0) — finishes dim H_3(q)≥6 ⇒ dim=6 ⇒ Wedderburn iso (R2-inst)'
status: todo
type: task
created_at: 2026-08-10T18:45:50Z
updated_at: 2026-08-10T18:45:50Z
parent: qou-59vq
blocked_by:
    - qou-0h5k
---

The ONLY remaining step for dim H_3(q)=6 and the SW-7 Wedderburn iso H_3(q)≅ℝ×ℝ×M₂ (= R2-inst at n=3). WIP HeckeDim3Indep.lean already proves the reductions sorry-free (hqi, hK, hD, hC, h45:c₄=c₅, h36:c₃=c₆-c₄(q-q⁻¹)); the tail is one sorry. TASK: from the 2 seminormal DIAGONAL entries m00 (coeff c00=-1/(q³+q)) and m11 (coeff c11=q³/(q²+1)) + et (triv) + es (sign), after substituting c₅=c₄ and c₃=c₆-c₄(q-q⁻¹), close c₁=c₂=c₄=c₆=0. Clear denominators ×(q³+q),×(q²+1) to a polynomial identity in q; finish with explicit linear_combination coefficients (or nlinarith/field_simp). Only the coefficients remain. Ref: [kassel1995] Ch. XII (dim H_n(q)=n!).
