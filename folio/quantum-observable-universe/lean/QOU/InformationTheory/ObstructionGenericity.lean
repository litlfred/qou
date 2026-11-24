import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Data.Set.Finite.Basic

/-!
# QOU.Information.ObstructionGenericity — chippable genericity kernel (sorry-free)

Generic-`R` companion to
[`QouPNeqNp`](QouPNeqNp.lean) / content block
[`conj:qou-p-neq-np`](../../../quantum-observable-universe/information-theory/qou-p-neq-np.md),
split into its own file per §7c (these lemmas need no archimedean
construct; the conjecture carrier's `residual : ℝ` stays in
`QouPNeqNp.lean`).

The two lemmas formalise *why* a concrete non-vanishing
$\chi(A) \neq 0$ at a generic point cannot by itself discharge the
conjecture: a nonzero polynomial obstruction vanishes at only finitely
many parameter values, so its non-vanishing locus over an infinite
domain is cofinite, hence infinite — a *generic* (Zariski-open)
condition, never equivalent to a uniform hardness statement (the
"case-(a) leak" in `conj:qou-p-neq-np`).
-/

namespace QOU.Information

open Polynomial

/-- **Chippable kernel (sorry-free).**  A nonzero polynomial
    obstruction vanishes at only finitely many parameter values.
    Generic base ring per §7c — no archimedean input. -/
theorem obstruction_vanishing_locus_finite {R : Type*} [CommRing R] [IsDomain R]
    {f : R[X]} (hf : f ≠ 0) : {q : R | f.eval q = 0}.Finite := by
  simpa [Polynomial.IsRoot] using Polynomial.finite_setOf_isRoot hf

/-- **Chippable kernel (sorry-free).**  The non-vanishing locus of a
    nonzero polynomial obstruction is infinite (indeed cofinite): over
    an infinite domain, `f.eval q ≠ 0` holds at all but finitely many
    `q`.  Exhibiting a concrete `χ(A) ≠ 0` at a generic `q₀` is
    therefore an *easy, generic* condition — it cannot by itself be
    equivalent to the uniform hardness statement `P ≠ NP` without
    collapsing the claimed equivalence. -/
theorem obstruction_nonvanishing_locus_infinite {R : Type*} [CommRing R] [IsDomain R]
    [Infinite R] {f : R[X]} (hf : f ≠ 0) : {q : R | f.eval q ≠ 0}.Infinite := by
  apply Set.infinite_of_finite_compl
  have hcompl : {q : R | f.eval q ≠ 0}ᶜ = {q : R | f.eval q = 0} := by
    ext q; simp
  rw [hcompl]
  exact obstruction_vanishing_locus_finite hf

end QOU.Information
