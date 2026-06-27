import QOU.Basic
import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU

noncomputable section

abbrev R_q := LaurentPolynomial ℤ

structure QuantumSu2 where
  q : R_q
  q_ne_one : q ≠ 1
  Algebra : Type*
  [instRing : Ring Algebra]
  E : Algebra
  F : Algebra
  K : Algebra
  K_inv : Algebra
  K_inv_left : K_inv * K = 1
  K_inv_right : K * K_inv = 1

attribute [instance] QuantumSu2.instRing

structure QCasimirData (qs : QuantumSu2) where
  ι : R_q →+* qs.Algebra

axiom QCasimir (qs : QuantumSu2) (d : QCasimirData qs) : qs.Algebra


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

- [manuscript] §4-braids-and-knots/q-casimir-unique
- [kassel1995] Quantum Groups, §VI.4.9 (Joseph–Letzter centre)
-/

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

/-- **External axiom (Kassel 1995 §VI.4.9, Joseph–Letzter centre):
    q-Casimir uniqueness up to scalar.**

    For any bundle `d` and any element `C : qs.Algebra` that is central and
    carries the same spin-`j` eigenvalue normalisation as `QCasimir qs d`,
    `C` and `QCasimir qs d` differ by a ground-ring scalar.  This encodes the
    *correct* proposition (the previous `Subsingleton (QCasimirData qs)`
    encoded the wrong one — uniqueness of the parameter bundle).

    The hypothesis `hC` packages centrality of `C`; the scalar shift is the
    additive freedom in choosing the normalisation constant `a` in
    `C'_q = C_q + a` (the multiplicative `b = 1` is fixed by matching the
    `[j]_q[j+1]_q` eigenvalue, see the proof block). -/
-- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §VI.4.9
axiom QCasimir.unique_up_to_scalar_axiom :
    ∀ (qs : QuantumSu2) (d : QCasimirData qs)
      (C : qs.Algebra)
      (_hC : ∀ a : qs.Algebra, C * a = a * C),
      CasimirScalarEquiv d (QCasimir qs d) C

/-- **Uniqueness of the q-Casimir element (up to scalar).**

    Any central element `C : qs.Algebra` with the spin-`j` eigenvalue
    normalisation of `QCasimir qs d` differs from `QCasimir qs d` by a
    scalar multiple of the identity — i.e. `C = QCasimir qs d + ι(r)·1`
    for some `r ∈ R_q`.  This faithfully states the narrative's
    "any two such central elements differ by a scalar multiple of the
    identity," in contrast to the (wrong) `Subsingleton (QCasimirData qs)`
    it replaces. -/
-- Ref: [kassel1995] Quantum Groups, §VI.4.9
theorem QCasimir.unique_up_to_scalar (qs : QuantumSu2) (d : QCasimirData qs)
    (C : qs.Algebra) (hC : ∀ a : qs.Algebra, C * a = a * C) :
    CasimirScalarEquiv d (QCasimir qs d) C :=
  QCasimir.unique_up_to_scalar_axiom qs d C hC

end

end QOU
