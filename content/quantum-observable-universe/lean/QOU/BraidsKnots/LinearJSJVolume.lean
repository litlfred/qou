import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

namespace QOU.BraidsKnots

/--
An opaque type representing the knot complement of an isotope `(Z, N)`.
(Postulated — the construction lives in the categorical substrate.)
-/
-- Ref: [manuscript] §brings-surface — the atomic knot complement of an
-- isotope (Z,N) is a QOU substrate construction; this names it as an
-- opaque input rather than re-deriving the categorical construction here.
opaque AtomicKnot (Z N : ℕ) : Type

/--
Axiomatization of the hyperbolic volume of a knot complement
(Gromov norm / Thurston's volume).
-/
-- Ref: [thurston1978] https://www.msri.org/publications/books/gt3m/
-- — hyperbolic volume (Gromov norm) of a 3-manifold / knot complement.
opaque Vol (K : Type) : ℝ

/--
The foundational topological volume quanta for the QOU nucleon blocks.
-/
-- Ref: [manuscript] §mass-theory — Vol_p, Vol_n are the QOU proton/neutron
-- block volume quanta (substrate-fixed constants), not external values.
opaque Vol_p : ℝ
opaque Vol_n : ℝ

/-! ### The theorem and the conjecture, kept apart

The linear volume law `Vol(𝒦(Z,N)) = Z·Vol_p + N·Vol_n` used to be a single
`axiom JSJ_volume_additivity` carrying a Thurston citation. That conflated
two very different inputs, and the citation covered only one of them.

The content block
[`conj:jsj-decomposition-linearity`](../../../quantum-observable-universe/braids-and-knots/jsj-decomposition-linearity.md)
already draws the line correctly, and this file now matches it:

> *"Additivity of hyperbolic volume over the pieces of the geometric
> decomposition along essential tori is a theorem of 3-manifold topology
> (Thurston). **The conjectural content therefore lies entirely in the
> decomposition hypothesis**: that the atomic knot complement JSJ-decomposes
> along the inter-nucleon tori into exactly `Z` proton and `N` neutron
> hyperbolic pieces, each carrying an isotope-independent volume quantum."*

Thurston gives additivity over *whatever* the JSJ pieces happen to be. He
does not say the pieces are `Z` copies of one block and `N` copies of
another, nor that their volumes are isotope-independent constants — that is
the QOU claim, and it is open. Labelling the combined statement
`[thurston1978]` made an open conjecture of this framework read as a cited
external theorem. Bean `qou-t7zg`.

So: `AtomicJSJDecomposition` is the conjecture (a §3b-cond class, **no
instance** — the honest open state per §3b-tax), and the three consequences
below now take it as an explicit `[Instance]` hypothesis. They are unchanged
in content and still fully verified — conditional on the named hypothesis
rather than on a mislabelled axiom. -/

/-- **The decomposition hypothesis** (conjectural; `conj:jsj-decomposition-linearity`).

    The atomic knot complement `𝒦(Z,N)` JSJ-decomposes along the
    inter-nucleon essential tori into exactly `Z` proton pieces and `N`
    neutron pieces, each carrying an isotope-independent volume quantum.
    Given Thurston's additivity over the pieces, this yields the linear law.

    This is the *open* part. It is a primary conjecture carrier: it takes no
    other conjecture class as a hypothesis, and **no instance is provided**. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/jsj-decomposition-linearity.md
class AtomicJSJDecomposition : Prop where
  /-- The linear volume law that the decomposition hypothesis delivers,
      via Thurston additivity over the `Z + N` pieces. -/
  volume_linear : ∀ Z N : ℕ,
    Vol (AtomicKnot Z N) = (Z : ℝ) * Vol_p + (N : ℝ) * Vol_n

/-- The linear law, conditional on the decomposition hypothesis. -/
theorem JSJ_volume_additivity [AtomicJSJDecomposition] (Z N : ℕ) :
    Vol (AtomicKnot Z N) = (Z : ℝ) * Vol_p + (N : ℝ) * Vol_n :=
  AtomicJSJDecomposition.volume_linear Z N

/--
**Cluster additivity.** Combining two nucleon clusters adds their volumes
(hence, under the mass functor, the *leading* `m_qCLT_approx` masses).
A genuine consequence of the decomposition hypothesis — this is the
structural content the `m_qCLT_approx` channel relies on, not a restatement
of the hypothesis.
-/
theorem atomic_volume_additive [AtomicJSJDecomposition] (Z N Z' N' : ℕ) :
    Vol (AtomicKnot (Z + Z') (N + N'))
      = Vol (AtomicKnot Z N) + Vol (AtomicKnot Z' N') := by
  rw [JSJ_volume_additivity, JSJ_volume_additivity, JSJ_volume_additivity]
  simp only [Nat.cast_add]
  ring

/--
**Proton increment.** Each added proton contributes exactly `Vol_p`: the
discrete `Z`-derivative of the atomic volume is the constant `Vol_p`.
-/
theorem vol_proton_increment [AtomicJSJDecomposition] (Z N : ℕ) :
    Vol (AtomicKnot (Z + 1) N) - Vol (AtomicKnot Z N) = Vol_p := by
  rw [JSJ_volume_additivity, JSJ_volume_additivity]
  simp only [Nat.cast_add, Nat.cast_one]
  ring

/--
**Neutron increment.** Each added neutron contributes exactly `Vol_n`.
-/
theorem vol_neutron_increment [AtomicJSJDecomposition] (Z N : ℕ) :
    Vol (AtomicKnot Z (N + 1)) - Vol (AtomicKnot Z N) = Vol_n := by
  rw [JSJ_volume_additivity, JSJ_volume_additivity]
  simp only [Nat.cast_add, Nat.cast_one]
  ring

end QOU.BraidsKnots
