Let $\mathcal{L}_k = (A_k, c_k, \mathcal{A}_k)$ be a confinement layer over a strictly linearly ordered commutative ring $K$ \cite{dantzig-wolfe1960,bloch-horowitz1958,schrieffer-wolff1966}.

1. **Conservation-fiber invariance and LP optimality:** For every shadow-price vector $y \in K^{d_k}$ and any two configurations $u, v \in \mathbb{Z}^{m_k}$ in the same conservation fiber $A_k u = A_k v$,
   $$
     \bar{c}_k(y)(u - v) = c_k(u - v).
   $$
   If $u^* \in \mathbb{N}^{m_k}$ satisfies $A_k u^* = b$, $\bar{c}_k(y^*)_j \ge 0$, and $u^*_j \bar{c}_k(y^*)_j = 0$ for all $j$, then $c_k(u^*) = b^\top y^* \le c_k(u)$ for every $u \in \mathbb{N}^{m_k}$ with $A_k u = b$.
2. **Adiabatic confinement stability:** Let $g \in \ker_{\mathbb{Z}}(A_k)$ be an intra-layer motif-fission move satisfying $c_k(g) \ge \Delta_k > 0$, and let $\delta_V(g) \in K$ be the residual Layer-$(k+1)$ cost perturbation on $g$. If $|\delta_V(g)| < \Delta_k$ (equivalently, over a linearly ordered field, $\eta_k := |\delta_V(g)| / \Delta_k < 1$), then
   $$
     c_k(g) + \delta_V(g) > 0,
   $$
   with lower margin $c_k(g) + \delta_V(g) \ge \Delta_k - |\delta_V(g)| > 0$.
3. **Cross-layer deconfinement flip:** Conversely, if $c_k(g) \le \Delta_k$ and an external chemical potential or Fermi pressure drives $-\delta_V(g) > \Delta_k$, then
   $$
     c_k(g) + \delta_V(g) < 0.
   $$
