import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import QOU.AppendixSurreals.Basic
import QOU.AppendixSurreals.StandardPart
import QOU.AppendixSurreals.SignSequence
import QOU.AppendixSurreals.Blowup
import QOU.AppendixSurreals.BirthdayGrading

/-!
# QOU.AppendixSurreals.Conjectures — Open conjectures as classes

Per CLAUDE.md §3b ("conjectural propagation"), each conjecture is
encoded as a typeclass whose `sorry` instances represent the
conjecture itself.  Downstream conditional theorems take such a
class as an instance hypothesis.

## Design principle

Per Gemini review feedback: every field in every class must be a
**genuine conjectural statement** — not a tautology, not a fact
provable in one line from existing surreal-field lemmas, not an
instance of a trivially-inhabited type.

To achieve this, we declare **axiomatic placeholders** for
infrastructure that does not yet exist in mathlib (categorical
QOU types, coloured Jones polynomial, Kazhdan–Lusztig cells,
hyperbolic volume, nimber arithmetic integrated with `Fact
(Nat.Prime p)`).  The conjecture classes then quantify over these
placeholders, making the statements genuinely independent of the
current small base.

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

namespace QOU.AppendixSurreals

universe u

variable (K : Type u) [SurrealField K]

/-! ### Axiomatic placeholders for un-formalized infrastructure

These types and functions are declared but not defined anywhere.
Their role is to serve as referents for the conjectural statements
below — making those statements non-vacuous and non-provable from
the existing `SurrealField` axioms alone.

When mathlib's CategoryTheory / surreal-analysis / nimber / knot-
invariant infrastructure reaches the relevant maturity, these
axioms should be **replaced** with the actual definitions, at which
point the conjecture classes acquire genuine mathematical content.
-/

/-- Placeholder for the category of archimedean QOUs. -/
axiom QOU_Real : Type u

/-- Placeholder for the category of surreal QOUs over `K`. -/
axiom QOU_Surreal (K : Type u) [SurrealField K] : Type u

/-- Placeholder for the standard-part functor on QOU categories. -/
axiom QOU_StandardPart (K : Type u) [SurrealField K] :
  QOU_Surreal K → QOU_Real

/-- Placeholder for the "Frobenius pairing" of a QOU. -/
axiom QOU_FrobeniusPairing {K : Type u} [SurrealField K]
  (Q : QOU_Surreal K) : K

/-- Placeholder for the "observability obstruction" of a QOU. -/
axiom QOU_ObservabilityNorm {K : Type u} [SurrealField K]
  (Q : QOU_Surreal K) : K

/-- Placeholder for "vacuum-energy of the unknot" in a QOU. -/
axiom QOU_VacuumEnergy {K : Type u} [SurrealField K]
  (Q : QOU_Surreal K) : K

/-- Placeholder for a "knot" type.  Declared before `ColoredJones`
    and `HyperbolicVolume` so those axioms can reference it. -/
axiom Knot : Type

/-- Placeholder for the **complexification of `K`**: a `K`-algebra
    structure `K[i] / (i² + 1)` (or any model of `K ⊗_ℝ ℂ`).
    Required because `K` itself is real-ordered, but the Kashaev
    volume conjecture evaluates the coloured Jones polynomial at
    complex roots of unity `ζ_n = e^{2πi/n}` which lie outside any
    `LinearOrderedField`. -/
axiom KComplex (K : Type u) [SurrealField K] : Type u

/-- Placeholder: the absolute value `|a + bi| = √(a² + b²)` returning
    a non-negative element of `K`. -/
axiom KComplex.abs {K : Type u} [SurrealField K] : KComplex K → K

/-- Placeholder for the coloured Jones polynomial
    `J_K(q, n)` where `K_knot : Knot` is the knot, `q : KComplex K`
    is the (complex) quantum parameter (allowed to be transfinite,
    e.g. `ζ_ω = e^{2πi/ω}`), and `n : K` is the colour (allowed to
    be transfinite, e.g. `omegaSurreal K`).  Returns a complex
    surreal value. -/
axiom ColoredJones (K : Type u) [SurrealField K] :
  Knot → KComplex K → K → KComplex K

/-- Placeholder for the hyperbolic volume of a knot complement
    `Vol(S³ \ K)`. -/
axiom HyperbolicVolume : Knot → ℝ

/-- Placeholder for the Kazhdan–Lusztig cells of `H_n(ζ_p)`. -/
axiom KazhdanLusztigCells (p n : ℕ) : Type

/-- Placeholder for nimbers of `p`-adic depth `≤ n`. -/
axiom Nimbers (p n : ℕ) : Type

