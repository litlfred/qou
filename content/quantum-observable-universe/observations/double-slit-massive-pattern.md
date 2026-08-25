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

At $q = 1$, we recover the Fraunhofer pattern. For $q \neq 1$, the envelope widens, matching precision observations \cite{bach2013}.
