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

- **NS-regular** if $\mathrm{NS}(A) = 0$;
- **NS-singular** if $\mathrm{NS}(A) \neq 0$.

These are labels for the categorical class only. Neither implies a statement about the classical Navier--Stokes equation; in particular, $\mathrm{NS}(A) = 0$ does not establish global regularity of classical solutions.

The NS obstruction tracks only the rigid categorical properties of $(\mathbf{C}, A, \tau)$. It operates independently of the selected substrate section $q$ and ignores specific initial data.

**The classification is currently degenerate.** The collision locus $\Sigma$ is one-dimensional, so $H^2(\Sigma, \mathcal{B}) = 0$ and $\mathrm{NS}(A) = \kappa_0|_\Sigma = 0$ for every quantum universe, whatever $\chi(A)$:

| $\chi(A)$ | $\mathrm{NS}(A)$ | Status |
|---|---|---|
| $\neq 0$ | $= 0$ | NS-regular (label only) |
| $= 0$ | $= 0$ | NS-regular (label only) |

An earlier version of this table assigned $\mathrm{NS}(A) \neq 0$ to $\chi(A) \neq 0$ by Kummer non-divisibility. The Kummer class $\chi(A) \bmod n$ is a global class on the surface and restricts to zero on $\Sigma$; see the [Descartes theorem](#thm:ns-singularity-descartes), item 3. Defining a non-degenerate invariant is open.

The defining observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ acts as a **sufficient condition** guaranteeing $\chi(A) \neq 0$ (forcing rigid irreducibility on the adjoint representation to guarantee a nonzero Euler class). It is a diagnostic, not an assumption.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
