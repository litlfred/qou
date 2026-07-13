<!-- FILE_START: q-deformed-operators-intro.md -->
The categorical $q$-deformed operators specialise to a concrete CR manifold $M$. We record the formulas in classical differential-geometric language. Each operator inherits the uniform interpolation pattern $q^{-1}(\text{classical}) + (1 - q^{-1})(\text{Reeb correction})$.
<!-- FILE_END: q-deformed-operators-intro.md -->

<!-- FILE_START: q-ext-deriv.md -->
In the archimedean realisation, the categorical $d_q$ specialises to $d_q \colon \Omega^k(M) \to \Omega^{k+1}(M)$:

$$
  d_q\alpha = q^{-1}d\alpha + (1 - q^{-1})\varTheta \wedge \mathcal{L}_\xi\alpha.
$$

The vertical projection $\pi_V \circ d$ becomes $\varTheta \wedge \mathcal{L}_\xi$, and $d_q^2 = q^{-1}(1-q^{-1})d\varTheta \wedge \mathcal{L}_\xi$.
<!-- FILE_END: q-ext-deriv.md -->

<!-- FILE_START: q-lie-bracket.md -->
In the archimedean realisation, the categorical Reeb derivation induces the $q$-deformed Lie bracket on vector fields $V, W \in \mathfrak{X}(M)$:

$$
  [V, W]_q = q^{-1}[V, W] + (1 - q^{-1})\bigl(\varTheta(V)\mathcal{L}_\xi W - \varTheta(W)\mathcal{L}_\xi V\bigr).
$$
<!-- FILE_END: q-lie-bracket.md -->

<!-- FILE_START: q-connection.md -->
In the archimedean realisation, the categorical $q$-connection specialises to $A_q = q^{-1}A + (1 - q^{-1})\iota_\xi A\varTheta$. At $q = 1$, it recovers the full instanton connection $A$. As $q \to \infty$, it reduces to the Reeb component $\iota_\xi A\varTheta$.
<!-- FILE_END: q-connection.md -->

<!-- FILE_START: q-reeb-vector-field.md -->
The categorical Reeb derivation $\xi$ deforms in the archimedean setting to $\xi_q$, acting on smooth functions $f \in C^\infty(M)$ by

$$
  \xi_q(f) =  q^{-1}\xi(f) + (1 - q^{-1})[\xi, X_f]_q,
$$

where $X_f$ is the horizontal lift of $\mathrm{grad}_{g_\varTheta}f$ to $\ker\varTheta$.
<!-- FILE_END: q-reeb-vector-field.md -->

<!-- FILE_START: q-reeb-flow.md -->
In the archimedean realisation, the $q$-deformed Reeb vector field $\xi_q$ generates a one-parameter family of diffeomorphisms $\phi_t^q \colon M \to M$:

$$
  \frac{d}{dt}\phi_t^q =  \xi_q \circ \phi_t^q, \qquad \phi_0^q = \mathrm{id}_M.
$$
<!-- FILE_END: q-reeb-flow.md -->

<!-- FILE_START: q-torsion-leaf.md -->
Let $H = \ker\varTheta \subset TM$ be the horizontal distribution on the CR manifold $M$. A $q$-torsion leaf is a maximal integral submanifold $L \hookrightarrow M$ of $H$ invariant under the $q$-deformed Reeb flow:

$$
  T_p L \subset H_p \quad\text{and}\quad \phi_t^q(L) = L.
$$
<!-- FILE_END: q-torsion-leaf.md -->

<!-- FILE_START: q-torsion-existence.md -->
Maximal integral submanifolds of $H$ are Legendrian submanifolds. A $q$-torsion leaf is a Legendrian submanifold invariant under the $q$-deformed Reeb flow. For $q > 1$, the deformation generically breaks periodicity, demanding KAM-type persistence results. The failure of the Frobenius structure on $H$ forces the dimension bound and provides $q$-torsion leaves their rigidity.
<!-- FILE_END: q-torsion-existence.md -->

<!-- FILE_START: quantum-torsion-motivation.md -->
Classical torsion measures the failure of infinitesimal parallelograms to close. Quantum torsion identifies the failure of the algebra of states to commute. The $\mathrm{SU}(2)$ action on the Frobenius–Hopf object $A$ dictates this twist.

The substrate parameter $q$ acts as a torsion index. At $q = 1$, quantum torsion vanishes, the $\mathrm{SU}(2)$ action operates smoothly, and the algebra commutes. For $q \neq 1$, non-commutativity tightens the structure, forcing the $q$-deformed Reeb flow and its invariant leaves into rigid configurations.

The spinor sign rule follows. The first $360^\circ$ rotation addresses the physical state in space; the second $360^\circ$ completes the quantum torsion reset, unwinding the twist imposed by the $\mathrm{SU}(2)$ action on the vortex-tube fibre of the state bundle.
<!-- FILE_END: quantum-torsion-motivation.md -->

