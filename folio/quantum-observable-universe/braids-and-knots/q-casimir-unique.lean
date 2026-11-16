import QOU.BraidKnot.CasimirShared


/-!
# QOU.QCasimir.unique_up_to_scalar — uniqueness of the q-Casimir

`C_q` is the unique central element of `𝒰_q(𝔰𝔲(2))` whose eigenvalue
on the spin-`j` irrep is `[j]_q [j+1]_q`, **up to a scalar multiple of
the identity**: any two central elements with this property differ by
`r · 1` for a ground-ring scalar `r ∈ R_q`.

LaTeX: `\label{prop:q-casimir-unique}`

## Why the statement is up-to-scalar, not `Subsingleton`

`QCasimirData qs` (in the sibling file `q-casimir.lean`) is the
**auxiliary parameter bundle** (explicit inverse witnesses for `q` and
`q - q⁻¹`, the central embedding `ι : R_q →+* qs.Algebra`).  It is **not**
the q-Casimir element — that is `QCasimir qs d : qs.Algebra`, built from a
bundle `d`.  Asserting `Subsingleton (QCasimirData qs)` claims the *bundle*
is unique, which is both false (the embedding/inverse fields admit distinct
valid choices) and beside the point: the narrative claim is about the
**element**.

The honest statement is therefore phrased on `qs.Algebra` directly: two
elements that are central and have the prescribed eigenvalue normalisation
differ by a ground-ring scalar (Joseph–Letzter: the centre
`Z(𝒰_q(𝔰𝔲(2)))` is the polynomial ring `R_q[C_q]`, so a central element
fixed to be degree `≤ 1` in `C_q` with vanishing eigenvalue on `V_0` is
pinned up to the additive `R_q`-scalar — Kassel §VI.4.9).

## References

- [leitner2026] §4-braids-and-knots/q-casimir-unique
- [kassel1995] Quantum Groups, §VI.4.9 (Joseph–Letzter centre)
-/

namespace QOU

noncomputable section

/-- **Differ by a scalar multiple of the identity.**  Two algebra elements
    `x y : qs.Algebra` are *scalar-equivalent* when `y = x + ι(r) · 1` for
    some ground-ring scalar `r ∈ R_q` embedded via a central embedding `ι`.
    This is the precise meaning of the narrative's "differ by a scalar
    multiple of the identity" (`R_q`-scalars sit in the centre, so the shift
    `C'_q = C_q + ι(r)·1` exhausts the admissible re-normalisations). -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §VI.4.9
def CasimirScalarEquiv {qs : QuantumSu2} (d : QCasimirData qs)
    (x y : qs.Algebra) : Prop :=
  ∃ r : R_q, y = x + d.ι r

/-- `R_q = ℚ(q)` has characteristic zero. -/
instance charZero_R_q_casimirUnique : CharZero R_q :=
  charZero_of_injective_algebraMap (algebraMap ℚ R_q).injective

/-! **The former axiom `QCasimir.unique_up_to_scalar_axiom` was false**
    (removed 2026-11-15). It claimed that every central `C` in every
    `qs.Algebra` equals `QCasimir qs d + ι r`. Two problems:

    1. `qs.Algebra` is an arbitrary ring, so its centre can be far bigger
       than `ι(R_q)`. `not_unique_up_to_scalar_unconstrained` below uses
       `R_q × R_q`, where `(1, 0)` is central but not `0 + ι r`.
    2. Even in the true `𝒰_q(𝔰𝔲(2))` the statement fails: the centre is
       the polynomial ring `R_q[C_q]`, so `C_q²` is central and is not
       `C_q + scalar`. The manuscript claim needs the eigenvalue
       normalisation (degree-one in `C_q`) as a hypothesis.

    The repaired statement is recorded as open in bean `qou-n2un`. -/

/-- The diagonal algebra `R_q × R_q` with `q = 2`, `E = F = 0`,
    `K = K⁻¹ = 1`. -/
def QCasimir.qsDiag : QuantumSu2.{0} where
  q := 2
  q_ne_one := by norm_num
  Algebra := R_q × R_q
  E := 0
  F := 0
  K := 1
  K_inv := 1
  K_inv_left := mul_one 1
  K_inv_right := mul_one 1

/-- Casimir data on `QCasimir.qsDiag`, with `ι` the diagonal map. -/
def QCasimir.dDiag : QCasimirData QCasimir.qsDiag where
  qInv := 1 / 2
  qInv_left := by simp only [QCasimir.qsDiag]; norm_num
  qInv_right := by simp only [QCasimir.qsDiag]; norm_num
  ι := RingHom.prod (RingHom.id R_q) (RingHom.id R_q)
  ι_central := fun _ _ => Prod.ext (mul_comm _ _) (mul_comm _ _)
  invQm := ((2 / 3 : R_q), (2 / 3 : R_q))
  invQm_left := by
    simp only [QCasimir.qsDiag, RingHom.prod_apply, RingHom.id_apply,
      Prod.mk_mul_mk, Prod.mk_eq_one]
    constructor <;> norm_num
  invQm_right := by
    simp only [QCasimir.qsDiag, RingHom.prod_apply, RingHom.id_apply,
      Prod.mk_mul_mk, Prod.mk_eq_one]
    constructor <;> norm_num
  invQm_central := fun _ => Prod.ext (mul_comm _ _) (mul_comm _ _)

/-- **The former axiom is false**: in `R_q × R_q` the central element
    `(1, 0)` is not the Casimir plus a scalar. -/
-- Ref: [kassel1995] Quantum Groups, §VI.4.9 (centre is R_q[C_q])
theorem QCasimir.not_unique_up_to_scalar_unconstrained :
    ¬ ∀ (qs : QuantumSu2.{0}) (d : QCasimirData qs) (C : qs.Algebra),
      (∀ a : qs.Algebra, C * a = a * C) → CasimirScalarEquiv d (QCasimir qs d) C := by
  intro h
  obtain ⟨r, hr⟩ := h QCasimir.qsDiag QCasimir.dDiag ((1 : R_q), (0 : R_q))
    (fun _ => Prod.ext (mul_comm _ _) (mul_comm _ _))
  have hC : QCasimir QCasimir.qsDiag QCasimir.dDiag = 0 := by
    simp [QCasimir, QCasimir.qsDiag, QCasimir.dDiag]
  rw [hC, zero_add] at hr
  have h1 : (1 : R_q) = r := congrArg Prod.fst hr
  have h0 : (0 : R_q) = r := congrArg Prod.snd hr
  exact one_ne_zero (h1.trans h0.symm)

end

end QOU
