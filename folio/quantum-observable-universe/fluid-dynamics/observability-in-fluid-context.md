Before formalising [NS regularity](#def:ns-regular-qou), this remark clarifies the QOU observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ structurally within the fluid-dynamical setting.

**Categorical statement.**
No morphism $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$ exists within $\mathbf{C}$. The adjoint representation of the Frobenius--Hopf object $A$ admits no trivial sub-object.

**Gauge-theoretic translation.**
$H^0(M, \mathrm{Ad}(P)) = 0$: no nonzero section of the adjoint bundle $\mathrm{Ad}(P) = P \times_G \mathfrak{g}$ remains gauge-equivariant. Every infinitesimal gauge transformation operates nontrivially against some observable.

**No contact-geometric translation.**
Observability cannot be translated as universal non-degeneracy of a Levi form $\mathcal{L}_\varTheta$: on the three-dimensional flow domain the plane field is $\ker\varTheta = \xi^\perp$, with $\xi$ the vorticity direction, and its Levi datum is the single scalar $\xi\cdot\mathrm{curl}\,\xi$ ([core Levi form](#prop:core-levi-form)). No result in this chapter links the non-vanishing of that scalar to $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.

**Fluid-dynamical translation.**
Evaluated on the [brane fluid](#sec:brane-fluid):

1. **No stagnant directions.** Every spatial direction in the brane actively drives fluid dynamics. The gauge structure strictly forbids directions supporting an identically zero velocity field.
2. **No hidden laminar sectors.** If $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$, a gauge symmetry would render a designated direction dynamically trivial, yielding a guaranteed laminar sector. Observability precludes this: every direction forces dynamic engagement.
3. **Vortex stretching is isotropic.** The [weight-space decomposition](#def:weight-decomposition) of the adjoint bundle lacks a trivial component. Consequently, the stretching term $(\omega \cdot \nabla)v$ applies pressure in all directions. Vorticity cannot vent into a "neutral" axis.

**The alternative: what $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$ implies.**

A surviving morphism $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$ would establish a **preferred direction** operating in the brane:

- A designated axis where vortex stretching zeroes out.
- A physical channel permitting vorticity to drain without local concentration.

This structural leak would provide a persistent **regularity mechanism**: vorticity would dissipate cleanly along the preferred direction rather than concentrating into a blowup.

**Observability asserts that no such escape route exists.** The brane fluid remains dynamically active; colliding vortices lack any structural geometry to dissipate through.
