Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $\mathbf{C} = \mathrm{Rep}(\mathrm{SU}_q(2))$ and $V$ the fundamental representation. Assume $q$ is not a root of unity.

1. **Semisimplicity.** The Iwahori--Hecke algebra $H_n(R, q)$ is semisimple. It acts on $V^{\otimes n}$ through its Temperley--Lieb quotient, $H_n(R, q) \twoheadrightarrow \mathrm{TL}_n(q) \cong \mathrm{End}_{\mathrm{SU}_q(2)}(V^{\otimes n})$, and $V^{\otimes n}$ decomposes completely into irreducible $H_n(R, q)$-modules:

   $$
     V^{\otimes n}
      \cong 
     \bigoplus_{\lambda \vdash n}
     V_\lambda \otimes S_\lambda.
   $$

   Here, $\lambda$ ranges over partitions of $n$ with at most two parts. $V_\lambda$ is the irreducible $\mathrm{SU}_q(2)$-module of spin $j = (\lambda_1 - \lambda_2)/2$, and $S_\lambda$ is the irreducible $H_n(R, q)$-module labelled by $\lambda$.

2. **Alexander surjectivity.** By Alexander's theorem, every oriented link $L$ in $S^3$ is the closure $\hat{\beta}$ of some braid $\beta \in B_n$. The Markov trace assigns the value $\mathrm{tr}_M(\rho_n(\beta))$ to each braid closure, recovering the Jones polynomial $J_L(q)$ up to framing. Every irreducible summand $S_\lambda$ ($\ell(\lambda) \leq 2$) is detected by some braid closure: its component $y_\lambda \chi_\lambda(\rho_n(\beta))$ in $\mathrm{tr}_M(\rho_n(\beta))$ is non-zero for some $\beta \in B_n$. The summands are labelled by partitions, not by knot types: many knots give the same summand, and one closure generally meets several summands.

3. **Algebraic spanning.** The physical state space is the algebraic direct limit $V_{\mathrm{phys}} := \varinjlim V^{\otimes n}$ under the inclusions $\iota_n \colon V^{\otimes n} \to V^{\otimes (n+1)}$, $x \mapsto x \otimes v_0$, for a fixed nonzero $v_0 \in V$. Each $\iota_n$ intertwines the action of $H_n(R, q)$ with its restriction from $H_{n+1}(R, q)$ along $H_n \subset H_{n+1}$; it is not $\mathrm{SU}_q(2)$-equivariant, and no equivariant inclusion exists because $\mathrm{Hom}(\mathbf{1}, V) = 0$. Because each $V^{\otimes n}$ is completely decomposed, the set of irreducible summands, labelled by the partitions $\lambda$ with $\ell(\lambda) \leq 2$, spans $V_{\mathrm{phys}}$ without requiring metric completion.

A reading of this decomposition as a knot-type eigenbasis is given in [rem:knot-eigenbasis-complete-reading](#rem:knot-eigenbasis-complete-reading).
