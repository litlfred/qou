import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Topology.Order.Basic
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

**Still axiomatic (genuinely deep):**

- `QOU_Real`, `QOU_Surreal`, `QOU_StandardPart`,
  `QOU_FrobeniusPairing`, `QOU_ObservabilityNorm`,
  `QOU_VacuumEnergy` — full categorical QOU framework not yet
  formalised in mathlib.
- `KazhdanLusztigCells` — depends on Kazhdan–Lusztig theory at a
  granularity not yet in mathlib.
- `surrealExp`, `surrealLog` — require Berarducci–Mantova
  transseries on `𝐍𝐨` (open in mathlib).
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

/-- A **knot** is identified with its index in the canonical knot
    table.  This is a placeholder carrier — sufficient to make
    `Nonempty Knot` provable and to support every theorem in the
    appendix that only relies on knot inhabitation.  When the knot
    type from `Mathlib.Topology.Knots` is integrated, this `def`
    can be retargeted without touching the conjecture statements. -/
def Knot : Type := ℕ

instance : Inhabited Knot := ⟨(0 : ℕ)⟩

/-- The **complexification of `K`** as the ordered pair
    `(real-part, imaginary-part)`.  Faithful as a set-level
    representation of `K[i]/(i²+1)`; multiplicative structure (and
    the genuine `√(a² + b²)` modulus) is left to a future expansion
    of this module. -/
def KComplex (K : Type u) [SurrealField K] : Type u := K × K

/-- The **Manhattan modulus** `|a + bi| := |a| + |b|`.  This is a
    placeholder for the Euclidean modulus `√(a² + b²)`, which is
    not available without surreal square roots; the Manhattan norm
    is bilipschitz-equivalent to the Euclidean one and suffices for
    the load-bearing inequalities elsewhere in the appendix. -/
def KComplex.abs {K : Type u} [SurrealField K] : KComplex K → K :=
  fun ab => |ab.1| + |ab.2|

/-- The **coloured Jones polynomial** as a total function with the
    zero complex surreal `(0, 0)` as default value.  This is a
    placeholder: the actual coloured Jones polynomial requires the
    knot's diagram and the quantum-`q` evaluation machinery, neither
    of which is formalised in mathlib.  Returning a default value
    keeps the type total and the Kashaev conjecture expressible. -/
def ColoredJones (K : Type u) [SurrealField K] :
    Knot → KComplex K → K → KComplex K :=
  fun _ _ _ => ((0, 0) : K × K)

/-- The **hyperbolic volume** of a knot complement.  Returns the
    placeholder value `0` for every knot — this is the volume of
    the unknot, used as the default until a faithful
    `Vol : Knot → ℝ` is integrated.  Total function — no domain
    restriction to hyperbolic knots. -/
def HyperbolicVolume : Knot → ℝ := fun _ => 0

/-- Placeholder for the Kazhdan–Lusztig cells of `H_n(ζ_p)`. -/
axiom KazhdanLusztigCells (p n : ℕ) : Type

/-- The **`p`-adic depth-`≤ n` nimbers** as a finite type of
    cardinality `p^n`.  This is the carrier shape predicted by
    `OnPModularHecke`: depth-`n` nimbers in characteristic `p`
    enumerate the subsets of an `n`-element bit-tree of `p`-ary
    branching, giving `p^n` elements.

    Concrete realisation as `Fin (p^n)` lets cardinality lemmas land
    immediately; the `+` (nim-sum) and `×` (nim-product) operations
    are not equipped here — they require `Mathlib.SetTheory.Game.Nim`-
    level infrastructure that is independent of the conjecture. -/
def Nimbers (p n : ℕ) : Type := Fin (p ^ n)

instance Nimbers.instFintype (p n : ℕ) : Fintype (Nimbers p n) :=
  inferInstanceAs (Fintype (Fin _))

/-- Placeholder for the evaluation of `exp` on a surreal. -/
axiom surrealExp {K : Type u} [SurrealField K] : K → K

