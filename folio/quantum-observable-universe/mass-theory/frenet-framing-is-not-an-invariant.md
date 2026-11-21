*The [chain result](#prop:canonical-closure-torus-chain) fixed the curvature
half of Călugăreanu for the canonical closure: Milnor's infimum of total
curvature over the isotopy class is $2\pi(2A+1)$. The refrain of the same
thread was that the binding gap needs the* other *half -- a fractional framing
scalar, i.e. twist, which the osculating circle is blind to. This remark says
what that half can and cannot be, on a realisation of the component knots.*

*For a closed curve with a framing $F$, $\mathrm{Lk}_F = \mathrm{Wr} +
\mathrm{Tw}_F$ with $\mathrm{Lk}_F \in \mathbb{Z}$, and for the Frenet framing
$\mathrm{Tw}_F = \frac{1}{2\pi}\oint \tau\, ds$. The infimum of total*
curvature *over an isotopy class is an invariant (Milnor); total* torsion
*has no extremal invariant, and neither has the writhe -- a helical
perturbation of any arc moves both by an arbitrary amount inside the isotopy
class. Measured on the standard torus embedding*

$$
  \gamma(t) = \bigl((1 + r\cos qt)\cos 2t,\; (1 + r\cos qt)\sin 2t,\; r\sin qt\bigr)
$$

*of $T(2,q)$, $q \in \{3, 5, 7\}$, along $r \in \{0.45, \dots, 0.02\}$
(mpmath quadrature, 24 digits): $\int\kappa\, ds$ decreases monotonically to
$4\pi$ ($\int\kappa/4\pi$ from $1.34$, $2.26$, $3.27$ down to $1.0003$,
$1.003$, $1.014$), the infimum approached and never attained; $\oint\tau\, ds$
and $\mathrm{Wr}$ both move across the family; and $\mathrm{Wr} +
\mathrm{Tw}_F$ is an integer at every $r$ -- but not the* same *integer.*

## The jump

At $t = \pi/q$ one has $\cos qt = -1$, $\sin qt = 0$, and with $\rho = 1-r$,
$c = \cos(2\pi/q)$, $s = \sin(2\pi/q)$,

$$
  \gamma'(\pi/q) \times \gamma''(\pi/q)
  \;=\;
  \bigl(q^2 r - 4\rho\bigr)\cdot\bigl(q r s,\; -q r c,\; -2\rho\,(c^2+s^2)\bigr),
$$

so the curvature vanishes there exactly when $r = r^* = 4/(q^2+4)$: $4/13$,
$4/29$, $4/53$ for the three component types. Since $\cos qt = -1$ at the $q$
parameters $(2k+1)\pi/q$, the family crosses $q$ inflection points at once; the
Frenet normal flips at each, and the Frenet self-linking jumps by $q$:
$\mathrm{Lk}_F = -2q$ for $r > r^*$ and $-q$ for $r < r^*$, in all three
families. The factorisation is exact, and the algebra (the cross product of
velocity and acceleration, the inflection criterion, the three inflection
radii, the inflection parameters and their injectivity) is proved.

## What this closes

Even the integer half of Călugăreanu is a property of the *curve*: the Frenet
framing is a framing of the embedding, discontinuous across an inflection, not
a framing of the knot type. So no framing datum -- fractional or integral --
comes from the geometry of the isotopy class alone. Whatever fractional
framing datum the substrate carries is therefore a property of the algebra
(the fractional twist $q^{2c(\lambda)/n}$), or of a canonical *embedding*
(a Möbius-energy or ropelength minimiser), never of the knot type. That is
the honest closure of the "missing half" question inside this thread: the
half the geometry supplies invariantly is exactly the half already in hand,
the curvature floor, and it is not the one the binding gap needs.

## Scope

Per component, on one convenient embedding; no canonical embedding is chosen
and no torsion number is compared with the substrate's hull-exit window,
because the principle says such a comparison has no invariant meaning. That
the $t = \pi/q$ inflections are the only ones in the family is observed
(sampled $\kappa_{\min} > 0$ at every listed $r$), not proved; the
differentiation behind $\gamma'(\pi/q)$, $\gamma''(\pi/q)$ is a symbolic
computation and is not part of the proved algebra. Nothing here connects curvature or torsion to binding.
