Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
brane curve $X$ and quantum gauge group $G_q$
([quantum gauge group](#def:quantum-gauge-group)).  For a closed
point $x \in X$ and a dominant coweight $\lambda$ of $G_q$, the
**$q$-Hecke operator** $\mathbf{T}_{x,\lambda}^{(q)}$ is the
integral transform

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

where $\mathrm{Hecke}_{x,\lambda}^{(q)}$ parametrises pairs
$(\mathcal{P}, \mathcal{P}')$ of $G_q$-bundles on $X$ together with
an isomorphism $\mathcal{P}|_{X \setminus x} \xrightarrow{\sim}
\mathcal{P}'|_{X \setminus x}$ of relative position $\lambda$.

The $q$-Hecke operators satisfy the Iwahori--Hecke algebra relation
([braiding eigenvalues](#prop:braid-action-tensor)):

$$
  (\mathbf{T}_{x,\lambda}^{(q)} - q)
  (\mathbf{T}_{x,\lambda}^{(q)} + q^{-1}) = 0,
$$

acting with eigenvalues $q$ and $-q^{-1}$ on the symmetric and
antisymmetric channels respectively.
