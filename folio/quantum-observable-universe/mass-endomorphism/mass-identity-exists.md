Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe ([quantum observable universe](#def:quantum-observable-universe)) and $\varrho \colon \mathbf{1} \to A$ a closed cycle. The inertial mass

$$
  \mathfrak{m}(\varrho)
  \;=\;
  \bigl\lVert
    \mathrm{tr}\bigl( (\int_A \otimes \mathrm{id}) \circ \Delta \circ \varrho \bigr)
  \bigr\rVert
$$

of the [mass identity](#def:mass-identity) is a well-defined element of $R$ for every $\varrho$, by construction. Each step of the composite is a morphism of $\mathbf{C}$ or a map on $R$ that the definition already supplies:

1. $\Delta \colon A \to A \otimes A$ is part of the Frobenius--Hopf
   structure on $A$.
2. $\int_A \otimes \mathrm{id} \colon A \otimes A \to \mathbf{1} \otimes A \cong A$
   is a morphism by tensor functoriality.
3. $\mathrm{tr} \colon \mathrm{End}_{\mathbf{C}}(A) \to R$ is given by
   the rigid dual structure
   ([rigid :refterm[monoidal category]{#monoidal-category}](#def:rigid-monoidal-category)).
4. The norm $\lVert \cdot \rVert$ on $R$ induced by the
   [Frobenius pairing](#def:frobenius-pairing) is defined on every
   element of $R$.

Nothing here is a further claim; it records that the definition is total. Its archimedean value is non-negative, since it is a norm.
