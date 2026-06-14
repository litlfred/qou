import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring

namespace QOU.BraidsKnots

/--
An opaque type representing the knot complement of an isotope `(Z, N)`.
(Postulated — the construction lives in the categorical substrate.)
-/
axiom AtomicKnot (Z N : ℕ) : Type

/--
Axiomatization of the hyperbolic volume of a knot complement
(Gromov norm / Thurston's volume).
-/
axiom Vol (K : Type) : ℝ

/--
The foundational topological volume quanta for the QOU nucleon blocks.
-/
axiom Vol_p : ℝ
axiom Vol_n : ℝ

/--
The Jaco–Shalen–Johannson (JSJ) additivity of hyperbolic volume.
Because the inter-nucleon braids form essential tori, the atomic knot
complement `AtomicKnot Z N` JSJ-decomposes into `Z` proton components and
`N` neutron components, and hyperbolic volume is additive under torus
gluing.
-/
axiom JSJ_volume_additivity (Z N : ℕ) :
    Vol (AtomicKnot Z N) = (Z : ℝ) * Vol_p + (N : ℝ) * Vol_n

/--
**Cluster additivity.** Combining two nucleon clusters adds their volumes
(hence, under the mass functor, the *leading* `m_qCLT_approx` masses).
A genuine consequence of `JSJ_volume_additivity` — this is the structural
content the `m_qCLT_approx` channel relies on, not a restatement of the
axiom.
-/
theorem atomic_volume_additive (Z N Z' N' : ℕ) :
    Vol (AtomicKnot (Z + Z') (N + N'))
      = Vol (AtomicKnot Z N) + Vol (AtomicKnot Z' N') := by
  rw [JSJ_volume_additivity, JSJ_volume_additivity, JSJ_volume_additivity]
  simp only [Nat.cast_add]
  ring

/--
**Proton increment.** Each added proton contributes exactly `Vol_p`: the
discrete `Z`-derivative of the atomic volume is the constant `Vol_p`.
-/
theorem vol_proton_increment (Z N : ℕ) :
    Vol (AtomicKnot (Z + 1) N) - Vol (AtomicKnot Z N) = Vol_p := by
  rw [JSJ_volume_additivity, JSJ_volume_additivity]
  simp only [Nat.cast_add, Nat.cast_one]
  ring

/--
**Neutron increment.** Each added neutron contributes exactly `Vol_n`.
-/
theorem vol_neutron_increment (Z N : ℕ) :
    Vol (AtomicKnot Z (N + 1)) - Vol (AtomicKnot Z N) = Vol_n := by
  rw [JSJ_volume_additivity, JSJ_volume_additivity]
  simp only [Nat.cast_add, Nat.cast_one]
  ring

end QOU.BraidsKnots
