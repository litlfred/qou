import Mathlib.Algebra.Ring.Basic

namespace QOU.Information.OneDimChannel

variable {R : Type*} [CommRing R]
variable {M : Type*}

/-- A channel algebra or link category admitting a parallel composition
    and a Markov trace. -/
class SplitLinkTrace (M : Type*) (R : Type*) [CommRing R] where
  tr_M : M → R
  parallel : M → M → M
  multiplicative : ∀ A B : M, tr_M (parallel A B) = tr_M A * tr_M B

/-- **Parallel fibres are non-interacting.**
    The Markov trace is multiplicative over split links, so the
    transmitted datum of the joint channel factorizes. -/
theorem parallel_noninteraction [inst : SplitLinkTrace M R] (F_A F_B : M) :
    inst.tr_M (inst.parallel F_A F_B) =
    inst.tr_M F_A * inst.tr_M F_B :=
  inst.multiplicative F_A F_B

end QOU.Information.OneDimChannel
