The Descartes elliptic curve $\mathcal{E}_q$ ([Descartes elliptic curve](#prop:descartes-elliptic-curve)) degenerates at a value of $q$ determined by the golden ratio.

With $s = \sqrt{q}$, the second Weierstrass coefficient factors as:

$$
  s^3 \cdot r(q)
  = 
  \frac{5(s^2 + s - 1)(4s^4 - s^3 - 4s^2 + s + 4)}{27}.
$$

The factor $(s^2 + s - 1)$ vanishes at:

$$
  s =  \frac{\sqrt{5} - 1}{2}
  =  \frac{1}{\varphi}
  =  \varphi - 1,
$$

where $\varphi = (1 + \sqrt{5})/2$ is the golden ratio. Since $q = s^2$, this yields the golden ratio threshold:

$$
  q_{\mathrm{gold}}
  =  \frac{1}{\varphi^2}
  =  \frac{3 - \sqrt{5}}{2}
   \approx  0.382.
$$

At $q = q_{\mathrm{gold}}$, the constant term $r(q)$ vanishes and the Weierstrass equation reduces to $y^2 = x^3 + p(q_{\mathrm{gold}})x = x(x^2 + p)$. The curve acquires a node at the origin. The smooth elliptic fiber pinches to a rational curve with a double point. The chiral fibration of Bring's surface loses its elliptic structure — the three color tubes $(r, g, b)$ collapse to a degenerate configuration where two roots coincide.

**Origin of the golden ratio.**

The polynomial $s^2 + s - 1$ is the minimal polynomial of $1/\varphi$ over $\mathbb{Q}$. Its appearance in the Weierstrass coefficient is mathematically rigid. The Bring's surface is defined by $\sum x_i = \sum x_i^2 = \sum x_i^3 = 0$ in $\mathbb{CP}^4$. The $S_5$ symmetry of this quintic acts on the Lagrange resolvents through fifth roots of unity $\zeta = e^{2\pi i/5}$. The golden ratio satisfies $\varphi = -2\cos(4\pi/5) = 2\cos(\pi/5)$, directly linking it to the $\zeta$-action on the color tube coordinates. The degeneration at $q = 1/\varphi^2$ occurs exactly when the substrate deformation resonates with the $S_5$ symmetry of Bring's surface.

**Physical significance.**

The golden ratio threshold divides the $(q, \chi)$ parameter space into three regimes:

| Regime | $q$ | $\mathcal{E}_q$ | Chiral structure | Nuclear stability |
| --- | --- | --- | --- | --- |
| Sub-golden | $q < 1/\varphi^2$ | singular | degenerate | no stable hadrons |
| Classical band | $1/\varphi^2 < q < 1$ | smooth | intact but sub-classical | symmetric nuclei ($n = p$) |
| Physical | $q > 1$ | smooth, $\Delta < 0$ | one real component | full nuclear chart |

The observed universe sits at $q = q_0$, well above the golden threshold. The distance from the degeneration,

$$
  q_0 - q_{\mathrm{gold}}
  =  1.110 - 0.382
  =  0.728,
$$

measures the stability margin of the Descartes universe. It quantifies how far the chiral elliptic fiber is from collapsing.

**The golden ratio in other contexts.**

The appearance of $\varphi$ in the Descartes universe connects to its role in related algebraic structures:

* **Penrose tilings**: $\varphi$ governs the quasicrystalline order of Penrose tilings. These are projections of the $A_4$ root lattice, which shares the $S_5$ symmetry underlying Bring's surface.
* **Fibonacci phyllotaxis**: The golden angle $2\pi/\varphi^2 \approx 137.5^\circ$ optimises packing on surfaces, reflecting the same algebraic constraint $(s^2 + s - 1 = 0)$ that governs the chiral degeneration.
* **$E_8$ and the icosahedron**: The golden ratio arises in the McKay correspondence for the icosahedral group (order $60$), which is $A_5 \cong S_5/\mathbb{Z}_2$ (the quotient of the symmetry group of Bring's surface by its centre).

The golden ratio is not an input to the QOU framework. It emerges strictly from the $S_5$ symmetry of the quintic and the requirement $\chi_{\mathrm{eu}}(M_0) = -6$.
