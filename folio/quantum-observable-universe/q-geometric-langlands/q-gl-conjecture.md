Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
brane curve $X$, quantum gauge group $G_q$, and $q$-Langlands dual
$\check{G}_q$ ([q-Langlands dual](#def:q-langlands-dual)).

The correspondence below is the substrate-level analogue of geometric
Langlands: it relates $\mathcal{D}_q$-modules on the quantum bundle
stack to quasi-coherent sheaves on the moduli of local systems for the
$q$-dual, so that spectral data on one side controls automorphic data
on the other.  At the classical value $q = 1$ it specialises to the
ordinary geometric Langlands equivalence (property 5 below), which
fixes the target that the deformed statement must recover; the parameter
$q$ then deforms that equivalence across the non-torsion locus of the
substrate.  With this anchor in hand, the
**$q$-Geometric Langlands correspondence** asserts the existence of
an equivalence of $\infty$-categories:

$$
  \mathbb{L}_q \colon
  \mathcal{D}_q\text{-}\mathrm{mod}(\mathrm{Bun}_{G_q}(X))
  \xrightarrow{ \sim }
  \mathrm{QCoh}(\mathrm{LocSys}_{\check{G}_q}(X)).
$$

This equivalence is parametrised by the non-torsion locus $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$ and satisfies five properties:

1. **Hecke compatibility**: For every $q$-Hecke operator $\mathbf{T}_{x,\lambda}^{(q)}$ ([q-Hecke operator](#def:q-hecke-operator)), $\mathbb{L}_q$ intertwines the action on the left with the action of $V_\lambda^{(q)}$ on $\mathrm{LocSys}_{\check{G}_q}(X)$:
   $$
     \mathbb{L}_q \circ \mathbf{T}_{x,\lambda}^{(q)}
     \simeq
     V_\lambda^{(q)}(-)_x \otimes \mathbb{L}_q.
   $$
   This is the eigensheaf-matching condition: intertwining the
   $q$-Hecke action with tensoring by $V_\lambda^{(q)}$ is what makes
   $\mathbb{L}_q$ a Langlands correspondence rather than an arbitrary
   equivalence of categories.

2. **Fibre-functor factorisation**: the equivalence factors through
   the fibre functor $\tau$:
   $$
     \mathbb{L}_q = \tau^* \circ \mathbb{L}_q^{\mathrm{Tannakian}}.
   $$
   where $\mathbb{L}_q^{\mathrm{Tannakian}}$ is determined by
   Tannaka--Krein reconstruction for $\check{G}_q$.  Routing the
   equivalence through $\tau$ keeps it compatible with the observation
   frame, so that the dual group is recovered from its representation
   category rather than posited independently.

3. **$q$-Oper locus**: the equivalence $\mathbb{L}_q$ restricts to
   a bijection between $q$-opers ([q-oper](#def:q-oper)) and
   $q$-Hecke eigensheaves
   ([q-Hecke eigensheaf](#def:q-hecke-eigensheaf)):
   $$
     \mathrm{Op}_{\check{G}_q}(X)  \hookrightarrow 
     \mathrm{LocSys}_{\check{G}_q}(X)
     \quad\xrightarrow{\mathbb{L}_q^{-1}}\quad
     \{\text{$q$-Hecke eigensheaves}\}.
   $$
   This pins down which local systems arise as $q$-Hecke
   eigensheaves: the $q$-opers cut out the distinguished spectral
   parameters that the eigensheaves correspond to under $\mathbb{L}_q$.

4. **Kummer constraint**: the equivalence $\mathbb{L}_q$ is
   well-defined as a $\mathbb{G}_m$-family on the non-torsion
   locus $\mathbb{G}_m^{\mathrm{nt}}$.  At roots of unity
   $q \in \mu_n$ the quantum dimension $[n]_q = 0$ vanishes,
   the Frobenius pairing degenerates, and $\mathbb{L}_q$
   degenerates.  The obstruction
   ([Kummer filtration](#rem:kummer-filtration-obstruction))
   persists at all Kummer levels $n \nmid \chi(A)$.

5. **Classical limit**: as $q \to 1$, $\mathbb{L}_q$ recovers the
   classical Geometric Langlands equivalence.
