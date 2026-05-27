| Path | Time (5 atoms) | Precision floor |
|---|---:|---:|
| Canonical reducer (`markov_trace_recursive`, 50 dps mpmath) | ~30 s | $10^{-50}$ |
| Hybrid partition-sum (30-dps $y_\lambda$ + float64 $\chi^\lambda_q$) | ~66 s | $10^{-14}$ (machine $\varepsilon$) |
| Full mpmath partition-sum | ~5–10 min | $10^{-50}$ |
| Pure float64 partition-sum (legacy) | ~1 s | $10^{-5}$ at $n = 9$ |
| Pure symbolic Wenzl + symbolic χ^λ | timeout (>4 min) | exact |
