**Definition.**
*Let $X$ be a variety in $\mathbf{C}$—typically the exceptional divisor of a collision locus, the singular state of a tangled braid, or a fluid blow-up. Its **$n$-th jet scheme** $\mathcal{L}_n(X)$ rigorously represents the functor:*
$$
  R \longmapsto \mathrm{Hom}_{\mathrm{Sch}}\!\bigl(\mathrm{Spec}\,R[t]/(t^{n+1}),\; X\bigr).
$$
*The **arc space** of $X$ is the formal inverse limit:*
$$
  \mathcal{L}(X) = \varprojlim_{n} \mathcal{L}_n(X).
$$

**Identification with the brane tower.** The QOU framework's recursive brane tower $\mathcal{S}_0 \hookrightarrow \mathcal{S}_1 \hookrightarrow \cdots$ mathematically forms a tower of jet schemes. The $n$-th jet prolongation $j^n v$ of a section $v$ acts as an $R$-point of $\mathcal{L}_n(X)$. The inverse limit physically coincides with $\mathcal{L}(X)$:
$$
  \mathcal{S}_n \equiv \mathcal{L}_n(X), \qquad \mathcal{S}_\infty := \varprojlim_n \mathcal{S}_n \equiv \mathcal{L}(X).
$$

**Role of arc spaces.** When the base $X$ is singular—a vortex reconnection, an exceptional divisor, or a braid resolution—the arc space $\mathcal{L}(X)$ safely retains the formal data necessary to evaluate the variety algebraically without analytic charts. This algebraic evaluation grounds the [motivic mass measure](#def:motivic-mass-measure), predictably assigning a finite volume to subsets of $\mathcal{L}(X)$ even when $X$ inherently lacks a smooth volume form.

Through this arc-space identification, the brane tower natively inherits motivic integration. The [algebraic quantum volume](#def:algebraic-quantum-volume) formally makes this measure explicit.
