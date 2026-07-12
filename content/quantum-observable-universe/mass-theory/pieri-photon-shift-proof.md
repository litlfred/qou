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

**Step 1: reduction by linearity.**
Since $\gamma \beta_m = \beta_m + \sum_i \phi_i \, (\sigma_i \beta_m)$
and $\mathrm{supp}(x + y) \subseteq \mathrm{supp}(x) \cup \mathrm{supp}(y)$,
it suffices to bound the support of each summand. The identity term
contributes $\mathrm{supp}(\beta_m) = \{\lambda\}$, unchanged. It
remains to show
$\mathrm{supp}(\sigma_i \beta_m) \subseteq \{\lambda + \square\} \cup \{\lambda - \square\}$
for each generator term.

**Step 2: a single crossing couples one fundamental factor.**
Each generator term couples the degree-one strand to the state
through exactly one crossing $\sigma_i$. In the Schur–Weyl picture
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
(\cite{fulton1997}, Ch. 2; \cite{kassel1995}, Ch. VII). In the
two-row spectrum of $\mathrm{SU}_q(2)$ a complete column of two
boxes carries the trivial determinant weight, so adding a box in
the second row is equivalent to removing a box from the first: the
two summands are precisely $\lambda + \square$ and
$\lambda - \square$ (when $\lambda - \square$ is a valid shape;
otherwise only $\lambda + \square$ occurs, and the containment
below holds a fortiori). Hence
$\mathrm{supp}(\sigma_i \beta_m) \subseteq \{\lambda + \square\} \cup \{\lambda - \square\}$.

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
seminormal basis and the inclusion basis); we do not compute them
here. For the purposes of the QOU mass-formula pipeline, only the
support statement is used: it bounds the spectral spread induced by a
single photon coupling to one box.

**Relation to the volume vanishing.** The
[degree-one volume lemma](#lem:degree-one-braid-trivial-volume) says
$\tau_{\mathrm{arch}}(\gamma) = 0$. The Pieri shift is the
*representation-theoretic* counterpart: it tracks how $\gamma$ moves
the Wedderburn support without itself contributing to the archimedean
volume of $\overline{\gamma}$.
