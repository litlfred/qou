import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Analysis.Real.Hyperreal
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp

/-!
# QOU.AlgebraicSubstrate.SurrealRateCalculus — rate table

Records the four classical-limit scaling laws of the QOU framework
as non-archimedean ordered-field inequalities over an ordered extension
`ι : K →+* F` (`K` = standard archimedean scalars such as `ℝ` or `ℚ`,
`F` = infinitesimal-enriched ordered field such as `𝐍𝐨` or `ℝ*`):

- Mass gap `Δ_q = ε^3` — positive infinitesimal of order 3 (`Δ_q < ι(λ)` for all `0 < λ : K`).
- Reeb period `Ω_q = ε⁻¹` — positive transfinite of order 1 (`ι(λ) < Ω_q` for all `0 < λ : K`).
- Enstrophy ceiling `Z_q³ · ε⁴ = 1` — transfinite of order 4/3.
- Rogue-zero cost `E(δ) · ε = δ²` — standard-scale cost `E(ι(δ)) = ι(δ)² · Ω_q > Δ_q` for all `0 < δ : K`.

Includes a concrete inhabited, non-vacuous model `surrealRateCalculus_hyperreal : SurrealRateCalculus ℝ*`
satisfying `0 < epsilon` and `∀ (n : ℕ) (lam : ℝ), 0 < lam → epsilon ^ (n + 1) < hyperrealRealHom lam`.

LaTeX label: `prop:surreal-rate-calculus`.

## References

- [conway1976] Conway, *On Numbers and Games*.
- [gonshor1986] Gonshor, *Introduction to the Theory of Surreal Numbers*.
-/

namespace QOU.AlgebraicSubstrate

universe u v

/-- The rate-table *shape*: a class recording the four classical-limit rates
    as data over an abstract commutative ring carrier `F`. -/
-- Ref: [conway1976] On Numbers and Games §III
-- Ref: [leitner2026] Chapter 8 §5 (Surreal rate calculus)
class SurrealRateCalculus (F : Type u) [CommRing F] where
  /-- The Reeb infinitesimal embedded in `F`. -/
  epsilon : F
  /-- The mass gap `Δ = ε³`. -/
  massGap : F
  /-- The Reeb period `Ω` satisfying `Ω · ε = 1`. -/
  reebPeriod : F
  /-- The enstrophy ceiling `Z` satisfying `Z³ · ε⁴ = 1`. -/
  enstrophyCeiling : F
  /-- Rogue-zero energy cost, parametrised by a drift `δ`. -/
  roguePartCost : F → F
  /-- Mass-gap leading-coefficient equation: `Δ = ε³`. -/
  massGap_order : massGap = epsilon ^ 3
  /-- Reeb-period leading-coefficient equation: `Ω · ε = 1`. -/
  reebPeriod_order : reebPeriod * epsilon = 1
  /-- Enstrophy leading-coefficient equation: `Z³ · ε⁴ = 1`. -/
  enstrophy_order : enstrophyCeiling ^ 3 * epsilon ^ 4 = 1
  /-- Rogue-zero leading-coefficient equation: `E(δ) · ε = δ²`. -/
  rogueZero_order : ∀ δ : F, roguePartCost δ * epsilon = δ ^ 2

/-- **Classical-limit baseline** (`ε = 1`), kept as an explicit `def` (not an `instance`). -/
def surrealRateCalculus_classicalLimit (F : Type u) [CommRing F] :
    SurrealRateCalculus F where
  epsilon := 1
  massGap := 1
  reebPeriod := 1
  enstrophyCeiling := 1
  roguePartCost := fun δ => δ ^ 2
  massGap_order := by norm_num
  reebPeriod_order := by norm_num
  enstrophy_order := by norm_num
  rogueZero_order := fun _ => by ring

/-- **Surreal rate calculus — the four strict inequalities**
    ([`prop:surreal-rate-calculus`]).

    Given an ordered base field `K` (standard scalars `λ, δ > 0`) embedded via
    `ι : K →+* F` into a strictly ordered field `F` carrying `[S : SurrealRateCalculus F]`
    with `0 < S.epsilon` and `hε_inf : ∀ (n : ℕ) (lam : K), 0 < lam → S.epsilon ^ (n + 1) < ι lam`,
    all four claims of `prop:surreal-rate-calculus` hold:
    1. **Positivity:** `0 < S.massGap ∧ 0 < S.reebPeriod`.
    2. **Infinitesimal gap:** `∀ lam : K, 0 < lam → S.massGap < ι lam`.
    3. **Transfinite period:** `∀ lam : K, 0 < lam → ι lam < S.reebPeriod`.
    4. **Squeeze:** `∀ δ : K, 0 < δ → S.massGap < (ι δ) ^ 2 * S.reebPeriod ∧ S.roguePartCost (ι δ) = (ι δ) ^ 2 * S.reebPeriod`. -/
