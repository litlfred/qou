import QOU.FluidDynamics.DECNavierStokes
import Mathlib.Analysis.Calculus.Deriv.MeanValue
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.Calculus.Deriv.Mul

/-!
# QOU.FluidDynamics.q_ns_dec_refinement

The DEC model of the q-NS system (`DECNavierStokes`, PR #9434) as the mesh is
refined, `N → ∞`, for Part A of `conj:regularity-breakdown` (bean `qou-pa7n`,
owner request 2026-11-27: "the DEC to infinity").

## The question

On a fixed finite 2-complex the enstrophy is at most `λ_max(Δ₁) · E(0)`, so
Part A fails at every fixed resolution. `λ_max` grows under refinement, so a
fixed-resolution bound says nothing about `N → ∞`.

## The answer for the existing (2-complex) model

The DEC model lives on a **2-complex**: vorticity is a 2-cochain, a scalar per
face. In two dimensions there is no vortex stretching. When the advection
transports vorticity without creating enstrophy (`⟨ω, d₁ B⟩ = 0`, named
hypothesis `hens`), the enstrophy is nonincreasing:

* `enstrophy_equality_of_enstrophy_skew`: `⟨ω, ω̇⟩ = −ν |d₁ᵀ ω|²`;
* `GalerkinTraj.enstrophy_le_initial`: `Ω(t) ≤ Ω(0)` for every `t ≥ 0`.

Neither depends on the complex, its size `N`, or `q` (through `ν = ν_q ≥ 0`,
Euler included). So **no refinement of a 2-complex model can carry Part A**:
the bound holds at every resolution, and with data fixed in the substrate
layer `Ω(0)` does not depend on `q`. This is a (b) structural exclusion, and
the invariant is enstrophy skewness.

What Part A needs is a **3-complex** (vorticity a 2-form on a 3-manifold, with
the stretching term `ω · ∇v`). No DEC 3-complex q-NS model exists in the corpus.

## Scope and hypotheses

* `hens` is the discrete form of the continuum 2D identity
  `∫ ω (u · ∇ω) = 0` for divergence-free `u`. It is a hypothesis on the
  discretisation of `B`, stated in every lemma that uses it. It is not
  derived for any particular scheme here.
* Non-vacuity: `gradient_advection_skew` shows that a nonzero advection
  (a gradient field) satisfies both `⟨v, B⟩ = 0` and `hens`.

No empirical value enters any proof. Owner rule 2026-11-27: only QOU-formalised
work.

## References

- [leitner2026] fluid-dynamics/regularity-breakdown.md (`conj:regularity-breakdown`)
- [mohamed2016dec] Mohamed–Hirani–Samtaney, arXiv:1508.01166, §3.3
-/

namespace QOU.FluidDynamics.DEC

open Matrix Finset

namespace Complex2

section Algebraic

variable {R : Type*} [CommRing R]
variable {V E F : Type*} [Fintype V] [Fintype E] [Fintype F]
variable (C : Complex2 R V E F)

/-- **Enstrophy equality** for the full semi-discrete system, given an
    enstrophy-skew advection `⟨ω, d₁ B⟩ = 0` (two-dimensional transport):
    `⟨ω, ω̇⟩ = −ν |d₁ᵀ ω|²`. -/
theorem enstrophy_equality_of_enstrophy_skew (v vdot B : E → R) (p : V → R) (ν : R)
    (hNS : vdot = -B - C.d0 *ᵥ p - ν • (C.lap1 *ᵥ v))
    (hens : C.vort v ⬝ᵥ C.vort B = 0) :
    C.vort v ⬝ᵥ C.vort vdot = -ν * ((C.d1ᵀ *ᵥ C.vort v) ⬝ᵥ (C.d1ᵀ *ᵥ C.vort v)) := by
  rw [C.vorticity_equation v vdot B p ν hNS, dotProduct_sub, dotProduct_neg, hens,
    dotProduct_smul, C.lap2_form, smul_eq_mul]
  ring

/-- **Non-vacuity of the skew hypotheses.** A gradient advection `B = d₀ φ`
    does no work on a divergence-free velocity and creates no vorticity. -/
theorem gradient_advection_skew (v : E → R) (φ : V → R) (hinc : C.divg v = 0) :
    v ⬝ᵥ (C.d0 *ᵥ φ) = 0 ∧ C.vort v ⬝ᵥ C.vort (C.d0 *ᵥ φ) = 0 := by
  refine ⟨C.pressure_orth_of_divFree v φ hinc, ?_⟩
  simp [vort, mulVec_mulVec, C.dd]

end Algebraic

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
variable {V E F : Type*} [Fintype V] [Fintype E] [Fintype F]
variable (C : Complex2 K V E F)

/-- Enstrophy is nonincreasing pointwise for `ν ≥ 0`. -/
theorem enstrophy_nonincreasing_of_enstrophy_skew (v vdot B : E → K) (p : V → K)
    (ν : K) (hν : 0 ≤ ν)
    (hNS : vdot = -B - C.d0 *ᵥ p - ν • (C.lap1 *ᵥ v))
    (hens : C.vort v ⬝ᵥ C.vort B = 0) :
    C.vort v ⬝ᵥ C.vort vdot ≤ 0 := by
  rw [C.enstrophy_equality_of_enstrophy_skew v vdot B p ν hNS hens]
  have := dotProduct_self_nonneg' (C.d1ᵀ *ᵥ C.vort v)
  nlinarith

end Ordered

end Complex2

/-! ### Trajectories over `ℝ` -/

variable {V E F : Type*} [Fintype V] [Fintype E] [Fintype F]

/-- A trajectory of the semi-discrete q-NS system on a 2-complex, with an
    enstrophy-skew advection at every time. -/
structure GalerkinTraj (C : Complex2 ℝ V E F) (ν : ℝ) where
  /-- Velocity 1-cochain. -/
  v : ℝ → E → ℝ
  /-- Its time derivative. -/
  vdot : ℝ → E → ℝ
  /-- Advection. -/
  B : ℝ → E → ℝ
  /-- Pressure. -/
  p : ℝ → V → ℝ
  /-- Componentwise time derivative. -/
  hderiv : ∀ e t, HasDerivAt (fun s => v s e) (vdot t e) t
  /-- The semi-discrete q-NS equation. -/
  hNS : ∀ t, vdot t = -B t - C.d0 *ᵥ p t - ν • (C.lap1 *ᵥ v t)
  /-- Two-dimensional transport: the advection creates no enstrophy. -/
  hens : ∀ t, C.vort (v t) ⬝ᵥ C.vort (B t) = 0

namespace GalerkinTraj

variable {C : Complex2 ℝ V E F} {ν : ℝ}

/-- The enstrophy `Ω(t) = |d₁ v(t)|²`. -/
def enstrophy (tr : GalerkinTraj C ν) (t : ℝ) : ℝ :=
  C.vort (tr.v t) ⬝ᵥ C.vort (tr.v t)

/-- `dΩ/dt = 2 ⟨ω, d₁ v̇⟩`. -/
theorem enstrophy_hasDerivAt (tr : GalerkinTraj C ν) (t : ℝ) :
    HasDerivAt tr.enstrophy (2 * (C.vort (tr.v t) ⬝ᵥ C.vort (tr.vdot t))) t := by
  -- each vorticity component is a fixed linear combination of the components of `v`
  have hω : ∀ f, HasDerivAt (fun s => C.vort (tr.v s) f) (C.vort (tr.vdot t) f) t := by
    intro f
    simp only [Complex2.vort, mulVec, dotProduct]
    exact HasDerivAt.fun_sum (fun e _ => (tr.hderiv e t).const_mul (C.d1 f e))
  have h := HasDerivAt.fun_sum (u := (univ : Finset F)) (fun f _ => (hω f).mul (hω f))
  have hfun : tr.enstrophy = fun s => ∑ f ∈ univ, C.vort (tr.v s) f * C.vort (tr.v s) f := by
    funext s; rfl
  rw [hfun]
  refine h.congr_deriv ?_
  simp only [dotProduct, mul_sum]
  refine sum_congr rfl fun f _ => ?_
  ring

/-- **Enstrophy never exceeds its initial value**, on every 2-complex, at
    every resolution, for every `ν ≥ 0`. -/
theorem enstrophy_le_initial (tr : GalerkinTraj C ν) (hν : 0 ≤ ν) {t : ℝ}
    (ht : 0 ≤ t) : tr.enstrophy t ≤ tr.enstrophy 0 := by
  have hanti : Antitone tr.enstrophy := by
    refine antitone_of_deriv_nonpos
      (fun s => (tr.enstrophy_hasDerivAt s).differentiableAt) ?_
    intro s
    rw [(tr.enstrophy_hasDerivAt s).deriv]
    have := C.enstrophy_nonincreasing_of_enstrophy_skew (tr.v s) (tr.vdot s) (tr.B s)
      (tr.p s) ν hν (tr.hNS s) (tr.hens s)
    linarith
  exact hanti ht

end GalerkinTraj

/-- **Part A fails on every 2-complex DEC model, at every resolution.**
    For any family of q-dependent viscosities `ν q ≥ 0` (with `ν_q = ½(1 − q⁻¹)`
    the case of interest) and any trajectories with the same initial
    enstrophy, `sup_t Ω` is bounded by that initial enstrophy, uniformly in `q`
    and in the complex. -/
theorem partA_fails_dec2d (C : Complex2 ℝ V E F) (ν : ℝ → ℝ)
    (hν : ∀ q, 1 < q → 0 ≤ ν q) (tr : ∀ q, GalerkinTraj C (ν q)) (Ω₀ : ℝ)
    (h0 : ∀ q, (tr q).enstrophy 0 = Ω₀) :
    ∀ q, 1 < q → ∀ t, 0 ≤ t → (tr q).enstrophy t ≤ Ω₀ := by
  intro q hq t ht
  rw [← h0 q]
  exact (tr q).enstrophy_le_initial (hν q hq) ht

/-- The corpus viscosity `ν_q = ½(1 − q⁻¹)` is nonnegative on `q > 1`. -/
theorem nuQ_nonneg {q : ℝ} (hq : 1 < q) : 0 ≤ nuQ q := by
  have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  unfold nuQ; linarith

end QOU.FluidDynamics.DEC