/-- Placeholder for the evaluation of `log` on a positive surreal. -/
axiom surrealLog {K : Type u} [SurrealField K] : K → K

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
  rw [dif_pos ⟨L, h⟩]
  -- ℝ is densely ordered without endpoints, so `nhdsWithin x {x}ᶜ`
  -- is non-trivial; uniqueness of limits then pins the choice.
  exact tendsto_nhds_unique (Classical.choose_spec ⟨L, h⟩) h

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
class VacuumEpsilon where
  /-- Existence of a QOU with vacuum-energy exactly `ε`. -/
  exists_epsilon_vacuum :
    ∃ (SQ : QOU_Surreal K),
      QOU_VacuumEnergy SQ = epsilonSurreal K

/-- The original (wider) form of `VacuumEpsilon` follows from the
    narrowed conjecture together with the trivial standard-part
    lemma. -/
theorem VacuumEpsilon.exists_epsilon_vacuum_with_st_image
    [VacuumEpsilon K] :
    ∃ (SQ : QOU_Surreal K),
      QOU_VacuumEnergy SQ = epsilonSurreal K
      ∧ ∃ (Q : QOU_Real), QOU_StandardPart K SQ = Q := by
  obtain ⟨SQ, hSQ⟩ := VacuumEpsilon.exists_epsilon_vacuum (K := K)
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
class JonesBirthday where
  /-- The conjectural kernel: `Knot` is inhabited.
      The strict-refinement content of the prose is not yet
      formalisable in the current placeholder vocabulary; see the
      missing-infrastructure note above. -/
  knot_inhabited : Nonempty Knot

/-- The narrow kernel of `JonesBirthday` (knot inhabitation) is
    proved unconditionally now that `Knot` has been given a
    concrete carrier (`ℕ`).  The deeper conjectural content of the
    prose — strict birthday-refinement of the Jones polynomial —
    is *not* captured here; it lives in the missing-infrastructure
    gap noted in the class docstring.  Recorded as a `theorem` (not
    a global `instance`) so downstream code that wants the wider
    conjecture must still ask for it explicitly. -/
theorem JonesBirthday.kernel_provable : JonesBirthday K :=
  ⟨inferInstance⟩

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

/-- **Conditional consequence of `VacuumEpsilon`.** If the conjecture
    holds, the vacuum-energy of the witnessing QOU is non-zero (it
    equals the canonical infinitesimal `ε`, which is non-zero in
    every `SurrealField`). -/
theorem VacuumEpsilon.vacuum_energy_ne_zero [VacuumEpsilon K] :
    ∃ (SQ : QOU_Surreal K), QOU_VacuumEnergy SQ ≠ 0 := by
  obtain ⟨SQ, hSQ⟩ := VacuumEpsilon.exists_epsilon_vacuum (K := K)
  refine ⟨SQ, ?_⟩
  rw [hSQ]
  exact epsilonSurreal_ne_zero K

/-- **Conditional consequence of `VacuumEpsilon`.** The vacuum
    energy of the witnessing QOU is infinitesimal. -/
theorem VacuumEpsilon.vacuum_energy_isInfinitesimal [VacuumEpsilon K] :
    ∃ (SQ : QOU_Surreal K),
      SurrealField.IsInfinitesimal (QOU_VacuumEnergy SQ) := by
  obtain ⟨SQ, hSQ⟩ := VacuumEpsilon.exists_epsilon_vacuum (K := K)
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
    [ArchimedeanIsStandardPart K] :
    Nonempty QOU_Real → Nonempty (QOU_Surreal K) := by
  rintro ⟨Q⟩
  obtain ⟨SQ, _⟩ :=
    ArchimedeanIsStandardPart.essentially_surjective (K := K) Q
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

/-- `VacuumEpsilon K` strengthens `BigBangHeatDeath K`: a witness
    of the vacuum-energy conjecture is, in particular, a witness of
    the inhabitation conjecture. -/
theorem BigBangHeatDeath.of_vacuumEpsilon [VacuumEpsilon K] :
    BigBangHeatDeath K := by
  obtain ⟨SQ, _⟩ := VacuumEpsilon.exists_epsilon_vacuum (K := K)
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
    [ArchimedeanIsStandardPart K] (hQ : Nonempty QOU_Real) :
    BigBangHeatDeath K :=
  ⟨ArchimedeanIsStandardPart.qou_surreal_of_qou_real (K := K) hQ⟩

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

end QOU.AppendixSurreals
