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
convention-C Markov weight; the results above hold in that frame, as the pair
Skein formula does. The section `ConventionD` below re-derives the map in the
canonical frame `z = q³/(q²+1)`; see its own docstring for what is derived
there and what is still a reading.

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

/-! ## Convention D

This section re-derives the pair Skein map in the canonical frame. Throughout,
`q` is the Hecke parameter of `σᵢ² = (q − q⁻¹)σᵢ + 1` and `z` is the
convention-D Markov parameter, given as the hypothesis `z·(q² + 1) = q³`
(the same predicate as `QOU.QBeta.TemperleyLiebTower.IsConventionD`).

**What the convention-C formula is made of.** Read in its own frame, where the
Hecke parameter is `s = q^{1/2}`, the formula `𝒮_ab = (s²μ_a + s⁻²μ_b)/(s + s⁻¹)`
has two parts:

* the weights `s^{±2}` are the coefficients of the Jones skein relation in
  that frame, `s²·X(L₊) − s⁻²·X(L₋) = (s − s⁻¹)·X(L₀)`, which is the relation
  `QOU.HadronicMass.SkeinMassRelation` records;
* the normaliser `1/(s + s⁻¹)` is the Temperley–Lieb loop reciprocal `1/δ` in
  that frame, i.e. the trace of the TL generator `e`, not of `σ`
  (trace-convention registry, §"Two cautions", item 2).

**What is derived here, in the canonical frame.**

* `trE_conventionD`: `(q − z)(q + q⁻¹) = 1`. Since `e = q − σ`, the trace of
  `e` is `q − z = 1/[2]_q`, the loop reciprocal. This is the convention-D
  normaliser. In particular `[2]_q ≠ 0` follows from the hypothesis.
* `markovII_ratio`, `writheFactor_sq`, `writheFactor_eq`: the two Markov-II
  conditions (stabilising by `σ` and by `σ⁻¹`) force the writhe factor `c` to
  satisfy `c² = q⁻⁴`, so `c = ±q⁻²`. The skein relation of `X = c^{writhe}·tr`
  is then `c⁻¹·X(L₊) − c·X(L₋) = (q − q⁻¹)·X(L₀)`, with weights `±q^{±2}`.
  So the convention-D skein weights are `q^{±2}`, not `q^{±1}`.
* `pairSkeinD_eq`: with those two ingredients,
  `𝒮ᴰ_ab = (q − z)·(q²μ_a + q⁻²μ_b) = (q²μ_a + q⁻²μ_b)/(q + q⁻¹)`,
  which is `pairSkein` with `s := q`. So every theorem above transfers, and
  `terminal_resolution_conventionD` restates them.

**What is not derived.** That a crossing pair contributes
`(trace of e) × (skein-weighted dressed masses)` is the reading of the
convention-C formula, not a theorem: nothing here builds the Borromean braid
or a mass functional on it, and the convention-C proof does not derive its
denominator either. Two choices inside the reading are named, not hidden:

* the sign branch `c = +q⁻²` (the `−q⁻²` branch flips the sign of every
  `𝒮_ab`);
* the normaliser is the trace of `e`, not `z` itself. Using `z` would multiply
  every `𝒮_ab` by `q²` (`z_eq_sq_mul_trE`). The registry identifies attaching
  the loop reciprocal to `σ` as the convention-C defect, which is why `e` is
  used here.

