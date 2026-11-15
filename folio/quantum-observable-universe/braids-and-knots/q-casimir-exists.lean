import QOU.BraidKnot.CasimirShared


/-!
# QOU.QCasimir.exists — existence of the q-Casimir element

C_q = FE + (qK + q⁻¹K⁻¹ - (q + q⁻¹))/(q - q⁻¹)² is central in
𝒰_q(𝔰𝔲(2)) and acts as [j]_q[j+1]_q on V_j.

LaTeX: `\label{prop:q-casimir-exists}`

## References

- [manuscript] §4-braids-and-knots/q-casimir-exists
- [kassel1995] Quantum Groups (Springer GTM 155), §VI.4
- [lusztig1993] Introduction to Quantum Groups (Birkhäuser)
-/

namespace QOU

noncomputable section

/-- `R_q = ℚ(q)` has characteristic zero. -/
instance charZero_R_q_casimirExists : CharZero R_q :=
  charZero_of_injective_algebraMap (algebraMap ℚ R_q).injective

/-! **The former axiom `QCasimir.exists_axiom` was false** (removed
    2026-11-15). It claimed `Nonempty (QCasimirData qs)` for every
    `qs : QuantumSu2`. `QuantumSu2` only asks `q ≠ 1`, so `q = 0` is
    allowed, and then the field `qInv_left : qInv * q = 1` cannot hold.
    The data also needs a ring map `R_q → qs.Algebra`, which an arbitrary
    ring need not admit. The true statement is the construction of `C_q`
    in an actual `𝒰_q(𝔰𝔲(2))` with `q` generic; recorded as open in bean
    `qou-n2un`. -/

/-- A `QuantumSu2` with `q = 0`, which `QuantumSu2` allows. -/
def QCasimir.qsZero : QuantumSu2.{0} where
  q := 0
  q_ne_one := zero_ne_one
  Algebra := R_q
  E := 0
  F := 0
  K := 1
  K_inv := 1
  K_inv_left := mul_one 1
  K_inv_right := mul_one 1

/-- **The former axiom is false**: at `q = 0` there is no `QCasimirData`. -/
-- Ref: [kassel1995] Quantum Groups, §VI.4 (needs q invertible)
theorem QCasimir.not_exists_unconstrained :
    ¬ ∀ qs : QuantumSu2.{0}, Nonempty (QCasimirData qs) := by
  intro h
  obtain ⟨d⟩ := h QCasimir.qsZero
  have := d.qInv_left
  simp only [QCasimir.qsZero, mul_zero] at this
  exact zero_ne_one this

end

end QOU
