Under the hypotheses of the
[$q$-Geometric Langlands conjecture](#conj:q-geometric-langlands),
the Tannakian rigidity of the fibre functor $\tau$ pins the
correspondence: it forces $\tau$ to determine the equivalence
$\mathbb{L}_q$ uniquely up to natural isomorphism:

$$
  \mathbb{L}_q(\mathcal{M})(\mathcal{L}_q)
  \simeq
  \mathrm{Hom}_{\mathbf{Rep}(\check{G}_q)}
  \big(\tau(-),
  \mathrm{Hecke}_q(\mathcal{M}, \mathcal{L}_q)\big).
$$

where $\mathrm{Hecke}_q(\mathcal{M}, \mathcal{L}_q)$ is the tensor
functor $V_\lambda^{(q)} \mapsto
\mathbf{T}_{x,\lambda}^{(q)}(\mathcal{M}) \otimes
\mathcal{L}_q(V_\lambda^{(q)})_x^*$ encoding all Hecke eigenvalue
data simultaneously. Evaluated at a single dominant weight
$\lambda$, the right-hand side is the Hom-set into
$\mathbf{T}_{x,\lambda}^{(q)}(\mathcal{M}) \otimes
\mathcal{L}_q(V_\lambda^{(q)})_x^*$ — the Hecke eigenvalue datum at
that one $\lambda$; letting $\lambda$ range over all dominant
weights assembles these single-weight data into the equivalence
above.

This uniqueness is the Tannakian rigidity of $\tau$
([fibre-functor rigidity](#rem:fibre-functor-rigidity)): any two
equivalences compatible with the Hecke eigensheaf structure and the
fibre functor are connected by a unique natural isomorphism.
