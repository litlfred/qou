| Quantity | Value (50 dps) |
|---|---|
| $h(q_0)$ | $0.20906032199\ldots$ |
| $\hbar_q(q_0) = (q_0 - 1)/q_0$ | $0.09908172644\ldots$ |
| $1 + q_0$ | $2.10997859556\ldots$ |
| $\log(1/h(q_0))$ | $1.56513244670\ldots$ |
| $\log(1/\hbar_q(q_0))$ | $2.31181024982\ldots$ |
| $\log(1 + q_0)$ | $0.74667780313\ldots$ |
| $\log(1/\hbar_q) - \log(1 + q_0)$ | $1.56513244670\ldots$ (matches) |

> **⚠ These three figures carry a retired $q_0$ (measured 2026-09-05, `qou-i229`).**
> $1 + q_0 = 2.10997859556$, $\log(1+q_0) = 0.74667780313$ and
> $\log(1/\hbar_q) = 2.31181024982$ are all reproduced by
> $q_0 = 1.1099785955541805\ldots$, which now appears **only** in eight
> `computations/_deprecated/` witnesses and one deprecated script. It is neither
> live anchor — proton $1.10997858275\ldots$, muon $1.10997859564\ldots$ — and
> sits between them, so the discrepancy is not visible by inspection. At the two
> live anchors the same quantities are
>
> | figure | published | proton | muon |
> |---|---|---|---|
> | $1 + q_0$ | $2.10997859556$ | $2.10997858275138$ | $2.10997859564274$ |
> | $\log(1+q_0)$ | $0.74667780313$ | $0.746677797081664$ | $0.746677803191375$ |
> | $\log(1/\hbar_q)$ | $2.31181024982$ | $2.31181035472636$ | $2.31181024912344$ |
>
> **Not silently recomputed.** Which anchor this table should use is owner-gated:
> `q_parameter.py` records the corpus as "genuinely MIXED (279 proton + 455
> muon)", that "a blanket flip is WRONG", and "do NOT change this default".
> Substituting a pin here would be choosing one on the author's behalf.
> Measured in `published_figures_carry_a_retired_q0_probe.py`.
