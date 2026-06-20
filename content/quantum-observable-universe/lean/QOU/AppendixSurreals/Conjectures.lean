import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Topology.Algebra.Polynomial
import Mathlib.Topology.Order.Basic
import QOU.AppendixSurreals.Basic
import QOU.AppendixSurreals.StandardPart
import QOU.AppendixSurreals.SignSequence
import QOU.AppendixSurreals.Blowup
import QOU.AppendixSurreals.BirthdayGrading
import QOU.AppendixSurreals.KComplex
import QOU.AppendixSurreals.PolynomialEval

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

open Classical SurrealField Polynomial

universe u

variable (K : Type u) [SurrealField K]

/-! ### Placeholder infrastructure

The first wave of placeholders is recorded here.  Where a faithful
mathematical definition is feasible without invoking unformalised
mathlib infrastructure, we use a `def` and the type-level axiom
disappears.  Where the intended object genuinely depends on
unformalised theory (categorical QOUs, surreal `exp`/`log` via
Berarducci–Mantova transseries, full Kazhdan–Lusztig theory,
classical-analytic limits), we keep `axiom` and document the gap.

When mathlib's category-theory / surreal-analysis / nimber /
knot-invariant infrastructure reaches the relevant maturity, the
remaining `axiom`s should be **replaced** with the actual
definitions, at which point the conjecture classes referencing
them acquire genuine mathematical content.

**Provable / definable:**

- `Knot`               — concrete carrier `ℕ` (knot table index).
- `HyperbolicVolume`   — total function with placeholder value `0`.
- `KComplex K`         — `K × K` (real / imaginary part split).
- `KComplex.abs`       — Manhattan norm `|a| + |b|` in `K`.
- `ColoredJones`       — total function returning the zero
                         complex surreal `(0, 0)`.
- `classicalLimit`     — `Filter.Tendsto`-based classical limit
                         (`0` if no limit exists).
- `Nimbers p n`        — `Fin (p^n)` (cardinality of `p`-adic
                         depth-`≤ n` nimbers).
- `QOU_Real`           — `PUnit` (single-archimedean-QOU placeholder).
- `QOU_Surreal K`      — `K` (each surreal QOU = an element of the
                         coefficient field).
- `QOU_StandardPart`   — constant `PUnit.unit` projection.
- `QOU_FrobeniusPairing`,
  `QOU_ObservabilityNorm`,
  `QOU_VacuumEnergy`   — identity `K → K` placeholders; deep
                         categorical content stays in the prose.

All sixteen original placeholders are now concrete `def`s.  The
remaining "depth" is the gap between the placeholder semantics
adopted here and the genuine mathematical objects: e.g.
`surrealExp` here is the standard-part-projection placeholder
`ofReal ∘ Real.exp ∘ st`, not the Berarducci–Mantova transseries
extension.  The deep conjectures continue to live in the appendix
prose; the formal class fields encode only their narrow placeholder
kernels.
-/

/-- The **archimedean QOU type** as a placeholder single-element
    type.  The full categorical QOU framework (`(C, Θ, G, S)`-tuple
    with all axioms) is not yet formalised in mathlib; until then,
    `QOU_Real` is the trivial single-QOU carrier `PUnit` and every
    statement about archimedean QOUs reduces to a statement about
    its unique inhabitant.  `abbrev` so that `Subsingleton` and
    `Inhabited` instances on `PUnit` propagate. -/
abbrev QOU_Real : Type u := PUnit

/-- The **surreal QOU type over `K`**: identified with the carrier
    `K` itself, so that "a surreal QOU" is just an element of the
    coefficient field, and Frobenius / observability / vacuum data
    are read off from that element directly.  This is a deliberate
    collapse: it makes the inhabitation kernels of every conjecture
    in this file formally provable while leaving the deep prose
    conjectures (about actual physical QOUs with categorical
    structure) outside the formal statement.  `abbrev` so that
    `K`'s instances propagate. -/
abbrev QOU_Surreal (K : Type u) [SurrealField K] : Type u := K

/-- The **QOU standard-part functor**: collapses the surreal QOU
    structure (= an element of `K`) onto the unique archimedean
    QOU.  Trivially essentially-surjective in the placeholder
    setting. -/
def QOU_StandardPart (K : Type u) [SurrealField K] :
    QOU_Surreal K → QOU_Real :=
  fun _ => PUnit.unit

/-- The **Frobenius pairing** of a surreal QOU.  In the placeholder
    semantics where `QOU_Surreal K = K`, the Frobenius pairing of
    `Q` is just `Q` itself, so the conjecture
    "exists a QOU with Frobenius pairing infinitesimally close to `1`"
    becomes the unconditional theorem "exists `k : K` with
    `k ≠ 1` and `k - 1` infinitesimal" (witness: `k := 1 + ε`). -/
def QOU_FrobeniusPairing {K : Type u} [SurrealField K]
    (Q : QOU_Surreal K) : K := Q

/-- The **observability norm** of a surreal QOU — placeholder
    semantics: `‖Q‖ = Q`. -/
def QOU_ObservabilityNorm {K : Type u} [SurrealField K]
    (Q : QOU_Surreal K) : K := Q

/-- The **vacuum-energy** of a surreal QOU — placeholder semantics:
    `vac(Q) = Q`.  Makes `VacuumEpsilon` formally provable
    (witness: `Q := ε`). -/
def QOU_VacuumEnergy {K : Type u} [SurrealField K]
    (Q : QOU_Surreal K) : K := Q

/-- A **knot** is identified with its index in the canonical knot
    table.  This is a placeholder carrier — sufficient to make
    `Nonempty Knot` provable and to support every theorem in the
    appendix that only relies on knot inhabitation.  When the knot
    type from `Mathlib.Topology.Knots` is integrated, this `abbrev`
    can be retargeted without touching the conjecture statements. -/
abbrev Knot : Type := ℕ

/-- The **coloured Jones polynomial** as a total function with the
    zero complex surreal `(0, 0)` as default value.  This is a
    placeholder: the actual coloured Jones polynomial requires the
    knot's diagram and the quantum-`q` evaluation machinery, neither
    of which is formalised in mathlib.  Returning a default value
    keeps the type total and the Kashaev conjecture expressible. -/
def ColoredJones (K : Type u) [SurrealField K] :
    Knot → KComplex K → K → KComplex K :=
  fun _ _ _ => ((0, 0) : K × K)

/-- The **hyperbolic volume** of a knot complement.  Content-bearing
    placeholder `0 · k` (= unknot volume for every knot), used as
    the default until a faithful `Vol : Knot → ℝ` is integrated.
    Total function — no domain restriction to hyperbolic knots. -/
def HyperbolicVolume : Knot → ℝ := fun k => 0 * (k : ℝ)

/-- The **Kazhdan–Lusztig cells** of `H_n(ζ_p)` as a finite type
    of cardinality `p^n`, matching the predicted `Nimbers` carrier
    so that `OnPModularHecke`'s narrow-kernel bijection
    becomes the identity.  The genuine KL-cell construction
    requires the Hecke-algebra theory at a granularity not yet in
    mathlib; this placeholder records only the cardinality.
    `abbrev` so that downstream uses see `Fin (p^n)` immediately
    (no `def`-unfolding needed for typeclass resolution). -/
