Interactive 3D visualisation of quaternionic spectral resolvent coordinates on Bring's surface (§3.1).

The simulator renders the four $\beta$-branches of the spectral resolvent in $\omega$-coordinates using Three.js WebGL:

- $\beta_1 = \pi - 3\alpha$ (blue)
- $\beta_2 = (\pi + \alpha)/3$ (red-orange)
- $\beta_3 = (3\pi + \alpha)/3$ (green)
- $\beta_4 = (5\pi + \alpha)/3$ (orange-yellow)

**Default view**: Standard resolvent with $N = 18$ $q$-series terms, moderate grid density, and $\omega$-coordinate projection. Auto-rotation enabled for an overview of the surface topology.

**Parameters**:

- $r_{\min}$, $r_{\max}$ — radial range for the resolvent.
- $\delta r$, $\delta\zeta$ — grid density (radial and angular).
- $N$ — $q$-series truncation precision (number of terms).
- Projection mode: $\omega$-coords, $+\mathrm{Sp}(1)$ rotation, or raw $x_j$.

Growth factor profiles and Weierstrass curve data appear in auxiliary panels.