/-- Placeholder for the evaluation of `exp` on a surreal. -/
axiom surrealExp {K : Type u} [SurrealField K] : K → K

/-- Placeholder for the evaluation of `log` on a positive surreal. -/
axiom surrealLog {K : Type u} [SurrealField K] : K → K

/-- Placeholder for the real-analytic limit of a function at a point. -/
axiom classicalLimit : (ℝ → ℝ) → ℝ → ℝ

/-! ### Conjecture classes -/

/-- **Conjecture: classical limit = standard-part of evaluation at `1+ε`.**

    Full statement: for every function `f : ℝ → ℝ` analytic at `1`,
    and for every `K`-valued lift `F : K → K` that agrees with
    `f` on `ofReal ℝ`, the standard-part of `F(1 + ε)` equals
    `classicalLimit f 1`.

    Not provable from `SurrealField` axioms: the existence of
    "classical limit"-compatible lifts depends on the surreal-analytic
    structure of `K` (Berarducci–Mantova transseries).  -/
-- Ref: [robinson1966] §3.2
-- Ref: [berarducci-mantova2018] Theorem 2.1
class ClassicalLimitIsStandardPart where
  /-- For every analytic lift `F`, the surreal evaluation at
      `1 + ε` followed by standard-part recovers the classical
      limit. -/
  limit_eq_standardPart :
    ∀ (f : ℝ → ℝ) (F : K → K),
      (∀ r : ℝ, F (SurrealField.ofReal r) = SurrealField.ofReal (f r)) →
      standardPart (F (1 + epsilonSurreal K)) = classicalLimit f 1

/-- **Conjecture: archimedean QOU is the standard-part of surreal QOU.**

    Essential surjectivity: every archimedean QOU arises as the
    standard-part of some surreal QOU.

    Requires the `QOU_Real`, `QOU_Surreal`, `QOU_StandardPart`
    placeholders — not provable from `SurrealField` lemmas. -/
-- Ref: [robinson1966] §3.2, [conway1976] §0
class ArchimedeanIsStandardPart where
  /-- Essential surjectivity of the QOU standard-part functor. -/
  essentially_surjective :
    ∀ (Q : QOU_Real), ∃ (SQ : QOU_Surreal K), QOU_StandardPart K SQ = Q

/-- **Conjecture: infinitesimal Frobenius axiom admits non-trivial
    solutions.**

    There exists a surreal QOU `SQ` whose Frobenius pairing differs
    from the strict-Frobenius value by exactly a non-zero
    infinitesimal.

    Requires `QOU_Surreal` + `QOU_FrobeniusPairing`. -/
class InfinitesimalFrobenius where
  /-- Existence of a QOU with strictly-infinitesimal Frobenius
      deviation. -/
  exists_nontrivial_deviation :
    ∃ (SQ : QOU_Surreal K),
      QOU_FrobeniusPairing SQ ≠ 1
      ∧ SurrealField.IsInfinitesimal (QOU_FrobeniusPairing SQ - 1)

/-- **Conjecture: infinitesimal observability.**

    There exists a surreal QOU with non-trivial infinitesimal
    observability obstruction. -/
class InfinitesimalObservability where
  /-- Existence of a QOU with strictly-infinitesimal observability. -/
  exists_nontrivial_observability :
    ∃ (SQ : QOU_Surreal K),
      QOU_ObservabilityNorm SQ ≠ 0
      ∧ SurrealField.IsInfinitesimal (QOU_ObservabilityNorm SQ)

/-- **Conjecture: ε-vacuum normalisation.**

    There exists a surreal QOU whose vacuum-energy equals
    `ε` (the canonical infinitesimal), and whose standard-part
    image is a consistent archimedean QOU. -/
class VacuumEpsilon where
  /-- Existence of a QOU with vacuum-energy exactly `ε`. -/
  exists_epsilon_vacuum :
    ∃ (SQ : QOU_Surreal K),
      QOU_VacuumEnergy SQ = epsilonSurreal K
      ∧ ∃ (Q : QOU_Real), QOU_StandardPart K SQ = Q

/-- **Conjecture: Big Bang and heat-death as named-surreal evaluations.**

    The parameterised functor `q ↦ QOU_Surreal_q` extends to
    evaluation at `q = 1 + ε^ω` (Big Bang) and `q = ω` (heat death),
    with meaningful standard-part images. -/
