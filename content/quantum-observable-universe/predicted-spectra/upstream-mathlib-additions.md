**Proposition (Upstream Mathlib Additions).**

The Lean file [`upstream-mathlib-additions.lean`](upstream-mathlib-additions.lean) provides three sorry-free additions targeting Mathlib:

See [Table 1](#tbl:upstream-mathlib-additions-table1-data).

## Advances

**(A) Towards `Real.dilog`/`Complex.dilog`.**
The `complexLiTwo` definition implements a concrete `tsum`-based dilogarithm. With absolute-convergence proofs added, this becomes a candidate Mathlib PR. (Mathlib provides `Summable` for geometric series; the $1/k^2$ factor guarantees summability on the closed unit disk).

**(B) Towards `BlochWigner`.**
The `blochWigner` definition leverages Mathlib's `Complex.log` and `Complex.arg`. Proving the standard 5-term pentagon identity for `blochWigner` closes substantive gap (2). This proof reduces to the absolute-convergence of `complexLiTwo` and the Spence-style functional equations for the real and imaginary parts of $\mathrm{Li}_2$.

**(C) Towards $\mathrm{Cl}_2$ functional equations.**
The reflection `Cl_2(-θ) = -Cl_2(θ)` is now a sorry-free Lean theorem. The proof relies directly on `Real.sin_neg` and `tsum_neg`. This establishes the simplest $\mathrm{Cl}_2$ functional equation. Analogous `tsum` rearrangements extend this technique to other identities, such as periodicity `Cl_2(θ + 2π) = Cl_2(θ)`.

## Significance

The §3b-cond chain now features two unconditional functional identities (`Cl_2_neg`, `complexLiTwo_zero`, `blochWigner_zero`) alongside concrete Lean definitions for `complexLiTwo` and `blochWigner`. This translates a previously axiomatic "Mathlib gap" into specific, named Lean targets ready for individual upstreaming.
