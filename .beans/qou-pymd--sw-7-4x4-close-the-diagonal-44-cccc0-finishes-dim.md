---
# qou-pymd
title: 'SW-7-4x4: close the diagonal 4×4 (c₁=c₂=c₄=c₆=0) — finishes dim H_3(q)≥6 ⇒ dim=6 ⇒ Wedderburn iso (R2-inst)'
status: completed
type: task
priority: normal
created_at: 2026-08-10T18:45:50Z
updated_at: 2026-08-10T19:44:44Z
parent: qou-59vq
blocked_by:
    - qou-0h5k
---

The ONLY remaining step for dim H_3(q)=6 and the SW-7 Wedderburn iso H_3(q)≅ℝ×ℝ×M₂ (= R2-inst at n=3). WIP HeckeDim3Indep.lean already proves the reductions sorry-free (hqi, hK, hD, hC, h45:c₄=c₅, h36:c₃=c₆-c₄(q-q⁻¹)); the tail is one sorry. TASK: from the 2 seminormal DIAGONAL entries m00 (coeff c00=-1/(q³+q)) and m11 (coeff c11=q³/(q²+1)) + et (triv) + es (sign), after substituting c₅=c₄ and c₃=c₆-c₄(q-q⁻¹), close c₁=c₂=c₄=c₆=0. Clear denominators ×(q³+q),×(q²+1) to a polynomial identity in q; finish with explicit linear_combination coefficients (or nlinarith/field_simp). Only the coefficients remain. Ref: [kassel1995] Ch. XII (dim H_n(q)=n!).

## FULL derivation solved on paper (2026-08-10) — Lean plumbing is all that remains

The 4×4 closure is mathematically DONE; only the `linear_combination` coefficient
tuning remains. Robust Lean recipe (AVOID `field_simp` — it reshapes the hyps;
instead multiply by the nonzero denominator and factor the OTHER nonzero factor):

Given (verified, sorry-free in the file): h45 (c₄=c₅), h36 (c₃=c₆-c₄(q-q⁻¹)),
hqi (q·q⁻¹=1), and the raw equations et, es, m00, m01, m10, m11.

1. **hP: c₃ + q(c₄+c₅) + q²c₆ = 0.**  `et - m00` cancels c₁,c₂ (both have c₁+c₂q).
   Identity: (q³+q)·(et_lhs - m00_lhs) = (q⁴+q²+1)·(c₃+q(c₄+c₅)+q²c₆)  [polynomial,
   the 1/(q³+q) in m00 cancels]. So:
   `have h1 : (q^4+q^2+1)*(c₃+q*(c₄+c₅)+q^2*c₆) = 0 := by linear_combination (q^3+q)*et - (q^3+q)*m00`
   then `(mul_eq_zero.mp h1).resolve_left (by positivity)`.
2. **hQ: c₃q² - q(c₄+c₅) + c₆ = 0.**  `es - m11` cancels c₁,c₂ (both c₁-c₂q⁻¹).
   es has q⁻¹..q⁻³, m11 has q⁻¹ and 1/(q²+1); multiply by q³(q²+1) and use hqi:
   identity q³(q²+1)(es_lhs-m11_lhs) = (q⁴+q²+1)·(c₃q²-q(c₄+c₅)+c₆) modulo q·q⁻¹=1.
   `linear_combination q^3*(q^2+1)*es - q^3*(q^2+1)*m11 + <c-terms>*hqi` (tune the hqi
   coefficient to kill residual q·q⁻¹ factors), then factor (q⁴+q²+1)≠0.
3. **hS: c₃+c₆=0.**  hP+hQ = (1+q²)(c₃+c₆); factor (1+q²)≠0.
4. **hc6: c₆=0.**  hT: c₄(q-q⁻¹)=2c₆ (`linear_combination hS - h36`); hU: 2qc₄=c₆(1-q²)
   (`linear_combination hP - hS - q*h45`).  Eliminate c₄: 2q·hT vs (q-q⁻¹)·hU with
   q·(q-q⁻¹)=q²-1 (hqi) gives c₆·(q²+1)²=0  [4q²+(q²-1)²=(q²+1)²]; factor ≠0.
   (The hV linear_combination needs its hqi coefficient tuned — this was the failing line.)
5. **Cascade:** hc3 (hS-hc6), hc4 (hU: 2qc₄=0, q≠0), hc5 (h45), then hc2 from
   et-es (c₂(q+q⁻¹)=0, needs hqi for the q⁻¹² terms), hc1 from et.

Everything except the exact hqi-correction coefficients in steps 2,4,5 is settled.
An agent should extract each hyp's post-simp form with a `have DIAG:True:=by exact e`
probe (as done here) and tune. Est: ~1 focused session. Result: dim H_3(q)=6 ⇒
SW-7 iso H_3(q)≅ℝ×ℝ×M₂ = R2-inst at n=3.

## ✅ CLOSED (2026-08-10) — sixWords_indep now sorry-free

The 4×4 closure compiled. Robust recipe that worked: `subst c₅` (=c₄); derive
hPz/hQz by multiply-by-denominator with `linear_combination (norm := (field_simp; ring))`
(ring alone can't cancel (q³+q)·(1/(q³+q)) — field_simp uses the ≠0 hyps); then the
q⁻¹-free cascade hS→hU,hT→ c₆(q²+1)²=0 ⇒ c₆=0, c₄=0, c₃=0, then c₂(q+q⁻¹)=0⇒c₂=0, c₁=0.
Axiom-clean [propext, Classical.choice, Quot.sound]; lean-direct exit 0; 0 sorries.
dim H_3(q) ≥ 6 proven; with span_sixWords_eq_top (dim ≤ 6) ⇒ dim H_3(q) = 6.
