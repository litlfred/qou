import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination


/-!
# QOU.BraidKnot.ThreeHalvesStructuralFactor

Lean proofs of the **lepton-tower closure structural identities**
(PR #1127 muon + PR #1253 tau extension).

## Muon (T6 gap (c), PR #1127)

  (3 + h²) / (2 + h²) = [3]_q · [2]_q / [4]_q

Equivalent fundamental identity:
  [4]_q = (2 + h²) · [2]_q

Numerically at q₀ ≈ 1.110, this factor = 1.4893; closes T6 to
0.034 % of CODATA m_μ/m_e.

## Tau (PR #1253 amphichiral probe — candidate 10_43 closure)

  [6]_q = [2]_q · [3]_q · (1 + h²)

This is the structural q-bracket identity for the conjectured
tau-mass closure `ξ_3 = [5]_q · [3]_q / [6]_q` (analog of muon's
`ξ_2 = [3]_q · [2]_q / [4]_q`). Combined with the muon identity,
the lepton-tower closure factors live in a single h-graded family
(see `three_halves_factor_cross_mul` for m=2 and
`bracket6_eq_bracket2_bracket3_times_one_plus_h_sq` for m=3).

Numerically at q₀ ≈ 1.110, the tau form `[5]_q · [3]_q / [6]_q`
applied to `Vol(10_43) / ℏ_q²` closes m_τ/m_e to +0.79% of CODATA
3477.23 — best result for an amphichiral hyperbolic knot under
q-bracket-corrected formulas (PR #1253 witness).

## Conventions

- h = q - q⁻¹ (Hecke amplitude)
- [n]_q = q^(n-1) + q^(n-3) + ... + q^(−(n-1)) (symmetric q-integer)

## Base ring (AGENTS.md §7c)

Every identity below is a **Laurent identity** in `q, q⁻¹`: it needs
`q` to be invertible and nothing else. The declarations therefore live
over a generic `{R : Type*} [CommRing R]` with the substrate modulus
carried as a **unit** `q : Rˣ`, so `↑q⁻¹` is a `Units` coercion rather
than a ring inverse — i.e. they are statements about `ℤ[q, q⁻¹] ⊗ R`
and hold in every commutative ring, in every characteristic, with no
ordering and no division. Each proof is a single `linear_combination`
against `q.mul_inv : ↑q * ↑q⁻¹ = 1`; no `field_simp` is used.

A **field is needed only to write the two ratio presentations**
(`(3+h²)/(2+h²)` and `[5]·[3]/[6]`), because a quotient requires
division. Those live in the `RatioForm` section at the bottom and are
one-line consequences of the generic cross-multiplied identities via
`div_eq_div_iff`. In a field every `q ≠ 0` is a unit (`Units.mk0`), so
the `Kˣ` hypothesis is exactly the earlier `(q : K) (hq : q ≠ 0)` one;
`heckeH_mk0` records the bridge explicitly.

Ref: [leitner2026] docs/audits/2026-05-25-lepton-bring-surface-h3-3channel-convention.md
Ref: [leitner2026] computations/t6_three_halves_factor_probes.py
Ref: [leitner2026] computations/probes/tau_amphichiral_sdp_probe.py
Ref: [leitner2026] prop:lepton-bring-surface-h3-3channel
Ref: [leitner2026] conj:lepton-tower-h-n-plus-1-branching
-/

namespace QOU.BraidKnot.ThreeHalvesStructuralFactor

variable {R : Type*} [CommRing R]

/-- Hecke amplitude h = q - q⁻¹. -/
def heckeH (q : Rˣ) : R := (q : R) - (↑q⁻¹ : R)

/-- q-bracket [2]_q = q + q⁻¹. -/
def bracket2 (q : Rˣ) : R := (q : R) + (↑q⁻¹ : R)

/-- q-bracket [3]_q = q² + 1 + q⁻². -/
def bracket3 (q : Rˣ) : R := (q : R) ^ 2 + 1 + (↑q⁻¹ : R) ^ 2

/-- q-bracket [4]_q = q³ + q + q⁻¹ + q⁻³. -/
def bracket4 (q : Rˣ) : R :=
  (q : R) ^ 3 + (q : R) + (↑q⁻¹ : R) + (↑q⁻¹ : R) ^ 3

/-- q-bracket [5]_q = q⁴ + q² + 1 + q⁻² + q⁻⁴. -/
def bracket5 (q : Rˣ) : R :=
  (q : R) ^ 4 + (q : R) ^ 2 + 1 + (↑q⁻¹ : R) ^ 2 + (↑q⁻¹ : R) ^ 4

/-- q-bracket [6]_q = q⁵ + q³ + q + q⁻¹ + q⁻³ + q⁻⁵. -/
def bracket6 (q : Rˣ) : R :=
  (q : R) ^ 5 + (q : R) ^ 3 + (q : R) + (↑q⁻¹ : R) + (↑q⁻¹ : R) ^ 3
    + (↑q⁻¹ : R) ^ 5

/-! ## Muon identities (PR #1127) -/

/-- **THEOREM (algebraic).** 3 + h² = [3]_q. Laurent identity over any
    commutative ring; only `↑q * ↑q⁻¹ = 1` is used. -/
theorem three_plus_h_sq_eq_bracket3 (q : Rˣ) :
    3 + (heckeH q) ^ 2 = bracket3 q := by
  have h : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  unfold heckeH bracket3
  linear_combination (-2 : R) * h

/-- **THEOREM (algebraic).** (2 + h²) · [2]_q = [4]_q. -/
theorem two_plus_h_sq_times_bracket2_eq_bracket4 (q : Rˣ) :
    (2 + (heckeH q) ^ 2) * bracket2 q = bracket4 q := by
  have h : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  unfold heckeH bracket2 bracket4
  linear_combination (-((q : R) + (↑q⁻¹ : R))) * h

/-- **MAIN THEOREM (T6 gap (c) muon structural identity), division-free.**
    The canonical lepton-mass-tower correction factor for the muon is
    `[3]_q · [2]_q / [4]_q`, with equivalent closed form
    `(3 + h²) / (2 + h²)`. Stated here as the cross-multiplied identity

      (3 + h²) · [4]_q = [3]_q · [2]_q · (2 + h²)

    which is the content of the ratio equality and holds over **any**
    commutative ring — no denominators, hence no non-vanishing
    hypotheses. `three_halves_factor_eq_q_brackets` below recovers the
    quotient form over a field. -/
theorem three_halves_factor_cross_mul (q : Rˣ) :
    (3 + (heckeH q) ^ 2) * bracket4 q
      = bracket3 q * bracket2 q * (2 + (heckeH q) ^ 2) := by
  rw [three_plus_h_sq_eq_bracket3, ← two_plus_h_sq_times_bracket2_eq_bracket4]
  ring

/-! ## Tau identities (PR #1253 amphichiral probe)

The tau lepton candidate-knot closure under owner directive 2026-05-25
("tau is not torus knot, same symmetries as 1st gen") singles out
amphichiral hyperbolic knots. The structural q-bracket factor
`ξ_3 = [5]_q · [3]_q / [6]_q` for the 10_43 candidate at +0.79%
reduces to a single fundamental identity analogous to muon's
`[4]_q = (2 + h²) · [2]_q`:

  `[6]_q = [2]_q · [3]_q · (1 + h²)`

This is the m=3 case of the symmetric q-bracket family
`[2m+1]_q · [2m-1]_q / [2m+2]_q` covering both muon (m=2) and tau
(m=3) under `conj:lepton-tower-h-n-plus-1-branching`. -/

/-- **THEOREM (algebraic — tau structural).** [6]_q = [2]_q · [3]_q · (1 + h²).
    The fundamental identity behind the tau closure
    `ξ_3 = [5]_q · [3]_q / [6]_q`. -/
theorem bracket6_eq_bracket2_bracket3_times_one_plus_h_sq (q : Rˣ) :
    bracket6 q = bracket2 q * bracket3 q * (1 + (heckeH q) ^ 2) := by
  have h : (q : R) * (↑q⁻¹ : R) = 1 := q.mul_inv
  unfold heckeH bracket2 bracket3 bracket6
  linear_combination
    ((q : R) * (↑q⁻¹ : R) * ((q : R) + (↑q⁻¹ : R))
      - ((q : R) + (↑q⁻¹ : R)) * ((q : R) ^ 2 + (↑q⁻¹ : R) ^ 2)
      + 2 * ((q : R) ^ 3 + (↑q⁻¹ : R) ^ 3)) * h

/-- **THEOREM (tau structural-factor reduction), division-free.** The
    conjectured tau closure factor `[5]_q · [3]_q / [6]_q` reduces to
    `[5]_q / ([2]_q · (1 + h²))`; cross-multiplied,

      [5]_q · [3]_q · ([2]_q · (1 + h²)) = [5]_q · [6]_q.

    Holds over any commutative ring. `bracket5_bracket3_div_bracket6`
    below recovers the quotient form over a field. -/
theorem bracket5_bracket3_cross_mul (q : Rˣ) :
    bracket5 q * bracket3 q * (bracket2 q * (1 + (heckeH q) ^ 2))
      = bracket5 q * bracket6 q := by
  rw [bracket6_eq_bracket2_bracket3_times_one_plus_h_sq]
  ring

/-! ## Ratio presentations (a field is needed only to divide)

The two headline identities are quoted in the narrative as quotients.
A quotient needs division, so these two — and only these two — are
stated over a field. Each is a one-line consequence of the generic
cross-multiplied identity above. -/

section RatioForm

variable {K : Type*} [Field K]

/-- Bridge to the classical presentation: over a field, `Units.mk0`
    turns the earlier hypothesis `q ≠ 0` into the unit `q` used above,
    and the unit coercion `↑q⁻¹` is the field inverse `q⁻¹`. Nothing is
    lost by carrying `q : Kˣ`. -/
theorem heckeH_mk0 (q : K) (hq : q ≠ 0) :
    heckeH (Units.mk0 q hq) = q - q⁻¹ := by
  simp [heckeH]

/-- **Muon ratio presentation.** `(3 + h²)/(2 + h²) = [3]_q · [2]_q / [4]_q`.
    Over a general field the quotient form needs both denominators
    nonzero (the equality is vacuous where `[4]_q` or `2 + h²` vanishes,
    e.g. char 2); the underlying identity
    `three_halves_factor_cross_mul` needs neither. -/
theorem three_halves_factor_eq_q_brackets (q : Kˣ)
    (h2 : 2 + (heckeH q) ^ 2 ≠ 0) (hb4 : bracket4 q ≠ 0) :
    (3 + (heckeH q) ^ 2) / (2 + (heckeH q) ^ 2)
      = bracket3 q * bracket2 q / bracket4 q := by
  rw [div_eq_div_iff h2 hb4]
  exact three_halves_factor_cross_mul q

/-- **Tau ratio presentation.** `[5]_q · [3]_q / [6]_q = [5]_q / ([2]_q · (1 + h²))`.
    As above, the non-vanishing hypotheses are an artefact of writing the
    identity as a quotient. -/
theorem bracket5_bracket3_div_bracket6 (q : Kˣ)
    (hb6 : bracket6 q ≠ 0)
    (hd : bracket2 q * (1 + (heckeH q) ^ 2) ≠ 0) :
    bracket5 q * bracket3 q / bracket6 q
      = bracket5 q / (bracket2 q * (1 + (heckeH q) ^ 2)) := by
  rw [div_eq_div_iff hb6 hd]
  exact bracket5_bracket3_cross_mul q

end RatioForm

/-! ## Generalised lepton-tower closure family

The unified pattern: for each lepton generation m ∈ {2, 3, ...},
the structural closure factor is a ratio of q-brackets whose
fundamental identity expresses `[2m+2]_q` as `[2]_q · [2m]_q · (1 + ?_m h²)`
or similar. Muon (m=2) has `[4]_q = [2]_q · (2 + h²)`, tau (m=3) has
`[6]_q = [2]_q · [3]_q · (1 + h²)`. The pattern beyond is the subject
of `conj:lepton-tower-h-n-plus-1-branching`. -/

end QOU.BraidKnot.ThreeHalvesStructuralFactor
