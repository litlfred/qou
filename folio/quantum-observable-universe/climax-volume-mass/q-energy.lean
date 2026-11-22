import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.Real.Basic


/-!
# QOU.Archimedean.QEnergy — q-Energy from angular momentum + momentum + action

The q-energy of a particle knot is the sum of three terms,

  `E_q = J_q² · ℏ_q + p_q² · ℏ_q / (2 [n]_q) + S_q`,

where `S_q` is the categorical action (rest-mass energy).

LaTeX label: `def:q-energy`

## References
- [leitner2026] §6/q-energy

**Ground ring (AGENTS.md §7c).** Every term above is a ring operation plus
division, so the whole construction — carrier, total, and the rest-energy
theorem — is stated over a generic `{R : Type*} [Field R]`, with the
q-number carried as *data* on the structure. Only two facts need `ℝ`: the
real-exponent bracket `[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)`, where `q ^ n` at a real
`n` is `Real.rpow`, and the crossing-energy asymmetry, which is an ordering
statement. Both sit below the substrate→archimedean wall and say `ℝ`.

This file previously opened with `abbrev R_q := ℝ`,
`def q_param : R_q := 1.1097` and `def hbarQ_q (q : R_q) : R_q`, all inside
`namespace QOU.Archimedean`, where `R_q` canonically means
`LaurentPolynomial ℤ`, `q_param` the indeterminate `T 1`, and `hbarQ_q` the
element `1 - q_inv` of that ring (`QOU/Archimedean/GroundRing.lean`,
`QOU/Archimedean/ParticleKnots.lean`). Three names, each meaning two
different things depending on which copy a reader or a checker reached. The
helpers now live in the block's own `QEnergy` namespace, which cannot
collide with the library's (bean `qou-u87j`).
-/

namespace QOU.Archimedean

/-- **q-Energy of a particle knot**: rotational + translational + rest mass.

The q-number is a *field* rather than a fixed function, which is what keeps
the structure generic — `total` below is the same expression whichever
bracket the instance supplies. -/
structure QEnergy (R : Type*) [Field R] where
  /-- The q-number `[·]_q` this instance is built over. -/
  qNumber : R → R → R
  /-- Substrate parameter. -/
  q : R
  /-- Spin quantum number `j`. -/
  j : R
  /-- q-momentum (writhe-derived). -/
  p_q : R
  /-- Number of strands in the braid representative. -/
  n_strands : R
  /-- Categorical action `S_q` (rest-mass energy). -/
  S_q : R

namespace QEnergy

variable {R : Type*} [Field R]

/-- `ℏ_q = 1 - q⁻¹`, the quantum Planck constant, over any field.

Distinct from the library's `QOU.Archimedean.hbarQ_q`, which is the *element*
`1 - q_inv` of the Laurent ground ring rather than this function of `q`. -/
-- Ref: [leitner2026] §6/q-energy
def hbarQ (q : R) : R := 1 - q⁻¹

/-- The crossing energy at a single positive crossing. -/
-- Ref: [leitner2026] §6/q-energy
def crossingEnergyPos (q : R) : R := q

/-- The crossing energy at a single negative crossing. -/
-- Ref: [leitner2026] §6/q-energy
def crossingEnergyNeg (q : R) : R := 1 / q

/-- The total q-energy: rotational `[j]_q [j+1]_q ℏ_q`, translational
`p_q² ℏ_q / (2 [n]_q)`, and the action `S_q`. -/
-- Ref: [leitner2026] §6/q-energy
def total (E : QEnergy R) : R :=
  E.qNumber E.q E.j * E.qNumber E.q (E.j + 1) * hbarQ E.q
  + E.p_q ^ 2 * hbarQ E.q / (2 * E.qNumber E.q E.n_strands)
  + E.S_q

/-- **At rest the q-energy is the action.** With `j = 0` the rotational term
carries `[0]_q = 0` and with `p_q = 0` the translational term vanishes,
leaving `S_q`.

The only hypothesis is that the bracket kills `0`; no ordering, no
exponentiation, no archimedean structure. Note the translational term needs
no non-vanishing side condition on `[n]_q`, because `0 / x = 0` holds in any
`DivisionRing` including at `x = 0`. -/
-- Ref: [leitner2026] §6/q-energy
theorem total_rest (qn : R → R → R) (h : ∀ q, qn q 0 = 0) (q S : R) :
    (QEnergy.mk qn q 0 0 1 S).total = S := by
  unfold total
  simp [h]

/-! ### Archimedean specialisation

Below the substrate→archimedean wall: a real exponent is `Real.rpow`, and an
asymmetry is an ordering claim. -/

/-- The q-number `[n]_q = (qⁿ - q⁻ⁿ)/(q - q⁻¹)` at **real** exponents. -/
-- Ref: [leitner2026] §6/q-energy
noncomputable def qNumberReal (q n : ℝ) : ℝ :=
  (q ^ n - q ^ (-n)) / (q - q ^ (-(1 : ℝ)))

/-- `[0]_q = 0`, the hypothesis `total_rest` asks for, discharged at `ℝ`. -/
-- Ref: [leitner2026] §6/q-energy
theorem qNumberReal_zero (q : ℝ) : qNumberReal q 0 = 0 := by
  unfold qNumberReal
  simp

/-- The real q-energy at rest is its action — `total_rest` instantiated. -/
-- Ref: [leitner2026] §6/q-energy
theorem total_rest_real (q S : ℝ) :
    (QEnergy.mk qNumberReal q 0 0 1 S).total = S :=
  total_rest qNumberReal qNumberReal_zero q S

/-- Positive crossings carry more energy than negative at `q > 1`.

An ordering statement, so `ℝ`: it is false over a generic field, which has
no order to state it in. -/
-- Ref: [leitner2026] §6/q-energy
theorem crossingEnergyNeg_lt_pos {q : ℝ} (hq : 1 < q) :
    crossingEnergyNeg q < crossingEnergyPos q := by
  unfold crossingEnergyPos crossingEnergyNeg
  rw [div_lt_iff₀ (by linarith : (0 : ℝ) < q)]
  nlinarith

/-- **Q-Deformed Energy**: a rest-mass-nonnegative configuration exists. -/
-- Ref: [leitner2026] def:q-energy
theorem exists_nonneg_action : ∃ E : QEnergy ℝ, E.S_q ≥ 0 :=
  ⟨QEnergy.mk qNumberReal 1.1097 0 0 1 0, le_refl 0⟩

end QEnergy

end QOU.Archimedean
