import QOU.BraidKnot.HabiroNewtonLadder

/-!
# QOU.BraidKnot.AJFigureEight

**The AJ conjecture at the QOU anchor knot, stated concretely.**

Part of the "AJ in QOU, fully and honestly" tranche
(`docs/audits/2026-07-03-aj-conjecture-dialog-assessment.md`).  The corpus's
existing AJ carrier (`QuantumAPolynomial` in
`stochastic-mechanics/phi-q-aj-machinery-identification.lean`) is a
degree-placeholder; with `coloredJones41` now a concrete Lean object
(`QOU.BraidKnot.HabiroNewtonLadder`, sorry-free), the AJ statement can be
made **content-bearing** for the figure-eight: an explicit q-difference
operator structure, the annihilation property against the actual colored
Jones tower, and the strong-AJ q→1 specialization against the explicit
classical A-polynomial
`A_{4₁}(L, M) = M⁴L² − (M⁸ − M⁶ − 2M⁴ − M² + 1)L + M⁴` (CCGLS tables).

## Honest status (§3b)

* Everything in this file is **sorry-free**; the open/literature content
  lives in the class `StrongAJFigureEight`, which carries the statement of
  the theorem PROVED in the literature — Ref: [nguyen-tran-2021]
  (strong AJ for 4₁) — as §3b class fields.  **No instance is fabricated**:
  instantiating the class requires transcribing the explicit
  Garoufalidis–Koutschan operator, which is queued (bean lineage `cp4i`;
  empirical reconstruction: `computations/aj_figure_eight_operator_construct_verify.py`).
* The derived theorems genuinely *derive* (∃-packaging, bar transport via
  the proved `coloredJones41_bar_symmetric`) — they do not merely project a
  class field (§3b-cond non-degeneracy).
* For the Borromean `𝓑₃` the AJ input stays OPEN, consistent with
  `phi-q-aj-machinery-identification.lean` (no instance there either).

## Base ring (§7c)

Generic `{K : Type*} [Field K]` throughout (inverses needed); no `ℝ`, no
ordering, no archimedean constructs.  The q→1 specialization is evaluation
at `1 : K` — algebraic, not a limit.
-/

namespace QOU.BraidKnot.AJFigureEight

open Finset
open QOU.BraidKnot.HabiroNewtonLadder

variable {K : Type*} [Field K]

/-- An (inhomogeneous) q-difference operator acting on color towers:
    `order`, coefficient functions `coeff j q m` of the deformation
    parameter `q` and the multiplication variable `m = q^N`, and an
    inhomogeneous part `rhs q m` (`0` for a homogeneous operator). -/
structure QDifferenceOperator (K : Type*) [Field K] where
  /-- The order (L̂-degree) of the operator. -/
  order : ℕ
  /-- Coefficient of the `j`-th shift, as a function of `(q, m)`. -/
  coeff : ℕ → K → K → K
  /-- Inhomogeneous right-hand side, as a function of `(q, m)`. -/
  rhs : K → K → K

/-- `op` annihilates the tower `J` at deformation parameter `q`:
    `∑_j coeff_j(q, q^N) · J(N+j) = rhs(q, q^N)` for every color `N`. -/
def Annihilates (op : QDifferenceOperator K) (q : K) (J : ℕ → K) : Prop :=
  ∀ N : ℕ,
    ∑ j ∈ Finset.range (op.order + 1), op.coeff j q (q ^ N) * J (N + j)
      = op.rhs q (q ^ N)

/-- Non-triviality of `op` at `q`: the top coefficient is not identically
    zero in `m`. -/
def NontrivialAt (op : QDifferenceOperator K) (q : K) : Prop :=
  ∃ m : K, op.coeff op.order q m ≠ 0

/-- A tower `J` is q-holonomic at `q` when some non-trivial q-difference
    operator annihilates it — the existence half of the AJ machinery
    (a THEOREM for all knots, Garoufalidis–Lê 2005; here stated as the
    target predicate). -/
def IsQHolonomic (q : K) (J : ℕ → K) : Prop :=
  ∃ op : QDifferenceOperator K, NontrivialAt op q ∧ Annihilates op q J

/-- The classical A-polynomial of the figure-eight knot, as an explicit
    two-variable polynomial function (CCGLS tables):
    `A_{4₁}(L, M) = M⁴L² − (M⁸ − M⁶ − 2M⁴ − M² + 1)L + M⁴`. -/
