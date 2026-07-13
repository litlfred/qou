<!-- FILE_START: quantum-observable-universes-intro.md -->
The remaining sections elaborate the categorical, algebraic, and analytic context of the QOU axioms. They establish the TQFT setting, record the $q$-jacobiator identity, give the physical reading of the categorical action, and assemble the categorical lifting for the Yekutieli brane tower.
<!-- FILE_END: quantum-observable-universes-intro.md -->

<!-- FILE_START: tqft-context.md -->
The axioms of the quantum universe and quantum observable universe are grounded in topological quantum field theory. The Frobenius--Hopf object $A$ carries the $2$d cobordism data and the Hopf structure for quantum-group symmetry.

The condition $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ acts as the categorical contact condition. It ensures irreducibility of the associated $3$d TQFT, non-degeneracy of the pairing across cobordisms, and full dualisability. In the archimedean realisation, this enforces $H^0(M, \mathrm{Ad}(P)) = 0$, eliminating infinitesimal automorphisms on the instanton connection.
<!-- FILE_END: tqft-context.md -->

<!-- FILE_START: vanishing-explication.md -->
In the archimedean $\mathbb{C}$-QOU, $H^0(M, \mathrm{Ad}(P)) = 0$ eliminates infinitesimal gauge symmetries, and $\Gamma_c(M,\mathcal{S}) = 0$ secures the injectivity of the jet-bundle map $\Gamma(J^1 \mathcal{S}) \hookrightarrow \mathcal{A}(P)$.
<!-- FILE_END: vanishing-explication.md -->

<!-- FILE_START: levi-generalisation.md -->
The QOU framework relies on Levi non-degeneracy over strict pseudoconvexity, requiring three conditions:
1. **Kohn--Rossi finite-dimensionality:** The tangential CR complex has finite-dimensional cohomology, securing analytic control over $q$-harmonic forms.
2. **Non-degeneracy of the substrate:** The Levi form $L_\varTheta$ is non-degenerate, fixing the substrate parameter $q(p) = 1 + \lvert\langle L_\varTheta, F_A^+\rangle\rvert \geq 1$.
3. **QOU vanishing:** $H^0(M, \mathrm{Ad}(P)) = 0$ and $\Gamma_c(M,\mathcal{S}) = 0$ provide the topological gauge obstructions.
<!-- FILE_END: levi-generalisation.md -->

<!-- FILE_START: quantum-gauge-group-category.md -->
The quantum gauge group operates fibrewise via the representation category $\mathrm{Rep}(\mathrm{SU}_{q(p)}(2))$. Tannaka--Krein duality reconstructs the Hopf algebra $\mathcal{O}_{q(p)}(\mathrm{SU}(2))$ through the forgetful fibre functor. The Hopf-algebra and representation-category viewpoints act equivalently across fibres.
<!-- FILE_END: quantum-gauge-group-category.md -->

<!-- FILE_START: hopf-structure-diagrams.md -->
The Hopf comultiplication $\Delta_q$ on $\mathcal{O}_q(\mathrm{SU}(2))$ obeys coassociativity.
<!-- FILE_END: hopf-structure-diagrams.md -->

<!-- FILE_START: quantum-flatness.md -->
Let $B \in \Omega^2(A) \otimes \mathrm{Ad}(A)$ be the $2$-form datum of the inner-automorphism $2$-group $\mathrm{INN}(G_q)$. The connection $\nabla$ is **quantum flat** when its curvature equates to the $2$-form datum: $F_\nabla = B$.
<!-- FILE_END: quantum-flatness.md -->

<!-- FILE_START: self-dual-2group.md -->
A $2$-connection for $\mathrm{INN}(G)$ dictates $F_A = B$. Under the simplicity constraint $B \in \Gamma(\Lambda^+\!H^* \otimes \mathrm{Ad}(P))$, the $2$-form datum evaluates as self-dual. The conjunction of quantum flatness $F_A = B$ and simplicity forces $F_A = F_A^+$, securing the instanton equation $F_A^- = 0$.
<!-- FILE_END: self-dual-2group.md -->

<!-- FILE_START: emergence-to-quantum-flat.md -->
For a QOU meeting the categorical volume constraint, $G_q \cong \mathrm{SU}_q(2)$. The inner-automorphism $2$-group $\mathrm{INN}(G_q)$ governs the quantum flatness condition $F_A = B$, reproducing the instanton equation $F_A^- = 0$ under simplicity. Quantum flatness operates as a derived consequence of the instanton axiom.
<!-- FILE_END: emergence-to-quantum-flat.md -->

<!-- FILE_START: simplicity-from-category.md -->
The $*$-involution enforces self-duality on the $2$-forms. The categorical axioms mandate the sequence: volume constraint $\Rightarrow G_q = \mathrm{SU}_q(2) \Rightarrow F_A = B \Rightarrow B = F_A^+ \Rightarrow F_A^- = 0$. The geometric input reduces entirely to the CR structure.
<!-- FILE_END: simplicity-from-category.md -->

<!-- FILE_START: frobenius-simplification.md -->
The Haar state $h_q$ induces a non-degenerate Frobenius pairing on $\mathcal{O}_q(\mathrm{SU}(2))$. The non-degeneracy of the Frobenius form forces $H^0(M, \mathrm{Ad}(A)) = 0$, as any global parallel section in the adjoint representation would pair with itself against the irreducibility constraint.
<!-- FILE_END: frobenius-simplification.md -->

<!-- FILE_START: j1e-local-states.md -->
The jet bundle $J^1 \mathcal{S}$ accommodates the local states. The substrate parameter $q$ weights the classical gauge dynamics on the instanton connection to constitute the quantum field algebra $\mathrm{SU}_q(2)$.
<!-- FILE_END: j1e-local-states.md -->
