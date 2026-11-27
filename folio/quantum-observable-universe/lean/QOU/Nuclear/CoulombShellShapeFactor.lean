import Mathlib.Algebra.BigOperators.Field
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-!
# Coulomb shape factor of concentric charged shells is scale-free

Bean `qou-usft` (shape half). A charge density on a Jackson lattice is a finite sum of
concentric spherical shells: shell `i` has charge `P i` and radius `r i > 0`. Exact 3-D
electrostatics (Newton's shell theorem) gives its self-energy

    E(P, r) = ½ · Σᵢ Σⱼ P i · P j / max (r i) (r j),

and its second moment `M₂(P, r) = Σᵢ P i · r i²`, total charge `Q(P) = Σᵢ P i`. The shape factor
`f` of `E_C = f · Q² / r_rms`, with `r_rms² = M₂ / Q`, satisfies

    f² = E² · M₂ / Q⁵.

This file proves the structural facts the probe
`computations/probes/coulomb_shape_factor_qbessel_probe.py` relies on:

1. `shellEnergy_dilate`: `E(P, λ·r) = E(P, r) / λ` for `λ > 0` — the energy carries a length.
2. `shellMoment_dilate`: `M₂(P, λ·r) = λ² · M₂(P, r)`.
3. `shapeFactorSq_dilate`: `f²` is invariant under every dilation. So a `q^ℤ`-dilation symmetry
   (E_q(2)) leaves `f` fixed while fixing no radius.
4. `shapeFactorSq_charge_scale`: `f²` is invariant under rescaling the charges, so the
   normalisation of a q-Hankel state does not enter `f`.
5. `shapeFactorSq_lattice_shift`: on the lattice `r k = p ^ k`, the shifted radii
   `p ^ (k + n)` give the same `f²`. This is the precise form of "every dilate
   `J_ν(p^n x; p²)` of the q-Hankel state has the same `f`".
6. `shapeFactorSq_single_shell`: one shell has `f² = 1/4` — a non-vacuity check that the
   definition is not identically constant.

What is NOT proved here: the q-Hankel orthogonality that makes the state normalisable, and the
numerical value `f = 0.520011` at `q₀`. Both are analytic; the first is cited
(Koelink–Swarttouw), the second is computed by the probe.

Base ring: a linearly ordered field (the `max` in the shell kernel needs the order, §7c).
-- Ref: [koelink-swarttouw-1994] https://doi.org/10.1006/jmaa.1994.1330
-/

namespace QOU.Nuclear.CoulombShell

open scoped BigOperators

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
variable {ι : Type*}

/-- Self-energy of concentric charged shells, `½ Σᵢ Σⱼ Pᵢ Pⱼ / max rᵢ rⱼ`. -/
def shellEnergy (s : Finset ι) (P r : ι → K) : K :=
  (1 / 2) * ∑ i ∈ s, ∑ j ∈ s, P i * P j / max (r i) (r j)

/-- Second moment `Σᵢ Pᵢ rᵢ²` (charge times `r_rms²`). -/
def shellMoment (s : Finset ι) (P r : ι → K) : K :=
  ∑ i ∈ s, P i * r i ^ 2

/-- Total charge `Σᵢ Pᵢ`. -/
def shellCharge (s : Finset ι) (P : ι → K) : K :=
  ∑ i ∈ s, P i

/-- Square of the shape factor `f = E · r_rms / Q²`, written without a square root:
`f² = E² · M₂ / Q⁵`. -/
def shapeFactorSq (s : Finset ι) (P r : ι → K) : K :=
  shellEnergy s P r ^ 2 * shellMoment s P r / shellCharge s P ^ 5

theorem shellEnergy_dilate (s : Finset ι) (P r : ι → K) {l : K} (hl : 0 < l) :
    shellEnergy s P (fun i => l * r i) = shellEnergy s P r / l := by
  unfold shellEnergy
  have hl0 : l ≠ 0 := hl.ne'
  have key : ∀ i j, P i * P j / max (l * r i) (l * r j) = (P i * P j / max (r i) (r j)) / l := by
    intro i j
    rw [← mul_max_of_nonneg _ _ hl.le, div_div, mul_comm (max (r i) (r j)) l]
  simp_rw [key, ← Finset.sum_div]
  ring

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem shellMoment_dilate (s : Finset ι) (P r : ι → K) (l : K) :
    shellMoment s P (fun i => l * r i) = l ^ 2 * shellMoment s P r := by
  unfold shellMoment
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl fun i _ => ?_
  ring

theorem shapeFactorSq_dilate (s : Finset ι) (P r : ι → K) {l : K} (hl : 0 < l) :
    shapeFactorSq s P (fun i => l * r i) = shapeFactorSq s P r := by
  unfold shapeFactorSq
  rw [shellEnergy_dilate s P r hl, shellMoment_dilate]
  have hl0 : l ≠ 0 := hl.ne'
  rw [div_pow]
  by_cases hQ : shellCharge s P ^ 5 = 0
  · simp [hQ]
  · field_simp

theorem shapeFactorSq_charge_scale (s : Finset ι) (P r : ι → K) {c : K} (hc : c ≠ 0) :
    shapeFactorSq s (fun i => c * P i) r = shapeFactorSq s P r := by
  unfold shapeFactorSq shellEnergy shellMoment shellCharge
  have e1 : ∀ i j, c * P i * (c * P j) / max (r i) (r j) = c ^ 2 * (P i * P j / max (r i) (r j)) := by
    intro i j; ring
  have e2 : ∀ i, c * P i * r i ^ 2 = c * (P i * r i ^ 2) := by intro i; ring
  simp_rw [e1, e2, ← Finset.mul_sum]
  by_cases hQ : (∑ i ∈ s, P i) = 0
  · simp [hQ]
  · field_simp

/-- On the Jackson lattice `r k = p ^ k`, shifting every radius by `p ^ n` (the `n`-th dilate
of the state) leaves `f²` unchanged. -/
theorem shapeFactorSq_lattice_shift (s : Finset ℤ) (P : ℤ → K) {p : K} (hp : 0 < p) (n : ℤ) :
    shapeFactorSq s P (fun k => p ^ (k + n)) = shapeFactorSq s P (fun k => p ^ k) := by
  have h : (fun k : ℤ => p ^ (k + n)) = fun k => p ^ n * p ^ k := by
    funext k; rw [zpow_add₀ hp.ne', mul_comm]
  rw [h]
  exact shapeFactorSq_dilate s P (fun k => p ^ k) (zpow_pos hp n)

/-- Non-vacuity: a single shell of charge `P ≠ 0` at radius `r > 0` has `f² = 1/4`
(`E = P²/(2r)`, `r_rms = r`, so `f = 1/2`). -/
theorem shapeFactorSq_single_shell (P r : K) (hP : P ≠ 0) (hr : 0 < r) :
    shapeFactorSq ({()} : Finset Unit) (fun _ => P) (fun _ => r) = 1 / 4 := by
  unfold shapeFactorSq shellEnergy shellMoment shellCharge
  simp only [Finset.sum_singleton, max_self]
  have hr0 : r ≠ 0 := hr.ne'
  field_simp
  ring

end QOU.Nuclear.CoulombShell
