**Proof.**
Let $\gamma = \gamma(\varphi)$ be a [photon](#def:photon). Its
degree-one specialisation $\varphi_{01} = 0$ is the element of the
[degree-one volume lemma](#lem:degree-one-braid-trivial-volume).
Let $\beta_m$ be supported purely on the $\lambda$-block. Here
the *support* $\mathrm{supp}(x)$ of an element is the set of labels
in the Young lattice indexing the isotypic components on which $x$
has a non-zero component, read through Schur–Weyl duality: at
generic $q$, the Hecke algebra $H_n(q)$ and $\mathrm{SU}_q(2)$
generate each other's commutant on $V_\square^{\otimes n}$, where
$V_\square$ is the two-dimensional fundamental representation, and
the simple module $V_\lambda$ is matched with the
$\lambda$-isotypic component of the $\mathrm{SU}_q(2)$ action
\cite{kassel1995}. The hypothesis on $\beta_m$ says its image lies
in the $V_\lambda$-isotypic component.

**Step 1: reduction by linearity.**
Write $\gamma\beta_m = \beta_m + \varphi_0\,\sigma_a\beta_m + \varphi_1\,\sigma_b\beta_m + \varphi_{01}\,\sigma_a\sigma_b^{-1}\beta_m$. Since $\mathrm{supp}(x + y) \subseteq \mathrm{supp}(x) \cup \mathrm{supp}(y)$, it suffices to bound the support of each summand.

**Case $b \leq n - 1$.** Every term lies in $H_n(q)$; the vertex term does too, because $\sigma_b^{-1} = \sigma_b - h$ with $h = q - q^{-1}$. The central idempotent $e_\lambda$ of $H_n(q)$ commutes with every element, and $\beta_m = e_\lambda \beta_m$, so $\gamma\beta_m = \gamma e_\lambda \beta_m = e_\lambda\gamma\beta_m$. Hence $\mathrm{supp}(\gamma\beta_m) \subseteq \{\lambda\}$.

**Case $b = n$.** All four terms lie in $H_{n+1}(q) \supset H_n(q)$. Let $e_\mu$, $\mu \vdash n + 1$, be the central idempotents of $H_{n+1}(q)$. By the branching rule for $H_n(q) \subset H_{n+1}(q)$ at generic $q$ (the same as for $S_n \subset S_{n+1}$), $e_\mu e_\lambda = 0$ unless $\mu \supset \lambda$. For any $x \in H_{n+1}(q)$,

$$
  e_\mu\, x\, \beta_m \;=\; x\, e_\mu\, e_\lambda\, \beta_m ,
$$

since $e_\mu$ is central. So $e_\mu \gamma \beta_m = 0$ unless $\mu \supset \lambda$. The partitions $\mu \vdash n + 1$ with $\mu \supset \lambda$ are $(\lambda_1 + 1, \lambda_2)$, $(\lambda_1, \lambda_2 + 1)$ when $\lambda_2 < \lambda_1$, and $(\lambda_1, \lambda_2, 1)$. By Schur–Weyl duality for $\mathrm{SU}_q(2)$ \cite{kassel1995}, $H_{n+1}(q)$ acts on $V_\square^{\otimes(n+1)}$ through its two-row quotient, so the three-row component acts by zero there. This gives the stated containment. $\blacksquare$

**Scope.**
The proposition gives a *containment* of supports, not equality. The
actual coefficients are dictated by the $\phi_i$ and the Hecke-algebra
6j-symbols (matrix elements of the basis change between the
seminormal basis and the inclusion basis); they are not computed
here. For the purposes of the QOU mass-formula pipeline, only the
support statement is used: it bounds the spectral spread induced by a
single photon coupling to one box.

**Relation to the volume vanishing.** The
[degree-one volume lemma](#lem:degree-one-braid-trivial-volume) says
every braid word in the support of $\gamma$ has volume $0$. The Pieri shift is the
*representation-theoretic* counterpart: it tracks how $\gamma$ moves
the Wedderburn support without itself contributing to the archimedean
volume of $\overline{\gamma}$.
