import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp

/-!
# The own-sector weight of the matter term comes from the state being a weight vector

The matter term of the two-term Lagrangian is `ψ* ≫ ψ ≫ 𝒟`. The composite `ψ* ≫ ψ` factors
through the unit object, so in a matrix model it is the rank-one matrix `ψ φ` (a column `ψ`
times a row `φ = ψ*`). Take the trace to be the quantum trace `τ(X) = tr(K X)` with a Cartan
weight `K`.

* `qtrace_rank_one`: if `K ψ = w • ψ`, then `tr(K · (ψ φ) · M) = w · tr(φ M ψ)`. So the
  sector weight of the matter term is the `K`-eigenvalue of the state `ψ`, and the rest is the
  single matrix element `φ M ψ`. Nothing is assumed about the trace beyond cyclicity.
* `matrix_element_eq_of_intertwiner`: if an invertible flip `P` sends the proton state to the
  neutron state (`P ψp = ψn`, `φn P = φp`) and intertwines the two connections (`P Mp = Mn P`), the two matrix elements are
  equal. So a common `c` for both nucleons follows from the flip intertwining the two horizontal connections.

Together these reduce the hypotheses `hHorizP`/`hHorizN` of `TwoTermMatterOwnSector.lean` to
two checkable facts: the nucleon state is a `K`-weight vector of weight `q` (proton) or `q⁻¹`
(neutron), and the flip intertwines the two horizontal connections.
-/

namespace QOU.MassTheory.MatterTraceWeightVector

open Matrix

variable {R : Type*} [CommRing R] {n : Type*} [Fintype n]

/-- The quantum trace of a rank-one matter term is the weight of the state times one matrix
element. -/
theorem qtrace_rank_one (K M : Matrix n n R) (ψ : Matrix n (Fin 1) R) (φ : Matrix (Fin 1) n R)
    (w : R) (hK : K * ψ = w • ψ) :
    trace (K * (ψ * φ) * M) = w * trace (φ * M * ψ) := by
  have h1 : K * (ψ * φ) * M = (K * ψ) * (φ * M) := by simp only [Matrix.mul_assoc]
  rw [h1, Matrix.trace_mul_comm, hK, Matrix.mul_smul, Matrix.trace_smul, smul_eq_mul,
    Matrix.mul_assoc]

/-- An up/down flip intertwining the proton and neutron connections (`P Mp = Mn P`, the
relation `P A₁ = B₁ P` of `NucleonWeightSpaceTwoTerm` has this shape) makes the two matrix
elements equal. -/
theorem matrix_element_eq_of_intertwiner (P Mp Mn : Matrix n n R)
    (ψp ψn : Matrix n (Fin 1) R) (φp φn : Matrix (Fin 1) n R)
    (hψ : P * ψp = ψn) (hφ : φn * P = φp) (hPM : P * Mp = Mn * P) :
    φn * Mn * ψn = φp * Mp * ψp := by
  rw [← hψ, ← hφ, Matrix.mul_assoc φn Mn, ← Matrix.mul_assoc Mn P, ← hPM]
  simp only [Matrix.mul_assoc]

/-- Both together: proton weight `q`, neutron weight `q⁻¹`, common matrix element. The
neutron's matter trace is `q⁻²` times the proton's, before the horizontal `q⁻¹`. -/
theorem nucleon_matter_qtraces (K P Mp Mn : Matrix n n R)
    (ψp ψn : Matrix n (Fin 1) R) (φp φn : Matrix (Fin 1) n R) (q qi : R)
    (hKp : K * ψp = q • ψp) (hKn : K * ψn = qi • ψn)
    (hψ : P * ψp = ψn) (hφ : φn * P = φp) (hPM : P * Mp = Mn * P) :
    trace (K * (ψp * φp) * Mp) = q * trace (φp * Mp * ψp) ∧
    trace (K * (ψn * φn) * Mn) = qi * trace (φp * Mp * ψp) := by
  refine ⟨qtrace_rank_one K Mp ψp φp q hKp, ?_⟩
  rw [qtrace_rank_one K Mn ψn φn qi hKn,
    matrix_element_eq_of_intertwiner P Mp Mn ψp ψn φp φn hψ hφ hPM]

/-- **The bridge's equal-horizontal-trace hypothesis forces the matrix element to vanish.**
`CategoricalLagrangianTwoTermBridge` assumes the proton and neutron horizontal matter traces
are equal (`hHoriz`). If the states are `K`-weight vectors of weights `q` and `q⁻¹` and the
flip intertwines the connections, the two traces are `q·m` and `q⁻¹·m`. They are equal only if
`m = 0` (for `q² ≠ 1`). So under (a) and (b), `hHoriz` leaves no horizontal own-sector constant. -/
theorem matrix_element_zero_of_equal_traces {F : Type*} [Field F] {n : Type*} [Fintype n]
    (K P Mp Mn : Matrix n n F)
    (ψp ψn : Matrix n (Fin 1) F) (φp φn : Matrix (Fin 1) n F) (q : F)
    (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1)
    (hKp : K * ψp = q • ψp) (hKn : K * ψn = q⁻¹ • ψn)
    (hψ : P * ψp = ψn) (hφ : φn * P = φp) (hPM : P * Mp = Mn * P)
    (hHoriz : trace (K * (ψn * φn) * Mn) = trace (K * (ψp * φp) * Mp)) :
    trace (φp * Mp * ψp) = 0 := by
  obtain ⟨hp, hn⟩ := nucleon_matter_qtraces K P Mp Mn ψp ψn φp φn q q⁻¹ hKp hKn hψ hφ hPM
  rw [hp, hn] at hHoriz
  have h : (q ^ 2 - 1) * trace (φp * Mp * ψp) = 0 := by
    have hqq : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
    have := congrArg (fun x => q * x) hHoriz
    try simp only at this
    linear_combination (-1 : F) * this + (trace (φp * Mp * ψp)) * hqq
  rcases mul_eq_zero.mp h with h1 | h1
  · exact absurd (sub_eq_zero.mp h1) hq2
  · exact h1

end QOU.MassTheory.MatterTraceWeightVector
