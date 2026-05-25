| Addition | Content | Status |
|---|---|---|
| `complexLiTwo : ℂ → ℂ` | $\sum_{k \geq 1} z^{k+1}/(k+1)^2$ via `tsum` | unconditional definition; convergence on closed unit disk implicit |
| `complexLiTwo_zero` | `Li_2(0) = 0` | proved by `simp` |
| `blochWigner : ℂ → ℝ` | $\mathrm{Im}(\mathrm{Li}_2(z)) + \log\lvert z\rvert \cdot \arg(1-z)$ | unconditional definition using Mathlib's `Complex.log`, `Complex.arg`, `Complex.abs` |
| `blochWigner_zero` | `D(0) = 0` (boundary) | proved using `Real.log_zero = 0` Mathlib convention |
| `Cl_2_neg` | `Cl_2(-θ) = -Cl_2(θ)` (oddness) | proved by `tsum`-rearrangement + `Real.sin_neg` |
| `Cl_2_zero_via_oddness` | re-derivation of `Cl_2(0) = 0` from oddness | sorry-free linarith |
