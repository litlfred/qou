---
# qou-0h5k
title: 'SW-7 (=R2c): Wedderburn iso H_n(q) ≅ ⊕_{λ⊢n} M_{d_λ}(K)'
status: todo
type: task
created_at: 2026-08-02T19:33:07Z
updated_at: 2026-08-02T19:33:07Z
parent: qou-59vq
blocked_by:
    - qou-j377
    - qou-wtny
---

Assemble ⊕_λ ρ_λ : H_n(q) → ⊕_λ M_{d_λ}(K); injective (SW-5/6) + dim both sides = n! (SW-3) ⇒ AlgEquiv. This is the  field of HeckeWedderburnData.

## Refine (recon): Mathlib Wedderburn-Artin is EXISTENCE only (exists_algEquiv_pi_matrix_of_isAlgClosed) — block set/dims existential. Route to the partition-INDEXED iso: assemble ⊕_λ ρ_λ (SW-4) + injective (SW-5) + dim match Σd_λ²=n! (SW-3) ⇒ AlgEquiv directly, rather than extracting from the existential form. Does NOT need Jacobson density (SW-9).

## ⏩ Spanning half of dim H_3(q)=6 PROVED (2026-08-10) — sorry-free

[`QOU/SchurWeyl/HeckeDim3.lean`](https://github.com/litlfred/qou/blob/claude/schur-weyl-sw5-irreducibility-2026-08-10/content/quantum-observable-universe/lean/QOU/SchurWeyl/HeckeDim3.lean):
`span_sixWords_eq_top` — the six words `{1,σ₀,σ₁,σ₀σ₁,σ₁σ₀,σ₀σ₁σ₀}` span
H_3(q) = Hecke K q qi 2, i.e. **dim_K H_3(q) ≤ 6**. Generic [CommRing K].
Proof: `adjoin{σ₀,σ₁}=⊤` (mk surjective + FreeAlgebra.induction) + closure
span = adjoin (`Algebra.adjoin_eq_span`) + closure_induction_left with the 12
explicit quadratic/braid left-mult reductions. Axiom-clean; wired into QOU.lean;
lean-direct exit 0. On PR #4942.

**Remaining for full SW-7 (Wedderburn iso / dim=6):** the matching lower bound
`dim ≥ 6` (the six words linearly INDEPENDENT), via ρ=(triv,sign,seminormalRep21):
either the 6×6 independence of ρ(sixWords) in ℝ×ℝ×M₂, or ρ surjective (then
dim≥6 from spanning ⇒ dim=6 ⇒ ρ iso = R2-inst). That is the next increment.
