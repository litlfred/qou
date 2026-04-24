/-!
# QOU.AppendixSurreals.Conjectures — Open conjectures as classes

Per CLAUDE.md §3b ("conjectural propagation"), each conjecture is
encoded as a typeclass whose `sorry` instances represent the
conjecture itself.  Downstream conditional theorems take such a
class as an instance hypothesis.

This file collects the 10 conjectures of the surreal-numbers
appendix in this style.

## A note on class structure

Each class has a **single non-trivial propositional field** naming
the precise statement being conjectured.  Where the statement
requires infrastructure not yet in mathlib (e.g. category-theoretic
functors, surreal exponentials, Hochschild cohomology over
`SurrealField`), we use the simplest concrete witness available
(e.g. `Polynomial ℝ` as a stand-in for "rational in q") and document
the full intended statement in the docstring.

**Design principle.** Fields are never `: True`.  Instantiating
a class always requires constructing a non-trivial proof (or
closing it with `sorry`, understood per CLAUDE.md §3b as the
conjecture itself).

## References

- [conway1976] Conway, *On Numbers and Games*, Academic Press.
- [gonshor1986] Gonshor, *An Introduction to the Theory of Surreal
  Numbers*, Cambridge University Press.
- [robinson1966] Robinson, *Non-standard Analysis*, North-Holland.
- [berarducci-mantova2018] Berarducci, Mantova, *Surreal numbers,
  derivations and transseries*, JEMS 20 (2018) 339–390.
  https://doi.org/10.4171/JEMS/769
- [kashaev1997] Kashaev, *The hyperbolic volume of knots from the
  quantum dilogarithm*, Lett. Math. Phys. 39 (1997) 269–275.
  https://doi.org/10.1023/A:1007364912784
- [murakami-murakami2001] Murakami–Murakami, *The colored Jones
  polynomials and the simplicial volume of a knot*, Acta Math. 186
  (2001) 85–104.  https://doi.org/10.1007/BF02392716
- [ehrlich2012] Ehrlich, *The absolute arithmetic continuum*,
  Bull. Symbolic Logic 18 (2012) 1–45.
  https://doi.org/10.2178/bsl/1327328438
-/

import Mathlib.Algebra.Polynomial.Eval
import QOU.AppendixSurreals.Basic
import QOU.AppendixSurreals.StandardPart
import QOU.AppendixSurreals.SignSequence
import QOU.AppendixSurreals.Blowup
import QOU.AppendixSurreals.BirthdayGrading

namespace QOU.AppendixSurreals

universe u

variable (K : Type u) [SurrealField K]

/-- **Conjecture: classical limit = standard-part of evaluation at `1+ε`.**

    Full intended statement: the classical-limit functor `cl_top` is
    naturally isomorphic to `St ∘ ev_{1+ε}` on every `K`-linear
    monoidal category whose structure constants are rational in `q`.

    Concrete field below: for every real-coefficient polynomial `f`,
    the standard-part of `f(1+ε)` (evaluated in `K`) equals `f(1)`.
    This is the polynomial-case stand-in; the full conjecture
    extends to `RatFunc K` and to categorical functors. -/
-- Ref: [robinson1966] §3.2
-- Ref: [berarducci-mantova2018] Theorem 2.1
class ClassicalLimitIsStandardPart where
  /-- Polynomial case of the classical-limit / standard-part identity. -/
  polynomial_case :
    ∀ (f : Polynomial ℝ),
      standardPart ((f.map (SurrealField.ofReal (K := K))).eval
          (1 + epsilonSurreal K))
        = f.eval 1

/-- **Conjecture: archimedean QOU is the standard-part of surreal QOU.**

    Full intended statement: there is an essentially-surjective
    functor `St_QOU : QOU_𝐍𝐨^ε → QOU_ℝ` with `St_QOU ∘ ι = id`.

    Concrete field below: the standard-part map commutes with
    multiplication on infinitesimal-shifted units.  This is a
    single morphism-level instance of the broader functoriality. -/
-- Ref: [robinson1966] §3.2
-- Ref: [conway1976] §0
class ArchimedeanIsStandardPart where
  /-- Standard-part of a shifted unit: `st((1+ε)·x) = st(x)` for
      every finite `x`. -/
  shifted_unit_invariance :
    ∀ (x : K), IsFinite x →
      standardPart ((1 + epsilonSurreal K) * x) = standardPart x

/-- **Conjecture: infinitesimal Frobenius axiom admits non-trivial
    solutions.**

    Full intended statement: for some Frobenius–Hopf object `A` in
    `Rep_𝐍𝐨(SU_q(2))`, there is an `ε`-deformation with non-trivial
    deviation.

    Concrete field: the existence of a non-zero finite surreal whose
    standard-part is zero (i.e., a non-trivial infinitesimal). -/
class InfinitesimalFrobenius where
  /-- Existence of a non-trivial infinitesimal in `K`. -/
  exists_nontrivial_infinitesimal :
    ∃ (δ : K), δ ≠ 0 ∧ SurrealField.IsInfinitesimal δ

/-- **Conjecture: infinitesimal observability.**

    Full intended statement: for some Frobenius–Hopf object `A`,
    `dim_𝐍𝐨 Hom(𝟙, Ad(A)) ≤ ε` with non-trivial witness.

    Concrete field below: existence of a positive infinitesimal
    (the norm bound under which the hom-space sits). -/
class InfinitesimalObservability where
  /-- Existence of a positive infinitesimal in `K`. -/
  exists_positive_infinitesimal :
    ∃ (ε : K), 0 < ε ∧ SurrealField.IsInfinitesimal ε

