import QOU.MassTheory.NeutronCartanConstant
import Mathlib.LinearAlgebra.Matrix.Trace

/-!
# What the sector decomposition gives the own-sector premise, and what it does not

The own-sector premise (`NeutronSectorQTraceConstant`) says: the constant term of the nucleon
mass is a quantum trace taken on the nucleon's own weight space, while the volume term is a
whole-space trace. This file separates the part the axioms force from the part they do not.

**Forced (`qtrace_eq_sum_sectors`).** The maximal torus `T` of a quantum observable universe
(`def:maximal-torus`) acts diagonally on the weight spaces of `V`. If the pivotal element is a
torus element `K = Σ_N λ_N π_N` (weight projectors `π_N`, eigenvalues `λ_N`), then the
quantum trace of any endomorphism `x` is the `λ`-weighted sum of its weight-sector traces. For
`V^{⊗3}` and `K = K^{⊗3}`, the nucleon sectors carry `λ_p = q`, `λ_n = q⁻¹`. So once a term
of the mass is read sector by sector, its proton and neutron weights are forced, and with them
the ratio `q²` (`restrictedTrace_ratio`).

**Uniform rules fail (`uniform_rule_neutron_not_heavier`).** Any rule that treats the volume term and
the constant term alike (both bare, or both sector-resolved with the same weight) cannot give a
heavier neutron once the proton mass is positive. Both bare gives `m_n = m_p`; both resolved
gives `m_p = s q (v − c) > 0`, so `v > c`, and then `m_n − m_p = −s(q − q⁻¹)(v − c) < 0`.

So the premise needs a term-specific rule: the constant is read in the nucleon's own sector
and the volume term is not. The sector decomposition alone does not supply that distinction.
Whether some other part of the axioms does is open; this file does not exclude it. No measured
value enters.
-/

namespace QOU.MassTheory.OwnSectorFromWeightGrading

open Matrix QOU.MassTheory.NeutronCartanConstant

section Sectors

variable {R : Type*} [CommRing R] {n ι : Type*} [Fintype n] [Fintype ι]

/-- **Sector decomposition of the quantum trace.** If the pivotal element is a torus element
`K = Σ_N λ_N π_N`, the quantum trace `tr(K x)` is the `λ`-weighted sum of the sector traces
`tr(π_N x)`. -/
theorem qtrace_eq_sum_sectors (π : ι → Matrix n n R) (lam : ι → R) (x : Matrix n n R) :
    trace ((∑ i, lam i • π i) * x) = ∑ i, lam i * trace (π i * x) := by
  rw [Finset.sum_mul, trace_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  rw [smul_mul_assoc, trace_smul, smul_eq_mul]

/-- For an `x` commuting with an idempotent sector projector, the sector trace is the trace of
the restriction `π x π`: the trace on the sector itself. -/
theorem sector_trace_eq_restriction (p x : Matrix n n R) (hp : p * p = p) (hc : p * x = x * p) :
    trace (p * x) = trace (p * x * p) := by
  rw [mul_assoc, ← hc, ← mul_assoc, hp]

end Sectors

section Uniform

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]

/-- **A uniform rule cannot make the neutron heavier.** If the volume term and the constant
term carry the same rule (both bare or both Cartan-weighted), `s > 0`, `q > 1`, and the proton
mass is positive, then the neutron is not heavier. -/
theorem uniform_rule_neutron_not_heavier (a : Assembly R) {s q : R} (hrule : a.wVol = a.wConst)
    (hs : 0 < s) (hq : 1 < q) (hpos : 0 < mass a s q .p) :
    ¬ mass a s q .p < mass a s q .n := by
  rcases a with ⟨v, c, wv, wc⟩
  simp only at hrule
  subst hrule
  cases wv with
  | false =>
    simp [mass, termWeight]
  | true =>
    rw [neutron_heavier_iff _ hs hq]
    have hq0 : 0 < q := lt_trans zero_lt_one hq
    have hsq : 0 < s * q := mul_pos hs hq0
    have hp : mass ⟨v, c, true, true⟩ s q .p = s * q * (v - c) := by
      simp [mass, termWeight, weight]; ring
    rw [hp] at hpos
    have hvc : 0 < v - c := pos_of_mul_pos_right hpos hsq.le
    simp only [weightedNet, if_true]
    linarith

/-- The term-specific rule (constant resolved, volume bare) is the only one of the four that
makes the neutron heavier for a positive constant. Restated from `NeutronCartanConstant`. -/
theorem term_specific_rule_neutron_heavier {v c s q : R} (hc : 0 < c) (hs : 0 < s) (hq : 1 < q) :
    mass ⟨v, c, false, true⟩ s q .p < mass ⟨v, c, false, true⟩ s q .n :=
  const_weighted_neutron_heavier hc hs hq

end Uniform

end QOU.MassTheory.OwnSectorFromWeightGrading
