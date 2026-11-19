Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with aether parameter $q \in k^{\times}$ ([aether parameter](#def:substrate-parameter)). Let $\gamma_i$ ($i = 1,2$) be two paths through slits of width $a$ separated by distance $d$.

The **$q$-deformed path phase** along $\gamma_i$ is

$$
  \Phi_q^{(i)}(y)
  =  \frac{1}{\hbar_q}\!\int_{\gamma_i}\! d_q\psi
  =  q^{-1}\Phi_{\mathrm{geom}}^{(i)}(y)
        +  (1 - q^{-1})\Phi_{\mathrm{Reeb}}^{(i)}(y).
$$

The terms are:

- $\Phi_{\mathrm{geom}}^{(i)} = (2\pi/\lambda)\ell_i(y)$: The geometric phase.
- $\Phi_{\mathrm{Reeb}}^{(i)} = \int_{\gamma_i} \iota_\xi\varTheta$: The Reeb phase ([Reeb derivation](#def:categorical-reeb)).
- $\hbar_q = 1 - q^{-1}$: The [quantum Planck constant](#def:quantum-planck-constant).

This decomposition stems from the [$q$-exterior derivative](#def:categorical-q-ext-deriv) $d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d$.

The $q$-deformed phase difference is

$$
  \Delta\Phi_q(y)
  =  \Phi_q^{(1)}(y) - \Phi_q^{(2)}(y)
  =  q^{-1}\frac{2\pi d\sin\theta}{\lambda}
        +  (1 - q^{-1})\Delta\phi_\xi(y).
$$

Here $\theta$ is the scattering angle and $\Delta\phi_\xi(y)$ is the Reeb phase mismatch. At $q = 1$, the Reeb term vanishes.
