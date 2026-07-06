The [time reversal barrier](#rem:time-reversal-energy-barrier) shows that chirality reversal requires infinite energy **in the observable sector**. Here, the Frobenius form is non-degenerate and $q$ must be real. The [cosmological limits](#ex:cosmological-limits) identify two regimes where this topological protection fails.

**Formalization status.** The claims below are conjectural. The cosmological limits block provides an example with a conjectural interpretation. The Frobenius degeneration at $q \to \infty$ is not formalized in Lean. The only proven limits are the trivial evaluations $\hbar_q(1) = 0$ and $|\hbar_q(q) - 1| < \epsilon$ for large $q$. The categorical description of initial and terminal objects in a category of degenerations remains a research direction.

**At the Big Bang ($q \to \infty$).**

The Frobenius form degenerates: $\int_A(f^\dagger f) \sim q^{-1} \to 0$. The [Heisenberg commutator](#rem:heisenberg-commutator) $[\hat{X}, \hat{P}]_q \to J$ reaches its maximum, rendering all observables maximally non-commutative. The positive-definiteness axiom that forces $q$ to be real no longer constrains the system. With a degenerate Frobenius pairing, the dagger structure has no norm to be positive-definite against.

In this regime, $q$ can acquire an imaginary part $\theta \neq 0$. The [complex substrate interpretation](#rem:complex-substrate-interpretation) permits continuous chirality rotation in the fibers. At each blow-up point, the [exceptional divisor](#def:exceptional-divisor) $\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$ acts as the space where trefoils and their mirrors interconvert via the phase rotation $\mathcal{X}_\varphi$. The chirality flip occurs **in the fibers**, not at the base level.

Sakharov's conditions are met here:
1. Frobenius form degeneration permits baryon number violation (topological protection weakens when the pairing degenerates).
2. The complex phase $\theta$ provides CP violation.
3. The Big Bang itself supplies the departure from equilibrium.

**At heat death ($q \to 1$).**

The Hopf algebra becomes cocommutative ($\sigma \circ \Delta = \Delta$), [$\hbar_q \to 0$](#def:substrate-parameter), and by [prop:u1-equivariant-reduction](#prop:u1-equivariant-reduction) the three Descartes color tubes collapse to a single $\mathrm{U}(1)$ phase tube on $\mathcal{X}_5$. The crossing-energy asymmetry $q - q^{-1} = 2\sinh(\ln q) \to 0$ vanishes. Chirality becomes undetectable: $T_{2,3}$ and $T_{2,3}^{\sigma}$ merge, and the strong and Coulomb channels unify. Only the two $S_5$-equivariant generators ([rem:symmetry-preserving-leptons](#rem:symmetry-preserving-leptons)) — the electron and muon — survive as distinguishable topological excitations. Their masses vanish alongside $q - q^{-1}$.

**Categorical picture (conjectural).**

The correct categorical framework for these limits requires a **category of QOU degenerations** $\mathbf{QOU}_{\mathrm{deg}}$. Its objects are triples $(\mathbf{C}, A, \tau)$ equipped with a substrate parameter $q$. Its morphisms are structure-preserving maps that may selectively degrade axioms:

- The **initial object** represents the Big Bang state. This is the maximally degenerate state where $q = \infty$, the Frobenius form vanishes, and the only data is the [bundle initial condition](#def:bundle-initial-conditions) $E_0 = \sum_i (p_i, H_i)$ (positions without momenta). Every state with finite $q$ receives a unique morphism from this initial object (time evolution from the singularity).
- The **terminal object** is [Bring's surface](#thm:descartes) $\Sigma_4$, which is terminal in $\mathbf{C}_{-6}$. In the degeneration category, the $q = 1$ classical limit acts as the terminal object. Every state admits a unique morphism to the fully cocommutative structure by sending $q \mapsto 1$.
- The **observable era** forms the full subcategory on objects with $1 < q < \infty$, where all axioms hold non-degenerately.

This picture lacks formalization. The necessary steps are:
1. Defining "degenerate QOU" precisely by weakening the Frobenius non-degeneracy axiom.
2. Proving the $q \to \infty$ limit is initial (showing the bundle initial condition determines all subsequent time evolution).
3. Proving $q \to 1$ is terminal (showing the classical projection is unique and structure-preserving).
4. Formalizing these definitions and proofs in Lean.

**The aeon boundary.**

At both cosmological extremes, the fiber geometry permits actions forbidden in the observable interior. Between these endpoints, the physically meaningful regime $1 < q < \infty$ enforces strict chirality conservation:

1. **Big Bang** (initial object): Frobenius degeneration removes the observability constraint. Chirality flips occur freely in the fibers at the exceptional divisors. The residual complex phase $\theta$ generates matter-antimatter asymmetry via CP violation before the Frobenius form stabilizes.
2. **Observable era** (full subcategory, $1 < q < \infty$): Chirality is frozen. Electrons, protons, and neutrons maintain their handedness. The topological barrier remains infinite.
3. **Heat death** (terminal object): The $q \to 1$ limit erases the chirality distinction. Particles and antiparticles become indistinguishable. Crossing energy vanishes. Matter and radiation merge in the frozen geometry.

If the universe is cyclic — where heat death transitions into the next Big Bang — the chirality flip occurs at the **aeon boundary**. Here the Frobenius form either degenerates ($q \to \infty$) or trivializes ($q \to 1$). The exceptional divisors are the geometric locus of this transition. They provide the space where fibers reset, assigning fresh chirality for the next aeon.

The categorical conjecture frames the aeon transition as a morphism from the terminal object of one copy of $\mathbf{QOU}_{\mathrm{deg}}$ to the initial object of the next. This categorical recycling map preserves topological data (knot types) while resetting metric data (masses, charges).
