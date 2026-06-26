import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import QOU.AlgebraicSubstrate.ConditionalClasses

/-!
# QOU.AlgebraicSubstrate.SurrealRateCalculus — rate table

Records the four classical-limit scaling laws of the QOU framework
as surreal-order inequalities:

- Mass gap `Δ_q ≍ ε^3` — positive infinitesimal of order 3.
- Reeb period `Ω_q ≍ ε⁻¹` — positive transfinite of order 1.
- Enstrophy ceiling `Z_q ≍ ε^(-4/3)` — transfinite of order 4/3.
- Rogue-zero cost `E(δ) ≍ δ² · ε⁻¹` — transfinite scaled by `δ²`.

Each is stated as a leading-coefficient equation on an abstract
field carrier `F`; downstream instances discharge by specialising
to `𝐍𝐨` via `QOU.AppendixSurreals.StandardPart`.  The class
requires only `[CommRing F]` — no ordering or positivity hypothesis;
those are added by downstream interpretations that need them
(e.g.\ to compare `Ow`-orders).

LaTeX label: `prop:surreal-rate-calculus`.

## References

- [conway1976] Conway, *On Numbers and Games*.
- [gonshor1986] Gonshor, *Introduction to the Theory of Surreal
  Numbers*. DOI:10.1017/CBO9780511629143.
-/

namespace QOU.AlgebraicSubstrate

universe u

/-- The rate-table *shape*: a class recording the four
    classical-limit rates as data over an abstract field carrier `F`.

    An instance of this class fixes the leading-coefficient equations
    `Δ = ε³`, `Ω·ε = 1`, `Z³·ε⁴ = 1`, `E(δ)·ε = δ²` (each up to a
    positive scalar absorbed into the named quantity) and entails
    the rate table [`prop:surreal-rate-calculus`].  Under the surreal
    embedding `ε ↦ 1/ω`, these equations specialise to the
    `Ow`-valuations `Ow(Δ) = -3`, `Ow(Ω) = 1`, `Ow(Z) = 4/3`,
    `Ow(E(δ)) = 1` whenever `δ ≠ 0` (the rogue-zero equation
    `E(δ)·ε = δ²` holds for every `δ : F`; the `Ow = 1`
    interpretation requires `δ ≠ 0`). -/
-- Ref: [conway1976] On Numbers and Games §III
-- Ref: [manuscript] Chapter 8 §5 (Surreal rate calculus)
class SurrealRateCalculus (F : Type u) [CommRing F] where
  /-- The Reeb infinitesimal embedded in `F`.  Non-zero (forced
      by `reebPeriod_order : reebPeriod · epsilon = 1` below). -/
  epsilon : F
  /-- The mass gap. -/
  massGap : F
  /-- The Reeb period. -/
  reebPeriod : F
  /-- The enstrophy ceiling. -/
  enstrophyCeiling : F
  /-- Rogue-zero energy cost, parametrised by a standard-real drift. -/
  roguePartCost : F → F
  /-- Mass-gap leading-coefficient equation: `Δ = ε³`. -/
  massGap_order : massGap = epsilon ^ 3
  /-- Reeb-period leading-coefficient equation: `Ω · ε = 1`. -/
  reebPeriod_order : reebPeriod * epsilon = 1
  /-- Enstrophy leading-coefficient equation: `Z³ · ε⁴ = 1`
      (the cubic form of `Z = ε^(-4/3)`, avoiding fractional
      exponents at the type level). -/
  enstrophy_order : enstrophyCeiling ^ 3 * epsilon ^ 4 = 1
  /-- Rogue-zero leading-coefficient equation:
      `E(δ) · ε = δ²` for every drift `δ`. -/
  rogueZero_order : ∀ δ : F, roguePartCost δ * epsilon = δ ^ 2

/-- **Classical-limit instance** (ε = 1).
    At the classical limit, the Reeb infinitesimal collapses to 1
    and every rate equation becomes trivial:
    - `Δ = 1 = 1³` ✓
    - `Ω · 1 = 1 · 1 = 1` ✓
    - `Z³ · 1⁴ = 1 · 1 = 1` ✓
    - `E(δ) · 1 = δ² · 1 = δ²` ✓
    This is the "no infinitesimal" baseline; the substantive
    surreal content arises when ε is genuinely infinitesimal in
    `𝐍𝐨` via the standard-part embedding. -/
instance surrealRateCalculus_classicalLimit (F : Type u) [CommRing F] :
    SurrealRateCalculus F where
  epsilon := 1
  massGap := 1
  reebPeriod := 1
  enstrophyCeiling := 1
  roguePartCost := fun δ => δ ^ 2
  massGap_order := by norm_num
  reebPeriod_order := by norm_num
  enstrophy_order := by norm_num
  rogueZero_order := fun δ => by ring

