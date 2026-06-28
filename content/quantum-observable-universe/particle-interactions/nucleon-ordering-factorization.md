The Wedderburn--Artin decomposition of $H_3(q)$ into irreducible
representations, combined with jet-descended confinement of hadrons,
yields a factorization of the nuclear Markov trace that makes the
ground-state ordering search trivial in two of three channels.

## Statement

**Proposition.**
*Let $\mathcal{N}(Z, N)$ be a nuclear braid in $H_A(q)$ with
nucleon ordering $\pi = (t_1, \ldots, t_A)$ where
$t_k \in \{\mathfrak{p}, \mathfrak{n}\}$.  Then the Markov trace
decomposes as:*

$$
  \mathrm{tr}_M(\mathcal{N})
  =
  W_{\mathrm{sym}} \cdot S(\pi)
  + W_{\mathrm{std}} \cdot (z \cdot a_\pi + b_\pi)
  + W_{\mathrm{alt}} \cdot A(\pi)
$$

*where:*

**(i) Ordering independence of scalar channels.**
*The symmetric product $S(\pi) = \prod_k s_k$ and alternating
product $A(\pi) = \prod_k a_k$ are products of commutative
scalars.  Since scalar multiplication commutes, $S$ and $A$ are
independent of the nucleon ordering $\pi$:*

$$
  S(\pi) = S(\pi') = \prod_{k} (q + d_k),
  \qquad
  A(\pi) = A(\pi') = \prod_{k} (-q^{-1} + d_k)
$$

*for any two orderings $\pi, \pi'$ with the same nucleon
composition $(Z, N)$.*

**(ii) Standard-channel factorization.**
*The standard-channel state $(a_\pi, b_\pi) \in \mathbb{R}^2$
is the result of a $2 \times 2$ matrix product:*

$$
  \begin{pmatrix} a_\pi \\ b_\pi \end{pmatrix}
  =
  \left(\prod_{k=1}^{K} \sigma_k^{\mathrm{std}}\right)
  \begin{pmatrix} 0 \\ 1 \end{pmatrix},
  \qquad
  \sigma_k^{\mathrm{std}}(c, d)
  =
  \begin{pmatrix}
    c(q - q^{-1}) + d & c \\
    c & d
  \end{pmatrix}
$$

*where $K$ is the total number of crossings (nucleon-internal
$+$ inter-nucleon $+$ electron).*

**(iii) Jet-descended nucleon blocks.**
*By the confinement theorem
([confinement-topological](#prop:confinement-topological)),
proton and neutron are topologically stable normal forms in
$H_3(q)$.  By the ordering-jet compatibility theorem
([ordering-jet-compatibility](#prop:ordering-jet-compatibility)),
the admissible ordering propagates through jet levels.  This
means the intra-nucleon crossings
($\mathcal{B}_3$ $+$ quark pairs $+$ gluon dressing) produce
fixed $2 \times 2$ transfer matrices:*

$$
  T_\mathfrak{p}^{\mathrm{std}}
  =
  \prod_{i=1}^{n_p}
  \sigma_i^{\mathrm{std}}(c_i, d_i)
  \in \mathbb{R}^{2 \times 2},
  \qquad
  T_\mathfrak{n}^{\mathrm{std}}
  =
  \prod_{j=1}^{n_n}
  \sigma_j^{\mathrm{std}}(c_j, d_j)
  \in \mathbb{R}^{2 \times 2}
$$

*These are precomputed once and reused for every nucleus.*

**(iv) Inter-nucleon crossings (transient).**
*In the jet-stratified language
([jet-stratified-reduction](#unital-groebner-bases:prop:jet-stratified-reduction)),
the nucleon blocks are **descended** (resolved at the quark level).
The inter-nucleon crossings are **transient** (new at the nuclear
level).  Each has a $2 \times 2$ matrix determined by the nucleon
pair type:*

$$
  T_{\mathfrak{p}\mathfrak{p}}^{\mathrm{std}}
  =
  \begin{pmatrix} q - q^{-1} & 1 \\ 1 & 0 \end{pmatrix},
  \quad
  T_{\mathfrak{n}\mathfrak{n}}^{\mathrm{std}}
  =
  \begin{pmatrix} 0 & 1 \\ 1 & -(q - q^{-1}) \end{pmatrix},
  \quad
  T_{\mathfrak{p}\mathfrak{n}}^{\mathrm{std}}
  =
  \begin{pmatrix}
    \tfrac{1}{2}(q - q^{-1}) & 1 \\
    1 & -\tfrac{1}{2}(q - q^{-1})
  \end{pmatrix}
$$
