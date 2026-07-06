We proceed in three steps.

**Step 1: Tannakian reconstruction of $\check{G}_q$.**
By [fibre-functor rigidity](#rem:fibre-functor-rigidity), the fibre functor $\tau \colon \mathbf{Rep}(G_q) \to \mathrm{Vect}$ is unique up to unique isomorphism. Tannaka--Krein reconstruction gives $G_q \cong \mathrm{Aut}^\otimes(\tau)$. Applying root-system duality and inversion $q \mapsto q^{-1}$ yields $\check{G}_q$ and its canonical fibre functor $\check{\tau}$.

**Step 2: Hecke data determines $\mathbb{L}_q$.**
Let $\mathcal{M}$ be a $q$-Hecke eigensheaf with eigenvalue $\mathcal{L}_q$. The collection of isomorphisms $\{\mathbf{T}_{x,\lambda}^{(q)}(\mathcal{M}) \simeq \mathcal{M} \otimes V_\lambda^{(q)}(\mathcal{L}_q)_x\}$ defines a tensor functor $\mathbf{Rep}(\check{G}_q) \to \mathrm{Vect}_X$. This functor is a point of $\mathrm{LocSys}_{\check{G}_q}(X)$ ([q-Hecke eigenvalue determination](#prop:q-hecke-eigenvalue)). Conversely, the Hecke correspondence sends every $q$-local system $\mathcal{L}_q$ to a $q$-$\mathcal{D}$-module $\mathbb{L}_q^{-1}(\mathcal{L}_q)$ on $\mathrm{Bun}_{G_q}$.

**Step 3: Uniqueness from rigidity.**
Suppose $\mathbb{L}_q$ and $\mathbb{L}_q'$ both satisfy properties (1)--(3) of the [$q$-Geometric Langlands conjecture](#conj:q-geometric-langlands). The composition $\mathbb{L}_q' \circ \mathbb{L}_q^{-1}$ is a tensor auto-equivalence of $\mathrm{QCoh}(\mathrm{LocSys}_{\check{G}_q}(X))$ that preserves the tautological $q$-local system. By the rigidity of $\tau$, this auto-equivalence is uniquely isomorphic to the identity. $\square$
