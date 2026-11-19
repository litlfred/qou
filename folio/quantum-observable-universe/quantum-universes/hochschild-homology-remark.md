**The cyclic term.** The last term of the Hochschild boundary $b$ wraps the tensor around: it is the cyclic structure of the complex, and the reason its homology deserves the name of a trace.

**Degree two of cohomology.** The group $HH^{2}(A, M)$ classifies first-order deformations of the multiplication of $A$ with values in $M$ \cite{weibel1994}.

**Degree zero.** A linear functional $\tau \colon A \to R$ with $\tau(ab) = \tau(ba)$ vanishes on $[A, A]$ and therefore factors through $HH_{0}(A)$. Every trace in this paper — the rigid trace of an endomorphism, the Markov trace on the Hecke algebra, a character of a representation — is a functional of this kind, and every one of them is a function of the Hochschild class alone. This is the whole reason the paper's traces live in degree zero, and it is the part of the definition that the Lean formalisation carries: the cocenter, the identity $[ab] = [ba]$, and the factorisation of traces through it.

**Degree one.** For $A$ commutative, $HH_{1}(A) = \Omega^{1}_{A/R}$, the module of Kähler differentials: the class of $a_0 \otimes a_1$ goes to $a_0\, da_1$. For $A$ smooth over a field of characteristic zero the pattern continues in every degree, $HH_{n}(A) \cong \Omega^{n}_{A/R}$; that is the Hochschild–Kostant–Rosenberg theorem, stated with its hypotheses in a later chapter. For a noncommutative $A$, such as the quantised coordinate ring of a group at $q \neq 1$, no such identification is available, and the groups have to be computed \cite{loday-1998}.

**Algebra and category.** It is the Hochschild homology $HH_{0}(\mathbf{C})$ of the category, not that of a single algebra, that receives the [Chern character](#def:chern-character).