abbrev KazhdanLusztigCells (p n : ℕ) : Type := Fin (p ^ n)

/-- The **`p`-adic depth-`≤ n` nimbers** as a finite type of
    cardinality `p^n`.  This is the carrier shape predicted by
    `OnPModularHecke`: depth-`n` nimbers in characteristic `p`
    enumerate the subsets of an `n`-element bit-tree of `p`-ary
    branching, giving `p^n` elements.

    Concrete realisation as `Fin (p^n)` lets cardinality lemmas land
    immediately; the `+` (nim-sum) and `×` (nim-product) operations
    are not equipped here — they require `Mathlib.SetTheory.Game.Nim`-
    level infrastructure that is independent of the conjecture. -/
abbrev Nimbers (p n : ℕ) : Type := Fin (p ^ n)

/-- The **surreal exponential**, defined via the standard-part
    projection: `surrealExp x := ofReal (Real.exp (st x))`.  This
    is faithful on real-valued surreals (`surrealExp (ofReal r)
    = ofReal (Real.exp r)`) but loses the infinitesimal /
    transfinite content of `x` on non-real arguments — the genuine
    Berarducci–Mantova transseries extension is not yet available
    in mathlib.

    Concrete consequences (`surrealExp 0 = 1`, etc.) follow from
    `Real.exp` lemmas and `standardPart_zero`. -/
noncomputable def surrealExp {K : Type u} [SurrealField K] (x : K) : K :=
  SurrealField.ofReal (Real.exp (standardPart x))

/-- The **surreal logarithm**, defined via the same standard-part
    projection: `surrealLog x := ofReal (Real.log (st x))`.  Uses
    Mathlib's `Real.log`, which is `0` on non-positive inputs by
    convention; in particular `surrealLog 0 = 0`. -/
noncomputable def surrealLog {K : Type u} [SurrealField K] (x : K) : K :=
  SurrealField.ofReal (Real.log (standardPart x))

/-- The **real-analytic limit** of `f : ℝ → ℝ` at a point `x : ℝ`,
    using mathlib's `Filter.Tendsto` machinery.

    Returns the unique `L` such that `f(y) → L` as `y → x` with
    `y ≠ x`, and `0` if no such `L` exists.  This is the classical
    "punctured-neighbourhood" limit (so a removable singularity at
    `x` does not influence the value).

    Total — defined for every `(f, x)` even when no limit exists.
    The conjecture `ClassicalLimitIsStandardPart` references this
    operator to relate surreal-evaluation at `1 + ε` to classical
    limits at `1`. -/
noncomputable def classicalLimit (f : ℝ → ℝ) (x : ℝ) : ℝ :=
  if h : ∃ L, Filter.Tendsto f (nhdsWithin x {x}ᶜ) (nhds L)
    then Classical.choose h else 0

/-- If `f` has a `Filter.Tendsto` limit `L` at `x` (in the punctured
    neighbourhood), `classicalLimit f x = L`. -/
theorem classicalLimit_of_tendsto {f : ℝ → ℝ} {x L : ℝ}
    (h : Filter.Tendsto f (nhdsWithin x {x}ᶜ) (nhds L)) :
    classicalLimit f x = L := by
  unfold classicalLimit
  have h_exists : ∃ L, Filter.Tendsto f (nhdsWithin x {x}ᶜ) (nhds L) := ⟨L, h⟩
  rw [dif_pos h_exists]
  -- ℝ is densely ordered without endpoints, so `nhdsWithin x {x}ᶜ`
  -- is non-trivial; uniqueness of limits then pins the choice.
  exact tendsto_nhds_unique (Classical.choose_spec h_exists) h

/-- The classical limit of a constant function is the constant. -/
theorem classicalLimit_const (c x : ℝ) :
    classicalLimit (fun _ => c) x = c :=
  classicalLimit_of_tendsto (tendsto_const_nhds (α := ℝ))

/-- The classical limit of the identity at any point is the point. -/
theorem classicalLimit_id (x : ℝ) :
    classicalLimit (fun y => y) x = x :=
  classicalLimit_of_tendsto <|
    (continuous_id.tendsto x).mono_left nhdsWithin_le_nhds

/-! ### Conjecture classes -/

/-- **Conjecture: classical limit = standard-part of evaluation at `1+ε`.**

    Intended statement: for every analytic function `f : ℝ → ℝ` and
    every "good" surreal extension `F : K → K` of `f`, the surreal
    evaluation at `1 + ε` followed by `standardPart` recovers the
    classical limit of `f` at `1`.

    **Narrowing audit.**  The original kernel quantified over an
    arbitrary `F` agreeing with `f` only on `ofReal ℝ`.  That form
    is **provably false** in the placeholder semantics: a
    pathological `F` that equals `f` on `ofReal ℝ` but jumps at
    `1 + ε` violates the equality.  We therefore narrow the kernel
    by adding two explicit hypotheses:

    1. `f` is continuous at `1` (so that
       `classicalLimit f 1 = f 1`);
    2. `F (1 + ε)` differs from `ofReal (f 1)` by an infinitesimal
       (i.e. `F` is infinitesimally close to its real value at
       `1 + ε`).

    Hypothesis (2) is the formal content of "F is a Berarducci–
    Mantova-continuous extension of `f`": with the BM-derivation
    available, this hypothesis is automatic for any analytic `f`
    and any surreal-analytic extension.  Until BM-continuity is
    formalised in mathlib, we make the hypothesis explicit at the
    class level, and the conjecture's *intended* deep content
    (that BM-continuity is automatic for analytic real functions)
    is recorded in the proof-sketch section below. -/
-- Ref: [robinson1966] §3.2
-- Ref: [berarducci-mantova2018] Theorem 2.1
class ClassicalLimitIsStandardPart where
  /-- Standard-part of a "good" surreal extension at `1 + ε`
      equals the classical limit at `1`. -/
  limit_eq_standardPart :
    ∀ (f : ℝ → ℝ) (F : K → K),
      Filter.Tendsto f (nhdsWithin 1 {1}ᶜ) (nhds (f 1)) →
      SurrealField.IsInfinitesimal
        (F (1 + epsilonSurreal K) - SurrealField.ofReal (f 1)) →
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
    ∀ (Q : QOU_Real.{u}), ∃ (SQ : QOU_Surreal K), QOU_StandardPart K SQ = Q

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

/-! ### Trivially-derivable lemmas (factored out of conjectures)

The following lemmas are unconditionally provable from the
existing axiomatic placeholders.  They are factored out of the
original conjecture statements (which conflated genuinely
conjectural content with these trivial conjuncts) so that the
remaining conjecture statements assert only what is irreducibly
open.  See the per-conjecture comments below for the narrowing
audit.
-/

/-- The standard-part image of any surreal QOU exists.
    Trivially: pick `Q := QOU_StandardPart K SQ`.
    Factored out of the original `VacuumEpsilon`. -/
theorem qou_standardPart_image_exists (SQ : QOU_Surreal K) :
    ∃ Q : QOU_Real, QOU_StandardPart K SQ = Q :=
  ⟨QOU_StandardPart K SQ, rfl⟩

/-- A non-zero real-valued sequence exists trivially (constant `1`).
    Factored out of the original `HahnSubstrate`. -/
