**Definition.**
A **quantum universe** is a tuple $(\mathbf{C}, A, \tau)$ consisting of:
1. an $R$-linear rigid [monoidal category](#monoidal-category) $\mathbf{C}$,
2. a distinguished object $A \in \mathrm{Ob}(\mathbf{C})$ equipped with a [Frobenius–Hopf algebra](#frobenius-hopf-algebra) structure,
3. an $R$-linear faithful fibre functor $\tau \colon \mathbf{C} \to \mathbf{Vect}_R$,

satisfying the following five axioms:
1. **(Rigidity)** Every object $V \in \mathbf{C}$ possesses left and right duals.
2. **(Frobenius--Hopf)** $A$ carries compatible associative multiplication $\mu$, co-multiplication $\Delta$, unit $\eta$, co-unit $\varepsilon$, and antipode $S$. The space $A$ acts on every $V \in \mathbf{C}$ via a categorical representation $\rho_V \colon A \otimes V \to V$.
3. **(Temporal braiding)** $\mathbf{C}$ admits a braiding isomorphism $c_{V,W} \colon V \otimes W \xrightarrow{\sim} W \otimes V$. The induced ordering $\prec_c$ on the Hecke basis of $A$ is well-founded.
4. **(Spherical)** The left and right categorical traces coincide for every endomorphism.
5. **(Mass identity)** The Frobenius codimensional trace identity ([Frobenius co-Casimir universal](#thm:frobenius-codim-universal)) holds in $A$:
$$
  \tau_M(C_{\dim_q}) \;=\; \sum_\lambda \frac{1}{\dim_q(\lambda)}.
$$
