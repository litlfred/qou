The electromagnetic fine structure constant $\alpha_{\mathrm{EM}}$
is not a free parameter in the Descartes universe.  It is determined
by three finite, combinatorial ingredients: the antisymmetric
eigenvalue of the $R$-matrix, the $q$-deformed crossing numbers of
the two force-carrier generators, and the substrate parameter $q$.
No contour integrals, no factors of $2\pi i$, and no
renormalisation-group running are required at the fundamental level.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with substrate
parameter $q$ and force-carrier generators $T_{2,9}$ (crossing
number $c_s = 9$) and $T_{3,5}$ (crossing number $c_w = 10$).  Then
the electromagnetic fine structure constant, defined as the
$\tau$-trace of the antisymmetric braiding component normalised by
the force-carrier crossing complexities, is

$$
  \alpha_{\mathrm{EM}}(q)
  \;=\;
  \frac{q^{-1}}{[c_s]_q \cdot [c_w]_q}
  \;=\;
  \frac{q^{-1}}{[9]_q \cdot [10]_q}
$$

where $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ is the $q$-integer.

**Derivation from three layers.**

The electromagnetic coupling between two charged localized knots
$(c_1, K_1)$ and $(c_2, K_2)$ factorises into three finite
contributions:

*Layer 1: Charge (discrete, from writhe).*
The electromagnetic charge of a knot $K$ is its $q$-writhe, the
antisymmetric crossing count under the crossing reversal involution
$\sigma$
([antiparticle crossing reversal](#prop:antiparticle-crossing-reversal)):

$$
  Q_q(K) \;=\; [w(K)]_q
  \;=\; \frac{q^{w(K)} - q^{-w(K)}}{q - q^{-1}}
$$

where $w(K) = \sum_i \epsilon_i \in \mathbb{Z}$ is the writhe (signed
crossing sum).  For a torus knot $T_{m,n}$, all crossings share the
same sign, so $w(T_{m,n}) = \pm m(n-1)$.  This is purely
combinatorial: a finite sum of $\pm 1$ values, $q$-deformed.

*Layer 2: Coupling strength (from the $R$-matrix).*
The categorical braiding $\sigma_{K_1, K_2}$ decomposes into
$\dagger$-eigenspaces:

$$
  \sigma = \sigma_{\mathrm{sym}} \oplus \sigma_{\mathrm{anti}}.
$$

The antisymmetric eigenvalue of the $R$-matrix for
$\mathrm{SU}_q(2)$ is $-q^{-1/2}$, giving

$$
  |\mathrm{tr}_\tau(\sigma_{\mathrm{anti}})|^2 = q^{-1}.
$$

This is the **bare coupling**: the probability amplitude for an
electromagnetic interaction at a single crossing site, evaluated
by the fibre functor $\tau$.  It is a rational function of $q$ —
no transcendental constants.

*Layer 3: Normalisation by force-carrier complexity.*
The bare coupling $q^{-1}$ must be normalised by the total
crossing complexity of the force-carrying sector.  The two
genus-$4$ saturating generators $T_{2,9}$ and $T_{3,5}$
([force identification](#rem:force-knot-identification)) carry
the strong and weak forces respectively.  Their $q$-deformed
crossing numbers $[9]_q$ and $[10]_q$ measure the total
topological complexity available for non-electromagnetic
interactions.  The electromagnetic coupling is what remains
after this complexity is factored out:

$$
  \alpha_{\mathrm{EM}}
  \;=\;
  \frac{|\mathrm{tr}_\tau(\sigma_{\mathrm{anti}})|^2}{[c_s]_q \cdot [c_w]_q}
  \;=\;
  \frac{q^{-1}}{[9]_q \cdot [10]_q}.
$$

The denominator $[9]_q \cdot [10]_q$ is the product of the
$q$-crossing complexities of the strong and weak sectors.  The
numerator $q^{-1}$ is the antisymmetric braiding eigenvalue.
The ratio gives the fraction of the total interaction that is
electromagnetic.

**Numerical evaluation.**

At the substrate parameter $q = 1.110$:

| Quantity | Value |
|----------|-------|
| $q^{-1}$ | $0.900\,901$ |
| $[9]_q$ | $10.364\,04$ |
| $[10]_q$ | $11.895\,01$ |
| $[9]_q \cdot [10]_q$ | $123.257$ |
| $\alpha_{\mathrm{EM}}(1.110)$ | $0.007\,308$ |
| $1/\alpha_{\mathrm{EM}}(1.110)$ | $\mathbf{136.84}$ |
| Experimental (CODATA) | $137.036$ |
| Discrepancy | $+0.14\%$ |

The value $q = 1.110\,23$ gives the exact CODATA value
$\alpha^{-1} = 137.036$.

**Why this formula is finite.**

Every ingredient is a finite algebraic expression in $q$:

- The charge $Q_q = [w]_q$ is a ratio of $q$-powers — no integral.
- The coupling $q^{-1}$ is an eigenvalue of the $R$-matrix — no
  trace over infinite-dimensional spaces.
- The normalisation $[9]_q \cdot [10]_q$ is a product of
  $q$-integers — no renormalisation group.
- The spatial dependence (Coulomb $1/r^2$) is added by the
  Green's function of the base manifold, which is external to
  $\alpha_{\mathrm{EM}}$ itself.

The formula makes sense over any completion of the base field:
archimedean ($\mathbb{R}$), $p$-adic ($\mathbb{Q}_p$), or finite
($\mathbb{F}_q$).  The fine structure constant is a
**$q$-arithmetic invariant** of the Descartes universe, not a
continuous parameter requiring measurement.

**Projection to spacetime.**

The coupling $\alpha_{\mathrm{EM}}$ becomes visible in spacetime
through three steps:

1. **Charge attachment.**  The localized knot $(c, K)$ descends via
   $\tau$ to a point $c \in \mathbb{P}(V)$ carrying scalar charge
   $Q_q(K)$.

2. **Braiding evaluation.**  The interaction between $(c_1, K_1)$
   and $(c_2, K_2)$ is the $\tau$-image of the categorical
   braiding $\sigma_{K_1, K_2}$.  The antisymmetric component
   evaluates to $\alpha_{\mathrm{EM}} \cdot Q_q(K_1) \cdot Q_q(K_2)$.

3. **Base propagation.**  The spatial dependence is the Green's
   function $G(c_1, c_2)$ on the base $\mathbb{P}(V)$.  In the
   archimedean completion, $\mathbb{P}^1(\mathbb{C}) \cong S^2$
   descends to flat $\mathbb{R}^3$ at low energies, giving the
   Coulomb potential:

$$
  V_{\mathrm{EM}}(r)
  \;=\;
  \alpha_{\mathrm{EM}} \cdot Q_q(K_1) \cdot Q_q(K_2)
  \cdot G(r)
  \;=\;
  \frac{q^{-1}}{[9]_q [10]_q}
  \cdot [w_1]_q \cdot [w_2]_q
  \cdot \frac{1}{r}.
$$

In the $p$-adic completion, $G(x) = |x|_p^{-1}$, giving a $p$-adic
Coulomb law with the same $\alpha_{\mathrm{EM}}$.  The coupling
constant is completion-independent; only the propagator changes.

**Remark on running.**
The formula $\alpha_{\mathrm{EM}}(q)$ gives the coupling at the
fundamental (Planck-scale) value of $q$.  At lower energies, $q$
flows under the Reeb vector field
toward $q \to 1$, and $[n]_q \to n$, so
$\alpha_{\mathrm{EM}} \to 1/(9 \times 10) = 1/90$ — a different
value.  The observed running of $\alpha_{\mathrm{EM}}$ from $1/137$
at low energy to $\sim 1/128$ near the $Z$ mass would correspond
to the flow of $q$ in the opposite direction.  The precise
relationship between $q$-flow and energy scale is determined by the
Reeb dynamics on the Bring surface.
