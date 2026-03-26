The nuclear chart is a **Diophantine geometry** problem.  The
beta-stability curve

$$
  p^*(A)
  \;=\;
  \frac{A}{2 + c \, A^{2/3}}
$$

lives in $\mathbb{R}^2$, but the physical nuclei occupy the
integer lattice $\mathbb{Z}^2_{\geq 0}$.  The valley of stability
is the set of lattice points that best approximate this curve,
subject to the energy functional $M(p, A - p)$.

**Why this is non-trivial.**
If the stability curve were a line $p = \alpha A$ with rational
slope $\alpha = r/s$, every $s$-th mass number would have zero
Diophantine error and the lattice points would fall on the curve
periodically.  But the curve $p^*(A) = A/(2 + cA^{2/3})$ has
*irrational curvature*: the effective slope

$$
  \frac{p^*(A)}{A}
  \;=\;
  \frac{1}{2 + c \, A^{2/3}}
$$

decreases monotonically from $1/2$ (at $A = 0$) toward $0$
(as $A \to \infty$), passing through every rational value exactly
once.  The fractional parts $\{p^*(A)\}$ are therefore
equidistributed modulo $1$ (Weyl), and the Diophantine error
$\varepsilon(A) = |p_{\mathrm{stab}} - p^*|$ exhibits no periodic
pattern.

**The $n/p$ ratio as a continued-fraction problem.**
For each element with atomic number $p$, the stable neutron
number $n^*(p)$ satisfies

$$
  \frac{n^*(p)}{p}
  \;=\;
  1 + c' \cdot (p + n^*)^{2/3} + O(1/p)
$$

where $c' = a_C / (4\,a_A)$.  The ratio $n/p$ is a slowly
growing function of $p$ whose integer-part transitions
($n/p$ crossing from $1.0$ to $1.1$, from $1.1$ to $1.2$, etc.)
occur at specific elements:

| $n/p$ threshold | Element | $p$ | $n$ |
|-----------------|---------|-----|-----|
| $1.00$ | Calcium | 20 | 20 |
| $1.10$ | Krypton | 36 | 48 |
| $1.20$ | Tin | 50 | 70 |
| $1.30$ | Tungsten | 74 | 110 |
| $1.40$ | Lead | 82 | 126 |
| $1.54$ | Uranium | 92 | 146 |

The spacing between these thresholds is governed by the
continued-fraction expansion of the curve $p^*(A)$ evaluated at
successive integers — a classical problem in Diophantine
approximation theory.

**Connection to the substrate parameter.**
The curvature parameter $c = a_C / (2\,a_A) =
(q - q^{-1}) \lambda_C / (2\,a_A)$ is controlled entirely by $q$.
At $q = 1$, $c = 0$ and $p^* = A/2$ for all $A$: the curve is
a line, the Diophantine problem is trivial, and all nuclei have
$n = p$.  As $q$ increases from $1$, the curvature $c$ grows,
the curve bends away from the diagonal, and the Diophantine
structure becomes nontrivial — producing the characteristic
neutron excess of heavy elements and the magic-number shell
closures.

The entire nuclear chart — including its number-theoretic
fine structure — is encoded in the single parameter $q$.
