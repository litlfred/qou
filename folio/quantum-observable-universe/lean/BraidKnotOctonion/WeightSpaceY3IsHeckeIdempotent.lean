import BraidKnotOctonion.HeckeTrivialBlockWeight
import QOU.Nuclear.WeightSpaceMarkov

/-!
# The weight-space `y₃` is the trace of the Hecke trivial central idempotent

`QOU.QBeta.WeightSpaceMarkov.y3 = 1 − 2/[2]²` is obtained from the four weight spaces of
`V^{⊗3}` and is forced by the convention-D moment equations (`D_moments_force_weights`).
`HeckeTrivialBlockWeight.p3` is the central idempotent of the trivial block in `H₃(q)` itself,
built from the q-symmetriser.

`jimboTrace_p3_eq_y3`: the convention-D trace of `p3` equals `y3`. So the weight that the
electron unit split uses (`ElectronUnitSplit.tau_electron_eq_framing_mul_y3`, `τ_e = q³·y₃`) is
the trace of an element of the Hecke algebra, not only a solution of moment equations.

Generic field. No measured value enters.
-/

namespace QOU.IwahoriHecke.WeightSpaceY3IsHeckeIdempotent

open QOU.SchurWeyl QOU.SchurWeyl.HeckeInclusion QOU.SchurWeyl.JimboActionKernel
open QOU.IwahoriHecke.TLKernelRootOfUnity QOU.IwahoriHecke.HeckeTrivialBlockWeight

variable {K : Type*} [Field K] (q : K) (hq : q ≠ 0)

theorem y3_closed (hq21 : q ^ 2 + 1 ≠ 0) :
    QOU.QBeta.WeightSpaceMarkov.y3 q = (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  unfold QOU.QBeta.WeightSpaceMarkov.y3
  have e : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
  rw [e]
  field_simp
  ring

theorem jimboTrace_p3_eq_y3 (hq21 : q ^ 2 + 1 ≠ 0) (h3 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    jimboTrace q hq 2 (p3 q hq) = QOU.QBeta.WeightSpaceMarkov.y3 q := by
  rw [jimboTrace_p3 q hq hq21 h3, y3_closed q hq21]

end QOU.IwahoriHecke.WeightSpaceY3IsHeckeIdempotent
