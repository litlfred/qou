Let $T$ be a splay with coordinate algebras $A_i$, with a strongly
filtered [Poisson structure](#def:skewed-poisson-structure) $\pi$, and let
$\cdot$ denote the multiplication of $S = \bigotimes_i A_i$ (transported to
$T$ through a choice of ordering $<$ on $I$). A map
$\Delta \colon T \to T \otimes T$ is **strongly multiplicative** with respect
to $<$ if
$$
  \Delta \circ \pi \;=\; (\cdot \otimes \pi \;+\; \pi \otimes \cdot \;+\; \pi \otimes \pi)
  \circ (1 \otimes \tau \otimes 1) \circ \Delta,
$$
where $\tau$ is the flip of tensor factors.

For the tensor algebra of a Lie algebra $\mathfrak{g}$ with the diagonal
comultiplication, the $\pi \otimes \pi$ term vanishes on $\mathfrak{g}$ and the
condition reduces to the usual multiplicativity of a Lie bialgebra
(\cite{leitner2006}, Remark 1.12).

**Consequence** (\cite{leitner2006}, Proposition 1.13). If each $A_i$ carries
an algebra map $\Delta_i \colon A_i \to A_i \otimes A_i$ and the induced
$\Delta$ on $T$ is strongly multiplicative, then $\Delta$ descends to an
algebra map $U \to U \otimes U$ on the quotient
$U = T / (fg - gf - \pi(f, g))$ of
[the integration theorem](#thm:skew-poisson-integrates).

Reference: \cite{leitner2006}, Definition 1.11 and Proposition 1.13.
