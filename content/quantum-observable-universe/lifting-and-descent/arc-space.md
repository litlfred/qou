**Definition.**
*Let $X$ be a variety in $\mathbf{C}$ — typically the exceptional
divisor of a collision locus, the singular state of a tangled braid,
or a fluid blow-up
([recursive brane tower](#def:recursive-brane-tower)).
Its **$n$-th jet scheme** $\mathcal{L}_n(X)$ is the scheme
representing the functor*

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

**Identification with the brane tower.** The QOU framework's
recursive brane tower
$\mathcal{S}_0 \hookrightarrow \mathcal{S}_1 \hookrightarrow
\mathcal{S}_2 \hookrightarrow \cdots$
([recursive brane tower](#def:recursive-brane-tower))
is exactly a tower of jet schemes: the $n$-th jet prolongation
$j^n v$ of a section $v$
([jet prolongation](#prop:jet-prolongation))
is an $R$-point of $\mathcal{L}_n(X)$, and the inverse limit of the
brane tower coincides with $\mathcal{L}(X)$. Schematically,

$$
  \mathcal{S}_n \;\equiv\; \mathcal{L}_n(X),
  \qquad
  \mathcal{S}_\infty
  \;:=\;\varprojlim_n \mathcal{S}_n
  \;\equiv\;
  \mathcal{L}(X).
$$

**Why arc spaces.** Even when the underlying base $X$ is singular —
a vortex reconnection, an exceptional divisor of a fluid blow-up, a
braid resolution with crossings — the arc space $\mathcal{L}(X)$
contains all the formal data needed to evaluate the variety
*algebraically*, without recourse to differential calculus or
analytic charts. This is the precondition for the
[motivic mass measure](#def:motivic-mass-measure):
a measure assigning a finite, well-defined "volume" to subsets of
$\mathcal{L}(X)$ even when $X$ itself has no smooth volume form.

The brane tower thus inherits, through the arc-space identification,
the full apparatus of motivic integration. The next step
([algebraic quantum volume](#def:algebraic-quantum-volume)) makes
this measure explicit.
