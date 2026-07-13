The linear $\mathrm{C}_6$ chain links six carbon atoms end-to-end.

**Construction.**
Each carbon has 4 open linking sites. In the chain $\mathcal{C}_6^{(1)}$, each interior carbon consumes 2 sites for backbone bonds. The endpoint carbons consume 1 site each.

The linking matrix is the $6 \times 6$ tridiagonal matrix:

$$
  L^{\mathrm{chain}}
  = 
  \begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    1 & 0 & 1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 1 & 0 & 0 \\
    0 & 0 & 1 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1 & 0 & 1 \\
    0 & 0 & 0 & 0 & 1 & 0
  \end{pmatrix}.
$$

**Crossing energy.**
The chain has 5 bonds, giving $\mathfrak{E}_{\mathrm{cross}}(\mathrm{C}_6^{\mathrm{chain}}) = 5 \cdot E_{\mathrm{bond}}(1)$.

**Spring behaviour.**
The endpoint carbons act as soft modes. The endpoints can oscillate and the chain can bend and stretch at energies below the bond-breaking threshold. In chemistry, linear $\mathrm{C}_6$ is observed as cumulene and carbyne. These correspond to bond-order patterns $(2,2,2,2,2)$ and $(1,3,1,3,1)$.
