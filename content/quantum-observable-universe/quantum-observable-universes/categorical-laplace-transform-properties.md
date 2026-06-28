This remark collects the base-ring, three-context, and $q$-heat
realisations of the
[categorical Laplace transform](#def\:categorical-laplace).

**Base-ring independence.**  Because $\exp_q(-s\cdot)$ is defined
abstractly as a grouplike of $\mathcal{H}_q$ — not as a convergent series —
$\mathcal{L}$ makes sense over any base ring $R$ where $\mathcal{H}_q$ has the
grouplike, i.e. anywhere $q \ne 1$ and $s$ is algebraic.  The familiar
integral

$$
  \mathcal{L}[f](s) \;=\; \int_0^\infty e^{-st} f(t)  dt
  \qquad (\mathbb{R}\text{-realisation})
$$

is recovered by evaluating the abstract pairing against the
archimedean realisation of the grouplike ($q \to 1$, $R = \mathbb{C}$,
Haar measure on $\mathbb{R}_{\ge 0}$).  Over $\mathbb{F}_p$ or
$\mathbb{Q}_p$ the integral is replaced by a sum over Frobenius
orbits, but $\mathcal{L}$ itself is unchanged.

**Three-context behaviour.**  Paralleling $\exp_q$
([finite-field obstruction](#rem\:q-exp-finite-field-obstruction),
[$p$-adic $\exp_q$](#rem\:q-exp-p-adic)):

* **$\mathbb{F}_p$.**  $\mathcal{L}$ becomes a finite sum over the
  grouplike spectrum $\mathrm{Spec}_{\mathbb{F}_p}(G(\mathcal{H}_q))$, which is
  finite because $G(\mathcal{H}_q) \otimes \mathbb{F}_p$ is an étale group scheme
  of bounded rank.  This is the Gauss-sum avatar: pairing against
  $\exp_q^{(p)}$ over a finite base gives a finite character sum, and
  monoidality of $\mathcal{L}$ is the product formula for Gauss sums.
* **$\mathbb{Q}_p$.**  $\mathcal{L}$ is a continuous functional on
  locally constant $f \colon p\mathbb{Z}_p \to \mathbb{Q}_p$, computed
  as a $p$-adic integral against the Witt-lifted $\exp_q$.  The monoidal
  property $\mathcal{L}[f \ast_q g] = \mathcal{L}[f] \cdot \mathcal{L}[g]$
  is Amice--Velu theory: the Mellin transform of a $p$-adic measure.
* **$\mathbb{C}_p$.**  $\mathcal{L}$ extends to rigid-analytic $f$ on
  the open disc $v_p(x) > 1/(p-1)$; beyond this disc the pairing is
  purely formal, $\mathcal{L}[f](s) \in \mathbb{C}_p[\![s]\!]$ with no
  evaluation at concrete $s$.  This is the categorical $p$-adic
  Laplace transform.

**Role in the $q$-heat story.**  The $q$-heat equation
([$q$-heat equation](#def\:q-heat-equation)) $\partial_t u = -\Delta_q u$
is turned by $\mathcal{L}$ into a spectral equation: differentiation
in $t$ maps to multiplication by $s$ (plus initial data), so

$$
  s  \hat{u}(s) - u_0
  \;=\;
  -\widehat{\Delta_q}  \hat{u}(s),
$$

yielding the *resolvent of the $q$-Laplacian*,
$\hat{u}(s) = (s + \widehat{\Delta_q})^{-1} u_0$
([$q$-resolvent](#def\:q-resolvent)).  The heat kernel is
the inverse Laplace of the resolvent, and lives in the archimedean
realisation.
