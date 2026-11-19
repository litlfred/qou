**Derivation (Breit--Wheeler categorical pair production).**

This derivation establishes categorical Breit--Wheeler pair production by introducing the bare and colored photon states, computing the normal-form reduction of their pair product, evaluating the linear and circular polarization limits, and identifying the four-term extension.

#### Bare photon pair

Two identical bare photons yield the product $\gamma\gamma = \sigma_0^2$. Applying the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + \mathbf{1}$ gives:

$$
  \mathrm{NF}(\gamma\gamma)
  =  (q - q^{-1})\sigma_0 + \mathbf{1}.
$$

The net valuation is $\mathrm{net}(\gamma\gamma) = 1 + (q - q^{-1}) \approx 1.209$. This corresponds to a bare pair energy $E_{\mathrm{pair}} \approx 1.006$ MeV. This falls $1.6\%$ short of the physical $2m_e = 1.022$ MeV threshold.

#### Colored photon

Matching the $2m_e$ threshold requires color dressing. The photon incorporates an admixture of the Hecke generators $\sigma_0$ and $\sigma_1$. A color parameter weights each generator:

$$
  \gamma
  = 
  \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  + \varphi_{01}\sigma_0\sigma_1^{-1},
$$

where $\varphi_0, \varphi_1, \varphi_{01} \in \mathbb{R}$. The generator $\sigma_0$ acts on the $(\sigma, r)$ plane. The generator $\sigma_1$ acts on the $(r, g)$ plane. The switched Borromean-step word $V = \sigma_0\sigma_1^{-1} = L_+ - h\sigma_0$ ($h = q - q^{-1}$) provides two-step dressing. 

This derivation treats the 3-term specialization $\varphi_{01} = 0$.

#### Normal-form pair product

Expanding the product $\gamma_1 \cdot \gamma_2$ for two 3-term colored photons $\gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1$ and $\gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1$ and reducing via $\sigma_i^2 = h\sigma_i + \mathbf{1}$ with $h = q - q^{-1}$, collecting by basis element yields:

$$
  \mathrm{NF}(\gamma_1 \cdot \gamma_2)
  = 
  \underbrace{(1 + \varphi_0\psi_0 + \varphi_1\psi_1)}_{\gamma}
  \mathbf{1}
  + 
  \underbrace{(\varphi_0 + \psi_0 + \varphi_0\psi_0h)}_{\sigma_0}
  \sigma_0
  + 
  \underbrace{(\varphi_1 + \psi_1 + \varphi_1\psi_1h)}_{\sigma_1}
  \sigma_1
  + 
  \underbrace{\varphi_0\psi_1}_{L_+}
  \sigma_0\sigma_1
  + 
  \underbrace{\varphi_1\psi_0}_{L_-}
  \sigma_1\sigma_0.
$$

The Hecke self-energy terms $\varphi_0\psi_0$ and $\varphi_1\psi_1$ contribute to the $\mathbf{1}$ coefficient. The Hopf link terms $L_\pm$ arise strictly from cross-color products $\varphi_0\psi_1$ and $\varphi_1\psi_0$.

The net evaluation is the sum of all coefficients:

$$
  \mathrm{net}
  = 
  (1 + \varphi_0 + \varphi_1)(1 + \psi_0 + \psi_1)
  + 
  (\varphi_0\psi_0 + \varphi_1\psi_1)h.
$$

#### Polarization limits

**Linear (symmetric) polarization:** 
Setting equal color weights across both generators, $\varphi_0 = \varphi_1 = \psi_0 = \psi_1 = \phi$, yields:
- $\gamma$: $1 + 2\phi^2$
- $\sigma_0$: $2\phi + \phi^2 h$
- $\sigma_1$: $2\phi + \phi^2 h$
- $L_+$: $\phi^2$
- $L_-$: $\phi^2$

The equal Hopf link content ($L_+ = L_- = \phi^2$) implies zero chirality. The net valuation is $(1 + 2\phi)^2 + 2\phi^2 h$. Fitting this to $E_{\mathrm{pair}} = 2m_e$ gives $\phi = 0.0487$. This value is a fit to the measured electron mass rather than a derivation.

**Circular (orthogonal) polarization:**
Setting orthogonal polarization weights, $\varphi_0 = s$, $\varphi_1 = 0$, $\psi_0 = 0$, $\psi_1 = s$, yields:
- $\gamma$: $1$
- $\sigma_0$: $s$
- $\sigma_1$: $s$
- $L_+$: $s^2$
- $L_-$: $0$

Only $L_+$ appears ($L_- = 0$). This produces maximally chiral Hopf content. The Hecke self-energy vanishes ($\varphi_0\psi_0 = \varphi_1\psi_1 = 0$). The net valuation is $(1 + s)^2$. Fitting this to $E_{\mathrm{pair}} = 2m_e$ gives $s = 0.0978$. This value is a fit rather than a derivation.

Both fits close the $1.6\%$ energy gap by construction, so closing it is not evidence for either model. The color weight generates Hopf link content $L_\pm$ that supplies the missing pair production energy. The asymmetry $L_+ \neq L_-$ in the circular model acts as the categorical expression of photon helicity.

#### Four-term extension

Activating $\varphi_{01} \neq 0$ recovers the general 4-term photon. The $\gamma\gamma$ product directly opens the $e^-$ (trefoil) channel. The 6-term normal form and the derivation of nucleons from pair production follow from these operations.
