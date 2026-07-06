import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring


/-!
# QOU.AlphaBasisKnot.deltaQ_eq_h_qbracket

The q-dimension decoration of the α_{basis-knot} couplings:
`δ_q(T_{2,k}) = q^k − q^{-k} = h·[k]_q`, `h = q − q⁻¹`, `[k]_q = (q^k−q^{-k})/h`.

A trivial but pre-archimedean identity — it lives entirely in the substrate
ring (no `ℝ`, no `π`); only `q − q⁻¹ ≠ 0` is needed for the division.
Underlies `prop:alpha-em-categorical-trace-ratio`
(`α_EM = h²/(q·δ_q(T_{2,9})·δ_q(T_{3,5}))`). Symbolic cross-check:
`computations/delta_q_h_bracket_identity.py`.

LaTeX label: `prop:alpha-basis-knot-delta-q`. **Ground ring**: a field `R`.
-/

namespace QOU.AlphaBasisKnot

variable {R : Type*} [Field R]

/-- q-dimension decoration `δ_q(T_{2,k}) = q^k − q^{-k}`. -/
def deltaQ (q : R) (k : ℕ) : R := q ^ k - q⁻¹ ^ k

/-- Quantum integer `[k]_q = (q^k − q^{-k})/(q − q⁻¹)`. -/
noncomputable def qbracket (q : R) (k : ℕ) : R := (q ^ k - q⁻¹ ^ k) / (q - q⁻¹)

/-- **`δ_q(T_{2,k}) = h·[k]_q`** with `h = q − q⁻¹` — the pre-archimedean
    q-dimension identity (no `π`). Sorry-free. -/
-- Ref: [manuscript] mass-theory/alpha-basis-knot-delta-q
theorem deltaQ_eq_h_qbracket (q : R) (k : ℕ) (hh : q - q⁻¹ ≠ 0) :
    deltaQ q k = (q - q⁻¹) * qbracket q k := by
  unfold deltaQ qbracket
  rw [mul_comm, div_mul_cancel₀ _ hh]

end QOU.AlphaBasisKnot
