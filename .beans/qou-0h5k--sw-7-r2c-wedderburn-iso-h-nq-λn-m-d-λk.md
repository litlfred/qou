---
# qou-0h5k
title: 'SW-7 (=R2c): Wedderburn iso H_n(q) ≅ ⊕_{λ⊢n} M_{d_λ}(K)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-02T19:33:07Z
updated_at: 2026-08-11T00:18:45Z
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

## Independence (dim ≥ 6) — reductions VERIFIED, messy 4×4 tail remains (2026-08-10)

WIP saved (compiles, one Ref'd GAP sorry): scratchpad `HeckeDim3Indep.WIP.lean`.
Route: specialize K=ℝ, qi=q⁻¹; apply the three reps to a linear relation
Σcᵢwᵢ=0 and read off 6 equations (et=triv, es=sign, m00/m01/m10/m11=seminormal
M₂ entries). **VERIFIED sorry-free reductions:**
- `hqi := mul_inv_cancel₀ hq` (q·q⁻¹=1); `hqi_ne : q+q⁻¹≠0`; `hK : K≠0` (K=(q⁴+q²+1)/(q²+1)²).
- `hD : c₃ - c₄q⁻¹ + c₅q - c₆ = 0` — from `m10 = K·(…)`, factor K≠0.
  (`linear_combination m10 + c₆*K*hqi` — the c₆ term needs the q·q⁻¹=1 correction.)
- `hC : c₃ + c₄q - c₅q⁻¹ - c₆ = 0` — `linear_combination m01 + c₆*hqi`.
- `h45 : c₄ = c₅` — from `hC - hD = (c₄-c₅)(q+q⁻¹)=0`, q+q⁻¹≠0.
- `h36 : c₃ = c₆ - c₄(q-q⁻¹)` — `linear_combination hC - q⁻¹*h45`.

**Remaining (the GAP):** close `c₁=c₂=c₄=c₆=0` (then c₃=c₅=0 via h45,h36) from the
2 DIAGONAL seminormal entries `m00` (coeff c00=-1/(q³+q)) and `m11` (coeff
c11=q³/(q²+1)) together with `et`, `es`. After substituting c₅=c₄ and
c₃=c₆-c₄(q-q⁻¹), this is a 4×4 in (c₁,c₂,c₄,c₆); clear denominators
(×(q³+q), ×(q²+1)) to a polynomial identity in q and finish with
`linear_combination`/`nlinarith`. The coefficients are the only thing left to
compute. This closure gives dim H_3(q)=6 AND, since the 3 reps then biject,
the SW-7 Wedderburn iso H_3(q)≅ℝ×ℝ×M₂ = R2-inst at n=3.

## ✅ dim H_3(q) = 6 — BOTH BOUNDS PROVEN (2026-08-10)
- dim ≤ 6: HeckeDim3.span_sixWords_eq_top (sorry-free).
- dim ≥ 6: HeckeDim3Indep.sixWords_indep (sorry-free, qou-pymd closed).
Next for the SW-7 Wedderburn ISO (R2-inst at n=3): assemble the six words into a
Basis (finrank=6) and package ρ=(triv,sign,seminormalRep21) as the iso H_3(q)≅ℝ×ℝ×M₂.
The hard dimension theorem is done; remaining is finrank/Basis + iso plumbing.
