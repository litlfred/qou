import Mathlib.NumberTheory.Zsqrtd.GaussianInt
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.Order.Archimedean.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
# Do regularity conditions fix the q-NS viscosity? (bean `qou-gd5s`)

Ref: [bredberg2011] Bredberg–Keeler–Lysov–Strominger, arXiv:1101.2451, §4 (pp. 5–7):
in their setting, smoothness of the dual geometry at the cutoff forces the
viscosity `η = r_c`. [bhattacharyya2008] arXiv:0712.2456 §4.5: horizon regularity
fixes `η/s = 1/4π`. [habiro2004] Habiro, *Cyclotomic completions of polynomial
rings*: an element of the Habiro ring evaluates at a primitive `n`-th root of
unity `ζ` into `ℤ[ζ]`.

The QOU question (owner, 2026-11-25: *"can we generalize and make use?"*): does a
regularity or convergence condition on the q-step force
`ν_q = ½(1 − q⁻¹)`? Three candidate conditions are tested. They were **not**
chosen because they give `ℏ_q/2` (anti-fit), and none of them does.

1. **Positivity of dissipation.** `DEC.Complex2.energy_nonincreasing`
   (`DECNavierStokes.lean`) holds for every `ν ≥ 0`. This condition is a
   half-line, so it leaves `ν` free. No new lemma is needed.
2. **Stability of the explicit q-step on the full ladder.** A mode with
   eigenvalue `λ ≥ 0` under the explicit step `v ↦ (1 − δνλ) v` is non-expansive
   iff `δνλ ≤ 2` (`explicit_mode_stable_iff`). On the q-ladder the eigenvalues
   `[k]_q²` are unbounded, so stability of **every** rung with a fixed step
   `δ > 0` forces `ν = 0` (`nu_eq_zero_of_stable_on_unbounded_ladder`). That
   condition selects a value, but the value is `0` (Euler), not `ℏ_q/2`. An
   implicit step is unconditionally stable and leaves `ν` free.
3. **Habiro integrality.** At the primitive 4th root of unity `q = i`,
   `ν_q = (1 + i)/2`, and `2z ≠ 1 + i` for every Gaussian integer `z`
   (`two_mul_ne_one_add_I`). So, *given* Habiro's evaluation property (cited,
   not proved here), `ν_q` is **not** in the Habiro ring, whereas `ℏ_q = 1 − q⁻¹`
   is (it is a Laurent polynomial over `ℤ` in the unit `q`). A Habiro-integrality
   condition would therefore exclude the factor `½`.

Net: of the three conditions, none forces `ν_q = ℏ_q/2`. One leaves `ν` free,
one forces `ν = 0`, and one excludes the corpus value. Scope (a) for each: these
three conditions alone do not fix `ν_q`. That is not a claim that no condition does.
-/

namespace QOU.FluidDynamics.ViscosityRoutes

section Ordered

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Explicit q-step on one mode: `|1 − δνλ| ≤ 1 ↔ δνλ ≤ 2` when `δνλ ≥ 0`. -/
theorem explicit_mode_stable_iff (δ ν lam : K) (h : 0 ≤ δ * ν * lam) :
    |1 - δ * ν * lam| ≤ 1 ↔ δ * ν * lam ≤ 2 := by
  rw [abs_le]
  constructor
  · rintro ⟨h1, -⟩; linarith
  · intro h2; constructor <;> linarith

/-- Stability of the explicit step on every rung of an **unbounded** ladder of
nonnegative eigenvalues, with a fixed step `δ > 0` and `ν ≥ 0`, forces `ν = 0`. -/
theorem nu_eq_zero_of_stable_on_unbounded_ladder [Archimedean K]
    (δ ν : K) (hδ : 0 < δ) (hν : 0 ≤ ν) (lam : ℕ → K) (hlam : ∀ k, 0 ≤ lam k)
    (hunb : ∀ M : K, ∃ k, M < lam k)
    (hstab : ∀ k, |1 - δ * ν * lam k| ≤ 1) : ν = 0 := by
  by_contra hne
  have hνpos : 0 < ν := lt_of_le_of_ne hν (Ne.symm hne)
  obtain ⟨k, hk⟩ := hunb (2 / (δ * ν))
  have hdn : 0 < δ * ν := mul_pos hδ hνpos
  have hle := (explicit_mode_stable_iff δ ν (lam k)
    (mul_nonneg hdn.le (hlam k))).1 (hstab k)
  have : 2 < δ * ν * lam k := by
    rw [div_lt_iff₀ hdn] at hk; linarith
  linarith

end Ordered

/-- At `q = i`, `ν_q = (1 − i⁻¹)/2 = (1 + i)/2`, and `1 + i` is not twice a
Gaussian integer. With Habiro's evaluation property this excludes `ν_q` from
the Habiro ring. -/
theorem two_mul_ne_one_add_I (z : GaussianInt) : 2 * z ≠ ⟨1, 1⟩ := by
  intro h
  have hre := congrArg Zsqrtd.re h
  simp at hre
  omega

end QOU.FluidDynamics.ViscosityRoutes
