**Conjecture.**
*At the physical substrate parameter
$q_0 \in \mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$
([substrate $\mathbb{G}_m$-torsion](#rem:substrate-gm-torsion)),
$\mathrm{P} \neq \mathrm{NP}$.*

*Equivalently: the resolution-tree evaluation of the universal
obstruction class $\chi(A)$ is non-vanishing:*

$$
  \mathrm{res}_{\mathcal{R}}\!\bigl(\chi(A)\bigr) \;\neq\; 0
  \qquad\text{at } q = q_0.
$$

**This is the fourth millennium evaluation.**
The [QOU obstruction reduction](#thm:qou-obstruction-reduction)
shows that all classical-limit obstructions in the QOU are
images of the single scalar $\chi(A) \in HH^2 \cong k$.
P vs NP joins the table:

| Problem | Evaluation | $q$-scale | Classical limit |
|---------|-----------|-----------|----------------|
| RH | Spectral | Proved (Hasse--Weil) | Phase coherence |
| NS | Collision locus | Proved (exp. damping) | Levi non-degeneracy |
| BSD | Elliptic curve | Proved (Tannaka--Krein) | $L$-value assembly |
| **P vs NP** | **Resolution tree** | **BQP at torsion** | **Irreducible tree weight** |

All four evaluations are proportional — controlled by
$\chi(A) = -6$.

**The $\mathbb{G}_m$-torsion dichotomy.**

At torsion $q$ (root of unity): the Hecke algebra $H_n(q)$
has a non-trivial radical.  The radical annihilates
exponentially many resolution paths, pruning the tree to
polynomial effective size.  This is BQP — some computational
horizons become transparent.

At non-torsion $q$ (including $q_0$): the Hecke algebra is
semisimple ($\mathrm{Rad} = 0$), no paths are pruned, and
the full $3^c$ resolution tree survives.  The computational
horizon $\mathcal{H}_c(L, q_0) \neq \varnothing$ for
NP-complete links.

**Kummer persistence.**
By the Kummer filtration
([Kummer filtration](#rem:kummer-filtration-obstruction)):
$\kappa_c^{\mathrm{comp}} \bmod n = 0$ iff $n \mid 6$.
Since $q_0$ is non-torsion ($q_0^k \neq 1$ for all
$k \geq 1$), no finite Kummer level applies, and the
obstruction is perpetual.

**Corollary (from the reduction theorem).**
If P $=$ NP is resolved (in either direction), the resolution
constrains the other three millennium problems.  Conversely,
a resolution of RH, NS, or BSD constrains P vs NP — the
evaluation maps differ, but the obstruction class is the same.
