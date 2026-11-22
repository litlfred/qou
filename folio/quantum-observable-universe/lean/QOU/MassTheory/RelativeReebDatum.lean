/-
# Relative Reeb datum — a primary conjecture class (owner, 2026-09-16), no instance

The corpus has a single-knot Reeb angle per irrep
(`QOU.BraidsAndKnots.BringFiberActionInstance.reebAngle`, `θ_λ = arccos(χ_λ(C₅)/dim λ)`)
and no datum relating *two* knots' flows (bean `qou-jfx8`; the q-stochastic analysis,
ingredient I6). The owner's specification: the relative angle between two knot particles
"is the evaluation/trace of the substrate phase space at the point", the phase space
being the common entanglement light cone of the two histories; the knot convolution is
`a ⋈_{⟨K, phase⟩} b`; with no prior shared γγ history the phase space contributes nothing.

Encoded as a class over branching data `B` (two particles of one algebra inside a
composite), with three data fields and three content-bearing clauses, each checkable once
an instance is proposed:

* `lightCone a b : A` — the common entanglement light cone of two particles, an element
  of the composite algebra; its block vector `λ ↦ y_λ χ_λ(lightCone a b)` is the
  evaluation of the substrate phase space (`phaseSpace`), and its trace is the sum of that
  vector (`sum_phaseSpace`);
* `compose_eq` — the knot convolution is the free product twisted by the light cone,
  `a ⋈ b = (a ⊗ b) · lightCone a b` (the corpus's `K = ρ(atom) ρ(free)⁻¹`,
  `def:ew-interface-knot`);
* `lightCone_of_not_entangled` — no shared prior history, no contribution: the light
  cone is the unit;
* `trM_lightCone_mem` — the trace evaluation lies in `[−1, 1]`, so the relative angle
  `relAngle a b := arccos (tr_M (lightCone a b))` is defined. At `q₀` on the production
  chains the trace of the light cone is the bond product `∏(z_D + d_i) ∈ (0, 1)`
  (`relative_reeb_datum_trace_angle_probe.py`: D `0.508`, T `0.205`, ³He `0.311`,
  ⁴He `0.126`), so the clause holds there and is falsified by any light cone whose
  trace leaves `[−1, 1]`.

Consequences proved from the clauses, as theorems taking the class as hypothesis
(§3b-cond): no shared history ⇒ the composite is the free product
(`compose_eq_tensor_of_not_entangled`), its trace factorises
(`trM_compose_of_not_entangled`), its log-binding vanishes
(`bindingForm_compose_eq_zero_of_not_entangled`), and its relative angle is `0`
(`relAngle_eq_zero_of_not_entangled`).

Deliberately NOT encoded: the owner's "fully entangled ⇒ all of the phase space weighted
in the negative coefficients" — for the production letters this is *derived*, not
conjectured (`InterfaceLetterCrossingMixture.lean`: every letter is `(1−e)σ + eσ⁻¹`, and
`e` is the weight on the inverse crossing), so a grade field here would restate a theorem;
and the "annihilation" clause, which the owner posed as a question and which, as the
algebra stands, runs the other way — `w w⁻¹ = 1` needs the inverse crossing on the *same*
strands, i.e. maximal shared history, while disjoint strands give the free product
(`trM_tensor`) and nothing cancels. Bean `qou-1x56`.

§7c: over `ℝ` because `Real.arccos` and `Real.log` are archimedean.

-- Ref: [leitner2026] prop:figure-eight-reeb-rotation; def:ew-interface-knot;
   rem:light-cone-affine; conj:reeb-linking-cwf-normalization
-/
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse
import QOU.MassTheory.BlockMeasureBindingFormArchimedean

namespace QOU.MassTheory.BlockMeasure

open Finset

variable {A₁ A : Type*} [Ring A₁] [Ring A] {Λ₁ Λ : Type*} [Fintype Λ₁] [Fintype Λ]

