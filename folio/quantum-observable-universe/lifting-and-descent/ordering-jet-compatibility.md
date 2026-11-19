*Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with braiding-induced ordering $\prec_c$ on the Hecke basis of $A$ ([temporal braiding](#def:quantum-observable-universe), axiom 5). Let $A_0 = A \hookrightarrow A_1 \hookrightarrow A_2 \hookrightarrow \cdots$ be the recursive brane tower ([recursive brane tower](#def:recursive-brane-tower)), with $A_{n+1} = J^1(A_n)$ ([jet prolongation](#prop:jet-prolongation)). Then:*

1. **(Extension.)** *At each level $n$, the jet prolongation $\ell_n \colon A_n \hookrightarrow A_{n+1}$ induces an admissible ordering $\prec_{n+1}$ on the Hecke basis of $A_{n+1}$ that extends $\prec_n$:*
$$
  a \prec_n b \implies \ell_n(a) \prec_{n+1} \ell_n(b), \qquad a, b \in A_n.
$$

2. **(Compatibility with multiplication.)** *The ordering $\prec_{n+1}$ satisfies left and right compatibility. If $a \prec_{n+1} b$, then $c \cdot a \prec_{n+1} c \cdot b$ and $a \cdot d \prec_{n+1} b \cdot d$ for all $c, d \in A_{n+1}$ ([admissible system](#unital-groebner-bases:def:admissible-system)).*

3. **(Well-foundedness.)** *Each $\prec_n$ is well-founded. There are no infinite descending chains in the Hecke basis of $A_n$.*

4. **(Direct limit.)** *The direct limit algebra $\mathcal{A}_\infty = \varinjlim \mathrm{End}(A_n)$ ([direct limit algebra](#def:direct-limit-algebra)) carries a filtered admissible ordering $\prec_\infty = \bigcup_n \prec_n$. Every element $a \in \mathcal{A}_\infty$ has a well-defined leading monomial $\mathrm{LM}(a)$ with respect to $\prec_\infty$. The Gröbner--Shirshov reduction algorithm terminates on every element of $\mathcal{A}_\infty$ that belongs to a finite level $A_n$.*
