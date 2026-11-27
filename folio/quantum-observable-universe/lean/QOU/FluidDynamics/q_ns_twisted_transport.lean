import QOU.FluidDynamics.q_ns_triad_noncomm
import CompactQuantumMetrics.OqSU2HaarState

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
* **The sign is set by orientation (`qDiff_neg`).** `D` with step `−c` is
  `−D` with step `c`, so the backward difference has the opposite budget, as
  upwind and downwind schemes do. The sign is a choice of the operator, not a
  property of the algebra.
* **The balanced difference conserves energy (`qCen_energy_conserving`).**
  For an automorphism `θ` with `φ ∘ θ = φ`, the operator `(θ − θ⁻¹)/c` (the
  one behind balanced `q`-integers) gives `φ(Xu·u) + φ(u·Xu) = 0` exactly,
  for every `u` and every `c`.
* **Instantiated on `O_q(SU(2))` (`theta3D`, `theta3D_energy`).** The
  automorphism that Hadfield–Krähmer attach to Woronowicz's 3D calculus,
  `(a, b, c, d) ↦ (q⁻²a, q⁴b, q⁻⁴c, q²d)` (the twist of its cyclic cocycle), is
  the corpus torus automorphism `torusScaleAlgEquiv q (q⁻²) (q⁴)`. For any
  functional invariant under it, the one-sided budget is `−c·φ(Du·Du)` and the
  balanced budget is `0`. Invariance of the Haar state is a hypothesis here.
  This `σ` is **not** the Leibniz twist of a left-invariant field: that twist is
  a right translation `(u, u⁻¹)`, while `σ` is a two-sided translation
  (`OqSU2Coproduct.lean`, `hk_sigma_eq_two_sided`, `cartanField`).
* **Non-vacuity (`qDiff_energy_budget_ne_zero`).** On `ℚ × ℚ` with the swap
  automorphism and the invariant functional `(a, b) ↦ a + b`, the budget for
  `u = (1, 0)`, `c = 1` is `−2`, not `0`.

## What this does not establish

* That the corpus `∇_q` *is* a `q`-difference operator on `O_q(SU(2))`. The
  corpus names the 3D calculus but does not define `∇_q` on the
  noncommutative algebra. The vector fields of that calculus are
  combinations of such twisted operators. Their exact form is not built here.
* Which difference (one-sided or balanced) the corpus vector fields are.
  The vector fields of the 3D calculus are not built here.
* Any sign for the dissipation on `O_q(SU(2))`, which needs positivity of the
  Haar state and a `*`-structure. Neither is used. Haar invariance under
  `theta3D` is carried as a hypothesis.
* Anything about Part A, which stays open (bean `qou-pa7n`).

No empirical value enters any proof.

## References

- [leitner2026] quantum-observable-universes/connection-su2.md (`ex:connection-su2`)
- [woronowicz1989] Woronowicz, *Differential calculus on compact matrix
  pseudogroups (quantum groups)*, Comm. Math. Phys. 122 (1989): the 3D
  calculus and its bimodule relations.
- [hadfield-krahmer-2005] Hadfield, Krähmer, *Twisted homology of quantum
  SL(2)*, arXiv:math/0405249, section "three dimensional left-covariant
  calculus": the automorphism `σ` used for `theta3D`
  (library `arxiv-math-0405249v5`).
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

/-! ### Orientation, and the balanced (centred) q-difference -/

/-- Reversing the step reverses the operator: `D_{−c} = −D_c`. So the sign of
    the budget term `−c·φ(Du·Du)` is set by the orientation of the transport,
    not by the calculus. -/
theorem qDiff_neg (θ : A →ₐ[K] A) (c : K) (f : A) :
    qDiff θ (-c) f = -qDiff θ c f := by
  rw [qDiff_apply, qDiff_apply, inv_neg, neg_smul]

/-- The balanced `q`-difference `(θ − θ⁻¹)/c`, the operator behind balanced
    `q`-integers `[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)`. -/
noncomputable def qCen (θ : A ≃ₐ[K] A) (c : K) : A →ₗ[K] A :=
  c⁻¹ • (θ.toLinearMap - θ.symm.toLinearMap)

theorem qCen_apply (θ : A ≃ₐ[K] A) (c : K) (f : A) :
    qCen θ c f = c⁻¹ • (θ f - θ.symm f) := rfl

/-- **The balanced `q`-difference conserves energy.** For a `θ`-invariant
    functional, `φ(Xu·u) + φ(u·Xu) = 0` with `X = (θ − θ⁻¹)/c`, for every
    `u` and every step `c`. The one-sided terms of the two orientations
    cancel exactly. -/
