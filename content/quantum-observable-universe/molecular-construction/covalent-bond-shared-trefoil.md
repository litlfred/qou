*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Definition.**
*A **covalent bond of order $k$** between atoms $i$ and $j$ is the
Hopf linking of $k$ electron trefoils across the two nuclei.
Specifically, let $e_1, \ldots, e_k$ be electrons from atom $i$
(or shared between $i$ and $j$).  Each electron is a trefoil
$T_{2,3} = \sigma_0\sigma_1\sigma_0$ in its local $H_3(q)$.*

*In the [molecular braid](#def:molecular-braid), the covalent bond
operator for bond $b$ connecting atoms $i$ and $j$ is:*

$$
  L_b = \prod_{e=1}^{k_b}
  \sigma_{g_e(\mathfrak{p}_j)}^{-1} \cdot
  \sigma_{g_e(\mathfrak{p}_i)}^{-1}
$$

*where $g_e(\mathfrak{p}_j)$ is the generator index for the
crossing between shared electron $e$ and proton $\mathfrak{p}_j$
of atom $j$, and $g_e(\mathfrak{p}_i)$ for proton
$\mathfrak{p}_i$ of atom $i$.  Both crossings are $\sigma^{-1}$
(EM attraction), so each shared electron contributes **two
attractive crossings** — one to each nucleus.*

*The key distinction from a lone electron (bound to a single
nucleus):*

| | Lone electron | Shared electron (covalent) |
|:---|:---|:---|
| Crossings | $\sigma^{-1}_{g(\mathfrak{p}_i)}$ (1 attractive) | $\sigma^{-1}_{g(\mathfrak{p}_i)} \cdot \sigma^{-1}_{g(\mathfrak{p}_j)}$ (2 attractive) |
| Transfer matrix | $T_{\mathfrak{p}e}$ (single) | $T_{\mathfrak{p}_ie} \cdot T_{\mathfrak{p}_je}$ (product) |
| $\Phi_1$ contribution | $\ln\lvert V_e\rvert$ | $\ln\lvert V_{e,i}\rvert + \ln\lvert V_{e,j}\rvert$ |

*A bond of order $k$ contributes $2k$ attractive crossings.  The
LP dual finds the optimal assignment of electrons to bonding
positions by minimizing the total $\Phi_1$.*

*Bond orders:*
- *$k = 1$: single bond (H--H, C--H, C--C) — 1 shared pair*
- *$k = 2$: double bond (C=O, C=C) — 2 shared pairs*
- *$k = 3$: triple bond (C$\equiv$O, N$\equiv$N) — 3 shared pairs*
