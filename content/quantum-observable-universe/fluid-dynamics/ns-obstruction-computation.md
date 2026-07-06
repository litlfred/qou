Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with $\chi(A) = -6$ (Bring's surface of genus 4). Let $\Sigma$ be the collision locus of an anti-parallel vortex pair with linking number $\mathrm{lk} = 1$.

The [NS obstruction](#prop:ns-obstruction-tower) at level $n$ restricted to $\Sigma$ is $\kappa_n|_\Sigma = \mathrm{lk} \cdot e(\xi)|_\Sigma + \delta_n|_\Sigma$. We compute each term.

**(a) The Euler class term.**
The Euler class $e(\xi) \in H^2(\Sigma_4, \mathbb{Z})$ of the Reeb bundle satisfies $\mathrm{tr}(e(\xi)) = \chi(A) = -6$. Bring's surface is a closed orientable surface, so $H^2(\Sigma_4, \mathbb{Z}) \cong \mathbb{Z}$. Thus $e(\xi) = -6$ as an integer.

The restriction to $\Sigma$ (a contractible line segment) yields $e(\xi)|_\Sigma = 0$ in $H^2(\Sigma, \mathbb{Z})$. However, the local Euler class at a point $p \in \Sigma$ is measured by the local cohomology $H^2_{\{p\}}(\Sigma_4, \mathbb{Z})$, which is nonzero. By excision:

$$
  H^2_{\{p\}}(\Sigma_4, \mathbb{Z})
   \cong 
  H^2(D^4, S^3; \mathbb{Z})
   \cong 
  \mathbb{Z},
$$

where $D^4$ is a small ball around $p$ and $S^3$ is its boundary. The Euler class restricts to the local degree at $p$:

$$
  e(\xi)|_p = -6 \cdot \deg_p(\xi) \in \mathbb{Z}.
$$

For a generic point, $\deg_p(\xi) = 0$ (the Reeb vector field is nonvanishing). At a vortex collision point, the Reeb field has a zero (the contact structure degenerates if the core flattens). The value $\deg_p(\xi)$ is the index of this zero.

**(b) The jet correction term.**
The jet correction $\delta_n$ at level $n$ in the Yekutieli tower is computed from the $n$-th iterated jet prolongation. By [Euler characteristic stability](#prop:euler-char-stability), $\chi(E_n) = \chi(A) = -6$ for all $n$. The topological contribution does not change with level.

The analytic contribution $\delta_n|_\Sigma$ depends on the $(n+1)$-jet of the velocity field at $\Sigma$. For the anti-parallel pair, the velocity field has the Biot–Savart structure $v \sim \Gamma/(2\pi d)$ near the collision, with jets diverging as $d \to 0$:

$$
  |j^n v|_\Sigma
   \sim 
  \frac{\Gamma}{d^{n+1}}
   \sim 
  \frac{1}{(T^* - t)^{(n+1)/2}}.
$$

The jet correction $\delta_n|_\Sigma$ is controlled by $|j^n v|$. It is nonzero whenever the $n$-th jet diverges. For the anti-parallel pair, $|j^n v| \to \infty$ for all $n \geq 1$ as $t \to T^*$.

**(c) The total obstruction.**
The NS obstruction at the collision locus has two components:
1. **Topological:** $\mathrm{lk} \cdot e(\xi)|_p$. This is nonzero if and only if the Reeb field has a zero at $p$ (i.e. the contact structure degenerates).
2. **Analytic:** $\delta_n|_\Sigma$. This is nonzero whenever the $n$-th jet of the velocity diverges (for all $n \geq 1$ in the anti-parallel case).

The topological and analytic terms live in complementary subgroups of $H^2(\mathcal{S}, \mathcal{B})$ (by the [QU-to-QOU theorem](#thm:qu-to-qou)). Therefore:
- If the Reeb field has no zero at $p$ ($\deg_p(\xi) = 0$): the topological term vanishes, but the analytic term $\delta_n|_\Sigma \neq 0$ persists. The obstruction is purely analytic and the contact structure is non-degenerate. This is the NS-singular case (blowup).
- If the Reeb field has a zero at $p$ ($\deg_p(\xi) \neq 0$): both terms are nonzero and cannot cancel across complementary subgroups. The obstruction is again nonzero. This is also NS-singular.

**(d) Result.**
For the Descartes universe with $\chi(A) = -6$:

$$
  \kappa_n\big|_\Sigma  \neq  0
  \qquad\text{for all } n \geq 1.
$$

The analytic term $\delta_n|_\Sigma$ is nonzero because the jets of the Biot–Savart velocity diverge at the collision. The topological term is either zero or nonzero, but the total obstruction is always nonzero because the two terms cannot cancel.

Therefore, $\mathrm{Obs}_\partial(A) = 0$ and the Descartes universe is **NS-singular**.

*Formal asymptotic content. The jet divergence $|j^n v|_\Sigma \sim 1/(T^*-t)^{(n+1)/2}$ has $\ordw(\lvert j^n v \rvert_\Sigma) = -\tfrac{n+1}{2}\,\ordw(T^*-t)$ as $t \to T^*$. The recursive jet tower is the [surreal blow-up calculus](#def:surreal-blowup-calculus), and the $q \to 1$ classical-limit reading is the [standard-part functor](#def:standard-part-functor).*

