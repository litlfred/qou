import QOU.FluidDynamics.q_ns_triad_derivation

/-!
# QOU.FluidDynamics.q_ns_triad_noncomm

Bean `qou-q3dc`. Owner route "q-Clebsch–Gordan coefficients", next step
"twisted Leibniz on `O_q(SU(2))`" (2026-11-27).

`q_ns_triad_derivation.lean` derived triad-wise energy conservation from the
Leibniz rule, but only for a **commutative** algebra with a trace. The
coordinate algebra `O_q(SU(2))` is noncommutative, and its Haar state is not a
trace (`h(ab) = h(b σ(a))` with the modular automorphism `σ = nuAlgEquiv`,
`CompactQuantumMetrics.OqSU2ModularNakayama`).

## Result: neither commutativity nor traciality is needed

Let `φ : A → K` be **any** linear functional on an associative, possibly
noncommutative, algebra `A`. Let `X : A → A` be linear, satisfy the untwisted
Leibniz rule `X(fg) = X f · g + f · X g`, and satisfy `φ ∘ X = 0`. Then:

* `φ(u · X u) + φ(X u · u) = φ(X(u²)) = 0` (`transport_skew_nc`). So the
  quadratic energy `u ↦ φ(u²)` is conserved along `u̇ = X u`. No trace and no
  modular twist enters.
* The **symmetrised form** `B(f, g) = (φ(fg) + φ(gf))/2` is the only part of
  `φ` that the energy sees, and `X` is `B`-skew. Modal couplings taken against
  `B` are therefore pairwise skew (`modalDnc_skew`). Through `ofTransportSkew`
  they give a Kraichnan-conserving `TriadCoeff` (`advectionTriadNc`).
* For modes that are orthogonal under `B` (not necessarily under `φ` itself),
  `φ(u²) = ∑ wₙ aₙ²` (`parsevalNc`), and the Galerkin transfer is the advection
  (`transfer_eq_advection_nc`).

So the obstruction recorded in `q_ns_triad_derivation.lean` disappears. The
twist `σ` does not have to be undone, because the energy only sees the
symmetric part of the Haar form. For a self-adjoint velocity `u = u*` the
Hilbert energy `h(u* u)` is `h(u²)`, which is the quantity conserved here.

## Non-vacuity on a non-tracial state

For a state with the modular property `φ(ab) = φ(b σ(a))` and an element `c`
fixed by `σ`, the inner derivation `f ↦ cf − fc` satisfies both the untwisted
Leibniz rule and `φ ∘ X = 0` (`innerDer_leibniz`,
`innerDer_div_free_of_kms`). On `O_q(SU(2))` the corpus already proves that the
modular automorphism `nuAlgEquiv` fixes the Cartan elements
(`nuAlgEquiv_fixes_cartan`), so such transports exist there. This file does not
build the Haar state itself.

## What stays a hypothesis

* **The untwisted Leibniz rule (`hleib`).** The derivations of `O_q(SU(2))`
  that come from the quantum group are typically *twisted*
  (`X(fg) = X f · g + σ'(f) · X g` for an automorphism `σ'`). The argument
  above uses the untwisted form. Whether the q-NS transport `∇_q` is an
  untwisted derivation on the noncommutative algebra is **not** settled here.
  For a twisted derivation, `φ(X(u²)) = φ(X u · u) + φ(σ'(u) · X u)`, which is
  not a symmetric combination. This is the precise remaining gap.
* **Incompressibility (`hdiv`)**, `φ ∘ Xₚ = 0`, as in the corpus.
* **The selection rule (`hsel`)**, `B(eₙ, Xₚ eᵣ) = 0` off fusion triads.
* **The numerical coupling values.** None are computed and none enter a proof.

In the noncommutative case the corpus field `q⁻¹ X + (1 − q⁻¹) θ ξ` is a
derivation only when `θ` is central. This file does not use `qField`.

No empirical value enters any proof.

## References

- [leitner2026] fluid-dynamics/q-navier-stokes.md (`def:q-navier-stokes`)
- [woronowicz1987] Woronowicz, *Compact matrix pseudogroups*, Comm. Math.
  Phys. 111 (1987): the Haar state of `SU_q(2)` and its modular property.
