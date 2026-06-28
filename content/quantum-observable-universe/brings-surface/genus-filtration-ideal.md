The genus of the moduli surface is not assumed --- it is
**determined by the Iwahori--Hecke algebra**.  The QOU axioms force
$g = 4$ through a completeness condition on the irreducible
representations of $H_2(q) \oplus H_3(q)$, and the
genus-filtration ideal $\mathfrak{I}_4 = (u^5)$ is the
algebraic obstruction that kills $T_{2,p}$ for all primes
$p \geq 11$.

## Part 0: the genus is determined by the algebra

**Proposition (Genus from Hecke completeness).**
*Let $(\mathbf{C}, A, \tau)$ be a QOU with
$G = \mathrm{SU}_q(2)$.  The braiding on $V_1^{\otimes n}$
gives the Iwahori--Hecke algebra $H_n(q)$.  The relevant strand
counts are $n = 2$ and $n = 3$:*

- *$H_2(q)$ has $2$ irreducible representations
  (partitions of $2$: $(2)$ trivial, $(1,1)$ sign).*
- *$H_3(q)$ has $3$ irreducible representations
  (partitions of $3$: $(3)$, $(1,1,1)$, $(2,1)$).*
- *Total: $5$ irreps.*

*At genus $g$, the embeddable torus knots $T_{r,s}$ with
$(r-1)(s-1) \leq 2g$ and $\gcd(r,s) = 1$ are the ones whose
Jones polynomials can be evaluated on $\Sigma_g$.  Completeness
([cohomological embedding](#prop:cohomological-embedding))
requires that these evaluations **span all $5$ irrep
characters**: the evaluation matrix
$M_{ij} = \chi_{\lambda_j}(\sigma_i)$ must have rank $5$.*

*The strand counts $m \geq 4$ contribute no new knots: at genus
$g$, the constraint $(m-1)(s-1) \leq 2g$ with $m \geq 4$ and
$m < s$, $\gcd(m,s) = 1$, gives $s \leq 2g/(m-1) + 1$, which
for $m = 4$ yields $T_{4,3} = T_{3,4}$ (already counted) and
for $m \geq 5$ yields no valid $(m, s)$ pairs with $m < s$.
Therefore $H_2(q) \oplus H_3(q)$ is the complete Hecke
algebra of the QOU.*

**The genus scan.**

See [Table 1](#tbl:genus-filtration-ideal-table1-data).

*At $g = 3$: only $4$ knots are available, but $5$ irreps
must be spanned.  Rank $\leq 4 < 5$ --- incomplete.
Observability
($\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$) would be
violated: there would exist knot observables not determined
by the generators.*

*At $g = 4$: the two additional knots $T_{2,9}$ (Chebyshev
degree $4$, saturates) and $T_{3,5}$ (genus $4$, saturates)
bring the total to $6$ knots spanning $5$ irreps.
Rank $= 5$ --- complete.*

*At $g \geq 5$: $T_{2,11}$ and further knots embed, but they
add no new irreps (rank stays $5$).  These extra knots predict
**unobserved particles** --- the redundancy violates
minimality.*

*Therefore $g = 4$ is the **unique minimal genus** where the
Hecke completeness condition holds.*

## Part I: Chebyshev degree = Seifert genus

**Origin of the Chebyshev structure.**
The Iwahori--Hecke algebra $H_2(q)$ is $2$-dimensional with basis
$\{1, T\}$ and the single relation $T^2 = sT + 1$ where
$s = q - q^{-1}$.  The generator $T$ has two eigenvalues:
$q$ (symmetric channel) and $-q^{-1}$ (antisymmetric channel).
Computing $T^p$ --- the $p$-th power of the braid generator
--- reduces it via the relation:

$$
  T^p =  a_p \cdot T +  a_{p-1} \cdot \mathbf{1}
$$

The coefficients $a_n$ satisfy the recurrence
$a_{n+1} = s \cdot a_n + a_{n-1}$ with $a_0 = 0$, $a_1 = 1$.
This is the **Chebyshev recurrence**: powers of a matrix with
two eigenvalues are always Chebyshev polynomials.  Precisely,
$a_p = U_{p-1}(s/2)$, the Chebyshev polynomial of the second
kind evaluated at $s/2$, where
$U_n(\cos\varTheta) = \sin((n+1)\varTheta)/\sin\varTheta$.

For odd $p$, only even powers of $s$ appear, so writing
$u = s^2 = (q - q^{-1})^2$:

$$
  a_p(u)
  = 
  U_{p-1}\!\left(\tfrac{s}{2}\right)
  = 
  \sum_{j=0}^{(p-1)/2} c_j u^j
$$

with leading coefficient $c_{(p-1)/2} = 1$.

**The degree--genus identity.**
The algebraic complexity of the Hecke coefficient (the
polynomial degree $\deg_u a_p$) equals the topological
complexity of the knot (the Seifert genus $g(T_{2,p})$):

$$
  \deg_u a_p =  \frac{p-1}{2} =  g(T_{2,p}).
$$

Each monomial $u^k$ in $a_p$ represents the $k$-th independent
$1$-cycle of the Seifert surface $F_p$.  To realise $T_{2,p}$
as a localized knot on $\Sigma_g$, each cycle needs a target
class in $H^1(\Sigma_g)$.  When $\deg_u a_p > g$, the
polynomial encodes more topology than the surface can hold ---
the surplus monomials have no geometric home.  This is the
**Chebyshev overflow**: the Iwahori--Hecke algebra knows the knot
doesn't fit, before any surface is chosen.

## The Chebyshev table

The Hecke recurrence $a_{n+1} = s \cdot a_n + a_{n-1}$ with
$a_0 = 0$, $a_1 = 1$ gives, for odd $p$, the following
polynomials in $u = s^2 = (q - q^{-1})^2$:

See [Table 2](#tbl:genus-filtration-ideal-table2-data).

($*$: $9 = 3^2$ is not prime but $T_{2,9}$ is the degree-$2$
tower of the trefoil.)

The saturation at $a_9$ (degree $4$) and the overflow at
$a_{11}$ (degree $5$) are not coincidences --- they are the
Chebyshev reflection of the Hecke completeness condition.
The completeness scan (Part 0) shows that $g = 4$ is the
minimum genus where all $5$ irreps are spanned.  The
Chebyshev degree at the boundary is $\deg_u a_9 = 4 = g$,
and $\deg_u a_{11} = 5 = g + 1$ is the first overflow.

## Part II: the genus-filtration ideal

*Define the genus-$g$ filtration ideal
$\mathfrak{I}_g \subset \mathbb{Z}[u]$ by*

$$
  \mathfrak{I}_g
  = 
  \bigl\{ f(u) \in \mathbb{Z}[u] : \deg f > g \bigr\}
  = 
  (u^{g+1}).
$$

*A torus knot $T_{2,p}$ admits a localized knot structure on
$\Sigma_g$ if and only if $a_p \notin \mathfrak{I}_g$, i.e.,
$\deg_u a_p \leq g$.*

For $g = 4$ (as determined by Hecke completeness):
$\mathfrak{I}_4 = (u^5)$.  Every $T_{2,p}$ with $p \geq 11$
has $a_p \in \mathfrak{I}_4$ because $\deg_u a_p \geq 5$.
The ideal $(u^5)$ catches all of them simultaneously: $u^k = u^{k-5} \cdot u^5 \in (u^5)$ for all $k \geq 5$.

## Part III: Yekutieli obstruction = leading coefficient

*The Yekutieli obstruction class
$\kappa(T_{2,p}) \in H^2(\Sigma_g, \mathbb{Z})$ is
the image of the leading monomial of $a_p$ under the
projection $\pi_g \colon \mathbb{Z}[u] \to \mathbb{Z}[u]/(u^{g+1})$:*

$$
  \kappa(T_{2,p})
  = 
  \begin{cases}
    0 & \text{if } (p-1)/2 \leq g \quad
      (\text{lifts: } a_p \text{ fits in } H^1(\Sigma_g)), \\[6pt]
    c_{(p-1)/2} \cdot [u^{(p-1)/2}] \neq 0 &
      \text{if } (p-1)/2 > g \quad
      (\text{obstructed: overflow}).
  \end{cases}
$$

*Since $c_{(p-1)/2} = 1$ for all odd $p$, the obstruction is
nonzero for every prime $p \geq 2g + 3 = 11$.*

