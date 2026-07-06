The [core-Levi equivalence](#prop:core-levi-form) reformulates the Navier--Stokes millennium problem as a question about the contact geometry of the brane:

$$
  \text{NS blows up}
  \Longleftrightarrow
  \text{Levi form non-degenerate at collision}
  \Longleftrightarrow
  \kappa(t) = O(1).
$$

**Interpretation of each outcome.**

If the Levi form **stays non-degenerate** ($\kappa = O(1)$): vorticity concentrates in tubular cores. The lower bound $\|\omega\|_\infty \geq c/(T^*-t)$ holds. BKM diverges, and NS loses regularity. This establishes the [counter-example](#conj:ns-counterexample). Physically, the contact structure resists integrability, the vortex remains a topological defect, and the collision produces a genuine singularity.

If the Levi form **degenerates** ($\kappa \to 0$ or $\infty$): vorticity spreads into a sheet. The lower bound fails, and NS might remain regular. Physically, the contact structure becomes partially integrable at the collision locus. A 2-dimensional integral submanifold forms, the observability axiom fails locally, and the vortex dissolves into a diffuse structure that classical viscosity can regularise.

**The root-of-unity constraint.**
At $q = e^{i\pi/\kappa}$, the [truncation](#prop:root-of-unity-truncation) to $(\kappa-1)/2$ modes bounds the core aspect ratio by $1 + C(\kappa-1)$. As $\kappa \to \infty$ ($q \to 1$), this bound diverges, but only linearly. The collision dynamics drives $\kappa(t)$ at a rate set by the Biot--Savart stretching $\sim 1/(T^*-t)$. Whether the representation-theoretic bound $O(\kappa)$ or the dynamical rate $O(1/(T^*-t))$ wins determines the outcome.

The contact-geometric reformulation asks: **does the finite-dimensional approximation of $\mathrm{SU}_q(2)$ preserve the non-degeneracy of the Levi form in the infinite-dimensional limit?**