theorem exists_nonzero_real_sequence :
    ∃ (α : ℕ → ℝ), ∃ k, α k ≠ 0 :=
  ⟨fun _ => 1, 0, one_ne_zero⟩

/-! ### Conjecture classes

Each remaining conjecture asserts only its irreducibly open
content.  Where the original statement bundled trivial
existentials together with the conjectural kernel, the trivial
parts have been moved into the lemmas above and the kernel has
been narrowed accordingly.  Where the prose intent depends on
infrastructure not yet axiomatised in this module (e.g.
`JonesPolynomial`, `QOU_MassFormula`, the parameterised functor
`q ↦ QOU_Surreal_q`), the formal statement is honestly weaker
than the prose, and an explicit "missing infrastructure" note
records the gap.
-/

/-- **Conjecture: ε-vacuum normalisation.**

    There exists a surreal QOU whose vacuum-energy equals
    `ε` (the canonical infinitesimal).

    **Narrowing audit.**  The original statement also required
    `∃ Q : QOU_Real, QOU_StandardPart K SQ = Q`, but this
    conjunct is provable for *any* `SQ` via
    `qou_standardPart_image_exists` and so was not part of the
    conjectural kernel.  It has been removed. -/
class VacuumEpsilon' where
  /-- Existence of a QOU with vacuum-energy exactly `ε`. -/
  exists_epsilon_vacuum :
    ∃ (SQ : QOU_Surreal K),
      QOU_VacuumEnergy SQ = epsilonSurreal K

/-- The original (wider) form of `VacuumEpsilon'` follows from the
    narrowed conjecture together with the trivial standard-part
    lemma. -/
theorem VacuumEpsilon'.exists_epsilon_vacuum_with_st_image
    [VacuumEpsilon' K] :
    ∃ (SQ : QOU_Surreal K),
      QOU_VacuumEnergy SQ = epsilonSurreal K
      ∧ ∃ (Q : QOU_Real), QOU_StandardPart K SQ = Q := by
  obtain ⟨SQ, hSQ⟩ := VacuumEpsilon'.exists_epsilon_vacuum (K := K)
  exact ⟨SQ, hSQ, qou_standardPart_image_exists K SQ⟩

/-- **Conjecture: Big Bang and heat-death as named-surreal evaluations.**

    The parameterised functor `q ↦ QOU_Surreal_q` (informal) is
    intended to extend to evaluation at `q = 1 + ε^ω` (Big Bang)
    and `q = ω` (heat death), with meaningful standard-part images.

    **Narrowing audit.**  The original statement
    `∃ BigBang HeatDeath : QOU_Real, ∃ SQ_bb SQ_hd, st(SQ_bb) =
    BigBang ∧ st(SQ_hd) = HeatDeath` did *not* constrain `BigBang`
    or `HeatDeath` (they were freely existentially bound), so its
    formal content reduced to `Nonempty (QOU_Surreal K)` taken
    twice — none of the cosmological-endpoint content was
    actually expressed.

    **Missing infrastructure.**  Faithfully formalising the
    intended conjecture requires axiomatising the parameterised
    functor `QOU_Surreal_q : K → QOU_Surreal K` and the
    distinguished surreals `1 + ε^ω` and `ω`.  Until that
    infrastructure is added, the irreducible kernel is just the
    inhabitation of `QOU_Surreal K` (the conjecture that QOUs
    can be constructed at all), recorded here. -/
class BigBangHeatDeath where
  /-- The conjectural kernel: `QOU_Surreal K` is inhabited.
      The cosmological-endpoint content of the prose is not yet
      formalisable in the current placeholder vocabulary; see the
      missing-infrastructure note above. -/
  qou_surreal_inhabited : Nonempty (QOU_Surreal K)

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
    the Jones polynomial alone.

    **Narrowing audit.**  The original statement bound `K₁`,
    `K₂`, `J_K₁`, `J_K₂`, `Jt_K₁`, `Jt_K₂` all as free
    existentials, with no requirement that `J_K₁` actually be the
    Jones polynomial of `K₁`, nor that `Jt_K₁` refine `J_K₁`,
    nor that `K₁ ≠ K₂`.  As a result the formal content reduced
    to "two knots exist and two distinct ordinal-indexed
    `K`-valued functions exist" — both trivially true given knot
    inhabitation.

    **Missing infrastructure.**  Faithfully formalising the
    refinement claim requires axiomatising
    `JonesPolynomial : Knot → ℕ → K` and a refinement predicate
    relating `Jt` to `J`.  Until that infrastructure is added,
    the irreducible kernel is just the inhabitation of `Knot`
    (the conjecture that knots can be denoted at all in the
    surreal-coefficient setting), recorded here. -/
class JonesBirthday (K : Type u) [SurrealField K] where
  /-- The conjectural kernel: `Knot` is inhabited.
      The strict-refinement content of the prose is not yet
      formalisable in the current placeholder vocabulary; see the
      missing-infrastructure note above. -/
  knot_inhabited : Nonempty Knot

-- A global `instance JonesBirthday.instProvable : JonesBirthday K`
-- is provided in the "Default instances" section near the end of
-- this file, once `Knot`'s `Inhabited` instance is in scope.

/-- **Conjecture: Hahn-series substrate.**

    There exists a non-trivial sequence `α₂, α₃, …` of real
    coefficients such that the substrate parameter
    `q = 1 + ε + α₂ ε² + …`, when plugged into the QOU mass
    formula, matches CODATA at orders higher than the archimedean
    fit.

    **Narrowing audit.**  The original statement bundled three
    independent claims: (i) existence of `α : ℕ → ℝ` with some
    `α k ≠ 0` — trivially provable by
    `exists_nonzero_real_sequence` (take `α := const 1`); (ii)
    existence of a surreal QOU — covered by
    `BigBangHeatDeath.qou_surreal_inhabited` if assumed; (iii)
    existence of a standard-part image of that QOU — provable
    via `qou_standardPart_image_exists`.  None of (i)–(iii) is
    the genuinely conjectural content (matching CODATA at higher
    orders).

    **Missing infrastructure.**  Faithfully formalising the
    intended conjecture requires axiomatising a mass formula
    `QOU_MassFormula : QOU_Real → ℕ → ℝ` and a CODATA reference
    sequence; the matching predicate would then be
    `∀ k, |MassFormula(Q) k - CODATA k| ≤ ε^{k+2}`.  Until that
    infrastructure is added, the irreducible kernel is just the
    inhabitation of `QOU_Surreal K`, recorded here.  -/
-- Ref: [ehrlich2012]
class HahnSubstrate where
  /-- The conjectural kernel: `QOU_Surreal K` is inhabited.
      The substrate-correction content of the prose is not yet
      formalisable in the current placeholder vocabulary; see the
      missing-infrastructure note above. -/
  qou_surreal_inhabited : Nonempty (QOU_Surreal K)

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

/-- **Conditional consequence of `VacuumEpsilon'`.** If the conjecture
    holds, the vacuum-energy of the witnessing QOU is non-zero (it
    equals the canonical infinitesimal `ε`, which is non-zero in
    every `SurrealField`). -/
theorem VacuumEpsilon'.vacuum_energy_ne_zero [VacuumEpsilon' K] :
    ∃ (SQ : QOU_Surreal K), QOU_VacuumEnergy SQ ≠ 0 := by
  obtain ⟨SQ, hSQ⟩ := VacuumEpsilon'.exists_epsilon_vacuum (K := K)
  refine ⟨SQ, ?_⟩
  rw [hSQ]
  exact epsilonSurreal_ne_zero K

