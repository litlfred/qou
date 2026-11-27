import QOU.FluidDynamics.q_ns_twisted_transport
import CompactQuantumMetrics.OqSU2BudgetSign

/-!
# QOU.FluidDynamics.q_ns_cartan_transport_budget

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`), point 1: is the Cartan budget
integrand `h(X a · X a)` of `CompactQuantumMetrics.OqSU2BudgetSign` the energy budget of a
transport equation?

## Results (sorry-free)

Let `X = (id ⊗ c⁻¹(ε − χ_{s²}))Δ` be the Cartan left-invariant field and `h` the Haar state.

* `haarState_cartan_div_free`: `h(X f) = 0` for every `f`.
* `haarState_cartan_transport_energy`: for `c⁻¹ ≠ 0` and every `u`,
  `h(X u · u) + h(u · X u) = c · h(X u · X u)`.
  The left side is the rate of change of the quadratic energy `h(u²)` along `u̇ = X u`.
  So the budget integrand is that energy rate, up to the step `c`.
* `haarState_cartan_transport_dissipates`: over an ordered field, for `0 < q`, `q ≠ 1`,
  `0 < c⁻¹` and self-adjoint `u`, the energy rate is `≤ 0`.

The proof reuses `twisted_energy_budget` (`q_ns_twisted_transport.lean`) with the twist
`T_{s², s⁻²}` that `cartanField` gives the field.

## Not established here

* That `u̇ = X u` along the Cartan field is the q-NS transport. The corpus names the 3D
  calculus but does not define `∇_q` on `O_q(SU(2))` (see `q_ns_twisted_transport.lean`).
  So this identifies the integrand with the energy rate of *one* transport term, not of
  the q-NS equation.
* The off-diagonal pair `h(X₊ a · X₋ a)`. It is not the energy rate of a single transport
  along `X₊` or `X₋`: `twisted_energy_budget` gives `h(X₊ u · (u − θ u))`, a mixed
  `X₊`/Cartan term. How the pair enters the q-NS budget is not built here.
* Any statement about the limit `q → 1`, or about Part A (bean `qou-pa7n`).

No empirical value enters any proof.

## References

- [woronowicz1987-twisted-su2] S. L. Woronowicz, Twisted SU(2) group. An example of a
  non-commutative differential calculus, Publ. RIMS 23 (1987), 117–181, §4.
- [leitner2026] quantum-observable-universes/connection-su2.md (`ex:connection-su2`).
-/

namespace QOU.FluidDynamics.ModalTriad

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2

section Field

variable {K : Type*} [Field K] (q : Kˣ)

/-- The Cartan left-invariant field `(id ⊗ c⁻¹(ε − χ_{s²}))Δ`. -/
noncomputable abbrev cartanX (s : Kˣ) (cinv : K) : OqSU2 K q →ₗ[K] OqSU2 K q :=
  leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q (s ^ 2)).toLinearMap))

/-- The Cartan field is divergence-free for the Haar state. -/
theorem haarState_cartan_div_free (s : Kˣ) (cinv : K) (f : OqSU2 K q) :
    haarState q (cartanX q s cinv f) = 0 := by
  rw [(cartanField q (s ^ 2) cinv f f).1 f, map_smul, map_sub, haarState_torus, sub_self,
    smul_zero]

/-- **The Cartan budget integrand is the transport energy rate.** Along `u̇ = X u`,
    `h(X u · u) + h(u · X u) = c · h(X u · X u)`, with `c = (c⁻¹)⁻¹`. -/
theorem haarState_cartan_transport_energy (s : Kˣ) (cinv : K) (hc : cinv ≠ 0)
    (u : OqSU2 K q) :
    haarState q (cartanX q s cinv u * u) + haarState q (u * cartanX q s cinv u) =
      cinv⁻¹ * haarState q (cartanX q s cinv u * cartanX q s cinv u) := by
  rw [twisted_energy_budget (cartanX q s cinv)
      (torusScaleAlgHom q (s ^ 2) (s ^ 2)⁻¹).toLinearMap
      (fun f g => (cartanField q (s ^ 2) cinv f g).2) (haarState q)
      (haarState_cartan_div_free q s cinv) u]
  have hu : u - (torusScaleAlgHom q (s ^ 2) (s ^ 2)⁻¹).toLinearMap u =
      cinv⁻¹ • cartanX q s cinv u := by
    rw [(cartanField q (s ^ 2) cinv u u).1 u, smul_smul, inv_mul_cancel₀ hc, one_smul,
      AlgHom.toLinearMap_apply]
  rw [hu, mul_smul_comm, map_smul, smul_eq_mul]

end Field

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] (q : Kˣ)

/-- **Transport along the Cartan field dissipates the Haar energy** of a self-adjoint
    state, for `0 < q`, `q ≠ 1` and a positive inverse step `c⁻¹`. -/
theorem haarState_cartan_transport_dissipates (hq0 : 0 < (q : K)) (hq1 : (q : K) ≠ 1)
    (s : Kˣ) (cinv : K) (hc : 0 < cinv) (u : OqSU2 K q) (hu : compactStar q u = u) :
    haarState q (cartanX q s cinv u * u) + haarState q (u * cartanX q s cinv u) ≤ 0 := by
  rw [haarState_cartan_transport_energy q s cinv hc.ne' u]
  exact mul_nonpos_of_nonneg_of_nonpos (inv_nonneg.2 hc.le)
    (haarState_cartan_nonpos q hq0 hq1 s cinv u hu)

end Ordered

end QOU.FluidDynamics.ModalTriad
