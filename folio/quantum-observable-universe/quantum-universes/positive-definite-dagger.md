A positive-definite dagger gives categorical states genuine squared lengths. Let $(\mathbf{C}, A)$ be a [quantum universe](#def:quantum-universe) whose endomorphism ring $\mathrm{End}(\mathbf{1}) \cong R$ is an ordered field. Assume a [Frobenius pairing](#def:frobenius-pairing) with form $\int_A$, and an antipode $S$ that is $R$-linear, involutive ($S^2 = \mathrm{id}$), anti-multiplicative ($S(xy) = S(y)\,S(x)$) and unital.

For a morphism $f \colon \mathbf{1} \to A$ define the *Frobenius dagger*

$$
  f^{\dagger} =  \int_A \circ\, \mu(S(f) \otimes -),
$$

and the form $h(f, g) = \int_A \mu(S(f) \otimes g)$, so that $f^{\dagger} \circ f = h(f, f)$. Assume that $h$ is positive definite: $h(f, f) > 0$ for every non-zero $f \colon \mathbf{1} \to A$. Write $L_x$ for left multiplication by $x \in A$. Then:

1. $L_{S(x)}$ is the unique $R$-linear adjoint of $L_x$ for $h$, that is $h(L_x a, b) = h(a, L_{S(x)} b)$;
2. the dagger $L_x^{\dagger} = L_{S(x)}$ is an [involutive structure](#def:involutive-structure) on these operators: $L_x^{\dagger\dagger} = L_x$ and $(L_x L_y)^{\dagger} = L_y^{\dagger} L_x^{\dagger}$;
3. on $\mathrm{End}(\mathbf{1}) \cong R$ the dagger is $S$, which is the identity there;
4. $f^{\dagger} \circ f > 0$ for every non-zero $f \colon \mathbf{1} \to A$.

Item 4 is the positivity hypothesis on $h$ read through $f^{\dagger} \circ f = h(f, f)$.
