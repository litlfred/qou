With the substrate parameter $q$ in hand, the remark in the [quantum universe](#def:quantum-universe) definition — that a ground ring limits which block decompositions it can carry — becomes concrete. The invertibility clauses of axiom 4 are quantified over the universe's own blocks, so they constrain the pair $(R, \mathbf{C})$ and not $R$ alone.

That limit is real. In $\mathbb{Z}[q, q^{-1}]$ the units are exactly $\pm q^{k}$, while each quantum integer is a monomial times a product of cyclotomic polynomials $\Phi_d$ of positive degree — $[2]_q = q^{-1}\Phi_4(q)$, $[3]_q = q^{-2}\Phi_3\Phi_6$, $[4]_q = q^{-3}\Phi_4\Phi_8$. No $[m]_q$ with $m \geq 2$ is a unit there, so over that ring the block index collapses to the trivial block: the axioms are satisfiable, but only degenerately, and none of the Hecke decompositions of the later chapters fit. Inverting the cyclotomics is what makes a non-degenerate universe available:

$$
  R \;=\; \mathbb{Z}[q, q^{-1}]\bigl[\, \Phi_d(q)^{-1} \;:\; d \geq 2 \,\bigr],
$$

whose spectrum is the $q$-line with the roots of unity of order $\geq 2$ removed. Starting at $d = 1$ would additionally delete $q = 1$, which the classical limit needs, and nothing requires it: $q^{n} - 1 = (q-1)\,[n]_q$, so $q^n - 1$ is a unit exactly when $q - 1$ is, and the constructs inverting $q - 1$ live past the archimedean wall.

**This is a choice of instance, not a strengthening of the definition.** Call a pair $(R, q)$ *$q$-generic* when $q$ and every $\Phi_d(q)$, $d \geq 2$, are invertible in $R$. The property belongs to the *construction* of a Hecke-type universe, where it is what makes the axiom-4 invertibility conditions hold. It is deliberately not a hypothesis of the quantum-universe definition, which asks only for a commutative ring. The ring above is the initial $q$-generic ring, so any other base with the property — $\mathbb{Q}(q)$, a real algebra at the substrate anchor, a neighbouring convention's Laurent ring — receives a unique map *from* it and inherits the construction. The map runs outward; no universe is asked to embed in this ring, and injectivity is never required — the evaluation at $q = 1$ is not injective, and must not be.