-- Ref: [conway1976] On Numbers and Games §III
-- Ref: [leitner2026] Chapter 8 §5 (Surreal rate calculus)
theorem surreal_rate_calculus_conditional
    {K : Type v} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {F : Type u} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (ι : K →+* F)
    [S : SurrealRateCalculus F]
    (hε_pos : 0 < S.epsilon)
    (hε_inf : ∀ (n : ℕ) (lam : K), 0 < lam → S.epsilon ^ (n + 1) < ι lam) :
    (0 < S.massGap ∧ 0 < S.reebPeriod)
    ∧ (∀ lam : K, 0 < lam → S.massGap < ι lam)
    ∧ (∀ lam : K, 0 < lam → ι lam < S.reebPeriod)
    ∧ (∀ δ : K, 0 < δ →
        S.massGap < (ι δ) ^ 2 * S.reebPeriod ∧
        S.roguePartCost (ι δ) = (ι δ) ^ 2 * S.reebPeriod) := by
  have hΔ := S.massGap_order
  have hΩ := S.reebPeriod_order
  have hε_ne : S.epsilon ≠ 0 := ne_of_gt hε_pos
  have hΩpos : 0 < S.reebPeriod := by
    rcases lt_trichotomy S.reebPeriod 0 with h | h | h
    · exfalso; nlinarith [mul_pos (neg_pos.mpr h) hε_pos]
    · exfalso; rw [h] at hΩ; simp at hΩ
    · exact h
  have hΔpos : 0 < S.massGap := by rw [hΔ]; positivity
  refine ⟨⟨hΔpos, hΩpos⟩, ?_, ?_, ?_⟩
  · intro lam hlam
    rw [hΔ]
    exact hε_inf 2 lam hlam
  · intro lam hlam
    have hlam_inv_pos : 0 < lam⁻¹ := inv_pos.mpr hlam
    have hι_pos : 0 < ι lam :=
      lt_trans (pow_pos hε_pos 1) (hε_inf 0 lam hlam)
    have hεlt : S.epsilon ^ (0 + 1) < ι lam⁻¹ := hε_inf 0 lam⁻¹ hlam_inv_pos
    simp only [zero_add, pow_one, map_inv₀] at hεlt
    have hle : ι lam * S.epsilon < 1 := by
      have hmul := (mul_lt_mul_iff_right₀ hι_pos).mpr hεlt
      rwa [mul_inv_cancel₀ (ne_of_gt hι_pos)] at hmul
    nlinarith [mul_pos hι_pos hε_pos]
  · intro δ hδ
    have hrogue : S.roguePartCost (ι δ) = (ι δ) ^ 2 * S.reebPeriod := by
      apply mul_right_cancel₀ hε_ne
      calc S.roguePartCost (ι δ) * S.epsilon
          = (ι δ) ^ 2 := S.rogueZero_order (ι δ)
        _ = (ι δ) ^ 2 * 1 := (mul_one _).symm
        _ = (ι δ) ^ 2 * (S.reebPeriod * S.epsilon) := by rw [hΩ]
        _ = ((ι δ) ^ 2 * S.reebPeriod) * S.epsilon := (mul_assoc _ _ _).symm
    refine ⟨?_, hrogue⟩
    rw [hΔ, ← mul_lt_mul_iff_left₀ hε_pos]
    have lhs : (ι δ) ^ 2 * S.reebPeriod * S.epsilon = ι (δ ^ 2) := by
      rw [mul_assoc, hΩ, mul_one, map_pow]
    have rhs : S.epsilon ^ 3 * S.epsilon = S.epsilon ^ 4 := by ring
    rw [rhs, lhs]
    simpa using hε_inf 3 (δ ^ 2) (sq_pos_of_pos hδ)

/-! ### Non-vacuity witness on `ℝ*` (`Hyperreal`) -/

/-- Canonical ring embedding `ℝ →+* ℝ*` of standard reals into the hyperreals. -/
noncomputable def hyperrealRealHom : ℝ →+* ℝ* where
  toFun r := (r : ℝ*)
  map_one' := Hyperreal.coe_one
  map_mul' := Hyperreal.coe_mul
  map_zero' := Hyperreal.coe_zero
  map_add' := Hyperreal.coe_add

/-- Concrete inhabited model of `SurrealRateCalculus ℝ*` with `ε = Hyperreal.epsilon³`,
    `Δ = Hyperreal.epsilon⁹`, `Ω = Hyperreal.omega³`, `Z = Hyperreal.omega⁴`
    (`Z³ · ε⁴ = ω¹² · ε¹² = 1`), and `E(δ) = δ² · ω³`. -/
