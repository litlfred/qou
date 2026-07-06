**Conjecture.**
*At the physical substrate parameter $q_0 \in \mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$ ([substrate $\mathbb{G}_m$-torsion](#rem:substrate-gm-torsion)), $\mathrm{P} \neq \mathrm{NP}$.*

*Equivalently, the resolution-tree evaluation of the universal obstruction class $\chi(A)$ is non-vanishing:*

$$
  \mathrm{res}_{\mathcal{R}}\!\bigl(\chi(A)\bigr)  \neq  0
  \qquad\text{at } q = q_0.
$$

**The fourth millennium evaluation.** The [QOU obstruction reduction](#thm:qou-obstruction-reduction) establishes that all classical-limit obstructions in the QOU are images of the single scalar class $\chi(A) \in HH^2 \cong k$. P vs NP joins RH, NS, and BSD as a fourth restriction of the same class via the resolution-tree evaluation map. All four evaluations are proportional and controlled by $\chi(A) = -6$.

**The $\mathbb{G}_m$-torsion dichotomy.** When $q$ is a root of unity (torsion), the Iwahori--Hecke algebra $H_n(q)$ acquires a non-trivial radical. This radical annihilates exponentially many resolution paths and prunes the tree to polynomial effective size. This regime corresponds to BQP. The computational horizon becomes transparent.

When $q$ is non-torsion (including the physical $q_0$), the Iwahori--Hecke algebra is semisimple ($\mathrm{Rad} = 0$). No paths are pruned. The full $3^c$ resolution tree survives. The computational horizon $\mathcal{H}_c(L, q_0) \neq \varnothing$ strictly blocks NP-complete links.

**Kummer persistence.** The Kummer filtration ([Kummer filtration](#rem:kummer-filtration-obstruction)) gives $\kappa_c^{\mathrm{comp}} \bmod n = 0$ if and only if $n \mid 6$. Since $q_0$ is non-torsion ($q_0^k \neq 1$ for all $k \geq 1$), no finite Kummer level applies. The obstruction is perpetual.

**Corollary (from the reduction theorem).** A resolution of P vs NP (in either direction) tightly constrains the other three millennium problems. Conversely, a resolution of RH, NS, or BSD constrains P vs NP. The evaluation maps differ, but the underlying obstruction class is identical.
