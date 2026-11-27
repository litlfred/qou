import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# QOU.FluidDynamics.q_ns_triad_core

The algebraic core of the q-NS modal triad model (bean `qou-pa7n`). It covers
the `SU_q(2)` fusion rule on doubled spins (`FusionTriad`), triad coefficient
systems with Kraichnan detailed conservation (`TriadCoeff`), the Galerkin
transfer, its energy conservation and its finite reach, and the non-vacuity
witness `kraichnan`.

Everything here is over a generic `Field K`. There is no `ℝ` and no analysis.
The Galerkin dynamics over `ℝ` and the Part A truncation bound live in
`QOU.Transcendental.FluidDynamics.q_ns_modal_triad`, which imports this file.
They were split on 2026-11-27 so that the algebraic triad files
(`q_ns_triad_derivation`, `q_ns_triad_noncomm`) do not import a Transcendental
module.

No empirical value enters any proof.

## References

- [leitner2026] fluid-dynamics/q-navier-stokes.md (`def:q-navier-stokes`)
- [leitner2026] fluid-dynamics/quantum-peter-weyl.md (`thm:quantum-peter-weyl`)
-/

namespace QOU.FluidDynamics.ModalTriad

open Finset

/-! ### The `SU_q(2)` fusion rule on doubled spins -/

/-- `V_a ⊂ V_b ⊗ V_c` for generic `q`, labels being doubled spins `a = 2j`. -/
def FusionTriad (a b c : ℕ) : Prop :=
  a ≤ b + c ∧ b ≤ a + c ∧ c ≤ a + b ∧ Even (a + b + c)

instance (a b c : ℕ) : Decidable (FusionTriad a b c) := by
  unfold FusionTriad; infer_instance

theorem FusionTriad.rotate {a b c : ℕ} (h : FusionTriad a b c) :
    FusionTriad b c a := by
  obtain ⟨h1, h2, h3, h4⟩ := h
  refine ⟨by omega, by omega, by omega, ?_⟩
  have : b + c + a = a + b + c := by ring
  rw [this]; exact h4

theorem FusionTriad.swap {a b c : ℕ} (h : FusionTriad a b c) :
    FusionTriad a c b := by
  obtain ⟨h1, h2, h3, h4⟩ := h
  refine ⟨by omega, by omega, by omega, ?_⟩
  have : a + c + b = a + b + c := by ring
  rw [this]; exact h4

/-! ### Triad coefficient systems -/

/-- A quadratic modal nonlinearity on fusion triads that conserves the weighted
    energy `∑ wₙ aₙ²` triad by triad. `C n p r` is the coupling of the pair
    `(p, r)` into mode `n`. -/
structure TriadCoeff (K : Type*) [Field K] where
  /-- Parseval weights of the energy. -/
  w : ℕ → K
  /-- Coupling coefficients. -/
  C : ℕ → ℕ → ℕ → K
  /-- Couplings vanish off the fusion rule. -/
  supp : ∀ n p r, ¬ FusionTriad n p r → C n p r = 0
  /-- The pair `(p, r)` is unordered. -/
  symm : ∀ n p r, C n p r = C n r p
  /-- Detailed (triad-wise) energy conservation. -/
  conserve : ∀ n p r, w n * C n p r + w p * C p r n + w r * C r n p = 0

variable {K : Type*} [Field K]

/-- The Galerkin transfer into mode `n` on the finite mode set `S`. -/
def transfer (T : TriadCoeff K) (S : Finset ℕ) (a : ℕ → K) (n : ℕ) : K :=
  ∑ p ∈ S, ∑ r ∈ S, T.C n p r * a p * a r

/-- **Galerkin energy conservation.** On every finite mode set, the nonlinear
    transfer does no work on the weighted energy. -/
