Interactive 3D visualisation of the color tube divisors on the
Brings surface brane, embedded in $\mathbb{P}^4(\mathbb{C})$ —
the projective space containing both the spacetime base
$\mathbb{P}^1(\mathbb{C})$ and the color fiber directions.

The brown surface of revolution represents the brane with smooth
profile $R(z) = s\sqrt{(2+z+2z^2)/3}$ derived from the cubic
discriminant structure.  Three color tubes spiral around it:

| Tube | Color coordinate | Resolvent |
|------|-----------------|-----------|
| Red  | $c_r = w_2 - z$ | $w_2 = \tfrac{1}{\sqrt5}\sum_j \zeta^{2j}x_j$ |
| Green | $c_g = w_3 - z$ | $w_3 = \tfrac{1}{\sqrt5}\sum_j \zeta^{3j}x_j$ |
| Blue | $c_b = w_4 - z$ | $w_4 = \tfrac{1}{\sqrt5}\sum_j \zeta^{4j}x_j$ |

where $x_2, x_3, x_4$ are the three roots of the Brings fiber cubic
$$
  t^3 + (1{+}z)\,t^2 + (1{+}z{+}z^2)\,t + (1{+}z)(1{+}z^2) = 0
$$
at each point $z \in [0, \infty] = \mathbb{P}^1(\mathbb{R})$.

**Base scaling.**  Four modes map $z \in [0, \infty]$ to visual space:

| Mode | Mapping | Behaviour |
|------|---------|-----------|
| arctan | $x = \arctan z$ | Compactifies $\infty$; projective |
| log | $x = \ln(1+z)$ | Moderate compression |
| $\sqrt{z}$ | $x = \sqrt{z}$ | Emphasises small $z$ |
| linear | $x = z$ | Affine chart |

Each color tube is a *section* of the cover — it lives **on** the brane
surface at azimuthal angle $\arg(c_k(z))$, never piercing through it.
Its 3D position is $(x(z),\, R(z)\cos\arg c_k,\, R(z)\sin\arg c_k)$,
with only the phase of $c_k$ determining the position.

**Divisor markers** (white spheres) appear where two color tubes collide
in angle, $\arg(c_j) \equiv \arg(c_k) \pmod{2\pi}$.  These are the
ramification points of the covering $\pi\colon\Sigma_4\to\mathbb{P}^1(\mathbb{C})$
— where two sheets of the cover merge.

**Torsion parameter $q$.**  The substrate parameter controls the
twist rate of the color tubes via $(q - q^{-1})\cdot z$.  At $q = 1$
(classical limit) the torsion vanishes; as $q$ departs from $1$ the
color tubes wind more tightly, shifting the divisor locations.
