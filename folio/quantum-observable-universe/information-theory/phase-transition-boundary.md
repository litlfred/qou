Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $N$ particle knots in a region $U$. A **phase transition** occurs at a critical temperature $T_q^{(c)}$. At this temperature, the dominant saddle point of the partition function $Z_q$ jumps discontinuously between topologically distinct sectors of $\mathrm{Conf}(U)$.

The **$S^3$ boundary action** dictates the critical temperatures. It restricts the categorical action $\mathfrak{S}_q$ to the Hopf base $S^2$ of the fibration $S^1 \hookrightarrow S^3_q \to S^2$:
$$
  \mathfrak{S}_q^{(\partial)} = \mathrm{tr}_{\mathrm{Ad}} \!\oint_{S^2} \omega_{\mathcal{F}} \,\wedge\, *\eta_q,
$$
This is the non-abelian Stokes surface integral of the adjoint connection.

The gas--liquid critical temperature is
$$
  T_q^{(g \to l)} = \frac{\mathfrak{S}_q^{(\partial)}}{[2]_q}.
$$
The liquid--solid critical temperature is
$$
  T_q^{(l \to s)} = \frac{\mathfrak{S}_q^{(\partial)}}{[2]_q \cdot [n_K]_q},
$$
where $n_K$ denotes the crossing number of the particle knot.

Sublimation represents a direct solid--gas transition. It occurs when the intermediate liquid phase is not populated at any temperature between the two critical values.

No Hecke extension class obstructs that phase, because there are no non-split extensions here to carry one. The symmetric and antisymmetric channels are the $q$- and $-q^{-1}$-eigenspaces of the braiding $\sigma$ ([The Iwahori--Hecke algebra $H_n(q)$ as a categorical quotient](#rem:hecke-algebra-from-braiding)), and the eigenprojections
$$
  e_{+} = \frac{\sigma + q^{-1}}{[2]_q},
  \qquad
  e_{-} = \frac{q - \sigma}{[2]_q}
$$
are orthogonal idempotents summing to $1$ whenever $[2]_q$ is invertible — the same condition the two critical temperatures above already require, since they divide by it. So $V^{\otimes 2} = S^2 V \oplus \Lambda^2 V$ is a direct sum, not an extension. For general $n$ the conclusion follows instead from semisimplicity: at a substrate parameter that is not a root of unity, $H_n(q)$ is semisimple ([Complete decomposition of the tensor tower](#prop:knot-eigenbasis-complete)(1)), so every short exact sequence of $H_n(q)$-modules splits and $\mathrm{Ext}^1_{H_n(q)}$ vanishes on every pair of modules.

Over the Laurent ring $\mathbb{Z}[q, q^{-1}]$, where $[2]_q$ is not invertible, extensions of the antisymmetric channel by the symmetric one are classified by $\mathbb{Z}[q, q^{-1}] / ([2]_q) \cong \mathbb{Z}[q, q^{-1}] / (q^2 + 1) \cong \mathbb{Z}[i]$. That group is supported on $q^2 = -1$, which no real $q$ meets, so the archimedean realisation never leaves the split case. What selects sublimation over a stable liquid phase is left open.
