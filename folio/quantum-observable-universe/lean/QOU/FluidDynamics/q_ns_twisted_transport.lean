import QOU.FluidDynamics.q_ns_triad_noncomm

/-!
# QOU.FluidDynamics.q_ns_twisted_transport

Bean `qou-q3dc`, owner route "q-Clebsch–Gordan coefficients", next gap after
`q_ns_triad_noncomm.lean`: is the q-NS transport an *untwisted* derivation on
`O_q(SU(2))`?

## The corpus answer is no

At generic `q` the corpus takes the connection on `O_q(SU(2))` to be built on
Woronowicz's 3D calculus (`ex:connection-su2`). There, `df = ∑ᵢ Xᵢ(f) ωᵢ`, and
the bimodule relations `ωᵢ g = θᵢ(g) ωᵢ` hold with torus automorphisms `θᵢ`.
So the vector fields satisfy a **twisted** Leibniz rule
`Xᵢ(fg) = Xᵢ f · θᵢ g + f · Xᵢ g`. The same holds in the archimedean
realisation, where the `q`-derivative is a `q`-difference operator. So
`q_ns_triad_noncomm.lean`, which needs `θ = id`, does not apply to the
corpus transport.

## What this file proves (any algebra, any linear functional)

* **Exact budget for twisted transport (`twisted_energy_budget`).** If `X` is
  `θ`-twisted and `φ ∘ X = 0`, then along `u̇ = Xu` the quadratic energy
  changes at the rate
  `φ(Xu·u) + φ(u·Xu) = φ(Xu · (u − θu))`.
  The rate is zero when `θ = id`, which recovers `transport_skew_nc`.
* **`q`-difference transport (`qDiff`).** For an algebra automorphism `θ` with
  `φ ∘ θ = φ` (for example a torus scaling, under which the Haar state is
  invariant) and a scalar `c ≠ 0`, the operator `D = (θ − id)/c` is a
  `θ`-twisted derivation with `φ ∘ D = 0` (`qDiff_leibniz`, `qDiff_div_free`).
* **It dissipates (`qDiff_energy_budget`).** Along `u̇ = Du`,
  `φ(Du·u) + φ(u·Du) = −c · φ(Du · Du)`.
  This is an identity, not an estimate. For a positive state and
  self-adjoint `Du`, the right side has the sign of `−c`. So `q`-difference
  transport is not energy-conserving. It carries an intrinsic dissipation term
  that is first order in the step `c`.
* **Non-vacuity (`qDiff_energy_budget_ne_zero`).** On `ℚ × ℚ` with the swap
  automorphism and the invariant functional `(a, b) ↦ a + b`, the budget for
  `u = (1, 0)`, `c = 1` is `−2`, not `0`.

## What this does not establish

* That the corpus `∇_q` *is* a `q`-difference operator on `O_q(SU(2))`. The
  corpus names the 3D calculus but does not define `∇_q` on the
  noncommutative algebra. The vector fields of that calculus are
  combinations of such twisted operators. Their exact form is not built here.
* Any sign for the dissipation on `O_q(SU(2))`, which needs positivity of the
  Haar state and a `*`-structure. Neither is used.
* Anything about Part A, which stays open (bean `qou-pa7n`).

No empirical value enters any proof.

## References

- [leitner2026] quantum-observable-universes/connection-su2.md (`ex:connection-su2`)
- [woronowicz1989] Woronowicz, *Differential calculus on compact matrix
  pseudogroups (quantum groups)*, Comm. Math. Phys. 122 (1989): the 3D
  calculus and its bimodule relations.
-/

namespace QOU.FluidDynamics.ModalTriad

variable {K : Type*} [Field K]
variable {A : Type*} [Ring A] [Algebra K A]

/-- **Exact energy budget for a twisted transport.** If
    `X(fg) = X f · θ g + f · X g` and `φ ∘ X = 0`, the rate of change of
    `φ(u²)` along `u̇ = X u` is `φ(X u · (u − θ u))`. -/
theorem twisted_energy_budget (X θ : A →ₗ[K] A)
    (hleib : ∀ f g, X (f * g) = X f * θ g + f * X g)
    (φ : A →ₗ[K] K) (hdiv : ∀ f, φ (X f) = 0) (u : A) :
    φ (X u * u) + φ (u * X u) = φ (X u * (u - θ u)) := by
  have h0 := hdiv (u * u)
  rw [hleib, map_add] at h0
  rw [mul_sub, map_sub]
  linear_combination h0

