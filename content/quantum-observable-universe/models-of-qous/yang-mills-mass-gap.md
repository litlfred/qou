**Conjecture (Yang--Mills existence and mass gap, categorical
formulation).**
*Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) over a
commutative ring $R$ with substrate parameter $q > 1$.  Let
$\nabla$ be a ([categorical connection](#def:categorical-connection)) on
the Frobenius--Hopf object $A$ with curvature $F_\nabla = \nabla^2$,
and let $\mathfrak{S}_q[\nabla]$ be the
([$q$-weighted Yang--Mills--Levi functional](#def:q-yang-mills-levi)).
Let $\Omega_0 \colon R \to \mathrm{End}_{\mathbf{C}}(A)$ be the
([vacuum state](#prop:vacuum-state)) --- the unique
$G_q$-invariant functional on the direct limit algebra
$\mathcal{A}_\infty = \varinjlim \mathrm{End}_{\mathbf{C}}(A_n)$.*

*Then:*

1. **Existence.**  *There exists a connection $\nabla$ that is a
   critical point of $\mathfrak{S}_q[\nabla]$ (a categorical Yang--Mills
   connection), and the vacuum state $\Omega_0$ extends to a
   positive-definite sesquilinear form on the Hilbert completion
   $\overline{\mathcal{A}_\infty}$, defining a physical Hilbert
   space $\mathcal{H}_q$.*

2. **Mass gap.**  *Every non-vacuum excitation
   $\varrho \colon \mathbf{1} \to A$ in the spectrum of the
   categorical transfer matrix
   $\mathcal{T}_q \colon \mathrm{End}_{\mathbf{C}}(A_n)
   \to \mathrm{End}_{\mathbf{C}}(A_n)$
   satisfies*

$$
  \mathfrak{m}(\varrho)  \geq  \Delta_q  >  0,
$$

*where $\mathfrak{m}(\varrho)$ is the categorical mass
([mass identity](#def:mass-identity)) and $\Delta_q$ is a
strictly positive constant depending only on $q$ and the
Frobenius--Hopf structure of $A$.  Equivalently, the two-point
function*

$$
  \bigl\langle
  \tau(\varrho(t)),
  \tau(\varrho(0))
  \bigr\rangle_{\Omega_0}
   \sim 
  \sum_{n \geq 0}
  A_n \exp\!\bigl(-\Delta_n t\bigr)
  \qquad (t \to \infty)
$$

*has $\Delta_0 = \Delta_q > 0$: there is no massless excitation
above the vacuum.*

**Translation from the classical problem.**
The classical Yang--Mills millennium problem asks for the existence
of a quantum Yang--Mills theory on $\mathbb{R}^4$ with compact
simple gauge group $G$, satisfying the Wightman axioms, and having
a strictly positive mass gap $\Delta > 0$ in the energy spectrum.

In the QOU framework, the translation is:

See [Table](#tbl:yang-mills-mass-gap-table-data).

**Why the categorical setting is natural.**
The mass gap is a topological consequence of the Frobenius--Hopf
structure: the categorical mass $\mathfrak{m}(\varrho)$ is computed
via the trace-norm through the comultiplication $\Delta$, and the
topological decomposition ([topological mass](#thm:topological-mass))
shows that every non-trivial vortex acquires at least one crossing
energy $\mathfrak{E}_\times(q) = \tfrac{1}{2}(q - q^{-1}) > 0$
from the Skein relation.  In particular, the mass gap is bounded
below by the minimum crossing energy:

$$
  \Delta_q
   \geq 
  \mathfrak{E}_\times(q) \cdot (q - 1)^2
  = 
  \tfrac{1}{2}(q - q^{-1})(q - 1)^2
   >  0
  \quad\text{for all } q > 1.
$$

The positivity of $\Delta_q$ for $q > 1$ is the categorical
shadow of confinement: the deformation parameter $q \neq 1$
breaks the classical conformal symmetry that would allow massless
excitations, and the Skein relation forces every non-trivial
braid word to carry strictly positive crossing energy.

**The $\mathbb{G}_m$-torsion obstruction.**
The mass gap is a regular function on
$\mathbb{G}_m = \mathrm{Spec}\mathbb{Z}[q, q^{-1}]$
([substrate as $\mathbb{G}_m$-section](#rem:substrate-gm-torsion)).
It vanishes precisely on the 2-torsion subgroup
$\mu_2 = \{1, -1\}$, and is strictly positive on the
non-torsion locus $(1, \infty) \subset \mathbb{G}_m(\mathbb{R})$.
The [not-root-of-unity axiom](#def:substrate-parameter) ensures
$q \notin \mu_\infty$, placing the substrate parameter in the
region where the gap is positive.

The [Kummer filtration](#rem:kummer-filtration-obstruction) of the
obstruction space $H^2(\mathcal{S}, \mathbb{G}_m)$ provides the
common algebraic framework: the mass gap and the
[classical limit obstruction](#def:classical-limit-obstruction)
both reduce to divisibility of
$\chi(A)$ in the Kummer tower.  Since $\chi(A) = -6$ for the
Descartes universe, the
[obstruction is one-dimensional](#thm:qou-obstruction-reduction)
and persists at all primes $> 3$.

**Relation to confinement.**
In the archimedean realisation, the mass gap implies that
the lightest glueball (the simplest non-trivial closed vortex
$\varrho \colon \mathbf{1} \to A$ with no quark endpoints) has
mass $\mathfrak{m}_{\mathrm{glue}} \geq \Delta_q > 0$.  Since
isolated colour charges would require a vortex of infinite
length (and hence infinite mass), confinement follows: all
finite-energy excitations are colour singlets.
