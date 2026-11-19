Assume $(\mathbf{C}, A, \tau)$ represents a valid quantum universe placing $A$ on the classical 2-torus $\Sigma_1$ (genus $g = 1$). Its Euler characteristic is

$$
  \chi(A) = 2 - 2g = 0.
$$

**The global NS obstruction vanishes.**
Under the global surface definition ([NS-regular QOU](#def:ns-regular-qou)), the NS obstruction is the global Euler class of the Reeb bundle $\xi$ on $\mathcal{S} = \Sigma_1$, whose degree is $\deg e(\xi) = \mathrm{tr}(\kappa_0) = \chi(A) = 0$. Hence the global class vanishes directly in $H^2(\Sigma_1, \mathbb{Z}) \cong \mathbb{Z}$:

$$
  \mathrm{NS}(A) = e(\xi) = 0 \in H^2(\Sigma_1, \mathbb{Z}),
$$

and for every integer $n \geq 1$ its Kummer reduction $\chi(A) \bmod n \in H^2(\Sigma_1, \mu_n)$ vanishes identically ([Kummer specialisation](#prop:ns-kummer-specialisation)). Because $\mathrm{NS}(A)$ is evaluated on the global surface $\mathcal{S}$ rather than on a 1D collision locus $\Sigma$ (where $H^2(\Sigma, \cdot) = 0$ vanishes on every curve), $\mathrm{NS}(A) = 0$ on $\Sigma_1$ contrasts non-degenerately with $\mathrm{NS}(A) = -6 \neq 0$ on Bring's surface $\Sigma_4$.

The torus quantum universe is therefore categorically **NS-regular**.

**Physical meaning and 2D vs 3D Navier--Stokes scope.**
Because $e(\xi) = 0$, the unit tangent bundle of $\Sigma_1$ is trivial and admits a nowhere-vanishing section. For a 2D incompressible fluid directly on the surface $\Sigma_1 = \mathbb{T}^2$, global regularity for all smooth initial data is a classical PDE theorem (Ladyzhenskaya), owing to 2D vorticity conservation rather than to a vanishing cohomology class or to a Levi-eigenvalue core-flattening mechanism ([core Levi form](#prop:core-levi-form)). By contrast, the categorical label $\mathrm{NS}(A) = 0$ does not establish global regularity for classical unforced 3D Navier--Stokes (such as Fefferman's Alternative B on $\mathbb{T}^3$): by Tao's averaged Navier--Stokes barrier (*J. Amer. Math. Soc.* **29** (2016), 601--674), no argument that depends only on topology and ignores the structure of the 3D advection nonlinearity $B(u, u) = P[(u \cdot \nabla)u]$ can prove 3D global regularity, and the $q \to 1$ limit at $\nu_q = (q - 1)/(2q)$ is the inviscid Euler limit unless taken along the fixed-$\hbar_q$ scaling branch.

**Failure of the torus to support the observed physics.**
Because the torus anchors at $g = 1$, it physically embeds exactly one torus knot: $T_{2,3}$ (the generic trefoil spanning Seifert genus 1). The generated knot spectrum isolates a single physical generator — effectively abandoning the muon, the tau, and any quarks outside the first generation. The explicit representation theory governing $\pi_1(\Sigma_1) = \mathbb{Z}^2$ behaves completely abelian: every valid $\mathrm{SU}(2)$ representation must mechanically factor down through $\mathrm{U}(1)$. The base gauge group completely collapses. The expected full particle spectrum simply cannot emerge.

**The torus also fails observability.**
Evaluated over $\Sigma_1$, explicitly flat $\mathrm{SU}(2)$ connections reliably exist bearing holonomy restricted to $\mathrm{U}(1) \subset \mathrm{SU}(2)$. These remaining connections act entirely **reducible**: $H^0(\Sigma_1, \mathrm{Ad}(P)) \neq 0$ (the isolated Cartan subalgebra $\mathfrak{u}(1) \subset \mathfrak{su}(2)$ automatically supplies a persistent nonzero equivariant section). Consequently, $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$. The core observability axiom explicitly fails.

The resulting torus structure forms a quantum pre-universe (QPU), definitively rejecting QOU status.

**Contrast with the Descartes universe.**

See [Table](#tbl:torus-ns-regular-table-data).

The mathematical torus provides the simplest mechanical example where $\chi(\mathcal{S}) = 0$ yields categorical NS-regularity ($\mathrm{NS}(A) = e(\xi) = 0$). Predictably, it is also physically trivial: the vanishing Euler characteristic prevents the torus from supporting an irreducible QOU.

**Other $\chi = 0$ examples (2D spectral surfaces vs 3-manifolds).**
Any genus-1 spectral surface $\mathcal{S}$ has $\chi(\mathcal{S}) = 0$ (such as the flat 2-torus $\mathbb{R}^2/\mathbb{Z}^2$ or a complex elliptic curve) and is categorically NS-regular in the same sense. *Scope note on 3-manifolds:* closed orientable 3-manifolds $M^3$ — such as the Heisenberg nilmanifold $\mathrm{Heis}(\mathbb{Z}) \backslash \mathrm{Heis}(\mathbb{R})$, Seifert 3-manifolds, $\mathbb{T}^3$, or the unit tangent bundle $\mathrm{UT}(\Sigma_4)$ of Bring's surface — all satisfy $\chi(M^3) = 0$ automatically by Poincaré duality, whereas $\mathrm{NS}(A) = e(\xi) \in H^2(\mathcal{S}, \mathbb{Z})$ is defined on the 2D spectral surface $\mathcal{S}$ and does not settle 3D Navier--Stokes regularity on $M^3$.
