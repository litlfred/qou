Interactive 3D visualisation of the Brings-surface cover
$\pi \colon \Sigma_4 \to \mathbb{P}^1(\mathbb{C})$ on the **Riemann sphere**.

**Geometry.**  The base $\mathbb{P}^1 \cong S^2$ is shown as a sphere.
The brane lives on the **interior** of the sphere (the filled 3-ball).
The three color tubes (sheets of the cover) live on the **exterior** of
the sphere — at radius $R_{\text{brane}} + \Delta R$ — so they never
pierce spacetime.

**Parameterisation.**  For $z \in [0, \infty] = \mathbb{P}^1(\mathbb{R})$,
the meridian $\theta(z) \in [0,\pi]$ traces the sphere from pole to pole.
At each meridian point, the three cover sheets are placed at azimuthal
angles $\varphi_k(z) = \arg c_k(z)$:

$$
  \text{sheet}_k(z) = \bigl((R_b+\Delta R)\sin\theta\cos\varphi_k,\; (R_b+\Delta R)\cos\theta,\; (R_b+\Delta R)\sin\theta\sin\varphi_k\bigr).
$$

**Exceptional divisors.**  At the two poles $\theta = 0$ (z=0) and
$\theta = \pi$ (z=∞), $\sin\theta \to 0$ so all three color tubes
converge to the *same* point.  These are the **exceptional divisors**
— the loci where the brane (interior) and color sheets (exterior)
meet.  They are the ramification points of $\pi$ at $z=0$ and
$z=\infty$.

| Tube | Color coordinate | Resolvent |
|------|-----------------|-----------|
| Red  | $c_r = w_2 - z$ | $w_2 = \tfrac{1}{\sqrt5}\sum_j \zeta^{2j}x_j$ |
| Green | $c_g = w_3 - z$ | $w_3 = \tfrac{1}{\sqrt5}\sum_j \zeta^{3j}x_j$ |
| Blue | $c_b = w_4 - z$ | $w_4 = \tfrac{1}{\sqrt5}\sum_j \zeta^{4j}x_j$ |

where $x_2, x_3, x_4$ are the three roots of the Brings fiber cubic
$$
  t^3 + (1{+}z)\,t^2 + (1{+}z{+}z^2)\,t + (1{+}z)(1{+}z^2) = 0
$$
at each point $z$.

**Base scaling.**  Four modes map $z \in [0, \infty]$ to $\theta \in [0,\pi]$:

| Mode | Mapping | Behaviour |
|------|---------|-----------|
| arctan | $\theta \propto \arctan z$ | Compactifies $\infty$; projective |
| log | $\theta \propto \ln(1+z)$ | Moderate compression |
| $\sqrt{z}$ | $\theta \propto \sqrt{z}$ | Emphasises small $z$ |
| linear | $\theta \propto z$ | Affine |

**Torsion parameter $q$.**  The substrate parameter rotates the sheets
by $(q - q^{-1})\cdot z \cdot \text{rate}$, shifting the secondary (blue)
collision markers along the sphere while leaving the two pole divisors
fixed.
