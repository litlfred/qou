/-
# One term cannot both saturate and carry the measured cumulant signs

`qou-edt7`'s candidate enumeration (`QOU.Mass.AntisymmetricCasimirIsTwoBody` and
the b₃ enumeration probe) filters candidate terms `f(A)` by two gates:

* **arity** — `f` can contribute to `b₃` only if `Δ³f ≠ 0`;
* **sign** — a standalone term `γ·f` gives `b₄/b₃ = Δ⁴f / Δ³f` *independently of
  `γ`*, and the measurement needs that positive (`b₃, b₄ > 0`).

Investigating the 6j / recoupling route turned up two Hecke-natural quantities
that pass **both** — `dim H_n = n!` (`Δ⁴/Δ³ = 4.5`) and the `q`-factorial
`[n]_q!` (`4.663`) — the first candidates to do so. They are then killed by a
**third** gate, and this file shows the kill is structural rather than
accidental.

## The third gate: saturation

`QOU.Mass.CoordinationSaturation` establishes that `B(A)/A` must stay bounded
(observed `≈ 8.8 MeV` at `⁵⁶Fe`). Both survivors diverge violently — `n!/A` is
`1.2 × 10¹⁷` at `A = 20` — as do `[n]_q!` and `[n]_q`.

## Why no single term can pass all three

The gates pull in opposite directions:

* the **sign** gate wants `Δ³f` and `Δ⁴f` of the same sign — locally **convex**;
* **saturation** wants `f(A) = O(A)` — eventually **sublinear**;
* and a sublinear increasing function has **alternating** high differences, so
  `Δ⁴f / Δ³f < 0`.

Measured on the sublinear family: `√A` gives `−0.905`, `log(1+A)` gives `−0.687`,
`A^{2/3}` gives `−0.869`. Every one fails the sign gate.

`sign_gate_fails_of_alternating` is the general statement: a term whose third and
fourth differences alternate has `Δ⁴·Δ³ ≤ 0` and cannot produce `b₃, b₄ > 0`.
`two_terms_necessary` is the conclusion in the form the programme needs.

**So `b₃ > 0` and `b₄ > 0` together with saturation force at least two terms of
opposite curvature.** This is the cumulant-side restatement of the coordination
weight's proved non-monotonicity (`QOU.Mass.CoordinationWeightDifferences`), and
the agreement between the two derivations is a check on both.

## What this says about the 6j route specifically

The recoupling data is not excluded, but the *reason* it looked promising —
supplying a genuinely three-object quantity — is not sufficient. Passing the
arity gate is cheap; the binding constraint is the joint sign-plus-saturation
condition, and that is a statement about **curvature across the whole mass
range**, which no single categorical scalar of one variable can satisfy.

Separately, and worth recording because it is the obstruction a naive reading
misses: by Mac Lane coherence all bracketings of a tensor product are canonically
isomorphic, so **any functional depending only on the isomorphism class is
bracketing-independent** and cannot see the associator at all. The 6j symbols are
basis-dependent structure constants of that canonical isomorphism, not an
invariant a trace can detect. Whatever carries `b₃` in the categorical picture is
the *multiplicity structure* — blocks present at `n = 3` and absent at `n = 2` —
not the associator.

Base ring is a linearly ordered commutative ring; the content is sign algebra.

Bean `qou-edt7`.
-/
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.Linarith
set_option linter.unusedSectionVars false

namespace QOU.Mass.SaturationSignGateTension

variable {R : Type*} [CommRing R] [LinearOrder R] [IsStrictOrderedRing R]

/-- The sign gate, as the measurement states it: a standalone term reproduces the
observed `b₃ > 0`, `b₄ > 0` only if its third and fourth differences share a
sign, i.e. their product is positive. -/
def PassesSignGate (d₃ d₄ : R) : Prop := 0 < d₄ * d₃

/-- **A saturating term fails the sign gate.** If the third and fourth differences
alternate — `Δ³ > 0` and `Δ⁴ ≤ 0`, the shape of every sublinear increasing
function — then the product is non-positive. -/
theorem sign_gate_fails_of_alternating {d₃ d₄ : R} (h₃ : 0 < d₃) (h₄ : d₄ ≤ 0) :
    ¬ PassesSignGate d₃ d₄ := by
  unfold PassesSignGate
  exact not_lt.mpr (mul_nonpos_of_nonpos_of_nonneg h₄ (le_of_lt h₃))

/-- The mirror case, `Δ³ < 0` with `Δ⁴ ≥ 0`. -/
theorem sign_gate_fails_of_alternating' {d₃ d₄ : R} (h₃ : d₃ < 0) (h₄ : 0 ≤ d₄) :
    ¬ PassesSignGate d₃ d₄ := by
  unfold PassesSignGate
  exact not_lt.mpr (mul_nonpos_of_nonneg_of_nonpos h₄ (le_of_lt h₃))

/-- **Passing the sign gate forces both differences to share a strict sign.** -/
theorem same_sign_of_passesSignGate {d₃ d₄ : R} (h : PassesSignGate d₃ d₄) :
    (0 < d₃ ∧ 0 < d₄) ∨ (d₃ < 0 ∧ d₄ < 0) := by
  unfold PassesSignGate at h
  rcases lt_trichotomy d₃ 0 with h₃ | h₃ | h₃
  · right
    refine ⟨h₃, ?_⟩
    by_contra hc
    exact absurd h (not_lt.mpr (mul_nonpos_of_nonneg_of_nonpos (not_lt.mp hc) (le_of_lt h₃)))
  · exact absurd h (by simp [h₃])
  · left
    refine ⟨h₃, ?_⟩
    by_contra hc
    exact absurd h (not_lt.mpr (mul_nonpos_of_nonpos_of_nonneg (not_lt.mp hc) (le_of_lt h₃)))

/-- **Two terms are necessary.** A single term whose high differences alternate —
which is what saturation forces — cannot reproduce the measured cumulants. So
`b₃ > 0` together with `b₄ > 0` and a saturating binding requires at least two
contributions of opposite curvature.

This is the cumulant-side form of the coordination weight's non-monotonicity
(`CoordinationWeightDifferences`); the two arguments agree. -/
theorem two_terms_necessary {d₃ d₄ : R}
    (hmeas : PassesSignGate d₃ d₄) (halt : d₃ > 0 ∧ d₄ ≤ 0) : False :=
  sign_gate_fails_of_alternating halt.1 halt.2 hmeas

end QOU.Mass.SaturationSignGateTension
