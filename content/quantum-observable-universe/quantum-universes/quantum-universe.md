**Definition.**
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

Rigidity of $\mathbf{C}$ is not required here. It is imposed on a [quantum observable universe](#def:quantum-observable-universe), where duals carry the antiparticles.

**On the ground ring.** $R$ is a commutative ring, not a field, and "invertible in $R$" in axiom 4 is strictly stronger than "nonzero" once $R$ has non-units. The two clauses coincide only over a field.

**Which commutative ring.** The Laurent ring $\mathbb{Z}[q, q^{-1}]$ alone is *not* enough: its units are exactly $\pm q^{k}$, while each quantum integer factors as a monomial times a cyclotomic product of positive degree — $[2]_q = q^{-1}\Phi_4(q)$, $[3]_q = q^{-2}\Phi_3\Phi_6$, $[4]_q = q^{-3}\Phi_4\Phi_8$ — so no $[m]_q$ with $m \geq 2$ is a unit and axiom 4 fails for every block beyond the trivial one. The ground ring is therefore the localisation

$$
  R \;=\; \mathbb{Z}[q, q^{-1}]\bigl[\, \Phi_d(q)^{-1} \;:\; d \geq 2 \,\bigr],
$$

whose spectrum is the $q$-line with the roots of unity of order $\geq 2$ removed — precisely the locus axiom 4 forbids. Starting the localisation at $d = 1$ would additionally delete $q = 1$, which the classical limit needs, and nothing requires it: $q^{n} - 1 = (q-1)\,[n]_q$, so $q^n - 1$ is a unit exactly when $q - 1$ is, and the constructs that invert $q - 1$ live past the archimedean wall.

**The definition does not depend on that choice.** What the axioms use is only that $q$ and every $\Phi_d(q)$, $d \geq 2$, are invertible — the property `QOU.AlgebraicSubstrate.IsQGeneric`. The ring above is the *initial* object satisfying it, so any other base with the same property — $\mathbb{Q}(q)$ for generic-$q$ representation theory, a real algebra at the substrate anchor, a neighbouring convention's Laurent ring — receives a unique map from it and inherits every statement made here. The property transports along any ring homomorphism (`IsQGeneric.map`), which is what makes a definition stated over it usable in each such setting without restatement.

The identification $R \cong \mathrm{End}_{\mathbf{C}}(\mathbf{1})$ in item 1 is a genuine hypothesis and not a consequence of $R$-linearity. Linearity supplies only the ring map $r \mapsto r \cdot \mathrm{id}_{\mathbf{1}}$; its bijectivity is the statement that $\mathbf{1}$ is simple, and it is what licenses reading the block data $\int_A p_\lambda$ and $\dim_q(\lambda)$ as elements of $R$ rather than as endomorphisms of the unit. It is stated here because the rest of the paper uses it silently — for instance in taking the substrate parameter $q \in \mathrm{End}(\mathbf{1})$.
