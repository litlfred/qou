import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-!
# QOU.MassTheory.PairSkeinNucleon — nucleon masses under the pair Skein formula

LaTeX label: `prop:terminal-resolution`.

The pair Skein formula (`lem:pair-skein-mass-formula`) assigns to an ordered
quark pair `(a, b)` the crossing-pair mass

  `S_ab = (q·μ_a + q⁻¹·μ_b) / (q^{1/2} + q^{-1/2})`,

and a nucleon mass is the sum over its three pairs:
`m_p = S_uu + 2·S_ud`, `m_n = 2·S_ud + S_dd`.

This file proves what that formula determines, and nothing more:

1. `neutron_sub_proton` — the exact splitting identity
   `m_n − m_p = [2]_q · (μ_d − μ_u) / (q^{1/2} + q^{-1/2})`.
2. `det_eq` — the 2×2 map `(μ_u, μ_d) ↦ (m_p, m_n)` has determinant
   `3·[2]_q²` (before the common factor `(q^{1/2}+q^{-1/2})⁻²`).
3. `up_eq`, `down_eq`, `injective`, `surjective` — when `s ≠ 0`,
   `s + s⁻¹ ≠ 0`, `[2]_q ≠ 0` and `3 ≠ 0` the map is a bijection,
   with explicit inverse. So every pair `(m_p, m_n)` is reproduced by exactly
   one pair of dressed quark masses: reproducing measured nucleon masses this
   way is a change of variables and carries no predictive content.

No numerical value of `q` and no measured mass appears here.

**Base ring (§7c).** A generic field `K`. The square root is avoided by
working with `s`, where `q = s²`; so `q^{1/2} + q^{-1/2} = s + s⁻¹`.

**Convention.** The denominator `s + s⁻¹` is the reciprocal of the excised
convention-C Markov weight; the results hold in that frame, as the pair Skein
formula does. Re-deriving the formula under convention D is open.

-- Ref: [leitner2026] mass-theory, `lem:pair-skein-mass-formula`
-/

namespace QOU.MassTheory.PairSkeinNucleon

variable {K : Type*} [Field K]

/-- Crossing-pair mass `S_ab` with `q = s²`. -/
def pairSkein (s a b : K) : K := (s ^ 2 * a + (s ^ 2)⁻¹ * b) / (s + s⁻¹)

/-- Proton mass `S_uu + 2·S_ud` under the pair Skein formula. -/
def protonMass (s u d : K) : K := pairSkein s u u + 2 * pairSkein s u d

/-- Neutron mass `2·S_ud + S_dd` under the pair Skein formula. -/
def neutronMass (s u d : K) : K := 2 * pairSkein s u d + pairSkein s d d

/-- **Splitting identity.** `m_n − m_p = [2]_q·(μ_d − μ_u)/(q^{1/2}+q^{-1/2})`,
with `[2]_q = q + q⁻¹`, `q = s²`. Holds with no hypothesis. -/
theorem neutron_sub_proton (s u d : K) :
    neutronMass s u d - protonMass s u d
      = (s ^ 2 + (s ^ 2)⁻¹) * (d - u) / (s + s⁻¹) := by
  unfold neutronMass protonMass pairSkein
  ring

