By \[Theorem 1.1, yekutieli2010], a weak equivalence of central
extensions of gerbes induces an isomorphism on the category of global
objects up to isomorphism.  In the brane tower, the coface maps (jet
prolongation) and codegeneracy maps (:refterm[descent]{#descent}) compose to give the :refterm[descent]{#descent}
involution $\hat{\tau}_n$ ([:refterm[descent]{#descent} involution](#def:descent-involution)), which is
idempotent.  The image $\mathcal{A}_{n+1}^{\mathrm{desc}}$
([:refterm[descent]{#descent} eigenspaces](#prop:descent-eigenspaces)) is therefore isomorphic, as
an algebra, to the level-$n$ section algebra via the ascent embedding
$\ell_n$.

For the vacuum state, the compatibility
$\tau(\iota_n(a|_n)) = \tau^{(n)}(a|_n)$ holds by the universal property
of the direct limit ([direct limit algebra](#def:direct-limit-algebra)).  The
Haar-averaging construction in the proof of
[vacuum state](#prop:vacuum-state) produces states $\tau^{(n)}$ that are
compatible with the transition maps:
$\tau^{(n+1)} \circ \iota_{n,n+1} = \tau^{(n)}$, where
$\iota_{n,n+1}$ is the transition map.  A zigzag of coface and
codegeneracy maps between levels $n$ and $m$ factors as a sequence of
such transition maps and their adjoints (the :refterm[descent]{#descent} homomorphisms),
each of which preserves the Haar state by equivariance
([:refterm[descent]{#descent}](#lem:descent), Step 5).

Therefore the expectation value
$\tau(\iota_n(a|_n)) = \tau^{(n)}(a|_n) = \tau^{(m)}(a|_m) = \tau(\iota_m(a|_m))$
is invariant under weak equivalence.

For the GNS representation: the Hilbert space
$\mathcal{H}_\tau = \overline{\mathcal{A}_\infty / \ker(\tau)}$ with
inner product $\langle [a], [b] \rangle = \tau(a^* b)$ is unchanged by
the weak equivalence because $\tau$ is invariant.  The cyclic vector
$\Omega = [1]$ generates the same representation regardless of the brane
level at which it is evaluated, so the physical states (vectors in
$\mathcal{H}_\tau$) are insensitive to the aether parameter
fluctuations across the tower.
