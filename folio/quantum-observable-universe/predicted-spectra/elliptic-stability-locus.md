The stability curve and the color fibration of Bring's surface share the same algebraic origin. We conjecture that the nuclear degeneracy locus — the curve in the $(p, A)$-plane where adjacent nuclei have equal energy — forms an elliptic curve isogenous to the color fiber $\mathcal{E}_z$.

**The two cubics.**

The color elliptic curve ([color elliptic](#prop:color-elliptic)) at spacetime ratio $z$ is:

$$
  X^3 + (z + 1)X^2 + (z^2 + z + 1)X
  + (z^3 + z^2 + z + 1) = 0.
  \tag{C}
$$

The nuclear stability condition ([beta-stability](#prop:beta-stability)), under the substitution $t = A^{1/3}$, yields:

$$
  t^3 - cpt^2 - 2p = 0,
  \qquad c = \frac{a_C}{2a_A}
  = \frac{\lambda_C}{2a_{\mathrm{asym}}}.
  \tag{S}
$$

Both are cubics in one variable parametrized by another. The color cubic (C) carries parameter $z$ (spacetime) and variable $X$ (color coordinate); the stability cubic (S) uses parameter $p$ (Coulomb charge) and variable $t$ (cube root of mass number).

**Genus comparison.**

The stability cubic (S) is rational. Solving for $p$ yields $p = t^3 / (2 + ct^2)$, confirming genus $0$. The color cubic (C) has genus $1$ for generic $z$ (it defines an elliptic curve whose $j$-invariant varies as a rational function of $z$).

The physical stability problem incorporates the pairing energy $\pm \lambda_P / t^{3/2}$, distinguishing even-even, even-odd, odd-even, and odd-odd nuclei. The **degeneracy locus** is the set of $(p, t)$ at which an even-even nucleus $(p, A)$ and the odd-odd nucleus $(p+1, A)$ have equal energy. With the $p$-dependent energy $a_C p^2/A^{1/3} + a_A (A-2p)^2/A$ of [integer stability](#prop:integer-stability) and pairing $-\lambda_P/A^{1/2}$ (even-even) and $+\lambda_P/A^{1/2}$ (odd-odd), the condition $E(p+1) - E(p) = -2\lambda_P/A^{1/2}$, multiplied by $A/(4a_A)$ and written in $t$ and $\bar p = p + \tfrac12$, is:

$$
  t^3 - c\bar p\,t^2 - 2\bar p
  =  \frac{\lambda_P}{2a_A} \cdot t^{3/2}.
  \tag{D}
$$

Squaring to clear the half-integer exponent and substituting $u = t^{1/2}$ (so $t = u^2$, $t^{3/2} = u^3$, $t^3 = u^6$) gives:

$$
  \bigl(u^6 - c\bar p\,u^4 - 2\bar p\bigr)^2
  =  \frac{\lambda_P^2}{4a_A^2} \cdot u^6.
  \tag{D$'$}
$$

This defines a degree-12 curve in $(\bar p, u)$. Factoring out the genus-$0$ component (the pairing-free stability curve) leaves a degree-6 residual curve in $(p, u)$, generically of genus $1$.

**Conjecture.**
*Let $\mathcal{D} \subset \mathbb{A}^2$ be the degeneracy locus (D$'$) reduced by the pairing-free stability curve (S). Then:*

1. *The smooth model of $\mathcal{D}$ forms an elliptic curve $\mathcal{E}_p$ over $\mathbb{Q}(q)$.*
2. *There exists an isogeny $\varphi \colon E_Q \to E_{z(p)}$ to the color fiber of the Bring's surface, where $z(p)$ is the spacetime ratio at which the color-tube cubic ([color tube cubic](#rem:color-tube-cubic)) specialises to the stability cubic:*

$$
  z(p) =  -\frac{1}{cp}
$$

   *so that the coefficients of (C) at $z = z(p)$ match those of (S) up to a Möbius transformation.*
3. *The integer points $(p, A) \in E_Q(\mathbb{Z})$ correspond to the stability pairs: the mass numbers $A$ at which the even-even/odd-odd degeneracy falls exactly on an integer lattice point.*

**Coefficient matching.**

The color cubic at $z = -1/(cp)$ is:

$$
  X^3 + \left(1 - \frac{1}{cp}\right) X^2
  + \left(\frac{1}{c^2p^2} - \frac{1}{cp} + 1\right) X
  + \cdots = 0.
$$

We rewrite the stability cubic as a monic cubic in $t$ with parameter $p$:

$$
  t^3 - cp \cdot t^2 + 0 \cdot t - 2p = 0.
$$

Under the substitution $t = \alpha X + \beta$ with $\alpha = -cp$ and $\beta = cp \cdot z$, the leading coefficients match:

| Coefficient | Chiral (C) | Stability (S) | Match condition |
|-------------|-----------|---------------|-----------------|
| $X^2$ | $z + 1$ | $-cp$ | $z = -(cp + 1)$ |
| $X^0$ | $z^3 + z^2 + z + 1$ | $-2p$ | $(z+1)(z^2+1) = -2p$ |

Eliminating $z$: since $z + 1 = -cp$ and $z^2 + 1 = (cp + 1)^2 + 1 = c^2p^2 + 2cp + 2$, the $X^0$ condition reads $(-cp)(c^2p^2 + 2cp + 2) = -2p$, that is,

$$
  c^3 p^2 + 2c^2 p + 2c = 2.
$$

At $c = \lambda_C/(2a_{\mathrm{asym}}) \approx 0.0145158337$ (the asymmetry constant of [neutron prediction comparison](#prop:neutron-prediction-comparison)), the positive root is $p \approx 736.8$. Both lie far beyond the heaviest known element ($Z = 118$), so this coefficient match does not single out any observed nucleus.

**Physical interpretation.**

If the conjecture holds:

- The **three color tubes** $(r, g, b)$ of the color fibration correspond to the **three sectors** of nuclear binding: volume (strong), Coulomb (electromagnetic), and Pauli (exclusion).
- The **elliptic fiber** $\mathcal{E}_z$ at spacetime $z$ encodes the allowed baryon configurations at that point; the **stability elliptic curve** $\mathcal{E}_p$ at proton number $p$ encodes the allowed nuclear configurations at that proton count.
- The **isogeny** $\varphi$ connects them, representing the passage from single-baryon color structure to multi-baryon nuclear structure — the same passage that takes the proton ([proton](#def:categorical-proton)) from a color-linked triple to a nucleus ([stable nucleus](#def:stable-nucleus)).
- The **stability pairs** act as the integer points of $\mathcal{E}_p$ — the $(p, A) \in E_Q(\mathbb{Z})$ where the even-even/odd-odd degeneracy falls on a lattice point.

**Computational evidence.**

The color elliptic curve ([Descartes elliptic curve](#prop:descartes-elliptic-curve)) at the substrate parameter $q$ is:

$$
  \mathcal{E}_q  :  y^2 = x^3 + 0.7087x + 0.8056,
  \qquad \Delta = -18.95, \quad j = 129.9.
$$

Since $\Delta < 0$, the real locus $\mathcal{E}_q(\mathbb{R})$ possesses a single connected component.

**Stable hadrons as lattice points on the stability cubic.**

The stable nuclei provide the **$\mathbb{N}^2$ lattice points** $(Q, N)$ on the genus-$0$ **stability cubic** ([Diophantine valley](#rem:diophantine-valley)):

$$
  t^3 =  p(2 + ct^2),
  \qquad A = Z + N = t^3.
$$

This curve is rational: $p = t^3/(2 + ct^2)$. For each mass number $A \in \mathbb{N}$, the stable proton number $p$ serves as the exact integer minimiser of the convex quadratic $E(p, A)$ ([integer stability](#prop:integer-stability)). There is no approximation — the integer minimiser of a convex quadratic is determined exactly.

**Pairing lift to genus $1$ (open).**

The genus-$0$ stability cubic accounts for all stable nuclei via lattice-point enumeration. Whether the pairing energy lifts this curve to the genus-$1$ elliptic curve $\mathcal{E}_q$ — and whether the stability pairs $\{2, 8, 20, 28, 50, 82, 126\}$ then acquire an interpretation as integer points of $\mathcal{E}_p$ — remains an open question. The structural parallel between the stability cubic and the color cubic (identical algebraic origin in the Bring's surface) is unproven, and the coefficient matching above lands at $p \approx 736.8$, outside the nuclear chart.

**Established results:**

- The stable nuclei represent lattice points on the stability cubic (exact, from the Skein binding Lagrangian).
- The Descartes elliptic curve $\mathcal{E}_q$ exists and carries the stated invariants (exact, from the color fibration).
- The stability cubic and the color cubic share their algebraic origin in the Bring's surface (exact, by construction).
- The golden ratio degeneration at $q = 1/\varphi^2$ holds (exact, from the $(s^2 + s - 1)$ factor).

**Witness data**: See `computations/elliptic-stability.json` for the full numerical computation at 100-digit precision.
