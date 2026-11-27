Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q \in k^{\times}$ ([substrate parameter](#def:substrate-parameter)), and let $\gamma_i$ ($i = 1,2$) be two paths through slits of width $a$ separated by distance $d$.

For a massive excitation of rest mass $m$, the spatial wavelength is not an external optical parameter; it is forced by Lorentz covariance of the internal meridian clock. In its rest frame, the excitation ticks at the Compton angular frequency $\omega_0 = m c^2 / \hbar$ of the exceptional-divisor meridian cycle ([meridian Compton tick](#rem:meridian-exceptional-divisor-note)). Following Louis de Broglie (1924), boosting along the beam axis at velocity $v$ with Lorentz factor $\gamma^2(1 - v^2 / c^2) = 1$ transforms proper time as $\tau_{\mathrm{prop}} = \gamma(t - v x / c^2)$ and decomposes the invariant clock phase into temporal and spatial components:

$$
  \omega_0 \tau_{\mathrm{prop}}
  = \frac{E t - p x}{\hbar},
  \qquad
  E = \gamma m c^2,
  \qquad
  p = \gamma m v,
  \qquad
  E^2 - (p c)^2 = (m c^2)^2.
$$

The spatial gradient fixes the relativistic de Broglie wavenumber $k_{\mathrm{dB}} = p / \hbar$ and wavelength $\lambda_{\mathrm{dB}} = 2\pi\hbar / p = h / (\gamma m v)$, with phase velocity $E / p$ satisfying $(E / p)\,v = c^2$.

Along each slit trajectory $\gamma_i$, the [$q$-exterior derivative](#def:categorical-q-ext-deriv) $d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d$ splits the accumulated **$q$-deformed path phase** into horizontal and vertical parts:

$$
  \Phi_q^{(i)}(y)
  = \frac{1}{\hbar_q}\!\int_{\gamma_i}\! d_q\psi
  = q^{-1}\Phi_{\mathrm{geom}}^{(i)}(y)
      + (1 - q^{-1})\Phi_{\mathrm{Reeb}}^{(i)}(y),
$$

where:

- $\Phi_{\mathrm{geom}}^{(i)}(y) = (2\pi / \lambda_{\mathrm{dB}})\,\ell_i(y)$ is the horizontal de Broglie geometric phase along path length $\ell_i(y)$,
- $\Phi_{\mathrm{Reeb}}^{(i)}(y) = \int_{\gamma_i} \iota_\xi\varTheta$ is the vertical [Reeb phase](#def:categorical-reeb), and
- $\hbar_q = 1 - q^{-1}$ is the [quantum Planck constant](#def:quantum-planck-constant).

Subtracting the two paths at scattering angle $\theta$ gives the $q$-deformed interference phase difference

$$
  \Delta\Phi_q(y)
  = \Phi_q^{(1)}(y) - \Phi_q^{(2)}(y)
  = q^{-1}\frac{2\pi d\sin\theta}{\lambda_{\mathrm{dB}}}
      + (1 - q^{-1})\Delta\phi_\xi(y)
  = \frac{2\pi d\sin\theta}{\lambda_q}
      + (1 - q^{-1})\Delta\phi_\xi(y),
$$

where $\Delta\phi_\xi(y)$ is the Reeb phase mismatch and $\lambda_q = q\lambda_{\mathrm{dB}}$ is the stretched effective fringe wavelength. At detector distance $L$, the horizontal $q^{-1}$ factor stretches the Young fringe spacing to $\Delta y_q = q\lambda_{\mathrm{dB}} L / d$, whereas the $q^{-2}\Delta$ classical Hodge core of the [$q$-Laplacian expansion](#rem:q-laplacian-expansion) broadens the single-slit diffraction envelope by $q^2$ for controlled comparison with relativistic $600\;\mathrm{eV}$ electron interferometry \cite{bach2013}. At $q = 1$, the Reeb mismatch vanishes and $\lambda_q$ reduces to $\lambda_{\mathrm{dB}}$.
