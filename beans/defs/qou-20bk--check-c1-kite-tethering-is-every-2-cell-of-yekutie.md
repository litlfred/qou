---
# qou-20bk
title: 'Check C1: kite tethering — is every 2-cell of Yekutieli''s multiplicative integral a basepoint-tethered (pair-local) object, with the balloon the first 3-body object?'
status: completed
type: task
priority: normal
created_at: 2026-09-06T03:54:12Z
updated_at: 2026-09-06T04:05:04Z
parent: qou-2akx
---

## 2026-09-06 — DECIDED from the held definitions; my §4.4 reason was wrong, the conclusion survives sharpened

Read Def 4.1.1 (kite), 4.3.3 (basic Riemann product: RP0 = exp_H(area·Ψ_h(g)(β̃(z))), g = 1-dim MI along tether+probe), 4.3.6/4.2.7 (refined product over the 4^k-kite binary tessellation), 4.4.16 (MI = lim RP_k), Thm 0.4.2 (2-dim Stokes: Φ(MI(α,β|σ,τ)) = MI(α|∂(σ,τ))), Thm 0.9.1 (Ψ(g) = Ad_H(h)), §0.5 (H0 = ker Φ inertia, central abelian), Def 8.6.1 (γ = dβ + ψ_h(α)(β)), Lemma 8.6.3 (MI over ∂balloon ∈ H0), Thm 8.6.6 (γ inert; MI(α,β|∂(σ,τ)) = MI(α,γ|τ)).

TETHERING IS NOT THE MECHANISM — it is a basepoint gauge choice. The mechanism is the 2-dim Stokes theorem + Peiffer: for a connection–curvature (fake-flat) pair, the surface holonomy h is determined by its boundary path holonomy g = Φ(h) up to ker Φ, and ker Φ is CENTRAL (Lean: QOU/LiftingDescent/CrossedModuleSurfaceHolonomy.lean, sorry-free: ker_le_center, eq_mul_center_of_feedback_eq, classFn_factors_through_feedback). So: (i) the NON-ABELIAN content of any 2-dim Yekutieli object is its boundary 1-holonomy = a path-ordered product = word/ordering data (the degree-0 class of §7b–7d); (ii) the remainder is abelian/inert; (iii) the 3-dim Stokes theorem says the remainder over a closed surface is the ABELIAN volume integral of the inert 3-curvature γ over the 3-cell, additive over 3-cells.

CONSEQUENCE: no 2-dim Yekutieli object carries a non-abelian 3-body term. The ONLY 3-body-shaped object in the book is ∫γ over a balloon — abelian, extensive, additive over triples: exactly the 'super-pairwise additive extensive object' the Δ_λ audit asks for. It is live IFF γ ≠ 0 for the framework's connection — and that cannot be evaluated: Step 2's curvature is stipulated, not a form (no α, β exist in the Lean; cheat-sheet §2a). Route D2's decisive check is therefore 'construct (α, β) as forms on the brane tower, compute γ' — the honest wall, which is Step 2 itself. Route D1's Lean prune (ii) is vacuous as stated: in the alternating Čech complex a 2-object cover has C² = 0, so every H² class is 'pairwise trivial' by definition; the content is whether κ_n ≠ 0 for the tower, which needs the tower's transition data.
