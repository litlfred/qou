import QOU.MassTheory.PairSkeinMassConventionD
import Mathlib.Tactic.LinearCombination

/-!
# QOU.MassTheory.PairSkeinNucleon — nucleon masses under the pair Skein formula

LaTeX label: `prop:terminal-resolution`.

The convention-D pair Skein formula (`lem:pair-skein-mass-formula`, derived in
`QOU.MassTheory.PairSkeinD`) assigns to an ordered quark pair `(a, b)` the
pair mass

  `S_ab = trace₂ z_D (μ_a·σ + μ_b·σ⁻¹) = w₊·μ_a + w₋·μ_b`,

with `w₊ = z_D = q³/(q² + 1)` and `w₋ = z_D − h = q⁻¹/(q² + 1)`. A nucleon
mass is the sum over its three pairs: `m_p = S_uu + 2·S_ud`,
`m_n = 2·S_ud + S_dd`.

This file proves what that formula determines, and nothing more:

1. `neutron_sub_proton` — the exact splitting identity
   `m_n − m_p = κ · (μ_d − μ_u)`, `κ = w₊ + w₋ = (q⁴ + 1)/(q(q² + 1))`.
2. `det_eq` — the 2×2 map `(μ_u, μ_d) ↦ (m_p, m_n)` has determinant `3κ²`.
3. `up_eq`, `down_eq`, `injective`, `surjective` — when `κ ≠ 0` and `3 ≠ 0`
   the map is a bijection with explicit inverse. So every pair `(m_p, m_n)` is
   reproduced by exactly one pair of dressed quark masses: reproducing
   measured nucleon masses this way is a change of variables and carries no
   predictive content.

No numerical value of `q` and no measured mass appears here.

**Base ring (§7c).** A generic field `K`. No square root appears.

