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
    le_of_lt (by simpa using Hyperreal.epsilon_lt_of_pos (r := 1) zero_lt_one)
  refine ⟨by change (0 : ℝ*) < Hyperreal.epsilon ^ 3; positivity, ?_⟩
  intro n lam hlam
  simp only [surrealRateCalculus_hyperreal, hyperrealRealHom, RingHom.coe_mk, MonoidHom.coe_mk,
    OneHom.coe_mk]
  have hpow_le : (Hyperreal.epsilon ^ 3) ^ (n + 1) ≤ Hyperreal.epsilon := by
    rw [← pow_mul]
    have hge1 : 1 ≤ 3 * (n + 1) := by omega
    calc Hyperreal.epsilon ^ (3 * (n + 1))
        ≤ Hyperreal.epsilon ^ 1 := pow_le_pow_of_le_one (le_of_lt hu_pos) hu_le1 hge1
      _ = Hyperreal.epsilon := pow_one _
  exact lt_of_le_of_lt hpow_le (Hyperreal.epsilon_lt_of_pos hlam)

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

/-! ### Asymptotic Rate Calculus (`Δ_q ≍ ε³`, `Ω_q ≍ ε⁻¹`) with Degree-1 Infinitesimal -/

/-- **Asymptotic surreal rate calculus** (`prop:surreal-rate-calculus`, asymptotic form):
    relaxes strict power equalities to genuine two-sided asymptotic bounds
    `c₁ · ε³ ≤ Δ_q ≤ C₁ · ε³` (`0 < c₁ ≤ C₁`) and
    `c₂ · ε⁻¹ ≤ Ω_q ≤ C₂ · ε⁻¹` (`0 < c₂ ≤ C₂`) with standard scalar constants in `K`,
    accommodating `Δ_q = (1/2) · ε³ + O(ε⁴)` and decoupling `enstrophy_order` so a
    degree-1 infinitesimal `ε` (`Hyperreal.epsilon`) inhabits the structure directly. -/
