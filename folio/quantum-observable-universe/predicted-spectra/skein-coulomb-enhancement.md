Let $(\mathbf{C}, A, \tau)$ be a Descartes universe with substrate parameter $q$. Consider the beta decay $\mathcal{N}(Z, N) \to \mathcal{N}(p\!+\!1, n\!-\!1) + T_{2,3} + \nu^{\sigma}$. The emitted electron $T_{2,3}$ crosses each of the $Z = p + 1$ proton strands of the daughter nucleus as it exits the Hopf link. The $q$-deformed wedge product $\wedge_q$ ([crossing asymmetry](#rem:skein-crossing-asymmetry)) assigns weight $q$ to each positive electron-proton crossing. This produces a coherent product that multiplies the decay rate by the **Skein-Coulomb enhancement factor**:

$$
  F_q(Z, E)
  = 
  \frac{2\pi\eta_q}{1 - e^{-2\pi\eta_q}}
$$

The $q$-deformed Sommerfeld parameter is:

$$
  \eta_q
  = 
  \alpha_{\mathrm{EM}}(q)
  \cdot \frac{Z}{\beta_e}
$$

The EM coupling projection is $\alpha_{\mathrm{EM}}(q) = q^{-1}/([9]_q \cdot [10]_q)$ ([EM coupling projection](#prop:em-coupling-projection)). The velocity of the emitted electron is $\beta_e = v_e / c$.

**Derivation.**
Evaluating the canonical action $\mathfrak{S}_q$ ([canonical action](#prop:qou-canonical-action)) on the full outgoing state $\psi = T_{2,3} \cup \mathcal{N}(p\!+\!1, n\!-\!1)$ decomposes the action as:

$$
  \mathfrak{S}_q\big|_\psi
  = 
  \mathfrak{S}_q\big|_{\mathcal{N}}
  + 
  \sum_{j=1}^{Z} \mathcal{S}_{e\text{-}p_j}
  + 
  \mathfrak{S}_q\big|_{T_{2,3}}
$$

The middle sum runs over all electron-proton crossings. Each crossing contributes a Skein weight $\mathcal{S}_{e\text{-}p_j}(q) = q$. This is a positive crossing between two like-charge constituents. The electron radial wave function picks up a phase $e^{i\delta_\ell}$ at each proton. The phase shift is:

$$
  \delta_\ell
  = 
  \arg \Gamma(\ell + 1 + i\eta_q).
$$

Forming the coherent product of $Z$ such scattering amplitudes, summing over partial waves $\ell$, and integrating over the electron energy spectrum yields:

$$
  |\psi_e(0)|^2_{\text{Coulomb}}
  = 
  |\psi_e(0)|^2_{\text{free}}
   \times 
  F_q(Z, E).
$$

The decay rate is directly proportional to $|\psi_e(0)|^2$, the electron wave function at the nuclear origin. Thus, $F_q$ multiplies the leading-order rate.