**Convention.** Convention D (owner ruling 2026-11-27, Carl: *"Derive the
convention D. Formula. Go ahead and migrate the convention D"*). The
convention-C form, with denominator `q^{1/2} + q^{-1/2}`, is retired. The
bijection argument is unchanged in shape: the determinant is `3κ²` in both
conventions, with `κ` the sum of the two crossing weights.

-- Ref: [leitner2026] mass-theory, `lem:pair-skein-mass-formula`
-/

namespace QOU.MassTheory.PairSkeinNucleon

open QOU.MassTheory.PairSkeinD

variable {K : Type*} [Field K]

/-- Crossing-pair mass `S_ab`, the convention-D Markov trace. -/
def pairSkein (q a b : K) : K := pairMassD q a b

/-- Proton mass `S_uu + 2·S_ud` under the pair Skein formula. -/
def protonMass (q u d : K) : K := pairSkein q u u + 2 * pairSkein q u d

/-- Neutron mass `2·S_ud + S_dd` under the pair Skein formula. -/
def neutronMass (q u d : K) : K := 2 * pairSkein q u d + pairSkein q d d

/-- The positive-crossing weight `w₊ = z_D`. -/
def wPos (q : K) : K := zD q

/-- The negative-crossing weight `w₋ = z_D − h`. -/
def wNeg (q : K) : K := zD q - hD q

theorem kappaD_eq_wPos_add_wNeg (q : K) : kappaD q = wPos q + wNeg q := by
  rw [kappaD_eq]; unfold wPos wNeg; ring

/-- **Splitting identity.** `m_n − m_p = κ·(μ_d − μ_u)`. Holds with no
hypothesis. -/
theorem neutron_sub_proton (q u d : K) :
    neutronMass q u d - protonMass q u d = kappaD q * (d - u) := by
  unfold neutronMass protonMass pairSkein
  rw [pairMassD_eq, pairMassD_eq, pairMassD_eq, kappaD_eq]
  ring

/-- **Linear form of the proton mass.** `m_p = (3w₊ + w₋)·μ_u + 2w₋·μ_d`. -/
theorem proton_linear (q u d : K) :
    protonMass q u d = (3 * wPos q + wNeg q) * u + 2 * wNeg q * d := by
  unfold protonMass pairSkein wPos wNeg
  rw [pairMassD_eq, pairMassD_eq]
  ring

/-- **Linear form of the neutron mass.** `m_n = 2w₊·μ_u + (w₊ + 3w₋)·μ_d`. -/
theorem neutron_linear (q u d : K) :
    neutronMass q u d = 2 * wPos q * u + (wPos q + 3 * wNeg q) * d := by
  unfold neutronMass pairSkein wPos wNeg
  rw [pairMassD_eq, pairMassD_eq]
  ring

/-- **Determinant.** `(3w₊ + w₋)(w₊ + 3w₋) − (2w₋)(2w₊) = 3(w₊ + w₋)²`. -/
theorem det_eq (a b : K) :
    (3 * a + b) * (a + 3 * b) - (2 * b) * (2 * a) = 3 * (a + b) ^ 2 := by
  ring

/-- `κ ≠ 0` whenever `q ≠ 0`, `q² + 1 ≠ 0` and `q⁴ + 1 ≠ 0`. -/
theorem kappaD_ne_zero (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + 1 ≠ 0) : kappaD q ≠ 0 := by
  rw [kappaD_closed q hq hq2]
  exact div_ne_zero hq4 (mul_ne_zero hq hq2)

/-- **Inverse, up quark.** When `κ ≠ 0` and `3 ≠ 0`, `μ_u` is recovered from
`(m_p, m_n)`. -/
theorem up_eq (q u d : K) (hκ : kappaD q ≠ 0) (h3 : (3 : K) ≠ 0) :
    u = ((wPos q + 3 * wNeg q) * protonMass q u d
          - 2 * wNeg q * neutronMass q u d) / (3 * kappaD q ^ 2) := by
  have hden : 3 * kappaD q ^ 2 ≠ 0 := mul_ne_zero h3 (pow_ne_zero 2 hκ)
  rw [eq_div_iff hden, proton_linear, neutron_linear, kappaD_eq_wPos_add_wNeg]
  ring

/-- **Inverse, down quark.** -/
theorem down_eq (q u d : K) (hκ : kappaD q ≠ 0) (h3 : (3 : K) ≠ 0) :
    d = ((3 * wPos q + wNeg q) * neutronMass q u d
          - 2 * wPos q * protonMass q u d) / (3 * kappaD q ^ 2) := by
  have hden : 3 * kappaD q ^ 2 ≠ 0 := mul_ne_zero h3 (pow_ne_zero 2 hκ)
  rw [eq_div_iff hden, proton_linear, neutron_linear, kappaD_eq_wPos_add_wNeg]
  ring

/-- **The nucleon map is injective.** Two dressed-quark pairs giving the same
`(m_p, m_n)` are equal. -/
theorem injective (q u d u' d' : K) (hκ : kappaD q ≠ 0) (h3 : (3 : K) ≠ 0)
    (hp : protonMass q u d = protonMass q u' d')
    (hn : neutronMass q u d = neutronMass q u' d') :
    u = u' ∧ d = d' := by
  constructor
  · rw [up_eq q u d hκ h3, up_eq q u' d' hκ h3, hp, hn]
  · rw [down_eq q u d hκ h3, down_eq q u' d' hκ h3, hp, hn]

/-- **The nucleon map is surjective.** Every pair `(P, N)` is `(m_p, m_n)` for
the dressed-quark pair given by the inverse formulas. -/
theorem surjective (q P N : K) (hκ : kappaD q ≠ 0) (h3 : (3 : K) ≠ 0) :
    ∃ u d : K, protonMass q u d = P ∧ neutronMass q u d = N := by
  have hab : wPos q + wNeg q ≠ 0 := by rwa [← kappaD_eq_wPos_add_wNeg]
  refine ⟨((wPos q + 3 * wNeg q) * P - 2 * wNeg q * N) / (3 * (wPos q + wNeg q) ^ 2),
    ((3 * wPos q + wNeg q) * N - 2 * wPos q * P) / (3 * (wPos q + wNeg q) ^ 2), ?_, ?_⟩
  · rw [proton_linear]; field_simp; ring
  · rw [neutron_linear]; field_simp; ring

/-- **Terminal resolution, bundled.** The splitting identity, injectivity and
surjectivity of the nucleon map under the convention-D pair Skein formula. -/
theorem terminal_resolution (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + 1 ≠ 0) (h3 : (3 : K) ≠ 0) :
    (∀ u d : K, neutronMass q u d - protonMass q u d = kappaD q * (d - u)) ∧
    (∀ u d u' d' : K, protonMass q u d = protonMass q u' d' →
        neutronMass q u d = neutronMass q u' d' → u = u' ∧ d = d') ∧
    (∀ P N : K, ∃ u d : K, protonMass q u d = P ∧ neutronMass q u d = N) :=
  have hκ := kappaD_ne_zero q hq hq2 hq4
  ⟨neutron_sub_proton q, fun u d u' d' hp hn => injective q u d u' d' hκ h3 hp hn,
   fun P N => surjective q P N hκ h3⟩

end QOU.MassTheory.PairSkeinNucleon
