Let $\alpha$ be a massive $q$-harmonic form ([particle](#def:q-harmonic-form)) incident on a double slit. The $q$-deformed intensity at scattering angle $\theta$ is

$$
  I_q(\theta)
  =  4I_0\cos^2\!\!\left(\frac{\Delta\Phi_q(\theta)}{2}\right)
        \cdot
        \left(\frac{\sin\beta_q(\theta)}{\beta_q(\theta)}\right)^{\!2}.
$$

The interference phase is

$$
  \Delta\Phi_q(\theta)
  =  q^{-1}\frac{2\pi d\sin\theta}{\lambda}
        +  (1 - q^{-1})\Delta\phi_\xi(\theta).
$$

The envelope parameter is

$$
  \beta_q(\theta)
  =  q^{-1}\frac{\pi a\sin\theta}{\lambda}
        +  (1 - q^{-1})^2\beta_\xi(\theta).
$$

The term $\beta_\xi(\theta)$ is the spin-core contribution of the [$q$-Laplacian expansion](#rem:q-laplacian-expansion).

The $q$-Laplacian separates into three scales:

- **Classical core** ($\propto q^{-2}$): Standard Hodge diffusion $\Delta$.
- **Spin core** ($\propto (1 - q^{-1})^2$): Pure Reeb dynamics $\Delta_\xi$.
- **Cross-coupling** ($\propto q^{-1}(1 - q^{-1})$): Mixes spatial and Reeb modes.

The fringe spacing is

$$
  \Delta y_q =  \frac{q\lambda L}{d}.
$$

The envelope half-width broadens:

$$
  w_q =  \frac{q^2\lambda L}{a}
        \left(1 +  (1 - q^{-1})^2
        \frac{\langle\Delta_\xi\rangle}{\langle\Delta\rangle}\right).
$$

At $q = 1$, this recovers the classical Fraunhofer pattern. In the $600\;\mathrm{eV}$ single-electron double-slit buildup experiment of Roger Bach, Damian Pope, Sy-Hwang Liou, and Herman Batelaan \cite{bach2013} ($a = 50\;\mathrm{nm}$, $d = 280\;\mathrm{nm}$, relativistic $\lambda_{\mathrm{dB}} \approx 50.05\;\mathrm{pm}$, $6{,}235$ electrons across the central five interference orders), an electrostatic quadrupole lens magnifies the pattern without an independent angular scale bar, making the dimensionless envelope-to-fringe ratio $w_q / \Delta y_q \ge q(d/a)$ and the order-$m$ peak modulation $I_q(\theta_m)/I_q(0) = \mathrm{sinc}^2(m\pi a / (q d))$ the magnification-invariant observables. Under the local vacuum profile $q_{\mathrm{local}}(y) \to 1$, the aperture-averaged departure $\langle q_{\mathrm{local}} - 1 \rangle_a \le 1.70 \times 10^{-6}$ across $a = 50\;\mathrm{nm}$ agrees with $q = 1$ Fraunhofer to better than $8.1 \times 10^{-6}$ pointwise and predicts $I(\theta_{\pm 2})/I(0) = \mathrm{sinc}^2(5\pi/14) \approx 0.6448$ against the digitized Figure 3e mean $m = \pm 2$ peak height $0.6552$ ($1.58\%$ difference), whereas a uniform exterior $q = q_0 \approx 1.1100$ would lift $I_{q_0}(\theta_{\pm 2})/I_{q_0}(0)$ to $0.7026$ and stretch the physical fringe spacing $\Delta\theta_{q_0} = q_0\lambda_{\mathrm{dB}}/d$ by $+11.00\%$.
