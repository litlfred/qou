/-
# The §10a Cauchy derivation cannot reach the 3-body cumulant

`docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md` §10a
derives the binding functional's *shape*: the Markov trace is multiplicative over
**independent** subsystems and energy is extensive over **non-interacting** ones,
so the map from trace to energy satisfies the Cauchy functional equation
`f (x * y) = f x + f y`, whose continuous solutions are `f x = c * log x`.
"The log form is forced."

This file records what that argument does **not** reach, and it is not a defect
of the Cauchy step. §10a determines the *bond functional* `f`; the binding is
then assembled as a **sum over bonds**, `B = Σ_{i<j} f (μ i j)`. Every such
assembly is pairwise-additive, and a pairwise-additive set function has
identically vanishing connected cumulants above order two — **whatever `f` is**.

So the choice of `f` is orthogonal to the 3-body defect. `f = c * log` gives
`b₃ = 0`; so does every other `f`. The measured target is `b₃ = +1.426222` MeV
(AME2020 Ursell inversion, `he4_body_order_shortfall_location_probe.py`), so the
assembly — not the functional it applies — is what a nonzero connected 3-body
cumulant refutes.

Companion results already on `main`, which this completes into a dichotomy:

* `QOU.MassTheory.MayerThreeBodySign.lt_of_b3_pos` — the **multiplicative**
  assembly `W = 1 - Π f` needs `f_pn > 2/3` for `b₃ > 0`, and every measured
  bond factor is below it, so that assembly forces `b₃ < 0`.
* This file — the **pairwise-additive** assembly forces `b₃ = 0`.

Nature gives `b₃ > 0`. Neither corpus assembly can produce it.

**Scope.** Nothing here refutes §10a's premises. Trace multiplicativity over
independent subsystems and energy extensivity over non-interacting ones are
untouched, and so is the conclusion that `f` is a logarithm *on the sector where
those premises hold*. What is established is that the sector is the wrong one:
the premises constrain `f` on **disjoint** clusters, and the observable that
fails is a **connected** quantity, which by construction vanishes on every
assembly built by summing over disjoint pairs.

Base ring is a generic `CommRing` throughout (AGENTS.md §7c) — the statements are
algebraic identities and inclusion-exclusion bookkeeping; no ordering, no
archimedean input, no `ℝ`.

Bean `qou-bhzt`; successor question of `qou-edt7`.
-/
import Mathlib.Algebra.Ring.Defs

namespace QOU.Mass.PairwiseCumulantVanishing

variable {R : Type*} [CommRing R]

/-- A binding map on a four-body system, recorded by its values on every
sub-cluster **independently**. Nothing here assumes the values are related;
`IsPairwise` below is what asserts a relation, and it is a hypothesis. -/
structure BindingMap (R : Type*) [CommRing R] where
  /-- the binding of the pair `{i, j}` -/
  pair : Fin 4 → Fin 4 → R
  /-- the binding of the triple `{i, j, k}` — an independent datum -/
  triple : Fin 4 → Fin 4 → Fin 4 → R
  /-- the binding of the whole four-body cluster — an independent datum -/
  quad : R

namespace BindingMap

variable (M : BindingMap R)

/-- The **connected three-body cumulant** of a triple: its binding, less the
three pair bindings inside it. This is the Ursell/Möbius definition, and it is
the quantity the AME inversion measures as `b₃ = +1.426222` MeV. -/
def b3 (i j k : Fin 4) : R :=
  M.triple i j k - (M.pair i j + M.pair i k + M.pair j k)

/-- The sum of the six pair bindings of the four-body cluster. -/
def pairSum : R :=
  M.pair 0 1 + M.pair 0 2 + M.pair 0 3 + M.pair 1 2 + M.pair 1 3 + M.pair 2 3

/-- The sum of the four triple cumulants of the four-body cluster. -/
def b3Sum : R :=
  M.b3 0 1 2 + M.b3 0 1 3 + M.b3 0 2 3 + M.b3 1 2 3

/-- The **connected four-body cumulant**: the whole-cluster binding, less the
pair terms and the connected triple terms. -/
def b4 : R := M.quad - M.pairSum - M.b3Sum

