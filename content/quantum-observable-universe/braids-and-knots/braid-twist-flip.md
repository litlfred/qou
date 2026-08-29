Let $\mathbf{w}=(w_1,w_2,w_3,w_4)$ be a spectral resolvent tuple. The two generators of the trefoil monodromy group $S_3\cong D_3$ are the **twist** $\sigma_1=(w_1\,w_2)$ and the **flip** $\sigma_2=(w_2\,w_3)$:
```tex
\begin{align}
  \sigma_1(\mathbf{w}) &= (w_2,w_1,w_3,w_4)
    \label{eq:braid-twist}\\[4pt]
  \sigma_2(\mathbf{w}) &= (w_1,w_3,w_2,w_4).
    \label{eq:braid-flip}
\end{align}
```
As $4\times 4$ permutation matrices, these are:
```tex
\begin{equation}\label{eq:perm-matrices}
  \sigma_1=\begin{pmatrix}
    0&1&0&0\\1&0&0&0\\0&0&1&0\\0&0&0&1
  \end{pmatrix},\quad
  \sigma_2=\begin{pmatrix}
    1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1
  \end{pmatrix}.
\end{equation}
```
Both are involutions. A faithful $S_3$ action on four resolvents must fix one resolvent and permute the other three by the standard representation, since $S_3$ has no faithful action on four points ($4\nmid 6$); here $w_4$ is the fixed resolvent, the choice of index being a labelling convention. The generators satisfy the **braid relation** $\sigma_1\sigma_2\sigma_1=\sigma_2\sigma_1\sigma_2$ — the defining relation of the trefoil-knot group $B_3$ — and their product is the order-$3$ $3$-cycle $\sigma_1\sigma_2\colon\mathbf{w}\mapsto(w_3,w_1,w_2,w_4)$. They do **not** commute; the commuting reading (which would give the Klein four-group $V_4$) violates the braid relation.
