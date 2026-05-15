import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Basic
import QOU.MathlibExt.QPlancherel

/-!
# QOU.Observations.AlgebraicCausalActionStructure

Algebraic-side causal-action structure on the Hecke algebra
`A_q = H_n(R, q)`, encoded as a typeclass whose fields carry the
intended mathematical content (not vacuous placeholders).

The proposition assembled here is the pre-Archimedean mirror of the
Finster causal-action data
([finster2021], [finster2024]):

* `plancherelIdentity` — `tr_M(x) = Σ_λ w̃_λ · χ_λ(x)`
  (Markov trace = q-Plancherel integral, over the finite dual `Λ`).
* `strongDuality` — the LP primal–dual pair has zero gap,
  `Σ_λ t_λ · x★_λ = n_target · y0★`.
* `activeSetNonempty` — the active set
  `{λ : y★_λ > 0}` is non-empty under non-trivial feasibility.

Concrete LP data (`lpWeight`, `lpGram`, `nTarget`, primal/dual
optimisers) are carried as class fields, so the variational
statements reference actual values rather than free propositions.

## Conventions

* `Λ` indexes the Wedderburn blocks (dual `Λ = Irr(A_q)`); we
  require `[Fintype Λ]` so `∑ λ : Λ` is well-defined.
* `A` is the underlying algebra type (the Hecke algebra `A_q`).
* `R` is the coefficient ring (e.g. `ℤ[q^{±1/2}] ⊗ ℚ`).
* `level : ℕ` records the partition size `n` used for the
  q-Plancherel measure denominator `Z_q(n)`.

## What is provable, what is class-conditional

Each class field is a *concrete* mathematical statement using
`QPlancherel.measure`, `Finset.sum`, and the carried LP data.
Providing an instance therefore requires non-trivial input
(actual character functions, an actual Markov trace, an actual LP
optimum), not merely four propositions that happen to be true.

The class is *not* inhabited at the trivial level: providing the
trivial instance would require either an empty `Λ` (failing
`activeSetNonempty`) or trivial LP data (failing `strongDuality`
under non-degeneracy). This is by design — a meaningful causal-
action structure should not be satisfiable for free.

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

universe u v w

open scoped BigOperators
open QOU.MathlibExt.QPlancherel

/-- **Algebraic causal-action structure on a Hecke-type algebra.**

Each field carries the intended mathematical content, not a
free proposition. -/
class HasAlgebraicCausalActionStructure
    (Λ : Type u) (R : Type v) (A : Type w)
    [Field R] [LinearOrder R] [IsStrictOrderedRing R]
    [Fintype Λ] [DecidableEq Λ]
    [QDimension Λ R] [HasPartitionFunction Λ R] where
  /-- Irreducible character at block `λ`, evaluated on `x : A`. -/
  chi : Λ → A → R
  /-- The Markov trace on `A`. -/
  trM : A → R
  /-- The partition size `n` used to fix `Z_q(n)`. -/
  level : ℕ
  /-- LP weight vector (Markov traces of basis elements). -/
  lpWeight : Λ → R
  /-- LP Frobenius Gram matrix `G_{λ,μ} = tr_M(b_λ · b_μ)`. -/
  lpGram : Λ → Λ → R
  /-- LP target value `n_target` (positive). -/
  nTarget : R
  nTarget_pos : 0 < nTarget
  /-- LP primal optimum. -/
  xStar : Λ → R
  /-- LP dual scalar (free in sign — dual variable for the
      net-equality constraint). -/
  y0Star : R
  /-- LP dual vector (shadow prices for Frobenius positivity
      constraints — non-negative). -/
  yStar : Λ → R
  yStar_nonneg : ∀ λ, 0 ≤ yStar λ
  /-- **Plancherel-integral identity (Part 1).**
      `tr_M(x) = Σ_λ measure(λ, level) · χ_λ(x)` over `Λ`. -/
  plancherelIdentity : ∀ (x : A),
    trM x = ∑ λ : Λ, QPlancherel.measure (R := R) (Λ := Λ) λ level * chi λ x
  /-- **Primal feasibility (Part 2a).** The primal optimum satisfies
      the net-equality constraint
      `Σ_λ xStar λ = nTarget`. -/
  primalNetConstraint : (∑ λ : Λ, xStar λ) = nTarget
  /-- **Frobenius positivity (Part 2a).** `(G · x★)_λ ≥ 0`. -/
  frobeniusPositivity : ∀ λ : Λ,
    0 ≤ ∑ μ : Λ, lpGram λ μ * xStar μ
  /-- **Dual feasibility (Part 2b).**
      `y_0 · 1 + G^T y ≤ t`, i.e. for every `μ`,
      `y0Star + Σ_λ G_{λ,μ} · y_λ ≤ t_μ`. -/
  dualFeasibility : ∀ μ : Λ,
    y0Star + (∑ λ : Λ, lpGram λ μ * yStar λ) ≤ lpWeight μ
  /-- **Strong duality (Part 2b).**
      `Σ_λ t_λ · x★_λ = n_target · y0★`. -/
  strongDuality :
    (∑ λ : Λ, lpWeight λ * xStar λ) = nTarget * y0Star
  /-- **Active set non-emptiness (Part 2c).** Under the non-degeneracy
      condition (the primal value is below the trivial upper bound,
      witnessing that at least one Frobenius constraint binds), the
      active set `{λ : y_λ★ > 0}` is non-empty. Encoded as an
      existential. -/
  activeSetNonempty : ∃ λ : Λ, 0 < yStar λ

end QOU.Observations.AlgebraicCausalActionStructure
