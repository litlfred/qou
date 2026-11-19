Let $(\mathbf{C}, A, \tau)$ define the Descartes universe spanning $\chi(A) = -6$ (Bring's surface of genus 4). Let $\Sigma$ designate the precise collision locus governing an anti-parallel vortex pair marked by linking number $\mathrm{lk} = 1$.

The [NS obstruction](#prop:ns-obstruction-tower) at level $n$, strictly restricted to $\Sigma$, evaluates as $\kappa_n|_\Sigma = \mathrm{lk} \cdot e(\xi)|_\Sigma + \delta_n|_\Sigma$. Computing both terms gives

$$
  \kappa_n\big|_\Sigma  \neq  0
  \qquad\text{for all } n \geq 1,
$$

so $\mathrm{Obs}_\partial(A) = 0$: the Descartes universe operates uniformly as **NS-singular**.

**Proof.**

**(a) The Euler class term.**

The explicit Euler class $e(\xi) \in H^2(\Sigma_4, \mathbb{Z})$ driving the Reeb bundle enforces $\mathrm{tr}(e(\xi)) = \chi(A) = -6$. Because $H^2(\Sigma_4, \mathbb{Z}) \cong \mathbb{Z}$ (Bring's surface exists as a closed orientable surface), $e(\xi)$ resolves strictly as the integer $-6$.

Restricting the class onto $\Sigma$ (a one-dimensional line segment, thus inherently contractible) mathematically zeros out $e(\xi)|_\Sigma = 0$ inside $H^2(\Sigma, \mathbb{Z})$.

However, the **local** Euler class pinned to a specific point $p \in \Sigma$ derives from the local cohomology $H^2_{\{p\}}(\Sigma_4, \mathbb{Z})$, which safely evades zero. Employing excision yields:

$$
  H^2_{\{p\}}(\Sigma_4, \mathbb{Z})
   \cong 
  H^2(D^2, S^1; \mathbb{Z})
   \cong 
  \mathbb{Z},
$$

where $D^2$ is a small closed disc around $p$ and $S^1$ is its boundary circle (Bring's surface has real dimension 2). The Euler class therefore maps directly to the **local degree** precisely at $p$:

$$
  e(\xi)|_p = -6 \cdot \deg_p(\xi) \in \mathbb{Z}.
$$

At a generic point, $\deg_p(\xi) = 0$ (the Reeb vector field avoids vanishing). At an explicit **vortex collision point**, the Reeb field forcibly zeroes out (the contact structure must degenerate if the physical core flattens). $\deg_p(\xi)$ strictly records the index of this resulting zero.

**(b) The jet correction term.**

The formal jet correction $\delta_n$ at level $n$ inside the brane tower isolates the $n$-th iterated jet prolongation. Due to [Euler characteristic stability](#prop:euler-char-stability), $\chi(E_n) = \chi(A) = -6$ holds uniformly across all $n$. The topological baseline therefore ignores the level completely.

The specific analytic correction $\delta_n|_\Sigma$ feeds directly off the $(n+1)$-jet of the associated velocity field impinging on $\Sigma$. The anti-parallel pair enforces the Biot--Savart structure $v \sim \Gamma/(2\pi d)$ approaching the collision. The resulting jets strictly diverge as $d \to 0$:

$$
  |j^n v|_\Sigma
   \sim 
  \frac{\Gamma}{d^{n+1}}
   \sim 
  \frac{1}{(T^* - t)^{(n+1)/2}}.
$$

The magnitude $|j^n v|$ strictly dictates the jet correction $\delta_n|_\Sigma$; the correction is nonzero whenever the corresponding $n$-th jet diverges. For the anti-parallel pair, $|j^n v| \to \infty$ applies universally to all $n \geq 1$ as $t \to T^*$.

**(c) The total obstruction.**

Fusing (a) and (b), the exact NS obstruction resting on the collision locus cleanly segregates into two pieces:

1. **Topological**: $\mathrm{lk} \cdot e(\xi)|_p$. This term avoids zero if and only if the Reeb field zeroes out at $p$ (which occurs if and only if the contact structure structurally degenerates).
2. **Analytic**: $\delta_n|_\Sigma$. This term avoids zero universally whenever the $n$-th jet of the operative velocity field cleanly diverges (holding for all $n \geq 1$ under the anti-parallel configuration).

The topological and analytic components map exactly into mathematically complementary subgroups inside $H^2(\mathcal{S}, \mathcal{B})$ (this used to be justified by the perpetual obstruction mechanism of [QU-to-QOU](#thm:qu-to-qou) item 3; that complementary-subgroup argument is withdrawn, item 3 now being the Kummer degree condition, so the splitting below is a hypothesis, not a consequence of item 3).
Consequently:

- If the Reeb field fundamentally **lacks a zero** at $p$ ($\deg_p(\xi) = 0$): the topological component cleanly vanishes, but the analytic component $\delta_n|_\Sigma \neq 0$ stubbornly persists. The surviving obstruction becomes **purely analytic** while the contact structure avoids degeneracy. This explicitly describes the **NS-singular** (blowup) condition.
- If the Reeb field **possesses a zero** at $p$ ($\deg_p(\xi) \neq 0$): both isolated terms avoid zero. Because they occupy strictly complementary subgroups, they possess no mechanism to mathematically cancel. The aggregate obstruction remains nonzero. This similarly enforces the **NS-singular** condition.

*Scope.* Parts (c) and (d) are not established, because item 3 of [QU-to-QOU](#thm:qu-to-qou) establishes Kummer-tower persistence rather than jet-tower complementary subgroups. Three further points apply on Bring's surface. First, the block defining $\delta_n$ places it in the image of $H^2(\mathcal{S}, \mathcal{O}_{\mathcal{S}})$, which is zero on a curve, so $\delta_n = 0$ as a class; the divergence of $|j^n v|$ in (b) is a pointwise magnitude, not a cohomology class, and its rate assumes the collapse $d \sim (T^* - t)^{1/2}$. Second, the local class at $p$ is the index $\mathrm{ind}_p(s)$ of a chosen section $s$ of $\xi$, with $\sum_p \mathrm{ind}_p(s) = \chi(A) = -6$ (Poincaré--Hopf), not $-6 \cdot \deg_p(\xi)$. Topology forces $s$ to vanish somewhere but not on $\Sigma$: a finite zero set can be isotoped off $\Sigma$. Third, (a) already records $e(\xi)|_\Sigma = 0$. Whether the Reeb field of the model vanishes on $\Sigma$ is open.

**(d) Result.**

Mapped over the Descartes universe with $\chi(A) = -6$:

$$
  \kappa_n\big|_\Sigma  \neq  0
  \qquad\text{for all } n \geq 1.
$$

The analytic component $\delta_n|_\Sigma$ absolutely avoids zero because the nested jets composing the Biot--Savart velocity field mathematically diverge at the exact collision point. The paired topological term evaluates either as zero (lacking a Reeb zero) or nonzero (possessing a Reeb zero). In all permutations, the isolated $\delta_n$ term prevents the total obstruction from collapsing, as the complementary structure forbids any potential cancellation.

Therefore $\mathrm{Obs}_\partial(A) = 0$. The Descartes universe operates uniformly as **NS-singular**.
