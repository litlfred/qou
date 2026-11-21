**Derivation (Breit--Wheeler categorical pair production).**

This derives the Breit--Wheeler categorical pair production with the [photon](#def:photon) $\gamma(\varphi) = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\,\sigma_0\sigma_1^{-1}$. It treats the bare photon, the three-term specialisation $\varphi_{01} = 0$, its polarization limits, and the full four-term product.

#### Bare photon pair

The bare photon is $\gamma(0) = \mathbf{1}$, so two bare photons give $\gamma(0)\gamma(0) = \mathbf{1}$. A bare pair carries no crossing.

An earlier version of this derivation took a bare photon to be the single crossing $\sigma_0$, and so took the bare pair to be $\sigma_0^2 = (q - q^{-1})\sigma_0 + \mathbf{1}$, with net valuation $1 + (q - q^{-1}) \approx 1.209$ and pair energy $\approx 1.006$ MeV. Under [the photon definition](#def:photon) $\sigma_0$ is one term of a photon, not a photon, so that computation is about the $\sigma_0$ term squared, not about a photon pair.

#### Colored photon

A [photon](#def:photon) carries three colour weights:

$$
  \gamma
  = 
  \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  {} + \varphi_{01}\,\sigma_0\sigma_1^{-1},
$$

where $\varphi_0, \varphi_1, \varphi_{01} \in R$. The generator $\sigma_0$ acts on the $(\sigma, r)$ plane and $\sigma_1$ on the $(r, g)$ plane. The fourth term is the chiral pair-production vertex $\sigma_0\sigma_1^{-1} = \sigma_0\sigma_1 - h\,\sigma_0$, with $h = q - q^{-1}$ ([photon](#def:photon)).

This derivation first treats the three-term specialisation $\varphi_{01} = 0$, which is the same element whether the fourth term is written $\sigma_0\sigma_1^{-1}$ or $\sigma_0\sigma_1$. The colour weights were introduced here to match the $2m_e$ threshold; that is selection against the target, and the weights below are fits.

#### Normal-form pair product

Expand the product $\gamma_1 \cdot \gamma_2$ for two 3-term colored photons $\gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1$ and $\gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1$. Reduce via $\sigma_i^2 = h\sigma_i + \mathbf{1}$, where $h = q - q^{-1}$.

Collecting by basis element yields:

$$
  \mathrm{NF}(\gamma_1 \cdot \gamma_2)
  = 
  \underbrace{(1 + \varphi_0\psi_0 + \varphi_1\psi_1)}_{\gamma}
  \mathbf{1}
  {} + 
  \underbrace{(\varphi_0 + \psi_0 + \varphi_0\psi_0h)}_{\sigma_0}
  \sigma_0
  {} + 
  \underbrace{(\varphi_1 + \psi_1 + \varphi_1\psi_1h)}_{\sigma_1}
  \sigma_1
  {} + 
  \underbrace{\varphi_0\psi_1}_{L_+}
  \sigma_0\sigma_1
  {} + 
  \underbrace{\varphi_1\psi_0}_{L_-}
  \sigma_1\sigma_0.
$$

The Hecke self-energy terms $\varphi_0\psi_0$ and $\varphi_1\psi_1$ contribute to the $\mathbf{1}$ coefficient. The Hopf link terms $L_\pm$ arise strictly from cross-color products $\varphi_0\psi_1$ and $\varphi_1\psi_0$.

The net evaluation is the sum of all coefficients:

$$
  \mathrm{net}
  = 
  (1 + \varphi_0 + \varphi_1)(1 + \psi_0 + \psi_1)
  {} + 
  (\varphi_0\psi_0 + \varphi_1\psi_1)h.
$$

#### Polarization limits

**Linear (symmetric) polarization:** 
Take equal color in both generators, $\varphi_0 = \varphi_1 = \psi_0 = \psi_1 = \phi$.
- $\gamma$: $1 + 2\phi^2$
- $\sigma_0$: $2\phi + \phi^2 h$
- $\sigma_1$: $2\phi + \phi^2 h$
- $L_+$: $\phi^2$
- $L_-$: $\phi^2$

The equal Hopf link content ($L_+ = L_- = \phi^2$) implies zero chirality. The net valuation is $(1 + 2\phi)^2 + 2\phi^2 h$. Fitting this to $E_{\mathrm{pair}} = 2m_e$ gives $\phi = 0.0487$. This value is a fit to the measured electron mass, not a derivation.

**Circular (orthogonal) polarization:**
Take orthogonal polarization, $\varphi_0 = s$, $\varphi_1 = 0$, $\psi_0 = 0$, $\psi_1 = s$.
- $\gamma$: $1$
- $\sigma_0$: $s$
- $\sigma_1$: $s$
- $L_+$: $s^2$
- $L_-$: $0$

Only $L_+$ appears ($L_- = 0$). This produces maximally chiral Hopf content. The Hecke self-energy vanishes ($\varphi_0\psi_0 = \varphi_1\psi_1 = 0$). The net valuation is $(1 + s)^2$. Fitting this to $E_{\mathrm{pair}} = 2m_e$ gives $s = 0.0978$. This value is a fit, not a derivation.

Both fits close the $1.6\%$ energy gap by construction, so closing it is not evidence for either model. The color weight generates Hopf link content $L_\pm$ that supplies the missing pair production energy. The asymmetry $L_+ \neq L_-$ in the circular model acts as the categorical expression of photon helicity.

#### Four-term extension

Activating $\varphi_{01} \neq 0$ recovers the full photon. The product of two photons spans all six normal-form words. Its $e^-$ (trefoil) coefficient is

$$
  \varphi_{01}\psi_0 + \varphi_1\psi_{01},
$$

so the trefoil channel needs the vertex term of one photon and a single-crossing term of the other. For the eigenvalue-pair weights $\gamma(0, 0, qh)\,\gamma(0, 0, -q^{-1}h) = (\sigma_0\sigma_1^{-1})^3$ ([Borromean two-photon factorisation](#prop:borromean-two-photon-factorisation)) that coefficient is zero. The 6-term normal form is in [the $\gamma\gamma$ generation proposition](#prop:gamma-gamma-generates-particles). The coefficients are recomputed exactly over $\mathbb{Q}(q)$.
