*Let $P$ be a confined particle and let $\mathcal{G} \subset \mathbb{R}_{>1}$ be the generic locus of the substrate parameter $q$. Write strict feasibility of the confinement SDP as a finite system of strict inequalities $0 < g_i(q, X)$, $i \in I$, in $q$ and the decision variable $X$, with each $g_i$ continuous. (Positive definiteness of a Gram matrix is such a system, by Sylvester's criterion on its leading principal minors.) The **confinement locus** of $P$ is*

$$
  \Omega(P) \;:=\; \{\, q : \exists X,\ \forall i \in I,\ 0 < g_i(q, X) \,\}.
$$

*Let $u^*_\lambda(q)$ be the dual variables of the SDP and $s_\lambda(q)$ the matching primal slacks. The **active support** is $\mathcal{S}^*(P, q) := \{\lambda : u^*_\lambda(q) > 0\}$ and the **binding multiplicity** is $\mu(P, q) := |\mathcal{S}^*(P, q)|$. Then:*

1. ***Openness.** $\Omega(P)$ is open.*
2. ***Constancy on a phase.** Let $C \subseteq \Omega(P)$ be connected. Suppose $u^*_\lambda$ and $s_\lambda$ are continuous in $q$, complementary ($u^*_\lambda s_\lambda = 0$) and strictly complementary ($u^*_\lambda > 0$ or $s_\lambda > 0$) at every $q \in C$. Then $\mathcal{S}^*(P, q)$ and $\mu(P, q)$ are constant on $C$.*

*The remaining structure of the phases (the boundary stratification, analyticity of the Frobenius stability index, scope and phase transitions) is stated separately as [conj:confinement-phase-boundaries](#conj:confinement-phase-boundaries).*

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: the locus is a subset of $\mathbb{R}$, and openness and connectedness are statements about the real topology.
