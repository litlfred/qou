The identification of the bar-odd $S = \mathfrak{Q}_\beta / E_0$ with the decay projection $\mathrm{Im}(q)$ (candidate (iii); [`rem:c3-s-imq-decay-projection`](#rem:c3-s-imq-decay-projection)) has a clean structural counterpart at the level of the figure-eight complex volume $\mathfrak{V} = \mathrm{Vol} + i\,\mathrm{CS}$. The finite-$b$ (one-loop-plus-corrections) expansion is the Ohtsuki tower

$$
  \mathfrak{V}_b = \mathfrak{V}_0 + \sum_{n \geq 1} \kappa_n\,(2\pi b^2)^n,
$$

with **real** coefficients $\kappa_n \in \mathbb{Q}(\sqrt{3})\cdot\pi^{\lceil n/2\rceil}$ (for instance $\kappa_1 = 11\sqrt{3}\,\pi/108$ and $\kappa_2 = 2\pi^2/27$). At the substrate the fluctuation variable is **imaginary**: with $b = \sqrt{\log q_0 / 2\pi}\,e^{i\pi/4}$ one has $2\pi b^2 = i\,t$, where $t = \log q_0 \in \mathbb{R}$.

The imaginary substrate direction splits the tower by parity, and the split is exactly the $\mathfrak{V} = \mathrm{Vol} + i\,\mathrm{CS}$ decomposition. Since $(i\,t)^2 = -t^2$ is real, pairing the imaginary factors gives:

- **even rungs are real** — $\mathrm{Im}\big((i\,t)^{2m}\,\kappa\big) = 0$, so the even sub-tower feeds $\mathrm{Re}\,\mathfrak{V} = \mathrm{Vol}$, the bar-even (mass) face;
- **odd rungs are imaginary** — $\mathrm{Re}\big((i\,t)^{2m+1}\,\kappa\big) = 0$, so the odd sub-tower feeds $\mathrm{Im}\,\mathfrak{V} = \mathrm{CS}$, the bar-odd $S$ (decay) face.

Both statements are proved sorry-free over $\mathbb{C}$ in the Lean file `OhtsukiTowerBarParity.lean` (`even_rung_real`, `odd_rung_imaginary`), with the concrete leading rungs $\kappa_1$ (odd, imaginary) and $\kappa_2$ (even, real) as instances.

The consequence for the c₃ wall is that the bar-odd $S$ — hence its anchor-dependent sign-flip — lives **entirely in the odd (imaginary) sub-tower**; the even sub-tower is the anchor-blind volume/mass channel. The odd sub-tower is factorially divergent (Gevrey-1), and its Borel–Padé resummation at the imaginary substrate is single-valued: the Borel singularity sits at the real action $A = \mathrm{Vol}(4_1)/\pi \approx 0.646$ (the geometric-to-conjugate saddle gap), off the imaginary integration ray, so there is no Stokes ambiguity and no exponentially small trans-series. Resurgence therefore returns the exact smooth $\mathrm{Im}\,\mathfrak{V} \approx 0.055$ together with the action cross-check, but supplies no anchor-dependent piece. This confirms, from the resummation side, that the $S$ sign-flip is the $1/u^3$ ladder representation of a smooth object rather than a physical singularity (compare [`rem:c3-s-imq-decay-projection`](#rem:c3-s-imq-decay-projection)); the resummation is recorded in [`qbeta_c3_borel_pade_resummation_probe.py`](../../../computations/qbeta/qbeta_c3_borel_pade_resummation_probe.py).
