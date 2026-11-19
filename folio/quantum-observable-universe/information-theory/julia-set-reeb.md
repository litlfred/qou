The $q$-deformed Reeb flow $\phi_t^q$ ([$q$-Reeb flow](#ex:q-reeb-flow)) restricted to the exceptional divisor $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$ ([Reeb on exceptional divisor](#rem:reeb-exceptional-divisor)) generates a discrete dynamical system. Its Julia set encodes the photon diffraction envelope.

**The iteration.**
The aether parameter $q$ drives the main-cardioid parameterization of the Mandelbrot set:

$$
  c(q) =  \tfrac{1}{2}e^{2\pi i q}
  - \tfrac{1}{4}e^{4\pi i q}.
$$

The associated quadratic map $f_q(z) = z^2 + c(q)$ acts as the discrete-time skeleton of the continuous Reeb flow. Each iteration of $f_q$ corresponds to one full circuit of the $U(1)$ fiber above $\mathcal{S}_c$. The **Julia set** $J(f_q) \subset \mathbb{C}$ marks the boundary between escaping orbits and bounded orbits. It is the fractal frontier of the Reeb dynamics.

**Photon envelope.**
Photons propagate as exceptional-divisor flux rather than as $q$-harmonic forms. Their diffraction envelope follows the **Julia-set measure** $\mu_J$ (the natural invariant measure on $J(f_q)$), rather than the sinc${}^2$ distribution of massive particles. The Hausdorff dimension $d_H = d_H(q)$ of $J(f_q) \cap S^1$ governs the power-law tails of the photon envelope. It replaces the $|\varTheta|^{-2}$ falloff of classical Airy diffraction with $|\varTheta|^{-d_H}$.

**Julia set at the golden ratio.**
At the golden threshold $q_{\mathrm{gold}} = 1/\varphi^2 \approx 0.382$, the effective angle on the main cardioid is

$$
  \varTheta_{\mathrm{gold}}
  =  2\pi/\varphi^2
   \approx  137.5°
$$

This is the **golden angle**. It is the most irrational angle. Its continued fraction $[0; 1, 1, 1, \ldots]$ converges slower than any other. At this rotation number, the Julia set $J(f_{q_{\mathrm{gold}}})$ develops a **Siegel disk boundary**. This yields the richest fractal structure among cardioid parameters. The golden rotation number is the hardest to linearize because the small denominators in the linearization series are maximally large.

**Julia set at the reciprocal $q_{\mathrm{gold}}^{-1} = \varphi^2$.**
At the reciprocal, $\varphi^2 = \varphi + 1$. The effective angle is

$$
  2\pi\varphi^2 \bmod 2\pi
  =  2\pi(\varphi^2 - 2)
  =  2\pi/\varphi
   \approx  222.5°,
$$

which is the **golden complement** ($360° - 137.5°$). The cardioid parameterization is symmetric, so the Julia set at $q = \varphi^2$ has the **same Hausdorff dimension** as at $q = 1/\varphi^2$:

$$
  d_H(\varphi^2) =  d_H(1/\varphi^2).
$$

**The asymmetry: Julia meets fiber.**
The Julia set is symmetric under $q \leftrightarrow 1/q$ (via the complementary golden angle), but the elliptic fiber is not.

| | $q = 1/\varphi^2$ | $q = \varphi^2$ |
|---|---|---|
| **Elliptic fiber $\mathcal{E}_q$** | Singular (node) | Smooth ($\Delta = -200$, $j = 160$) |
| **Julia set** | Siegel boundary, maximal $d_H$ | Same $d_H$ (golden complement) |
| **Reeb flow** | No smooth carrier | Strong torsion, deep quantum |
| **Physics** | No stable chiral structure | Stable; Big Bang territory |

At $q = \varphi^2$, the photon envelope exhibits its richest fractal structure (the same $d_H$ as the golden threshold), and the Reeb bundle retains a smooth elliptic fiber. This characterizes the deep-quantum regime: maximal fractal diffraction paired with stable chiral geometry.

**Information-theoretic content.**
The Hausdorff dimension $d_H(q)$ measures the **information density** of the photon envelope. A higher $d_H$ indicates that the diffraction pattern encodes more structure per unit angle. The golden angle maximizes $d_H$ because the Fibonacci convergents of $1/\varphi$ are the worst rational approximants. The iteration $f_q$ cannot lock into any periodic orbit. The dynamics must explore the full complexity of the Julia set. This directly connects to the golden-angle phyllotaxis of the Bring surface ([golden ratio degeneration](#rem:golden-ratio-degeneration)). The irrationality optimizing surface packing also maximizes the information content of photon scattering.

The experimental discriminant is the ratio of photon-to-electron envelope widths at identical slit geometries:

$$
  \frac{w_{\mathrm{photon}}}{w_{\mathrm{electron}}}
  = 
  \frac{d_H}{2}
  \bigl(1 + (1 - q^{-1})^2
  \langle\Delta_\xi\rangle_e / \langle\Delta\rangle_e\bigr).
$$

This ratio strictly depends on $q$ rather than on slit width or wavelength. It provides a sharp experimental test of the Julia-set envelope prediction.