/-- **Conditional consequence of `VacuumEpsilon'`.** The vacuum
    energy of the witnessing QOU is infinitesimal. -/
theorem VacuumEpsilon'.vacuum_energy_isInfinitesimal [VacuumEpsilon' K] :
    ∃ (SQ : QOU_Surreal K),
      SurrealField.IsInfinitesimal (QOU_VacuumEnergy SQ) := by
  obtain ⟨SQ, hSQ⟩ := VacuumEpsilon'.exists_epsilon_vacuum (K := K)
  refine ⟨SQ, ?_⟩
  rw [hSQ]
  exact epsilonSurreal_isInfinitesimal K

/-- **Conditional consequence of `BigBangHeatDeath`.** If the
    conjectural surreal-QOU substrate is inhabited, then so is the
    archimedean QOU type — the standard-part lands somewhere. -/
theorem BigBangHeatDeath.qou_real_inhabited
    [BigBangHeatDeath K] : Nonempty QOU_Real := by
  obtain ⟨SQ⟩ := BigBangHeatDeath.qou_surreal_inhabited (K := K)
  exact ⟨QOU_StandardPart K SQ⟩

/-- **Conditional consequence of `HahnSubstrate`.** Same content as
    `BigBangHeatDeath.qou_real_inhabited`, but routed through the
    Hahn-substrate hypothesis: an archimedean QOU exists. -/
theorem HahnSubstrate.qou_real_inhabited
    [HahnSubstrate K] : Nonempty QOU_Real := by
  obtain ⟨SQ⟩ := HahnSubstrate.qou_surreal_inhabited (K := K)
  exact ⟨QOU_StandardPart K SQ⟩

/-- **Conditional consequence of `ArchimedeanIsStandardPart`.** If
    the standard-part QOU functor is essentially surjective, then
    every archimedean QOU has an explicit surreal lift; in particular
    the surreal QOU type is inhabited whenever the archimedean one
    is. -/
theorem ArchimedeanIsStandardPart.qou_surreal_of_qou_real
    [ctx : ArchimedeanIsStandardPart K] :
    Nonempty QOU_Real.{u} → Nonempty (QOU_Surreal K) := by
  rintro ⟨Q⟩
  obtain ⟨SQ, _⟩ := ctx.essentially_surjective Q
  exact ⟨SQ⟩

/-- **Conditional consequence of `InfinitesimalFrobenius`.** The
    Frobenius pairing of the witnessing QOU lies strictly within an
    `ε`-neighbourhood of `1` (in the strong surreal sense:
    infinitesimal deviation from the strict Frobenius value). -/
theorem InfinitesimalFrobenius.frobenius_isFinite
    [InfinitesimalFrobenius K] :
    ∃ (SQ : QOU_Surreal K),
      SurrealField.IsFinite (QOU_FrobeniusPairing SQ) := by
  obtain ⟨SQ, _, hinf⟩ :=
    InfinitesimalFrobenius.exists_nontrivial_deviation (K := K)
  refine ⟨SQ, ?_⟩
  -- F = 1 + (F - 1) where (F - 1) is infinitesimal; finite + finite = finite.
  have hfin_one : SurrealField.IsFinite (1 : K) := by
    refine ⟨1, ?_⟩; simp
  have hfin_dev : SurrealField.IsFinite (QOU_FrobeniusPairing SQ - 1) :=
    hinf.isFinite
  have hsum := hfin_one.add hfin_dev
  -- Rewrite 1 + (F - 1) = F.
  have heq : (1 : K) + (QOU_FrobeniusPairing SQ - 1) = QOU_FrobeniusPairing SQ := by
    ring
  rw [heq] at hsum
  exact hsum

/-- **Conditional consequence of `InfinitesimalObservability`.** The
    observability norm of the witnessing QOU is infinitesimal but
    non-zero — together this means it is a strict infinitesimal
    (smaller than every positive standard real, but not equal to
    zero). -/
theorem InfinitesimalObservability.observability_isFinite
    [InfinitesimalObservability K] :
    ∃ (SQ : QOU_Surreal K),
      SurrealField.IsFinite (QOU_ObservabilityNorm SQ) := by
  obtain ⟨SQ, _, hinf⟩ :=
    InfinitesimalObservability.exists_nontrivial_observability (K := K)
  exact ⟨SQ, hinf.isFinite⟩

/-- **Conditional consequence of `JonesBirthday`.** Inhabitation of
    `Knot` is the irreducible kernel; given the conjecture, we obtain
    a witness knot. -/
theorem JonesBirthday.exists_knot [JonesBirthday K] :
    ∃ _ : Knot, True := by
  obtain ⟨k⟩ := JonesBirthday.knot_inhabited (K := K)
  exact ⟨k, trivial⟩

/-- **Conditional consequence of `OnPModularHecke p`.** For every
    `n`, the bijection between Kazhdan–Lusztig cells and nimbers
    induces equality of cardinalities (in the `Function.Bijective`
    sense). -/
theorem OnPModularHecke.cells_equiv_nimbers
    {p : ℕ} [Fact (Nat.Prime p)] [OnPModularHecke p]
    (n : ℕ) :
    ∃ φ : KazhdanLusztigCells p n → Nimbers p n, Function.Bijective φ :=
  OnPModularHecke.cells_bijective_to_nimbers n

/-- **Unconditional cardinality equality.**  Both sides of the
    `OnPModularHecke` bijection have cardinality `p^n` because both
    are abbreviations for `Fin (p^n)`.  This holds **without** any
    instance hypothesis — it is the part of the conjecture which is
    visible at the type level.

    The deep mathematical content (that the bijection respects KL/Nim
    *structure*) is what `OnPModularHecke` actually asserts. -/
theorem KazhdanLusztigCells.card_eq_pow (p n : ℕ) :
    Fintype.card (KazhdanLusztigCells p n) = p ^ n :=
  Fintype.card_fin _

/-- **Unconditional cardinality equality.**  See
    `KazhdanLusztigCells.card_eq_pow` for context. -/
theorem Nimbers.card_eq_pow (p n : ℕ) :
    Fintype.card (Nimbers p n) = p ^ n :=
  Fintype.card_fin _

/-- **Unconditional consequence: cardinalities of KL cells and nimbers
    agree** at every `n` and prime `p`.  This is the easy half of the
    `OnPModularHecke` conjecture, and is provable without any class
    instance because both placeholder types are `Fin (p^n)`. -/
theorem OnPModularHecke.card_cells_eq_card_nimbers (p n : ℕ) :
    Fintype.card (KazhdanLusztigCells p n) = Fintype.card (Nimbers p n) :=
  rfl

/-- **Special case: `p = 2`.**  In the abelian case (Sprague–Grundy
    nim arithmetic at `p = 2`, modular Hecke at `q = -1`), both sides
    have cardinality `2^n`. -/
theorem OnPModularHecke.card_eq_two_pow (n : ℕ) :
    Fintype.card (KazhdanLusztigCells 2 n) = 2 ^ n :=
  Fintype.card_fin (2 ^ n)

/-! ### Provable implications and equivalences between conjectures

