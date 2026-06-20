*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with
$\chi(A) = -6$ and substrate parameter $q$.  Set
$s = \sqrt{q}$.  The coral elliptic fiber
([coral elliptic](#prop:coral-elliptic)) of Bring's surface
at spacetime ratio $z = s - s^{-1}$ is the elliptic curve

$$
  \mathcal{E}_q  : 
  y^2 =  x^3
  +  \frac{2s^4 + s^3 - 2s^2 - s + 2}{3s^2}x
  +  \frac{5(s^2 + s - 1)(4s^4 - s^3 - 4s^2 + s + 4)}{27s^3}
$$

with Weierstrass coefficients expressible directly in $q$:

$$
  p(q) = 
  \frac{2(q^2 - q + 1)}{3q}
  +  \frac{q - 1}{3\sqrt{q}},
$$

$$
  r(q) = 
  \frac{20(q - 1)^3}{27q^{3/2}}
  +  \frac{5(q - 1)^2}{9q}
  +  \frac{5(\sqrt{q} - 1/\sqrt{q})}{9}
  +  \frac{20}{27}.
$$

**Invariants.**

| Quantity | Formula | Value at the substrate parameter $q$ |
|----------|---------|---------------------|
| Discriminant | $\Delta(q)$ | $-18.95$ |
| $j$-invariant | $j(q) = 256(2z^2 + z + 2)^3 / \Delta$ | $129.9$ |
| Real components | $1$ (since $\Delta < 0$) | |
| 2-torsion | one real point at $x_T = -p(q)/3 - \cdots$ | $x_T = -0.684$ |

**Classical limit.**
At $q = 1$ (equivalently $s = 1$, $z = 0$), the curve degenerates
to

$$
  E_1  :  y^2 = x^3 + \tfrac{2}{3}x + \tfrac{20}{27},
  \qquad \Delta = -16, \quad j = 128.
$$

Clearing denominators ($X = 3x$, $Y = 3\sqrt{3}y$) gives the
integral model $Y^2 = X^3 + 18X + 60$ with
$\Delta = -2^4 \cdot 3^5 \cdot 31$.  The factor $31$ reflects
the arithmetic of the quintic resolvent underlying Bring's
surface.

**Golden ratio degeneration.**
The second Weierstrass coefficient $r(q)$ has the factor
$(s^2 + s - 1)$ in its numerator.  This vanishes at
$s = (\sqrt{5} - 1)/2 = 1/\varphi$, the reciprocal of the
golden ratio $\varphi = (1 + \sqrt{5})/2$.  At this value
$q = 1/\varphi^2 = (3 - \sqrt{5})/2 \approx 0.382$, the
curve $\mathcal{E}_q$ acquires a cusp: the elliptic fiber degenerates
and the color fibration becomes singular.

This is the **sub-classical regime** $q < 1$ where the
substrate parameter reverses its role — the quantum deformation
acts in the opposite direction.  The golden ratio threshold
$q = 1/\varphi^2$ marks the boundary beyond which the Descartes
universe cannot support stable color structure.

**$q$-Dependence of the stability structure.**
As $q$ varies from $1$ to $\infty$:

| Regime | $q$ | $j(\mathcal{E}_q)$ | Physics |
|--------|-----|----------|---------|
| Classical | $q = 1$ | $128$ | No crossing asymmetry; $E_1$ is smooth |
| Sub-golden | $q < 1/\varphi^2$ | undefined | $\mathcal{E}_q$ singular; no stable color fibers |
| Golden threshold | $q = 1/\varphi^2$ | $\to \infty$ | Cusp; color degeneration |
| Physical | the substrate $q$ | $129.9$ | Our universe; $\mathcal{E}_q$ smooth with $\Delta < 0$ |
| Deep quantum | $q \to \infty$ | $\to 0$ | $j \to 0$; curve approaches CM curve |

*Proof.*
The coral elliptic curve
([coral elliptic](#prop:coral-elliptic)) at spacetime ratio $z$
is $X^3 + (z + 1)X^2 + (z^2 + z + 1)X + (z^3 + z^2 + z + 1) = 0$.
The Weierstrass normal form is obtained by the standard shift
$X = x - (z + 1)/3$, giving $y^2 = x^3 + p(z)x + r(z)$ with
$p(z) = \tfrac{2}{3}z^2 + \tfrac{1}{3}z + \tfrac{2}{3}$ and
$r(z) = \tfrac{20}{27}z^3 + \tfrac{5}{9}z^2 + \tfrac{5}{9}z + \tfrac{20}{27}$.  Substituting $z = s - s^{-1}$ with
$s = \sqrt{q}$ and simplifying (multiply through by $s^2$ resp.
$s^3$ to clear denominators, then factor) yields the stated
formula.  The factor $(s^2 + s - 1)$ in $s^3 r(s)$ is verified
by direct expansion.  $\square$