Both choices are then fixed by the two structural tests the corpus already
applies to this normaliser (#6820 / #6823): bar-covariance
`𝒮_ab(q⁻¹) = 𝒮_ba(q)` holds for the chosen form (`pairSkein_bar`) and fails
for the `z`-normalised one unless `q⁴ = 1` (`zNormalised_bar_forces`); the
classical limit `𝒮_aa(1) = μ_a` holds on the `+` branch
(`pairSkein_classical`) and fails on the `−` branch
(`minusBranch_classical`). Those tests are corpus criteria, not theorems about
a mass functional. Either alternative would rescale all `𝒮_ab` by one common
nonzero factor, so the bijection (hence the "change of variables, no
prediction" conclusion) would be unchanged in any case.

No numerical value of `q` and no measured mass appears here.
-/

section ConventionD

/-- **Trace of the TL generator under convention D.** `(q − z)·[2]_q = 1`.
Mirror of `QOU.QBeta.TemperleyLiebTower.loop_reciprocal`, restated here so this
file keeps Mathlib-only imports. -/
theorem trE_conventionD (q z : K) (hq : q ≠ 0) (hD : z * (q ^ 2 + 1) = q ^ 3) :
    (q - z) * (q + q⁻¹) = 1 := by
  field_simp
  linear_combination -hD

/-- `[2]_q ≠ 0` is a consequence of convention D, not an extra hypothesis. -/
theorem two_ne_zero_conventionD (q z : K) (hq : q ≠ 0)
    (hD : z * (q ^ 2 + 1) = q ^ 3) : q + q⁻¹ ≠ 0 :=
  right_ne_zero_of_mul_eq_one (trE_conventionD q z hq hD)

/-- `z ≠ 0` under convention D. -/
theorem z_ne_zero_conventionD (q z : K) (hq : q ≠ 0)
    (hD : z * (q ^ 2 + 1) = q ^ 3) : z ≠ 0 := by
  rintro rfl
  have h3 : q ^ 3 = 0 := by rw [← hD]; ring
  exact pow_ne_zero 3 hq h3

/-- **The `σ⁻¹` trace against the `σ` trace.** Under convention D,
`tr(x·σ⁻¹)/tr(x) = z − (q − q⁻¹) = q⁻⁴·z`. -/
theorem markovII_ratio (q z : K) (hq : q ≠ 0) (hD : z * (q ^ 2 + 1) = q ^ 3) :
    z - (q - q⁻¹) = ((q ^ 2)⁻¹) ^ 2 * z := by
  field_simp
  linear_combination (q ^ 2 - 1) * hD

/-- **Markov II forces the writhe factor.** If `X = c^{writhe}·D^{n-1}·tr` is
invariant under stabilisation by `σ` (`c·D·z = 1`) and by `σ⁻¹`
(`c⁻¹·D·(z − (q − q⁻¹)) = 1`), then `c² = q⁻⁴`. -/
theorem writheFactor_sq (q z c D : K) (hq : q ≠ 0)
    (hD : z * (q ^ 2 + 1) = q ^ 3)
    (hplus : c * D * z = 1) (hminus : c⁻¹ * D * (z - (q - q⁻¹)) = 1) :
    c ^ 2 = ((q ^ 2)⁻¹) ^ 2 := by
  have hc : c ≠ 0 := by
    rintro rfl
    simp at hplus
  rw [markovII_ratio q z hq hD] at hminus
  have hDz : D * z = c⁻¹ :=
    eq_inv_of_mul_eq_one_left (by linear_combination hplus)
  have h : c⁻¹ * ((q ^ 2)⁻¹) ^ 2 * (D * z) = 1 := by
    rw [← hminus]; ring
  rw [hDz] at h
  field_simp at h
  field_simp
  linear_combination -h

/-- **The writhe factor is `±q⁻²`.** -/
theorem writheFactor_eq (q z c D : K) (hq : q ≠ 0)
    (hD : z * (q ^ 2 + 1) = q ^ 3)
    (hplus : c * D * z = 1) (hminus : c⁻¹ * D * (z - (q - q⁻¹)) = 1) :
    c = (q ^ 2)⁻¹ ∨ c = -(q ^ 2)⁻¹ :=
  sq_eq_sq_iff_eq_or_eq_neg.mp (writheFactor_sq q z c D hq hD hplus hminus)

/-- **Skein weights on the `+` branch.** With `c = q⁻²`, the skein relation
`c⁻¹·X(L₊) − c·X(L₋) = (q − q⁻¹)·X(L₀)` has weights `(q², q⁻²)`. -/
theorem skeinWeights_plus (q : K) :
    ((q ^ 2)⁻¹)⁻¹ = q ^ 2 := inv_inv _

/-- **`z` itself is `q²` times the trace of `e`.** Using `z` as the normaliser
instead of `q − z` would rescale every `𝒮_ab` by `q²`. -/
theorem z_eq_sq_mul_trE (q z : K) (hD : z * (q ^ 2 + 1) = q ^ 3) :
    z = q ^ 2 * (q - z) := by
  linear_combination hD

/-- **Convention-D pair Skein mass**: trace of `e` times the skein-weighted
dressed masses, `𝒮ᴰ_ab = (q − z)·(q²·μ_a + q⁻²·μ_b)`. -/
def pairSkeinD (q z a b : K) : K := (q - z) * (q ^ 2 * a + (q ^ 2)⁻¹ * b)

/-- Proton mass `𝒮ᴰ_uu + 2·𝒮ᴰ_ud`. -/
def protonMassD (q z u d : K) : K := pairSkeinD q z u u + 2 * pairSkeinD q z u d

/-- Neutron mass `2·𝒮ᴰ_ud + 𝒮ᴰ_dd`. -/
def neutronMassD (q z u d : K) : K := 2 * pairSkeinD q z u d + pairSkeinD q z d d

/-- **The convention-D map is the convention-C map at `s := q`.**
`𝒮ᴰ_ab = (q²μ_a + q⁻²μ_b)/(q + q⁻¹)`. -/
theorem pairSkeinD_eq (q z a b : K) (hq : q ≠ 0) (hD : z * (q ^ 2 + 1) = q ^ 3) :
    pairSkeinD q z a b = pairSkein q a b := by
  have h := trE_conventionD q z hq hD
  have h2 := two_ne_zero_conventionD q z hq hD
  have hz : q - z = (q + q⁻¹)⁻¹ := eq_inv_of_mul_eq_one_left h
  unfold pairSkeinD pairSkein
  rw [hz, div_eq_inv_mul]

theorem protonMassD_eq (q z u d : K) (hq : q ≠ 0) (hD : z * (q ^ 2 + 1) = q ^ 3) :
    protonMassD q z u d = protonMass q u d := by
  unfold protonMassD protonMass
  simp only [pairSkeinD_eq q z _ _ hq hD]

theorem neutronMassD_eq (q z u d : K) (hq : q ≠ 0) (hD : z * (q ^ 2 + 1) = q ^ 3) :
    neutronMassD q z u d = neutronMass q u d := by
  unfold neutronMassD neutronMass
  simp only [pairSkeinD_eq q z _ _ hq hD]

/-- **Splitting identity, convention D.**
`m_n − m_p = (q − z)·(q² + q⁻²)·(μ_d − μ_u) = ([4]_q/[2]_q²)·(μ_d − μ_u)`. -/
theorem neutron_sub_proton_conventionD (q z u d : K) :
    neutronMassD q z u d - protonMassD q z u d
      = (q - z) * (q ^ 2 + (q ^ 2)⁻¹) * (d - u) := by
  unfold neutronMassD protonMassD pairSkeinD
  ring

/-- **Determinant, convention D.** The linear map `(μ_u, μ_d) ↦ (m_p, m_n)` has
matrix `(q − z)·[[3q² + q⁻², 2q⁻²], [2q², q² + 3q⁻²]]`, with determinant
`(q − z)²·3·(q² + q⁻²)²`. -/
theorem det_conventionD (q z : K) (hq : q ≠ 0) :
    ((q - z) * (3 * q ^ 2 + (q ^ 2)⁻¹)) * ((q - z) * (q ^ 2 + 3 * (q ^ 2)⁻¹))
      - ((q - z) * (2 * (q ^ 2)⁻¹)) * ((q - z) * (2 * q ^ 2))
      = (q - z) ^ 2 * (3 * (q ^ 2 + (q ^ 2)⁻¹) ^ 2) := by
  have := det_eq (q ^ 2) (pow_ne_zero 2 hq)
  linear_combination (q - z) ^ 2 * this

/-! ### The two named choices are fixed by bar-covariance and the classical limit

The corpus already holds two structural tests for a pair Skein normaliser
(issue #6820, settled on PR #6823, probe
`computations/qbeta/pair_skein_mass_bar_parity_probe.py`):

* **bar-covariance**: `q ↦ q⁻¹` should exchange the two constituents,
  `𝒮_ab(q⁻¹) = 𝒮_ba(q)`;
* **classical limit**: at `q = 1`, `𝒮_aa = μ_a`.

The three lemmas below show these tests select the `+` branch with the
`e`-normaliser, and reject both alternatives. -/

/-- **Bar-covariance of the convention-D pair Skein mass.** Holds with no
hypothesis. -/
theorem pairSkein_bar (q a b : K) : pairSkein q⁻¹ a b = pairSkein q b a := by
  unfold pairSkein
  rw [inv_inv, inv_pow, inv_inv]
  ring

/-- **The `z`-normalised alternative is not bar-covariant.** If
`q²·𝒮(q)` (the result of using `z = q²·(q − z)` as the normaliser) were
bar-covariant on the pair `(μ_a, μ_b) = (1, 0)`, then `q⁴ = 1`. -/
theorem zNormalised_bar_forces (q : K) (hq : q ≠ 0) (h2 : q + q⁻¹ ≠ 0)
    (hbar : (q⁻¹) ^ 2 * pairSkein q⁻¹ 1 0 = q ^ 2 * pairSkein q 0 1) :
    q ^ 4 = 1 := by
  rw [pairSkein_bar] at hbar
  have hS : pairSkein q 0 1 ≠ 0 := by
    unfold pairSkein
    simp only [mul_zero, zero_add, mul_one]
    exact div_ne_zero (inv_ne_zero (pow_ne_zero 2 hq)) h2
  have h := mul_right_cancel₀ hS hbar
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  field_simp at h
  linear_combination -h

/-- **Classical limit, `+` branch.** At `q = 1`, `𝒮_aa = μ_a`. -/
theorem pairSkein_classical (a : K) (h2 : (2 : K) ≠ 0) : pairSkein (1 : K) a a = a := by
  unfold pairSkein
  norm_num
  field_simp
  ring

/-- **Classical limit, `−` branch.** The `c = −q⁻²` branch negates every
`𝒮_ab`, so at `q = 1` it gives `𝒮_aa = −μ_a`, which equals `μ_a` only for
`μ_a = 0` (characteristic not `2`). -/
theorem minusBranch_classical (a : K) (h2 : (2 : K) ≠ 0)
    (h : -pairSkein (1 : K) a a = a) : a = 0 := by
  rw [pairSkein_classical a h2] at h
  have : (2 : K) * a = 0 := by linear_combination -h
  exact (mul_eq_zero.mp this).resolve_left h2

/-- **Orientation caveat (PR #8904, audit §20).** `protonMassD` and
`neutronMassD` put `u` before `d` in every mixed pair, so they are not
invariant under relabelling the three strands. The symmetrised pair mass
`(𝒮_ab + 𝒮_ba)/2 = (q − z)(q² + q⁻²)(μ_a + μ_b)/2` gives the same splitting
coefficient, so part (i) does not depend on that choice. -/
theorem neutron_sub_proton_symmetrised (q z u d : K) (h2 : (2 : K) ≠ 0) :
    let S : K → K → K := fun a b => (pairSkeinD q z a b + pairSkeinD q z b a) / 2
    (2 * S u d + S d d) - (S u u + 2 * S u d)
      = (q - z) * (q ^ 2 + (q ^ 2)⁻¹) * (d - u) := by
  intro S
  simp only [S, pairSkeinD]
  field_simp
  ring

/-- **Statement of `prop:terminal-resolution` in convention D.** Over a field
with `3 ≠ 0`, for `q ≠ 0` with `q² + q⁻² ≠ 0` and `z·(q² + 1) = q³`:
the splitting identity holds, and the nucleon map is a bijection. The
hypothesis `[2]_q ≠ 0` of the convention-C statement is not needed: it follows
from convention D (`two_ne_zero_conventionD`). -/
theorem terminal_resolution_conventionD (q z : K) (hq : q ≠ 0)
    (hD : z * (q ^ 2 + 1) = q ^ 3)
    (h4 : q ^ 2 + (q ^ 2)⁻¹ ≠ 0) (h3 : (3 : K) ≠ 0) :
    (∀ u d : K, neutronMassD q z u d - protonMassD q z u d
        = (q - z) * (q ^ 2 + (q ^ 2)⁻¹) * (d - u)) ∧
    (∀ u d u' d' : K, protonMassD q z u d = protonMassD q z u' d' →
        neutronMassD q z u d = neutronMassD q z u' d' → u = u' ∧ d = d') ∧
    (∀ P N : K, ∃ u d : K, protonMassD q z u d = P ∧ neutronMassD q z u d = N) := by
  have h2 := two_ne_zero_conventionD q z hq hD
  refine ⟨neutron_sub_proton_conventionD q z, ?_, ?_⟩
  · intro u d u' d' hp hn
    rw [protonMassD_eq q z _ _ hq hD, protonMassD_eq q z _ _ hq hD] at hp
    rw [neutronMassD_eq q z _ _ hq hD, neutronMassD_eq q z _ _ hq hD] at hn
    exact injective q u d u' d' hq h2 h4 h3 hp hn
  · intro P N
    obtain ⟨u, d, hp, hn⟩ := surjective q P N hq h2 h4 h3
    exact ⟨u, d, by rw [protonMassD_eq q z _ _ hq hD, hp],
      by rw [neutronMassD_eq q z _ _ hq hD, hn]⟩

end ConventionD

end QOU.MassTheory.PairSkeinNucleon