theorem galerkin_energy_conservation (T : TriadCoeff K) (S : Finset ℕ)
    (a : ℕ → K) (h3 : (3 : K) ≠ 0) :
    ∑ n ∈ S, T.w n * a n * transfer T S a n = 0 := by
  set X := ∑ n ∈ S, ∑ p ∈ S, ∑ r ∈ S, T.w n * T.C n p r * a n * a p * a r
    with hX
  have hL : ∑ n ∈ S, T.w n * a n * transfer T S a n = X := by
    rw [hX]
    refine sum_congr rfl fun n _ => ?_
    simp only [transfer, mul_sum]
    refine sum_congr rfl fun p _ => sum_congr rfl fun r _ => ?_
    ring
  have hY : (∑ n ∈ S, ∑ p ∈ S, ∑ r ∈ S,
      T.w p * T.C p r n * a p * a r * a n) = X := by
    rw [hX, Finset.sum_comm]
    refine sum_congr rfl fun p _ => ?_
    rw [Finset.sum_comm]
  have hZ : (∑ n ∈ S, ∑ p ∈ S, ∑ r ∈ S,
      T.w r * T.C r n p * a r * a n * a p) = X := by
    have : (∑ n ∈ S, ∑ p ∈ S, ∑ r ∈ S, T.w r * T.C r n p * a r * a n * a p)
        = ∑ n ∈ S, ∑ r ∈ S, ∑ p ∈ S, T.w r * T.C r n p * a r * a n * a p :=
      sum_congr rfl fun n _ => Finset.sum_comm
    rw [this, Finset.sum_comm]
  have hsum : X + X + X = 0 := by
    calc X + X + X
        = (∑ n ∈ S, ∑ p ∈ S, ∑ r ∈ S, T.w n * T.C n p r * a n * a p * a r)
          + (∑ n ∈ S, ∑ p ∈ S, ∑ r ∈ S, T.w p * T.C p r n * a p * a r * a n)
          + (∑ n ∈ S, ∑ p ∈ S, ∑ r ∈ S, T.w r * T.C r n p * a r * a n * a p) := by
          rw [hY, hZ]
      _ = ∑ n ∈ S, ∑ p ∈ S, ∑ r ∈ S,
            a n * a p * a r *
              (T.w n * T.C n p r + T.w p * T.C p r n + T.w r * T.C r n p) := by
          simp only [← sum_add_distrib]
          refine sum_congr rfl fun n _ => sum_congr rfl fun p _ =>
            sum_congr rfl fun r _ => ?_
          ring
      _ = 0 := by simp [T.conserve]
  have : (3 : K) * X = 0 := by rw [← hsum]; ring
  rw [hL]
  exact (mul_eq_zero.mp this).resolve_left h3

/-- **Support growth.** Data on modes `≤ m` feed only modes `≤ 2m`: reaching
    mode `N` from data on modes `≤ m` takes at least `log₂ (N/m)` triad steps. -/
theorem transfer_eq_zero_of_gt (T : TriadCoeff K) (S : Finset ℕ) (a : ℕ → K)
    {m n : ℕ} (hS : ∀ p ∈ S, p ≤ m) (hn : 2 * m < n) :
    transfer T S a n = 0 := by
  unfold transfer
  refine sum_eq_zero fun p hp => sum_eq_zero fun r hr => ?_
  have hnot : ¬ FusionTriad n p r := by
    intro h
    have h1 := h.1
    have := hS p hp
    have := hS r hr
    omega
  rw [T.supp n p r hnot]; ring

/-! ### Non-vacuity: a nonzero coefficient system -/

/-- Kraichnan-type coefficients `Cₙₚᵣ = (fₚ + fᵣ − 2fₙ)/wₙ` on fusion triads.
    A non-vacuity witness, **not** the q-NS coefficient system. -/
noncomputable def kraichnan (w f : ℕ → K) (hw : ∀ n, w n ≠ 0) : TriadCoeff K where
  w := w
  C n p r := if FusionTriad n p r then (f p + f r - 2 * f n) / w n else 0
  supp n p r h := by simp [h]
  symm n p r := by
    by_cases h : FusionTriad n p r
    · simp only [if_pos h, if_pos h.swap]; ring
    · have h' : ¬ FusionTriad n r p := fun h' => h h'.swap
      simp [h, h']
  conserve n p r := by
    by_cases h : FusionTriad n p r
    · rw [if_pos h, if_pos h.rotate, if_pos h.rotate.rotate,
        mul_div_cancel₀ _ (hw n), mul_div_cancel₀ _ (hw p),
        mul_div_cancel₀ _ (hw r)]
      ring
    · have h1 : ¬ FusionTriad p r n := fun h' => h h'.rotate.rotate
      have h2 : ¬ FusionTriad r n p := fun h' => h h'.rotate
      simp [h, h1, h2]

/-- The witness is not the zero nonlinearity: with `w ≡ 1`, `f = id`, the pair
    `(1, 1)` (two spin-½ modes) couples into mode `0` with coefficient `2`. -/
theorem kraichnan_ne_zero :
    (kraichnan (K := ℚ) (fun _ => 1) (fun n => (n : ℚ)) (fun _ => one_ne_zero)).C 0 1 1
      = 2 := by
  have h : FusionTriad 0 1 1 := ⟨by norm_num, by norm_num, by norm_num, ⟨1, rfl⟩⟩
  simp only [kraichnan, if_pos h]
  norm_num

end QOU.FluidDynamics.ModalTriad