theorem qCen_energy_conserving (θ : A ≃ₐ[K] A) (c : K) (φ : A →ₗ[K] K)
    (hφ : ∀ f, φ (θ f) = φ f) (u : A) :
    φ (qCen θ c u * u) + φ (u * qCen θ c u) = 0 := by
  have h1 : φ (θ.symm u * u) = φ (u * θ u) := by
    rw [← hφ (θ.symm u * u), map_mul, AlgEquiv.apply_symm_apply]
  have h2 : φ (u * θ.symm u) = φ (θ u * u) := by
    rw [← hφ (u * θ.symm u), map_mul, AlgEquiv.apply_symm_apply]
  simp only [qCen_apply, smul_mul_assoc, mul_smul_comm, map_smul, smul_eq_mul,
    sub_mul, mul_sub, map_sub, h1, h2]
  ring

/-! ### The Hadfield–Krähmer automorphism of the 3D calculus on `O_q(SU(2))` -/

section OqSU2

open QOU.AlgebraicSubstrate QOU.AlgebraicSubstrate.OqSU2

/-- The automorphism Hadfield–Krähmer attach to Woronowicz's three-dimensional
    left-covariant calculus (the twist of its cyclic 3-cocycle),
    `(α, β, γ, δ) ↦ (q⁻² α, q⁴ β, q⁻⁴ γ, q² δ)` (Hadfield–Krähmer, eq.
    `3dcalc_aut`), as the corpus torus automorphism. -/
noncomputable def theta3D (q : Kˣ) : OqSU2 K q ≃ₐ[K] OqSU2 K q :=
  torusScaleAlgEquiv q (q⁻¹ ^ 2) (q ^ 4)

theorem theta3D_alpha (q : Kˣ) :
    theta3D q (α q) = (((q⁻¹ ^ 2 : Kˣ) : K)) • α q := by
  simp [theta3D, torusScaleAlgEquiv, torusScaleAlgHom]

theorem theta3D_beta (q : Kˣ) :
    theta3D q (β q) = (((q ^ 4 : Kˣ) : K)) • β q := by
  simp [theta3D, torusScaleAlgEquiv, torusScaleAlgHom]

/-- The 3D-calculus `q`-difference is a twisted derivation of `O_q(SU(2))`. -/
theorem theta3D_qDiff_leibniz (q : Kˣ) (c : K) (f g : OqSU2 K q) :
    qDiff (theta3D q).toAlgHom c (f * g) =
      qDiff (theta3D q).toAlgHom c f * theta3D q g + f * qDiff (theta3D q).toAlgHom c g :=
  qDiff_leibniz _ c f g

/-- **On `O_q(SU(2))`, for any `θ₃D`-invariant functional** (the Haar state is
    invariant under the torus, which is carried as the hypothesis `hφ`): the
    one-sided 3D-calculus transport changes the energy at rate
    `−c·φ(Du·Du)`, and the balanced one conserves it. -/
theorem theta3D_energy (q : Kˣ) (c : K) (hc : c ≠ 0) (φ : OqSU2 K q →ₗ[K] K)
    (hφ : ∀ f, φ (theta3D q f) = φ f) (u : OqSU2 K q) :
    φ (qDiff (theta3D q).toAlgHom c u * u) + φ (u * qDiff (theta3D q).toAlgHom c u) =
        -c * φ (qDiff (theta3D q).toAlgHom c u * qDiff (theta3D q).toAlgHom c u) ∧
      φ (qCen (theta3D q) c u * u) + φ (u * qCen (theta3D q) c u) = 0 :=
  ⟨qDiff_energy_budget _ c hc φ hφ u, qCen_energy_conserving _ c φ hφ u⟩

/-- `θ₃D`-invariance of every zero-weight functional (in particular of the Haar
    state), discharged by the torus conjugation of the algebraic model. -/
theorem theta3D_zeroWeight_invariant (q : Kˣ) (lam : ℕ → K) (f : OqSU2 K q) :
    zeroWeightFunctional q lam (theta3D q f) = zeroWeightFunctional q lam f :=
  zeroWeightFunctional_torusEquiv q lam _ _ f

/-- **The energy identities for the Haar state, with no invariance hypothesis**: the
    `hφ` of `theta3D_energy` is proved for the algebraically constructed `haarState`
    (indeed for every zero-weight functional). -/
theorem theta3D_energy_haar (q : Kˣ) (c : K) (hc : c ≠ 0) (u : OqSU2 K q) :
    haarState q (qDiff (theta3D q).toAlgHom c u * u) +
        haarState q (u * qDiff (theta3D q).toAlgHom c u) =
        -c * haarState q (qDiff (theta3D q).toAlgHom c u * qDiff (theta3D q).toAlgHom c u) ∧
      haarState q (qCen (theta3D q) c u * u) + haarState q (u * qCen (theta3D q) c u) = 0 :=
  theta3D_energy q c hc (haarState q) (theta3D_zeroWeight_invariant q _) u

end OqSU2

end QOU.FluidDynamics.ModalTriad
