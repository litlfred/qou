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

whose last term wraps the tensor around: it is the cyclic structure of the complex, and the reason its homology deserves the name of a trace. The companion groups $HH^{n}(A, M) = \operatorname{Ext}^{n}_{A^{e}}(A, M)$, for a bimodule $M$, are the Hochschild cohomology; $HH^{n}(A) := HH^{n}(A, A)$, and it is $HH^{2}(A, M)$ that classifies first-order deformations of the multiplication of $A$ with values in $M$ \cite{weibel1994}.

**Degree zero.** From the complex, $HH_{0}(A) = A / [A, A]$, the quotient of $A$ by the $R$-span of all commutators $ab - ba$; this is the *cocenter* of $A$. A linear functional $\tau \colon A \to R$ with $\tau(ab) = \tau(ba)$ vanishes on $[A, A]$ and therefore factors through $HH_{0}(A)$. Every trace in this paper — the rigid trace of an endomorphism, the Markov trace on the Hecke algebra, a character of a representation — is a functional of this kind, and every one of them is a function of the Hochschild class alone. This is the whole reason the paper's traces live in degree zero: the cocenter $HH_0(A)$, the identity $[ab] = [ba]$ in it, and the factorisation of every trace through it are all the definition needs.

**Degree one.** For $A$ commutative, $HH_{1}(A) = \Omega^{1}_{A/R}$, the module of Kähler differentials: the class of $a_0 \otimes a_1$ goes to $a_0\, da_1$. For $A$ smooth over a field of characteristic zero the pattern continues in every degree, $HH_{n}(A) \cong \Omega^{n}_{A/R}$; that is the Hochschild–Kostant–Rosenberg theorem, stated with its hypotheses in a later chapter. For a noncommutative $A$, such as the quantised coordinate ring of a group at $q \neq 1$, no such identification is available, and the groups have to be computed \cite{loday-1998}.

**Two conventions to keep apart.** The definition above is for an algebra. For an $R$-linear category $\mathbf{C}$ the same construction, with the objects of $\mathbf{C}$ in place of the single algebra, gives the Hochschild homology of the category; in degree zero it is the direct sum over objects $X$ of $\operatorname{End}(X)$, modulo the relations $fg = gf$ for every pair of morphisms $f \colon X \to Y$, $g \colon Y \to X$. It is this second object, written $HH_{0}(\mathbf{C})$, that receives the Chern character of the next definitions.
