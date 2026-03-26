The nuclear stability problem is a **Diophantine problem on an
algebraic curve**.  The stable hadrons — the nuclei that exist in
nature — are precisely the integer solutions to an equation
derived from the Skein binding Lagrangian.

**The stability cubic.**
Substituting $t = A^{1/3}$ into the continuous stability
condition $Q^*(A) = a_A A / (2a_A + 2a_C A^{2/3})$
([integer stability](#prop:integer-stability)) and clearing
denominators gives the **stability cubic**

$$
  t^3 \;=\; 2Q\,(1 + c\,t^2),
  \qquad
  c = \frac{a_C}{2\,a_A},
$$

a plane curve $\mathcal{S} \subset \mathbb{A}^2$ parametrising
the locus of beta-stable nuclei in the $(Q, t)$-plane.  The
physical nuclei are the **integer points** of $\mathcal{S}$:
pairs $(Q, A) \in \mathbb{Z}^2$ with $t = A^{1/3}$ and
$A = t^3 \in \mathbb{Z}$.

**Comparison with the chiral fibration.**
The chiral elliptic curve of Bring's surface
([chiral elliptic](#prop:chiral-elliptic)) is the cubic

$$
  X^3 + (z + 1)\,X^2 + (z^2 + z + 1)\,X
  + (z^3 + z^2 + z + 1) = 0
$$

in the chiral variable $X$ at spacetime ratio $z$.  The
stability cubic (S) and the chiral cubic (C) are both cubics
in one variable parametrised by another, arising from the
same $\chi = -6$ surface.  The
[elliptic stability conjecture](#conj:elliptic-stability-locus)
proposes that when the pairing energy lifts (S) to genus $1$,
the resulting elliptic curve is isogenous to the chiral fiber.

**The $n/p$ ratio as a function of $Q$.**
For each Coulomb charge $Q = p$, the stable neutron number
$n^*(Q)$ satisfies

$$
  \frac{n^*(Q)}{Q}
  \;=\;
  \frac{A^*(Q)}{Q} - 1
  \;=\;
  1 + 2c \cdot {A^*}^{2/3} + O(1/Q)
$$

where $A^*(Q)$ is the mass number solving $Q = A/(2 + cA^{2/3})$.
The ratio $n/p$ is a slowly growing function of $Q$ whose
integer-part transitions occur at specific elements:

| $n/p$ crosses | Element | $Q = p$ | $n$ |
|---------------|---------|--------:|----:|
| $1.00$ | Calcium | 20 | 20 |
| $1.10$ | Bromine | 35 | 44 |
| $1.20$ | Zirconium | 40 | 50 |
| $1.30$ | Tin | 50 | 70 |
| $1.40$ | Tungsten | 74 | 110 |
| $1.54$ | Lead | 82 | 126 |
| $1.59$ | Uranium | 92 | 146 |

**Stable hadrons as integer points on an algebraic curve.**
The central observation is that every stable nucleus in nature
corresponds to an integer point $(Q, A) \in \mathbb{Z}^2$ on
(or within one unit of) the stability cubic $\mathcal{S}$.  The
nuclear chart is not a phenomenological fit — it is the
**set of integer solutions** to an algebraic equation determined
by the single parameter $q$.

When the pairing correction lifts $\mathcal{S}$ from genus $0$
to genus $1$
([elliptic stability conjecture](#conj:elliptic-stability-locus)),
the magic numbers become **rational points** of an elliptic curve
$E_Q$ over $\mathbb{Q}(q)$, and Mordell's theorem constrains
them to a finite set — potentially explaining why only finitely
many magic numbers exist.

**Connection to the substrate parameter.**
The curvature parameter $c = (q - q^{-1})\lambda_C / (2a_A)$
is controlled entirely by $q$.  At $q = 1$ the stability cubic
degenerates to $t^3 = 2Q$ (a rational parametrisation with all
nuclei symmetric, $n = p$).  As $q$ increases from $1$, the
$ct^2$ term bends the curve, the integer solutions disperse,
and the rich structure of the nuclear chart — neutron excess,
magic numbers, even-odd staggering — emerges from a single
deformation parameter.
