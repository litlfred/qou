**Time relative to the observer.**
In the QOU formalism, time is relative to the observer rather than an absolute background parameter. The "time" experienced by an observer is the **computational time** required to evaluate the state space leading to or following from that point. This discrete sequence of Planck operations acts as the metric of temporal distance; the underlying definition is [information-theoretic time](#def:information-theoretic-time).

## Categorical dynamics

At the Planck length, geometric coordinates give way to a purely categorical framing of the observer and the time step. Let the observable universe $M$ be an object in a category $\mathbf{C}$ with a terminal object $\mathrm{pt}$.

**Point morphisms and particles.** A geometric "point" is a morphism $p : \mathrm{pt} \to M$. A particle is a section over points rather than a point: a morphism $s : M \to E$ into a bundle $E \to M$ whose composition with the projection is the identity. The state of the particle at a point is the composition of $p$ with $s$.

**Functorial evolution.** Dynamical evolution is modeled as an endofunctor on the category, or equivalently as an endomorphism $\mathrm{TimeStep} : M \to M$. The "flowed" state of a point under one Planck time step is the composition

$$
  p \;\mapsto\; p \circ \mathrm{TimeStep} .
$$

## The unification dictionary

The framework treats time-step evolution as a generic endofunctor. One expects — by analogy with the coherence theorems for braided monoidal categories — that a functorial time step preserving the QOU invariants is naturally isomorphic to the fundamental braiding action; this uniqueness is a heuristic identification here rather than a proved statement. Under that identification, four conceptual domains would describe the same underlying mechanism of the discrete computational Planck step:

| Conceptual domain | Mechanism / object | Evolution action |
| --- | --- | --- |
| **Category theory** | Point morphism $p : \mathrm{pt} \to M$ | Endofunctor $F$, flow $p \circ F$ |
| **Algebraic / knot theory** | State-space braiding | $R$-matrix operator $\check{R}$, Markov trace |
| **Conformal field theory** | Exceptional divisor $\mathcal{S}_p$ | Vertex operator $Y(a, z)$, OPE singularity |
| **Information theory** | Computational spacetime | Discrete Planck operation, evaluation step |

Read this dictionary as a proposed correspondence: the computational time-step functor acting on point morphisms would be instantiated by the $R$-matrix operator on the state space, which in turn evaluates as a vertex-operator insertion on Bring's surface.

## Bring's surface and the emergence of spacetime

The relationship between time, algebraic distance, and computational cost is carried by the first two coordinates of [Bring's surface](#def:brings-surface). Bring's surface has $2$ complex dimensions; under the action of the natural involution these supply the $4$ real dimensions interpreted as physical spacetime. The first two coordinates of Bring's surface map into the computational spacetime metric.

**Relative distance as computational cost.**
On this reading, physical distance is relative computational time: the separation between two events is the number of discrete lattice applications of the $R$-matrix (dependent on the local aether parameter $q$) required to connect their state spaces. While this computational distance is relative to the observer, it remains consistent across observers: the algebraic consistency of the state space (the Yang--Baxter equations on the $R$-matrix) makes the computational distance agree across observers, so macroscopic symmetries such as Lorentz covariance would emerge as information-theoretic agreement. This recovery of Lorentz covariance is an interpretive expectation rather than a derivation.

## The aether parameter and the mass ratio

In the trace-based mass channel, particle masses are computed from the Markov trace of their respective topological knots,

$$
  \mathfrak{m}(K) \;\approx\; \mathrm{tr}_M(K, q) \cdot \mathfrak{E}_0 ,
$$

with $\mathfrak{E}_0$ the scaling energy. For the ratio between two flavor generations (the muon and the electron), the scaling energy cancels, leaving an algebraic relation

$$
  \frac{\mathfrak{m}_\mu}{\mathfrak{m}_e} \;=\; \frac{\mathrm{tr}_M(K_\mu, q)}{\mathrm{tr}_M(K_e, q)} .
$$

This identity suggests a physical reading of the aether parameter $q$: rather than a hidden background parameter, $q$ is tied directly to the mass ratio itself. If $q$ is a local field $q(p)$ that evolves in response to local interactions (for example in regions of extreme electromagnetic field or gravity), then a topological deformation of the local geometry would manifest as a shift in the local mass ratio $\mathfrak{m}_\mu(p)/\mathfrak{m}_e(p)$, and tracking the evolution of $q(p)$ over the spacetime lattice would be observationally equivalent to tracking a drift of the flavor mass hierarchy. Both the local-field promotion of $q$ and the resulting drift are speculative interpretations of the trace identity.
