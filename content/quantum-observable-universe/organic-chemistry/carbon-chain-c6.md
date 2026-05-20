The simplest carbon Hopf chain is the linear $\mathrm{C}_6$
molecule: six carbon atoms linked end-to-end.

**Construction.**
Each carbon atom ([carbon valence](#rem:carbon-valence)) has 4
open linking sites.  In the chain $\mathcal{C}_6^{(1)}$
([molecular Hopf chain](#def:molecular-hopf-chain)), each interior
carbon ($\mathcal{A}_2$ through $\mathcal{A}_5$) consumes 2 sites
for backbone bonds, leaving 2 sites free.  The endpoint carbons
($\mathcal{A}_1$ and $\mathcal{A}_6$) consume 1 site each,
leaving 3 free.

$$
  \mathrm{C}_6^{\mathrm{chain}}
  = 
  \mathcal{A}(6,6)_1
   \underset{B_1}{\oplus}
  \mathcal{A}(6,6)_2
   \underset{B_1}{\oplus}
  \cdots
   \underset{B_1}{\oplus}
  \mathcal{A}(6,6)_6
$$

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
The chain has 5 bonds, giving

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathrm{C}_6^{\mathrm{chain}})
  = 
  5 \cdot E_{\mathrm{bond}}(1).
$$

**Spring behaviour.**
The endpoint carbons ($\mathcal{A}_1$ and $\mathcal{A}_6$) each
have 3 dangling linking sites.  These act as soft modes
([spring-like modes](#rem:chain-spring-modes)): the endpoints can
oscillate (Reidemeister I curls) and the chain can bend and
stretch at energies far below the bond-breaking threshold.

In real chemistry, linear $\mathrm{C}_6$ is observed as both
**cumulene** ($=\!=\!=\!=\!=\!=$, consecutive double bonds) and
**carbyne** ($-\!\equiv\!-\!\equiv\!-$, alternating single and
triple bonds) forms.  In the Hopf chain picture, these correspond
to bond-order patterns $(k_1, \ldots, k_5) = (2,2,2,2,2)$ and
$(1,3,1,3,1)$ respectively — different distributions of shared
trefoils across the 5 bonds (total bond order 10 and 9).
