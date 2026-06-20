*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $\alpha$ be a massive $q$-harmonic form
([particle](#def:q-harmonic-form)) with de Broglie wavelength $\lambda$,
incident on a double slit of width $a$ and separation $d$, with
detector screen at distance $L$.  The $q$-deformed intensity at
scattering angle $\theta$ is

$$
  I_q(\theta)
  =  4I_0\cos^2\!\!\left(\frac{\Delta\Phi_q(\theta)}{2}\right)
        \cdot
        \left(\frac{\sin\beta_q(\theta)}{\beta_q(\theta)}\right)^{\!2},
$$

where the *interference phase* is

$$
  \Delta\Phi_q(\theta)
  =  q^{-1}\frac{2\pid\sin\theta}{\lambda}
        +  (1 - q^{-1})\Delta\phi_\xi(\theta)
$$

from the [$q$-deformed path phase](#def:double-slit-q-phase), and the
*envelope parameter* is

$$
  \beta_q(\theta)
  =  q^{-1}\frac{\pia\sin\theta}{\lambda}
        +  (1 - q^{-1})^2\beta_\xi(\theta),
$$

with $\beta_\xi(\theta)$ the contribution from the spin-core term of
the [$q$-Laplacian expansion](#rem:q-laplacian-expansion).

The $q$-Laplacian separates into three scales:

- **Classical core** ($\propto q^{-2}$):
  standard Hodge diffusion $\Delta$, giving the Fraunhofer
  sinc${}^2$ envelope;
- **Spin core** ($\propto (1 - q^{-1})^2$):
  pure Reeb dynamics $\Delta_\xi$, adding an angular broadening
  $\beta_\xi$ to the envelope;
- **Cross-coupling** ($\propto q^{-1}(1 - q^{-1})$):
  the terms
  $d(\mathcal{L}_\xi^*\iota_\xi) + (\varTheta \wedge \mathcal{L}_\xi)\delta + \delta(\varTheta \wedge \mathcal{L}_\xi) + (\mathcal{L}_\xi^*\iota_\xi)d$
  that mix spatial and Reeb modes, producing the
  interference fringes.

The fringe spacing on the screen is $q$-corrected:

$$
  \Delta y_q =  \frac{q\lambdaL}{d},
$$

and the envelope half-width is broadened relative to Fraunhofer:

$$
  w_q =  \frac{q^2\lambdaL}{a}
        \left(1 +  (1 - q^{-1})^2
        \frac{\langle\Delta_\xi\rangle}{\langle\Delta\rangle}\right),
$$

where $\langle\Delta_\xi\rangle / \langle\Delta\rangle$ is the ratio
of Reeb to spatial Laplacian eigenvalues on the particle's harmonic
mode.

At $q = 1$: $\Delta\Phi_1 = 2\pi d\sin\theta/\lambda$,
$\beta_1 = \pi a\sin\theta/\lambda$, and the standard Fraunhofer
double-slit pattern is recovered exactly.  For $q \neq 1$ the
envelope is *wider* than Fraunhofer by a factor of order
$(1 - q^{-1})^2$, consistent with the systematic excess width
observed in precision electron and molecular diffraction experiments
\cite{bach2013}.
