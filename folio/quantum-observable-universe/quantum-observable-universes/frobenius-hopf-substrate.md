Let $\mathbf{C}$ be a braided monoidal category, with braiding $\beta$. A **Frobenius--Hopf substrate** is a sextuple $(A, \mu, \eta, \Delta, \varepsilon, S)$ in $\mathbf{C}$ equipped with a Frobenius form $\lambda \colon A \to \mathbf{1}$ satisfying the following axioms:

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

   In elements the first two read $S(ab) = S(b)\,S(a)$ and $\Delta(S x) = \sum S(x_{(2)}) \otimes S(x_{(1)})$. The braiding $\beta$ is what makes "reverses" expressible, which is why $\mathbf{C}$ is taken braided; that is no extra demand, since the substrate is invoked at the level of a [quantum universe](#def:quantum-universe), which is braided monoidal.

   **$S$ is constrained but not determined.** Every classical unimodular antipode (such as $S(g) = g^{-1}$ on $k[G]$ or inversion on $\mathcal{O}(G)$ at $q = 1$) satisfies these six conditions, and on a non-commutative $A$ they exclude the trivial choice $S = \mathrm{id}_A$. Away from the involutive unimodular point --- for instance on $\mathcal{O}_q(\mathrm{SU}(2))$ at $q \neq \pm 1$, where $S^2(\beta) = q^{-2}\beta$, or on a non-unimodular finite Hopf algebra such as the Taft algebra $H_4$, where $S^2(X) = -X$ and $\lambda \circ S \neq \lambda$ --- the last two identities deform to the pivotal square law $S \circ S = \gamma_A$ for an automorphism $\gamma_A \colon A \xrightarrow{\sim} A$ and the modular-shifted law $\lambda \circ S = \lambda \circ \mu_{\mathrm{mod}}$. Even in the involutive case these conditions do not single $S$ out: the only condition that does is the convolution identity $\mu \circ (S \otimes \mathrm{id}) \circ \Delta = \eta \circ \varepsilon$, and that identity forces $A$ to be trivial whenever the scalars form a field, so it cannot be imposed here.
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

5. **Self-duality:** The pair $(\mathrm{ev}, \mathrm{coev})$ *exhibits* $A$ as its own dual. This couples the observer trace $\Phi = \lambda \circ \mu$ to the observed state space intrinsically, and it is what makes the left and right categorical traces on $\mathrm{End}(A)$ available.

**Duals are required of $A$ only, not of $\mathbf{C}$.** Axiom 4 supplies $\mathrm{coev}$ as part of the data, so $A$ carries its own duality datum and no object of $\mathbf{C}$ other than $A$ need have a dual. Consequently a Frobenius--Hopf object is available already at the level of a [quantum universe](#def:quantum-universe), which is braided monoidal but *not* rigid; rigidity is imposed one level up, on a [quantum observable universe](#def:quantum-observable-universe), where duals for every object carry the antiparticles and let a strand close into a knot.
