**Statement.**
*Let $\gamma \in H_n(q)$ be a degree-one element*

$$
  \gamma \;=\; 1 + \sum_{i=1}^{n-1} \phi_i\,\sigma_i,
$$

*and let $\beta_m \in H_n(q)$ be a state supported on the
$\lambda$-block of the
[Wedderburn--Artin decomposition](#prop:wedderburn-as-noncomm-fourier),
i.e. $\chi_\mu(\beta_m) = 0$ for $\mu \neq \lambda$. Under the
inclusion $H_n(q) \hookrightarrow H_{n+1}(q)$, the support of
$\gamma \cdot \beta_m$ is contained in the partitions obtained from
$\lambda$ by adding or removing a single box:*

$$
  \mathrm{supp}\bigl(\gamma \cdot \beta_m\bigr)
  \;\subseteq\;
  \{\lambda\} \;\cup\;
  \{\lambda + \square\} \;\cup\;
  \{\lambda - \square\},
$$

*where $\lambda \pm \square$ ranges over the addable / removable
corners of the Young diagram $\lambda$.*

**Proof sketch.**
Tensoring an irreducible Specht module $V_\lambda$ with the *fundamental
representation* $V_\square$ of $\mathrm{SU}_q(2)$ (equivalently, the
defining $(n-1)$-dimensional rep of $H_n(q)$) decomposes by the
**Pieri rule** for Hecke algebras:

$$
  V_\lambda \otimes V_\square
  \;\cong\;
  \bigoplus_{\mu = \lambda \pm \square} V_\mu,
$$

with multiplicity one for each addable/removable corner
[`fulton1997`, Ch. 2; `kassel1995`, Ch. XI]. Multiplication on the left
by a generator $\sigma_i$ realises the inclusion
$H_n(q) \hookrightarrow H_{n+1}(q)$ followed by braiding, which on
characters acts exactly as tensoring with $V_\square$. The identity term
$1$ in $\gamma$ contributes $V_\lambda$ unchanged. By
$\mathbb{C}$-linearity (Wedderburn--Artin), the support of $\gamma \beta_m$
is therefore contained in the union claimed.

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
