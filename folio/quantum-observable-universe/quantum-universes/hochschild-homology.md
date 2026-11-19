Let $A$ be an associative algebra over a commutative ring $R$, and write $A^{e} = A \otimes_R A^{\mathrm{op}}$ for its enveloping algebra, so that a bimodule over $A$ is the same thing as a left module over $A^{e}$; $A$ itself is one.

The **:defterm[Hochschild homology]{#hochschild-homology}** of $A$ is the graded $R$-module

$$
  HH_{n}(A) \;=\; \operatorname{Tor}^{A^{e}}_{n}(A, A), \qquad n \geq 0 .
$$

It is computed by the *Hochschild complex* $C_{n}(A) = A^{\otimes (n+1)}$ with the boundary

$$
  b(a_0 \otimes a_1 \otimes \cdots \otimes a_n)
  = \sum_{i=0}^{n-1} (-1)^{i}\, a_0 \otimes \cdots \otimes a_i a_{i+1} \otimes \cdots \otimes a_n
  \;+\; (-1)^{n}\, a_n a_0 \otimes a_1 \otimes \cdots \otimes a_{n-1}.
$$

In degree zero, $HH_{0}(A) = A / [A, A]$, the quotient of $A$ by the $R$-span of all commutators $ab - ba$; this is the *cocenter* of $A$.

For an $A$-bimodule $M$, the **Hochschild cohomology** of $A$ with values in $M$ is $HH^{n}(A, M) = \operatorname{Ext}^{n}_{A^{e}}(A, M)$, and $HH^{n}(A) := HH^{n}(A, A)$.

For an $R$-linear category $\mathbf{C}$, the same construction with the objects of $\mathbf{C}$ in place of the single algebra gives the Hochschild homology of $\mathbf{C}$; its degree-zero group $HH_{0}(\mathbf{C})$ is the direct sum over objects $X$ of $\operatorname{End}(X)$, modulo the relations $fg = gf$ for every pair of morphisms $f \colon X \to Y$, $g \colon Y \to X$.
