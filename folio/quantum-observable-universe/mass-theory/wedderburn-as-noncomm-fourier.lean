import Mathlib.Data.Real.Basic


/-!
# QOU.WedderburnFourier — Peter–Weyl/Plancherel reading of the Markov trace

The Wedderburn–Artin character expansion of the Markov trace on
`H_n(q)` is the inverse non-commutative Fourier transform on the
semisimple algebra `H_n(q)`. This file packages that reading as a
`structure`; it does *not* add new mathematics — it only re-labels
the existing Wedderburn decomposition so downstream files can refer
to "non-commutative Fourier coefficients" `χ_λ(β)` indexed by
partitions `λ ⊢ n`.

LaTeX label: `prop:wedderburn-as-noncomm-fourier`

## References

- [jones1987] https://doi.org/10.2307/1971403
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 (Ch. XII)
- [fulton1997] Young Tableaux (Cambridge University Press, 1997).
- [leitner2026] braids-and-knots / wedderburn-as-noncomm-fourier
-/

namespace QOU.WedderburnFourier

/-- Abstract data of a Wedderburn–Artin / Peter–Weyl decomposition of
    a finite-dimensional semisimple algebra `A` together with a trace
    `τ : A → ℝ`. We package the data so that any callers only depend
    on the *interface* (partitions = spectrum, characters = Fourier
    coefficients, weights = Plancherel measure), not on the underlying
    Hecke-algebra construction.

    Concrete instances for `H_n(q)` at generic `q` are constructed in
    `QOU.WedderburnMass`; this file is the abstract glue. -/
structure NonCommFourierData where
  /-- Carrier of the algebra (e.g. `H_n(q)`). -/
  carrier : Type*
  /-- Trace functional (e.g. the Jones–Markov trace). -/
  tr : carrier → ℝ
  /-- Index type for the non-commutative spectrum (e.g. `λ ⊢ n`). -/
  spectrum : Type*
  /-- Character on the `λ`-block. -/
  chi : spectrum → carrier → ℝ
  /-- Quantum dimension `d_λ` of the `λ`-block. -/
  dim : spectrum → ℝ
  /-- Plancherel/Markov weight `w_λ`. -/
  weight : spectrum → ℝ
  /-- All quantum dimensions are non-zero (semisimplicity). -/
  dim_ne_zero : ∀ lam, dim lam ≠ 0

/-- The **inverse non-commutative Fourier transform reading**: the
    trace evaluates as a weighted sum of character values. The sum is
    *finite* because `spectrum` is a partition lattice for fixed `n`
    (instantiated `Fintype` at use sites). We expose the equation as a
    field so downstream theorems can pattern-match on it without
    depending on a concrete `Fintype` instance.

    **Status.** This is the Peter–Weyl/Plancherel formula for a
    finite-dimensional semisimple algebra. Proving it generically
    requires Mathlib infrastructure for character orthogonality on
    Hecke algebras that is not yet in place. We therefore state the
    decomposition as a typeclass-style field; concrete instances
    (e.g. for `H_n(q)` at small `n`) supply the proof.
-/
class IsInverseFourier (D : NonCommFourierData) where
  /-- Existence of a finite indexing set on which the sum is taken. -/
  indexFin : List D.spectrum
  /-- The indexing list contains no duplicates: the Peter–Weyl sum
      ranges over the *set* of distinct irreducibles, so duplicate
      entries would overcount. -/
  nodup_indexFin : indexFin.Nodup
  /-- Decomposition: trace as a weighted sum of `χ_λ / d_λ`. -/
  decomposition :
    ∀ β, D.tr β =
      (indexFin.map (fun lam => D.weight lam * D.chi lam β / D.dim lam)).sum

/-- A re-export theorem in the same shape used by
    `QOU.WedderburnMass.atomicMass`: given the inverse-Fourier
    interface, the trace of `β` is reconstructed from its
    non-commutative Fourier coefficients `{χ_λ(β)}`.
-/
-- Ref: [leitner2026] prop:wedderburn-as-noncomm-fourier
theorem peter_weyl_decomposition
    (D : NonCommFourierData) [F : IsInverseFourier D] (β : D.carrier) :
    D.tr β =
      (F.indexFin.map (fun lam => D.weight lam * D.chi lam β / D.dim lam)).sum :=
  F.decomposition β

end QOU.WedderburnFourier
