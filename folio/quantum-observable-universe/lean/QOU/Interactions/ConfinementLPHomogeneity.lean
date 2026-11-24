import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import QOU.MathlibInfra.ConfinementLayerTower

/-!
# Confinement-LP Homogeneity and the Converse Shadow-Price Criterion (`qou-ndsa`)

Upgraded Mathlib/QOU formalization of the `qou-ndsa` LP homogeneity and radical-pairing
theorems (salvaged and generalized from PR `#8154` over generic `[CommRing K]` / `[IsDomain K]`
in accordance with AGENTS.md §7c).

## Mathematical Summary

For the operator-selection LP (`min t · x` subject to `𝟙 · x = n_target`, `G x ≥ 0`)
on `m` basis coordinates `Fin m → K`:

1. **Primal Cone Homogeneity under `n_target` Scaling (`netSum_smul`, `lpDot_smul_right`,
   `gramRow_nonneg_smul`):**
   Scaling any primal vector `x : Fin m → K` by `k ≥ 0` scales the net sum
   `netSum (k • x) = k * netSum x`, scales any linear objective or Gram row
   `lpDot a (k • x) = k * lpDot a x`, and preserves cone non-negativity `0 ≤ lpDot Gi (k • x)`.
   Thus letting the braid word enter *only* `n_target` scales `x*` homogeneously without
   changing the normalized operator profile.

2. **Exact Radical Pairing & Converse Non-Degeneracy (`radical_pairing_eq_shadow_price_mul_net`,
   `radical_pairing_ne_zero_of_shadow_price_ne_zero`, `shadow_price_unique_of_radical`):**
   For any dual-feasible cost decomposition `t j = y₀ + c j` whose constraint contribution `c`
   is orthogonal to a radical vector `v` (`lpDot c v = 0`), pairing `t` with `v` gives the
   exact identity `lpDot t v = y₀ * netSum v`.
   Consequently, over any integral domain `K`:
   * If `lpDot t v = 0` and `netSum v ≠ 0`, then `y₀ = 0` (excluding `G^w` and moment-SDP lifts).
   * Achieving a non-zero shadow price `y₀ ≠ 0` when `netSum v ≠ 0` **requires**
     `lpDot t v ≠ 0` — the objective `t(β)` must pair non-trivially with the radical direction `v`.

-- Ref: [leitner2026] bean qou-ndsa; QOU/ParticleInteractions/operator_selection_lp.lean;
-- computations/confinement_lp_braid_gram_probe.py
-/

namespace QOU.Interactions.ConfinementLPHomogeneity

open scoped BigOperators

section CommRing

variable {m : ℕ} {K : Type*} [CommRing K]

/-- Standard bilinear dot product `∑ j : Fin m, a j * b j` over `[CommRing K]`. -/
def lpDot (a b : Fin m → K) : K :=
  ∑ j : Fin m, a j * b j

/-- Net sum `∑ j : Fin m, x j = ⟨𝟙, x⟩` over `[CommRing K]`. -/
def netSum (x : Fin m → K) : K :=
  ∑ j : Fin m, x j

/-- Compatibility with `ConfinementLayerTower.configCost`: for integer vectors `z : Fin m → ℤ`,
`lpDot (fun j => (z j : K)) c` agrees definitionally with `ConfinementLayerTower.configCost c z`. -/
theorem lpDot_intCast_eq_configCost (c : Fin m → K) (z : Fin m → ℤ) :
    lpDot (fun j => (z j : K)) c = QOU.MathlibInfra.ConfinementLayerTower.configCost c z :=
  rfl

/-- **Homogeneity of the net sum under scalar multiplication:**
`netSum (k • x) = k * netSum x`. -/
theorem netSum_smul (k : K) (x : Fin m → K) :
    netSum (k • x) = k * netSum x := by
  simp only [netSum, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]

