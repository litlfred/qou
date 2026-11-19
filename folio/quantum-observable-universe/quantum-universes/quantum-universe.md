A **quantum universe** is a tuple $(\mathbf{C}, A, \tau)$ consisting of:
1. an $R$-linear braided [monoidal category](#def:rigid-monoidal-category) $\mathbf{C}$ over a commutative ring $R$, whose unit endomorphisms recover the ground ring: $R \xrightarrow{\ \sim\ } \mathrm{End}_{\mathbf{C}}(\mathbf{1})$, $r \mapsto r \cdot \mathrm{id}_{\mathbf{1}}$,
2. a distinguished object $A \in \mathrm{Ob}(\mathbf{C})$ equipped with a [Frobenius–Hopf algebra](#def:frobenius-hopf-substrate) structure,
3. an $R$-linear faithful fibre functor $\tau \colon \mathbf{C} \to R\text{-}\mathbf{Mod}$,

satisfying the following four axioms:
1. **(Temporal braiding)** The ordering $\prec_c$ induced by the braiding $c_{V,W} \colon V \otimes W \xrightarrow{\sim} W \otimes V$ on the Hecke basis of $A$ is well-founded.
2. **(Frobenius--Hopf)** $A$ carries compatible associative multiplication $\mu$, co-multiplication $\Delta$, unit $\eta$, co-unit $\varepsilon$, and antipode $S$. The space $A$ acts on every $V \in \mathbf{C}$ via a categorical representation $\rho_V \colon A \otimes V \to V$.
3. **(Symmetric Frobenius)** The left and right categorical traces on $\mathrm{End}(A)$ coincide. These traces are defined by the self-duality of $A$, which the snake identities for the pairing $\int_A \circ\, \mu$ supply in axiom 2.
4. **(Wedderburn semisimplicity)** $A$ is semisimple, with a finite index set $\widehat{A}$ of blocks. Each block $\lambda \in \widehat{A}$ carries a central idempotent $p_\lambda$, and these

```tex
\[
\begin{aligned}
\text{do not mix:} && p_\lambda \circ p_\mu &= 0 && (\lambda \neq \mu), \\
\text{and span:}   && \textstyle\sum_{\lambda \in \widehat{A}} p_\lambda &= \mathrm{id}_A. &&
\end{aligned}
\]
```

   Each block further carries a Frobenius weight $\int_A p_\lambda$ invertible in $R$, and a quantum dimension $\dim_q(\lambda)$ invertible in $R$.
