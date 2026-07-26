import QOU.Machinery.HeckeH4WedderburnMulC
import Mathlib.Tactic

/-!
# QOU.Machinery.HeckeH4WedderburnInv — left/right inverse of the rank-4 coordinate map

Wedderburn tranche **W3 (capstone)** (bean `qou-308a`; design doc §4): the
corollaries the assembly file `HeckeH4Wedderburn` consumes, derived from
the Lean-verified matrix identities of `HeckeH4WedderburnMul*` through the
`mulVec` glue of `HeckeH4WedderburnCoord`:

* `wedderburnInvV₄_left` — the coordinate **left inverse** (injectivity
  input): the inverse formulas recover every NF coordinate from the
  character/block component tuple;
* `homVec_wedderburnInvV₄` + the five component **right-inverse** lemmas
  `chiNF₄_wedderburnInvV₄_plus/_minus`, `blockOf22/31/211_wedderburnInvV₄`
  (surjectivity input).

Genericity hypotheses (read off $\det A = -(q^2+1)^{24}(q^4+1)^{10}
(q^2-q+1)^3(q^2+q+1)^3/q^{50}$): `q ≠ 0`, `q ^ 2 + 1 ≠ 0`,
`q ^ 4 + q ^ 2 + 1 ≠ 0`, `q ^ 4 + 1 ≠ 0` — note the **new** `[4]`-type
condition `q ^ 4 + 1 ≠ 0` absent at rank 3.  Over $\mathbb{R}$ all four
denominators are positive for `q ≠ 0`, so only `q ≠ 0` survives.

HONESTY (STRICT, §"Axiomatization is NOT a Proof"): every lemma is
discharged by computation — no axiom, no `sorry`, no conditional class, no
`native_decide`; the sympy cofactors are *payloads*, re-verified by Lean's
`linear_combination` kernel check.

Base ring (§7c): generic `[Field K]` — inverses are genuinely used; no
archimedean construct.

-- Ref: [wenzl1988] https://doi.org/10.1007/BF01239526
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/

namespace QOU.Machinery.H4

variable {K : Type*} [Field K]

/-- **Left inverse on coordinates (sorry-free):** the inverse formulas
    recover every NF coordinate from the character/block component tuple —
    the injectivity input of `wedderburn₄`. -/
theorem wedderburnInvV₄_left (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) (v : Fin 24 → K) :
    wedderburnInvV₄ q (chiNF₄ q v) (chiNF₄ (-q⁻¹) v) (blockOf22 q v)
      (blockOf31 q v) (blockOf211 q v) = v := by
  show (coordMInv q).mulVec (homVec q v) = v
  rw [homVec_eq_mulVec, Matrix.mulVec_mulVec,
    coordMInv_mul_coordM q hq h2 h3 h4, Matrix.one_mulVec]

/-- **Right inverse, stacked form (sorry-free):** the assembled map applied
    to the inverse formulas returns the component tuple — the surjectivity
    input of `wedderburn₄`. -/
theorem homVec_wedderburnInvV₄ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) (s t : K)
    (M2 : Matrix (Fin 2) (Fin 2) K) (M31 M211 : Matrix (Fin 3) (Fin 3) K) :
    homVec q (wedderburnInvV₄ q s t M2 M31 M211) = wvec s t M2 M31 M211 := by
  rw [homVec_eq_mulVec, wedderburnInvV₄_eq_mulVec, Matrix.mulVec_mulVec,
    coordM_mul_coordMInv q hq h2 h3 h4, Matrix.one_mulVec]

/-- **Right inverse, first character (sorry-free).** -/
theorem chiNF₄_wedderburnInvV₄_plus (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) (s t : K)
    (M2 : Matrix (Fin 2) (Fin 2) K) (M31 M211 : Matrix (Fin 3) (Fin 3) K) :
    chiNF₄ q (wedderburnInvV₄ q s t M2 M31 M211) = s := by
  have h := congrFun (homVec_wedderburnInvV₄ q hq h2 h3 h4 s t M2 M31 M211) 0
  simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using h

/-- **Right inverse, second character (sorry-free).** -/
theorem chiNF₄_wedderburnInvV₄_minus (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) (s t : K)
    (M2 : Matrix (Fin 2) (Fin 2) K) (M31 M211 : Matrix (Fin 3) (Fin 3) K) :
    chiNF₄ (-q⁻¹) (wedderburnInvV₄ q s t M2 M31 M211) = t := by
  have h := congrFun (homVec_wedderburnInvV₄ q hq h2 h3 h4 s t M2 M31 M211) 1
  simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using h

/-- **Right inverse, $(2,2)$ block (sorry-free).** -/
theorem blockOf22_wedderburnInvV₄ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) (s t : K)
    (M2 : Matrix (Fin 2) (Fin 2) K) (M31 M211 : Matrix (Fin 3) (Fin 3) K) :
    blockOf22 q (wedderburnInvV₄ q s t M2 M31 M211) = M2 := by
  have h := homVec_wedderburnInvV₄ q hq h2 h3 h4 s t M2 M31 M211
  ext r c
  fin_cases r <;> fin_cases c
  · have hc := congrFun h 2
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 3
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 4
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 5
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc

/-- **Right inverse, $(3,1)$ block (sorry-free).** -/
theorem blockOf31_wedderburnInvV₄ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) (s t : K)
    (M2 : Matrix (Fin 2) (Fin 2) K) (M31 M211 : Matrix (Fin 3) (Fin 3) K) :
    blockOf31 q (wedderburnInvV₄ q s t M2 M31 M211) = M31 := by
  have h := homVec_wedderburnInvV₄ q hq h2 h3 h4 s t M2 M31 M211
  ext r c
  fin_cases r <;> fin_cases c
  · have hc := congrFun h 6
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 7
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 8
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 9
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 10
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 11
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 12
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 13
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 14
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc

/-- **Right inverse, $(2,1,1)$ block (sorry-free).** -/
theorem blockOf211_wedderburnInvV₄ (q : K) (hq : q ≠ 0) (h2 : q ^ 2 + 1 ≠ 0)
    (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0) (s t : K)
    (M2 : Matrix (Fin 2) (Fin 2) K) (M31 M211 : Matrix (Fin 3) (Fin 3) K) :
    blockOf211 q (wedderburnInvV₄ q s t M2 M31 M211) = M211 := by
  have h := homVec_wedderburnInvV₄ q hq h2 h3 h4 s t M2 M31 M211
  ext r c
  fin_cases r <;> fin_cases c
  · have hc := congrFun h 15
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 16
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 17
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 18
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 19
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 20
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 21
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 22
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc
  · have hc := congrFun h 23
    simpa only [homVec, wvec, Matrix.cons_val_zero, Matrix.cons_val_succ, Matrix.cons_val',
    Matrix.cons_val, Fin.isValue, Matrix.head_cons] using hc

end QOU.Machinery.H4
