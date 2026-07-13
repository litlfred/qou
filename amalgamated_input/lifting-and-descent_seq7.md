<!-- FILE_START: betti-harmonic-intro.md -->
The Euler characteristic stabilizes along the tower, aggregating Hodge-theoretic data. We now refine this aggregate into Betti numbers, fix a $q$-harmonic basis, and filter the basis into fermionic and bosonic sectors via the curvature commutator.

The Betti numbers of the brane tower track the dimensions $b_k(A_n)$ packaged by the Euler characteristic. The $q$-harmonic basis chooses representatives compatible with the substrate parameter, splitting by $\mathrm{SU}(2)$ weight. The algebraic filter $[\text{--}, F]$ then classifies this basis into commuting (bosonic) and anti-commuting (fermionic) sectors. The distributional connection at the limit prepares the geometry for descent.

The next section projects the brane tower onto its physically realised stratum using this fermion--boson filter and eigenspace data.
<!-- FILE_END: betti-harmonic-intro.md -->

<!-- FILE_START: betti-numbers-brane.md -->
Let $b_k(\mathcal{S}_n) = \dim H^k(\mathcal{S}_n, \mathbb{R})$ denote the $k$-th Betti number of $\mathcal{S}_n$. Since $\mathcal{S}_{n+1}$ is the bundle of orthonormal frames of $J^1 \mathcal{S}_n$, the Leray--Serre spectral sequence of the fibration $\mathcal{S}_{n+1} \to \mathcal{S}_n$ determines the Betti numbers of $\mathcal{S}_{n+1}$. The [quantum characteristic classes](#def:quantum-characteristic-classes) obstruct the collapse of this spectral sequence, controlling the growth of $b_k(\mathcal{S}_{n+1})$ relative to $b_k(\mathcal{S}_n)$.
<!-- FILE_END: betti-numbers-brane.md -->

<!-- FILE_START: q-harmonic-basis-brane.md -->
For each level $n$, the $q$-harmonic $1$-forms $\alpha_{n,i}$ belong to the space $\mathcal{H}^1(\mathcal{S}_n, \mathrm{ad} \mathcal{S}_n)$ of harmonic $1$-forms on $\mathcal{S}_n$ with values in the adjoint bundle $\mathrm{ad} \mathcal{S}_n$. They are characterised by the self-duality condition relative to the instanton connection $A_n$ ([recursive brane tower](#def:recursive-brane-tower)):

$$
  \alpha_{n,i} \in \mathcal{H}^1
  \iff
  d_{A_n}\alpha = 0
  \quad\text{and}\quad
  d_{A_n}^*\alpha = 0.
$$

The Hodge-star operator is induced by the Hermitian metric that the Levi form $L$ ([substrate parameter](#def:substrate-parameter)) defines on the horizontal distribution. The index $i$ runs over $1 \leq i \leq b_1(\mathcal{S}_n)$ ([Betti numbers on branes](#rem:betti-numbers-brane)).

At the base level $n = 0$, with Euler characteristic $\chi(M) = 3$, there are three primary basis vectors $\{\phi_1, \phi_2, \phi_3\}$. At level $n = 1$ the basis lifts: it includes the original modes together with their $J^1$ prolongations ([jet prolongation](#prop:jet-prolongation)), which act as the first-order resolutions of the base flows.
<!-- FILE_END: q-harmonic-basis-brane.md -->

<!-- FILE_START: weight-space-decomposition-brane.md -->
The adjoint bundle $\mathrm{ad} \mathcal{S}_n$ has fibre $\mathfrak{su}(2)$. Via the weight-space decomposition of $\mathrm{SU}(2)$, the harmonic basis of $\mathcal{H}^1(\mathcal{S}_n, \mathrm{ad} \mathcal{S}_n)$ splits into two families.

**Longitudinal modes.** These forms constitute the $\mathrm{U}(1)$ backbone. They take values in the Cartan subalgebra of $\mathfrak{su}(2)$ and have the geometric form $\vartheta^0 \otimes H$, where $H$ is the diagonal generator. They represent steady-state laminar flows aligned with the $\mathrm{U}(1)$ subgroup. If the bundle splits at a monodromy fixed point, these are the only modes that survive; they correspond to the magnetic flux of the stable vortices.

**Ladder modes.** These are the raising and lowering vortices. They take values in the off-diagonal generators $E_\pm$ of $\mathfrak{su}(2)$ and have the geometric form $\vartheta^\pm \otimes E_\pm$. They describe entangling flows that twist the $\mathbb{P}^1(\mathbb{C})$ fibre along the brane. These modes generate the non-commutativity in the $\mathrm{SU}_q(2)$ algebra ([direct limit algebra](#def:direct-limit-algebra)).

In the $1$-jet bundle $J^1 \mathcal{S}_n$ ([$J^1\mathcal{S}$ local states](#rem:j1e-local-states)), each basis element $\alpha$ is a pair consisting of a value (the direction of the $\mathrm{SU}(2)$ flow in the fibre) and a momentum (the gradient of that flow relative to the complex structure of the brane).
<!-- FILE_END: weight-space-decomposition-brane.md -->

<!-- FILE_START: algebraic-filter-classification.md -->
Let $F_A$ be the curvature of the substrate parameter ([substrate parameter](#def:substrate-parameter)) and let $\alpha$ be a harmonic $1$-form in the $q$-harmonic basis on branes ([q-harmonic basis](#rem:q-harmonic-basis-brane)).

The commutator $[F_A, \alpha]$ classifies $\alpha$ into exactly one of two types:

1. **Fermionic (matter).** $[F_A, \alpha] \neq 0$.
2. **Bosonic (radiation).** $[F_A, \alpha] = 0$.
<!-- FILE_END: algebraic-filter-classification.md -->

<!-- FILE_START: algebraic-filter-physical.md -->
The two commutator classes of the [fermion--boson filter](#prop:algebraic-filter-classification) carry a geometric reading in the gauge-fluid flow.

1. **Fermionic (matter).** When $[F_A, \alpha] \neq 0$, the form $\alpha$ is entangled with the curvature. It sees the $\mathrm{SO}(3)$ holonomy and the index $-6$ fixed points, yielding geodesics that are trapped or spiralling around the fundamental vortex filaments.
2. **Bosonic (radiation).** When $[F_A, \alpha] = 0$, the form $\alpha$ commutes with the curvature. It corresponds to longitudinal modes that propagate through the bulk without deflection by the monodromy fixed points, yielding straight geodesics relative to the gauge-fluid flow.
<!-- FILE_END: algebraic-filter-physical.md -->

<!-- FILE_START: algebraic-filter.md -->
Let $\alpha$ be a harmonic $1$-form in the basis of [$q$-harmonic basis on branes](#rem:q-harmonic-basis-brane). Its signature is determined by its commutator with the curvature $F_A$ ([substrate parameter](#def:substrate-parameter)).

1. **Fermionic type (matter).** $[F_A, \alpha] \neq 0$. These forms are entangled with the curvature. They see the $\mathrm{SO}(3)$ holonomy and the index $-6$ fixed points, yielding geodesics trapped or spiralling around the three fundamental vortex filaments.
2. **Bosonic type (radiation).** $[F_A, \alpha] = 0$. These forms commute with the curvature. As longitudinal modes ([weight space decomposition](#rem:weight-space-decomposition)), they flow through the bulk undeflected by monodromy fixed points, yielding straight geodesics relative to the gauge-fluid flow.
<!-- FILE_END: algebraic-filter.md -->

<!-- FILE_START: distributional-connection.md -->
At the limit $n \to \infty$, we replace a single connection $A$ with a distributional connection represented by the series:

$$
  A_\infty
  = 
  \sum_{n=0}^{\infty}\sum_{i=1}^{b_1(\mathcal{S}_n)}
  c_{n,i}\alpha_{n,i},
$$

where $c_{n,i} \in \mathbb{C}$ and $\{\alpha_{n,i}\}$ is the $q$-harmonic basis ([$q$-harmonic basis on branes](#rem:q-harmonic-basis-brane)). This transforms the gauge field into a harmonic expansion across the infinite jet space $J^\infty \mathcal{S}$ ([jet shell](#rem:jet-shell)).
<!-- FILE_END: distributional-connection.md -->

