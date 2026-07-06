Before defining [NS regularity](#def:ns-regular-qou), we clarify the fluid-dynamical meaning of the QOU observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.

**Categorical statement.**
No morphism $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$ exists in $\mathbf{C}$. The adjoint representation of the Frobenius--Hopf object $A$ has no trivial sub-object.

**Gauge-theoretic translation.**
We have $H^0(M, \mathrm{Ad}(P)) = 0$. No nonzero section of the adjoint bundle $\mathrm{Ad}(P) = P \times_G \mathfrak{g}$ is gauge-equivariant. Every infinitesimal gauge transformation acts nontrivially on some observable.

**Contact-geometric translation.**
The Levi form $\mathcal{L}_\varTheta$ is everywhere non-degenerate. The horizontal distribution $\ker(\varTheta)$ is maximally non-integrable; it contains no integral submanifolds of dimension $> \frac{1}{2}\dim\ker\varTheta$.

**Fluid-dynamical translation.**
In the [brane fluid](#sec:brane-fluid):

1. **No stagnant directions.** Every direction in the brane carries nontrivial fluid dynamics. The velocity field cannot vanish identically along any direction without violating the gauge structure.
2. **Vortex cores are tubular.** The [core-Levi equivalence](#prop:core-levi-form) implies that a non-degenerate Levi form forces the vortex core cross-section to have bounded aspect ratio. The core cannot flatten into a sheet or collapse into a needle.
3. **No hidden laminar sectors.** If $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$, a gauge symmetry would render some direction dynamically trivial, forcing the fluid to be automatically laminar there. Observability forbids this: every direction remains dynamically active.
4. **Vortex stretching is isotropic.** The [weight-space decomposition](#def:weight-decomposition) of the adjoint bundle has no trivial component. The stretching term $(\omega \cdot \nabla)v$ in the vorticity equation acts nontrivially in every direction. Vorticity cannot leak into a "neutral" direction.

**The alternative: what $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$ would mean.**

A nonzero $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$ would define a preferred direction in the brane. This direction would provide:
- A 1-dimensional (partially integrable) foliation of the contact distribution.
- A direction where vortex stretching vanishes.
- A channel through which vorticity drains without concentrating.
- A mechanism for vortex cores to flatten into sheets (elongating along the foliation leaf).

This would yield a regularity mechanism: vorticity spreads into the integrable direction rather than concentrating, which prevents blowup.

Observability dictates that no such escape route exists. The brane fluid remains dynamically active in every direction, and colliding vortices have nowhere to spread.