def aPolyFigureEight (L M : K) : K :=
  M ^ 4 * L ^ 2 - (M ^ 8 - M ^ 6 - 2 * M ^ 4 - M ^ 2 + 1) * L + M ^ 4

/-- **Strong AJ for the figure-eight (§3b class; literature theorem,
    instance not fabricated).**  Carries, as content-bearing fields, the
    statement proved in the literature (Ref: [nguyen-tran-2021]): an
    explicit order-2 inhomogeneous q-difference operator annihilates the
    colored Jones tower of `4₁` for every `q ≠ 0`, and its homogeneous part
    evaluated at `q = 1` equals the classical A-polynomial up to a nonzero
    unit factor `unit m`.  Instantiating the class = transcribing the
    explicit Garoufalidis–Koutschan operator and discharging these fields
    (queued; empirical reconstruction in
    `computations/aj_figure_eight_operator_construct_verify.py`). -/
class StrongAJFigureEight (K : Type*) [Field K] where
  /-- The annihilating operator (explicit in the literature). -/
  op : QDifferenceOperator K
  /-- The inhomogeneous presentation has order 2. -/
  order_eq : op.order = 2
  /-- Non-trivial at every `q ≠ 0`. -/
  nontrivial : ∀ q : K, q ≠ 0 → NontrivialAt op q
  /-- Annihilates the (concrete, Lean-defined) colored Jones tower of `4₁`
      at every `q ≠ 0`. -/
  annihilates : ∀ q : K, q ≠ 0 →
    Annihilates op q (coloredJones41 q)
  /-- The strong-AJ unit factor relating the `q = 1` specialization to the
      classical A-polynomial. -/
  unit : K → K
  /-- The unit factor is nonvanishing away from `m = 0`. -/
  unit_ne_zero : ∀ m : K, m ≠ 0 → unit m ≠ 0
  /-- **Specialization (the AJ content)**: at `q = 1` the homogeneous part
      of the operator equals `unit m · A_{4₁}(L, m)` as a function of
      `(L, m)`. -/
  specializes : ∀ L m : K,
    op.coeff 2 1 m * L ^ 2 + op.coeff 1 1 m * L + op.coeff 0 1 m
      = unit m * aPolyFigureEight L m

/-- **Derived (conditional on the literature class): the figure-eight
    colored Jones tower is q-holonomic at every `q ≠ 0`.**  Genuinely
    derived ∃-packaging of the class data (§3b-cond non-degenerate). -/
theorem coloredJones41_qholonomic [inst : StrongAJFigureEight K]
    {q : K} (hq : q ≠ 0) :
    IsQHolonomic q (coloredJones41 q) :=
  ⟨inst.op, inst.nontrivial q hq, inst.annihilates q hq⟩

/-- **Bar transport of annihilators (unconditional — uses the PROVED bar
    symmetry of the tower).**  Any operator annihilating the figure-eight
    tower at `q⁻¹` annihilates the *same numerical tower* as at `q`: by
    `coloredJones41_bar_symmetric` the two towers coincide pointwise, so
    the bar involution moves annihilators without changing the annihilated
    object.  This is the operator-level face of the amphichirality of
    `4₁`. -/
theorem annihilates_bar_transport (op : QDifferenceOperator K)
    {q : K} (hq : q ≠ 0)
    (h : Annihilates op q⁻¹ (coloredJones41 q⁻¹)) :
    Annihilates op q⁻¹ (coloredJones41 q) := by
  intro N
  have hN := h N
  simpa only [coloredJones41_bar_symmetric hq] using hN

/-- **Derived (conditional): q-holonomicity transports across the bar
    involution** — the tower is q-holonomic at `q⁻¹` with the SAME tower
    values as at `q`. -/
theorem coloredJones41_qholonomic_bar [inst : StrongAJFigureEight K]
    {q : K} (hq : q ≠ 0) :
    IsQHolonomic q⁻¹ (coloredJones41 q) :=
  ⟨inst.op, inst.nontrivial q⁻¹ (inv_ne_zero hq),
    annihilates_bar_transport inst.op hq
      (inst.annihilates q⁻¹ (inv_ne_zero hq))⟩

/-- Sanity: the classical A-polynomial reference is the stated explicit
    polynomial (definitional anchor for reviewers diffing against CCGLS). -/
theorem aPolyFigureEight_def (L M : K) :
    aPolyFigureEight L M
      = M ^ 4 * L ^ 2 - (M ^ 8 - M ^ 6 - 2 * M ^ 4 - M ^ 2 + 1) * L + M ^ 4 :=
  rfl

end QOU.BraidKnot.AJFigureEight
