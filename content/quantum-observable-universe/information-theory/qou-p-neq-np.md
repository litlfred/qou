**Conjecture.** At the physical non-torsion substrate parameter $q_0 \in \mathbb{G}_m^{\mathrm{nt}}(\mathbb{R})$, we have $\mathrm{P} \neq \mathrm{NP}$. Equivalently, the resolution-tree evaluation of the universal obstruction class $\chi(A)$ is non-vanishing:
$$
  \mathrm{res}_{\mathcal{R}}\!\bigl(\chi(A)\bigr)  \neq  0 \qquad\text{at } q = q_0.
$$

**The fourth millennium evaluation.** The QOU obstruction reduction establishes that all classical-limit obstructions map to the scalar class $\chi(A) \in HH^2 \cong k$. Consequently, $\mathrm{P}$ vs $\mathrm{NP}$ acts as a fourth restriction of the same class alongside RH, NS, and BSD. All four evaluations are structurally proportional.

**The $\mathbb{G}_m$-torsion dichotomy.** When $q$ is a torsion root of unity, the Iwahori--Hecke algebra acquires a non-trivial radical. This radical annihilates exponentially many resolution paths, pruning the tree to polynomial effective size. This regime corresponds exactly to BQP, rendering the computational horizon transparent. Conversely, at non-torsion values like $q_0$, the algebra remains semisimple. No paths vanish; the full $3^c$ resolution tree survives. The computational horizon $\mathcal{H}_c(L, q_0) \neq \varnothing$ therefore strictly blocks NP-complete links.

**Kummer persistence.** The Kummer filtration yields $\kappa_c^{\mathrm{comp}} \bmod n = 0$ if and only if $n \mid 6$. Because $q_0$ is strictly non-torsion, no finite Kummer level applies. The obstruction remains perpetual.

**Corollary.** Resolving $\mathrm{P}$ vs $\mathrm{NP}$ strictly constrains RH, NS, and BSD, and vice versa. Although their evaluation maps differ, the underlying obstruction class remains identical.

**Parallel route.** This obstruction-class formulation (non-vanishing of $\mathrm{res}_{\mathcal{R}}(\chi(A))$ at non-torsion $q_0$) is one of two independent attacks on the same separation. The Reeb--surreal route ([P vs NP in the QOU](#conj:p-vs-np-qou)) instead recovers $\mathrm{P} \neq \mathrm{NP}$ as the standard part of a strict $\mathbf{P} \subsetneq \mathrm{BQP}_q$ inclusion, via the surreal squeeze $\mathrm{ord}_\omega(\text{cost}) > \mathrm{ord}_\omega(\text{budget})$. The two carriers agree on the conclusion but neither is derived from the other; both remain open.
