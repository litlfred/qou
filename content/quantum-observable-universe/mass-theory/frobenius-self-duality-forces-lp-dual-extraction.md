**Proposition.**
*The Markov trace $\tau$ on $H_n(R,q)$ is a non-degenerate
symmetric bilinear pairing. This makes $(H_n(R,q),\tau)$ a
Frobenius algebra, hence canonically isomorphic to its
$R$-linear dual. Under this isomorphism, the primal LP variable
$x \in H_n$ and the dual LP variable $u \in H_n^*$ live in the
same space, and the Observation Frame
$\mathrm{Obs}_\tau(a) := \tau(a \cdot -)$ extracts the
shadow-price representative of every observable.*

**Corollary (mass-formula coefficients are LP-dual variables).**
By [mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price),
every QOU mass-formula coefficient $C_\lambda$ at every
Hecke level $k$ is the τ-extraction of a shadow price; by the
proposition above, this is the *only* form a τ-extracted
observable can take in a Frobenius-self-dual category. The
mass formula is therefore canonically a sum of LP-dual
variables:

$$
  \mathfrak{m}(\varrho) = \sum_\ell u^{(\ell)*}
$$

where $u^{(\ell)*}$ is the optimal LP-dual at filtration level
$\ell$ (see
mass-formula-iterative-lp-dual).

**Remark (categorical content).** The Frobenius self-duality
holds at the categorical level: the rigid monoidal category
$\mathbf{Rep}(H_n(R,q))$ is self-dual under the
$\tau$-pairing, and $\tau$ is precisely the categorical trace
$\mathrm{tr}_C$ on the unit object. The "primal vs. dual"
distinction in the LP is a $K$-theoretic shadow of the
categorical self-duality; there is no other choice.
