<!-- FILE_START: q-hecke-correspondences-intro.md -->
Building on the moduli of $q$-local systems, we construct the $q$-Hecke operator: a Hecke modification twisted by the Iwahori–Hecke generators $\sigma_i$. This operator acts on the moduli of $G_q$-bundles. A $q$-Hecke eigensheaf diagonalises this action, with eigenvalues landing in the representation ring of the dual group. The rigid fibre functor $\tau$ extracts these eigenvalues as characters, matching the automorphic side to the spectral side in the $q$-Geometric Langlands correspondence.
<!-- FILE_END: q-hecke-correspondences-intro.md -->

<!-- FILE_START: q-hecke-operator.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with brane curve $X$ and quantum gauge group $G_q$ ([quantum gauge group](#def:quantum-gauge-group)). Let $x \in X$ be a closed point and $\lambda$ a dominant coweight of $G_q$. The **$q$-Hecke operator** $\mathbf{T}_{x,\lambda}^{(q)}$ is the integral transform

$$
  \mathbf{T}_{x,\lambda}^{(q)} \colon
  \mathcal{D}_q\text{-}\mathrm{mod}(\mathrm{Bun}_{G_q})
  \longrightarrow
  \mathcal{D}_q\text{-}\mathrm{mod}(\mathrm{Bun}_{G_q})
$$

defined by the $q$-Hecke correspondence:

```tex
\begin{tikzcd}
  & \mathrm{Hecke}_{x,\lambda}^{(q)} \arrow[dl, "h_\leftarrow"'] \arrow[dr, "h_\rightarrow"] & \\
  \mathrm{Bun}_{G_q}(X) & & \mathrm{Bun}_{G_q}(X)
\end{tikzcd}
```

Here, $\mathrm{Hecke}_{x,\lambda}^{(q)}$ parametrises pairs $(\mathcal{P}, \mathcal{P}')$ of $G_q$-bundles on $X$ equipped with an isomorphism $\mathcal{P}|_{X \setminus x} \xrightarrow{\sim} \mathcal{P}'|_{X \setminus x}$ of relative position $\lambda$.

The $q$-Hecke operators satisfy the Iwahori--Hecke algebra relation ([braiding eigenvalues](#prop:braid-action-tensor)):

$$
  (\mathbf{T}_{x,\lambda}^{(q)} - q)
  (\mathbf{T}_{x,\lambda}^{(q)} + q^{-1}) = 0.
$$

They act with eigenvalues $q$ and $-q^{-1}$ on the symmetric and antisymmetric channels, respectively.
<!-- FILE_END: q-hecke-operator.md -->

<!-- FILE_START: q-hecke-eigensheaf.md -->
A $q$-$\mathcal{D}$-module $\mathcal{M}$ on $\mathrm{Bun}_{G_q}(X)$ is a **$q$-Hecke eigensheaf** with eigenvalue $\mathcal{L}_q \in \mathrm{LocSys}_{\check{G}_q}(X)$ if it admits functorial isomorphisms

$$
  \mathbf{T}_{x,\lambda}^{(q)}(\mathcal{M})
  \simeq
  \mathcal{M} \otimes V_\lambda^{(q)}(\mathcal{L}_q)_x
$$

for every closed point $x \in X$ and every dominant coweight $\lambda$. Here, $V_\lambda^{(q)}$ is the irreducible representation of $\check{G}_q$ of highest weight $\lambda$, and $V_\lambda^{(q)}(\mathcal{L}_q)_x$ is its fibre at $x$ under the $q$-local system $\mathcal{L}_q$ ([q-local system](#def:q-local-system)).

These isomorphisms must be compatible with:

1. **Tensor products**: The isomorphism for $\lambda + \mu$ is the composition of the isomorphisms for $\lambda$ and $\mu$, twisted by the braiding $\sigma_q \colon V_\lambda^{(q)} \otimes V_\mu^{(q)} \to V_\mu^{(q)} \otimes V_\lambda^{(q)}$.
2. **Factorisation**: For distinct points $x \neq y$, the Hecke operators commute up to a $(q-1)$-correction: $[\mathbf{T}_{x,\lambda}^{(q)}, \mathbf{T}_{y,\mu}^{(q)}] = O(q-1)$.
<!-- FILE_END: q-hecke-eigensheaf.md -->

<!-- FILE_START: q-hecke-eigenvalue.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q$. Let $\mathcal{M}$ be a $q$-Hecke eigensheaf on $\mathrm{Bun}_{G_q}(X)$ ([q-Hecke eigensheaf](#def:q-hecke-eigensheaf)). Its eigenvalue $\mathcal{L}_q \in \mathrm{LocSys}_{\check{G}_q}(X)$ is uniquely determined by the action of $\tau$ on the Hecke eigenvalue data:

$$
  \mathcal{L}_q \simeq
  \mathrm{Aut}^\otimes(\tau)\text{-}\mathrm{equivariantisation of }
  \big\{ V_\lambda^{(q)}(\mathcal{L}_q)_x \big\}_{\lambda, x}.
$$

The rigidity of the fibre functor ([fibre-functor rigidity](#rem:fibre-functor-rigidity)) implies that this collection of Hecke eigenvalues determines $\mathcal{L}_q$ up to unique isomorphism.
<!-- FILE_END: q-hecke-eigenvalue.md -->

