Let $V$ be a complex vector space that is the algebraic direct sum $V = \bigoplus_j V_j$ of finite-dimensional subspaces, and let $\Delta_q \colon V \to V$ be a linear operator with $\Delta_q(V_j) \subseteq V_j$ for every $j$. (For the function algebra of a quantum observable universe the $V_j$ are the Peter–Weyl isotypic components and $\Delta_q$ is the $q$-Laplacian of [prop:q-heat-equation-exists](#prop:q-heat-equation-exists).) Write $\pi_j \colon V \to V_j$ for the projections. A *solution* of the $q$-heat equation $\partial_t u = -\Delta_q u$ on $[0, T)$ is a map $u \colon [0, T) \to V$ such that every $\pi_j u$ is differentiable and $\tfrac{d}{dt}\, \pi_j u = -\Delta_q\, \pi_j u$.

Then for every $u_0 \in V$ there is exactly one solution with $u(0) = u_0$, namely

$$
  \pi_j u(t) \;=\; \exp\!\bigl(-t\, \Delta_q|_{V_j}\bigr)\, \pi_j u_0
  \qquad \text{for all } j .
$$
