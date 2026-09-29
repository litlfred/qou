| Quantity at $q_0 = 1.109978595642739$ | Value |
|---|---|
| $\hbar_q = (q - 1)/q$ | $0.099081726507578$ |
| $1 + \hbar_q^2$ | $1.009817188527722$ |
| $E_{0, N=0}$ (MeV) | $4.18598082$ |
| $E_{0, N=1}$ (MeV) | $4.22707538$ |
| $\mathfrak{Q}_\beta^{A, N=0}$ (MeV) | $0.78364580$ |
| $\mathfrak{Q}_\beta^{A, N=1}$ (MeV) | $0.79133900$ |
| $\mathfrak{Q}_\beta^{\mathrm{CODATA}}$ (MeV) | $0.78233341$ |
| $N=0$ residual | $+1.31$ keV ($+0.168\%$) |
| $N=1$ residual | $+9.01$ keV ($+1.151\%$) |
| Per-braid $N=1$ ceiling | $\hbar_q^4 / (1 - \hbar_q^2) = 97.3$ ppm |

> **Refreshed to the live muon pin, 2026-09-05** (`qou-i229`, owner-approved) —
> **partially.** Producer:
> [`retired_q0_refresh_to_live_muon_pin_probe.py`](computations/probes/retired_q0_refresh_to_live_muon_pin_probe.py)
> (5/5).
>
> | figure | was | now |
> |---|---|---|
> | $q_0$ (header) | $1.109978595554181$ | $1.109978595642739$ |
> | $\hbar_q$ | $0.099081726435699$ | $0.099081726507578$ |
> | $1 + \hbar_q^2$ | $1.009817188513479$ | $1.009817188527722$ |
>
> The old pin was the **CODATA-2018 vintage of the muon anchor**; the shift is
> $8.0 \times 10^{-11}$ relative. The per-braid ceiling $\hbar_q^4/(1-\hbar_q^2)
> = 97.3$ ppm is unchanged at its stated precision.
>
> **⚠ The $E_0$ and $\mathfrak{Q}_\beta$ rows are NOT refreshed, deliberately.**
> They are producer outputs of the $q_\beta$ channel, whose values depend on the
> **trace convention** as well as on $q_0$ — and that channel's C→D migration is
> tracked separately as `qou-cds1`, where the $\mathfrak{Q}_\beta$ figures move by
> $\sim 0.05$ MeV. Refreshing a pin underneath a convention that is itself about
> to change would produce numbers nobody has checked. Those rows must be
> regenerated from the producer under D, in one pass, not substituted here.
>
> So this table currently mixes a **refreshed** $\hbar_q$ against
> **unrefreshed** $E_0$ and $\mathfrak{Q}_\beta$. That is the state the
> per-block rule warns about, and it is accepted here only because the remaining
> rows need a convention decision rather than an arithmetic one — recorded so it
> is not mistaken for completion.