-/

namespace QOU.FluidDynamics.ModalTriad

open Finset

variable {K : Type*} [Field K]
variable {A : Type*} [Ring A] [Algebra K A]

/-- The symmetrised bilinear form `B(f, g) = (φ(fg) + φ(gf)) / 2`. -/
noncomputable def symForm (φ : A →ₗ[K] K) (f g : A) : K :=
  (φ (f * g) + φ (g * f)) / 2

theorem symForm_comm (φ : A →ₗ[K] K) (f g : A) : symForm φ f g = symForm φ g f := by
  unfold symForm; ring

/-- **Noncommutative transport skewness.** A divergence-free (untwisted)
    derivation conserves `φ(u²)`: `φ(u · X u) + φ(X u · u) = 0`. -/
theorem transport_skew_nc (X : A →ₗ[K] A)
    (hleib : ∀ f g, X (f * g) = X f * g + f * X g)
    (φ : A →ₗ[K] K) (hdiv : ∀ f, φ (X f) = 0) (u : A) :
    φ (u * X u) + φ (X u * u) = 0 := by
  have h0 := hdiv (u * u)
  rw [hleib, map_add] at h0
  rw [add_comm]; exact h0

/-- `B(u, X u) = 0`. -/
theorem symForm_skew_diag (X : A →ₗ[K] A)
    (hleib : ∀ f g, X (f * g) = X f * g + f * X g)
    (φ : A →ₗ[K] K) (hdiv : ∀ f, φ (X f) = 0) (u : A) :
    symForm φ u (X u) = 0 := by
  unfold symForm; rw [transport_skew_nc X hleib φ hdiv u]; simp

/-- **Polarised skewness**: `B(f, X g) + B(g, X f) = 0`. -/
theorem symForm_skew (X : A →ₗ[K] A)
    (hleib : ∀ f g, X (f * g) = X f * g + f * X g)
    (φ : A →ₗ[K] K) (hdiv : ∀ f, φ (X f) = 0) (f g : A) :
    symForm φ f (X g) + symForm φ g (X f) = 0 := by
  have hfg := symForm_skew_diag X hleib φ hdiv (f + g)
  have hf := symForm_skew_diag X hleib φ hdiv f
  have hg := symForm_skew_diag X hleib φ hdiv g
  unfold symForm at *
  simp only [map_add, add_mul, mul_add] at hfg
  linear_combination hfg - hf - hg

/-- Modal couplings against the symmetrised form:
    `Dₙₚᵣ = B(eₙ, Xₚ eᵣ) / B(eₙ, eₙ)`. -/
noncomputable def modalDnc (φ : A →ₗ[K] K) (e : ℕ → A) (X : ℕ → A →ₗ[K] A)
    (n p r : ℕ) : K :=
  symForm φ (e n) (X p (e r)) / φ (e n * e n)

theorem modalDnc_skew (φ : A →ₗ[K] K) (e : ℕ → A) (X : ℕ → A →ₗ[K] A)
    (hleib : ∀ p f g, X p (f * g) = X p f * g + f * X p g)
    (hdiv : ∀ p f, φ (X p f) = 0)
    (hw : ∀ n, φ (e n * e n) ≠ 0) (n p r : ℕ) :
    φ (e n * e n) * modalDnc φ e X n p r + φ (e r * e r) * modalDnc φ e X r p n = 0 := by
  unfold modalDnc
  rw [mul_div_cancel₀ _ (hw n), mul_div_cancel₀ _ (hw r)]
  exact symForm_skew (X p) (hleib p) φ (hdiv p) (e n) (e r)

/-- **The triad system of a divergence-free advection on a noncommutative
    algebra.** The conservation field is proved from the untwisted Leibniz rule;
    no trace property of `φ` is used. -/
