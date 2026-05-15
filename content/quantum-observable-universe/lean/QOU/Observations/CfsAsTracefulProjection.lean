import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Basic
import QOU.MathlibExt.QPlancherel

/-!
# QOU.Observations.CfsAsTracefulProjection

The traceful (Plancherel) projection `Π_tr : (A_q, tr_M) →
(Irr(A_q), w̃_λ, {χ_λ})` sends QOU's non-commutative algebraic data
to its commutative spectral shadow, which is structurally a
CFS-style measure + functional family.

Encoded as a typeclass with three concrete content fields:

1. **Commutator vanishing under the trace** — `tr_M([x, y]) = 0`
   (kernel-of-projection content).
2. **Partition function** — `Z_Pl(x) := Σ_λ w̃_λ · χ_λ(x)` as a
   concrete sum (the character generating function).
3. **Plancherel identity** — `Z_Pl(x) = tr_M(x)` (trace recovery).

The class carries the trace and character data as fields, so each
statement is non-vacuous: providing an instance requires actual
trace and character functions, not merely four propositions.

## References

- [finster2021] F. Finster, N. Kamran, M. Oppio, *The linear
  dynamics of wave functions in causal fermion systems*, J. Diff.
  Eq. 293 (2021) 115-187. https://doi.org/10.1016/j.jde.2021.05.025
- [biane1998] P. Biane, *Representations of symmetric groups and
  free probability*, Adv. Math. 138 (1998) 126-181.
- [wenzl1988] H. Wenzl, *Hecke algebras of type A_n and subfactors*,
  Invent. Math. 92 (1988) 349-383.
-/

namespace QOU.Observations.CfsAsTracefulProjection

universe u v w

open scoped BigOperators
open QOU.MathlibExt.QPlancherel

/-- **Traceful projection class.**

Encodes the three structural conclusions of
`prop:cfs-as-traceful-projection-of-qou`. -/
class IsTracefulProjection
    (Λ : Type u) (R : Type v) (A : Type w)
    [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    [Fintype Λ] [DecidableEq Λ]
    [AddGroup A] [Mul A]
    [QDimension Λ R] [HasPartitionFunction Λ R] where
  /-- The Markov trace on `A`. -/
  trM : A → R
  /-- The character `χ_λ` at block `λ`. -/
  chi : Λ → A → R
  /-- The level `n` used for the q-Plancherel denominator. -/
  level : ℕ
  /-- **Conclusion 3 (kernel): trace kills commutators.** -/
  commutatorVanishes : ∀ (x y : A), trM (x * y - y * x) = 0
  /-- **Conclusion 2 (partition function): explicit
      character-generating-function form.** -/
  partitionFunction : A → R
  /-- Definition of the partition function as the Plancherel sum. -/
  partitionFunction_def : ∀ (x : A),
    partitionFunction x =
      ∑ λ : Λ, QPlancherel.measure (R := R) (Λ := Λ) λ level * chi λ x
  /-- **Trace recovery: `Z_Pl(x) = tr_M(x)`.** -/
  partitionFunction_eq_trace : ∀ (x : A),
    partitionFunction x = trM x

end QOU.Observations.CfsAsTracefulProjection
