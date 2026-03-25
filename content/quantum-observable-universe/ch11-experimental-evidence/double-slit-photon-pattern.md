A photon is *not* a $q$-harmonic form: it is background flux on the
exceptional divisor $E_p \cong \mathbb{P}^1(\mathbb{C})$
([exceptional divisor](#def:exceptional-divisor)).  Its phase is
governed by the [chiral sector coordinates](#def:chiral-sector-coords)
$(\phi, \psi)$ rather than by the $q$-Laplacian.

For a photon traversing path $\gamma_i$ through slit $i$, the
accumulated phase is the chiral twist along the path:

$$
  \Phi_{\mathrm{photon}}^{(i)}(y)
  \;=\; \psi_i(y) + q\,\phi_i(y),
$$

where $\phi_i(y)$ and $\psi_i(y)$ are the polar and azimuthal sector
coordinates traced by the exceptional-divisor fibre along $\gamma_i$.
The factor $q\phi$ is the *chiral twist* --- each sector rotates by
$q$ full turns as latitude runs from $0$ to $\pi$.

The photon interference at scattering angle $\theta$ is

$$
  I_{\mathrm{photon}}(\theta)
  \;=\; 4\,I_0\;\cos^2\!\!\left(
          \frac{q\,d\sin\theta}{2\,R_{\mathbb{P}^1}}
        \right)
        \;\cdot\; \mathcal{E}_J(\theta),
$$

where $R_{\mathbb{P}^1}$ is the radius of the exceptional divisor and
$\mathcal{E}_J(\theta)$ is the *Julia-set envelope*:

$$
  \mathcal{E}_J(\theta)
  \;=\; \mu_J\!\!\left(\left\{
          z \in S^1 \;:\;
          \bigl|f_q^{\,n}(z)\bigr|
          \;\leq\;
          \frac{a\sin\theta}{R_{\mathbb{P}^1}}
          \;\text{for all } n \geq 0
        \right\}\right),
$$

with $f_q \colon S^1 \to S^1$ the degree-$2$ endomorphism from the
$q$-deformed Reeb flow restricted to the equatorial circle
([Julia-set photon scattering](#rem:julia-s1-photon-scatter)), and
$\mu_J$ the harmonic measure on $\partial\mathcal{K}(f_q)$.

The Julia-set envelope $\mathcal{E}_J$ differs fundamentally from the
smooth sinc${}^2$ of Fraunhofer diffraction:

- Its support has **Hausdorff dimension** $d_H$ satisfying
  $1 < d_H < 2$, depending on $q$;
- The **central peak** is *narrower* than the Airy prediction,
  because the fractal boundary concentrates measure near $\theta = 0$;
- The **subsidiary maxima** are *more suppressed* than the
  $1/(m\pi)^2$ fall-off of Airy theory, because orbits of $f_q$ escape
  faster at large angles;
- The **tails** decay as a *power law*
  $\mathcal{E}_J(\theta) \sim |\theta|^{-d_H}$
  rather than as $|\theta|^{-2}$, giving broader wings than the
  textbook prediction.

At $q \to 1$: $f_q$ becomes the identity, $J(f_q)$ collapses,
$\mathcal{E}_J \to \mathrm{sinc}^2$, and the standard Airy pattern
is recovered.
