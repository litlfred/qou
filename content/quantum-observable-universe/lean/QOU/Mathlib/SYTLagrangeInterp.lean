import Mathlib.Algebra.BigOperators.Field
import QOU.Mathlib.SYTVandermondeKeystone

/-!
# QOU.Mathlib.SYTLagrangeInterp — the divided-difference leading-coefficient keystone for β-Lagrange

The Greene–Nijenhuis–Wilf hook-summation identity (`SYTHookGNW.gnwHookIdentity`) reduces, in β-number
coordinates, to a self-contained `ℚ` partial-fractions identity (the **β-Lagrange identity**).  Its
crux is the **divided-difference leading-coefficient identity**: for distinct nodes `β₀,…,β_{k−1}` and
the divided-difference weights `D i = ∏_{j≠i}(βᵢ − βⱼ)`,

    ∑ᵢ f(βᵢ) / Dᵢ = [Xᵏ⁻¹] f      whenever  deg f < k.

This used to be hand-rolled from `Polynomial.Roots` (Lagrange interpolation).  Per the owner directive
(2026-06-29) it is now a **thin wrapper over the determinant keystone**
`QOU.Mathlib.SYTVandermonde.interp_leadingCoeff` (PR #3079) — exact `det_vandermonde` algebra rather
than interpolation (no conditioning baggage over `ℚ`/`ℝ`).  The keystone is stated over `Fin (k+1)`
(`deg f ≤ k`, leading coefficient `f.coeff k`); the wrapper specialises it at `k ↦ k−1` using `0 < k`.
The local `vWeight` is definitionally the keystone's `vWeight` (same `∏_{j≠i}(βᵢ − βⱼ)`), so the bridge
is a one-step unfolding.

Pure `ℚ` determinant algebra; nothing archimedean; no interpolation; no fit.
-/

namespace QOU.Mathlib.SYTBetaLagrange

open Polynomial Finset

variable {k : ℕ}

/-- The divided-difference / Vandermonde weight `Dᵢ = ∏_{j≠i}(βᵢ − βⱼ)` (definitionally the keystone's
`QOU.Mathlib.SYTVandermonde.vWeight`). -/
noncomputable def vWeight (β : Fin k → ℚ) (i : Fin k) : ℚ :=
  ∏ j ∈ univ.erase i, (β i - β j)

/-- For injective nodes, every weight `Dᵢ` is nonzero (each factor `βᵢ − βⱼ ≠ 0`, `j ≠ i`). -/
theorem vWeight_ne_zero (β : Fin k → ℚ) (hβ : Function.Injective β) (i : Fin k) :
    vWeight β i ≠ 0 := by
  unfold vWeight
  rw [Finset.prod_ne_zero_iff]
  intro j hj
  rw [Finset.mem_erase] at hj
  exact sub_ne_zero.mpr (fun h => hj.1 (hβ h).symm)

/-- **Divided-difference leading-coefficient keystone.** For distinct nodes and any `f` with
`deg f < k`,

    ∑ᵢ f(βᵢ) / Dᵢ = [Xᵏ⁻¹] f.

A thin specialisation of the determinant keystone `QOU.Mathlib.SYTVandermonde.interp_leadingCoeff`
(proved by Laplace-expanding `Matrix.det_vandermonde`, PR #3079) at `k ↦ k−1`; the `0 < k` hypothesis
provides `(k−1)+1 = k`, and the two `vWeight` definitions coincide. -/
theorem interp_leadingCoeff (β : Fin k → ℚ) (hβ : Function.Injective β) (hk : 0 < k)
    (f : ℚ[X]) (hf : f.natDegree < k) :
    ∑ i, f.eval (β i) / vWeight β i = f.coeff (k - 1) := by
  obtain ⟨m, rfl⟩ := Nat.exists_eq_succ_of_ne_zero hk.ne'
  have hkey := QOU.Mathlib.SYTVandermonde.interp_leadingCoeff β hβ f (by omega)
  simpa [vWeight, QOU.Mathlib.SYTVandermonde.vWeight, Nat.succ_sub_one] using hkey

end QOU.Mathlib.SYTBetaLagrange