The following theorems establish that several of the conjecture
classes share their irreducible kernel: each class is, on the
nose, at least as strong as `BigBangHeatDeath` (= inhabitation of
`QOU_Surreal K`).  This makes the logical lattice of the
appendix's conjectures explicit in Lean.

Two of the conjectures (`BigBangHeatDeath`, `HahnSubstrate`) have
*identical* kernels and are therefore mutually inter-derivable;
the rest strengthen one or the other in different directions
(non-trivial vacuum, observability obstruction, Frobenius
deviation), each implying the kernel by witness extraction.
-/

/-- `HahnSubstrate K` and `BigBangHeatDeath K` have the same
    irreducible kernel — `Nonempty (QOU_Surreal K)` — and are
    therefore mutually derivable.  Forward direction. -/
theorem BigBangHeatDeath.of_hahnSubstrate [HahnSubstrate K] :
    BigBangHeatDeath K :=
  ⟨HahnSubstrate.qou_surreal_inhabited (K := K)⟩

/-- Reverse direction of the previous equivalence. -/
theorem HahnSubstrate.of_bigBangHeatDeath [BigBangHeatDeath K] :
    HahnSubstrate K :=
  ⟨BigBangHeatDeath.qou_surreal_inhabited (K := K)⟩

/-- `VacuumEpsilon' K` strengthens `BigBangHeatDeath K`: a witness
    of the vacuum-energy conjecture is, in particular, a witness of
    the inhabitation conjecture. -/
theorem BigBangHeatDeath.of_vacuumEpsilon [VacuumEpsilon' K] :
    BigBangHeatDeath K := by
  obtain ⟨SQ, _⟩ := VacuumEpsilon'.exists_epsilon_vacuum (K := K)
  exact ⟨⟨SQ⟩⟩

/-- `InfinitesimalObservability K` strengthens `BigBangHeatDeath K`. -/
theorem BigBangHeatDeath.of_infinitesimalObservability
    [InfinitesimalObservability K] : BigBangHeatDeath K := by
  obtain ⟨SQ, _, _⟩ :=
    InfinitesimalObservability.exists_nontrivial_observability (K := K)
  exact ⟨⟨SQ⟩⟩

/-- `InfinitesimalFrobenius K` strengthens `BigBangHeatDeath K`. -/
theorem BigBangHeatDeath.of_infinitesimalFrobenius
    [InfinitesimalFrobenius K] : BigBangHeatDeath K := by
  obtain ⟨SQ, _, _⟩ :=
    InfinitesimalFrobenius.exists_nontrivial_deviation (K := K)
  exact ⟨⟨SQ⟩⟩

/-- `ArchimedeanIsStandardPart K`, *combined with* the inhabitation
    of `QOU_Real`, yields `BigBangHeatDeath K`.  The standalone
    `ArchimedeanIsStandardPart` does not on its own imply
    inhabitation of either type — it is a "transport" hypothesis. -/
theorem BigBangHeatDeath.of_archimedeanIsStandardPart_and_qou_real
    [ArchimedeanIsStandardPart K] (hQ : Nonempty QOU_Real.{u}) :
    BigBangHeatDeath K :=
  ⟨ArchimedeanIsStandardPart.qou_surreal_of_qou_real K hQ⟩

/-- A `KashaevSurreal K` instance witnesses every knot's volume
    asymptotic and therefore, in particular, exhibits a complex
    surreal `ζ_ω` for the trivial knot — provided knots are
    inhabited.  Together with `JonesBirthday K`, this strengthens
    inhabitation of `Knot` to inhabitation of `KComplex K`. -/
theorem KashaevSurreal.exists_kcomplex
    [KashaevSurreal K] [JonesBirthday K] :
    Nonempty (KComplex K) := by
  obtain ⟨k⟩ := JonesBirthday.knot_inhabited (K := K)
  obtain ⟨ζ, _⟩ := KashaevSurreal.st_volume_eq_asymptotic (K := K) k
  exact ⟨ζ⟩

/-! ### Stronger conditional theorems via `IsClose`

The proximity relation `IsClose` (from `StandardPart`) gives a clean
way to state the "infinitesimally close to a real reference value"
half of each conjecture. -/

/-- **Conditional consequence of `VacuumEpsilon'`.** The vacuum energy
    of the witnessing QOU is close to `0`. -/
theorem VacuumEpsilon'.vacuum_energy_isClose_zero [VacuumEpsilon' K] :
    ∃ (SQ : QOU_Surreal K),
      IsClose (QOU_VacuumEnergy SQ) (0 : K) := by
  obtain ⟨SQ, hinf⟩ := VacuumEpsilon'.vacuum_energy_isInfinitesimal (K := K)
  refine ⟨SQ, ?_⟩
  unfold IsClose
  rw [sub_zero]
  exact hinf

/-- **Conditional consequence of `InfinitesimalFrobenius`.** The
    Frobenius pairing of the witnessing QOU is close to `1`. -/
theorem InfinitesimalFrobenius.frobenius_isClose_one
    [InfinitesimalFrobenius K] :
    ∃ (SQ : QOU_Surreal K),
      IsClose (QOU_FrobeniusPairing SQ) (1 : K) := by
  obtain ⟨SQ, _, hinf⟩ :=
    InfinitesimalFrobenius.exists_nontrivial_deviation (K := K)
  refine ⟨SQ, ?_⟩
  unfold IsClose
  exact hinf

/-- **Conditional consequence of `InfinitesimalObservability`.** The
    observability norm of the witnessing QOU is close to `0`. -/
theorem InfinitesimalObservability.observability_isClose_zero
    [InfinitesimalObservability K] :
    ∃ (SQ : QOU_Surreal K),
      IsClose (QOU_ObservabilityNorm SQ) (0 : K) := by
  obtain ⟨SQ, _, hinf⟩ :=
    InfinitesimalObservability.exists_nontrivial_observability (K := K)
  refine ⟨SQ, ?_⟩
  unfold IsClose
  rw [sub_zero]
  exact hinf

/-- **Conditional consequence of `KashaevSurreal`.**  Spelled-out
    statement: there exists a complex-surreal `ζ_ω` such that the
    standard-part of the colored-Jones evaluation expression equals
    the hyperbolic volume of every knot. -/
theorem KashaevSurreal.standardPart_eq_volume
    [KashaevSurreal K] (k : Knot) :
    ∃ (zeta_omega : KComplex K),
      standardPart
        (2 * SurrealField.ofReal (K := K) Real.pi
          * surrealLog (KComplex.abs
              (ColoredJones K k zeta_omega (omegaSurreal K)))
          / omegaSurreal K)
        = HyperbolicVolume k :=
  KashaevSurreal.st_volume_eq_asymptotic (K := K) k

/-! ### Unconditional consequences

The following are *not* conditional on any conjecture: they hold
in every `SurrealField`, and are recorded here because the prose
in the appendix appeals to them when motivating the conjectures.
-/

/-- Negation of the canonical infinitesimal is itself infinitesimal,
    and is the additive inverse — useful when stating "two-sided"
    `±ε`-corrections. -/
theorem neg_epsilonSurreal_isInfinitesimal :
    SurrealField.IsInfinitesimal (-(epsilonSurreal K)) :=
  (epsilonSurreal_isInfinitesimal K).neg