/-- **Homogeneity of any linear pairing (objective or Gram row) under right scaling:**
`lpDot a (k • x) = k * lpDot a x`. -/
theorem lpDot_smul_right (k : K) (a x : Fin m → K) :
    lpDot a (k • x) = k * lpDot a x := by
  simp only [lpDot, Pi.smul_apply, smul_eq_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl ?_
  intro j _
  ring

/-- Dual decomposition identity along a vector `v`: if `t j = y₀ + c j` for all `j : Fin m`,
then `⟨t, v⟩ = y₀ * ⟨𝟙, v⟩ + ⟨c, v⟩`. -/
theorem lpDot_dual_decomp (t c v : Fin m → K) (y₀ : K)
    (hdual : ∀ j : Fin m, t j = y₀ + c j) :
    lpDot t v = y₀ * netSum v + lpDot c v := by
  simp only [lpDot, netSum, hdual, add_mul, Finset.sum_add_distrib, Finset.mul_sum]

/-- **Exact Radical Pairing Identity (`qou-ndsa`):**
Whenever the constraint contribution `c` is orthogonal to a radical direction `v`
(`lpDot c v = 0`), any dual-feasible cost vector `t j = y₀ + c j` satisfies
`lpDot t v = y₀ * netSum v`. -/
theorem radical_pairing_eq_shadow_price_mul_net (t c v : Fin m → K) (y₀ : K)
    (hdual : ∀ j : Fin m, t j = y₀ + c j)
    (hcv : lpDot c v = 0) :
    lpDot t v = y₀ * netSum v := by
  rw [lpDot_dual_decomp t c v y₀ hdual, hcv, add_zero]

end CommRing

section OrderedAndDomain

/-- **Cone preservation under non-negative scaling (`0 ≤ k`):**
If a Gram row pairing `lpDot Gi x` is non-negative, then so is `lpDot Gi (k • x)`. -/
theorem gramRow_nonneg_smul {m : ℕ} {K : Type*}
    [CommRing K] [LinearOrder K] [IsStrictOrderedRing K]
    {k : K} (hk : 0 ≤ k) (Gi x : Fin m → K) (hGx : 0 ≤ lpDot Gi x) :
    0 ≤ lpDot Gi (k • x) := by
  rw [lpDot_smul_right]
  exact mul_nonneg hk hGx

/-- **Converse Non-Degeneracy Theorem (`qou-ndsa`):**
Over any commutative domain `K`, if the constraint contribution annihilates the radical
(`lpDot c v = 0`), then achieving a non-zero shadow price (`y₀ ≠ 0`) on a radical direction
with `netSum v ≠ 0` **requires** `lpDot t v ≠ 0`. -/
theorem radical_pairing_ne_zero_of_shadow_price_ne_zero {m : ℕ} {K : Type*}
    [CommRing K] [NoZeroDivisors K]
    (t c v : Fin m → K) (y₀ : K)
    (hdual : ∀ j : Fin m, t j = y₀ + c j)
    (hcv : lpDot c v = 0)
    (hone : netSum v ≠ 0)
    (hy₀ : y₀ ≠ 0) :
    lpDot t v ≠ 0 := by
  rw [radical_pairing_eq_shadow_price_mul_net t c v y₀ hdual hcv]
  exact mul_ne_zero hy₀ hone

/-- **Forced Zero Shadow Price under Radical-Orthogonal Cost (`qou-ndsa`):**
Over any commutative domain `K`, if both the constraint contribution `c` and the cost vector `t`
are orthogonal to `v` (`lpDot c v = 0` and `lpDot t v = 0`) while `netSum v ≠ 0`, then `y₀ = 0`. -/
theorem shadow_price_eq_zero_of_radical_orthogonal {m : ℕ} {K : Type*}
    [CommRing K] [NoZeroDivisors K]
    (t c v : Fin m → K) (y₀ : K)
    (hdual : ∀ j : Fin m, t j = y₀ + c j)
    (hcv : lpDot c v = 0)
    (htv : lpDot t v = 0)
    (hone : netSum v ≠ 0) :
    y₀ = 0 := by
  have heq := radical_pairing_eq_shadow_price_mul_net t c v y₀ hdual hcv
  rw [htv] at heq
  exact (mul_eq_zero.mp heq.symm).resolve_right hone

/-- **Shadow-Price Uniqueness from the Radical Pairing (`qou-ndsa`):**
Over any commutative domain `K`, when `lpDot c₁ v = 0` and `lpDot c₂ v = 0` on a radical
direction with `netSum v ≠ 0`, any two dual certificates `(y₁, c₁)` and `(y₂, c₂)` for the
same cost vector `t` satisfy `y₁ = y₂`. -/
theorem shadow_price_unique_of_radical {m : ℕ} {K : Type*}
    [CommRing K] [IsDomain K]
    (t c₁ c₂ v : Fin m → K) (y₁ y₂ : K)
    (hdual₁ : ∀ j : Fin m, t j = y₁ + c₁ j)
    (hdual₂ : ∀ j : Fin m, t j = y₂ + c₂ j)
    (hcv₁ : lpDot c₁ v = 0)
    (hcv₂ : lpDot c₂ v = 0)
    (hone : netSum v ≠ 0) :
    y₁ = y₂ := by
  have h1 := radical_pairing_eq_shadow_price_mul_net t c₁ v y₁ hdual₁ hcv₁
  have h2 := radical_pairing_eq_shadow_price_mul_net t c₂ v y₂ hdual₂ hcv₂
  exact mul_right_cancel₀ hone (h1.symm.trans h2)

end OrderedAndDomain

end QOU.Interactions.ConfinementLPHomogeneity
