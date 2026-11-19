**Definition.**
A **quantum universe** is a tuple $(\mathbf{C}, A, \tau)$ consisting of:
1. an $R$-linear braided [monoidal category](#def:rigid-monoidal-category) $\mathbf{C}$ over a commutative ring $R$, whose unit endomorphisms recover the ground ring: $R \xrightarrow{\ \sim\ } \mathrm{End}_{\mathbf{C}}(\mathbf{1})$, $r \mapsto r \cdot \mathrm{id}_{\mathbf{1}}$,
2. a distinguished object $A \in \mathrm{Ob}(\mathbf{C})$ equipped with a [Frobenius--Hopf substrate](#def:frobenius-hopf-substrate) structure and a universal first-order differential calculus $\Omega^1(A) = \ker(\mu \colon A \otimes A \to A)$,
3. an $R$-linear faithful fibre functor $\tau \colon \mathbf{C} \to R\text{-}\mathbf{Mod}$,

satisfying the following three axioms:
1. **(Temporal braiding)** The ordering $\prec_c$ induced by the braiding $c_{V,W} \colon V \otimes W \xrightarrow{\sim} W \otimes V$ on the basis of $A$ is well-founded.
2. **(Frobenius--Hopf substrate action)** $A$ carries the compatible associative multiplication $\mu$, co-multiplication $\Delta$, unit $\eta$, co-unit $\varepsilon$, involutive antipode $S$, and Frobenius form $\int_A$ of a [Frobenius--Hopf substrate](#def:frobenius-hopf-substrate), and acts on every $V \in \mathbf{C}$ via a categorical representation $\rho_V \colon A \otimes V \to V$.
3. **(Symmetric Frobenius trace)** The left and right categorical traces on $\mathrm{End}(A)$ coincide. These traces are defined by the self-duality of $A$, which the [snake identities](#def:snake-identity) for the pairing $\int_A \circ\, \mu$ supply in the Frobenius--Hopf substrate datum.

Rigidity of $\mathbf{C}$ is not required here. Duals for arbitrary objects of $\mathbf{C}$ are imposed only at the next structural level, where they carry antiparticles and close braid strands into knots.

**On the ground ring and simplicity of the unit.** The base $R$ is an arbitrary commutative ring, not necessarily a field. The identification $R \xrightarrow{\sim} \mathrm{End}_{\mathbf{C}}(\mathbf{1})$ in item 1 is a genuine hypothesis and not a consequence of $R$-linearity: linearity supplies only the ring homomorphism $r \mapsto r \cdot \mathrm{id}_{\mathbf{1}}$, whereas its bijectivity is the statement that the monoidal unit $\mathbf{1}$ is simple. That isomorphism is what licenses reading categorical traces and pairings valued in $\mathrm{End}_{\mathbf{C}}(\mathbf{1})$ directly as elements of $R$.
