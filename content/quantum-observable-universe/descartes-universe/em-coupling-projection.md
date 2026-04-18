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
  = 
  \frac{q^{-1}}{[c_s]_q \cdot [c_w]_q}
  = 
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
  Q_q(K) =  [w(K)]_q
  =  \frac{q^{w(K)} - q^{-w(K)}}{q - q^{-1}}
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
  = 
  \frac{|\mathrm{tr}_\tau(\sigma_{\mathrm{anti}})|^2}{[c_s]_q \cdot [c_w]_q}
  = 
  \frac{q^{-1}}{[9]_q \cdot [10]_q}.
$$

The denominator $[9]_q \cdot [10]_q$ is the product of the
$q$-crossing complexities of the strong and weak sectors.  The
numerator $q^{-1}$ is the antisymmetric braiding eigenvalue.
The ratio gives the fraction of the total interaction that is
electromagnetic.

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

**Remark on the classical limit.**
As $q \to 1$, $[n]_q \to n$, and
$\alpha_{\mathrm{EM}} \to 1/(9 \times 10) = 1/90$.  The observed
value $\alpha^{-1} \approx 137$ requires $q > 1$; the departure
from the classical limit is what makes the coupling weaker than
$1/90$.

**Descent decomposition: Chern-Simons correction.**

The bare formula $\alpha^{-1} = q \cdot [9]_q \cdot [10]_q$ gives
the **base holonomy** of the electromagnetic endomorphism — the
bulk coupling from the $R$-matrix eigenvalue times the $q$-deformed
crossing complexities.  This is the analogue of the volume term
$\lambda_V \cdot A$ in the mass formula.

The full coupling receives an **exceptional divisor correction**
from the Chern-Simons invariants of the force-carrier torus knots
$T_{2,9}$ and $T_{3,5}$
([EM coupling Chern-Simons](#prop:em-coupling-chern-simons)):

$$
  \frac{1}{\alpha_{\mathrm{EM}}}
  =
  q \cdot [9]_q \cdot [10]_q
  \cdot \bigl(1 + c_1 + c_1^2 \cdot \kappa\bigr)
$$

where

$$
  c_1
  =
  \frac{\bigl(\mathrm{CS}(T_{2,9}) + \mathrm{CS}(T_{3,5})\bigr)
        \cdot \tfrac{[2]_q}{2} \cdot \hbar_q^2}
       {q \cdot [9]_q \cdot [10]_q}
$$

and $\kappa = \det G_{\mathrm{CS}}^{\mathrm{cl}}
/ \det G_{\mathrm{CS}}^{q} \approx 1.722$ is the Gram determinant
ratio of the classical and $q$-deformed Chern–Simons pairing,
capturing self-dual damping at the second jet level.

The Chern-Simons invariants of torus knots
$T_{m,n}$ are given by the universal formula

$$
  \mathrm{CS}(T_{m,n})
  =
  \frac{\pi^2 (m^2 - 1)(n^2 - 1)}{12\,m\,n},
$$

yielding $\mathrm{CS}(T_{2,9}) = \pi^2 \cdot \tfrac{10}{9}$ and
$\mathrm{CS}(T_{3,5}) = \pi^2 \cdot \tfrac{16}{15}$.  The quantum
Planck constant is $\hbar_q = (q - 1)/q$.

**Numerical evaluation.**

| Quantity | Value |
|----------|-------|
| Base: $q \cdot [9]_q \cdot [10]_q$ | $136.823$ |
| $\mathrm{CS}(T_{2,9})$ | $\pi^2 \cdot 10/9 \approx 10.966$ |
| $\mathrm{CS}(T_{3,5})$ | $\pi^2 \cdot 16/15 \approx 10.528$ |
| $\hbar_q^2$ | $0.009817$ |
| $[2]_q / 2$ | $1.00545$ |
| $c_1$ | $0.001551$ |
| $\kappa$ | $1.722$ |
| $\alpha^{-1}_{\mathrm{CS}}$ | $\mathbf{137.036}$ |
| CODATA 2018 | $137.035999084(21)$ |
| Residual | $-2.1\;\mathrm{ppm}$ |

The Chern-Simons correction reduces the discrepancy from $0.155\%$
(bare formula) to $2.1\;\mathrm{ppm}$ — a $120\times$ improvement
with zero additional parameters.

**Physical interpretation.**

The descent decomposition of the coupling mirrors that of the mass:

| | Mass | Coupling |
|---|---|---|
| **Base term** | $\lambda_V \cdot A$ (volume holonomy) | $q \cdot [9]_q \cdot [10]_q$ ($R$-matrix eigenvalue $\times$ $q$-dimensions) |
| **Divisor correction** | $-\lambda_S \cdot A^{2/3}$ (surface nucleons) | $(\mathrm{CS}_1 + \mathrm{CS}_2) \cdot \hbar_q^2$ (force-carrier blow-up centres) |
| **Sign** | Negative (reduces binding) | Positive (increases $1/\alpha$) |
| **Origin** | Nuclear boundary (fewer neighbors) | Crossing degeneracies on Bring's surface |

The correction is positive because the force-carrier braids
$T_{2,9}$ and $T_{3,5}$, embedded on the genus-$4$ Bring's surface,
have crossing degeneracies that **screen** the bare electromagnetic
charge, increasing $1/\alpha$ from the bare value.
