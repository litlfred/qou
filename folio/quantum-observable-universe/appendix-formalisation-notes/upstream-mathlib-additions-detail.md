## Advances

**(A)** `Real.dilog` and `Complex.dilog`.
The `complexLiTwo` definition implements a concrete `tsum`-based dilogarithm. The $1/k^2$ factor guarantees summability on the closed unit disk. Mathlib provides `Summable` for geometric series. Appending absolute-convergence proofs makes this a candidate Mathlib PR.

**(B)** `BlochWigner`.
The `blochWigner` definition utilizes `Complex.log` and `Complex.arg` from Mathlib. Proving the standard five-term pentagon identity for `blochWigner` closes gap (2). This proof reduces to the absolute convergence of `complexLiTwo` and the Spence-style functional equations for the real and imaginary parts of $\mathrm{Li}_2$.

**(C)** $\mathrm{Cl}_2$ functional equations.
The reflection identity `Cl_2(-θ) = -Cl_2(θ)` is an unconditional Lean theorem. The proof applies `Real.sin_neg` and `tsum_neg`. This establishes the simplest $\mathrm{Cl}_2$ functional equation. Analogous `tsum` rearrangements extend this technique to periodicity identities such as `Cl_2(θ + 2π) = Cl_2(θ)`.

## Target translation

The conditional-class chain provides unconditional functional identities alongside concrete Lean definitions for `complexLiTwo` and `blochWigner`. This translates a prior axiomatic gap into specific, named Lean targets ready for upstreaming.
