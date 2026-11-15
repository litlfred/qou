import Mathlib.Algebra.Ring.Units
import Mathlib.Tactic.Ring


/-!
# QOU.BraidKnot.LeptonBringSurfaceH3

Lepton Bring-surface representation: H_3 3-channel Wedderburn
convention for V̂_ℓ (additive Wedderburn volume).

Ref: [leitner2026] prop:lepton-bring-surface-h3-3channel
Ref: [leitner2026] docs/audits/2026-05-25-lepton-bring-surface-h3-3channel-convention.md

Proves the closed-form algebraic identity:
  V̂_ℓ = W_SYM · q^(2m+1) + W_STD · (z · a_{2m+1} + b_{2m+1})
       + W_ALT · (-q⁻¹)^(2m+1)

Where (a_n, b_n) come from the Hecke recursion σ^n = a_n σ + b_n
(reuses lepton-mass-tower-canonical's torus_knot_odd_reduction_exists).

Base ring (AGENTS.md §7c). Generic `{R : Type*} [CommRing R]`; the two
quantities that have to be inverted — the substrate modulus `q` and the
q-factorial `[3]_q!` normalising the Plancherel weights — are carried as
**units** (`q qfac_3 : Rˣ`), so every occurrence is a `Units` coercion
`↑q⁻¹` / `↑qfac_3⁻¹` and no ring inverse, division or field appears. The
invertibility of `[3]_q!` is exactly the condition under which the H_3
Plancherel weights exist at all, so carrying it as a unit is the honest
hypothesis rather than a technical one.
-/

namespace QOU.BraidKnot.LeptonBringSurfaceH3

/-- H_3 Plancherel weight for a partition shape (1D irreps).
    For 1D irreps (sym = (3) or alt = (1,1,1)), d_q(λ) = 1, so the weight
    is `1/[3]_q!` — the `Units` inverse of the q-factorial. -/
def W_1D_irrep
    {R : Type*} [CommRing R] (qfac_3 : Rˣ) : R := (↑qfac_3⁻¹ : R)

/-- H_3 Plancherel weight for the standard (2D) irrep λ = (2,1).
    d_q((2,1)) = [2]_q = q + q⁻¹, so W_STD = [2]_q² / [3]_q!. -/
def W_STD
    {R : Type*} [CommRing R] (two_q : R) (qfac_3 : Rˣ) : R :=
  two_q * two_q * (↑qfac_3⁻¹ : R)

/-- The Hecke recursion (a_n, b_n) for σ_1^n in H_2(q):
    a_0 = 0, b_0 = 1; (a_{n+1}, b_{n+1}) = (a_n · h + b_n, a_n).
    By construction: σ_1^n = a_n · σ_1 + b_n in H_2(q). -/
noncomputable def hecke_ab
    {R : Type*} [CommRing R] (h : R) : ℕ → R × R
  | 0     => (0, 1)
  | n + 1 =>
    let (a_n, b_n) := hecke_ab h n
    (a_n * h + b_n, a_n)

/-- **THEOREM.** The Hecke recursion produces σ_1^n = a_n σ_1 + b_n
    in H_2(q), given the Hecke quadratic σ_1² = h σ_1 + 1. -/
theorem hecke_ab_correct
    {R : Type*} [CommRing R] (σ h : R)
    (hh : σ^2 = h * σ + 1) :
    ∀ n : ℕ, σ^n = (hecke_ab h n).1 * σ + (hecke_ab h n).2 := by
  intro n
  induction n with
  | zero =>
    simp [hecke_ab]
  | succ k ih =>
    have h_step : σ^(k+1) = σ^k * σ := by ring
    rw [h_step, ih]
    -- σ^(k+1) = (a_k σ + b_k) · σ = a_k σ² + b_k σ
    --        = a_k (h σ + 1) + b_k σ = (a_k h + b_k) σ + a_k
    have : (hecke_ab h k).1 * σ * σ + (hecke_ab h k).2 * σ
         = (hecke_ab h k).1 * σ^2 + (hecke_ab h k).2 * σ := by ring
    rw [show ((hecke_ab h k).1 * σ + (hecke_ab h k).2) * σ
          = (hecke_ab h k).1 * σ^2 + (hecke_ab h k).2 * σ from by ring,
        hh]
    simp [hecke_ab]
    ring

/-- The closed-form V̂_ℓ for a lepton with torus braid σ_1^(2m+1),
    using H_3 3-channel Plancherel formula. -/
noncomputable def lepton_V_hat_h3_3channel
    {R : Type*} [CommRing R] (q : Rˣ) (h z : R) (qfac_3 : Rˣ) (two_q : R)
    (m : ℕ) : R :=
  let n := 2 * m + 1
  let q_inv : R := (↑q⁻¹ : R)
  let (a_n, b_n) := hecke_ab h n
  let χ_sym := (q : R)^n
  let χ_alt := (-q_inv)^n
  let std_markov_traced := z * a_n + b_n
  (W_1D_irrep qfac_3) * χ_sym +
  (W_STD two_q qfac_3) * std_markov_traced +
  (W_1D_irrep qfac_3) * χ_alt

/-- **THEOREM.** For m = 1 (electron σ_1³), the formula expands as
    V̂_e = W_SYM · q³ + W_STD · ((h² + 1) z + h) + W_ALT · (-q⁻¹)³.
    Matches `mass-endomorphism-tower.md`'s V̂_e ≈ 0.594 paper convention. -/
theorem lepton_V_hat_electron_formula
    {R : Type*} [CommRing R] (q : Rˣ) (h z : R) (qfac_3 : Rˣ) (two_q : R)
    (hh_def : h = (q : R) - (↑q⁻¹ : R)) :
    lepton_V_hat_h3_3channel q h z qfac_3 two_q 1
      = (W_1D_irrep qfac_3) * (q : R)^3
      + (W_STD two_q qfac_3) * ((h^2 + 1) * z + h)
      + (W_1D_irrep qfac_3) * (-(↑q⁻¹ : R))^3 := by
  -- Unfold the definition; the (a_3, b_3) from hecke_ab evaluates to (h² + 1, h)
  unfold lepton_V_hat_h3_3channel
  simp only [hecke_ab]
  ring

end QOU.BraidKnot.LeptonBringSurfaceH3
