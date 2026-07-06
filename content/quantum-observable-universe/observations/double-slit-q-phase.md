Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q \in k^{\times}$ ([substrate parameter](#def:substrate-parameter)). Let $\gamma_i$ ($i = 1,2$) be two paths from a source to a screen position $y$. Each path passes through one slit of width $a$. The slits are separated by distance $d$.

The $q$-deformed path phase accumulated along $\gamma_i$ is

$$
  \Phi_q^{(i)}(y)
  =  \frac{1}{\hbar_q}\!\int_{\gamma_i}\! d_q\psi
  =  q^{-1}\Phi_{\mathrm{geom}}^{(i)}(y)
        +  (1 - q^{-1})\Phi_{\mathrm{Reeb}}^{(i)}(y).
$$

The terms are:

- $\Phi_{\mathrm{geom}}^{(i)} = (2\pi/\lambda)\ell_i(y)$: The geometric (de Broglie) phase. $\ell_i(y)$ is the Euclidean path length through slit $i$ to screen point $y$.
- $\Phi_{\mathrm{Reeb}}^{(i)} = \int_{\gamma_i} \iota_\xi\varTheta$: The Reeb phase. This is the rotation accumulated by the internal color fibre along $\gamma_i$ ([Reeb derivation](#def:categorical-reeb)).
- $\hbar_q = 1 - q^{-1}$: The [quantum Planck constant](#def:quantum-planck-constant).

This decomposition follows directly from the [$q$-exterior derivative](#def:categorical-q-ext-deriv) $d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d$. It splits every phase integral into a horizontal (geometric) part weighted by $q^{-1}$ and a vertical (Reeb) part weighted by $1 - q^{-1}$.

The $q$-deformed phase difference between the two paths is

$$
  \Delta\Phi_q(y)
  =  \Phi_q^{(1)}(y) - \Phi_q^{(2)}(y)
  =  q^{-1}\frac{2\pid\sin\theta}{\lambda}
        +  (1 - q^{-1})\Delta\phi_\xi(y).
$$

Here $\theta$ is the scattering angle and $\Delta\phi_\xi(y) = \Phi_{\mathrm{Reeb}}^{(1)}(y) - \Phi_{\mathrm{Reeb}}^{(2)}(y)$ is the Reeb phase mismatch. At $q = 1$, the Reeb term vanishes, recovering the standard Young phase difference.