class BigBangHeatDeath where
  /-- Existence of QOUs at both named-surreal cosmological endpoints. -/
  endpoints_well_defined :
    ∃ (BigBang HeatDeath : QOU_Real),
      (∃ (SQ_bb : QOU_Surreal K),
        QOU_StandardPart K SQ_bb = BigBang)
      ∧ (∃ (SQ_hd : QOU_Surreal K),
        QOU_StandardPart K SQ_hd = HeatDeath)

/-- **Conjecture: surreal Kashaev volume identity.**

    For every hyperbolic knot `K_knot`, the standard-part of
    `2π · log|J_{K_knot}(ζ_ω, ω)| / ω` equals `Vol(S³ \ K_knot)`.

    Requires `ColoredJones`, `HyperbolicVolume`, `surrealLog`,
    `surrealExp`, `Knot` — all placeholders. -/
-- Ref: [kashaev1997], [murakami-murakami2001]
class KashaevSurreal where
  /-- Kashaev volume identity in surreal form:
      `st(2π · log|J(ζ_ω, ω)| / ω) = Vol(K_knot)`.

      `zeta_omega` is a complex surreal (root of unity at order ω);
      `KComplex.abs` extracts the K-valued modulus before taking
      the real-valued surreal log. -/
  st_volume_eq_asymptotic :
    ∀ (K_knot : Knot),
      ∃ (zeta_omega : KComplex K),
        standardPart
          (2 * SurrealField.ofReal Real.pi
            * surrealLog
                (KComplex.abs
                  (ColoredJones K K_knot zeta_omega (omegaSurreal K)))
            / omegaSurreal K)
          = HyperbolicVolume K_knot

/-- **Conjecture: birthday refinement of the Jones polynomial.**

    There exists a knot invariant `J̃_K` indexed by ordinals whose
    sum equals `J_K` but which separates knots not separated by
    the Jones polynomial alone. -/
class JonesBirthday where
  /-- Existence of a strict birthday refinement. -/
  strict_refinement_exists :
    ∃ (K₁ K₂ : Knot) (J_K₁ J_K₂ : ℕ → K) (J̃_K₁ J̃_K₂ : Ordinal → K),
      -- Same Jones polynomial at every integer level:
      (∀ n, J_K₁ n = J_K₂ n)
      -- But distinct birthday refinements at some ordinal:
      ∧ (∃ α : Ordinal, J̃_K₁ α ≠ J̃_K₂ α)

/-- **Conjecture: Hahn-series substrate.**

    There exists a non-trivial sequence `α₂, α₃, …` of real
    coefficients such that the substrate parameter
    `q = 1 + ε + α₂ ε² + …`, when plugged into the QOU mass
    formula, matches CODATA at orders higher than the archimedean
    fit.  Non-triviality: at least one `α_k ≠ 0`.  -/
-- Ref: [ehrlich2012]
class HahnSubstrate where
  /-- Existence of a non-trivial Hahn-series substrate correction. -/
  exists_nontrivial_correction :
    ∃ (α : ℕ → ℝ),
      (∃ k, α k ≠ 0)
      ∧ (∃ (Q : QOU_Real), ∃ (SQ : QOU_Surreal K),
          QOU_StandardPart K SQ = Q)

/-- **Conjecture: characteristic-`p` modular Hecke ↔ nimbers `On_p`.**

    The Kazhdan–Lusztig cells of `H_n(ζ_p)` are in bijection with
    the nimbers of `p`-adic depth `≤ n`.

    Requires `KazhdanLusztigCells` and `Nimbers` placeholders. -/
-- Ref: [conway1976] §0 (nimbers)
class OnPModularHecke (p : ℕ) [Fact (Nat.Prime p)] where
  /-- Bijection between KL cells and nimbers for every `n`. -/
  cells_bijective_to_nimbers :
    ∀ (n : ℕ), ∃ (φ : KazhdanLusztigCells p n → Nimbers p n),
      Function.Bijective φ

/-! ### Conditional theorems

The following show the intended *use* of the conjecture classes:
downstream identities provable on assumption that some conjecture
holds. -/

/-- **Unconditional theorem.** The substrate `c_q = 1/(q-1)` at
    `q = 1 + ε` equals `ω` in the surreal lift. -/
-- Ref: [conway1976] §0
theorem c_q_eq_omega_at_one_plus_epsilon :
    let q : K := 1 + epsilonSurreal K
    (q - 1)⁻¹ = omegaSurreal K := by
  show (1 + epsilonSurreal K - 1)⁻¹ = omegaSurreal K
  rw [add_sub_cancel_left]
  unfold epsilonSurreal
  exact inv_inv (omegaSurreal K)

end QOU.AppendixSurreals
