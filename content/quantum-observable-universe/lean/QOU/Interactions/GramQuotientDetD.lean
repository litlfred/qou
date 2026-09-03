import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Symmetric
import Mathlib.Tactic
import QOU.Shared.DetFin
import QOU.Interactions.GramMatrixH3Symbolic

/-!
# QOU.Interactions.GramQuotientDetD

**The convention-D successor to `gramMatrix_det_ne_zero`: the form induced by the
canonical H_3(q) Gram on the quotient `H_3(q)/rad` is NONDEGENERATE — and
indefinite — for every real `q`.**

## The gap this closes

`GramMatrixH3Symbolic.gramMatrix_det_ne_zero` is a convention-C result
(`z = √q/(q+1)`, excised 2026-08-09 / re-affirmed 2026-08-15). In the canonical
convention D (`z = q³/(q²+1)`) the 6×6 Gram is **exactly singular** for every
`q` — `gramMatrixD_det_eq_zero` — because `z_D` is a root of the determinant
factor `(q²+1)z − q³` (`markovWeightD_root`). So the C theorem has no D
analogue at the 6×6 level, and the positive-definiteness reading built on it
fails outright (`gramMatrixD_not_posDef`). Bean `qou-cds2` names the
replacement as its last open Lean item: what survives is the form on the
quotient by the radical.

## The statement

Under D the radical is one-dimensional, spanned by the three-strand
q-antisymmetriser `gramRadicalD q = (−q³, q², q², −q, −q, 1)`
(`gramMatrixD_mulVec_radical`). Its **last** coordinate is `1`
(`gramRadicalD_last`), nonzero for every `q` including `q = 0`, so the basis
vectors `e_0, …, e_4` project to a basis of `H_3(q)/rad` and the induced form
in that complement basis is the **leading 5×5 principal minor** of the Gram —
`gramQuotientD q`, defined here as a `Matrix.submatrix` of `gramMatrixD q`
along `Fin.castSucc` (never re-typed). Its determinant is

  det( G_D | H_3/rad ) = −(q⁴+1)(q²−q+1)⁴(q²+q+1)⁴ / (q²+1)¹⁰

(`gramQuotientD_det`). Every factor is real-rootless —
`q⁴+1 > 0`, `q²−q+1 = (q−½)²+¾ > 0`, `q²+q+1 = (q+½)²+¾ > 0`, `(q²+1)¹⁰ > 0` —
so the determinant is **strictly negative for every real `q`**
(`gramQuotientD_det_neg`), hence **nonzero** (`gramQuotientD_det_ne_zero`):
the quotient form is nondegenerate, with **no hypothesis on `q`** at all —
strictly stronger than the `1 < u` the C theorem needs.

The negative sign is not incidental: it means the nondegenerate quotient form
is **indefinite**, consistent with the negative eigenvalue the D-frame spectrum
carries at `q₀` (`gram-matrix-dual.witness.json`, and the docstring of
`gramMatrixD_not_posDef`). **Any D-frame successor to the C-frame
positive-definiteness reading must therefore say "nondegenerate", never
"positive".**

## What is basis-dependent and what is not

The VALUE above is stated in the complement basis `e_0, …, e_4`. A different
complement of the radical changes it by the **square of a change-of-basis
determinant**; the NONVANISHING is basis-independent, and that — not the value
— is what replaces `gramMatrix_det_ne_zero`. Quote the closed form only
together with its basis.

## Proof route

`Matrix.det_fin_five` (`QOU.Shared.DetFin`, the explicit 120-term Leibniz
formula) expands the determinant; the entries are unfolded from `gramEntryD`
by `simp` (every leading-block denominator divides `(q²+1)²`); `field_simp`
clears the `(q²+1)`-powers against the polynomial right-hand side, and `ring`
closes the degree-20 identity

  (q²+1)¹⁰ · det = −q²⁰ − 4q¹⁸ − 11q¹⁶ − 20q¹⁴ − 29q¹² − 32q¹⁰ − 29q⁸ − 20q⁶
                   − 11q⁴ − 4q² − 1 = −(q⁴+1)(q⁴+q²+1)⁴ .

