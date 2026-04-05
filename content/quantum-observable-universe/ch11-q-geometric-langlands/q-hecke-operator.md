Let $X$ be the brane curve and $G_q$ the quantum gauge group
(Definition \ref{def:quantum-gauge-group}).  For a closed point
$x \in X$ and a dominant coweight $\lambda$ of $G_q$, the
**$q$-Hecke operator** $\mathbf{T}_{x,\lambda}^{(q)}$ is the integral
transform

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

The $q$-Hecke operators satisfy the **Hecke algebra relation**:

$$
  (\mathbf{T}_{x,\lambda}^{(q)} - q)
  (\mathbf{T}_{x,\lambda}^{(q)} + q^{-1}) = 0,
$$

i.e. they act with eigenvalues $q$ and $-q^{-1}$ on the symmetric and
antisymmetric channels respectively, matching the braiding eigenvalues
of the Hecke algebra $H_n(q)$
(Definition \ref{def:braid-action-tensor}).