/-- **Linear form.** `(s + s⁻¹)·m_p = (3q + q⁻¹)·μ_u + 2q⁻¹·μ_d` and
`(s + s⁻¹)·m_n = 2q·μ_u + (q + 3q⁻¹)·μ_d`, given `s + s⁻¹ ≠ 0`. -/
theorem proton_linear (s u d : K) (hD : s + s⁻¹ ≠ 0) :
    (s + s⁻¹) * protonMass s u d
      = (3 * s ^ 2 + (s ^ 2)⁻¹) * u + 2 * (s ^ 2)⁻¹ * d := by
  have h : protonMass s u d
      = ((3 * s ^ 2 + (s ^ 2)⁻¹) * u + 2 * (s ^ 2)⁻¹ * d) / (s + s⁻¹) := by
    unfold protonMass pairSkein
    ring
  rw [h, mul_div_assoc', mul_div_cancel_left₀ _ hD]

theorem neutron_linear (s u d : K) (hD : s + s⁻¹ ≠ 0) :
    (s + s⁻¹) * neutronMass s u d
      = 2 * s ^ 2 * u + (s ^ 2 + 3 * (s ^ 2)⁻¹) * d := by
  have h : neutronMass s u d
      = (2 * s ^ 2 * u + (s ^ 2 + 3 * (s ^ 2)⁻¹) * d) / (s + s⁻¹) := by
    unfold neutronMass pairSkein
    ring
  rw [h, mul_div_assoc', mul_div_cancel_left₀ _ hD]

/-- **Determinant.** `(3q + q⁻¹)(q + 3q⁻¹) − (2q⁻¹)(2q) = 3·[2]_q²`, for `q ≠ 0`. -/
theorem det_eq (q : K) (hq : q ≠ 0) :
    (3 * q + q⁻¹) * (q + 3 * q⁻¹) - (2 * q⁻¹) * (2 * q)
      = 3 * (q + q⁻¹) ^ 2 := by
  field_simp
  ring

/-- **Inverse, up quark.** When `s ≠ 0`, `s + s⁻¹ ≠ 0`, `[2]_q ≠ 0` and `3 ≠ 0`,
`μ_u` is recovered from `(m_p, m_n)`. -/
theorem up_eq (s u d : K) (hs : s ≠ 0) (hD : s + s⁻¹ ≠ 0)
    (h2 : s ^ 2 + (s ^ 2)⁻¹ ≠ 0) (h3 : (3 : K) ≠ 0) :
    u = (s + s⁻¹) * ((s ^ 2 + 3 * (s ^ 2)⁻¹) * protonMass s u d
          - 2 * (s ^ 2)⁻¹ * neutronMass s u d)
        / (3 * (s ^ 2 + (s ^ 2)⁻¹) ^ 2) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hP := proton_linear s u d hD
  have hN := neutron_linear s u d hD
  have hden : 3 * (s ^ 2 + (s ^ 2)⁻¹) ^ 2 ≠ 0 := mul_ne_zero h3 (pow_ne_zero 2 h2)
  rw [eq_div_iff hden]
  have e1 : (s + s⁻¹) * ((s ^ 2 + 3 * (s ^ 2)⁻¹) * protonMass s u d
          - 2 * (s ^ 2)⁻¹ * neutronMass s u d)
        = (s ^ 2 + 3 * (s ^ 2)⁻¹) * ((s + s⁻¹) * protonMass s u d)
          - 2 * (s ^ 2)⁻¹ * ((s + s⁻¹) * neutronMass s u d) := by ring
  rw [e1, hP, hN]
  have hdet := det_eq (s ^ 2) hq
  linear_combination (-u) * hdet

/-- **Inverse, down quark.** -/
theorem down_eq (s u d : K) (hs : s ≠ 0) (hD : s + s⁻¹ ≠ 0)
    (h2 : s ^ 2 + (s ^ 2)⁻¹ ≠ 0) (h3 : (3 : K) ≠ 0) :
    d = (s + s⁻¹) * ((3 * s ^ 2 + (s ^ 2)⁻¹) * neutronMass s u d
          - 2 * s ^ 2 * protonMass s u d)
        / (3 * (s ^ 2 + (s ^ 2)⁻¹) ^ 2) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hP := proton_linear s u d hD
  have hN := neutron_linear s u d hD
  have hden : 3 * (s ^ 2 + (s ^ 2)⁻¹) ^ 2 ≠ 0 := mul_ne_zero h3 (pow_ne_zero 2 h2)
  rw [eq_div_iff hden]
  have e1 : (s + s⁻¹) * ((3 * s ^ 2 + (s ^ 2)⁻¹) * neutronMass s u d
          - 2 * s ^ 2 * protonMass s u d)
        = (3 * s ^ 2 + (s ^ 2)⁻¹) * ((s + s⁻¹) * neutronMass s u d)
          - 2 * s ^ 2 * ((s + s⁻¹) * protonMass s u d) := by ring
  rw [e1, hP, hN]
  have hdet := det_eq (s ^ 2) hq
  linear_combination (-d) * hdet

/-- **The nucleon map is injective.** Two dressed-quark pairs giving the same
`(m_p, m_n)` are equal. Hence the pair Skein formula reproduces any measured
`(m_p, m_n)` with exactly one `(μ_u, μ_d)`. -/
theorem injective (s u d u' d' : K) (hs : s ≠ 0) (hD : s + s⁻¹ ≠ 0)
    (h2 : s ^ 2 + (s ^ 2)⁻¹ ≠ 0) (h3 : (3 : K) ≠ 0)
    (hp : protonMass s u d = protonMass s u' d')
    (hn : neutronMass s u d = neutronMass s u' d') :
    u = u' ∧ d = d' := by
  constructor
  · rw [up_eq s u d hs hD h2 h3, up_eq s u' d' hs hD h2 h3, hp, hn]
  · rw [down_eq s u d hs hD h2 h3, down_eq s u' d' hs hD h2 h3, hp, hn]

/-- **The nucleon map is surjective.** Every pair `(P, N)` is `(m_p, m_n)` for
the dressed-quark pair given by the inverse formulas. -/
theorem surjective (s P N : K) (hs : s ≠ 0) (hD : s + s⁻¹ ≠ 0)
    (h2 : s ^ 2 + (s ^ 2)⁻¹ ≠ 0) (h3 : (3 : K) ≠ 0) :
    ∃ u d : K, protonMass s u d = P ∧ neutronMass s u d = N := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hden : 3 * (s ^ 2 + (s ^ 2)⁻¹) ^ 2 ≠ 0 := mul_ne_zero h3 (pow_ne_zero 2 h2)
  have hdet := det_eq (s ^ 2) hq
  set Δ := 3 * (s ^ 2 + (s ^ 2)⁻¹) ^ 2 with hΔ
  refine ⟨(s + s⁻¹) * ((s ^ 2 + 3 * (s ^ 2)⁻¹) * P - 2 * (s ^ 2)⁻¹ * N) / Δ,
    (s + s⁻¹) * ((3 * s ^ 2 + (s ^ 2)⁻¹) * N - 2 * s ^ 2 * P) / Δ, ?_, ?_⟩
  · have h : protonMass s
        ((s + s⁻¹) * ((s ^ 2 + 3 * (s ^ 2)⁻¹) * P - 2 * (s ^ 2)⁻¹ * N) / Δ)
        ((s + s⁻¹) * ((3 * s ^ 2 + (s ^ 2)⁻¹) * N - 2 * s ^ 2 * P) / Δ)
        = P * (((3 * s ^ 2 + (s ^ 2)⁻¹) * (s ^ 2 + 3 * (s ^ 2)⁻¹)
            - 2 * (s ^ 2)⁻¹ * (2 * s ^ 2)) / Δ) := by
      have hl : protonMass s ((s + s⁻¹) * ((s ^ 2 + 3 * (s ^ 2)⁻¹) * P - 2 * (s ^ 2)⁻¹ * N) / Δ)
          ((s + s⁻¹) * ((3 * s ^ 2 + (s ^ 2)⁻¹) * N - 2 * s ^ 2 * P) / Δ)
          = (s + s⁻¹) * (P * (((3 * s ^ 2 + (s ^ 2)⁻¹) * (s ^ 2 + 3 * (s ^ 2)⁻¹)
            - 2 * (s ^ 2)⁻¹ * (2 * s ^ 2)) / Δ)) / (s + s⁻¹) := by
        unfold protonMass pairSkein
        ring
      rw [hl, mul_div_cancel_left₀ _ hD]
    rw [h, hdet, div_self hden, mul_one]
  · have h : neutronMass s
        ((s + s⁻¹) * ((s ^ 2 + 3 * (s ^ 2)⁻¹) * P - 2 * (s ^ 2)⁻¹ * N) / Δ)
        ((s + s⁻¹) * ((3 * s ^ 2 + (s ^ 2)⁻¹) * N - 2 * s ^ 2 * P) / Δ)
        = N * (((3 * s ^ 2 + (s ^ 2)⁻¹) * (s ^ 2 + 3 * (s ^ 2)⁻¹)
            - 2 * (s ^ 2)⁻¹ * (2 * s ^ 2)) / Δ) := by
      have hl : neutronMass s ((s + s⁻¹) * ((s ^ 2 + 3 * (s ^ 2)⁻¹) * P - 2 * (s ^ 2)⁻¹ * N) / Δ)
          ((s + s⁻¹) * ((3 * s ^ 2 + (s ^ 2)⁻¹) * N - 2 * s ^ 2 * P) / Δ)
          = (s + s⁻¹) * (N * (((3 * s ^ 2 + (s ^ 2)⁻¹) * (s ^ 2 + 3 * (s ^ 2)⁻¹)
            - 2 * (s ^ 2)⁻¹ * (2 * s ^ 2)) / Δ)) / (s + s⁻¹) := by
        unfold neutronMass pairSkein
        ring
      rw [hl, mul_div_cancel_left₀ _ hD]
    rw [h, hdet, div_self hden, mul_one]

/-- **Statement of `prop:terminal-resolution`.** The splitting identity holds,
and the nucleon map is a bijection (injective and surjective). -/
theorem terminal_resolution (s : K) (hs : s ≠ 0) (hD : s + s⁻¹ ≠ 0)
    (h2 : s ^ 2 + (s ^ 2)⁻¹ ≠ 0) (h3 : (3 : K) ≠ 0) :
    (∀ u d : K, neutronMass s u d - protonMass s u d
        = (s ^ 2 + (s ^ 2)⁻¹) * (d - u) / (s + s⁻¹)) ∧
    (∀ u d u' d' : K, protonMass s u d = protonMass s u' d' →
        neutronMass s u d = neutronMass s u' d' → u = u' ∧ d = d') ∧
    (∀ P N : K, ∃ u d : K, protonMass s u d = P ∧ neutronMass s u d = N) :=
  ⟨neutron_sub_proton s, fun u d u' d' hp hn =>
    injective s u d u' d' hs hD h2 h3 hp hn,
   fun P N => surjective s P N hs hD h2 h3⟩

end QOU.MassTheory.PairSkeinNucleon
