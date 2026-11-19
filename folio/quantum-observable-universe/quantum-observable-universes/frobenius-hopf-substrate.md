Let $\mathbf{C}$ be a braided monoidal category, with braiding $\beta$. A **Frobenius--Hopf substrate** is a sextuple $(A, \mu, \eta, \Delta, \varepsilon, S)$ in $\mathbf{C}$ equipped with a Frobenius form $\lambda \colon A \to \mathbf{1}$ satisfying the following axioms:

1. **Algebra structure:** The morphisms $\mu \colon A \otimes A \to A$ and $\eta \colon \mathbf{1} \to A$ make $A$ an associative unital algebra object in $\mathbf{C}$.
2. **Coalgebra structure and antipode:** The morphisms $\Delta \colon A \to A \otimes A$ and $\varepsilon \colon A \to \mathbf{1}$ make $A$ a coassociative counital coalgebra object.

   The antipode $S \colon A \to A$ is an *involutive anti-automorphism of the whole structure*:

```tex
\[
\begin{aligned}
  S \circ \mu &= \mu \circ \beta_{A,A} \circ (S \otimes S),
  &\qquad \Delta \circ S &= (S \otimes S) \circ \beta_{A,A} \circ \Delta, \\
  S \circ \eta &= \eta,
  &\qquad \varepsilon \circ S &= \varepsilon, \\
  S \circ S &= \mathrm{id}_A,
  &\qquad \lambda \circ S &= \lambda.
\end{aligned}
\]
```

3. **Frobenius relation:** The Frobenius form $\lambda$ satisfies $\mu \circ \Delta = (\Delta \otimes \mathrm{id}) \circ \alpha \circ (\mathrm{id} \otimes \mu)$, where $\alpha$ is the associator in $\mathbf{C}$.
4. **Non-degeneracy:** Write $\mathrm{ev} = \lambda \circ \mu \colon A \otimes A \to \mathbf{1}$ for the Frobenius pairing $\langle a, b \rangle_F = \lambda(\mu(a \otimes b))$. There is a morphism $\mathrm{coev} \colon \mathbf{1} \to A \otimes A$ such that both snake identities hold:

```tex
\[
\begin{aligned}
(\mathrm{id}_A \otimes \mathrm{ev}) \circ (\mathrm{coev} \otimes \mathrm{id}_A) &= \mathrm{id}_A, \\
(\mathrm{ev} \otimes \mathrm{id}_A) \circ (\mathrm{id}_A \otimes \mathrm{coev}) &= \mathrm{id}_A,
\end{aligned}
\]
```

   each read modulo the unitors and the associator of $\mathbf{C}$.

5. **Self-duality:** The pair $(\mathrm{ev}, \mathrm{coev})$ *exhibits* $A$ as its own dual.
