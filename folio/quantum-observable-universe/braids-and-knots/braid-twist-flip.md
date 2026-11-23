Let $\mathbf{b}=(b_0,b_1,b_2)$ be the three branches of the cubic constraint — the sheets that the trefoil monodromy group $S_3\cong D_3$, the Galois group of the cubic, permutes. The two braid generators are the reflections **twist** $\sigma_1=(b_0\,b_1)$ and **flip** $\sigma_2=(b_1\,b_2)$, as $3\times 3$ permutation matrices:
```tex
\begin{equation}\label{eq:perm-matrices}
  \sigma_1=\begin{pmatrix}
    0&1&0\\1&0&0\\0&0&1
  \end{pmatrix},\quad
  \sigma_2=\begin{pmatrix}
    1&0&0\\0&0&1\\0&1&0
  \end{pmatrix}.
\end{equation}
```
Both are involutions ($\sigma_1^2=\sigma_2^2=\mathrm{id}$). They satisfy the **braid relation** $\sigma_1\sigma_2\sigma_1=\sigma_2\sigma_1\sigma_2$ — the defining relation of the trefoil-knot group $B_3$ — and their product is the order-$3$ **rotation**

$$
  \alpha=\sigma_1\sigma_2,\qquad \alpha^3=\mathrm{id},
$$

the cyclic permutation of the three branches; it is the $\mathrm{SU}(2)$ generator $\alpha$ of [the $\mathrm{SU}(2)$ generators](#def:su2-generators). The **dihedral relation** $\sigma_1\,\alpha\,\sigma_1=\alpha^{-1}$ exhibits $D_3\cong S_3$.