noncomputable def surrealRateCalculus_hyperreal : SurrealRateCalculus ℝ* where
  epsilon := Hyperreal.epsilon ^ 3
  massGap := Hyperreal.epsilon ^ 9
  reebPeriod := Hyperreal.omega ^ 3
  enstrophyCeiling := Hyperreal.omega ^ 4
  roguePartCost := fun δ => δ ^ 2 * Hyperreal.omega ^ 3
  massGap_order := by ring
  reebPeriod_order := by
    have hωε : Hyperreal.omega * Hyperreal.epsilon = 1 := by
      rw [mul_comm]; exact Hyperreal.epsilon_mul_omega
    calc Hyperreal.omega ^ 3 * Hyperreal.epsilon ^ 3
        = (Hyperreal.omega * Hyperreal.epsilon) ^ 3 := by ring
      _ = 1 ^ 3 := by rw [hωε]
      _ = 1 := one_pow 3
  enstrophy_order := by
    have hωε : Hyperreal.omega * Hyperreal.epsilon = 1 := by
      rw [mul_comm]; exact Hyperreal.epsilon_mul_omega
    calc (Hyperreal.omega ^ 4) ^ 3 * (Hyperreal.epsilon ^ 3) ^ 4
        = (Hyperreal.omega * Hyperreal.epsilon) ^ 12 := by ring
      _ = 1 ^ 12 := by rw [hωε]
      _ = 1 := one_pow 12
  rogueZero_order := fun δ => by
    have hωε : Hyperreal.omega * Hyperreal.epsilon = 1 := by
      rw [mul_comm]; exact Hyperreal.epsilon_mul_omega
    calc δ ^ 2 * Hyperreal.omega ^ 3 * Hyperreal.epsilon ^ 3
        = δ ^ 2 * (Hyperreal.omega * Hyperreal.epsilon) ^ 3 := by ring
      _ = δ ^ 2 * 1 ^ 3 := by rw [hωε]
      _ = δ ^ 2 := by ring

/-- Non-vacuity theorem: `surrealRateCalculus_hyperreal` satisfies BOTH hypotheses
    `0 < S.epsilon` and `∀ (n : ℕ) (lam : ℝ), 0 < lam → S.epsilon ^ (n + 1) < hyperrealRealHom lam`
    of `surreal_rate_calculus_conditional`! -/
theorem surrealRateCalculus_hyperreal_satisfies_hypotheses :
    0 < surrealRateCalculus_hyperreal.epsilon ∧
    ∀ (n : ℕ) (lam : ℝ), 0 < lam →
      surrealRateCalculus_hyperreal.epsilon ^ (n + 1) < hyperrealRealHom lam := by
  have hu_pos : 0 < Hyperreal.epsilon := Hyperreal.epsilon_pos
  have hu_le1 : Hyperreal.epsilon ≤ 1 :=
    le_of_lt (by simpa using Hyperreal.epsilon_lt_pos 1 zero_lt_one)
  refine ⟨by simp [surrealRateCalculus_hyperreal]; positivity, ?_⟩
  intro n lam hlam
  simp only [surrealRateCalculus_hyperreal, hyperrealRealHom, RingHom.coe_mk, MonoidHom.coe_mk,
    OneHom.coe_mk]
  have hpow_le : (Hyperreal.epsilon ^ 3) ^ (n + 1) ≤ Hyperreal.epsilon := by
    rw [← pow_mul]
    have hge1 : 1 ≤ 3 * (n + 1) := by omega
    calc Hyperreal.epsilon ^ (3 * (n + 1))
        ≤ Hyperreal.epsilon ^ 1 := pow_le_pow_of_le_one (le_of_lt hu_pos) hu_le1 hge1
      _ = Hyperreal.epsilon := pow_one _
  exact lt_of_le_of_lt hpow_le (Hyperreal.epsilon_lt_pos lam hlam)

/-- Direct instantiation of all four `surreal_rate_calculus_conditional` inequalities
    on the non-vacuous model `surrealRateCalculus_hyperreal`! -/
theorem surreal_rate_calculus_hyperreal_instantiated :
    letI : SurrealRateCalculus ℝ* := surrealRateCalculus_hyperreal
    (0 < surrealRateCalculus_hyperreal.massGap ∧ 0 < surrealRateCalculus_hyperreal.reebPeriod)
    ∧ (∀ lam : ℝ, 0 < lam → surrealRateCalculus_hyperreal.massGap < hyperrealRealHom lam)
    ∧ (∀ lam : ℝ, 0 < lam → hyperrealRealHom lam < surrealRateCalculus_hyperreal.reebPeriod)
    ∧ (∀ δ : ℝ, 0 < δ →
        surrealRateCalculus_hyperreal.massGap <
          (hyperrealRealHom δ) ^ 2 * surrealRateCalculus_hyperreal.reebPeriod ∧
        surrealRateCalculus_hyperreal.roguePartCost (hyperrealRealHom δ) =
          (hyperrealRealHom δ) ^ 2 * surrealRateCalculus_hyperreal.reebPeriod) := by
  letI : SurrealRateCalculus ℝ* := surrealRateCalculus_hyperreal
  obtain ⟨hpos, hinf⟩ := surrealRateCalculus_hyperreal_satisfies_hypotheses
  exact surreal_rate_calculus_conditional hyperrealRealHom hpos hinf

end QOU.AlgebraicSubstrate
