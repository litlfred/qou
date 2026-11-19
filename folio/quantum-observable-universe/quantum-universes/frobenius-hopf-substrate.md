Let $\mathbf{C}$ be a braided [monoidal category](#def:rigid-monoidal-category), with braiding $\beta$. A **Frobenius--Hopf aether** is a sextuple $(A, \mu, \eta, \Delta, \varepsilon, S)$ in $\mathbf{C}$ equipped with a Frobenius form $\lambda \colon A \to \mathbf{1}$ satisfying the following axioms:

1. **Algebra structure:** The morphisms $\mu \colon A \otimes A \to A$ and $\eta \colon \mathbf{1} \to A$ make $A$ an associative unital algebra object in $\mathbf{C}$.
2. **Coalgebra structure and antipode:** The morphisms $\Delta \colon A \to A \otimes A$ and $\varepsilon \colon A \to \mathbf{1}$ make $A$ a coassociative counital coalgebra object. The counit is **not** required to be multiplicative: together with the Frobenius relation (axiom 3) and counitality, $\varepsilon(ab) = \varepsilon(a)\,\varepsilon(b)$ forces $x = \varepsilon(x)\cdot 1$ for every $x$, so $A$ would be spanned by its unit.

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

   In elements the first two read $S(ab) = S(b)\,S(a)$ and $\Delta(S x) = \sum S(x_{(2)}) \otimes S(x_{(1)})$. The braiding $\beta$ is what makes reversal of multiplication and comultiplication expressible, which is why $\mathbf{C}$ is taken braided.

   **$S$ is constrained but not determined.** Every classical antipode satisfies these six conditions, and on a non-commutative $A$ they exclude the trivial choice $S = \mathrm{id}_A$. They do not single $S$ out: the only condition that does is the convolution identity $\mu \circ (S \otimes \mathrm{id}) \circ \Delta = \eta \circ \varepsilon$, and that identity forces $A$ to be trivial whenever the scalars form a field, so it cannot be imposed here.
3. **Frobenius relation:** The Frobenius form $\lambda$ satisfies $\mu \circ \Delta = (\Delta \otimes \mathrm{id}) \circ \alpha \circ (\mathrm{id} \otimes \mu)$, where $\alpha$ is the associator in $\mathbf{C}$.
4. **Non-degeneracy:** Write $\mathrm{ev} = \lambda \circ \mu \colon A \otimes A \to \mathbf{1}$ for the Frobenius pairing $\langle a, b \rangle_F = \lambda(\mu(a \otimes b))$. There is a morphism $\mathrm{coev} \colon \mathbf{1} \to A \otimes A$ such that both [snake identities](#def:snake-identity) hold:

```tex
\[
\begin{aligned}
(\mathrm{id}_A \otimes \mathrm{ev}) \circ (\mathrm{coev} \otimes \mathrm{id}_A) &= \mathrm{id}_A, \\
(\mathrm{ev} \otimes \mathrm{id}_A) \circ (\mathrm{id}_A \otimes \mathrm{coev}) &= \mathrm{id}_A,
\end{aligned}
\]
```

   each read modulo the unitors and the associator of $\mathbf{C}$.

5. **Self-duality:** The pair $(\mathrm{ev}, \mathrm{coev})$ *exhibits* $A$ as its own dual. This couples the observer trace $\Phi = \lambda \circ \mu$ to the observed state space intrinsically, and it is what makes the left and right categorical traces on $\mathrm{End}(A)$ available.

**Duals are required of $A$ only, not of $\mathbf{C}$.** Axiom 4 supplies $\mathrm{coev}$ as part of the data, so $A$ carries its own duality datum and no object of $\mathbf{C}$ other than $A$ need have a dual. Consequently a Frobenius--Hopf aether is defined in a braided monoidal category without assuming ambient rigidity on $\mathbf{C}$.
