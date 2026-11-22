A closed geodesic on the cusp torus of the figure-eight knot — the path traced by a braid word's particle/vortex flow — is a class $(m, \ell)$ in the cusp lattice $\mathbb{Z}\langle 1, \omega\rangle$, where $m$ counts meridian turns, $\ell$ counts longitude turns, and $\omega = e^{i\pi/3}$ is the cusp shape ([Cusp-shape bar-parity: the figure-eight modulus splits as $\mathfrak{V} = \mathrm{Vol} + i\,\mathrm{CS}$](cusp-shape-bar-parity.md)). Since one meridian turn is a boost of rapidity $\ln q_0$ ([Meridian holonomy is a boost: $\mathrm{barEven}(q)^2 - \mathrm{barOdd}(q)^2 = 4$](meridian-holonomy-boost.md)), the geodesic's log-holonomy is
$$
  u_{m,\ell} = (\ln q_0)\,(m + \ell\,\omega).
$$

**Proposition.** *Let $s$ satisfy $s^2 = 3$ and write $\omega = (1+s)/2$. For every $c, m, \ell$ in a commutative ring,*
$$
  \bigl(c(2m+\ell)\bigr)^2 - \bigl(c\,\ell\,s\bigr)^2 = c^2\bigl[(2m+\ell)^2 - 3\ell^2\bigr].
$$
*The bracket is the norm form of $\mathbb{Z}[\sqrt3]$, of discriminant $12$. Moreover the two relevant quadratic orders behave oppositely under their fundamental units:*

1. *(silver, disc $12$)* $\ N(2+\sqrt3) = +1$, *and every power satisfies $x_n^2 - 3y_n^2 = +1$;*
2. *(golden, disc $5$)* $\ N(\varphi) = -1$ *for $\varphi = (1+\sqrt5)/2$, and $N(\varphi^n) = (-1)^n$.*

Since $2\,\mathrm{Re}\,u_{m,\ell} = (\ln q_0)(2m+\ell)$ and $2\,\mathrm{Im}\,u_{m,\ell} = (\ln q_0)\,\ell\sqrt3$, the identity says the indefinite pairing $\mathrm{Re}^2 - \mathrm{Im}^2$ on the cusp lattice *is* the disc-$12$ norm form. Combined with the imaginary part of the Neumann–Zagier complex volume, $\mathrm{Im}\,\mathfrak{V}_{4_1} = \tfrac{\sqrt3}{4}\bigl(\mathrm{Re}^2 u - \mathrm{Im}^2 u\bigr)$, this gives
$$
  \mathrm{Im}\,\mathfrak{V}_{4_1}(u_{m,\ell}) = \frac{\sqrt3}{16}\,(\ln q_0)^2\,\bigl[(2m+\ell)^2 - 3\ell^2\bigr],
$$
so the *sign* of $\mathrm{Im}\,\mathfrak{V}_{4_1}$ is a discrete arithmetic invariant of the winding class alone, carrying no dependence on $q_0$.

Two consequences are immediate. First, because $\sqrt3$ is irrational the form never vanishes on a nonzero lattice class: every geodesic is strictly boost-dominated $(>0)$ or spin-dominated $(<0)$, never null. The spin-dominated sector is the winding-slope window $m/\ell \in \bigl(-\tfrac12 - \tfrac{\sqrt3}{2},\, -\tfrac12 + \tfrac{\sqrt3}{2}\bigr)$, containing exactly the integer slopes $0$ and $-1$ — the longitude-dominated directions. The meridian $(1,0)$ gives $+4$ and the longitude $(0,1)$ gives $-2$.

Second, the level set $(2m+\ell)^2 - 3\ell^2 = 1$ is Pell's equation, whose solutions are the units $(2+\sqrt3)^n$. Writing $x_n + y_n\sqrt3 = (2+\sqrt3)^n$ gives $x_n = \cosh(n\rho)$ and $\sqrt3\,y_n = \sinh(n\rho)$ with $\rho = \mathrm{arccosh}\,2 = \ln(2+\sqrt3)$, and under $(\mathrm{barEven}, \mathrm{barOdd}) = (2x_n, 2\sqrt3\,y_n)$ this is exactly the boost hyperbola $\mathrm{barEven}^2 - \mathrm{barOdd}^2 = 4$ of [Meridian holonomy is a boost: $\mathrm{barEven}(q)^2 - \mathrm{barOdd}(q)^2 = 4$](meridian-holonomy-boost.md). The boost identity and Pell's equation are the same statement, and the integer solutions form a discrete boost subgroup of rapidity $n\,\rho$.

The contrast in items 1 and 2 is what distinguishes the two orders. The silver recursion $(a,b) \mapsto (2a+3b,\, a+2b)$ *preserves* $a^2 - 3b^2$; the golden recursion $(a,b) \mapsto (b,\, a+b)$ *negates* $a^2 + ab - b^2$. A single `ring` identity each. Hence a sign alternating with a winding exponent is structurally unavailable on the cusp-torus order and available on the golden order carried by Bring's surface.

The ring identity holds over a generic commutative ring (no ordering, no $\mathbb{R}$, $s$ entering only through $s^2 = 3$), the two norm recursions hold over $\mathbb{Z}$, and induction gives $N(\varphi^n) = (-1)^n$.
