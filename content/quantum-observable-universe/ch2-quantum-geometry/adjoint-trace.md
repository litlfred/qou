The [Frobenius pairing](#def:frobenius-pairing) and the
[fibre-adjoint involution](#prop:fiber-adjoint-involution) together
equip every hom-space $\mathrm{Hom}_{\mathbf{C}}(X, Y)$ with a
canonical sesquilinear form. Define the *adjoint trace* on
endomorphisms of $V$ by

$$
  \mathrm{tr}_{\mathrm{Ad}}(f)
  \;=\;
  \int_A \!\circ\; \mu \circ (f \otimes \mathrm{id}_{V^{\vee}})
    \circ \mathrm{coev}_V
  \;\in\;
  \mathrm{Hom}(\mathbf{1}, \mathbf{1}) \cong R,
$$

where $\mathrm{coev}_V \colon \mathbf{1} \to V \otimes V^{\vee}$ is
the coevaluation (from rigidity) and $\mu$ is the Frobenius
multiplication on $A$.

This trace has two key properties:

1. **Cyclicity**: $\mathrm{tr}_{\mathrm{Ad}}(f \circ g) =
   \mathrm{tr}_{\mathrm{Ad}}(g \circ f)$, inherited from the
   Frobenius relation.
2. **Non-degeneracy**: the induced pairing
   $\langle f, g \rangle_{\mathrm{Ad}} =
   \mathrm{tr}_{\mathrm{Ad}}(f^{\dagger} \circ g)$
   is non-degenerate, because $\int_A$ is non-degenerate and the
   dagger is positive-definite.

In the archimedean realisation with $G = \mathrm{SU}(2)$, the adjoint
trace recovers the Killing form on $\mathfrak{su}(2)$:
$$
  \mathrm{tr}_{\mathrm{Ad}}(f)
  \;=\;
  \mathrm{tr}(\mathrm{ad}(f))
  \;=\;
  -2\,\mathrm{tr}_{\mathbb{C}^2}(f).
$$
