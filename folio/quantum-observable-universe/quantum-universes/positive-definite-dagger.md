A positive-definite dagger gives categorical states genuine squared lengths. Let $(\mathbf{C}, A)$ be a [quantum universe](#def:quantum-universe) whose endomorphism ring $\mathrm{End}(\mathbf{1}) \cong R$ is an ordered field. Assume a [Frobenius pairing](#def:frobenius-pairing) and an antipode $S$ that is involutive ($S^2 = \mathrm{id}$) and self-adjoint for the pairing.

Define the *Frobenius dagger* on morphisms by:

$$
  f^{\dagger} =  \int_A \circ\, \mu(S(f) \otimes -).
$$

Then $\dagger$ is an [involutive structure](#def:involutive-structure) that restricts to $S$ on $\mathrm{End}(\mathbf{1})$, and $f^{\dagger} \circ f = h(f, f)$, where $h(f, g) = \int_A \mu(S(f) \otimes g)$. If moreover $h$ is positive definite, that is $h(f, f) > 0$ for every non-zero $f \colon \mathbf{1} \to X$, then $\dagger$ is positive definite.
