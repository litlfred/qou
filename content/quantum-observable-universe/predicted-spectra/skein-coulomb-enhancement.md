*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be a Descartes universe with substrate
parameter $q$.  In the beta decay
$\mathcal{N}(Z, N) \to \mathcal{N}(p\!+\!1, n\!-\!1) + T_{2,3} + \nu^{\sigma}$, the emitted electron $T_{2,3}$ crosses each of the
$Z = p + 1$ proton strands of the daughter nucleus as it exits the
Hopf link.  The $q$-deformed wedge product $\wedge_q$
([crossing asymmetry](#rem:skein-crossing-asymmetry)) assigns weight
$q$ to each positive electron-proton crossing, producing a coherent
product that multiplies the decay rate by the **Skein-Coulomb
enhancement factor**

$$
  F_q(Z, E)
  = 
  \frac{2\pi\eta_q}{1 - e^{-2\pi\eta_q}}
$$

where the $q$-deformed Sommerfeld parameter is

$$
  \eta_q
  = 
  \alpha_{\mathrm{EM}}(q)
  \cdot \frac{Z}{\beta_e}
$$

with $\alpha_{\mathrm{EM}}(q) = q^{-1}/([9]_q \cdot [10]_q)$
([EM coupling projection](#prop:em-coupling-projection)) and
$\beta_e = v_e / c$ the velocity of the emitted electron.

**Derivation.**
The canonical action $\mathfrak{S}_q$
([canonical action](#prop:qou-canonical-action)) evaluated on the
full outgoing state $\psi = T_{2,3} \cup \mathcal{N}(p\!+\!1, n\!-\!1)$
decomposes as

$$
  \mathfrak{S}_q\big|_\psi
  = 
  \mathfrak{S}_q\big|_{\mathcal{N}}
  + 
  \sum_{j=1}^{Z} \mathcal{S}_{e\text{-}p_j}
  + 
  \mathfrak{S}_q\big|_{T_{2,3}}
$$

where the middle sum runs over electron-proton crossings.  Each
crossing contributes a Skein weight $\mathcal{S}_{e\text{-}p_j}(q) = q$
(positive crossing between two like-charge constituents).  The
electron's radial wave function picks up a phase
$e^{i\delta_\ell}$ at each proton, where the phase shift is

$$
  \delta_\ell
  = 
  \arg \Gamma(\ell + 1 + i\eta_q).
$$

The coherent product of $Z$ such scattering amplitudes,
summed over partial waves $\ell$ and integrated over the
electron energy spectrum, gives

$$
  |\psi_e(0)|^2_{\text{Coulomb}}
  = 
  |\psi_e(0)|^2_{\text{free}}
   \times 
  F_q(Z, E).
$$

The decay rate is proportional to $|\psi_e(0)|^2$ (the electron
wave function at the nuclear origin), so $F_q$ multiplies the
leading-order rate.
