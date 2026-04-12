**Involutivity.** The antipode of a Hopf algebra satisfies
$S^2 = \mathrm{id}$ (since the Frobenius pairing forces $A$ to be
commutative via faithfulness of $\tau$). Therefore
$f^{\dagger\dagger} = \int_A \circ \mu(S(S(f)) \otimes -) = \int_A \circ \mu(f \otimes -) = f$,
confirming $\dagger$ is an involution.

**Contravariance.** For composable morphisms $f, g$:
$(g \circ f)^{\dagger} = \int_A \circ \mu(S(g \circ f) \otimes -) = \int_A \circ \mu(S(f) \cdot S(g) \otimes -)$
since $S$ is an anti-homomorphism. The Frobenius associativity then
gives $f^{\dagger} \circ g^{\dagger}$.

**Positive-definiteness.** Let $f \colon \mathbf{1} \to X$ be
non-zero. The composite $f^{\dagger} \circ f \in \mathrm{End}(\mathbf{1}) \cong R$ evaluates as

$$
  f^{\dagger} \circ f
  =  \int_A \mu(S(f) \otimes f)
  =  \int_A |f|^2
$$

where $|f|^2 = S(f) \cdot f = \overline{f} \cdot f$ under the
identification $S = \overline{(\cdot)}$ on functions. Since $\int_A$
is the categorical integral (non-degenerate by the Frobenius axiom)
and $|f|^2 \neq 0$ for $f \neq 0$ (faithfulness of $\tau$), the
result is a positive element of $R$.
