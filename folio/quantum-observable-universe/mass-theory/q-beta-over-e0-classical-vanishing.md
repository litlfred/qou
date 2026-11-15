*Let $\mathfrak{Q}_\beta(q)$ and $E_0^{(N{=}0)}(q)$ be the substrate closed forms from [`prop:neutron-qvalue-symbolic`](../nuclear-interactions/neutron-qvalue-symbolic.md) and [`rem:beta-decay-energy-scale`](../nuclear-interactions/beta-decay-energy-scale.md):*

$$
\mathfrak{Q}_\beta(q) \;=\; m_e \cdot \frac{(2q + 1 - q^2)(q+1)}{2q^3},
\qquad
E_0^{(N=0)}(q) \;=\; \frac{m_e}{q(q-1)}.
$$

*The ratio*

$$
S(q) \;\coloneqq\; \frac{\mathfrak{Q}_\beta(q)}{E_0^{(N{=}0)}(q)} \;=\; \frac{(2q + 1 - q^2)\,(q^2 - 1)}{2 q^2}
$$

*satisfies $S(q = 1) = 0$ as an algebraic identity over any commutative ring.*

One reading has $c_k$ coming from the $u_{\text{ladder}}$ Taylor expansion of $S(q) = \mathfrak{Q}_\beta(q)/E_0(q)$. Taken literally, this is degenerate. The Taylor expansion of $S/S(1)$ around $q = 1$ is $0/0$. The proved $c_2 = -1$ cannot be recovered this way.

The term $S = \mathfrak{Q}_\beta / E_0$ is the SDP-constraint scalar (canonical at $q_0$, matching the affine target $n_{\text{target}} = S(q_0) \approx 0.18689$). The $c_k$ ladder normalization is $\mathfrak{Q}_\beta / [Q_A \cdot \cos(\alpha_{\text{eff}})]$, with $Q_A$ and $\alpha$ read from the operator-valued $N{=}3$ witness. This proposition exposes the algebraic obstruction that identifies the missing categorical input ($Q_A(q)$ and $\alpha(q)$).

The vanishing $S(1) = 0$ provides the direct-algebraic witness. An operator-theoretic witness arrives from the SDP strict-complementarity analysis. Both routes converge on the bare substrate scale $Q_A$. That scale is the retired Form A ($+0.168\%$ without CODATA input, kept as a historical cross-check); the ruled convention-D base, the Markov trace at $z_D$, gives $0.4447$ MeV ($-43.16\%$). The correction to the base is the $c_k$ ladder, which under convention D is not yet derived. Its normalization is not $S = \mathfrak{Q}_\beta/E_0$.
