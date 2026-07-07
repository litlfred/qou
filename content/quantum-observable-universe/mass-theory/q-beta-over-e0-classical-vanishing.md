**Proposition.** *Let $\mathfrak{Q}_\beta(q)$ and $E_0^{(N{=}0)}(q)$ be the substrate closed forms from [`prop:neutron-qvalue-symbolic`](neutron-qvalue-symbolic.md) and [`rem:beta-decay-energy-scale`](beta-decay-energy-scale.md):*

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

The shape-collapse audit states that $c_k$ comes from the $u_{\text{ladder}}$ Taylor expansion of $S(q) = \mathfrak{Q}_\beta(q)/E_0(q)$. Taken literally, this is degenerate. The Taylor expansion of $S/S(1)$ around $q = 1$ is $0/0$. The proved $c_2 = -1$ cannot be recovered this way.

The term $S = \mathfrak{Q}_\beta / E_0$ is the SDP-constraint scalar (canonical at $q_0$, matching the affine target $n_{\text{target}} = S(q_0) \approx 0.18689$). The $c_k$ ladder normalization is $\mathfrak{Q}_\beta / [Q_A \cdot \cos(\alpha_{\text{eff}})]$, with $Q_A$ and $\alpha$ read from the operator-valued $N{=}3$ witness. This proposition exposes the algebraic obstruction that identifies the missing categorical input ($Q_A(q)$ and $\alpha(q)$).

The vanishing $S(1) = 0$ provides the direct-algebraic witness. An operator-theoretic witness arrives from the SDP strict-complementarity analysis. Both routes converge: the bare substrate scale $Q_A$ predicts $\mathfrak{Q}_\beta$ to $0.168\%$ without CODATA input. The sub-ppb correction is the $c_k$ ladder. Its normalization is not $S = \mathfrak{Q}_\beta/E_0$.