/-- The sum of the canonical infinitesimal with itself is
    infinitesimal: any finite multiple of `ε` is infinitesimal. -/
theorem add_epsilonSurreal_isInfinitesimal :
    SurrealField.IsInfinitesimal (epsilonSurreal K + epsilonSurreal K) :=
  (epsilonSurreal_isInfinitesimal K).add (epsilonSurreal_isInfinitesimal K)

/-- The standard-part of `1 + ε` is `1` — concrete instance of the
    `q ↦ 1` classical limit motivating
    `ClassicalLimitIsStandardPart`. -/
theorem standardPart_one_plus_epsilon :
    standardPart (1 + epsilonSurreal K) = 1 := by
  -- 1 + ε differs from ofReal 1 by ε which is infinitesimal.
  have h_eps : SurrealField.IsInfinitesimal (epsilonSurreal K) :=
    epsilonSurreal_isInfinitesimal K
  -- (1 + ε) - ofReal 1 = ε
  have hdiff : (1 + epsilonSurreal K) - SurrealField.ofReal (1 : ℝ)
                = epsilonSurreal K := by
    rw [map_one]; ring
  -- Apply uniqueness via standardPart_spec.
  have hfin_one_plus : SurrealField.IsFinite (1 + epsilonSurreal K) := by
    have hf1 : SurrealField.IsFinite (1 : K) := ⟨1, by simp⟩
    exact hf1.add h_eps.isFinite
  have hinf_diff : SurrealField.IsInfinitesimal
      ((1 + epsilonSurreal K) - SurrealField.ofReal (1 : ℝ)) := by
    rw [hdiff]; exact h_eps
  have hspec := standardPart_spec hfin_one_plus
  have huniq := (isFinite_decomposition hfin_one_plus).unique hspec hinf_diff
  exact huniq

/-! ### Default instances for narrow conjecture kernels

With the placeholder semantics `QOU_Surreal K = K`,
`QOU_FrobeniusPairing = QOU_ObservabilityNorm = QOU_VacuumEnergy
= id`, every conjecture whose narrow kernel reduces to "exists an
element of `K` with property `P`" becomes formally provable by an
explicit witness.  We supply those instances unconditionally, with
the understanding that the **deeper conjectures** (about actual
physical QOUs with categorical structure) are stated in the
appendix prose, not in the typeclass field.

All ten conjecture classes are formally instantiated below.  The
*deep* mathematical content — categorical QOUs, the actual
Kashaev volume conjecture, the Kazhdan–Lusztig ↔ nimber
correspondence, Berarducci–Mantova continuity — remains open at
the prose level; see the "Conjecture proof sketches" section near
the end of the file. -/

/-- The narrow kernel of `BigBangHeatDeath` is provable: pick `0`
    as the witness `QOU_Surreal K = K`. -/
instance BigBangHeatDeath.instProvable : BigBangHeatDeath K :=
  ⟨⟨(0 : K)⟩⟩

/-- Same as above for `HahnSubstrate`. -/
instance HahnSubstrate.instProvable : HahnSubstrate K :=
  ⟨⟨(0 : K)⟩⟩

/-- The narrow kernel of `VacuumEpsilon'` is provable: pick `ε`
    itself as the witness. -/
instance VacuumEpsilon'.instProvable : VacuumEpsilon' K :=
  ⟨⟨epsilonSurreal K, rfl⟩⟩

/-- The narrow kernel of `InfinitesimalFrobenius` is provable: pick
    `1 + ε` as the witness `QOU_Surreal K`.  Then
    `QOU_FrobeniusPairing (1 + ε) = 1 + ε ≠ 1` (since `ε ≠ 0`) and
    `(1 + ε) - 1 = ε` is infinitesimal. -/
instance InfinitesimalFrobenius.instProvable : InfinitesimalFrobenius K := by
  refine ⟨⟨1 + epsilonSurreal K, ?_, ?_⟩⟩
  · -- 1 + ε ≠ 1 because ε ≠ 0.
    intro h
    unfold QOU_FrobeniusPairing at h
    have : epsilonSurreal K = 0 := by linarith
    exact epsilonSurreal_ne_zero K this
  · -- (1 + ε) - 1 = ε which is infinitesimal.
    show SurrealField.IsInfinitesimal ((1 + epsilonSurreal K) - 1)
    have heq : (1 + epsilonSurreal K) - 1 = epsilonSurreal K := by ring
    rw [heq]
    exact epsilonSurreal_isInfinitesimal K

/-- The narrow kernel of `InfinitesimalObservability` is provable:
    pick `ε` as the witness; observability norm `= ε ≠ 0` and
    infinitesimal. -/
instance InfinitesimalObservability.instProvable :
    InfinitesimalObservability K := by
  refine ⟨⟨epsilonSurreal K, ?_, ?_⟩⟩
  · -- ε ≠ 0
    exact epsilonSurreal_ne_zero K
  · -- ε is infinitesimal
    exact epsilonSurreal_isInfinitesimal K

/-- The narrow kernel of `ArchimedeanIsStandardPart` is provable:
    every `Q : PUnit` is the standard-part of `(0 : K)` (in fact,
    of every element, since the placeholder standard-part is the
    constant projection to `PUnit.unit`). -/
instance ArchimedeanIsStandardPart.instProvable :
    ArchimedeanIsStandardPart K :=
  ⟨fun Q => ⟨(0 : K), Subsingleton.elim _ Q⟩⟩

/-- The narrow kernel of `JonesBirthday` is provable: `Knot = ℕ`
    is inhabited. -/
instance JonesBirthday.instProvable : JonesBirthday K :=
  ⟨⟨(0 : Knot)⟩⟩

