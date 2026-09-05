| Quantity at $q_0 = 1.109978595557335$ | Value |
|---|---|
| $h = q - q^{-1}$ | $0.2090603219955937$ |
| $z = 1/(\sqrt q + 1/\sqrt q)$ | $0.4993203340335613$ |
| Form A: $\lvert\Delta(\mathrm{net})\rvert$ | $0.187207212879143$ |
| Form B: $\ln(1 + z h)$ | $0.09929139859972778$ |
| Predicted bridge $1/z + (z-1)h/(2z)$ | $1.897907634269324$ |
| Actual bridge $\mathrm{A}/\mathrm{B}$ | $1.885432328673596$ |
| Residual $\lvert$predicted $-$ actual$\rvert$ | $0.0124753$ |
| $O(h^2)$ tolerance ($h^2$) | $0.04370621823290131$ |
| $\mathfrak{Q}_\beta^{\mathrm{A}} = \lvert\Delta(\mathrm{net})\rvert \cdot E_0$ | $0.783645803897$ MeV |
| $\mathfrak{Q}_\beta^{\mathrm{B}} = \ln(1+zh) \cdot E_0 / z$ | $0.832395283254$ MeV |
| $\lvert \mathfrak{Q}_\beta^{\mathrm{A}} - \mathfrak{Q}_\beta^{\mathrm{B}}\rvert$ | $0.0487495$ MeV ($< h^2 E_0 = 0.183$ MeV) |

Values are the displayed digits of the 50-dps witness
[`q-beta-spectral-bridge.witness.json`](../../../computations/q-beta-spectral-bridge.witness.json),
regenerated from the canonical CAL-2 pinning
[`q-pinning-50-digit.witness.json`](../../../computations/q-pinning-50-digit.witness.json).

> **⚠ $h^2 = 0.04370621823290131$ carries a retired $q_0$** (measured
> 2026-09-05, `qou-i229`). Reproduced to 10 significant figures by
> $q_0 = 1.1099785955541805\ldots$, which survives only in
> `computations/_deprecated/`; the live anchors give $0.043706\ldots$ agreeing to
> 6 (proton) and 8 (muon) figures. Not silently recomputed — the anchor choice is
> owner-gated.
>
> Four further figures in this table were examined and are **not** resolved
> either way. $\lvert\mathfrak{Q}_\beta^{\mathrm{A}} - \mathfrak{Q}_\beta^{\mathrm{B}}\rvert$
> and the residual carry too few digits to matter here; and reading
> $\ln(1 + zh)$ and $1/z + (z-1)h/(2z)$ literally from their captions reproduces
> $0.09929139859972778$ and $1.897907634269324$ at **no** anchor, so either the
> caption is not the whole computation or another input enters. Recorded as
> unresolved rather than guessed at.
> `published_figures_carry_a_retired_q0_probe.py`.