The same closed form, the factorisation, the absence of real roots and the
value at `q₀` are reproduced independently, exactly over `ℚ(q)`, by the probe
`computations/probes/gram_h3_quotient_nondegeneracy_probe.py` (witness
`computations/probes/gram-h3-quotient-nondegeneracy-probe.witness.json`,
fields `quotient_form.det`, `numerator_factored`, `denominator_factored`,
`det_at_q0`).

## Base ring (AGENTS.md §7c)

The file inherits `ℝ` from `gramMatrixD`. That is acceptable here because the
two corollaries (`gramQuotientD_det_neg`, `gramQuotientD_det_ne_zero`) genuinely
use the order: real-rootlessness of the numerator is the archimedean content.
The closed-form identity itself is a `ℚ(q)` fact; it would state over any
field of characteristic zero, and does so the moment `gramMatrixD` does.

Ref: [halverson_ram_1998] Hoefsmit seminormal Gram on H_3(q)
Ref: [manuscript] docs/coordination/trace-convention-registry.md
Ref: bean `qou-cds2` ("S2 (SCIENCE): `pyhecke.gram.z` and the Gram
     singularity"), whose 2026-08-30 entry names this determinant as the last
     open Lean item; bean `qou-pmkh` (the four C-premised computation sites
     that cannot be migrated by substituting `z_D`)
Ref: `computations/probes/gram_h3_quotient_nondegeneracy_probe.py`
-/

namespace QOU.Interactions.GramMatrixH3Symbolic

/-- **THEOREM.** The last coordinate of the radical direction is `1`.

    This is what makes `e_0, …, e_4` a complement of the radical for every
    `q` (including `q = 0`), so that the quotient form may be read off the
    leading 5×5 principal minor. `gramRadicalD_ne_zero` used the same
    coordinate; this states it as the equality the complement argument
    actually needs. -/
theorem gramRadicalD_last (q : ℝ) : gramRadicalD q 5 = 1 := rfl

/-- The form induced by the canonical (convention-D) Gram on `H_3(q)/rad`, in
    the complement basis `e_0, …, e_4`: the leading `5×5` principal minor of
    `gramMatrixD q`, obtained as a `submatrix` along `Fin.castSucc`. The
    entries are **not** re-typed — everything below is derived from the
    36-entry table `gramEntryD`. -/
noncomputable def gramQuotientD (q : ℝ) : Matrix (Fin 5) (Fin 5) ℝ :=
  (gramMatrixD q).submatrix Fin.castSucc Fin.castSucc

/-- `gramQuotientD` is the leading block of `gramMatrixD`, entrywise. -/
theorem gramQuotientD_apply (q : ℝ) (i j : Fin 5) :
    gramQuotientD q i j = gramMatrixD q (Fin.castSucc i) (Fin.castSucc j) := rfl

/-- **THEOREM.** The quotient form is symmetric — inherited from
    `gramMatrixD_isSymm`, since a principal submatrix of a symmetric matrix is
    symmetric. -/
theorem gramQuotientD_isSymm (q : ℝ) : (gramQuotientD q).IsSymm :=
  (gramMatrixD_isSymm q).submatrix Fin.castSucc

/-- **THEOREM.** `G[0,0] = tr_M(1) = 1` survives on the quotient. -/
theorem gramQuotientD_top_left (q : ℝ) : gramQuotientD q 0 0 = 1 := rfl

set_option maxHeartbeats 4000000 in
/-- **THEOREM (cleared form).** `(q²+1)¹⁰ · det(G_D | H_3/rad)` is the
    degree-20 polynomial `−(q⁴+1)(q²−q+1)⁴(q²+q+1)⁴`.

    The workhorse: `Matrix.det_fin_five` expands the determinant into its 120
    Leibniz terms, the entries are unfolded from `gramEntryD`, `field_simp`
    clears the `(q²+1)`-power denominators and `ring` closes the polynomial
    identity. No hypothesis on `q`. -/
theorem gramQuotientD_det_mul_denom (q : ℝ) :
    (gramQuotientD q).det * (q ^ 2 + 1) ^ 10
      = -(q ^ 4 + 1) * (q ^ 2 - q + 1) ^ 4 * (q ^ 2 + q + 1) ^ 4 := by
  have hd : (q ^ 2 + 1) ≠ 0 := by positivity
  rw [Matrix.det_fin_five]
  simp only [gramQuotientD_apply, gramMatrixD, Matrix.of_apply, Fin.castSucc_zero,
    Fin.castSucc_one, Fin.reduceCastSucc, gramEntryD]
  field_simp
  ring

/-- **MAIN THEOREM.** The determinant of the form induced on `H_3(q)/rad` by
    the canonical Gram, in the complement basis `e_0, …, e_4`:

      det( G_D | H_3/rad ) = −(q⁴+1)(q²−q+1)⁴(q²+q+1)⁴ / (q²+1)¹⁰ .

    This is the convention-D replacement for the C-only
    `gramMatrix_det_ne_zero`. The value is basis-dependent (it moves by the
    square of a change-of-basis determinant); its nonvanishing is not. -/
theorem gramQuotientD_det (q : ℝ) :
    (gramQuotientD q).det
      = -(q ^ 4 + 1) * (q ^ 2 - q + 1) ^ 4 * (q ^ 2 + q + 1) ^ 4 / (q ^ 2 + 1) ^ 10 :=
  (eq_div_iff (by positivity)).mpr (gramQuotientD_det_mul_denom q)

/-- **THEOREM.** The quotient determinant is strictly negative for **every**
    real `q` — no `q > 0`, no `q > 1`, no substrate hypothesis. Each factor of
    the closed form is real-rootless: `q⁴+1 > 0`, `q²−q+1 = (q−½)²+¾ > 0`,
    `q²+q+1 = (q+½)²+¾ > 0`, `(q²+1)¹⁰ > 0`. So the nondegenerate quotient
    form is **indefinite**: any D-frame successor to the C-frame
    positive-definiteness reading must say "nondegenerate", never "positive". -/
theorem gramQuotientD_det_neg (q : ℝ) : (gramQuotientD q).det < 0 := by
  rw [gramQuotientD_det]
  have h1 : 0 < q ^ 4 + 1 := by positivity
  have h2 : 0 < q ^ 2 - q + 1 := by nlinarith [sq_nonneg (2 * q - 1)]
  have h3 : 0 < q ^ 2 + q + 1 := by nlinarith [sq_nonneg (2 * q + 1)]
  have h4 : 0 < (q ^ 2 + 1) ^ 10 := by positivity
  have hnum : 0 < (q ^ 4 + 1) * (q ^ 2 - q + 1) ^ 4 * (q ^ 2 + q + 1) ^ 4 :=
    mul_pos (mul_pos h1 (pow_pos h2 4)) (pow_pos h3 4)
  have hneg : -(q ^ 4 + 1) * (q ^ 2 - q + 1) ^ 4 * (q ^ 2 + q + 1) ^ 4 < 0 := by
    have e : -(q ^ 4 + 1) * (q ^ 2 - q + 1) ^ 4 * (q ^ 2 + q + 1) ^ 4
        = -((q ^ 4 + 1) * (q ^ 2 - q + 1) ^ 4 * (q ^ 2 + q + 1) ^ 4) := by ring
    rw [e]
    exact neg_neg_of_pos hnum
  exact div_neg_of_neg_of_pos hneg h4

/-- **THEOREM.** The induced form on `H_3(q)/rad` is **nondegenerate for every
    real `q`** — the statement that replaces `gramMatrix_det_ne_zero` in the
    canonical frame. Basis-independent, unlike the value it is derived from. -/
theorem gramQuotientD_det_ne_zero (q : ℝ) : (gramQuotientD q).det ≠ 0 :=
  (gramQuotientD_det_neg q).ne

end QOU.Interactions.GramMatrixH3Symbolic
