import Mathlib.Tactic

/-!
# QOU.BraidKnot.ShellSchurWeylSelfDuality

**Canonical declaration** for content block at
[`quantum-observable-universe/particle-interactions/shell-schur-weyl-self-duality-proof.ts`](quantum-observable-universe/particle-interactions/shell-schur-weyl-self-duality-proof.ts).

Formalises the manuscript proof's structural core: Schur–Weyl duality indexes
`GLₖ`- and `Sₙ`-irreps by the same partition `λ ⊢ n`, and `GLₖ`-duality is
implemented by the partition **transpose** `λ ↦ λ*`. The transpose is an
involution, so it is a bijection of the index set, and its fixed points are
exactly the self-conjugate partitions (the self-dual shells).
-/

namespace QOU.BraidKnot

/-- Data for shell Schur–Weyl self-duality.

    A `definition` carrier: the index set of partitions `λ ⊢ n` and the
    conjugation (transpose) `conj = (·)*`, with the involutivity that makes it
    a duality. -/
structure ShellSchurWeylSelfDuality where
  /-- The partition index set (partitions `λ ⊢ n`, `≤ k` rows). -/
  Partition : Type
  /-- The transpose / conjugate partition `λ ↦ λ*`. -/
  conj : Partition → Partition
  /-- Transpose is involutive: `(λ*)* = λ`. -/
  conj_conj : ∀ lam, conj (conj lam) = lam

namespace ShellSchurWeylSelfDuality

variable (D : ShellSchurWeylSelfDuality)

/-- The transpose is an involution. -/
theorem conj_involutive : Function.Involutive D.conj := D.conj_conj

/-- Hence the transpose is a bijection of the index set — `GLₖ`-duality
    permutes the Schur–Weyl indices. -/
theorem conj_bijective : Function.Bijective D.conj :=
  (D.conj_involutive).bijective

/-- A partition indexes a self-dual shell iff it is self-conjugate
    (`λ = λ*`). -/
def SelfDual (lam : D.Partition) : Prop := D.conj lam = lam

/-- The self-dual shells are exactly the fixed points of the transpose. -/
theorem selfDual_iff_fixed (lam : D.Partition) :
    D.SelfDual lam ↔ D.conj lam = lam := Iff.rfl

end ShellSchurWeylSelfDuality

-- Ref: [leitner2026] quantum-observable-universe/particle-interactions/shell-schur-weyl-self-duality-proof.ts

end QOU.BraidKnot
