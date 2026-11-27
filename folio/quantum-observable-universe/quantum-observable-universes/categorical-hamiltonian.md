Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe over a commutative ring $R$ with [categorical Dirac operator](#def:categorical-dirac-operator) $\mathcal{D}_\nabla = q^{-1}\nabla + \hbar_q\,\iota_\xi\nabla$ ($\hbar_q = 1 - q^{-1}$, [quantum Planck constant](#def:quantum-planck-constant)) and [categorical Lagrangian](#def:categorical-lagrangian) $\mathcal{L}_q(\nabla, \psi) = \mathcal{D}_\nabla^2 + \psi^* \otimes \mathcal{D}_\nabla\psi \in \mathrm{End}_{\mathbf{C}}(A)$. Grouping terms by degree $(2, 1, 0)$ in the Reeb contraction $\iota_\xi\nabla$ decomposes $\mathcal{L}_q = \mathcal{L}_2 + \mathcal{L}_1 + \mathcal{L}_0$, where

$$
\begin{aligned}
  \mathcal{L}_2 &= \hbar_q^2\,(\iota_\xi\nabla)^2, \\
  \mathcal{L}_1 &= q^{-1}\hbar_q\,\bigl(\nabla \circ \iota_\xi\nabla + \iota_\xi\nabla \circ \nabla\bigr) + \hbar_q\,\bigl(\psi^* \otimes (\iota_\xi\nabla)\psi\bigr), \\
  \mathcal{L}_0 &= q^{-2}\,\nabla^2 + q^{-1}\,\bigl(\psi^* \otimes \nabla\psi\bigr).
\end{aligned}
$$

Energy in a quantum observable universe is defined as the Legendre transform of $\mathcal{L}_q$ along the Reeb clock direction at two levels:

1. **Operator Reeb-velocity Legendre transform.** Over any commutative ring $R$, the directional Euler Legendre transform $D_v\mathcal{L}_q[v] - \mathcal{L}_q$ along $v = \iota_\xi\nabla$ defines the velocity-form Hamiltonian endomorphism
   $$
     \mathcal{H}_{\mathrm{vel}}(\mathcal{L}_q)
     = 2\,\mathcal{L}_2 + \mathcal{L}_1 - \mathcal{L}_q
     = \mathcal{L}_2 - \mathcal{L}_0 \in \mathrm{End}_{\mathbf{C}}(A),
   $$
   which cancels the degree-$1$ gyroscopic cross-term and Reeb-matter term without dividing by $2$ or assuming that $\nabla$ and $\iota_\xi\nabla$ commute.

2. **Phase-space canonical Reeb-momentum Legendre transform.** Scaling $\iota_\xi\nabla \mapsto \omega\,\iota_\xi\nabla$ by a clock rate $\omega$ and applying a linear [categorical action](#def:categorical-action) trace $\tau$ yields the clock polynomial $L_{\mathrm{clock}}(\omega) = a_2\,\omega^2 + a_1\,\omega + a_0$ with $a_k = \tau(\mathcal{L}_k)$. Over a field $K$ with $2 \neq 0$ and $a_2 \neq 0$, the canonical Reeb momentum $\Pi = 2\,a_2\,\omega + a_1$ defines the **categorical Hamiltonian**
   $$
     H_{\mathrm{can}}(a_2, a_1, a_0; \Pi)
     = \Pi\,\omega - L_{\mathrm{clock}}(\omega)
     = \frac{(\Pi - a_1)^2}{4\,a_2} - a_0.
   $$
   Over an ordered field with $a_2 > 0$, $H_{\mathrm{can}}(a_2, a_1, a_0; \Pi) = \sup_{\omega \in K}\bigl(\Pi\,\omega - L_{\mathrm{clock}}(\omega)\bigr)$, attained uniquely at $\omega = (\Pi - a_1)/(2\,a_2)$. Evaluating at the unit canonical clock momentum $\Pi = 2\,a_2$ gives
   $$
     H_{\mathrm{can}}(a_2, a_1, a_0; 2\,a_2)
     = a_2 - a_1 + \frac{a_1^2}{4\,a_2} - a_0,
   $$
   retaining the first-order minimal Reeb coupling $-a_1$ and the second-order recoil correction $a_1^2/(4\,a_2)$ inside the canonical shift $\Pi - a_1$.

**Three unit charts of the primitive energy.** With causal speed $c_q = q^{-1}/\hbar_q = 1/(q - 1)$ and full-circuit Reeb tick $t_P = \hbar_q^{-1} = q/(q - 1)$, every energy observable in this paper is a projection of $H_{\mathrm{can}}$ in one of three unit charts connected by exact field identities:

| Unit chart | Clock / length normalisation | Energy observable | Exact conversion identity |
|---|---|---|---|
| Aether action / mass chart | Full Reeb circuit $\ell_P = \hbar_q\,t_P = 1$ | Static action $\mathfrak{S}_q$, holonomy mass $\mathfrak{m}$ | Base trace in $K$ |
| Causal-cone / worldline chart | Per-step cone speed $c_q = 1/(q - 1)$ | Rest energy $\mathfrak{E} = \mathfrak{m}\,c_q^2$ | $\mathfrak{E} = \mathfrak{m}/(q - 1)^2$ |
| Electronic / hadronic per-tick chart | Planck circuit tick $t_P = q/(q - 1)$ | Hadronic scale $\mathfrak{E}_0$ | $\mathfrak{E}_0 = (\mathfrak{m}_e c_q^2)/t_P = \mathfrak{m}_e c_q^2 \hbar_q = \mathfrak{m}_e/\bigl(q(q - 1)\bigr)$ |
