**Conjecture (conditional on the genus-2 ansatz).**
Let $T_{r,s}$ be a torus knot with coprime parameters $r, s \geq 2$.
In the commutative-limit QOU, working under the genus-2 ansatz
([conj:genus-2-ansatz](#conj:genus-2-ansatz)) that the base surface
is $\mathcal{X}_5$ of Definition
[def:hyperelliptic-quintic](#def:hyperelliptic-quintic), the knot
$T_{r,s}$ admits a realisation on the state-space surface only if

$$
  \frac{(r-1)(s-1)}{2}  \leq  2.
$$

*Status.*  Conditional on the ansatz, this is a classical Seifert-genus
bound.  The Seifert genus of $T_{r,s}$ is exactly
$g(T_{r,s}) = (r-1)(s-1)/2$ (Seifert 1934), and a knot whose minimal
Seifert surface has genus exceeding the genus of the host Riemann
surface cannot embed homologically non-trivially on it.  Since
$g(\mathcal{X}_5) = 2$, the stated bound is immediate.  The block is
registered as a *conjecture* rather than a theorem because its
antecedent --- the genus-2 ansatz --- is itself conjectural, so per
the propagation rule of the manuscript any downstream bound inherits
conjectural status.

**Enumeration of admissible torus knots.**  The integer solutions of
$(r-1)(s-1) \leq 4$ with $r, s \geq 2$ and $\gcd(r, s) = 1$ are:

| $r$ | $s$ | $g(T_{r,s})$ | Seifert genus realised? |
|---|---|---|---|
| $2$ | $3$ | $1$ | yes ($< 2$) |
| $2$ | $5$ | $2$ | yes (saturates bound) |
| $3$ | $4$ | $3$ | **no** (exceeds bound) |
| $3$ | $5$ | $4$ | **no** |

The bound thus admits the trefoil $T_{2,3}$ and the Solomon-seal
$T_{2,5}$ while excluding $T_{3,4}$, $T_{3,5}$, and all higher torus
knots --- a sharp restriction on the spectrum of particle
topologies realisable in the commutative limit.