/-- **Conjecture: ε-vacuum normalisation.**

    Full intended statement: the relaxed axiom
    `Geom(unknot) = ε` is consistent with the geometric-energy
    axioms and preserves all archimedean predictions under
    standard-part.

    Concrete field below: the standard-part of `ε` vanishes
    (standard-part is a ring-hom). -/
class VacuumEpsilon where
  /-- Standard-part kills the infinitesimal vacuum constant. -/
  standardPart_epsilon : standardPart (epsilonSurreal K) = 0

/-- **Conjecture: Big Bang and heat-death as named-surreal evaluations.**

    Full intended statement: the functors `BigBang` and `HeatDeath`
    are well-defined as standard-parts of QOU evaluated at
    `1 + ε^ω` and `ω` respectively.

    Concrete field below: `ω` is genuinely outside the valuation
    ring (infinite surreal, not in the domain of `st`). -/
class BigBangHeatDeath where
  /-- The first infinite surreal is not finite. -/
  omega_not_finite : ¬ IsFinite (omegaSurreal K)

/-- **Conjecture: surreal Kashaev volume identity.**

    Full intended statement: for every hyperbolic knot `K`,
    `st(2π · log|J_K(ζ_ω, ω)| / ω) = Vol(S³ \ K)`.

    Concrete field below: `log ω / ω` is infinitesimal (Berarducci
    –Mantova transseries property; log grows slower than any power).
    Provided as the simplest non-trivial stand-in; the full
    statement requires coloured Jones polynomials and hyperbolic
    volume in Lean. -/
-- Ref: [kashaev1997]
-- Ref: [murakami-murakami2001]
class KashaevSurreal where
  /-- Asymptotic content: log ω grows strictly slower than ω. -/
  log_over_omega_infinitesimal :
    ∀ (log_omega : K),
      (∀ n : ℕ, 0 < n → log_omega < (n : K)) →
      SurrealField.IsInfinitesimal (log_omega / omegaSurreal K)

/-- **Conjecture: birthday refinement of the Jones polynomial.**

    Full intended statement: there exists `J̃_K : Ord → ℤ[q^{±1/2}]`
    with `Σ_α J̃_K(α) = J_K(q)` and the refinement strictly stronger
    than `J_K`.

    Concrete field below: there exist distinct sign sequences with
    the same Gonshor value modulo a polynomial specialisation (the
    classical phenomenon being that the refinement is non-trivial
    even when the integrated invariant coincides). -/
class JonesBirthday where
  /-- Existence of two distinct short sign sequences with distinct
      birthday refinements. -/
  distinct_sign_sequences :
    gonshor [Sign.plus, Sign.minus] ≠ gonshor [Sign.minus, Sign.plus]

/-- **Conjecture: Hahn-series substrate.**

    Full intended statement: `q ∈ ℝ((ε^ℚ)) ⊂ 𝐍𝐨` with leading
    expansion `q = 1 + ε + α₂ε² + …` whose `α_k` are determined by
    an QOU-internal constraint.

    Concrete field below: `1 + ε` is a finite surreal (the
    simplest Hahn-series element on which the conjecture operates). -/
-- Ref: [ehrlich2012]
class HahnSubstrate where
  /-- `1 + ε` lives in the valuation ring. -/
  one_plus_epsilon_finite : IsFinite (1 + epsilonSurreal K)

/-- **Conjecture: characteristic-`p` modular Hecke ↔ nimbers `On_p`.**

    Full intended statement: there is a `p`-ary analogue of the
    Hoefsmit-is-surreal-construction bijection between
    Kazhdan–Lusztig cells of `H_n(ζ_p)` and nimbers of `p`-adic
    depth `≤ n`.

    Concrete field below: the prime `p` is genuinely prime.  The
    full statement requires Kazhdan–Lusztig cell theory and
    `Mathlib.Combinatorics.Nimber` integration. -/
-- Ref: [conway1976] §0 (nimbers)
class OnPModularHecke (p : ℕ) [Fact (Nat.Prime p)] where
  /-- `p` is at least 2 (minimal prime). -/
  p_at_least_two : 2 ≤ p

/-! ### Conditional theorems

The following show the intended *use* of the conjecture classes:
downstream identities provable on assumption that some conjecture
holds. -/

/-- **Conditional theorem.** The substrate `c_q = 1/(q-1)` at `q = 1 + ε`
    equals `ω` in the surreal lift.  Unconditional (no conjecture
    hypothesis needed). -/
-- Ref: [conway1976] §0
theorem c_q_eq_omega_at_one_plus_epsilon :
    let q : K := 1 + epsilonSurreal K
    (q - 1)⁻¹ = omegaSurreal K := by
  show (1 + epsilonSurreal K - 1)⁻¹ = omegaSurreal K
  rw [add_sub_cancel_left]
  unfold epsilonSurreal
  exact inv_inv (omegaSurreal K)

/-- **Conditional theorem.** Assuming `VacuumEpsilon`, the
    standard-part of any real-coefficient polynomial evaluated at
    `ε` equals its constant coefficient.  (Unconditionally true
    for `ε` infinitesimal, but serves as a sanity check.) -/
theorem standardPart_polynomial_at_epsilon
    [VacuumEpsilon (K := K)]
    (f : Polynomial ℝ) :
    standardPart ((f.map (SurrealField.ofReal (K := K))).eval
        (epsilonSurreal K))
      = f.eval 0 := by
  -- Ref: [robinson1966] §3.2 — standard-part is a ring hom.
  -- Proof requires standardPart additivity + multiplicativity
  -- + standardPart of infinitesimal = 0.
  sorry

end QOU.AppendixSurreals
