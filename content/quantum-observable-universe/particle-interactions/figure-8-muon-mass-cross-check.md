**Remark (numerical cross-check of CAL-2 at 50 dps:
$\mathrm{Vol}(4_1)/\hbar_q^2 = m_\mu/m_e$).**
*The CAL-2 identity
([prop:three-calibration-inputs](#prop:three-calibration-inputs))*

$$
  \frac{m_\mu}{m_e}
  \;=\;
  \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
$$

*is the substrate-side anchor that fixes $q_0$. The
[derive\_m\_baryon\_volume\_form](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/derive_m_baryon_volume_form.py)
script evaluates both sides at 50-decimal precision and records the
residual in
[`m-baryon-volume-form.witness.json`](https://github.com/litlfred/qou/blob/claude/audit-plancherel-usage-a6DgI/computations/m-baryon-volume-form.witness.json):*

| Quantity | 50-dps value | Source |
|----------|-------------|--------|
| $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ | $2.0298832128\ldots$ | substrate (figure-8 archimedean image) |
| $\hbar_q^2 = ((q_0 - 1)/q_0)^2$ at $q_0$ | $9.8174\ldots \times 10^{-3}$ | substrate (CAL-2) |
| $\mathrm{Vol}(4_1)/\hbar_q^2$ at $q_0$ | $206.76828305\ldots$ | substrate |
| $m_\mu/m_e$ (CODATA 2022) | $206.7682830\ldots$ | empirical |
| relative residual | $1.45 \times 10^{-30}$ ppm | — |

## Why the residual is structurally zero (not "small")

The 50-dps residual is $\sim 10^{-30}$ ppm — *not* a fit, *not* a
coincidence, *not* a fortunate cancellation. It is exactly the
$q_0$-pinning equation read in the forward direction:

- the CAL-2 calibration *defines* $q_0$ as the unique real solution
  of $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$
  ([prop:local-substrate-q](#prop:local-substrate-q));
- evaluating both sides at *that* $q_0$ then gives equality by
  construction up to the 50-dps numerical precision of the pinning
  algorithm and the CODATA $m_\mu/m_e$ truncation.

The witness therefore serves as a **numerical certificate of the
pinning procedure**, not as a falsifiability test of the formula.
A falsifiability test would have to vary $q_0$ or add an independent
substrate constraint
([prop:three-calibration-inputs](#prop:three-calibration-inputs),
"what is forbidden").

## Significance for the Borromean baryon programme

The figure-8 (muon) sector verifies the
[$\mathrm{Vol}(K)/\hbar_q^2$](#lem:topological-mass-cat-descended) ansatz at the
single-knot level with topologically trivial Skein contribution
($S(4_1) = 0$ in the canonical orientation): the mass formula
reduces to $m_\mu = m_e \cdot \mathrm{Vol}(4_1)/\hbar_q^2$.

The Borromean baryon programme
([conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula))
asks whether the same ansatz, lifted to a 3-link with non-trivial
Skein contribution, gives baryon masses with a single common scale
$\lambda_{\mathrm{scale}}$:

$$
  m_B
  \;=\;
  m_e \cdot \left[\,
    \frac{\mathrm{Vol}(\mathcal{B}_3)}{\hbar_q^2}
    \cdot \lambda_{\mathrm{scale}}
    \;+\; S(B)
  \,\right].
$$

In the figure-8 case the formula degenerates to
$\lambda_{\mathrm{scale}}^{(4_1)} = 1$ and $S(4_1) = 0$; in the
Borromean case the empirical closure target is
$\lambda_{\mathrm{scale}}^{(\mathcal{B}_3)} \approx 2.46$ (see
[conj:borromean-baryon-mass-formula](#conj:borromean-baryon-mass-formula)).

The substrate consistency of $\Delta S(n - p)$
([rem:delta-skein-substrate-identity](#rem:delta-skein-substrate-identity))
to $\sim 1\,000$ ppm using only CAL-1 + CAL-2 +
$\mathrm{Vol}(\mathcal{B}_3)$ is the first non-trivial extension of
the figure-8 / muon cross-check shown here to the Borromean / baryon
sector.