/-- The untwisted case of `twisted_energy_budget` is conservation. -/
theorem twisted_energy_budget_id (X : A →ₗ[K] A)
    (hleib : ∀ f g, X (f * g) = X f * g + f * X g)
    (φ : A →ₗ[K] K) (hdiv : ∀ f, φ (X f) = 0) (u : A) :
    φ (X u * u) + φ (u * X u) = 0 := by
  have := twisted_energy_budget X LinearMap.id (by simpa using hleib) φ hdiv u
  simpa using this

/-- The `q`-difference operator `D = (θ − id) / c`. -/
noncomputable def qDiff (θ : A →ₐ[K] A) (c : K) : A →ₗ[K] A :=
  c⁻¹ • (θ.toLinearMap - LinearMap.id)

theorem qDiff_apply (θ : A →ₐ[K] A) (c : K) (f : A) :
    qDiff θ c f = c⁻¹ • (θ f - f) := rfl

/-- `D = (θ − id)/c` is a `θ`-twisted derivation. -/
theorem qDiff_leibniz (θ : A →ₐ[K] A) (c : K) (f g : A) :
    qDiff θ c (f * g) = qDiff θ c f * θ g + f * qDiff θ c g := by
  simp only [qDiff_apply, map_mul, smul_mul_assoc, mul_smul_comm, ← smul_add]
  congr 1
  noncomm_ring

/-- `D` is divergence-free for a `θ`-invariant functional. -/
theorem qDiff_div_free (θ : A →ₐ[K] A) (c : K) (φ : A →ₗ[K] K)
    (hφ : ∀ f, φ (θ f) = φ f) (f : A) : φ (qDiff θ c f) = 0 := by
  rw [qDiff_apply, map_smul, map_sub, hφ, sub_self, smul_zero]

/-- **`q`-difference transport dissipates.** Along `u̇ = D u`,
    `φ(Du·u) + φ(u·Du) = −c · φ(Du·Du)`. -/
theorem qDiff_energy_budget (θ : A →ₐ[K] A) (c : K) (hc : c ≠ 0)
    (φ : A →ₗ[K] K) (hφ : ∀ f, φ (θ f) = φ f) (u : A) :
    φ (qDiff θ c u * u) + φ (u * qDiff θ c u) = -c * φ (qDiff θ c u * qDiff θ c u) := by
  rw [twisted_energy_budget (qDiff θ c) θ.toLinearMap (qDiff_leibniz θ c) φ
    (qDiff_div_free θ c φ hφ) u]
  have hu : u - θ u = -c • qDiff θ c u := by
    rw [qDiff_apply, smul_smul, neg_mul, mul_inv_cancel₀ hc, neg_smul, one_smul, neg_sub]
  rw [AlgHom.toLinearMap_apply, hu, mul_smul_comm, map_smul, smul_eq_mul]

/-! ### Non-vacuity -/

/-- The swap automorphism of `ℚ × ℚ`. -/
def swapQ : (ℚ × ℚ) →ₐ[ℚ] (ℚ × ℚ) where
  toFun x := (x.2, x.1)
  map_one' := rfl
  map_mul' _ _ := rfl
  map_zero' := rfl
  map_add' _ _ := rfl
  commutes' _ := rfl

/-- The swap-invariant functional `(a, b) ↦ a + b`. -/
def sumQ : (ℚ × ℚ) →ₗ[ℚ] ℚ where
  toFun x := x.1 + x.2
  map_add' x y := by simp only [Prod.fst_add, Prod.snd_add]; ring
  map_smul' t x := by simp only [Prod.smul_fst, Prod.smul_snd, smul_eq_mul, RingHom.id_apply]; ring

/-- The dissipation is not identically zero: for `u = (1, 0)` and `c = 1` the
    energy budget is `−2`. -/
theorem qDiff_energy_budget_ne_zero :
    sumQ (qDiff swapQ 1 (1, 0) * (1, 0)) + sumQ ((1, 0) * qDiff swapQ 1 (1, 0)) = -2 := by
  simp [qDiff_apply, swapQ, sumQ]
  norm_num

end QOU.FluidDynamics.ModalTriad
