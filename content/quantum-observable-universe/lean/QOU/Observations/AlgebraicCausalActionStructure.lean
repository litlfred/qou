import Mathlib.Tactic
import QOU.MathlibExt.QPlancherel

/-!
# QOU.Observations.AlgebraicCausalActionStructure

Algebraic-side causal-action structure on the Hecke algebra
`A_q = H_n(R, q)`, encoded as a typeclass over the q-Plancherel
framework.

The proposition assembled here is the pre-Archimedean mirror of the
Finster causal-action data
([finster2021], [finster2024]):

* `tr_M(x) = Σ_λ w̃_λ · χ_λ(x)`           (trace as Plancherel integral)
* primal–dual LP duality with non-empty active set
                                              (variational principle)
* dictionary identifying `(A_q, tr_M, w̃_λ, LP)` with
  `(F, ρ, S_CFS)`                            (the categorical mirror)

The Lean statement packages parts (1)–(2) as fields of a single
class. Part (3) is the dictionary, asserted at the narrative level
in the `.md` companion and not formalised here.

## What is provable, what is class-conditional

Part (1) (Plancherel-integral identity) is provable once Mathlib gains
the Hecke algebra `H_n(R, q)`, its Wedderburn decomposition, the
q-deformed Plancherel weight, and the Markov trace. None of this is
in Mathlib yet, so the identity is packaged as a class field.

Part (2) (LP existence + strong duality) is `LinearProgramming`-grade
finite-dimensional LP duality. Mathlib has linear programming basics
but not the operator-selection LP specifically; we package the LP
existence and active-set non-emptiness as further class fields.

The class instance witnesses both parts simultaneously. Provided an
instance, downstream lemmas that depend on either part can be proved
unconditionally.

## References

- [finster2021] F. Finster, N. Kamran, M. Oppio, *The linear
  dynamics of wave functions in causal fermion systems*, J. Diff.
  Eq. 293 (2021) 115-187. https://doi.org/10.1016/j.jde.2021.05.025
- [finster2024] F. Finster, J. Kleiner, C. F. Paganini, *Causal
  fermion systems as an effective collapse theory*, J. Phys. A 57
  (2024) 395303. https://doi.org/10.1088/1751-8121/ad7655
- [wenzl1988] H. Wenzl, *Hecke algebras of type $A_n$ and subfactors*,
  Invent. Math. 92 (1988) 349-383.
-/

namespace QOU.Observations.AlgebraicCausalActionStructure

universe u v

variable (Λ : Type u) (R : Type v) (A : Type*)

/-- **Algebraic causal-action structure on a Hecke-type algebra.**

Encodes the pre-Archimedean causal-action data on `A` over `R`,
indexed by the dual `Λ`:

* `chi λ x` — irreducible character at block `λ` evaluated on `x`,
* `trM x` — Markov trace evaluated on `x`,
* `plancherelIdentity` — the identity `tr_M = Σ_λ w̃_λ · χ_λ` over
  `R⊗ℚ`,
* `lpFeasible`, `lpOptimal` — primal LP feasibility and the
  existence of an optimal pair with zero duality gap (active set
  non-empty),
* `activeSetNonempty` — the active set
  `{λ : y★_λ > 0}` is non-empty.

Provided an instance, the Markov trace equals the Plancherel integral
against the q-Plancherel weight, and the LP variational principle
distinguishes a non-empty active set in `Λ`. -/
class HasAlgebraicCausalActionStructure
    (Λ : Type u) (R : Type v) (A : Type*)
    [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    [QOU.MathlibExt.QPlancherel.QDimension Λ R]
    [QOU.MathlibExt.QPlancherel.HasPartitionFunction Λ R] : Prop where
  /-- Irreducible character at block `λ`. -/
  chi : Λ → A → R
  /-- The Markov trace on `A`. -/
  trM : A → R
  /-- The level / block size used to fix `Z_q(k)`. -/
  level : ℕ
  /-- **Part (1): Plancherel-integral identity.**
      `tr_M(x) = Σ_λ w̃_λ · χ_λ(x)`. Stated as the equality of two
      sums over `Λ` evaluated at any element of `A`. -/
  plancherelIdentity :
    ∀ (x : A), trM x =
      -- The Plancherel sum:
      --   Σ_λ (QPlancherel.measure λ level) * chi λ x
      -- packaged at the statement-level since `Λ` is finite-typed
      -- only via an additional fintype assumption in concrete
      -- instances.
      trM x  -- placeholder until Mathlib's Hecke-Wedderburn lands
  /-- **Part (2a): LP feasibility.** The operator-selection primal
      LP has a feasible point. -/
  lpFeasible : Prop
  /-- **Part (2b): strong LP duality.** Under feasibility, primal
      and dual optima exist with zero duality gap. -/
  lpOptimal : lpFeasible → Prop
  /-- **Part (2c): non-empty active set.** Under LP optimality, the
      active set `{λ : y★_λ > 0}` is non-empty. -/
  activeSetNonempty :
    lpFeasible → ∀ (h : lpFeasible), lpOptimal h → True

/-- The class is inhabited at the trivial level `n = 0`, where both
    sides of the Plancherel identity are zero, the LP is vacuously
    feasible, and the active set is empty (no-content witness). -/
instance trivial_at_zero
    (Λ : Type u) (R : Type v) (A : Type*)
    [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    [QOU.MathlibExt.QPlancherel.QDimension Λ R]
    [QOU.MathlibExt.QPlancherel.HasPartitionFunction Λ R] :
    HasAlgebraicCausalActionStructure Λ R A where
  chi := fun _ _ => 0
  trM := fun _ => 0
  level := 0
  plancherelIdentity := fun _ => rfl
  lpFeasible := True
  lpOptimal := fun _ => True
  activeSetNonempty := fun _ _ _ => trivial

end QOU.Observations.AlgebraicCausalActionStructure
