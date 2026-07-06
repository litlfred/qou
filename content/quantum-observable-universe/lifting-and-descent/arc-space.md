**Definition.**
*Let $X$ be a variety in $\mathbf{C}$ — typically the exceptional divisor of a collision locus, the singular state of a tangled braid, or a fluid blow-up ([recursive brane tower](#def:recursive-brane-tower)). Its **$n$-th jet scheme** $\mathcal{L}_n(X)$ is the scheme representing the functor*

$$
  R \;\longmapsto\;
  \mathrm{Hom}_{\mathrm{Sch}}\!\bigl(
    \mathrm{Spec}\,R[t]/(t^{n+1}),\; X
  \bigr).
$$

*The **arc space** of $X$ is the inverse limit*

$$
  \mathcal{L}(X)
  \;=\;
  \varprojlim_{n}\; \mathcal{L}_n(X).
$$

**Identification with the brane tower.** The QOU framework's recursive brane tower $\mathcal{S}_0 \hookrightarrow \mathcal{S}_1 \hookrightarrow \mathcal{S}_2 \hookrightarrow \cdots$ ([recursive brane tower](#def:recursive-brane-tower)) is a tower of jet schemes. The $n$-th jet prolongation $j^n v$ of a section $v$ ([jet prolongation](#prop:jet-prolongation)) is an $R$-point of $\mathcal{L}_n(X)$, and the inverse limit coincides with $\mathcal{L}(X)$:

$$
  \mathcal{S}_n \;\equiv\; \mathcal{L}_n(X),
  \qquad
  \mathcal{S}_\infty
  \;:=\;\varprojlim_n \mathcal{S}_n
  \;\equiv\;
  \mathcal{L}(X).
$$

**Role of arc spaces.** When the base $X$ is singular — a vortex reconnection, an exceptional divisor, or a braid resolution — the arc space $\mathcal{L}(X)$ retains the formal data required to evaluate the variety algebraically without analytic charts. This algebraic evaluation grounds the [motivic mass measure](#def:motivic-mass-measure), assigning a finite "volume" to subsets of $\mathcal{L}(X)$ even when $X$ lacks a smooth volume form.

Through the arc-space identification, the brane tower inherits motivic integration. The next step ([algebraic quantum volume](#def:algebraic-quantum-volume)) makes this measure explicit.