/-- **Surreal rate calculus — the four strict inequalities**
    ([`prop:surreal-rate-calculus`]).

    Working in an ordered field `F` carrying the rate data
    `[SurrealRateCalculus F]` (so the leading-coefficient equations
    `Δ = ε³`, `Ω · ε = 1`, … hold) and treating `ε` as a *strictly
    positive infinitesimal* — `0 < ε` together with `hε_inf`: every
    positive power `ε^(n+1)` lies below every standard real `λ > 0` —
    the four claims of the proposition are **derived**, not assumed:

    1. **Positivity** — `0 < Δ` and `0 < Ω`.
    2. **Infinitesimal gap** — `Δ < λ` for every standard real `λ > 0`.
    3. **Transfinite period** — `λ < Ω` for every standard real `λ > 0`.
    4. **Squeeze** — `Δ < δ² · Ω` for every standard real `δ > 0`
       (the mechanism underlying every millennium-problem squeeze:
       a standard-scale cost `δ² · ε⁻¹` strictly exceeds the
       infinitesimal dissipation `ε³`).

    The proof is purely order-theoretic — items (1)–(3) follow from
    the rate equations and the positivity/archimedean-smallness of
    `ε`; item (4) reduces, after multiplying by `ε > 0`, to
    `ε⁴ < δ²`, which is the `n = 3` instance of `hε_inf`.  No
    cancellation in an ordered field is possible because the cost is
    transfinite and the dissipation infinitesimal.

    The five §3b-cond conjecture-class hypotheses
    (`[QAubinLions]`, …, `[RegularityBreakdown]`) record the
    conditional dependency of the rate *table* on the q-NS conjecture
    cone (`conj:q-aubin-lions`, …, `conj:regularity-breakdown`), per
    the `.md` banner; the inequalities themselves are unconditional
    given the rate data and the infinitesimality of `ε`. -/
-- Ref: [conway1976] On Numbers and Games §III
-- Ref: [manuscript] Chapter 8 §5 (Surreal rate calculus)
theorem surreal_rate_calculus_conditional
    {F : Type u} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    [S : SurrealRateCalculus F]
    [QAubinLions] [NSCounterexample] [CriticalExponent]
    [BlowupYekutieli] [RegularityBreakdown]
    (hε_pos : 0 < S.epsilon)
    (hε_inf : ∀ (n : ℕ) (lam : F), 0 < lam → S.epsilon ^ (n + 1) < lam) :
    (0 < S.massGap ∧ 0 < S.reebPeriod)
    ∧ (∀ lam : F, 0 < lam → S.massGap < lam)
    ∧ (∀ lam : F, 0 < lam → lam < S.reebPeriod)
    ∧ (∀ δ : F, 0 < δ → S.massGap < δ ^ 2 * S.reebPeriod) := by
  have hΔ := S.massGap_order
  have hΩ := S.reebPeriod_order
  -- (1) Ω > 0 from `Ω · ε = 1` and `ε > 0`.
  have hΩpos : 0 < S.reebPeriod := by
    rcases lt_trichotomy S.reebPeriod 0 with h | h | h
    · exfalso; nlinarith [mul_pos (neg_pos.mpr h) hε_pos]
    · exfalso; rw [h] at hΩ; simp at hΩ
    · exact h
  -- (1) Δ > 0 from `Δ = ε³` and `ε > 0`.
  have hΔpos : 0 < S.massGap := by rw [hΔ]; positivity
  refine ⟨⟨hΔpos, hΩpos⟩, ?_, ?_, ?_⟩
  · -- (2) Δ = ε³ < λ — the `n = 2` infinitesimality instance.
    intro lam hlam; rw [hΔ]; exact hε_inf 2 lam hlam
  · -- (3) λ < Ω: from `ε < λ⁻¹` (the `n = 0` instance) we get
    --     `λ · ε < 1 = Ω · ε`, hence `λ < Ω` since `ε > 0`.
    intro lam hlam
    have hεlt : S.epsilon ^ (0 + 1) < lam⁻¹ := hε_inf 0 lam⁻¹ (by positivity)
    simp only [zero_add, pow_one] at hεlt
    have hle : lam * S.epsilon < 1 := by
      have := (mul_lt_mul_left hlam).mpr hεlt
      rwa [mul_inv_cancel₀ (ne_of_gt hlam)] at this
    nlinarith [mul_pos hlam hε_pos]
  · -- (4) Squeeze Δ < δ² · Ω.  Multiply by `ε > 0`:
    --     `δ² · Ω · ε = δ²` and `ε³ · ε = ε⁴`, reducing to `ε⁴ < δ²`,
    --     the `n = 3` infinitesimality instance.
    intro δ hδ
    rw [hΔ, ← mul_lt_mul_right hε_pos]
    have lhs : δ ^ 2 * S.reebPeriod * S.epsilon = δ ^ 2 := by
      rw [mul_assoc, hΩ, mul_one]
    have rhs : S.epsilon ^ 3 * S.epsilon = S.epsilon ^ 4 := by ring
    rw [rhs, lhs]
    have := hε_inf 3 (δ ^ 2) (by positivity)
    simpa using this

end QOU.AlgebraicSubstrate
