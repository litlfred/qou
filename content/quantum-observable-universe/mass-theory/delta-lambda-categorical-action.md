The per-block phase density $\Delta_\lambda$ for a partition $\lambda$ is resolved by evaluating the $q$-Reeb phase density over the partition.

The phase contribution from a single block in the categorical framework is defined via the fundamental action map:
$$ g(x) = -\mathrm{Li}_2^q(-x) $$
where $x$ is the spectral coordinate associated with the block, and $\mathrm{Li}_2^q$ is the quantum dilogarithm. 

In the context of the $q$-Reeb flow (cf. [Categorical q-Reeb flow](#def:categorical-q-reeb-flow)), the phase density over a partition $\lambda$ is determined by the trace over the associated categorical channels. We isolate the bar-even channel, which corresponds to the $\cosh$ projection of the action.

The quantum dilogarithm evaluates over the spectral weights $x_w$ associated with the constituent blocks $w \in \lambda$. The action $g(x)$ splits under the algebraic bar involution $q \leftrightarrow q^{-1}$ into bar-even and bar-odd channels. 

The bar-even channel is given by:
$$ g_{\text{even}}(x) = \frac{1}{2} \left( g(x) + g(x^{-1}) \right) $$
which corresponds structurally to the $\cosh$-like channel in the categorical Reeb flow. The anti-symmetric bar-odd component (the Faddeev $\Phi_q$ channel) governs topological interference but decouples from the strict mass density.

When evaluated over the partition $\lambda$, the $q$-Reeb phase density $\Delta_\lambda$ is the evaluation of this bar-even channel across the eigenvalues associated with all blocks in $\lambda$:
$$ \Delta_\lambda = \prod_{w \in \lambda} \exp\left( g_{\text{even}}(x_w) \right) $$

By projecting out the bar-odd phase, $\Delta_\lambda$ acts as the canonical structural coefficient for the partition $\lambda$, providing the exact evaluation of the phase density from the categorical action $g(x) = -\mathrm{Li}_2^q(-x)$.
