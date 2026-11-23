**Proposition.** *Let $K$ be a linearly ordered field, $\nu > 0$ a viscosity, $\delta \geq 0$ a time step, and $(k_n)_{n \geq 0}$ positive wavenumbers with $\delta\,\nu k_n^2 \leq 1$.*

1. *(Per-rung equilibrium.) A rung $u : \mathbb{N} \to K$ with $u(0) = 0$, forced by a constant $F \geq 0$ and damped at its own dissipation rate,*
   $$
   u(t+1) \;\leq\; u(t) + \delta\bigl(k_n F - \nu k_n^2\, u(t)\bigr),
   $$
   *satisfies $u(t) \leq F/(\nu k_n)$ for every $t$.*

2. *(Trajectory composition.) For a rung family $u_n(t) \geq 0$ with $u_{n+1}(0) = 0$, boundary bound $\sup_t u_0(t) \leq P$, and each rung forced by the square of the actual trajectory below it, every rung obeys the composed bound $u_n(t) \leq B_n$, where $B_0 = P$ and $B_{n+1} = B_n^2/(\nu k_{n+1})$.*

3. *(Geometric collapse.) If in addition the dissipation-scale condition $B_n \leq \theta\,\nu k_{n+1}$ holds with $0 \leq \theta \leq 1$, then*
   $$
   u_n(t) \;\leq\; \theta^{\,n} P \qquad \text{for all } n, t.
   $$

4. *(Stability under nonlocal transfer.) The equilibrium and the collapse persist when each rung is forced by its two predecessors with weight $\gamma \geq 0$ (pairwise maxima decay at rate $\theta$ per pair), and when every pair of rungs is coupled with geometric weight $\lambda^{\,n-m-1}$, $0 \leq \lambda < 1$ (every rung beyond the band is uniformly $\theta$-suppressed under $B \leq \theta(1-\lambda)\nu k_n$).*
