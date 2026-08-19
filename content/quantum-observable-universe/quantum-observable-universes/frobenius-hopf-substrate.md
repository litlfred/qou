Let $\mathbf{C}$ be a monoidal category. A **Frobenius--Hopf substrate** is a sextuple $(A, \mu, \eta, \Delta, \varepsilon, S)$ in $\mathbf{C}$ equipped with a Frobenius form $\lambda \colon A \to \mathbf{1}$ satisfying the following axioms:

1. **Algebra structure:** The morphisms $\mu \colon A \otimes A \to A$ and $\eta \colon \mathbf{1} \to A$ make $A$ an associative unital algebra object in $\mathbf{C}$.
2. **Coalgebra structure:** The morphisms $\Delta \colon A \to A \otimes A$ and $\varepsilon \colon A \to \mathbf{1}$ make $A$ a coassociative counital coalgebra object, with antipode $S \colon A \to A$ satisfying the Hopf compatibility $\varepsilon \circ \mu = u \circ (\varepsilon \otimes \varepsilon)$, where $u$ is the canonical unit isomorphism.
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

An earlier version of this definition opened *"Let $\mathbf{C}$ be a rigid monoidal category"* and phrased axioms 4--5 as *"the induced map $A \to A^\vee$ is an isomorphism"*. That notation presupposes an ambient dual $A^\vee$, which made this definition unusable at the level that actually invokes it: `def:quantum-universe` requires a Frobenius--Hopf object while explicitly stating that rigidity of $\mathbf{C}$ is *not* required there. The formalization never assumed rigidity either --- `FrobeniusHopfData` is stated over a bare monoidal category and derives self-duality from $\mathrm{coev}$ plus the snake identities, exactly as axiom 4 now does.
