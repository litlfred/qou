Let $\mathbf{w}=(w_1,w_2,w_3,w_4)$ be a spectral resolvent tuple. The two involutions are the **twist**:
```tex
\begin{align}
  \sigma_1(\mathbf{w}) &= (w_2,w_1,w_4,w_3)
    \label{eq:braid-twist}\\[4pt]
  \sigma_2(\mathbf{w}) &= (w_4,w_3,w_2,w_1)
    &&\text{(\textbf{flip}).}
    \label{eq:braid-flip}
\end{align}
```
As $4\times 4$ permutation matrices, these are:
```tex
\begin{equation}\label{eq:perm-matrices}
  \sigma_1=\begin{pmatrix}
    0&1&0&0\\1&0&0&0\\0&0&0&1\\0&0&1&0
  \end{pmatrix},\quad
  \sigma_2=\begin{pmatrix}
    0&0&0&1\\0&0&1&0\\0&1&0&0\\1&0&0&0
  \end{pmatrix}.
\end{equation}
```
On the 4-tuple, these involutions generate the Klein four-group $V_4=\{\mathrm{id},\sigma_1,\sigma_2,\sigma_1\sigma_2\}$, with $\sigma_1\sigma_2\colon\mathbf{w}\mapsto(w_3,w_4,w_1,w_2)$.
