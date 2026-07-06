**Setup (commutative ring of coefficients).**
Throughout, the categorical structure is enriched over the
commutative ring

$$
  R \;=\; \mathbb{Z}\bigl[q^{\pm 1/2},\, (q - q^{-1})^{-1}\bigr].
$$

We **do not** work over $\mathbb{C}$; every quantity below is defined
in $R$ and survives any ring map $\iota \colon R \to k$ with $k$ a
target commutative ring (archimedean: $\mathbb{R}$; $p$-adic:
$\mathbb{Q}_p$; finite: $\mathbb{F}_\ell$).

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe over $R$ with
substrate parameter $q$ and force-carrier generators $T_{2,9}$
(crossing number $c_s = 9$) and $T_{3,5}$ (crossing number
$c_w = 10$) — uniquely determined by the genus-$4$ classification
above.  Then the electromagnetic fine structure constant, defined as
the $\tau$-trace of the singlet idempotent $e_-$ normalised by the
force-carrier categorical complexity, is

$$
  \alpha_{\mathrm{EM}}(q)
  = 
  \frac{q^{-1}}{[c_s]_q \cdot [c_w]_q}
  = 
  \frac{q^{-1}}{[9]_q \cdot [10]_q}
$$

where $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ is the $q$-integer.

Although written as a quotient, the projection is **division-free over
the integral Laurent subring** $\mathbb{Z}[q, q^{-1}] \subset R$: since
$[9]_q$ and $[10]_q$ are genuine Laurent polynomials, the content of the
proposition is the cleared-denominator relation

$$
  [9]_q \cdot [10]_q \cdot \alpha_{\mathrm{EM}} \;=\; q^{-1},
$$

which already lives in $\mathbb{Z}[q, q^{-1}]$ — no localisation at
$(q - q^{-1})$ is required to *state* the coupling, only to *solve* the
relation for $\alpha_{\mathrm{EM}}$ (the product $[9]_q[10]_q$ is not a
unit of $\mathbb{Z}[q, q^{-1}]$).  This is the form carried by the
formalisation, mirroring the $2\,E_{\mathrm{cross}} = q - q^{-1}$
convention used elsewhere to keep cross-section data in the ground ring.

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

*Layer 2: Coupling strength (singlet idempotent).*
The two-strand spectral completeness theorem
([completeness](#thm:em-spectral-completeness)) decomposes the
braiding into central idempotents:

$$
  c_{A,A} \;=\; q^{1/2}\, e_+ \,-\, q^{-1/2}\, e_-,
  \qquad e_+ + e_- = \mathrm{id}_{A \otimes A},\;\; e_+ e_- = 0.
$$

The two eigenvalues $\{q^{1/2},\, -q^{-1/2}\} \subset R$ are the
**only** spectral data of $c_{A,A}$.  The singlet $e_-$ projects onto
the unique copy of the unit object $\mathbf{1} \subset A \otimes A$
(the antisymmetric channel $\Lambda^2 A$, of $R$-rank $1$).  Its
fibre-functor trace evaluates to

$$
  |\mathrm{tr}_\tau(e_-)|^2 \;=\; q^{-1} \,\in\, R.
$$

This is the **bare gauge coupling**: by uniqueness of the singlet
([completeness corollary](#thm:em-spectral-completeness)), it is
the *full* scalar exchange amplitude — there is no second EM-like
channel to add.  It is a unit in $R$, with no transcendental
content.

*Layer 3: Force-carrier complexity (Bring-forced denominator).*
By the genus-$4$ uniqueness theorem
([Bring uniqueness](#prop:force-carrier-bring-uniqueness)), the
force-carrier sector of any Bring-supported QOU is *exactly* the
two-element set $\{T_{2,9}, T_{3,5}\}$ — no choice is being made.
Their categorical $q$-dimensions are $\dim_q T_{2,9} = [9]_q$ and
$\dim_q T_{3,5} = [10]_q$, both elements of $R$.  The strong/weak
labelling ([force identification](#rem:force-knot-identification))
selects which knot mediates which sector but does not affect the
product $[9]_q \cdot [10]_q$, which is the categorical complexity
of the entire force-carrier object.  The electromagnetic coupling
is the singlet trace divided by this forced normalisation:

$$
  \alpha_{\mathrm{EM}}
  \;=\;
  \frac{|\mathrm{tr}_\tau(e_-)|^2}{\dim_q T_{2,9} \cdot \dim_q T_{3,5}}
  \;=\;
  \frac{q^{-1}}{[9]_q \cdot [10]_q} \,\in\, R.
$$

The numerator $q^{-1}$ is the singlet idempotent's squared trace —
the unique scalar coupling amplitude permitted by spectral
completeness.  The denominator $[9]_q \cdot [10]_q$ is the
$q$-categorical complexity of the unique pair of genus-$4$ torus
knots (Bring uniqueness).  The ratio is the fraction of the total
two-strand interaction that is *scalar*, i.e.\ electromagnetic.
**Both ingredients are forced** — there is no freedom in either
the numerator (one singlet) or the denominator (one Bring-saturating
torus pair).

**Finiteness and completeness in $R$.**

Every ingredient lives in the commutative ring $R$:

* The charge $Q_q = [w]_q \in R$ is a ratio of $q$-powers — no
  integral.
* The coupling $q^{-1} \in R^\times$ is the singlet idempotent's
  squared $\tau$-trace — by spectral completeness
  ([completeness](#thm:em-spectral-completeness)) the *only*
  scalar two-strand amplitude.
* The normalisation $[9]_q \cdot [10]_q \in R$ is the categorical
  complexity of the *unique* genus-$4$ torus pair — by Bring
  uniqueness ([Bring uniqueness](#prop:force-carrier-bring-uniqueness))
  the *only* available denominator.
* The spatial dependence (Coulomb $1/r^2$) is added by the
  Green's function of the base manifold, external to
  $\alpha_{\mathrm{EM}}$.

Plancherel completeness $w_+ + w_- = 1$ certifies that no scalar
channel has been missed: the Frobenius mass of $\mathrm{End}(A
\otimes A)$ is exhausted by these two idempotents.  The formula
makes sense over any specialisation $\iota \colon R \to k$:
archimedean ($k = \mathbb{R}$), $p$-adic ($k = \mathbb{Q}_p$), or
finite ($k = \mathbb{F}_\ell$).  The fine structure constant is a
**ring-theoretic invariant** of the Descartes universe, not a
continuous parameter requiring measurement.
