Let $\alpha$ be a massive $q$-harmonic form ([particle](#def:q-harmonic-form)) with de Broglie wavelength $\lambda$. It is incident on a double slit of width $a$ and separation $d$. A detector screen sits at distance $L$. The $q$-deformed intensity at scattering angle $\theta$ is

$$
  I_q(\theta)
  =  4I_0\cos^2\!\!\left(\frac{\Delta\Phi_q(\theta)}{2}\right)
        \cdot
        \left(\frac{\sin\beta_q(\theta)}{\beta_q(\theta)}\right)^{\!2}.
$$

The interference phase, derived from the [$q$-deformed path phase](#def:double-slit-q-phase), is

$$
  \Delta\Phi_q(\theta)
  =  q^{-1}\frac{2\pid\sin\theta}{\lambda}
        +  (1 - q^{-1})\Delta\phi_\xi(\theta).
$$

The envelope parameter is

$$
  \beta_q(\theta)
  =  q^{-1}\frac{\pia\sin\theta}{\lambda}
        +  (1 - q^{-1})^2\beta_\xi(\theta),
$$

where $\beta_\xi(\theta)$ is the contribution from the spin-core term of the [$q$-Laplacian expansion](#rem:q-laplacian-expansion).

The $q$-Laplacian separates into three scales:

- **Classical core** ($\propto q^{-2}$): Standard Hodge diffusion $\Delta$. This yields the Fraunhofer sinc${}^2$ envelope.
- **Spin core** ($\propto (1 - q^{-1})^2$): Pure Reeb dynamics $\Delta_\xi$. This adds an angular broadening $\beta_\xi$ to the envelope.
- **Cross-coupling** ($\propto q^{-1}(1 - q^{-1})$): The terms $d(\mathcal{L}_\xi^*\iota_\xi) + (\varTheta \wedge \mathcal{L}_\xi)\delta + \delta(\varTheta \wedge \mathcal{L}_\xi) + (\mathcal{L}_\xi^*\iota_\xi)d$. These mix spatial and Reeb modes, producing the interference fringes.

The fringe spacing on the screen is $q$-corrected:

$$
  \Delta y_q =  \frac{q\lambdaL}{d}.
$$

The envelope half-width is broadened relative to the Fraunhofer prediction:

$$
  w_q =  \frac{q^2\lambdaL}{a}
        \left(1 +  (1 - q^{-1})^2
        \frac{\langle\Delta_\xi\rangle}{\langle\Delta\rangle}\right),
$$

where $\langle\Delta_\xi\rangle / \langle\Delta\rangle$ is the ratio of Reeb to spatial Laplacian eigenvalues on the particle's harmonic mode.

At $q = 1$, we have $\Delta\Phi_1 = 2\pi d\sin\theta/\lambda$ and $\beta_1 = \pi a\sin\theta/\lambda$. The standard Fraunhofer double-slit pattern is recovered exactly. For $q \neq 1$, the envelope is wider than the Fraunhofer envelope by a factor of order $(1 - q^{-1})^2$. This is consistent with the systematic excess width observed in precision electron and molecular diffraction experiments \cite{bach2013}.
