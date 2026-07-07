Let $(\mathbf{C}, A, \tau)$ define a [quantum universe](#def:quantum-universe) sustaining a [brane tower](#def:recursive-brane-tower) $\{A_n\}_{n \geq 0}$ alongside [quantum characteristic classes](#def:quantum-characteristic-classes) $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$.

The **NS obstruction** governing $(\mathbf{C}, A, \tau)$ evaluates as the class

$$
  \mathrm{NS}(A)
  = 
  \kappa_0\big|_\Sigma
   \in 
  H^2(\Sigma, \mathcal{B}),
$$

with $\Sigma$ denoting the specific collision locus of a generic vortex pair. $\kappa_0 = e(\xi)$ denotes the rigid Euler class of the Reeb bundle tracking $\mathrm{tr}(\kappa_0) = \chi(A)$.

We categorise $(\mathbf{C}, A, \tau)$ as:

- **NS-regular** if $\mathrm{NS}(A) = 0$. The categorical obstruction zeroes out; the purely classical Navier--Stokes equation (specialised via $q = 1$ from the [q-NS system](#def:q-navier-stokes)) processes all smooth initial data into smooth global solutions.
- **NS-singular** if $\mathrm{NS}(A) \neq 0$. The obstruction holds firm; the classical Navier--Stokes equation inevitably ingests smooth initial data and produces a strict singularity in finite time.

The NS obstruction tracks only the rigid categorical properties of $(\mathbf{C}, A, \tau)$, relying specifically on $\chi(A)$. It operates independently of the selected substrate section $q$ and ignores specific initial data.

| $\chi(A)$ | $\mathrm{NS}(A)$ | Status |
|---|---|---|
| $\neq 0$ | $\neq 0$ (sustained via Kummer non-divisibility) | **NS-singular** |
| $= 0$ | $= 0$ | **NS-regular** |

The defining observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ acts as a **sufficient condition** guaranteeing $\chi(A) \neq 0$ (forcing rigid irreducibility on the adjoint representation to guarantee a nonzero Euler class). It is a diagnostic, not an assumption.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
