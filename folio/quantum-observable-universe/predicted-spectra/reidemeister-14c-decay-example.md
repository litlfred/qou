## Tracking the ${}^{14}\mathrm{C}$ decay

The move accounting of [the Reidemeister action table](#prop:reidemeister-action-table) tracks each contribution to the ${}^{14}\mathrm{C} \to {}^{14}\mathrm{N}$ beta decay:

| Quantity | Formula | Source moves |
|----------|---------|:---:|
| Parent mass | $\text{Vol}(\mathcal{N}(6,8)) / \hbar_q^2$ | R2 steps in parent |
| Daughter mass | $\text{Vol}(\mathcal{N}(7,7)) / \hbar_q^2$ | R2 steps in daughter |
| $Q$-value | $M_{\text{par}} - M_{\text{dau}} - m_e$ | Difference in R2 steps |
| $L_0$ amplitude | Skein weight of $e^- \sqcup \nu^{\sigma}$ | Skein crossing change |
| Matrix element | $\lVert\hat{V}(L_0)\rVert^2$ | R2 at converting generator |
| Writhe correction | $(-q^{3/4})^{-\Delta w}$ | R1 (writhe change = $A - 1$) |
| Half-life | $\ln 2 / (\lVert M_q\rVert^2 \times f(Z, Q))$ | All of the above |
