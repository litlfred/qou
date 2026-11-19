The stability curve and the color fibration of Bring's surface share the same algebraic origin. The nuclear degeneracy locus — the curve in the $(p, A)$-plane where adjacent nuclei have equal energy — is conjectured to form an elliptic curve isogenous to the color fiber $\mathcal{E}_z$.

**The two cubics.**

The color elliptic curve ([color elliptic](#prop:color-elliptic)) at spacetime ratio $z$ is:

$$
  X^3 + (z + 1)X^2 + (z^2 + z + 1)X
  + (z^3 + z^2 + z + 1) = 0.
  \tag{C}
$$

The nuclear stability condition ([beta-stability line](#prop:beta-stability)), under the substitution $t = A^{1/3}$, yields:

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
2. *There exists an isogeny $\varphi \colon \mathcal{E}_p \to \mathcal{E}_{z(p)}$ to the color fiber of the Bring's surface, where $z(p)$ is the spacetime ratio at which the quadratic coefficient of the color elliptic cubic (C) equals that of the stability cubic (S) under $X = t$:*

$$
  z(p) =  -(cp + 1).
$$

3. *The integer points $(p, A) \in \mathcal{E}_p(\mathbb{Z})$ correspond to the stability pairs: the mass numbers $A$ at which the even-even/odd-odd degeneracy falls exactly on an integer lattice point.*

**Coefficient matching.**

The stability cubic, written as a monic cubic in $t$ with parameter $p$, is

$$
  t^3 - cp \cdot t^2 + 0 \cdot t - 2p = 0.
$$

At $z = -(cp+1)$ the color cubic (C) becomes, with $z + 1 = -cp$, $z^2 + z + 1 = c^2p^2 + cp + 1$ and $z^3 + z^2 + z + 1 = (z+1)(z^2+1)$:

$$
  X^3 - cp\,X^2 + \bigl(c^2p^2 + cp + 1\bigr) X
  - cp\bigl(c^2p^2 + 2cp + 2\bigr) = 0.
$$

Identifying $X = t$, the coefficients compare as follows:

| Coefficient | Color (C) at $z = -(cp+1)$ | Stability (S) | Agreement |
|-------------|----------------------------|---------------|-----------|
| $X^2$ | $-cp$ | $-cp$ | for every $p$ (defines $z(p)$) |
| $X^1$ | $c^2p^2 + cp + 1$ | $0$ | never for real $cp$ (discriminant $-3$) |
| $X^0$ | $-cp(c^2p^2 + 2cp + 2)$ | $-2p$ | only on $c^3p^2 + 2c^2p + 2c = 2$ |

The constant-term condition $c^3p^2 + 2c^2p + 2c = 2$ has, at $c = \lambda_C/(2a_{\mathrm{asym}}) \approx 0.0145158337$ (the asymmetry constant of [neutron prediction comparison](#prop:neutron-prediction-comparison)), the positive root $p \approx 736.8$, far beyond the heaviest known element ($Z = 118$). The linear coefficient never agrees. So under $X = t$ the two cubics share only their quadratic coefficient.

**Affine obstruction.** No other identification does better. Removing the quadratic term writes a monic cubic as $Y^3 + PY + Q$, and a change of variable $X \mapsto \alpha X + \beta$ with $\alpha, \beta \in \mathbb{C}$, $\alpha \neq 0$, sends $(P, Q) \mapsto (\alpha^2 P, \alpha^3 Q)$. Hence

$$
  J = \frac{4P^3}{4P^3 + 27Q^2}
$$

is unchanged, and two cubics related by such a substitution have equal $J$. For (C),

$$
  P_C = \frac{2z^2 + z + 2}{3}, \qquad
  Q_C = \frac{5(z+1)(4z^2 - z + 4)}{27},
$$

and $2z^2 + z + 2 > 0$ for real $z$, so $P_C > 0$ and $4P_C^3 + 27Q_C^2 > 0$, giving $J_C > 0$. For (S),

$$
  P_S = -\frac{c^2p^2}{3}, \qquad
  4P_S^3 + 27Q_S^2 = \frac{4p^2(54c^3p^2 + 729)}{27},
$$

so $J_S < 0$ whenever $c > 0$ and $p \neq 0$. Therefore no substitution $X \mapsto \alpha X + \beta$ carries (S) to (C) at any real $z$; equality of $J$ requires complex $z$. Matching "up to a Möbius transformation" would add nothing, since any three distinct points of $\mathbb{P}^1$ map to any other three. The isogeny in item 2 is therefore the whole content of that item.

**Physical interpretation.**

Under this conjecture, four correspondences hold.

* **Three color tubes** $(r, g, b)$ of the color fibration correspond to the **three sectors** of nuclear binding: volume (strong), Coulomb (electromagnetic), and Pauli (exclusion).
* **Elliptic fibers** $\mathcal{E}_z$ at spacetime $z$ encode allowed baryon configurations, whereas the **stability elliptic curve** $\mathcal{E}_p$ at proton number $p$ encodes allowed nuclear configurations.
* **Isogeny** $\varphi$ connects single-baryon color structure ([proton](#def:categorical-proton)) to multi-baryon nuclear structure ([stable nucleus](#def:stable-nucleus)).
* **Stability pairs** act as the integer points $(p, A) \in \mathcal{E}_p(\mathbb{Z})$ where the even-even/odd-odd degeneracy falls on a lattice point.

**Computational evidence.**

The color elliptic curve ([Descartes elliptic curve](#prop:descartes-elliptic-curve)) at the aether parameter $q_0$ is:

$$
  \mathcal{E}_q  :  y^2 = x^3 + 0.7087x + 0.8056,
  \qquad \Delta = -16(4a^3 + 27b^2) \approx -303.17, \quad j \approx 129.86,
$$

with $a \approx 0.7087$ and $b \approx 0.8056$ its Weierstrass coefficients. Since $\Delta < 0$, the real locus $\mathcal{E}_q(\mathbb{R})$ possesses a single connected component.

**Stable hadrons as lattice points on the stability cubic.**

The stable nuclei provide the **$\mathbb{N}^2$ lattice points** $(Q, N)$ on the genus-$0$ **stability cubic** ([Diophantine valley](#rem:diophantine-valley)):

$$
  t^3 =  p(2 + ct^2),
  \qquad A = Z + N = t^3.
$$

This curve is rational: $p = t^3/(2 + ct^2)$. For each mass number $A \in \mathbb{N}$, the stable proton number $p$ serves as the exact integer minimiser of the convex quadratic $E(p, A)$ ([integer stability](#prop:integer-stability)). There is no approximation — the integer minimiser of a convex quadratic is determined exactly.

**Pairing lift to genus $1$ (open).**

The genus-$0$ stability cubic accounts for all stable nuclei via lattice-point enumeration. Whether the pairing energy lifts this curve to the genus-$1$ elliptic curve $\mathcal{E}_q$ — and whether the stability pairs $\{2, 8, 20, 28, 50, 82, 126\}$ then acquire an interpretation as integer points of $\mathcal{E}_p$ — remains an open question. The structural parallel between the stability cubic and the color cubic (identical algebraic origin in the Bring's surface) is unproven, and the coefficient matching above agrees in the quadratic coefficient only, with the constant term agreeing at $p \approx 736.8$, outside the nuclear chart.

**Established results.**

* The stable nuclei represent lattice points on the stability cubic (exact, from the Skein binding Lagrangian).
* The Descartes elliptic curve $\mathcal{E}_q$ exists and carries the stated invariants (exact, from the color fibration).
* Under $X = t$ at $z = -(cp+1)$, the color cubic and the stability cubic share their quadratic coefficient; their linear coefficients never agree (exact, by the table above).
* No substitution $X \mapsto \alpha X + \beta$ carries (S) to (C) at real $z$, since $J_C > 0 > J_S$.
* The golden ratio degeneration at $q = 1/\varphi^2$ holds (exact, from the $(s^2 + s - 1)$ factor).

The full numerical computation is carried out at 100-digit precision.
