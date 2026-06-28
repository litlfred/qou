## Locality from flatness of the KZ connection

The [lifted-crossing locality](#conj:lifted-crossing-locality)
hypothesis reduces to a statement about the **holonomy of the
Knizhnik-Zamolodchikov connection** at generic $q$.  The physical
content: cross-talk between two lifted crossings measures the
curvature of a flat connection on a punctured surface, and
flatness implies factorization.

## Setup — the KZ connection

Let $X_n := \{(w_1, \ldots, w_n) \in \mathbb{C}^n : w_i \neq w_j\}$
be the configuration space of $n$ distinct complex points.  The
(quantum) KZ connection on $X_n$ with values in
$V^{\otimes n}$ (for $V$ a $U_q(\mathfrak{sl}_2)$-module) is

$$
  \nabla \;=\; d \;-\; \frac{\hbar_q}{2 \pi i}
  \sum_{i < j} \Omega_{ij}\,\frac{dw_i - dw_j}{w_i - w_j},
$$

where $\Omega_{ij}$ is the Casimir element acting on factors
$i, j$ of $V^{\otimes n}$.

By the Kohno-Drinfeld theorem \cite{kohno1987}, the KZ connection is
flat:
$$
  [\nabla_i, \nabla_j] \;=\; 0
  \quad\Longleftrightarrow\quad
  [\Omega_{ij}, \Omega_{kl}] = 0 \text{ for disjoint pairs,}
  \text{ and infinitesimal braid relations.}
$$
Moreover the monodromy representation of $\pi_1(X_n / S_n) = B_n$
on $V^{\otimes n}$ coincides with the quantum-group R-matrix
representation of $U_q(\mathfrak{sl}_2)$.

## Applying to the mass endomorphism

Model each crossing $c$ of an atomic braid as a puncture in the
configuration space $X_n$.  A lifted crossing inserts a
**quantum-dilogarithm operator** $\Phi_q(z_c)$ at that puncture;
an unlifted crossing inserts the identity.

The mass contribution of a configuration with lifted subset
$S \subseteq \mathrm{Cr}(\mathcal{K})$ is the trace of the resulting
braid-word operator, which is computed by parallel transport along
the closure of the braid word in $X_n / S_n$.

The locality hypothesis is, in this language, the statement that at
generic $q$ the parallel transport factorizes over disjoint punctures:
$$
  \mathrm{Tr}\!\left[
    \prod_{c \in S} \Phi_q(z_c) \cdot \rho(\beta)
  \right]
  \;=\;
  \mathrm{Tr}[\rho(\beta)] \cdot \prod_{c \in S}
  \eta(c),
$$
where $\eta(c)$ is the single-crossing expectation value.

The factorization is read off from flatness as follows:
1. By flatness (Kohno-Drinfeld), any two closed loops
   $\gamma_i, \gamma_j$ encircling separated subsets
   $S_i, S_j \subseteq S$ have commuting holonomies:
   $[\mathrm{Mon}(\gamma_i), \mathrm{Mon}(\gamma_j)] = 0$.
2. Simultaneous diagonalization of the commuting monodromies
   decomposes the trace into a sum over eigenvalue-labelings.
3. The $\Phi_q$ insertions act by scalar on each eigenstrand
   (they are diagonal in the R-matrix eigenbasis).
4. Therefore the multi-crossing expectation is a product of
   single-crossing expectations.

The scalar obstruction — the only failure mode — would be a
non-abelian monodromy, ruled out by flatness.

## Failure of flatness

Flatness is equivalent to the **semisimplicity** of the braided
tensor category of $U_q(\mathfrak{sl}_2)$-representations:

- **Generic $q$ (not a root of unity)**: $U_q$-reps are semisimple,
  the KZ connection is flat, locality holds.
- **$q = e^{2 \pi i / \ell}$ (root of unity)**: non-semisimple
  subquotients appear (the Jones-Wenzl truncation at level
  $\ell - 2$); the category is still **modular** via Lyubashenko's
  construction, but the KZ connection acquires monodromy along
  paths encircling truncated weight spaces.  Locality fails at
  level $\ell$.
- **$q = 1/\varphi^2$ (golden degeneration)**: not a KZ failure
  per se — the connection is still flat on $X_n$, but the
  Descartes curve $\mathcal{E}_q$ itself becomes singular,
  so $z_q$ is undefined and locality is vacuous.

## The substrate as the locality window

At the pinned substrate parameter $q_0 \approx 1.11$, real and
generic:

$$
  q_0 \in \mathbb{R}_{>1} \setminus \{\text{roots of unity}\}
  \;\Longrightarrow\;
  \text{KZ flat}
  \;\Longrightarrow\;
  \text{locality.}
$$

Moreover, the
[soft confinement level $\ell_*(q_0) \approx 10$](#rem:soft-confinement-at-q0)
is far enough from the first non-trivial root of unity
$q = e^{i \pi / 3}$ (level $\ell = 3$) that Plancherel weights
for higher representations are exponentially suppressed — locality
holds to extremely high order in $1/\ell_*$.

## Corollary — exponential mass scaling

Combining locality (this remark) with the
[crossing-graded expansion](#conj:crossing-graded-mass-expansion),

$$
  \mathfrak{m}(\mathcal{K}; q_0)
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot
  \prod_{c \in \mathrm{Cr}(\mathcal{K})} (1 + \xi(q_0)\,\eta(c)).
$$

At the homogeneous fixed point $\eta(c) \equiv 1$:

$$
  \mathfrak{m}(\mathcal{K}; q_0)
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot (1 + \xi(q_0))^{c(\mathcal{K})}.
$$

At $q_0$, $\xi(q_0) = D(\lambda(\mathcal{E}_{q_0}))/\hbar_q^2
\approx 0.9170/0.00982 \approx 93.4$, so each crossing multiplies
mass by $\approx 94$.  Exponential scaling in crossing count is
then the empirical signature of KZ flatness at the substrate.
