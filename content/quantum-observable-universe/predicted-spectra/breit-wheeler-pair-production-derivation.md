**Derivation (Breit--Wheeler categorical pair production).**

We develop the [Breit--Wheeler categorical pair production](#def:breit-wheeler-pair-production). We define the bare and colored photon, compute the normal-form reduction of the pair product, evaluate linear and circular polarization limits, and identify the four-term extension.

#### Bare photon pair

Two identical bare photons yield the product $\gamma\gamma = \sigma_0^2$. Applying the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + \mathbf{1}$:

$$
  \mathrm{NF}(\gamma\gamma)
  =  (q - q^{-1})\sigma_0 + \mathbf{1}.
$$

The net valuation is $\mathrm{net}(\gamma\gamma) = 1 + (q - q^{-1}) \approx 1.209$. This corresponds to a bare pair energy $E_{\mathrm{pair}} \approx 1.006$ MeV, falling $1.6\%$ short of the physical $2m_e = 1.022$ MeV threshold.

#### Colored photon

Matching the $2m_e$ threshold requires color dressing. The photon incorporates an admixture of the Hecke generators $\sigma_0$ and $\sigma_1$, each weighted by a color parameter ([color content](#rem:knot-basis-color-content)):

$$
  \gamma
  = 
  \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  + \varphi_{01}\sigma_0\sigma_1,
$$

where $\varphi_0, \varphi_1, \varphi_{01} \in \mathbb{R}$. The generator $\sigma_0$ acts on the $(\sigma, r)$ plane, $\sigma_1$ on the $(r, g)$ plane, and $\sigma_0\sigma_1 = L_+$ provides Hopf-link dressing. 

The derivation below treats the 3-term specialization $\varphi_{01} = 0$. For the general 4-term formula, see [photon knot operations](#rem:physics-names-knot-operations).

#### Normal-form pair product

Given two 3-term colored photons $\gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1$ and $\gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1$, we expand the product $\gamma_1 \cdot \gamma_2$ and reduce via $\sigma_i^2 = h\sigma_i + \mathbf{1}$ (where $h = q - q^{-1}$).

See [Table: Breit-Wheeler Hecke product table](#tbl:breit-wheeler-pair-production-table-data).

Collecting by basis element yields:

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

The net evaluation (sum of all coefficients) is:

$$
  \mathrm{net}
  = 
  (1 + \varphi_0 + \varphi_1)(1 + \psi_0 + \psi_1)
  + 
  (\varphi_0\psi_0 + \varphi_1\psi_1)h.
$$

#### Polarization limits

**Linear (symmetric) polarization:** 
Set equal color in both generators, $\varphi_0 = \varphi_1 = \psi_0 = \psi_1 = \phi$.
- $\gamma$: $1 + 2\phi^2$
- $\sigma_0$: $2\phi + \phi^2 h$
- $\sigma_1$: $2\phi + \phi^2 h$
- $L_+$: $\phi^2$
- $L_-$: $\phi^2$

The equal Hopf link content ($L_+ = L_- = \phi^2$) implies zero chirality. The net valuation is $(1 + 2\phi)^2 + 2\phi^2 h$. Setting $E_{\mathrm{pair}} = 2m_e$ fixes $\phi = 0.0487$.

**Circular (orthogonal) polarization:**
Set orthogonal polarization, $\varphi_0 = s$, $\varphi_1 = 0$, $\psi_0 = 0$, $\psi_1 = s$.
- $\gamma$: $1$
- $\sigma_0$: $s$
- $\sigma_1$: $s$
- $L_+$: $s^2$
- $L_-$: $0$

Only $L_+$ appears ($L_- = 0$), producing maximally chiral Hopf content. The Hecke self-energy vanishes ($\varphi_0\psi_0 = \varphi_1\psi_1 = 0$). The net valuation is $(1 + s)^2$. Setting $E_{\mathrm{pair}} = 2m_e$ fixes $s = 0.0978$.

Both models close the $1.6\%$ energy gap. The color weight generates Hopf link content $L_\pm$ that supplies the missing pair production energy. The asymmetry $L_+ \neq L_-$ in the circular model acts as the categorical expression of photon helicity.

#### Four-term extension

Activating $\varphi_{01} \neq 0$ recovers the general 4-term photon. The $\gamma\gamma$ product then directly opens the $e^-$ (trefoil) channel. See [photon knot operations](#rem:physics-names-knot-operations) for the 6-term normal form, and [4-term pair nucleon](#prop:four-term-pair-nucleon) for the complete derivation of nucleons from pair production.

**Witness:** `breit-wheeler-nucleon-nf.witness.json`
