import QOU.Mass.PairwiseCumulantVanishing
import QOU.Mass.ArchimedeanTraceBridge
import Mathlib.Tactic

/-!
# The interaction amplitude cannot factorise over pairs

`QOU.Mass.ArchimedeanTraceBridge` derives the self/mutual partition at the Markov-trace level: if
the assembly amplitude is `(∏ Tᵢ)·I` — constituent self-traces times an **interaction factor** `I` —
then the mass-deficit binding is exactly `−log I = bindingFreeEnergy I`. That converts the
multiplicative categorical trace into the additive energy `SelfMutualPartition` had assumed.

It leaves `I` unstructured, and there is one obvious way to structure it. The §10a Cauchy argument
(see `PairwiseCumulantVanishing`'s docstring) says the trace-to-energy map is a logarithm; the
natural next move is to give each *pair* its own interaction factor and take the cluster's factor to
be the product,

    I(S) = ∏_{i<j ∈ S} I_ij .

This file says that move is **refuted by the data**, and it is worth stating before someone makes it,
because the multiplicative form disguises what it is: `−log ∏ I_ij = Σ (−log I_ij)` is a sum over
bonds, so it is pairwise-additive in the sense of `PairwiseCumulantVanishing.IsPairwise`, and every
such assembly has `b₃ = 0` identically. AME2020 measures `b₃ = +1.4262225`
(`QOU.MassTheory.AmeBindingNotPairwise.ame_b3_eq`).

So the interaction factor of a cluster is **not** the product of its pairs' factors. Whatever `I` is,
it carries irreducibly many-body structure — which is the multiplicative face of the same constraint
`QOU.Mass.CrossingModelPairLocality` states additively (a pair's crossing weight is not
assembly-independent), and which a Brunnian carrier supplies.

## Why this needed saying separately

The additive statement and the multiplicative one look different enough that closing one does not
visibly close the other. `bindingFreeEnergy` is *defined* through `Real.log`, and a product inside a
logarithm reads as "the natural factorisation" rather than as "a bond sum in disguise" — which is
exactly the shape §10a's own conclusion invites. The whole content of `pairFactorised_b3_eq_zero` is
that `log` moves it from one column to the other.

Ground ring `ℝ` (§7c: `Real.log` is archimedean). Beans `qou-w6vh`, `qou-brng`, `qou-bhzt`.
-/

namespace QOU.Mass.InteractionFactorNotPairwise

open QOU.Mass.PairwiseCumulantVanishing QOU.Mass.ArchimedeanTraceBridge

/-- An interaction factor assigned **per pair**, with every factor positive so the archimedean
functor `log` is defined on it. A cluster's interaction factor is the product over the pairs it
contains — the multiplicative analogue of pair-locality. -/
structure PairFactorised where
  /-- the interaction factor of the pair `{i,j}` -/
  I : Fin 4 → Fin 4 → ℝ
  /-- positivity, discharged for the framework's quantum-integer amplitude class at `q > 1`
  (`ArchimedeanTraceBridge`, `QOU.MathlibExt.qInt_pos`) -/
  pos : ∀ i j, 0 < I i j

namespace PairFactorised

variable (P : PairFactorised)

/-- The interaction factor of the triple `{i,j,k}`: the product over its three pairs. -/
def tripleI (i j k : Fin 4) : ℝ := P.I i j * P.I i k * P.I j k

/-- The interaction factor of the four-component assembly: the product over its six pairs. -/
def quadI : ℝ :=
  P.I 0 1 * P.I 0 2 * P.I 0 3 * P.I 1 2 * P.I 1 3 * P.I 2 3

/-- The binding map this interaction structure induces, via
`ArchimedeanTraceBridge.binding_eq_bindingFreeEnergy`: each cluster's binding is `−log` of its
interaction factor. -/
noncomputable def toBindingMap : BindingMap ℝ where
  pair i j := bindingFreeEnergy (P.I i j)
  triple i j k := bindingFreeEnergy (P.tripleI i j k)
  quad := bindingFreeEnergy P.quadI

end PairFactorised

open PairFactorised

/-- `bindingFreeEnergy` turns a product of positive factors into a sum — the negated
`freeEnergy_connectedSum`. This is the whole mechanism: the multiplicative structure is a bond sum
once the archimedean functor is applied. -/
theorem bindingFreeEnergy_mul {a b : ℝ} (ha : 0 < a) (hb : 0 < b) :
    bindingFreeEnergy (a * b) = bindingFreeEnergy a + bindingFreeEnergy b := by
  unfold bindingFreeEnergy
  rw [freeEnergy_connectedSum a b ha hb]
  ring

/-- **A pair-factorised interaction gives a pairwise-additive binding.** The product over pairs
becomes a sum over bonds under `log`. -/
theorem isPairwise_of_pairFactorised (P : PairFactorised) :
    P.toBindingMap.IsPairwise := by
  have hpos := P.pos
  constructor
  · intro i j k
    show bindingFreeEnergy (P.tripleI i j k) = _
    unfold PairFactorised.tripleI
    rw [bindingFreeEnergy_mul (mul_pos (hpos i j) (hpos i k)) (hpos j k),
        bindingFreeEnergy_mul (hpos i j) (hpos i k)]
    rfl
  · show bindingFreeEnergy P.quadI = _
    unfold PairFactorised.quadI BindingMap.pairSum
    have h2 : 0 < P.I 0 1 * P.I 0 2 := mul_pos (hpos 0 1) (hpos 0 2)
    have h3 : 0 < P.I 0 1 * P.I 0 2 * P.I 0 3 := mul_pos h2 (hpos 0 3)
    have h4 : 0 < P.I 0 1 * P.I 0 2 * P.I 0 3 * P.I 1 2 := mul_pos h3 (hpos 1 2)
    have h5 : 0 < P.I 0 1 * P.I 0 2 * P.I 0 3 * P.I 1 2 * P.I 1 3 :=
      mul_pos h4 (hpos 1 3)
    rw [bindingFreeEnergy_mul h5 (hpos 2 3),
        bindingFreeEnergy_mul h4 (hpos 1 3),
        bindingFreeEnergy_mul h3 (hpos 1 2),
        bindingFreeEnergy_mul h2 (hpos 0 3),
        bindingFreeEnergy_mul (hpos 0 1) (hpos 0 2)]
    rfl

/-- **Hence its 3-body cumulant vanishes identically** — the multiplicative form gains nothing over
the additive one. -/
theorem pairFactorised_b3_eq_zero (P : PairFactorised) (i j k : Fin 4) :
    P.toBindingMap.b3 i j k = 0 :=
  b3_eq_zero_of_isPairwise (isPairwise_of_pairFactorised P) i j k

/-- **And its 4-body cumulant.** -/
theorem pairFactorised_b4_eq_zero (P : PairFactorised) :
    P.toBindingMap.b4 = 0 :=
  b4_eq_zero_of_isPairwise (isPairwise_of_pairFactorised P)

/-- **The exclusion.** A nonzero measured 3-body cumulant refutes the pair-factorised interaction
factor. Since AME2020 gives `b₃ = +1.4262225 ≠ 0`, the interaction amplitude of a cluster is **not**
the product of its pairs' interaction amplitudes. -/
theorem not_pairFactorised_of_b3_ne_zero {P : PairFactorised} {i j k : Fin 4}
    (h : P.toBindingMap.b3 i j k ≠ 0) : False :=
  h (pairFactorised_b3_eq_zero P i j k)

/-- **Non-vacuity.** A pair-factorised interaction exists — the trivial one, `I ≡ 1`, which is the
independent (unbound) assembly and indeed has zero binding at every order. -/
theorem trivial_pairFactorised_binding_zero :
    (⟨fun _ _ => 1, fun _ _ => one_pos⟩ : PairFactorised).toBindingMap.b3 0 1 2 = 0 :=
  pairFactorised_b3_eq_zero _ 0 1 2

end QOU.Mass.InteractionFactorNotPairwise
