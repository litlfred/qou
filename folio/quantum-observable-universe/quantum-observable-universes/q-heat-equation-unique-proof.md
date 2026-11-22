*Proof.* Because each $V_j$ is $\Delta_q$-stable, $\pi_j \Delta_q = \Delta_q \pi_j$, so the equation splits into one linear ODE on each finite-dimensional space $V_j$.

*Existence.* The displayed formula gives a differentiable curve in $V_j$ with $\tfrac{d}{dt}\pi_j u = -\Delta_q \pi_j u$. Only the finitely many $j$ with $\pi_j u_0 \neq 0$ give a nonzero component, so $u(t)$ lies in the algebraic direct sum $V$.

*Uniqueness.* Let $u$ be any solution with $u(0) = u_0$ and fix $j$. Put $w(t) = \exp(t\,\Delta_q|_{V_j})\, \pi_j u(t)$. Then

$$
  \dot w(t) \;=\; \exp(t\,\Delta_q|_{V_j})\,\bigl(\Delta_q\, \pi_j u(t) + \tfrac{d}{dt}\pi_j u(t)\bigr) \;=\; 0 ,
$$

so $w$ is constant, equal to $w(0) = \pi_j u_0$. Hence $\pi_j u(t) = \exp(-t\,\Delta_q|_{V_j})\,\pi_j u_0$. This holds for every $j$, and $u(t)$ is determined by its projections. $\square$

No semisimplicity of $\Delta_q$ is used: the matrix exponential on each $V_j$ handles a non-diagonalisable block as well.
