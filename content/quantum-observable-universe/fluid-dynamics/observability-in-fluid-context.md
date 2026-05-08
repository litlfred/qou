Before defining [NS regularity](#def:ns-regular-qou), we
clarify what the QOU observability axiom
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ means in the
fluid-dynamical setting.

**Categorical statement.**
No morphism $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$ exists
in $\mathbf{C}$.  That is: the adjoint representation of the
Frobenius--Hopf object $A$ has no trivial sub-object.

**Gauge-theoretic translation.**
$H^0(M, \mathrm{Ad}(P)) = 0$: no nonzero section of the adjoint
bundle $\mathrm{Ad}(P) = P \times_G \mathfrak{g}$ is
gauge-equivariant.  Every infinitesimal gauge transformation
acts nontrivially on some observable.

**Contact-geometric translation.**
The Levi form $\mathcal{L}_\varTheta$ is non-degenerate everywhere.
The horizontal distribution $\ker(\varTheta)$ is maximally
non-integrable (no integral submanifolds of dimension
$> \frac{1}{2}\dim\ker\varTheta$).

**Fluid-dynamical translation.**
In the [brane fluid](#sec:brane-fluid):

1. **No stagnant directions.**  Every direction in the brane
   carries nontrivial fluid dynamics.  There is no direction
   along which the velocity field can be identically zero
   without violating the gauge structure.

2. **Vortex cores are tubular.**  The
   [core-Levi equivalence](#prop:core-levi-form) shows that
   non-degenerate Levi form implies the vortex core
   cross-section has bounded aspect ratio.  The core cannot
   flatten into a sheet or collapse into a needle.

3. **No hidden laminar sectors.**  If
   $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$, there
   would exist a direction in which the fluid is automatically
   laminar (a gauge symmetry renders that direction dynamically
   trivial).  Observability forbids this: every direction is
   dynamically active.

4. **Vortex stretching is isotropic.**  The
   [weight-space decomposition](#def:weight-decomposition)
   of the adjoint bundle has no trivial component.  The
   stretching term $(\omega \cdot \nabla)v$ in the vorticity
   equation acts nontrivially in every direction — vorticity
   cannot leak into a "neutral" direction.

**The alternative: what $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$ would mean.**

If a nonzero $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$
existed, it would define a **preferred direction** in the brane:

- A 1-dimensional foliation of the contact distribution
  (partially integrable)
- A direction in which vortex stretching vanishes
- A channel through which vorticity can drain without
  concentrating
- A mechanism for vortex cores to flatten into sheets
  (the core elongates along the foliation leaf)

This would provide a **regularity mechanism**: vorticity
spreads into the integrable direction instead of concentrating,
preventing blowup.

**Observability is therefore the statement that no such
escape route exists.** The brane fluid is dynamically active in
every direction, and colliding vortices have nowhere to spread.
