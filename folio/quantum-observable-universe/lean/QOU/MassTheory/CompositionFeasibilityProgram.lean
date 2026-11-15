/-
# The composition feasibility program, posed

Owner (2026-09-16): "Pose the composition feasibility program." Every LP/SDP in the
corpus is a *verification* or *ranking* program on a given composite
(`docs/audits/2026-09-16-sdp-analysis-entangled-deviation-and-light-cone-recursion.md`
§2, §5); the substrate-phase picture needs a *composition* program — marginals and an
interface letter in, composite out. Posed here with no objective:

* **data** — branching data `B` (two marginals inside a composite through the free
  product) and a finite alphabet `L` of interface letters, each acting on the composite
  algebra, with a unit letter that acts trivially;
* **variable** — a letter `ℓ : L`;
* **composite** — `act ℓ (a ⊗ b)`;
* **feasible set** — reading 3, whole word (owner rulings 2026-09-12/13): the composite's
  character is non-negative on every block of positive weight.

Proved: under reading 3 and a probability weight vector the composite's trace is
non-negative (`trM_nonneg_of_reading3`), so a feasible letter's weighted deviation is
bounded below by `−tr_M(a) tr_M(b)` (`weighted_letterDeviation_ge`); the unit letter is
feasible iff the free product is reading-3 feasible (`feasible_unit_iff`); the unit
letter's deviation vanishes (`letterDeviation_unit`).

Measured on `main` (bean `qou-7dal`, `branching_pushforward_entangled_support_probe.py`):
every free product passes reading 3 and every production bound word fails it, so the
production interface letters are **infeasible** at `A = 2, 3, 4` under this feasible set.
The one-parameter alphabet `(1 − e)σ + eσ⁻¹` (`InterfaceLetterCrossingMixture.lean`) is
enumerated at `A = 2` by `composition_feasibility_a2_probe.py`. Nothing here supplies an
objective; the Möbius objective's gap is bean `qou-ypc5`. Bean `qou-8r6b`.

-- Ref: [leitner2026] prop:operator-selection-lp; def:markov-axioms-primitive
-/
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import QOU.MassTheory.BranchingPushforwardMultiplicativity

namespace QOU.MassTheory.BlockMeasure

open Finset

section Reading3

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
variable {A : Type*} [Ring A] {Λ : Type*} [Fintype Λ]

/-- **Reading 3, whole word**: the character of `x` is non-negative on every block of
positive weight. -/
def FrobeniusPairingData.Reading3 (D : FrobeniusPairingData R A Λ) (x : A) : Prop :=
  ∀ l, 0 < D.y l → 0 ≤ D.χ l x

/-- Under reading 3 and non-negative weights the Markov trace is non-negative. -/
theorem FrobeniusPairingData.trM_nonneg_of_reading3 (D : FrobeniusPairingData R A Λ)
    (hy : D.IsProbability) {x : A} (hx : D.Reading3 x) : 0 ≤ D.trM x := by
  rw [D.pairing]
  refine sum_nonneg fun l _ => ?_
  rcases (hy l).lt_or_eq with hpos | hzero
  · exact mul_nonneg (hy l) (hx l hpos)
  · rw [← hzero, zero_mul]

end Reading3

/-- **The composition feasibility program**: two marginals inside a composite, and a
finite alphabet of interface letters acting on the composite algebra, with a unit letter. -/
structure CompositionProgram (R : Type*) [CommRing R]
    (A₁ A₂ A : Type*) [Ring A₁] [Ring A₂] [Ring A]
    (Λ₁ Λ₂ Λ : Type*) [Fintype Λ₁] [Fintype Λ₂] [Fintype Λ]
    (L : Type*) [Fintype L] where
  /-- The two marginals inside the composite. -/
  B : BranchingData R A₁ A₂ A Λ₁ Λ₂ Λ
  /-- The interface alphabet, acting on the composite algebra. -/
  act : L → A → A
  /-- The unit letter. -/
  unit : L
  /-- The unit letter acts trivially. -/
  act_unit : ∀ x, act unit x = x

