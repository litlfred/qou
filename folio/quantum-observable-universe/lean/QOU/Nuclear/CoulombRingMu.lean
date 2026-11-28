import QOU.Nuclear.CoulombRingLedger

/-!
# A pre-registered EM ring factor `μ` from the photon vertex pair — gap G3

Bean `qou-tcl3`. Audit `docs/audits/2026-11-27-coulomb-ring-mu.md`. Builds on
`QOU.Nuclear.CoulombRingLedger` (any reading `ρ` gives the IMME ledger with `ε = ρ(μ)`) and on
PR #9841 (`QOU.MassTheory.EmVertexPairScalarChain`): the chirality-summed photon vertex pair at
any two generators is the scalar `−h²`, `h = q − q⁻¹`, and each further pair in the
polarisation chain carries one `α`.

## The route

One Coulomb pair is one photon exchanged between two proton blocks, so one vertex pair. The
pre-registered ring factor is therefore `μ₁ = 1 + α·(−h²) = 1 − α h²`. Here `α` is a constant of
the coefficient ring (the corpus-derived `α_EM`, conditional on the unproved CS Gram-ratio identification, bean `qou-wkgp`; the old Witten-κ Gram `sorry` was refuted and removed 2026-11-20); no
value of it enters this file.

## What is proved (generic field, no measured value)

* `mu1_at_one`: `μ₁(1) = 1`. The factor is invisible at `q = 1`, like every γγ bond in the energy
  reading (PR #9793).
* `leibniz_inv`: for a Leibniz map with `D q = 1`, `D q⁻¹ = −q⁻²`.
* `euler_h`: `q·D h = q + q⁻¹ = [2]`.
* `energy_mu1`: `−q·D μ₁ / μ₁ = 2 α h [2] / μ₁`. So the energy-reading pair weight is
  `ε_U = 2αh[2]/(1 − αh²)`, which is `O(α h)` and vanishes at `q = 1`.
* `mirror_A3_mu1`: at `A = 3` the mirror split is exactly this `ε_U`.

## What is not proved

* That one exchange is the whole factor. The ladder `1/(1 + αh²)` differs at `O(α²)`; the
  vertex normalisation `S/2` (`§3b-cond` of #9841) would put `h²/4` in place of `h²`.
* The size dependence. `μ₁` does not depend on `A`. Comparison data (audit only) need
  `ε ∝ A^{−1/3}`, which a contact factor cannot give.
-/

namespace QOU.Nuclear.CoulombRingMu

open QOU.Nuclear.CoulombIsospinChannel QOU.Nuclear.CoulombRingLedger

variable {K : Type*} [Field K]

/-- `h = q − q⁻¹`. -/
def hq (q : K) : K := q - q⁻¹

/-- The one-exchange EM ring factor `μ₁ = 1 − α h²`. -/
def mu1 (α q : K) : K := 1 - α * hq q ^ 2

/-- **`μ₁(1) = 1`.** -/
theorem mu1_at_one (α : K) : mu1 α (1 : K) = 1 := by
  simp [mu1, hq]

/-- For a Leibniz map with `D q = 1` and `q ≠ 0`, `D q⁻¹ = −q⁻²`. -/
theorem leibniz_inv (D : K → K) (hD : ∀ x y, D (x * y) = x * D y + y * D x) (q : K)
    (hq0 : q ≠ 0) (hDq : D q = 1) : D q⁻¹ = -(q⁻¹) ^ 2 := by
  have h1 : D 1 = 0 := by
    have h := hD 1 1
    simp only [mul_one, one_mul] at h
    linear_combination -h
  have h := hD q q⁻¹
  rw [mul_inv_cancel₀ hq0, h1, hDq] at h
  have : q * D q⁻¹ = -q⁻¹ := by linear_combination -h
  have e : D q⁻¹ = q⁻¹ * (q * D q⁻¹) := by field_simp
  rw [e, this]
  ring

/-- **`q·D h = [2]`.** Needs additivity of `D` on the difference. -/
theorem euler_h (D : K → K) (hD : ∀ x y, D (x * y) = x * D y + y * D x)
    (hsub : ∀ x y, D (x - y) = D x - D y) (q : K) (hq0 : q ≠ 0) (hDq : D q = 1) :
    q * D (hq q) = q + q⁻¹ := by
  unfold hq
  rw [hsub, hDq, leibniz_inv D hD q hq0 hDq]
  field_simp
  ring

/-- **Energy reading of `μ₁`.** If `D` is Leibniz, additive, kills the constant `α`, and
`D q = 1`, then `−q·D μ₁ / μ₁ = 2 α h [2] / μ₁`. -/
theorem energy_mu1 (D : K → K) (hD : ∀ x y, D (x * y) = x * D y + y * D x)
    (hsub : ∀ x y, D (x - y) = D x - D y) (α q : K) (hq0 : q ≠ 0) (hDq : D q = 1)
    (hα : D α = 0) :
    -q * logDer D (mu1 α q) = 2 * α * hq q * (q + q⁻¹) / mu1 α q := by
  have h1 : D 1 = 0 := by
    have h := hD 1 1
    simp only [mul_one, one_mul] at h
    linear_combination -h
  have hsq : D (hq q ^ 2) = 2 * hq q * D (hq q) := by
    rw [pow_two, hD]; ring
  have hDmu : D (mu1 α q) = -(α * (2 * hq q * D (hq q))) := by
    unfold mu1
    rw [hsub, h1, hD, hsq, hα]
    ring
  have he := euler_h D hD hsub q hq0 hDq
  unfold logDer
  rw [hDmu]
  have : -q * (-(α * (2 * hq q * D (hq q)))) = 2 * α * hq q * (q * D (hq q)) := by ring
  rw [div_eq_mul_inv, ← mul_assoc, this, he, ← div_eq_mul_inv]

/-- **Mirror split at `A = 3` is one pair weight.** For any reading `ρ` of `μ`,
`E(½) − E(−½) = ρ(μ)` at `A = 3`. -/
theorem mirror_A3_mu1 [CharZero K] {M : Type*} [CommMonoid M] (ρ : Reading M K) (μ : M) :
    imme (ρ.toFun μ * emA 3) (ρ.toFun μ * emB 3) (ρ.toFun μ * emC) (1 / 2)
      - imme (ρ.toFun μ * emA 3) (ρ.toFun μ * emB 3) (ρ.toFun μ * emC) (-(1 / 2))
      = ρ.toFun μ :=
  emEnergy_mirror_A3 _

end QOU.Nuclear.CoulombRingMu
