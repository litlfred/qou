**Proof.**
Write the degree-one element as
$\gamma = 1 + \sum_{i=1}^{n-1} \phi_i \, \sigma_i$ with scalar
coefficients $\phi_i$
([degree-one volume lemma](#lem:degree-one-braid-trivial-volume)),
and let $\beta_m$ be supported purely on the $\lambda$-block. Here
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
degree: the identity term of $\gamma$ and the generator terms $\sigma_i$ with
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
Since $\gamma \beta_m = \beta_m + \sum_i \phi_i \, (\sigma_i \beta_m)$
and $\mathrm{supp}(x + y) \subseteq \mathrm{supp}(x) \cup \mathrm{supp}(y)$,
it suffices to bound the support of each summand. The identity term
contributes the level-$n$ component $\mathrm{supp}(\beta_m) = \{\lambda\}$,
unchanged. A generator $\sigma_i$ with $i \leq n - 1$ lies in $H_n(q)$
and commutes with the central idempotent $e_\lambda$; since
$\beta_m = e_\lambda \beta_m$, also $\sigma_i \beta_m = e_\lambda \sigma_i \beta_m$,
so these terms stay at level $n$ with support in $\{\lambda\}$. For
$\gamma$ as written, with the sum running to $i = n - 1$, this already
gives the containment. Only a term in $\sigma_n$, which adds a strand and
is present when $\gamma$ is taken in $H_{n+1}(q)$, can leave level $n$.
It remains to show, at level $n+1$,
$\mathrm{supp}(\sigma_n \beta_m) \subseteq \{\lambda + \square\} \cup \{\lambda - \square\}$.

**Step 2: a single crossing couples one fundamental factor.**
The $\sigma_n$ term couples the degree-one strand to the state
through exactly one crossing. In the Schur–Weyl picture
the coupled object lives in

$$
  V_\lambda \otimes V_\square,
$$

the isotypic component of the state tensored with the fundamental
representation carried by the coupled strand. The crossing acts by
the braiding, which is a morphism of $\mathrm{SU}_q(2)$-modules
(the Hecke action commutes with the quantum-group action), so it
preserves the isotypic decomposition of $V_\lambda \otimes V_\square$:
the support after coupling is contained in the set of $\mu$ for
which $V_\mu$ appears in $V_\lambda \otimes V_\square$.

**Step 3: the Pieri rule.**
The quantum Clebsch–Gordan rule for $\mathrm{SU}_q(2)$ at generic
$q$ — the one-box case of the Pieri rule — decomposes

$$
  V_\lambda \otimes V_\square
  \;\cong\;
  \bigoplus_{\mu = \lambda \pm \square} V_\mu,
$$

with multiplicity one for each summand
(\cite{fulton1997}, Ch. 2; \cite{kassel1995}, Ch. VII). The two
summands are the two level-$(n+1)$ blocks
$\lambda + \square = (\lambda_1 + 1, \lambda_2)$ and
$\lambda - \square = (\lambda_1, \lambda_2 + 1)$ of the support
convention (when $(\lambda_1, \lambda_2 + 1)$ is a valid two-row
shape; otherwise only $\lambda + \square$ occurs, and the
containment below holds a fortiori). Hence
$\mathrm{supp}(\sigma_n \beta_m) \subseteq \{\lambda + \square\} \cup \{\lambda - \square\}$
at level $n+1$.

**Step 4: assembly.**
Combining Steps 1–3,

$$
  \mathrm{supp}\bigl(\gamma \cdot \beta_m\bigr)
  \;\subseteq\;
  \{\lambda\} \;\cup\; \{\lambda + \square\} \;\cup\; \{\lambda - \square\},
$$

which is the claimed containment. $\blacksquare$

**Scope.**
The proposition gives a *containment* of supports, not equality. The
actual coefficients are dictated by the $\phi_i$ and the Hecke-algebra
6j-symbols (matrix elements of the basis change between the
seminormal basis and the inclusion basis) and are not computed
here. For the purposes of the QOU mass-formula pipeline, only the
support statement is used: it bounds the spectral spread induced by a
single photon coupling to one box.

**Relation to the volume vanishing.** The
[degree-one volume lemma](#lem:degree-one-braid-trivial-volume) says
every braid word in the support of $\gamma$ has volume $0$. The Pieri shift is the
*representation-theoretic* counterpart: it tracks how $\gamma$ moves
the Wedderburn support without itself contributing to the archimedean
volume of $\overline{\gamma}$.
