A $q$-$\mathcal{D}$-module $\mathcal{M}$ on $\mathrm{Bun}_{G_q}(X)$
is a **$q$-Hecke eigensheaf** with eigenvalue
$\mathcal{L}_q \in \mathrm{LocSys}_{\check{G}_q}(X)$ if, for every
closed point $x \in X$ and every dominant coweight $\lambda$, there
exists a functorial isomorphism

$$
  \mathbf{T}_{x,\lambda}^{(q)}(\mathcal{M})
  \simeq
  \mathcal{M} \otimes V_\lambda^{(q)}(\mathcal{L}_q)_x,
$$

where $V_\lambda^{(q)}$ is the irreducible representation of
$\check{G}_q$ of highest weight $\lambda$ and
$V_\lambda^{(q)}(\mathcal{L}_q)_x$ denotes its fibre at $x$ under
the $q$-local system $\mathcal{L}_q$
([q-local system](#def:q-local-system)).

The isomorphisms are required to be compatible with:

1. **Tensor products**: the isomorphism for $\lambda + \mu$ is the
   composition of the isomorphisms for $\lambda$ and $\mu$, twisted
   by the braiding $\sigma_q \colon V_\lambda^{(q)} \otimes
   V_\mu^{(q)} \to V_\mu^{(q)} \otimes V_\lambda^{(q)}$.

2. **Factorisation**: for distinct points $x \neq y$ the Hecke
   operators commute up to the $(q-1)$-correction:
   $[\mathbf{T}_{x,\lambda}^{(q)}, \mathbf{T}_{y,\mu}^{(q)}]
   = O(q-1)$.
