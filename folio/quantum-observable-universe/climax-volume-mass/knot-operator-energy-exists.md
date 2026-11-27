*For any partition $\lambda \vdash k$ with $k \leq k_{\max}$ and any $q$ in the generic locus $\{q \in R : [k]_q! \neq 0 \;\forall k \leq k_{\max}\}$, the [knot operator energy](#def:knot-operator-energy) $E(\lambda, q) = |u_\lambda(q)|$ exists as an element of the absolute-value image $|R|$ of the base ring.*

**Proof.** *The shadow price $u_\lambda(q) = w_\lambda(q)/d_\lambda(q) - 1/[k]_q! \in R$ is a rational function of $q$ with denominator $[k]_q! \cdot d_\lambda(q)$. Both factors are nonzero on the generic locus, since $[k]_q! \neq 0$ implies $[j]_q \neq 0$ for every hook length $j \leq k$ in the quantum hook-length formula for $d_\lambda(q)$. The absolute value $|\cdot|: R \to |R|$ is well-defined for:*

- *$R = \mathbb{R}$: archimedean $|\cdot|_\infty$, image $\mathbb{R}_{\geq 0}$;*
- *$R = \mathbb{Q}_p$: $p$-adic $|\cdot|_p$, image $\{p^{-n}\} \cup \{0\}$;*
- *$R = \mathbb{F}_p$: the only absolute value is the trivial one, so there is no archimedean place. The energy filtration is undefined and confinement falls back to ILP feasibility ([stable atom](#def:stable-atom)).*

*In each archimedean or non-archimedean case, $E(\lambda, q)$ exists and is uniquely determined by $\lambda$ and $q$.*
