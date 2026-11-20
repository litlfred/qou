import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

namespace QOU.BraidsKnots

/--
An opaque type representing the knot complement of an isotope `(Z, N)`.
(Postulated — the construction lives in the categorical substrate.)
-/
-- Ref: [leitner2026] §brings-surface — the atomic knot complement of an
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
-- Ref: [leitner2026] §mass-theory — Vol_p, Vol_n are the QOU proton/neutron
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
-- Ref: [leitner2026] quantum-observable-universe/braids-and-knots/jsj-decomposition-linearity.md
class AtomicJSJDecomposition where
  /-- Total hyperbolic volume of the `Z` proton JSJ pieces. -/
  protonPieceVol : ℕ → ℝ
  /-- Total hyperbolic volume of the `N` neutron JSJ pieces. -/
  neutronPieceVol : ℕ → ℝ
  /-- Isotope-independent proton piece quantum: `Z` proton pieces have volume `Z · Vol_p`. -/
  proton_piece_sum : ∀ Z : ℕ, protonPieceVol Z = (Z : ℝ) * Vol_p
  /-- Isotope-independent neutron piece quantum: `N` neutron pieces have volume `N · Vol_n`. -/
  neutron_piece_sum : ∀ N : ℕ, neutronPieceVol N = (N : ℝ) * Vol_n
  /-- Thurston JSJ volume additivity across the proton and neutron piece clusters. -/
  thurston_jsj_split : ∀ Z N : ℕ,
    Vol (AtomicKnot Z N) = protonPieceVol Z + neutronPieceVol N

/-- The linear law, derived from the JSJ piece split and per-nucleon piece quanta. -/
theorem JSJ_volume_additivity [ctx : AtomicJSJDecomposition] (Z N : ℕ) :
    Vol (AtomicKnot Z N) = (Z : ℝ) * Vol_p + (N : ℝ) * Vol_n := by
  rw [ctx.thurston_jsj_split Z N, ctx.proton_piece_sum Z, ctx.neutron_piece_sum N]

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

/-- **Vacuum normalisation.** At `Z = 0, N = 0`, the atomic knot volume vanishes. -/
theorem vol_vacuum_zero [AtomicJSJDecomposition] :
    Vol (AtomicKnot 0 0) = 0 := by
  rw [JSJ_volume_additivity]
  simp only [Nat.cast_zero]
  ring

/-- **Isobar volume difference.** Exchanging a neutron for a proton at fixed
    mass number `A = Z + N + 1` shifts the hyperbolic volume by `Vol_p - Vol_n`. -/
theorem vol_isobar_diff [AtomicJSJDecomposition] (Z N : ℕ) :
    Vol (AtomicKnot (Z + 1) N) - Vol (AtomicKnot Z (N + 1)) = Vol_p - Vol_n := by
  rw [JSJ_volume_additivity, JSJ_volume_additivity]
  simp only [Nat.cast_add, Nat.cast_one]
  ring

end QOU.BraidsKnots
