This analytical plotter evaluates the interference intensity envelope for the $q$-deformed double-slit geometry across two scattering modes:

1. **Mode 1 (Massive particle)**: $q$-harmonic form scattering.
2. **Mode 2 (Photon)**: Julia-set envelope scattering.

**Default view and parameter-free vacuum prediction**: For the $600\;\mathrm{eV}$ electron diffraction data of Roger Bach, Damian Pope, Sy-Hwang Liou, and Herman Batelaan (2013) \cite{bach2013} through gold-coated silicon slits, the [local aether $q$](#prop:local-aether-q) profile relaxes to $q_{\mathrm{local}}(y) \to 1$ in exterior vacuum and departs from unity only within the evanescent Yukawa or Compton boundary layers of the two slit walls at $y = \pm a / 2$:

$$
  q_{\mathrm{local}}(y) - 1
  = \Delta q_{\mathrm{wall}}
    \Bigl(e^{-(a/2 - y)/\ell} + e^{-(a/2 + y)/\ell}\Bigr),
  \qquad
  \langle q_{\mathrm{local}} - 1 \rangle_a
  = \Delta q_{\mathrm{wall}}\,\frac{2\ell}{a}\bigl(1 - e^{-a/\ell}\bigr).
$$

Even at the saturating hadronic-core upper bound $\Delta q_{\mathrm{wall}} = q_0 - 1 \approx 0.1100$, integrating across the $a = 50\;\mathrm{nm}$ slit aperture yields

$$
  \langle q_{\mathrm{local}} - 1 \rangle_{a=50\,\mathrm{nm}}^{(\pi)}
  \approx 6.22 \times 10^{-9}
  \quad\bigl(\ell = r_\pi = \hbar c / m_{\pi^\pm} \approx 1.4138\;\mathrm{fm}\bigr),
$$

$$
  \langle q_{\mathrm{local}} - 1 \rangle_{a=50\,\mathrm{nm}}^{(e)}
  \approx 1.70 \times 10^{-6}
  \quad\bigl(\ell = \bar{\lambda}_{C,e} = \hbar c / m_e \approx 386.16\;\mathrm{fm}\bigr),
$$

with electromagnetic vertex projection reducing the electronic tail further to $3.29 \times 10^{-10}$ (and $5.02 \times 10^{-9}$ to $1.37 \times 10^{-6}$ at the $a = 62\;\mathrm{nm}$ physical mask width). The resulting parameter-free fractional Young fringe shift $\delta\Delta y / \Delta y = \langle q_{\mathrm{local}} - 1 \rangle_a \le 1.70 \times 10^{-6}$ and single-slit Hodge envelope shift $\langle q_{\mathrm{local}}^2 - 1 \rangle_a \le 3.40 \times 10^{-6}$ coincide with the $q = 1$ Fraunhofer curve well below percent-level experimental resolution; interactive slider settings $q > 1$ illustrate hypothetical macroscopic deformations.

**Parameters**:

- $q$ --- aether parameter ($q = 1$ in exterior vacuum; slider explores illustrative $q > 1$ deformations)
- $a$ --- slit width
- $d$ --- slit separation
- $\lambda$ --- de Broglie wavelength
- $r_\xi$ --- Reeb coupling ratio