noncomputable def advectionTriadNc (φ : A →ₗ[K] K) (e : ℕ → A) (X : ℕ → A →ₗ[K] A)
    (hleib : ∀ p f g, X p (f * g) = X p f * g + f * X p g)
    (hdiv : ∀ p f, φ (X p f) = 0)
    (hw : ∀ n, φ (e n * e n) ≠ 0)
    (hsel : ∀ n p r, ¬ FusionTriad n p r → symForm φ (e n) (X p (e r)) = 0) :
    TriadCoeff K :=
  ofTransportSkew (fun n => φ (e n * e n)) (modalDnc φ e X)
    (fun n p r h => by simp [modalDnc, hsel n p r h])
    (modalDnc_skew φ e X hleib hdiv hw)

/-- `φ(u²)` only sees the symmetrised form. -/
theorem phi_sq_eq_symForm (φ : A →ₗ[K] K) (h2 : (2 : K) ≠ 0) (S : Finset ℕ) (a : ℕ → K)
    (e : ℕ → A) :
    φ ((∑ n ∈ S, a n • e n) * (∑ n ∈ S, a n • e n)) =
      ∑ m ∈ S, ∑ n ∈ S, a m * a n * symForm φ (e m) (e n) := by
  have h1 : φ ((∑ n ∈ S, a n • e n) * (∑ n ∈ S, a n • e n)) =
      ∑ m ∈ S, ∑ n ∈ S, a m * a n * φ (e m * e n) := by
    simp only [sum_mul, mul_sum, smul_mul_smul_comm, map_sum, map_smul, smul_eq_mul]
    rw [Finset.sum_comm]
  have h2' : (∑ m ∈ S, ∑ n ∈ S, a m * a n * φ (e m * e n)) =
      ∑ m ∈ S, ∑ n ∈ S, a m * a n * φ (e n * e m) := by
    rw [Finset.sum_comm]
    refine sum_congr rfl fun m _ => sum_congr rfl fun n _ => ?_
    ring
  have h3 : (∑ m ∈ S, ∑ n ∈ S, a m * a n * symForm φ (e m) (e n)) =
      ((∑ m ∈ S, ∑ n ∈ S, a m * a n * φ (e m * e n)) +
        ∑ m ∈ S, ∑ n ∈ S, a m * a n * φ (e n * e m)) / 2 := by
    rw [← sum_add_distrib, sum_div]
    refine sum_congr rfl fun m _ => ?_
    rw [← sum_add_distrib, sum_div]
    refine sum_congr rfl fun n _ => ?_
    unfold symForm; ring
  rw [h3, ← h2', h1]; field_simp; ring

/-- **Parseval** for modes orthogonal under the symmetrised form:
    `φ(u²) = ∑ wₙ aₙ²`, with `wₙ = φ(eₙ²)`. -/
theorem parsevalNc (φ : A →ₗ[K] K) (e : ℕ → A)
    (h2 : (2 : K) ≠ 0)
    (horth : ∀ m n, m ≠ n → symForm φ (e m) (e n) = 0) (S : Finset ℕ) (a : ℕ → K) :
    φ ((∑ n ∈ S, a n • e n) * (∑ n ∈ S, a n • e n)) =
      ∑ n ∈ S, φ (e n * e n) * a n ^ 2 := by
  rw [phi_sq_eq_symForm φ h2]
  refine sum_congr rfl fun m _ => ?_
  rw [sum_eq_single m]
  · unfold symForm; field_simp; ring
  · intro n _ hnm; rw [horth m n (Ne.symm hnm)]; ring
  · intro hm; exact absurd ‹m ∈ S› hm

/-- **The Galerkin transfer is the advection**, noncommutative case. The `n`-th
    modal coordinate of `X_v u` against the symmetrised form, with
    `X_v = ∑ₚ aₚ Xₚ` and `u = ∑ᵣ aᵣ eᵣ`, is the transfer of
    `advectionTriadNc`. -/
theorem transfer_eq_advection_nc (φ : A →ₗ[K] K) (e : ℕ → A) (X : ℕ → A →ₗ[K] A)
    (hleib : ∀ p f g, X p (f * g) = X p f * g + f * X p g)
    (hdiv : ∀ p f, φ (X p f) = 0)
    (hw : ∀ n, φ (e n * e n) ≠ 0)
    (hsel : ∀ n p r, ¬ FusionTriad n p r → symForm φ (e n) (X p (e r)) = 0)
    (h2 : (2 : K) ≠ 0) (S : Finset ℕ) (a : ℕ → K) (n : ℕ) :
    symForm φ (e n) ((∑ p ∈ S, a p • X p) (∑ r ∈ S, a r • e r)) / φ (e n * e n) =
      transfer (advectionTriadNc φ e X hleib hdiv hw hsel) S a n := by
  have hB : ∀ g : A, symForm φ (e n) g = (φ (e n * g) + φ (g * e n)) / 2 := fun _ => rfl
  have hlhs : symForm φ (e n) ((∑ p ∈ S, a p • X p) (∑ r ∈ S, a r • e r)) =
      ∑ p ∈ S, ∑ r ∈ S, a p * a r * symForm φ (e n) (X p (e r)) := by
    simp only [hB, LinearMap.sum_apply, LinearMap.smul_apply, map_sum, map_smul,
      mul_sum, sum_mul, mul_smul_comm, smul_mul_assoc, smul_eq_mul]
    conv_rhs => rw [Finset.sum_comm]
    rw [← sum_add_distrib, sum_div]
    refine sum_congr rfl fun p _ => ?_
    rw [← sum_add_distrib, sum_div]
    refine sum_congr rfl fun r _ => ?_
    ring
  have hsym : (∑ p ∈ S, ∑ r ∈ S, modalDnc φ e X n r p * a p * a r) =
      ∑ p ∈ S, ∑ r ∈ S, modalDnc φ e X n p r * a p * a r := by
    rw [Finset.sum_comm]
    refine sum_congr rfl fun p _ => sum_congr rfl fun r _ => ?_
    ring
  have hsplit : (∑ p ∈ S, ∑ r ∈ S,
      (modalDnc φ e X n p r + modalDnc φ e X n r p) / 2 * a p * a r) =
      ((∑ p ∈ S, ∑ r ∈ S, modalDnc φ e X n p r * a p * a r) +
        ∑ p ∈ S, ∑ r ∈ S, modalDnc φ e X n r p * a p * a r) / 2 := by
    rw [← sum_add_distrib, sum_div]
    refine sum_congr rfl fun p _ => ?_
    rw [← sum_add_distrib, sum_div]
    refine sum_congr rfl fun r _ => ?_
    ring
  simp only [transfer, advectionTriadNc, ofTransportSkew]
  rw [hlhs, hsplit, hsym, ← two_mul, mul_div_cancel_left₀ _ h2, sum_div]
  refine sum_congr rfl fun p _ => ?_
  rw [sum_div]
  refine sum_congr rfl fun r _ => ?_
  simp only [modalDnc]
  ring

/-! ### Non-vacuity on a KMS state: inner transport by a modular-fixed element -/

/-- The inner derivation `f ↦ c f − f c`. -/
def innerDer (c : A) : A →ₗ[K] A where
  toFun f := c * f - f * c
  map_add' f g := by noncomm_ring
  map_smul' t f := by simp [mul_sub, sub_mul, mul_smul_comm, smul_mul_assoc, smul_sub]

/-- Inner derivations satisfy the untwisted Leibniz rule in any ring. -/
theorem innerDer_leibniz (c f g : A) :
    innerDer (K := K) c (f * g) = innerDer (K := K) c f * g + f * innerDer (K := K) c g := by
  simp only [innerDer, LinearMap.coe_mk, AddHom.coe_mk]; noncomm_ring

/-- **A KMS state kills inner transport by a modular-fixed element.** If
    `φ(ab) = φ(b σ(a))` (the modular property of the Haar state) and
    `σ c = c`, then `φ(c f − f c) = 0`. So `innerDer c` meets both hypotheses
    `hleib` and `hdiv` of `advectionTriadNc`, for a state that is not a trace. -/
theorem innerDer_div_free_of_kms (φ : A →ₗ[K] K) (σ : A → A)
    (hkms : ∀ a b, φ (a * b) = φ (b * σ a)) (c : A) (hc : σ c = c) (f : A) :
    φ (innerDer (K := K) c f) = 0 := by
  simp only [innerDer, LinearMap.coe_mk, AddHom.coe_mk, map_sub]
  rw [hkms c f, hc, sub_self]

end QOU.FluidDynamics.ModalTriad
