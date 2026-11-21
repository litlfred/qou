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

**Support convention.** The element $\gamma \beta_m$ is of mixed
degree: the identity term of $\gamma$ and the terms built from $\sigma_i$ with
$i \leq n - 1$ leave $\beta_m$ at level $n$ of the tower, while a
$\sigma_n$ term, read in $H_{n+1}(q)$, couples one further strand and
lands at level $n + 1$. Support is therefore tracked in the
Wedderburn labels of the tower algebra $\bigoplus_m H_m(q)$, one
label set per level. At level $n + 1$ write
$\lambda + \square := (\lambda_1 + 1, \lambda_2) \vdash n+1$ and
$\lambda - \square := (\lambda_1, \lambda_2 + 1) \vdash n+1$; the
name of the latter comes from the two-row $\mathrm{SU}_q(2)$
identification, under which a complete two-box column carries the
trivial determinant weight and $(\lambda_1, \lambda_2 + 1)$
column-reduces to $(\lambda_1 - 1, \lambda_2)$. All partitions in a
given support statement below live at the level indicated.

**Step 1: reduction by linearity.**
Write the photon as $\gamma = \mathbf{1} + \varphi_0\sigma_a + \varphi_1\sigma_b + \varphi_{01}\,\sigma_a\sigma_b^{-1}$ on consecutive generators $a, b = a + 1$ ([photon](#def:photon)). Then $\gamma \beta_m = \beta_m + \varphi_0\,\sigma_a\beta_m + \varphi_1\,\sigma_b\beta_m + \varphi_{01}\,\sigma_a\sigma_b^{-1}\beta_m$. Since $\mathrm{supp}(x + y) \subseteq \mathrm{supp}(x) \cup \mathrm{supp}(y)$, it suffices to bound the support of each summand. The identity term contributes the level-$n$ component $\mathrm{supp}(\beta_m) = \{\lambda\}$, unchanged.

If $b \leq n - 1$, every term lies in $H_n(q)$. The vertex term is included because $\sigma_b^{-1} = \sigma_b - h$. Every term then commutes with the central idempotent $e_\lambda$. Since $\beta_m = e_\lambda \beta_m$, also $\gamma\beta_m = e_\lambda \gamma \beta_m$. For the four-term photon the step reads: anything that commutes with $\sigma_a$ and the unit $\sigma_b$ commutes with $\gamma(\varphi)$.

If $b = n$, the terms containing $\sigma_n$ lie in $H_{n+1}(q)$ and act on the module induced from $V_\lambda$. Its isotypic components are the $\lambda + \square$ and $\lambda - \square$ of the support convention, and every element of $H_{n+1}(q)$, the vertex term included, preserves that decomposition. This is the claimed containment. $\blacksquare$

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
