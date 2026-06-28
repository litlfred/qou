When
$G = C_5$ (cyclic of order $5$) and $q = 1$, the quantum-group
Fourier transform degenerates to the **classical discrete Fourier
transform** on $\mathbb{Z}/5$.  The five irreducible characters
$\chi_k(j) = \zeta^{kj}$ (where $\zeta = e^{2\pi i/5}$) are the
grouplikes $\exp_1(2\pi i k \cdot / 5)$, and the Peter--Weyl
projection becomes

$$
  \mathcal{F}[x](k) \;=\; \sum_{j=0}^{4} \zeta^{kj}  x_j \;=\; w_k,
$$

the $k$-th Lagrange resolvent
([Lagrange resolvents](#rem:lagrange-resolvents)).  The Briggs--Klein
chart ([Briggs--Klein chart](#def:briggs-klein-chart)) on Bring's
surface ([smoothness of Bring's surface](#rem:brings-smoothness))
is built from these DFT coordinates: even where two colour sheets
$x_i, x_j$ collide (branch points of the projection $\pi$), the
Fourier components $w_k$ remain pairwise distinct because they
live in *different* isotypic blocks.  Smoothness of the
Briggs--Klein chart is thus a direct consequence of the monoidal
property of $\mathcal{F}$: Fourier decomposition separates
spectral components, rendering the position-space collision
invisible on each summand.
