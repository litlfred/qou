The nuclear stability problem is a **Diophantine problem on an
algebraic curve**.  The stable hadrons — the nuclei that exist in
nature — are precisely the integer solutions to an equation
derived from the Skein binding Lagrangian.

**The stability cubic.**
Substituting $t = A^{1/3}$ into the continuous stability
condition $p^*(A) = a_A A / (2a_A + 2a_C A^{2/3})$
([integer stability](#prop:integer-stability)) and clearing
denominators gives the **stability cubic**

$$
  t^3 =  2p(1 + ct^2),
  \qquad
  c = \frac{a_C}{2a_A},
$$

a plane curve $\mathcal{S} \subset \mathbb{A}^2$ parametrising
the locus of beta-stable nuclei in the $(p, t)$-plane.  The
physical nuclei are the **integer points** of $\mathcal{S}$:
pairs $(p, A) \in \mathbb{Z}^2$ with $t = A^{1/3}$ and
$A = t^3 \in \mathbb{Z}$.

**Comparison with the color fibration.**
The color elliptic curve of Bring's surface
([color elliptic](#prop:color-elliptic)) is the cubic

$$
  X^3 + (z + 1)X^2 + (z^2 + z + 1)X
  + (z^3 + z^2 + z + 1) = 0
$$

in the color variable $X$ at spacetime ratio $z$.  The
stability cubic (S) and the color cubic (C) are both cubics
in one variable parametrised by another, arising from the
same $\chi = -6$ surface.  The
[elliptic stability conjecture](#rem:elliptic-stability-locus)
proposes that when the pairing energy lifts (S) to genus $1$,
the resulting elliptic curve is isogenous to the color fiber.

**The $n/p$ ratio.**
For each proton number $p$, the stable neutron number
$n^*(p)$ satisfies

$$
  \frac{n^*(p)}{p}
  = 
  \frac{A^*(p)}{p} - 1
  = 
  1 + 2c \cdot {A^*}^{2/3} + O(1/p)
$$

where $A^*(p)$ is the mass number solving $p = A/(2 + cA^{2/3})$.
The ratio $n/p$ is a slowly growing function of $p$ whose
integer-part transitions occur at specific elements:

See [Table](#tbl:diophantine-valley-table-data).

**Stable hadrons as integer points on an algebraic curve.**
The central observation is that every stable nucleus in nature
corresponds to a lattice point $(p, A) \in \mathbb{Z}^2$ on
the stability cubic $\mathcal{S}$.  The
nuclear chart is not a phenomenological fit — it is the
**set of integer solutions** to an algebraic equation determined
by the single parameter $q$.

When the pairing correction lifts $\mathcal{S}$ from genus $0$
to genus $1$
([elliptic stability conjecture](#rem:elliptic-stability-locus)),
the stability pairs become **rational points** of an elliptic curve
$\mathcal{E}_p$ over $\mathbb{Q}(q)$, and Mordell's theorem constrains
them to a finite set — potentially explaining why only finitely
many stability pairs exist.

**Connection to the substrate parameter.**
The curvature parameter $c = (q - q^{-1})\lambda_C / (2a_A)$
is controlled entirely by $q$.  At $q = 1$ the stability cubic
degenerates to $t^3 = 2p$ (a rational parametrisation with all
nuclei symmetric, $n = p$).  As $q$ increases from $1$, the
$ct^2$ term bends the curve, the integer solutions disperse,
and the rich structure of the nuclear chart — neutron excess,
stability pairs, even-odd staggering — emerges from a single
deformation parameter.
