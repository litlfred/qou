**Definition.**
A **quantum universe** is a tuple $(\mathbf{C}, A, \tau)$ consisting of:
1. an $R$-linear braided [monoidal category](#def:rigid-monoidal-category) $\mathbf{C}$,
2. a distinguished object $A \in \mathrm{Ob}(\mathbf{C})$ equipped with a [Frobenius–Hopf algebra](#def:frobenius-hopf-substrate) structure,
3. an $R$-linear faithful fibre functor $\tau \colon \mathbf{C} \to \mathbf{Vect}_R$,

satisfying the following four axioms:
1. **(Temporal braiding)** The ordering $\prec_c$ induced by the braiding $c_{V,W} \colon V \otimes W \xrightarrow{\sim} W \otimes V$ on the Hecke basis of $A$ is well-founded.
2. **(Frobenius--Hopf)** $A$ carries compatible associative multiplication $\mu$, co-multiplication $\Delta$, unit $\eta$, co-unit $\varepsilon$, and antipode $S$. The space $A$ acts on every $V \in \mathbf{C}$ via a categorical representation $\rho_V \colon A \otimes V \to V$.
3. **(Symmetric Frobenius)** The left and right categorical traces on $\mathrm{End}(A)$ coincide. These traces are defined by the self-duality of $A$, which the snake identities for the pairing $\int_A \circ\, \mu$ supply in axiom 2.
4. **(Mass identity)** The Frobenius codimensional trace identity ([Frobenius co-Casimir universal](#thm:frobenius-codim-universal)) holds in $A$:
$$
  \mathrm{tr}_M(C_{\dim_q}) \;=\; \sum_\lambda \frac{1}{\dim_q(\lambda)}.
$$

Rigidity of $\mathbf{C}$ is not required here. It is imposed on a [quantum observable universe](#def:quantum-observable-universe), where duals carry the antiparticles.