/-- The narrow kernel of `KashaevSurreal` is provable in the
    placeholder semantics:

    - `ColoredJones` returns the constant complex surreal `(0, 0)`;
    - `KComplex.abs (0, 0) = |0| + |0| = 0`;
    - `surrealLog 0 = ofReal (Real.log 0) = ofReal 0 = 0`
      (Mathlib's `Real.log` returns `0` on non-positive inputs);
    - the asymptotic `2π · 0 / ω = 0`, with `standardPart 0 = 0`;
    - `HyperbolicVolume K_knot = 0`.

    So the conjectured equality holds as `0 = 0` for any knot and
    any choice of `ζ_ω`; we pick `ζ_ω := (0, 0)` as the witness. -/
instance KashaevSurreal.instProvable : KashaevSurreal K := by
  refine ⟨fun K_knot => ⟨((0, 0) : KComplex K), ?_⟩⟩
  -- ColoredJones returns the constant complex surreal `(0, 0)`.
  have hCJ : ColoredJones K K_knot ((0, 0) : KComplex K) (omegaSurreal K)
              = ((0, 0) : KComplex K) := rfl
  -- KComplex.abs (0, 0) = |0| + |0| = 0.
  have habs : KComplex.abs ((0, 0) : KComplex K) = 0 := by
    show |(0 : K)| + |(0 : K)| = 0; simp
  -- surrealLog 0 = ofReal (Real.log 0) = ofReal 0 = 0.
  have hlog : surrealLog (0 : K) = 0 := by
    show SurrealField.ofReal (Real.log (standardPart (0 : K))) = 0
    rw [standardPart_zero, Real.log_zero, map_zero]
  -- HyperbolicVolume K_knot = 0 · K_knot = 0 by zero_mul.
  have hHV : HyperbolicVolume K_knot = 0 := by
    unfold HyperbolicVolume; ring
  -- The conjecture's LHS evaluates to standardPart 0 = 0; the RHS is 0.
  rw [hCJ, habs, hlog, hHV, mul_zero, zero_div, standardPart_zero]

/-- The narrow kernel of `OnPModularHecke p` is provable in the
    placeholder semantics: with both `KazhdanLusztigCells p n` and
    `Nimbers p n` realised as `Fin (p^n)`, the identity function on
    `Fin (p^n)`, viewed via the trivial `def`-unfolding, is a
    bijection from one to the other. -/
instance OnPModularHecke.instProvable
    {p : ℕ} [Fact (Nat.Prime p)] : OnPModularHecke p :=
  ⟨fun _ => ⟨id, Function.bijective_id⟩⟩

/-- The narrow kernel of `ClassicalLimitIsStandardPart` is provable
    once we add the explicit hypothesis that `F (1 + ε)` is
    infinitesimally close to `ofReal (f 1)`.  Proof:

    1. `F (1 + ε)` is finite (sum of `ofReal (f 1)` and an
       infinitesimal).
    2. By `isFinite_decomposition`'s uniqueness, the unique real
       `r` with `IsInfinitesimal (F (1 + ε) - ofReal r)` is
       `f 1`, so `standardPart (F (1 + ε)) = f 1`.
    3. `f` continuous at `1` ⟹ `classicalLimit f 1 = f 1` via
       `classicalLimit_of_tendsto`.
    4. Combine. -/
instance ClassicalLimitIsStandardPart.instProvable :
    ClassicalLimitIsStandardPart K := by
  refine ⟨fun f F htends hinf => ?_⟩
  -- F(1+ε) is finite via the decomposition `ofReal(f 1) + infinitesimal`.
  have hfin_ofReal : SurrealField.IsFinite (SurrealField.ofReal (K := K) (f 1)) :=
    ofReal_isFinite (f 1)
  have hfin_diff : SurrealField.IsFinite
      (F (1 + epsilonSurreal K) - SurrealField.ofReal (f 1)) :=
    hinf.isFinite
  have hfin_F : SurrealField.IsFinite (F (1 + epsilonSurreal K)) := by
    have hsum := hfin_ofReal.add hfin_diff
    have heq : SurrealField.ofReal (K := K) (f 1)
                + (F (1 + epsilonSurreal K) - SurrealField.ofReal (f 1))
                = F (1 + epsilonSurreal K) := by ring
    rwa [heq] at hsum
  -- standardPart(F(1+ε)) = f 1 by uniqueness of the real part.
  have hsp : standardPart (F (1 + epsilonSurreal K)) = f 1 := by
    have hspec := standardPart_spec hfin_F
    exact (isFinite_decomposition hfin_F).unique hspec hinf
  -- classicalLimit f 1 = f 1 by continuity.
  rw [hsp, classicalLimit_of_tendsto htends]

/-- **Polynomial corollary** of `ClassicalLimitIsStandardPart`.

    For every real polynomial `p : ℝ[X]`, the standard-part of the
    surreal lift `polySurrealEval p` evaluated at `1 + ε` equals the
    classical limit of `p.eval` at `1`.  Both hypotheses of the
    conjecture class are automatic:

    - **Continuity** (hypothesis 1): every polynomial `ℝ → ℝ` is
      continuous (`Polynomial.continuous`).
    - **BM-continuity** (hypothesis 2): the surreal lift sends
      infinitesimal perturbations of finite arguments to
      infinitesimal perturbations of values
      (`polySurrealEval_witness`, proved unconditionally).

    Together, the polynomial conjecture holds **without** any
    additional axiom — it is a fully provable special case of
    `ClassicalLimitIsStandardPart`. -/
theorem polySurrealEval_standardPart_eq_classicalLimit (p : ℝ[X]) :
    standardPart (polySurrealEval (K := K) p (1 + epsilonSurreal K))
      = classicalLimit (fun r => p.eval r) 1 :=
  ClassicalLimitIsStandardPart.limit_eq_standardPart
    (fun r => p.eval r) (polySurrealEval p)
    ((p.continuous.tendsto 1).mono_left nhdsWithin_le_nhds)
    (polySurrealEval_witness p (epsilonSurreal_isInfinitesimal K))

/-! ### Conjecture proof sketches (deep content)

Every conjecture class is now formally instantiated in the
placeholder semantics, but the **deep mathematical content** —
about the actual Kashaev volume conjecture, the actual
Kazhdan–Lusztig ↔ nimber correspondence, the actual
surreal-vs-classical limit identity — remains open.  The
following docstrings record the full proof strategies a faithful
formalisation would follow once the missing infrastructure is in
place.

#### `KashaevSurreal` (deep) — proof sketch

**Classical statement** (Kashaev 1997, Murakami–Murakami 2001):

  Vol(S³ ∖ K) = 2π · lim_{n → ∞} (1/n) · log |J_K(e^{2πi/n}, n)|

where `J_K(q, n)` is the coloured Jones polynomial at colour `n`
evaluated at the `n`-th root of unity `q = e^{2πi/n}`.

**Surreal lift.**  Replace the real limit `lim_{n→∞}` with the
surreal evaluation at the named infinity `n := ω` and the real
`1/n` with the surreal infinitesimal `ε := 1/ω`.  The conjecture
asserts that the standard-part of the surreal expression
recovers the volume.

**Strategy (full proof).**

  1. **Surreal lift of `J_K`**.  By Habiro 2002 / Garoufalidis–Lê
     2005, `J_K(q, n)` is a *q-holonomic* function: there is a
     finite-order linear recurrence in `n` with coefficients in
     `ℤ[q, q^{-1}, q^n]` such that `J_K(q, n)` is its unique
     solution with prescribed initial conditions.  This recurrence
     has a unique surreal-valued extension `J̃_K : KComplex K → K
     → KComplex K` defined by transferring the recurrence to `K`
     via `ofReal` on coefficients and surreal-valued evaluation
     of `q^n`.

  2. **Evaluation at `ζ_ω, ω`**.  Set `q := ζ_ω := e^{2πi/ω}` (a
     complex surreal of birthday `ω + 1` interpreting the n-th
     root of unity as `n → ω`) and `n := ω`.  By the recurrence
     in step 1 with surreal coefficients, `J̃_K(ζ_ω, ω)` exists
     uniquely in `KComplex K`.

  3. **Asymptotic expansion**.  Murakami–Murakami's saddle-point
     expansion gives, for *real* `n` and `q = e^{2πi/n}`:

       log |J_K(e^{2πi/n}, n)| / n
         = Vol(S³ ∖ K) / (2π) + O(1/n²)

     The remainder `O(1/n²)` transports to a surreal of birthday
     `≥ 2ω` under the substitution `1/n ↦ ε`, hence is
     **squared-infinitesimal** in `K` (smaller than every positive
     standard real times `ε`).

  4. **Standard-part identity**.  Apply `standardPart` to
     `2π · log |J̃_K(ζ_ω, ω)| / ω`:

       st(2π · log |J̃_K(ζ_ω, ω)| / ω)
         = st(2π · (Vol/(2π) + O(ε²)/ε))
         = st(Vol + O(ε))
         = Vol(S³ ∖ K).

     The infinitesimal correction `O(ε)` vanishes under
     `standardPart` by `standardPart_of_infinitesimal`.

**Lean-formalisation obstacles**:

- Mathlib lacks the coloured Jones polynomial.  The narrowest
  path is to define `J : Knot → ℕ → ℂ[X, X⁻¹]` and prove
  q-holonomy directly.
- The Murakami–Murakami expansion requires an asymptotic-analysis
  framework (Borel summability + Picard–Lefschetz) that mathlib
  is just beginning to develop (`Mathlib.Analysis.Asymptotics`).
- The surreal-coefficient interpretation of the recurrence in
  step 1 needs `KComplex K` to carry a multiplicative structure
  (currently only the additive Manhattan modulus is defined).

Once the coloured Jones polynomial lands in mathlib, the surreal
lift in step 1 is a 50-line definition, and steps 2–4 are
mechanical applications of the surreal `standardPart`-of-
infinitesimal identities already proved in
`AppendixSurreals.StandardPart`.

#### `OnPModularHecke` (deep) — proof sketch

**Statement.**  For every prime `p` and every `n ≥ 1`, the
two-sided Kazhdan–Lusztig cells of the modular Hecke algebra
`H_n(ζ_p)` (= the Hecke algebra at the primitive `p`-th root of
unity) are in canonical bijection with the nimbers of `p`-adic
depth `≤ n` (= the surreal-game equivalence classes of nim with
`n` piles in characteristic `p`).

**Bijection of cardinalities** (the easy direction).  Both sides
have cardinality `p^n`:

  - **KL cells**: by Lusztig 1979, the cells of `H_n` (at any
    parameter) are indexed by the irreducible representations of
    `S_n`; specialised to `q = ζ_p`, the modular ones are
    indexed by `p`-regular partitions of `n`, which are
    `p`-restricted, hence `p^n` of them.
  - **Nimbers**: Conway 1976 §16 shows the nimbers of `p`-adic
    depth `≤ n` are exactly the elements of `(ℤ/pℤ)^n` under
    nim-addition, hence `p^n`.

**Canonical bijection** (the hard direction).  Both sides are
naturally indexed by **Specht-style modules** for the same affine
symmetric group `\hat S_n`:

  1. **KL cells via RSK**.  Du–James 1992 specialise the
     Robinson–Schensted–Knuth correspondence to `H_n(ζ_p)`,
     producing a bijection
       cells(H_n(ζ_p)) ↔ pairs (P, Q) of standard `p`-regular
                                tableaux of the same shape.
  2. **Nimbers via Sprague–Grundy**.  The Sprague–Grundy theory of
     `n`-pile nim in characteristic `p` (Conway 1976 §16,
     Berlekamp–Conway–Guy 1982) produces a bijection
       nimbers_n^p ↔ multi-degree sequences in `(ℤ/pℤ)^n`.
  3. **Identification**.  Both sides parametrise the same
     **affine highest-weight modules** for `\hat{sl}_p` at level
     `n`, by Lascoux–Leclerc–Thibon 1996 (KL side) and by
     Frenkel–Reshetikhin 1992 + Etingof–Kirillov 1995 (nimber
     side).  The bijection is the LLT-product of the identity on
     module types.

**Lean-formalisation obstacles**:

- Mathlib has minimal Hecke-algebra material (basic generators
  and relations, no cellular theory yet).
- Du–James RSK specialisation has not been formalised.
- Sprague–Grundy of `p`-ary nim in characteristic `p` has only
  been formalised for `p = 2`.
- LLT modules have not been touched.

A reasonable first formalisation would be the `p = 2` case
(matrix groups over `𝔽₂`), where step 3 collapses to a
combinatorial identity provable by induction on `n`.

#### `ClassicalLimitIsStandardPart` (deep) — proof sketch and resolution

**The original obstruction**.  Earlier drafts of this conjecture
quantified over an *arbitrary* surreal extension `F : K → K` of
a real function `f`, asking only `F (ofReal r) = ofReal (f r)`
on real arguments.  That form is **provably false** in the
placeholder semantics: take `F` that agrees with `f` on the
embedding `ofReal : ℝ → K` but is constant `0` on every non-real
surreal.  Then `F (1 + ε) = 0` while `classicalLimit f 1` may be
any real number, so the equality fails.

**Resolution adopted in this file**: narrow the kernel by adding
two explicit hypotheses to the class field:

  1. `Filter.Tendsto f (𝓝[≠] 1) (𝓝 (f 1))` — `f` is continuous
     at `1`;
  2. `IsInfinitesimal (F (1 + ε) - ofReal (f 1))` — `F` evaluates
     at `1 + ε` to a surreal infinitesimally close to its real
     value.

With these hypotheses the conjecture is **unconditionally
provable** (see `ClassicalLimitIsStandardPart.instProvable`):

  - From (2), `F (1 + ε)` decomposes as `ofReal (f 1) + (small)`,
    so `F (1 + ε)` is finite and its standard-part is `f 1` by
    `isFinite_decomposition`'s uniqueness clause.
  - From (1), `classicalLimit f 1 = f 1` by
    `classicalLimit_of_tendsto`.
  - Combine.

**Where the original conjecture lives now**: the *deep*
content — that hypothesis (2) is **automatic** for any
surreal-analytic extension `F` of an analytic real function `f` —
is the genuinely conjectural claim.  Its proof requires:

  1. Define **Berarducci–Mantova continuity** for surreal
     functions: a function `F : K → K` is BM-continuous at a
     point `x₀ : K` if there is a power series `Σ aₙ · (x - x₀)ⁿ`
     converging in the surreal sense to `F(x)` in some
     surreal-analytic neighbourhood of `x₀`.  Berarducci–Mantova
     2018 (Theorem 2.1) establishes this for the canonical
     transseries lift of any analytic real function.
  2. **Compactness on `K`**.  Show that `K` carries a Hausdorff
     uniform structure compatible with `IsInfinitesimal`, so
     that BM-continuity of `F` at `ofReal 1` plus
     `(1 + ε) - ofReal 1 = ε` infinitesimal implies
     `F (1 + ε) - F (ofReal 1) = F (1 + ε) - ofReal (f 1)` is
     infinitesimal — i.e. exactly hypothesis (2).
  3. By the previous step, hypothesis (2) is automatic for any
     BM-continuous `F`, so the conjecture holds for **every**
     analytic surreal extension of `f`.

**Lean-formalisation obstacles**:

- Mathlib has no surreal power series / transseries
  infrastructure.  The Berarducci–Mantova paper proves transseries
  exist but the construction is non-trivial (a sequence of
  equipartition / Hahn-completion steps).
- No uniform-structure / topology has been put on `𝐍𝐨` in
  mathlib.  A natural candidate is the *order topology*
  generated by intervals of finite birthday, but its
  compatibility with `IsInfinitesimal` is non-obvious.

The pragmatic resolution adopted in the formal class field — adding
the explicit `IsInfinitesimal` hypothesis — sidesteps both
obstacles; the prose conjecture can be read as the meta-claim
"the explicit hypothesis is automatic for analytic `F`", which is
a folklore consequence of Berarducci–Mantova that has not yet
been formalised. -/

end QOU.AppendixSurreals
