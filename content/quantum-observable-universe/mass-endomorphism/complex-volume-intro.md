The mass endomorphism $\mathcal{M}$ carries more information than its real trace. Read over $\mathbb{C}$, the projection defect $\mathrm{tr}_M\big((\Pi_{\text{free}}-\mathbf{1})\circ\mathcal{M}\big)$ — the part of $\mathcal{M}$ that does not survive the factorized projector $\Pi_{\text{free}}$ onto the un-linked constituents — is a single complex observable, the **complex volume** $\mathfrak{V}(K) = E_0\,\mathrm{tr}_M\big((\Pi_{\text{free}}-\mathbf{1})\circ\mathcal{M}\big)$, the QOU analogue of the Neumann–Zagier $\mathbb{V}(K) = \operatorname{Vol}(K) + i\,\mathrm{CS}(K)$. This section introduces $\mathfrak{V}$ and the structural fact that the framework's two nuclear observables are its two real shadows: **binding energy is the real part** ($\mathfrak{E}_{\mathrm{bind}} = \operatorname{Re}\mathfrak{V}$, the bar-even / $\cosh$ / strong channel — stable binding) and **the $\beta$-decay $Q$-value is the imaginary part** ($\mathfrak{Q}_\beta = \operatorname{Im}\mathfrak{V}$, the bar-odd / $\sinh$ / weak channel — the anti-binding, unstable decay direction).

The single block **Complex-volume unification: binding $\mathfrak{E}_{\mathrm{bind}}$ and $\beta$-decay $\mathfrak{Q}_\beta$ are $\operatorname{Re}$/$\operatorname{Im}$ of one $\mathfrak{V}$** (conjecture) states the unification, derives the Re/Im split from the bar-parity decomposition of the two crossing eigenvalues $q, -q^{-1}$ (so $\cosh\lambda \pm \sinh\lambda = e^{\pm\lambda}$ continues to $\cos\theta \pm i\sin\theta$ on the unit circle), and records the corroboration from the precision-ladder compute. The reconstruction $\mathfrak{E}_{\mathrm{bind}} + i\,\mathfrak{Q}_\beta = \mathfrak{V}$ is proved sorry-free in Lean; only the physical match — that the *measured* binding and $Q$-value equal these definitional Re/Im at one normalisation — is conjectural.

**Fibre-level caveat (carried throughout).** At the archimedean / observable level $\operatorname{Im}(q_0) = 0$: binding and $\mathfrak{Q}_\beta$ are both real measured numbers. The complex structure is therefore *fibre-level* (pre-$\tau$); $\mathfrak{E}_{\mathrm{bind}}$ and $\mathfrak{Q}_\beta$ are real observable shadows of one complex fibre object under different archimedean evaluations (real-$q$ volume channel vs root-of-unity Chern–Simons channel), exactly as $\operatorname{Vol}$ and $\mathrm{CS}$ are separately real. There is no "complex mass."

The consequence reframes the rest of the mass and $\beta$-decay narrative: one computes $\mathfrak{V}(K)$ once; its real part is every binding energy (developed in the algebraic and physical faces of **Mass Analysis**), its imaginary part is every $Q$-value (the $\mathfrak{Q}_\beta$ precision ladder and the Q-value appendix). The two channels are not two stories but one complex object on its two parities.

The two real shadows of $\mathfrak{V}$ line up aspect-by-aspect:

| aspect | real part $\operatorname{Re}\mathfrak{V}$ | imaginary part $\operatorname{Im}\mathfrak{V}$ |
|---|---|---|
| **observable** | binding energy $\mathfrak{E}_{\mathrm{bind}}$ | $\beta$-decay $Q$-value $\mathfrak{Q}_\beta$ |
| **bar-parity** | bar-even ($\sigma$-fixed, $x+\sigma x$) | bar-odd ($\sigma$-anti, $x-\sigma x$) |
| **eigenvalue function** | $\tfrac{q+q^{-1}}{2}=\cosh\lambda$ | $\tfrac{q-q^{-1}}{2}=\sinh\lambda$ |
| **archimedean evaluation** | real $q$ (hyperbolic) | root-of-unity $q$ ($\cosh\!\to\!\cos$, $\sinh\!\to\! i\sin$) |
| **Neumann–Zagier analogue** | $\operatorname{Vol}(K)$ | $\mathrm{CS}(K)$ |
| **physical character** | strong / stable / confining | weak / unstable / anti-binding |
| **open number** | binding $\Delta_\lambda$ gap | $\mathfrak{Q}_\beta$ $c_k$ residual |

Closing either column is expected to close the other: they are the real and imaginary parts of the *same* unclosed defect.

_(draft.)_
