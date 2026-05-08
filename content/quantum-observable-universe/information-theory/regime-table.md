All quantitative regime claims in this chapter and Ch 9 collapse
into a single table.  Per-section tables in
[operational-entropy](#def:operational-entropy),
[information-speed-of-light](#def:information-speed-of-light),
[gravitational-constant](#def:gravitational-constant),
[hausdorff-dimension-recurrence](#rem:hausdorff-dimension-recurrence)
are projections of the corresponding columns of this master table
to the row(s) most relevant to that section.

| Regime | $q$ | $\hbar_q$ | $c_q$ | $\eta_q$ | $d_H(q)$ | $G(q)$ | Description |
|---|---|---|---|---|---|---|---|
| Classical limit | $q \to 1^+$ | $\to 0$ | $\to \infty$ | $\to 1$ | $\to 1$ | $\to G_{\mathrm{Newton}}$ | Spatial coupling becomes instantaneous; classical PDEs recovered; Julia set $=$ unit circle |
| Our universe | $q_0 \approx 1.110$ | $\approx 0.0991$ | $\approx 9.12$ | $\approx 0.892$ | $\approx 1.088$ | numerical (Planck-normalised) | Moderate quantum: $\sim 9$ fibres correlated per Reeb advance; ${\sim}0.89$ q-bits per Planck step |
| Golden crossover | $q = q_{\mathrm{gold}} = 1/\varphi^{2}$ | $-\varphi$ | $-\varphi$ | (sign flip) | (degenerate node) | (degenerate) | Reeb-weight sign flip; Descartes elliptic curve degenerates to nodal $\mathbb{P}^{1}$ |
| Deep quantum / Big Bang | $q \to \infty$ | $\to 1$ | $\to 0$ | $\to 0$ | $\to 0$ | $\to 0$ | No spatial propagation; each fibre isolated; Julia set collapses; zero information per step |

**Reading the table.**  $\hbar_q = 1 - q^{-1}$ is the quantum
Planck constant ([def:quantum-planck-constant](#def:quantum-planck-constant));
$c_q = 1/(q-1)$ is the information speed of light
([def:information-speed-of-light](#def:information-speed-of-light));
$\eta_q = (2q-1)/q^{3}$ is the operational entropy
([rem:operational-entropy](#def:operational-entropy));
$d_H(q) = (2q-1)^{2}/q^{3}$ is the Julia-set Hausdorff dimension
([rem:hausdorff-dimension-recurrence](#rem:hausdorff-dimension-recurrence));
$G(q)$ is the gravitational constant
([rem:gravitational-constant](#def:gravitational-constant)) in
Planck-normalised units (varies with $q$ in the table; equal to
$G_{\mathrm{Planck}} = 1$ exactly when $q = q_0$).

**Use.**  When a downstream block needs to cite a regime value, it
should reference this table (`[regime-table](#rem:regime-table)`)
rather than re-tabulate.  When a new derived quantity is added, it
gets a column here; the per-section tables in the cited blocks
should be re-projected to the relevant row(s).
