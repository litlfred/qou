**Remark (numerical cross-check of CAL-2 at 50 dps: $\mathrm{Vol}(4_1)/\hbar_q^2 = m_\mu/m_e$).**
*The CAL-2 identity*

$$
  \frac{m_\mu}{m_e}
  \;=\;
  \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
$$

*is the aether-side anchor that fixes $q_0$. Evaluating both sides at 50-decimal precision yields the residual recorded in the witness file:*

| Quantity | 50-dps value | Source |
|----------|-------------|--------|
| $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$ | $2.0298832128\ldots$ | aether (figure-8 archimedean image) |
| $\hbar_q^2 = ((q_0 - 1)/q_0)^2$ at $q_0$ | $0.00981719\ldots$ | aether (CAL-2) |
| $\mathrm{Vol}(4_1)/\hbar_q^2$ at $q_0$ | $206.76828305\ldots$ | aether |
| $m_\mu/m_e$ (CODATA **2018**) | $206.7682830\ldots$ | empirical |
| relative residual | $1.45 \times 10^{-30}$ ppm | — |

## Structural vanishing of the residual

The 50-dps residual is $\sim 10^{-30}$ ppm. This is exactly the $q_0$-pinning equation read in the forward direction. The CAL-2 calibration defines $q_0$ as the unique real solution of $m_\mu/m_e = \mathrm{Vol}(4_1)/\hbar_q^2$. Evaluating both sides at that $q_0$ yields equality by construction, up to the 50-dps numerical precision of the pinning algorithm and the CODATA $m_\mu/m_e$ truncation.

The witness serves as a numerical certificate of the pinning procedure. It is not a falsifiability test of the formula. A falsifiability test requires varying $q_0$ or adding an independent aether constraint.

## Significance for the Borromean baryon programme

The figure-8 sector — the Higgs knot, whose volume the muon mass proxy evaluates; the muon's identity knot is the cinquefoil $T(2,5)$ — verifies the mass ansatz at the single-knot level with a topologically trivial Skein contribution ($S(4_1) = 0$ in the canonical orientation). The mass formula reduces to $m_\mu = m_e \cdot \mathrm{Vol}(4_1)/\hbar_q^2$.

The Borromean baryon programme asks whether the same ansatz, lifted to a 3-link with non-trivial Skein contribution, gives baryon masses with a single common Borromean term $\mathfrak{m}_{\mathcal{B}_3}(q_0)$:

$$
  m_B
  \;=\;
  \mathfrak{m}_{\mathcal{B}_3}(q_0)
  \;+\;
  m_e \cdot S(B).
$$

In the figure-8 case, the common term degenerates to the bare volume form, $\mathfrak{m}_{4_1} = m_e \cdot \mathrm{Vol}(4_1)/\hbar_q^2$, with $S(4_1) = 0$. In the Borromean case, the empirical closure target exceeds the bare volume form by a factor $\approx 2.46$ (the purged historical $\lambda_{\mathrm{scale}}$ literal): $\mathfrak{m}_{\mathcal{B}_3}(q_0) \approx 2.46 \cdot m_e\,\mathrm{Vol}(\mathcal{B}_3)/\hbar_q^2$.

The aether consistency of $\Delta S(n - p)$ to $\sim 1\,000$ ppm using only CAL-1, CAL-2, and $\mathrm{Vol}(\mathcal{B}_3)$ is the first non-trivial extension of the figure-8 cross-check to the Borromean sector.
