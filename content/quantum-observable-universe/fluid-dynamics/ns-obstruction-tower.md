**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"NS obstruction tower").**

Let $(\mathbf{C}, A, \tau)$ be a QOU with Euler characteristic
$\chi(A)$ and [Yekutieli obstruction
classes](#def:quantum-characteristic-classes)
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$.  Let
$\Sigma \subset \mathcal{S}$ be the collision locus of two
anti-parallel vortex filaments.

The [boundary observability](#def:ns-regular-qou)
$\mathrm{Obs}_\partial(A)$ is measured by the restriction of the
Yekutieli obstruction classes to the collision locus:

$$
  \mathrm{Obs}_\partial(A)
  = 
  \ker\!\left(
    \bigoplus_{n \geq 0}
    H^2(\mathcal{S}, \mathcal{B})
    \xrightarrow{ \mathrm{res}_\Sigma}
    \bigoplus_{n \geq 0}
    H^2(\Sigma, \mathcal{B}|_\Sigma)
  \right).
$$

The QOU is [NS-singular](#def:ns-regular-qou) (blowup) iff
$\mathrm{res}_\Sigma(\kappa_n) \neq 0$ for some $n$; NS-regular
iff $\mathrm{res}_\Sigma(\kappa_n) = 0$ for all $n$.

**(a) Where the obstruction sits.**

By the [QU-to-QOU theorem](#thm:qu-to-qou), the first obstruction
is $\kappa_0 = e(\xi)$, the Euler class of the Reeb bundle, with
$\mathrm{tr}(\kappa_0) = \chi(A)$.  The obstruction at level $n$
is

$$
  \kappa_n
  = 
  \kappa_0
  + 
  \delta_n,
  \qquad
  \delta_n \in \mathrm{im}\!\bigl(
    H^2(\mathcal{S}, \mathcal{O}_\mathcal{S})
    \to H^2(\mathcal{S}, \mathcal{B})
  \bigr),
$$

where $\delta_n$ is the jet correction at level $n$.  By the
perpetual obstruction ([QU-to-QOU](#thm:qu-to-qou) item 3,
strengthened by [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction)
to a place-by-place non-vanishing of the substrate's motivic
Galois character), $\kappa_0$ and $\delta_n$ live in complementary
subgroups when $\kappa_0$ is non-torsion, so $\kappa_n \neq 0$
for all $n$.

**(b) Restriction to the collision locus.**

The collision locus $\Sigma$ is a 1-dimensional submanifold
(line segment) with $H^2(\Sigma, \mathcal{B}|_\Sigma)$ computed
by the long exact sequence of the pair
$(\mathcal{S}, \mathcal{S} \setminus \Sigma)$:

$$
  \cdots \to
  H^1(\mathcal{S} \setminus \Sigma, \mathcal{B})
  \xrightarrow{\partial}
  H^2_\Sigma(\mathcal{S}, \mathcal{B})
   \to 
  H^2(\mathcal{S}, \mathcal{B})
  \xrightarrow{ \mathrm{res}}
  H^2(\mathcal{S} \setminus \Sigma, \mathcal{B})
  \to \cdots
$$

The obstruction restricts nontrivially to $\Sigma$ iff
$\kappa_n$ is **not** in the image of the restriction map from
$\mathcal{S} \setminus \Sigma$.  Equivalently, the connecting
homomorphism $\partial$ detects it: $\kappa_n|_\Sigma \neq 0$
iff $\kappa_n$ has nontrivial **local cohomology** support
at $\Sigma$.

**(c) Local cohomology computation.**

The [local cohomology](#def:local-cohomology-group) at a point
$p \in \Sigma$ is

$$
  H^1_{\mathfrak{m}_p}(A)
  = 
  R^1\Gamma_{\mathfrak{m}_p}(A).
$$

For the anti-parallel vortex pair, each filament carries the
fundamental representation $V_{1/2}$ of
$\mathrm{SU}_q(2)$.  At the collision point $p$ where
both filaments meet, the local cohomology receives
contributions from both:

$$
  H^1_{\mathfrak{m}_p}(A)
  = 
  V_{1/2}^{(1)} \oplus V_{1/2}^{(2)},
$$

a 4-dimensional space.  This is **nonzero** iff both filaments
contribute nontrivial local sections at $p$ — i.e. iff the
vortex cores have not dissolved.

**(d) Connection to core aspect ratio.**

By the [core-Levi equivalence](#prop:core-levi-form), the
local cohomology is nonzero iff the Levi form is non-degenerate
at $p$.  Explicitly:

$$
  H^1_{\mathfrak{m}_p}(A) \neq 0
  \quad\Longleftrightarrow\quad
  \lambda_\parallel(p) > 0
   \text{ and }
  \lambda_\perp(p) > 0
  \quad\Longleftrightarrow\quad
  \kappa(p) = a_\perp/a_\parallel \in (0, \infty).
$$

When the core flattens ($\kappa \to 0$ or $\kappa \to \infty$),
one Levi eigenvalue vanishes, the local cohomology collapses
from $V_{1/2}^{\oplus 2}$ to a quotient, and the obstruction
class $\kappa_n|_\Sigma$ deforms toward zero.

**(e) The NS obstruction as an Euler-class residue.**

Combining (a)--(d): the NS obstruction at level $n$ restricted
to the collision locus is

$$
  \kappa_n\big|_\Sigma
  = 
  \mathrm{lk}(\varrho_1, \varrho_2)
  \cdot e(\xi)\big|_\Sigma
  +  \delta_n\big|_\Sigma,
$$

where $\mathrm{lk}(\varrho_1, \varrho_2)$ is the linking number
of the two filaments and $e(\xi)|_\Sigma$ is the Euler class of
the Reeb bundle restricted to $\Sigma$.

For the Descartes universe ($\chi(A) = -6$, Bring's surface):
$e(\xi) = -6 \cdot [\Sigma_4]$ in $H^2(\Sigma_4, \mathbb{Z})$.
The restriction $e(\xi)|_\Sigma$ is nonzero when $\Sigma$ is
homologically nontrivial in $\Sigma_4$, which holds for the
anti-parallel pair (linking number 1).

**Summary.** The NS obstruction is measured at every level of
the Yekutieli tower by restricting $\kappa_n$ to the collision
locus $\Sigma$.  It is nonzero (NS-singular, blowup) iff the
local cohomology $H^1_{\mathfrak{m}_p}(A)$ is nonzero at
collision points, which holds iff the Levi form is
non-degenerate (core aspect ratio bounded).  Computing
whether $\kappa_n|_\Sigma$ vanishes or persists as $q \to 1$
is the [Levi degeneracy conjecture](#conj:levi-degeneracy).
