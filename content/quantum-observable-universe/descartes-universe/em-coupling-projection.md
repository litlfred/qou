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
the electromagnetic fine structure constant is the antisymmetric
eigenvalue of the $R$-matrix normalised by the $q$-deformed crossing
complexities of the force-carrying sector:

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

**Categorical status of the formula.**

The coupling $\alpha$ is **not** the Markov trace of any braid
word.  It is assembled from representation-theoretic quantities:

- $q^{-1}$ = antisymmetric eigenvalue squared (from the $R$-matrix)
- $[9]_q$ = quantum dimension / character of $T_{2,9}$
- $[10]_q$ = quantum dimension / character of $T_{3,5}$

This contrasts with mass, where the Markov trace of the nuclear
braid is the central object.  The electromagnetic coupling is a
ratio of **eigenvalues and characters**, not a trace.

**Open problem: the 0.155% gap.**

The bare formula $\alpha^{-1} = q \cdot [9]_q \cdot [10]_q = 136.823$
agrees with CODATA to $0.155\%$.  By analogy with the descent
decomposition of mass, this gap should arise from exceptional
divisor corrections to the bare coupling — the transient component
of the descent involution $\hat{\tau}$ applied to the EM
endomorphism $P_{\mathrm{anti}}$.

For mass, the descent decomposition gives:

$$
  \mathfrak{m} = \underbrace{\mathrm{Hol}(\varrho_0)}_{\text{base / volume}}
  + \underbrace{\sum_i \Phi_q(z_i)}_{\text{exceptional divisors}}.
$$

For coupling, the analogous structure would be:

$$
  \frac{1}{\alpha} = \underbrace{q \cdot [9]_q \cdot [10]_q}_{\text{bare coupling}}
  + \underbrace{\text{(divisor corrections)}}_{\text{0.213 gap}}.
$$

The divisor corrections require the Frobenius form $\int_A$ evaluated
on the force-carrier braids $T_{2,9} \cup T_{3,5}$ on Bring's
surface, respecting the self-duality $A \cong A^{\vee}$ through the
categorical trace $S = \mathrm{ev} \circ (\mathrm{id} \otimes \Phi) \circ \mathrm{coev}$.

The specific computation — the blow-up structure at the crossing
degeneracies where $T_{2,9}$ and $T_{3,5}$ embed on the genus-$4$
surface — has not yet been carried out.
