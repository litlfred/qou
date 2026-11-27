Let $(\mathbf{C}, A, \tau)$ be the Descartes universe over Bring's surface $\Sigma_4$ of genus $4$ with $\chi_{\mathrm{eu}}(M_0) = -6$, and consider an anti-parallel vortex pair of linking number $\mathrm{lk}$ meeting along a one-dimensional locus $\Sigma \subset \Sigma_4$ at a point $p \in \Sigma$. Under the four directional hypotheses linking a local Euler-index datum $e(\xi)|_p$ to a zero of the Reeb section at $p$ and linking a per-jet datum $\delta_n|_\Sigma$ ($n \geq 1$) to divergence of the $n$-th velocity jet on $\Sigma$, one has the formal equivalences:

1. $\mathrm{lk} \cdot e(\xi)|_p \neq 0$ if and only if the chosen Reeb section vanishes at $p$;
2. for every $n \geq 1$, $\delta_n|_\Sigma \neq 0$ if and only if the $n$-th velocity jet diverges on $\Sigma$.

On Bring's surface $\Sigma_4$ itself, however, these local data do not assemble into a non-zero sheaf-cohomological restriction $\kappa_n|_\Sigma \in H^2(\Sigma, \mathcal{B}|_\Sigma)$: every restriction to the one-dimensional locus $\Sigma$ vanishes identically because $H^2(\Sigma, \cdot) = 0$, while the global Reeb Euler class is $e(\xi) = -6 \in H^2(\Sigma_4, \mathbb{Z})$ ([NS-regular QOU](#def:ns-regular-qou)).

**Proof and geometric scope.**

**(a) Global Euler class vs.\ point excision.**

The global Euler class $e(\xi) \in H^2(\Sigma_4, \mathbb{Z}) \cong \mathbb{Z}$ of the Reeb $\mathrm{U}(1)$-bundle satisfies $\deg e(\xi) = \chi_{\mathrm{eu}}(M_0) = -6$. Restricting directly to the one-dimensional curve $\Sigma$ gives $e(\xi)|_\Sigma = 0 \in H^2(\Sigma, \mathbb{Z}) = 0$. Excision around an isolated point $p \in \Sigma_4$ gives

$$
  H^2_{\{p\}}(\Sigma_4, \mathbb{Z})
   \cong 
  H^2(D^2, S^1; \mathbb{Z})
   \cong 
  \mathbb{Z},
$$

and by Poincaré--Hopf the local indices $\mathrm{ind}_p(s) \in \mathbb{Z}$ of any section $s$ with isolated zeros sum to $\sum_p \mathrm{ind}_p(s) = -6$. Topology forces $s$ to vanish somewhere on $\Sigma_4$, though a finite zero set can be isotoped off any given one-dimensional curve $\Sigma$, so whether a flow-adapted section vanishes on $\Sigma$ is an open analytical question rather than a topological consequence of $\chi(\Sigma_4) = -6$.

**(b) Pointwise Biot--Savart jet growth vs.\ sheaf cohomology.**

By [Euler characteristic stability](#prop:euler-char-stability), the surface Euler characteristic $\chi = -6$ is independent of jet level $n$. Under a self-similar filament-approach ansatz $d \sim (T^* - t)^{1/2}$ with Biot--Savart profile $v \sim \Gamma/(2\pi d)$, the pointwise $(n+1)$-jet magnitude scales as

$$
  |j^n v|_\Sigma
   \sim 
  \frac{\Gamma}{d^{n+1}}
   \sim 
  \frac{1}{(T^* - t)^{(n+1)/2}}.
$$

This scaling describes a pointwise analytic norm conditional on $d \to 0$, whereas the sheaf-cohomological jet group $H^2(\Sigma_4, \mathcal{O}_{\Sigma_4}) = 0$ vanishes identically on the complex curve $\Sigma_4$, so no non-zero cohomology class $\delta_n \in H^2(\Sigma_4, \mathcal{O}_{\Sigma_4})$ arises.

**(c) Consequence.**

The formal conjunction of (1) and (2) follows immediately from the paired directional hypotheses, while in sheaf cohomology on $\Sigma_4$ the global invariant is $\mathrm{NS}(A) = e(\xi) = -6 \in H^2(\Sigma_4, \mathbb{Z})$ and the curve restriction $\kappa_n|_\Sigma \in H^2(\Sigma, \cdot) = 0$ vanishes for every $n$. $\square$
