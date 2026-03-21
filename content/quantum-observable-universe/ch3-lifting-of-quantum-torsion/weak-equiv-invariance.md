Let $(\mathcal{C}, A, \omega)$ be a quantum observable universe and let
$\{A_n\}_{n \geq 0}$ be its recursive brane tower with cosimplicial
crossed groupoid structure
([Proposition](#prop:cosimplicial-crossed-groupoid)); let $q$ denote the substrate parameter.  Let
$\omega \colon \mathcal{A}_\infty \to \mathbb{C}$ be the vacuum state
([Proposition](#prop:vacuum-state)).  A *weak equivalence* between
brane levels $n$ and $m$ is a zigzag of coface and codegeneracy maps
$$
  \mathfrak{G}_n
  \xleftarrow{\;\sigma\;}
  \mathfrak{G}_{k_1}
  \xrightarrow{\;\delta\;}
  \cdots
  \xrightarrow{\;\delta\;}
  \mathfrak{G}_m
$$
in the cosimplicial crossed groupoid.  Then for every observable
$a \in \mathcal{A}_\infty$, the expectation value is invariant under
weak equivalence:
$$
  \omega\!\bigl(\iota_n(a|_n)\bigr)
  \;=\;
  \omega\!\bigl(\iota_m(a|_m)\bigr),
$$
where $\iota_n \colon \Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2))
\hookrightarrow \mathcal{A}_\infty$ is the canonical embedding and
$a|_n$ denotes the restriction of $a$ to level $n$.  In particular,
physical states (the GNS vectors of $\omega$) are invariant under
fluctuations of the substrate parameter $q(p)$ across brane levels.

---

By \cite[Theorem 1.1]{yekutieli2010}, a weak equivalence of central
extensions of gerbes induces an isomorphism on the category of global
objects up to isomorphism.  In the brane tower, the coface maps (jet
prolongation) and codegeneracy maps (descent) compose to give the descent
involution $\tau_n$ ([Definition](#def:descent-involution)), which is
idempotent.  The image $\mathcal{A}_{n+1}^{\mathrm{desc}}$
([Proposition](#prop:descent-eigenspaces)) is therefore isomorphic, as
an algebra, to the level-$n$ section algebra via the ascent embedding
$\ell_n$.

For the vacuum state, the compatibility
$\omega(\iota_n(a|_n)) = \omega_n(a|_n)$ holds by the universal property
of the direct limit ([Definition](#def:direct-limit-algebra)).  The
Haar-averaging construction in the proof of
[Proposition](#prop:vacuum-state) produces states $\omega_n$ that are
compatible with the transition maps:
$\omega_{n+1} \circ \iota_{n,n+1} = \omega_n$, where
$\iota_{n,n+1}$ is the transition map.  A zigzag of coface and
codegeneracy maps between levels $n$ and $m$ factors as a sequence of
such transition maps and their adjoints (the descent homomorphisms),
each of which preserves the Haar state by equivariance
([Lemma](#lem:descent), Step 5).

Therefore the expectation value
$\omega(\iota_n(a|_n)) = \omega_n(a|_n) = \omega_m(a|_m) =
\omega(\iota_m(a|_m))$
is invariant under weak equivalence.

For the GNS representation: the Hilbert space
$\mathcal{H}_\omega = \overline{\mathcal{A}_\infty / \ker(\omega)}$ with
inner product $\langle [a], [b] \rangle = \omega(a^* b)$ is unchanged by
the weak equivalence because $\omega$ is invariant.  The cyclic vector
$\Omega = [1]$ generates the same representation regardless of the brane
level at which it is evaluated, so the physical states (vectors in
$\mathcal{H}_\omega$) are insensitive to the substrate parameter
fluctuations across the tower.
