The equivalence is pinned by the Tannakian rigidity of the fibre
functor $\tau$: once $\tau$ is fixed, reconstructing the dual group,
transporting the Hecke datum, and closing uniqueness admit no
freedom.  The proof realises this in three steps.

Concretely, the archetype to keep in mind is a rank-one $q$-local
system $\mathcal{L}_q$ together with the single $q$-Hecke eigensheaf
it governs; the general statement replaces this pair by the full
tensor categories on either side.

**Step 1: Tannakian reconstruction of $\check{G}_q$.**
By [fibre-functor rigidity](#rem:fibre-functor-rigidity), the
fibre functor
$\tau \colon \mathbf{Rep}(G_q) \to \mathrm{Vect}$ is unique up to
unique isomorphism.  Tannaka--Krein reconstruction gives
$G_q \cong \mathrm{Aut}^\otimes(\tau)$.  Applying root-system duality
and inversion $q \mapsto q^{-1}$ yields $\check{G}_q$ together with
its canonical fibre functor $\check{\tau}$.

**Step 2: Hecke data determines $\mathbb{L}_q$.**
For a $q$-Hecke eigensheaf $\mathcal{M}$ with eigenvalue
$\mathcal{L}_q$, the collection of isomorphisms
$\{\mathbf{T}_{x,\lambda}^{(q)}(\mathcal{M}) \simeq
\mathcal{M} \otimes V_\lambda^{(q)}(\mathcal{L}_q)_x\}$ defines a
tensor functor $\mathbf{Rep}(\check{G}_q) \to \mathrm{Vect}_X$.
This functor is a point of $\mathrm{LocSys}_{\check{G}_q}(X)$
(by [q-Hecke eigenvalue determination](#prop:q-hecke-eigenvalue)).
Conversely, every $q$-local system $\mathcal{L}_q$ produces, via the
Hecke correspondence, a $q$-$\mathcal{D}$-module
$\mathbb{L}_q^{-1}(\mathcal{L}_q)$ on $\mathrm{Bun}_{G_q}$.

**Step 3: Uniqueness from rigidity.**
Suppose $\mathbb{L}_q$ and $\mathbb{L}_q'$ are two equivalences
satisfying properties (1)--(3) of the
[$q$-Geometric Langlands conjecture](#conj:q-geometric-langlands).
Then $\mathbb{L}_q' \circ \mathbb{L}_q^{-1}$ is a tensor
auto-equivalence of
$\mathrm{QCoh}(\mathrm{LocSys}_{\check{G}_q}(X))$
preserving the tautological $q$-local system.  By the rigidity of
$\tau$, such an auto-equivalence is uniquely isomorphic to the
identity.  $\square$
