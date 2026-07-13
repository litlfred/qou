| Open content | Substantive work needed |
|---|---|
| Absolute convergence of `complexLiTwo` on $\lvert z\rvert \leq 1$ | `Summable` proof comparing with $1/k^2$ series (requires adapting Mathlib's `Real.tsum_geometric_lt_top` analogues). |
| 5-term pentagon for `blochWigner` | Spence-style identities (approximately 50-100 lines of Lean). |
| `Cl_2(2π - θ) = -Cl_2(θ)` half-period reflection | Analogous to `Cl_2_neg`, but using `Real.sin_two_pi_sub`. |
| Faddeev-Kashaev uniform Tauberian for `complexLiTwo` | Substantial. Requires a Riemann-sum argument with a uniform error bound as $q \to 1$. |
