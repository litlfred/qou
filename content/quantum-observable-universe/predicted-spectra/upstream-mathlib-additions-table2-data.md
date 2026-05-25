| Open content | Substantive work needed |
|---|---|
| Absolute convergence of `complexLiTwo` on $\lvert z\rvert \leq 1$ | `Summable` proof using comparison with $1/k^2$ series (Mathlib has `Real.tsum_geometric_lt_top` analogues; needs adaptation) |
| 5-term pentagon for `blochWigner` | Spence-style identities, ~50-100 lines of Lean |
| `Cl_2(2π - θ) = -Cl_2(θ)` half-period reflection | analogous to `Cl_2_neg` but using `Real.sin_two_pi_sub` |
| Faddeev-Kashaev uniform Tauberian for `complexLiTwo` | substantial — Riemann-sum argument with uniform error bound on q $\to$ 1 |
