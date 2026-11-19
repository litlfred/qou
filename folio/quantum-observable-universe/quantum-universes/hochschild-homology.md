Let $A$ be an associative algebra over a commutative ring $R$, and write $A^{e} = A \otimes_R A^{\mathrm{op}}$ for its enveloping algebra, so that a bimodule over $A$ is the same thing as a left module over $A^{e}$; $A$ itself is one.

**Definition.** The **:defterm[Hochschild homology]{#hochschild-homology}** of $A$ is the graded $R$-module

$$
  HH_{n}(A) \;=\; \operatorname{Tor}^{A^{e}}_{n}(A, A), \qquad n \geq 0 .
$$

It is computed by the Hochschild complex $C_{n}(A) = A^{\otimes (n+1)}$ with the boundary

$$
  b(a_0 \otimes a_1 \otimes \cdots \otimes a_n)
  = \sum_{i=0}^{n-1} (-1)^{i}\, a_0 \otimes \cdots \otimes a_i a_{i+1} \otimes \cdots \otimes a_n
  \;+\; (-1)^{n}\, a_n a_0 \otimes a_1 \otimes \cdots \otimes a_{n-1},
$$

whose last term wraps the tensor around: it is the cyclic structure of the complex, and the reason its homology carries universal traces. The companion groups $HH^{n}(A, M) = \operatorname{Ext}^{n}_{A^{e}}(A, M)$, for a bimodule $M$, are the Hochschild cohomology; $HH^{n}(A) := HH^{n}(A, A)$, and $HH^{2}(A, M)$ classifies first-order deformations of the multiplication of $A$ with values in $M$ \cite{weibel1994}.

**Degree zero.** From the complex, $HH_{0}(A) = A / [A, A]$, the quotient of $A$ by the $R$-span of all commutators $ab - ba$; this is the *cocenter* of $A$. In the cocenter the class identity $[ab] = [ba]$ holds by construction, so every $R$-linear functional $\tau \colon A \to R$ satisfying $\tau(ab) = \tau(ba)$ vanishes on $[A, A]$ and factors uniquely through $HH_{0}(A)$. Every cyclic trace in this monograph — the categorical trace of an endomorphism, a Markov trace on a braid quotient, or a character of a representation — is a functional of this form and depends only on the degree-zero Hochschild class.

**Degree one.** For $A$ commutative, $HH_{1}(A) = \Omega^{1}_{A/R}$, the module of Kähler differentials: the class of $a_0 \otimes a_1$ maps to $a_0\, da_1$. For $A$ smooth over a field of characteristic zero the pattern continues in every degree, $HH_{n}(A) \cong \Omega^{n}_{A/R}$, by the Hochschild--Kostant--Rosenberg theorem. For a noncommutative algebra $A$, no such commutative identification holds in general, and the homology groups must be computed directly from the bar resolution \cite{loday-1998}.

**Two conventions to keep apart.** The definition above is for a single algebra. For an $R$-linear category $\mathbf{C}$ the same construction, with the objects of $\mathbf{C}$ in place of a single algebra, gives the Hochschild homology of the category; in degree zero it is the direct sum over objects $X$ of $\operatorname{End}_{\mathbf{C}}(X)$, modulo the commutator relations $fg = gf$ for every pair of morphisms $f \colon X \to Y$ and $g \colon Y \to X$. This categorical cocenter, written $HH_{0}(\mathbf{C})$, is the target of the Chern character defined below.