/-- **Relative Reeb datum** — primary conjecture class; no instance is provided. Data: the
common entanglement light cone of two particles, the knot convolution, and the shared-history
predicate. Clauses: the convolution is the free product twisted by the light cone; no shared
history ⇒ the light cone is the unit; the light cone's trace lies in `[−1, 1]`. -/
class RelativeReebDatum (B : BranchingData ℝ A₁ A₁ A Λ₁ Λ₁ Λ) where
  /-- The common entanglement light cone of two particles, in the composite algebra. -/
  lightCone : A₁ → A₁ → A
  /-- The knot convolution `a ⋈ b`. -/
  compose : A₁ → A₁ → A
  /-- The two particles share prior (γγ) history. -/
  Entangled : A₁ → A₁ → Prop
  /-- The convolution is the free product twisted by the light cone. -/
  compose_eq : ∀ a b, compose a b = B.tensor a b * lightCone a b
  /-- No shared prior history, no contribution: the light cone is the unit. -/
  lightCone_of_not_entangled : ∀ a b, ¬ Entangled a b → lightCone a b = 1
  /-- The trace evaluation of the light cone lies in the domain of `arccos`. -/
  trM_lightCone_mem : ∀ a b, B.D.trM (lightCone a b) ∈ Set.Icc (-1 : ℝ) 1

namespace RelativeReebDatum

variable (B : BranchingData ℝ A₁ A₁ A Λ₁ Λ₁ Λ) [RelativeReebDatum B]

/-- The evaluation of the substrate phase space on the light cone: its block vector
`λ ↦ y_λ χ_λ(lightCone a b)`. -/
noncomputable def phaseSpace (a b : A₁) : Λ → ℝ :=
  fun l => B.D.y l * B.D.χ l (lightCone (B := B) a b)

/-- The relative Reeb angle: the arccos of the trace evaluation of the light cone. -/
noncomputable def relAngle (a b : A₁) : ℝ :=
  Real.arccos (B.D.trM (lightCone (B := B) a b))

/-- The phase-space vector sums to the trace evaluation of the light cone. -/
theorem sum_phaseSpace (a b : A₁) :
    ∑ l, phaseSpace B a b l = B.D.trM (lightCone (B := B) a b) := by
  unfold phaseSpace
  rw [B.D.pairing]

/-- No shared history ⇒ the composite is the free product. -/
theorem compose_eq_tensor_of_not_entangled {a b : A₁} (h : ¬ Entangled (B := B) a b) :
    compose (B := B) a b = B.tensor a b := by
  rw [compose_eq, lightCone_of_not_entangled (B := B) a b h, mul_one]

/-- No shared history ⇒ the composite's trace factorises. -/
theorem trM_compose_of_not_entangled {a b : A₁} (h : ¬ Entangled (B := B) a b) :
    B.D.trM (compose (B := B) a b) = B.D₁.trM a * B.D₂.trM b := by
  rw [compose_eq_tensor_of_not_entangled B h, B.trM_tensor]

/-- No shared history ⇒ the relative Reeb angle is `0`. -/
theorem relAngle_eq_zero_of_not_entangled {a b : A₁} (h : ¬ Entangled (B := B) a b) :
    relAngle B a b = 0 := by
  unfold relAngle
  rw [lightCone_of_not_entangled (B := B) a b h, B.D.trM_one, Real.arccos_one]

/-- No shared history ⇒ the log-binding of the composite against the free product
vanishes. -/
theorem bindingForm_compose_eq_zero_of_not_entangled (α : ℝ) {a b : A₁}
    (h : ¬ Entangled (B := B) a b) (hfree : B.D.trM (B.tensor a b) ≠ 0) :
    B.D.bindingForm α (compose (B := B) a b) (B.tensor a b) = 0 := by
  unfold FrobeniusPairingData.bindingForm
  rw [compose_eq_tensor_of_not_entangled B h, div_self hfree, Real.log_one, mul_zero]

end RelativeReebDatum

end QOU.MassTheory.BlockMeasure