/-- `M` is **pairwise-additive**: every cluster's binding is the sum of the pair
bindings it contains. This is the shape §10a's assembly produces — the bond
functional `f` is applied per bond and the results are summed. -/
def IsPairwise : Prop :=
  (∀ i j k : Fin 4, M.triple i j k = M.pair i j + M.pair i k + M.pair j k) ∧
    M.quad = M.pairSum

end BindingMap

open BindingMap

/-- **A pairwise-additive binding has vanishing connected three-body cumulant.**
Not "small" — identically zero, for every triple. -/
theorem b3_eq_zero_of_isPairwise {M : BindingMap R} (h : M.IsPairwise)
    (i j k : Fin 4) : M.b3 i j k = 0 := by
  simp [BindingMap.b3, h.1 i j k]

/-- **And vanishing connected four-body cumulant.** The `b₄` term inherits the
result: with every triple cumulant zero, `b₄` collapses to `quad - pairSum`,
which pairwise-additivity sets to zero. -/
theorem b4_eq_zero_of_isPairwise {M : BindingMap R} (h : M.IsPairwise) :
    M.b4 = 0 := by
  have h3 : M.b3Sum = 0 := by
    simp [BindingMap.b3Sum, b3_eq_zero_of_isPairwise h]
  simp [BindingMap.b4, h3, h.2]

/-- **The falsifiable form**, and the one the measurement instantiates: a binding
map with any nonzero connected three-body cumulant is not pairwise-additive.
Since AME2020 gives `b₃ = +1.426222 ≠ 0`, the physical binding is not of this
shape. -/
theorem not_isPairwise_of_b3_ne_zero {M : BindingMap R} {i j k : Fin 4}
    (h : M.b3 i j k ≠ 0) : ¬ M.IsPairwise :=
  fun hp => h (b3_eq_zero_of_isPairwise hp i j k)

/-- The §10a assembly: a bond functional `f` evaluated on each bond factor `μ`
and summed over the bonds of each cluster. `f` is entirely arbitrary — it is
*not* assumed to be a logarithm, or continuous, or anything else. -/
def ofBondFunctional (f : R → R) (μ : Fin 4 → Fin 4 → R) : BindingMap R where
  pair i j := f (μ i j)
  triple i j k := f (μ i j) + f (μ i k) + f (μ j k)
  quad := f (μ 0 1) + f (μ 0 2) + f (μ 0 3) + f (μ 1 2) + f (μ 1 3) + f (μ 2 3)

/-- **Every bond-functional assembly is pairwise-additive**, for every `f`. This
is the step that makes the Cauchy determination of `f` irrelevant to the 3-body
defect: `f` does not appear in the conclusion. -/
theorem isPairwise_ofBondFunctional (f : R → R) (μ : Fin 4 → Fin 4 → R) :
    (ofBondFunctional f μ).IsPairwise := by
  constructor
  · intro i j k; rfl
  · rfl

/-- **The conclusion of the file.** Whatever bond functional §10a's Cauchy
argument selects — the forced logarithm included — the induced binding has
identically zero connected three-body cumulant. Deriving `f` therefore cannot
close the 3-body gap, because `f` is not what the gap is about. -/
theorem b3_eq_zero_ofBondFunctional (f : R → R) (μ : Fin 4 → Fin 4 → R)
    (i j k : Fin 4) : (ofBondFunctional f μ).b3 i j k = 0 :=
  b3_eq_zero_of_isPairwise (isPairwise_ofBondFunctional f μ) i j k

/-- Contrapositive, stated so a reader holding the measurement can apply it
directly: a nonzero connected three-body cumulant excludes **every** bond
functional at once, rather than excluding them one at a time. -/
theorem no_bondFunctional_of_b3_ne_zero {M : BindingMap R} {i j k : Fin 4}
    (h : M.b3 i j k ≠ 0) (f : R → R) (μ : Fin 4 → Fin 4 → R) :
    M ≠ ofBondFunctional f μ := by
  intro hEq
  exact h (hEq ▸ b3_eq_zero_ofBondFunctional f μ i j k)

end QOU.Mass.PairwiseCumulantVanishing