class SurrealRateAsymptoticCalculus
    (K : Type v) [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (F : Type u) [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (ι : K →+* F) where
  /-- The degree-1 Reeb infinitesimal `ε` in `F`. -/
  epsilon : F
  /-- The quantum mass gap `Δ_q`. -/
  massGap : F
  /-- The Reeb period `Ω_q`. -/
  reebPeriod : F
  /-- Rogue-zero energy cost `E(δ)`. -/
  roguePartCost : F → F
  /-- Standard scalar asymptotic constants `0 < c₁ ≤ C₁` and `0 < c₂ ≤ C₂`. -/
  c₁ : K
  C₁ : K
  c₂ : K
  C₂ : K
  hc₁_pos : 0 < c₁
  hc₁_le : c₁ ≤ C₁
  hc₂_pos : 0 < c₂
  hc₂_le : c₂ ≤ C₂
  /-- Two-sided asymptotic bounds `c₁ · ε³ ≤ Δ_q ≤ C₁ · ε³`. -/
  massGap_lower : ι c₁ * epsilon ^ 3 ≤ massGap
  massGap_upper : massGap ≤ ι C₁ * epsilon ^ 3
  /-- Two-sided asymptotic bounds `c₂ · ε⁻¹ ≤ Ω_q ≤ C₂ · ε⁻¹`. -/
  reebPeriod_lower : ι c₂ * epsilon⁻¹ ≤ reebPeriod
  reebPeriod_upper : reebPeriod ≤ ι C₂ * epsilon⁻¹
  /-- Rogue-zero cost bound `(ι δ)² · Ω_q ≤ E(ι δ)` for standard `δ > 0`. -/
  rogueZero_lower : ∀ δ : K, 0 < δ → (ι δ) ^ 2 * reebPeriod ≤ roguePartCost (ι δ)

/-- **Asymptotic surreal rate calculus — all four strict inequalities** from
    degree-1 infinitesimality (`0 < ε` and `∀ r : K, 0 < r → ε < ι r`) alone:
    1. **Positivity:** `0 < Δ_q ∧ 0 < Ω_q`.
    2. **Infinitesimal gap:** `∀ λ > 0, Δ_q < ι λ`.
    3. **Transfinite period:** `∀ λ > 0, ι λ < Ω_q`.
    4. **Squeeze:** `∀ δ > 0, Δ_q < (ι δ)² · Ω_q ∧ Δ_q < E(ι δ)`. -/
theorem surreal_rate_asymptotic_calculus
    {K : Type v} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    {F : Type u} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (ι : K →+* F)
    [S : SurrealRateAsymptoticCalculus K F ι]
    (hε_pos : 0 < S.epsilon)
    (hε_inf : ∀ r : K, 0 < r → S.epsilon < ι r) :
    (0 < S.massGap ∧ 0 < S.reebPeriod)
    ∧ (∀ lam : K, 0 < lam → S.massGap < ι lam)
    ∧ (∀ lam : K, 0 < lam → ι lam < S.reebPeriod)
    ∧ (∀ δ : K, 0 < δ →
        S.massGap < (ι δ) ^ 2 * S.reebPeriod ∧
        S.massGap < S.roguePartCost (ι δ)) := by
  have hι_pos : ∀ r : K, 0 < r → 0 < ι r := fun r hr => lt_trans hε_pos (hε_inf r hr)
  have hε1 : S.epsilon < 1 := by simpa only [map_one] using hε_inf 1 zero_lt_one
  have hC₁_pos : 0 < S.C₁ := lt_of_lt_of_le S.hc₁_pos S.hc₁_le
  have hιc₁_pos : 0 < ι S.c₁ := hι_pos S.c₁ S.hc₁_pos
  have hιC₁_pos : 0 < ι S.C₁ := hι_pos S.C₁ hC₁_pos
  have hιc₂_pos : 0 < ι S.c₂ := hι_pos S.c₂ S.hc₂_pos
  have hε_inv_pos : 0 < S.epsilon⁻¹ := inv_pos.mpr hε_pos
  have hε_ne : S.epsilon ≠ 0 := ne_of_gt hε_pos
  have hΔ_pos : 0 < S.massGap :=
    lt_of_lt_of_le (mul_pos hιc₁_pos (pow_pos hε_pos 3)) S.massGap_lower
  have hΩ_pos : 0 < S.reebPeriod :=
    lt_of_lt_of_le (mul_pos hιc₂_pos hε_inv_pos) S.reebPeriod_lower
  refine ⟨⟨hΔ_pos, hΩ_pos⟩, ?_, ?_, ?_⟩
  · intro lam hlam
    have hdiv_pos : 0 < lam / S.C₁ := div_pos hlam hC₁_pos
    have hlt1 : S.epsilon < ι (lam / S.C₁) := hε_inf (lam / S.C₁) hdiv_pos
    rw [map_div₀] at hlt1
    have hε3_le : S.epsilon ^ 3 ≤ S.epsilon := by
      calc S.epsilon ^ 3 ≤ S.epsilon ^ 1 := pow_le_pow_of_le_one hε_pos.le hε1.le (by decide)
        _ = S.epsilon := pow_one _
    have hε3_lt : S.epsilon ^ 3 < ι lam / ι S.C₁ := lt_of_le_of_lt hε3_le hlt1
    have hmul : ι S.C₁ * S.epsilon ^ 3 < ι lam := by
      have h := (lt_div_iff₀ hιC₁_pos).mp hε3_lt
      linarith
    exact lt_of_le_of_lt S.massGap_upper hmul
  · intro lam hlam
    have hιlam_pos : 0 < ι lam := hι_pos lam hlam
    have hdiv_pos : 0 < S.c₂ / lam := div_pos S.hc₂_pos hlam
    have hlt1 : S.epsilon < ι (S.c₂ / lam) := hε_inf (S.c₂ / lam) hdiv_pos
    rw [map_div₀] at hlt1
    have hmul1 : S.epsilon * ι lam < ι S.c₂ := (lt_div_iff₀ hιlam_pos).mp hlt1
    have hmul2 : (S.epsilon * ι lam) * S.epsilon⁻¹ < ι S.c₂ * S.epsilon⁻¹ :=
      (mul_lt_mul_iff_left₀ hε_inv_pos).mpr hmul1
    have hlhs : (S.epsilon * ι lam) * S.epsilon⁻¹ = ι lam := by
      calc (S.epsilon * ι lam) * S.epsilon⁻¹
          = ι lam * (S.epsilon * S.epsilon⁻¹) := by ring
        _ = ι lam * 1 := by rw [mul_inv_cancel₀ hε_ne]
        _ = ι lam := mul_one _
    rw [hlhs] at hmul2
    exact lt_of_lt_of_le hmul2 S.reebPeriod_lower
  · intro δ hδ
    have hδ2_pos : 0 < δ ^ 2 := sq_pos_of_pos hδ
    have hr_pos : 0 < (S.c₂ * δ ^ 2) / S.C₁ := div_pos (mul_pos S.hc₂_pos hδ2_pos) hC₁_pos
    have hlt1 : S.epsilon < ι ((S.c₂ * δ ^ 2) / S.C₁) := hε_inf _ hr_pos
    rw [map_div₀, map_mul, map_pow] at hlt1
    have hε4_le : S.epsilon ^ 4 ≤ S.epsilon := by
      calc S.epsilon ^ 4 ≤ S.epsilon ^ 1 := pow_le_pow_of_le_one hε_pos.le hε1.le (by decide)
        _ = S.epsilon := pow_one _
    have hε4_lt : S.epsilon ^ 4 < (ι S.c₂ * (ι δ) ^ 2) / ι S.C₁ :=
      lt_of_le_of_lt hε4_le hlt1
    have hmul1 : ι S.C₁ * S.epsilon ^ 4 < ι S.c₂ * (ι δ) ^ 2 := by
      have h := (lt_div_iff₀ hιC₁_pos).mp hε4_lt
      linarith
    have hmul2 : (ι S.C₁ * S.epsilon ^ 4) * S.epsilon⁻¹ < (ι S.c₂ * (ι δ) ^ 2) * S.epsilon⁻¹ :=
      (mul_lt_mul_iff_left₀ hε_inv_pos).mpr hmul1
    have hlhs : (ι S.C₁ * S.epsilon ^ 4) * S.epsilon⁻¹ = ι S.C₁ * S.epsilon ^ 3 := by
      calc (ι S.C₁ * S.epsilon ^ 4) * S.epsilon⁻¹
          = ι S.C₁ * S.epsilon ^ 3 * (S.epsilon * S.epsilon⁻¹) := by ring
        _ = ι S.C₁ * S.epsilon ^ 3 * 1 := by rw [mul_inv_cancel₀ hε_ne]
        _ = ι S.C₁ * S.epsilon ^ 3 := mul_one _
    have hrhs : (ι S.c₂ * (ι δ) ^ 2) * S.epsilon⁻¹ ≤ (ι δ) ^ 2 * S.reebPeriod := by
      have hcomm : (ι S.c₂ * (ι δ) ^ 2) * S.epsilon⁻¹ = (ι δ) ^ 2 * (ι S.c₂ * S.epsilon⁻¹) := by
        ring
      rw [hcomm]
      exact mul_le_mul_of_nonneg_left S.reebPeriod_lower (sq_nonneg _)
    rw [hlhs] at hmul2
    have hsqz : S.massGap < (ι δ) ^ 2 * S.reebPeriod :=
      lt_of_le_of_lt S.massGap_upper (lt_of_lt_of_le hmul2 hrhs)
    exact ⟨hsqz, lt_of_lt_of_le hsqz (S.rogueZero_lower δ hδ)⟩

/-- Concrete Hyperreal instantiation of `SurrealRateAsymptoticCalculus` with
    degree-1 `epsilon = Hyperreal.epsilon` (no `ε³` cube needed!),
    `massGap = (1/2) · ε³ + ε⁴` (`(1/2) · ε³ ≤ Δ_q ≤ 1 · ε³`), and
    `reebPeriod = Hyperreal.omega = ε⁻¹`. -/
noncomputable def surrealRateAsymptoticCalculus_hyperreal :
    SurrealRateAsymptoticCalculus ℝ ℝ* hyperrealRealHom where
  epsilon := Hyperreal.epsilon
  massGap := (1 / 2 : ℝ*) * Hyperreal.epsilon ^ 3 + Hyperreal.epsilon ^ 4
  reebPeriod := Hyperreal.omega
  roguePartCost := fun δ => δ ^ 2 * Hyperreal.omega
  c₁ := 1 / 2
  C₁ := 1
  c₂ := 1
  C₂ := 1
  hc₁_pos := by norm_num
  hc₁_le := by norm_num
  hc₂_pos := by norm_num
  hc₂_le := by norm_num
  massGap_lower := by
    have hε_pos : 0 < Hyperreal.epsilon := Hyperreal.epsilon_pos
    have hε4_nonneg : 0 ≤ Hyperreal.epsilon ^ 4 := by positivity
    have hcoe : hyperrealRealHom (1 / 2 : ℝ) = (1 / 2 : ℝ*) := by
      simp [hyperrealRealHom]
    rw [hcoe]
    linarith
  massGap_upper := by
    have hε_pos : 0 < Hyperreal.epsilon := Hyperreal.epsilon_pos
    have hε_lt_half : Hyperreal.epsilon < (1 / 2 : ℝ*) := by
      simpa using Hyperreal.epsilon_lt_of_pos (r := (1 / 2 : ℝ)) (by norm_num)
    have hε3_pos : 0 < Hyperreal.epsilon ^ 3 := pow_pos hε_pos 3
    have hε4_le : Hyperreal.epsilon ^ 4 ≤ (1 / 2 : ℝ*) * Hyperreal.epsilon ^ 3 := by
      have hmul : Hyperreal.epsilon * Hyperreal.epsilon ^ 3 ≤
          (1 / 2 : ℝ*) * Hyperreal.epsilon ^ 3 :=
        mul_le_mul_of_nonneg_right hε_lt_half.le hε3_pos.le
      calc Hyperreal.epsilon ^ 4 = Hyperreal.epsilon * Hyperreal.epsilon ^ 3 := by ring
        _ ≤ (1 / 2 : ℝ*) * Hyperreal.epsilon ^ 3 := hmul
    have hcoe : hyperrealRealHom (1 : ℝ) = (1 : ℝ*) := map_one _
    rw [hcoe, one_mul]
    linarith
  reebPeriod_lower := by
    have hcoe : hyperrealRealHom (1 : ℝ) = (1 : ℝ*) := map_one _
    rw [hcoe, one_mul, Hyperreal.inv_epsilon]
  reebPeriod_upper := by
    have hcoe : hyperrealRealHom (1 : ℝ) = (1 : ℝ*) := map_one _
    rw [hcoe, one_mul, Hyperreal.inv_epsilon]
  rogueZero_lower := fun _ _ => le_rfl

/-- Direct unconditional instantiation of all four `SurrealRateAsymptoticCalculus`
    inequalities on `ℝ*` with degree-1 `Hyperreal.epsilon` and
    `Δ_q = (1/2) · ε³ + ε⁴`. -/
theorem surreal_rate_asymptotic_hyperreal_instantiated :
    letI := surrealRateAsymptoticCalculus_hyperreal
    (0 < surrealRateAsymptoticCalculus_hyperreal.massGap ∧
      0 < surrealRateAsymptoticCalculus_hyperreal.reebPeriod)
    ∧ (∀ lam : ℝ, 0 < lam →
        surrealRateAsymptoticCalculus_hyperreal.massGap < hyperrealRealHom lam)
    ∧ (∀ lam : ℝ, 0 < lam →
        hyperrealRealHom lam < surrealRateAsymptoticCalculus_hyperreal.reebPeriod)
    ∧ (∀ δ : ℝ, 0 < δ →
        surrealRateAsymptoticCalculus_hyperreal.massGap <
          (hyperrealRealHom δ) ^ 2 * surrealRateAsymptoticCalculus_hyperreal.reebPeriod ∧
        surrealRateAsymptoticCalculus_hyperreal.massGap <
          surrealRateAsymptoticCalculus_hyperreal.roguePartCost (hyperrealRealHom δ)) := by
  letI := surrealRateAsymptoticCalculus_hyperreal
  exact surreal_rate_asymptotic_calculus hyperrealRealHom Hyperreal.epsilon_pos
    (fun r hr => Hyperreal.epsilon_lt_of_pos hr)

/-- Archimedean `(F := ℝ)` classical-limit specialisation of `surrealRateCalculus_classicalLimit`
    (§7c `_real` pair). -/
def surrealRateCalculus_classicalLimit_real : SurrealRateCalculus ℝ :=
  surrealRateCalculus_classicalLimit ℝ

end QOU.AlgebraicSubstrate
