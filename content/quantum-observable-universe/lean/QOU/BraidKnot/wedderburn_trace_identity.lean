import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Field.Basic

/-!
# QOU.BraidKnot.wedderburn_trace_identity — corrected (the old sum-identity was false)

This module formerly stated `Σ_{λ ⊢ n} dim_q(λ)² = [n]_q!` (behind a `sorry`, awaiting a
"sibling PR #2743"). **That identity is false at generic `q`** for the concrete `q`-hook dimension
`dim_q(λ) = [n]_q!/∏_c [h_c]_q` (`QPartitionCombinatorics.qDim`): symbolic computation gives, as
polynomials in `q`, `Σ_{λ⊢2} dim_q² = 2 ≠ q+1 = [2]_q!`, and likewise for `n = 3,4,5`; the two
sides agree only at `q = 1`. The disproof, the "1+1=2.230" inconsistency in the old narrative table,
and the consumer impact analysis are recorded in
`docs/audits/2026-06-29-wedderburn-trace-identity-false-at-generic-q.md`.

The false theorem (and the self-justifying `HeckeQHookDimension` premise it was projected through)
have been **removed** — a `sorry` on a false statement is a permanent landmine, not "pending
infrastructure". The genuine identities the corpus needs are:

* **Markov-trace normalization** (the restated `prop:wedderburn-trace-identity`):
  `Σ_λ d_λ · y_λ(q) = 1` — `QOU.BraidsAndKnots.plancherel_via_recipe`
  (`mass-theory/y-lambda-recipe-from-partition.lean`). `d_λ = f^λ` is the *ordinary* SYT dimension;
  `y_λ` the Markov weight.
* **Vector-space count** (q-independent): `Σ_λ d_λ² = n! = dim H_n` — `RegularRepBlockTrace.sumSq_dim_eq`.
* **Poincaré / major index** (the genuine `q`-identity for `[n]_q!`):
  `[n]_q! = Σ_w q^{maj(w)} = Σ_λ f^λ · q^{b(λ)} · dim_q(λ)` (ordinary dim × major-index generating
  function — note this is `f^λ · (q^{b}·dim_q)`, **not** `Σ dim_q²`).

Only the concrete `qInt` / `qFactorial` definitions are retained below (the right-hand side `[n]_q!`,
which is well-defined and used directly as a Hecke-level scale, e.g. `λ_W = [5]_q!·m_e`). No theorem
in this file asserts the old false equality.

-- Ref: [manuscript] quantum-observable-universe/mass-theory/wedderburn-trace-identity.md
-/

namespace QOU.BraidKnot

open scoped BigOperators

/-- The `q`-integer `[k]_q = 1 + q + … + q^{k-1}`. -/
def qInt {R : Type*} [Field R] (q : R) (k : ℕ) : R :=
  ∑ i ∈ Finset.range k, q ^ i

/-- The `q`-factorial `[n]_q! = [1]_q · [2]_q · … · [n]_q` — the Hecke-level scale (computed
    directly as this product, **not** as `Σ_λ dim_q²`, which is a different `q`-polynomial). -/
def qFactorial {R : Type*} [Field R] (q : R) (n : ℕ) : R :=
  ∏ k ∈ Finset.range n, qInt q (k + 1)

end QOU.BraidKnot