namespace CompositionProgram

variable {R : Type*} [CommRing R]
variable {A₁ A₂ A : Type*} [Ring A₁] [Ring A₂] [Ring A]
variable {Λ₁ Λ₂ Λ : Type*} [Fintype Λ₁] [Fintype Λ₂] [Fintype Λ]
variable {L : Type*} [Fintype L]
variable (P : CompositionProgram R A₁ A₂ A Λ₁ Λ₂ Λ L)

/-- The composite produced by the letter `ℓ` from the marginals `a`, `b`. -/
def composite (ℓ : L) (a : A₁) (b : A₂) : A := P.act ℓ (P.B.tensor a b)

/-- The block-resolved deviation of the letter's composite from the free product. -/
def letterDeviation (ℓ : L) (a : A₁) (b : A₂) (l : Λ) : R :=
  P.B.deviation (P.composite ℓ a b) a b l

/-- The unit letter's deviation vanishes on every block. -/
theorem letterDeviation_unit (a : A₁) (b : A₂) (l : Λ) :
    P.letterDeviation P.unit a b l = 0 := by
  unfold letterDeviation composite BranchingData.deviation
  rw [P.act_unit, sub_self]

end CompositionProgram

/-! ### The ordered part — over a linearly ordered field, matching `IsProbability` upstream -/

namespace CompositionProgram

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R]
variable {A₁ A₂ A : Type*} [Ring A₁] [Ring A₂] [Ring A]
variable {Λ₁ Λ₂ Λ : Type*} [Fintype Λ₁] [Fintype Λ₂] [Fintype Λ]
variable {L : Type*} [Fintype L]
variable (P : CompositionProgram R A₁ A₂ A Λ₁ Λ₂ Λ L)

/-- **The feasible set**: reading 3 on the letter's composite. -/
def Feasible (ℓ : L) (a : A₁) (b : A₂) : Prop := P.B.D.Reading3 (P.composite ℓ a b)

omit [IsStrictOrderedRing R] in
/-- The unit letter is feasible iff the free product itself satisfies reading 3. -/
theorem feasible_unit_iff (a : A₁) (b : A₂) :
    P.Feasible P.unit a b ↔ P.B.D.Reading3 (P.B.tensor a b) := by
  unfold Feasible composite
  rw [P.act_unit]

/-- A feasible letter's composite has non-negative trace. -/
theorem trM_composite_nonneg (hy : P.B.D.IsProbability) {ℓ : L} {a : A₁} {b : A₂}
    (h : P.Feasible ℓ a b) : 0 ≤ P.B.D.trM (P.composite ℓ a b) :=
  P.B.D.trM_nonneg_of_reading3 hy h

/-- **A feasible letter's weighted deviation is bounded below by minus the free trace.**
`−tr_M(a) tr_M(b) ≤ Σ_λ y_λ δ_λ(ℓ)`: reading 3 forbids the letter from cancelling the free
product's trace entirely. -/
theorem weighted_letterDeviation_ge (hy : P.B.D.IsProbability) {ℓ : L} {a : A₁} {b : A₂}
    (h : P.Feasible ℓ a b) :
    -(P.B.D₁.trM a * P.B.D₂.trM b) ≤ ∑ l, P.B.D.y l * P.letterDeviation ℓ a b l := by
  have h0 := P.trM_composite_nonneg hy h
  rw [P.B.trM_eq_tensor_add_weighted_deviation (P.composite ℓ a b) a b] at h0
  unfold letterDeviation
  linarith

/-- The feasible letters for a given pair of marginals. -/
noncomputable def feasibleSet (a : A₁) (b : A₂) : Finset L :=
  open Classical in univ.filter fun ℓ => P.Feasible ℓ a b

end CompositionProgram

end QOU.MassTheory.BlockMeasure
