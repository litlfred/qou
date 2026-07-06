Let $(\mathbf{C}, A, \tau)$ be a
[quantum universe](#def:quantum-universe) with
[brane tower](#def:recursive-brane-tower) $\{A_n\}_{n \geq 0}$
and [quantum characteristic classes](#def:quantum-characteristic-classes)
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$.

The **NS obstruction** of $(\mathbf{C}, A, \tau)$ is the class

$$
  \mathrm{NS}(A)
  = 
  \kappa_0\big|_\Sigma
   \in 
  H^2(\Sigma, \mathcal{B}),
$$

where $\Sigma$ is the collision locus of a generic vortex pair
and $\kappa_0 = e(\xi)$ is the Euler class of the Reeb bundle
with $\mathrm{tr}(\kappa_0) = \chi(A)$.

We say that $(\mathbf{C}, A, \tau)$ is:

- **NS-regular** if $\mathrm{NS}(A) = 0$: the obstruction
  vanishes and the classical Navier--Stokes equation (the
  $q = 1$ specialisation of the
  [q-NS system](#def:q-navier-stokes)) admits smooth global
  solutions for all smooth initial data.

- **NS-singular** if $\mathrm{NS}(A) \neq 0$: the obstruction
  persists and the classical Navier--Stokes equation admits
  smooth initial data for which the solution develops a
  singularity in finite time.

The NS obstruction depends only on the categorical data
$(\mathbf{C}, A, \tau)$ — specifically on $\chi(A)$ — and not
on the substrate section $q$ or on any particular initial data.
Different quantum universes may have different NS status:

| $\chi(A)$ | $\mathrm{NS}(A)$ | Status |
|---|---|---|
| $\neq 0$ | $\neq 0$ (Kummer non-divisibility) | **NS-singular** |
| $= 0$ | $= 0$ | **NS-regular** |

The observability axiom
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ is a
**sufficient condition** for $\chi(A) \neq 0$ (it forces
irreducibility of the adjoint representation, which gives
nonzero Euler class).  It is not assumed in this definition;
it is a diagnostic.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
