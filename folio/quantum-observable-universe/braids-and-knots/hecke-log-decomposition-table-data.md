| Quantity | Value (50 dps) |
|---|---|
| $h(q_0)$ | $0.20906032215\ldots$ |
| $\hbar_q(q_0) = (q_0 - 1)/q_0$ | $0.09908172651\ldots$ |
| $1 + q_0$ | $2.10997859564\ldots$ |
| $\log(1/h(q_0))$ | $1.56513244593\ldots$ |
| $\log(1/\hbar_q(q_0))$ | $2.31181024912\ldots$ |
| $\log(1 + q_0)$ | $0.74667780319\ldots$ |
| $\log(1/\hbar_q) - \log(1 + q_0)$ | $1.56513244593\ldots$ (matches) |

> **Refreshed to the live muon pin, 2026-09-05** (`qou-i229`, owner-approved).
> All seven rows moved together. Producer:
> [`retired_q0_refresh_to_live_muon_pin_probe.py`](../../../computations/probes/retired_q0_refresh_to_live_muon_pin_probe.py)
> (5/5).
>
> The table previously read
>
> | figure | was | now |
> |---|---|---|
> | $h(q_0)$ | $0.20906032199$ | $0.20906032215$ |
> | $\hbar_q(q_0)$ | $0.09908172644$ | $0.09908172651$ |
> | $1 + q_0$ | $2.10997859556$ | $2.10997859564$ |
> | $\log(1/h(q_0))$ | $1.56513244670$ | $1.56513244593$ |
> | $\log(1/\hbar_q(q_0))$ | $2.31181024982$ | $2.31181024912$ |
> | $\log(1 + q_0)$ | $0.74667780313$ | $0.74667780319$ |
>
> computed at $q_0 = 1.1099785955541805\ldots$ — the **CODATA-2018 vintage of
> the muon pin**, recovered by inverting CAL-2 at $m_\mu/m_e = 206.7682830$. The
> 2026-08-15 substrate fix that moved to the NIST table reached `computations/`
> and `tools/` and not `content/`. New pin
> $q_0 = 1.10997859564273904668\ldots$, from `q-pinning-50-digit.witness.json`;
> the shift is $8.0 \times 10^{-11}$ relative and nothing physical moves.
>
> **All seven rows, not the three a sweep found.** An earlier pass substituted
> only the flagged figures and was reverted: the unflagged rows are $q_0$-derived
> too — they merely had *some* provenance, so the no-provenance sweep never saw
> them — and refreshing one column while its siblings stay behind leaves a table
> the reader cannot recompute from itself, which is worse than the stale value.
>
> **Three rows were also wrong at their own anchor**, independently of the pin:
> $1 + q_0$ ($2.10997859556$ against $\ldots555$), $\log(1/\hbar_q)$
> ($\ldots982$ against $\ldots985$) and $\log(1 + q_0)$ ($\ldots313$ against
> $\ldots315$) — $1$–$3 \times 10^{-11}$, neither the rounding nor the
> truncation of the retired value. Corrected here by construction.
