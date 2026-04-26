The $q$-deformed Reeb flow $\phi_t^q$
([$q$-Reeb flow](#ex:q-reeb-flow)) restricted to the exceptional
divisor $\mathcal{S}_c \cong \mathbb{P}^1(\mathbb{C})$
([Reeb on exceptional divisor](#rem:reeb-exceptional-divisor))
generates a discrete dynamical system whose Julia set encodes
the photon diffraction envelope.

**The iteration.**
The substrate parameter $q$ drives the main-cardioid
parameterization of the Mandelbrot set:

$$
  c(q) =  \tfrac{1}{2}e^{2\pi i q}
  - \tfrac{1}{4}e^{4\pi i q}.
$$

The associated quadratic map $f_q(z) = z^2 + c(q)$ is the
discrete-time skeleton of the continuous Reeb flow: each iteration
of $f_q$ corresponds to one full circuit of the $U(1)$ fiber above
$\mathcal{S}_c$.  The **Julia set** $J(f_q) \subset \mathbb{C}$ is the
boundary between orbits that escape and orbits that remain bounded
— the fractal frontier of the Reeb dynamics.

**Photon envelope.**
Photons propagate as exceptional-divisor flux, not as
$q$-harmonic forms.  Their diffraction envelope is not the
sinc${}^2$ of massive particles but the **Julia-set measure**
$\mu_J$: the natural invariant measure on $J(f_q)$.
The Hausdorff dimension $d_H = d_H(q)$ of $J(f_q) \cap S^1$
governs the power-law tails of the photon envelope, replacing the
$|\varTheta|^{-2}$ falloff of classical Airy diffraction with
$|\varTheta|^{-d_H}$.

**Julia set at the golden ratio.**
At the golden threshold $q_{\mathrm{gold}} = 1/\varphi^2 \approx 0.382$, the effective angle on the main cardioid is

$$
  \varTheta_{\mathrm{gold}}
  =  2\pi/\varphi^2
   \approx  137.5°
$$

— the **golden angle**.  This is the most irrational angle: its
continued fraction $[0; 1, 1, 1, \ldots]$ converges slower than any
other.  At this rotation number, the Julia set $J(f_{q_{\mathrm{gold}}})$
develops a **Siegel disk boundary** — the richest fractal structure
among cardioid parameters, because the golden rotation number is
hardest to linearize (the small denominators in the linearization
series are as large as possible).

**Julia set at the reciprocal $q_{\mathrm{gold}}^{-1} = \varphi^2$.**
At the reciprocal, $\varphi^2 = \varphi + 1$, so the effective
angle is

$$
  2\pi\varphi^2 \bmod 2\pi
  =  2\pi(\varphi^2 - 2)
  =  2\pi/\varphi
   \approx  222.5°,
$$

the **golden complement** ($360° - 137.5°$).  By the symmetry of the
cardioid parameterization, the Julia set at $q = \varphi^2$ has the
**same Hausdorff dimension** as at $q = 1/\varphi^2$:

$$
  d_H(\varphi^2) =  d_H(1/\varphi^2).
$$

**The asymmetry: Julia meets fiber.**
The Julia set is symmetric under $q \leftrightarrow 1/q$ (via the
complementary golden angle), but the elliptic fiber is not:

| | $q = 1/\varphi^2$ | $q = \varphi^2$ |
|---|---|---|
| **Elliptic fiber $\mathcal{E}_q$** | Singular (node) | Smooth ($\Delta = -200$, $j = 160$) |
| **Julia set** | Siegel boundary, maximal $d_H$ | Same $d_H$ (golden complement) |
| **Reeb flow** | No smooth carrier | Strong torsion, deep quantum |
| **Physics** | No stable chiral structure | Stable; Big Bang territory |

At $q = \varphi^2$: the photon envelope has its richest fractal
structure (same $d_H$ as at the golden threshold), but the Reeb
bundle retains a smooth elliptic fiber.  This is the deep-quantum
regime — maximal fractal diffraction with stable chiral geometry.

**Information-theoretic content.**
The Hausdorff dimension $d_H(q)$ measures the **information density**
of the photon envelope: higher $d_H$ means the diffraction pattern
encodes more structure per unit angle.  The golden angle maximizes
$d_H$ because the Fibonacci convergents of $1/\varphi$ are the
worst rational approximants — the iteration $f_q$ cannot lock into
any periodic orbit, forcing the dynamics to explore the full
complexity of the Julia set.  This connects directly to the
golden-angle phyllotaxis of the Bring's surface
([golden ratio degeneration](#rem:golden-ratio-degeneration)):
the same irrationality that optimizes packing on surfaces
maximizes the information content of photon scattering.

The experimental discriminant is the ratio of photon-to-electron
envelope widths at the same slit geometry:

$$
  \frac{w_{\mathrm{photon}}}{w_{\mathrm{electron}}}
  = 
  \frac{d_H}{2}
  \bigl(1 + (1 - q^{-1})^2
  \langle\Delta_\xi\rangle_e / \langle\Delta\rangle_e\bigr).
$$

This ratio depends only on $q$ (not slit width or wavelength),
providing a sharp test of the Julia-set envelope prediction.
