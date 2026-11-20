All quantitative regime claims in this chapter and Chapter 9 unify into a single table. Per-section tables covering [operational entropy](#def:operational-entropy), [information speed of light](#def:information-speed-of-light), [gravitational constant](#def:gravitational-constant), and [Hausdorff dimension recurrence](#rem:hausdorff-dimension-recurrence) are direct projections of this master table to relevant rows.

| Regime | $q$ | $\hbar_q$ | $c_q$ | $\eta_q$ | $d_H(q)$ | $G_q$ | Description |
|---|---|---|---|---|---|---|---|
| Classical limit | $q \to 1^+$ | $\to 0$ | $\to \infty$ | $\to 1$ | $\to 1$ | $\to G_{\mathrm{Newton}}$ | Spatial coupling instantaneous; classical PDEs recovered; Julia set $=$ unit circle |
| The observed universe | $q_0 \approx 1.110$ | $\approx 0.0991$ | $\approx 9.093$ | $\approx 0.892$ | $\approx 1.088$ | numerical (Planck-normalised) | Moderate quantum: $\sim 9$ fibres correlated per Reeb advance; ${\sim}0.89$ q-bits per Planck step |
| Golden crossover | $q = q_{\mathrm{gold}} = 1/\varphi^{2}$ | $-\varphi$ | $-\varphi$ | (sign flip) | (degenerate node) | (degenerate) | Reeb-weight sign flip; Descartes elliptic curve degenerates to nodal $\mathbb{P}^{1}$ |
| Deep quantum / Big Bang | $q \to \infty$ | $\to 1$ | $\to 0$ | $\to 0$ | $\to 0$ | $\to 0$ | No spatial propagation; fibres isolated; Julia set collapses; zero information per step |

**Reading the table.**
The quantum Planck constant is $\hbar_q = 1 - q^{-1}$ ([def:quantum-planck-constant](#def:quantum-planck-constant)). The information speed of light is $c_q = 1/(q-1)$ ([def:information-speed-of-light](#def:information-speed-of-light)). The operational entropy evaluates to $\eta_q = (2q-1)/q^{3}$ ([rem:operational-entropy](#def:operational-entropy)). The Julia-set Hausdorff dimension is $d_H(q) = (2q-1)^{2}/q^{3}$ ([rem:hausdorff-dimension-recurrence](#rem:hausdorff-dimension-recurrence)). The parameter $G_q$ denotes the gravitational constant in Planck-normalised units ([rem:gravitational-constant](#def:gravitational-constant)). It varies with $q$ across the table, satisfying $G_{\mathrm{Planck}} = 1$ exactly at $q = q_0$.

**Observational caveat.**
The dispersive variables $\hbar_q$ and $c_q$ apply strictly at the substrate level. Any residual $q$-dispersion affecting archimedean photon propagation is tightly constrained by gamma-ray-burst time-of-flight measurements \cite{abdo2009}. These bounds are comprehensively surveyed in the Planck-scale phenomenology literature \cite{amelinocamelia2013}. The necessary theoretical suppression mechanism is recorded in [the DSR remark](#rem:dsr-planck-scale-phenomenology) and [the suppression-scale conjecture](#conj:dispersion-suppression-scale).

**Use.**
A downstream citation of a regime value should reference this table (`[regime-table](#rem:regime-table)`) rather than reproducing data. Any newly derived quantity should appear as an additional column here. Per-section tables in referenced blocks can then simply project the relevant rows.
