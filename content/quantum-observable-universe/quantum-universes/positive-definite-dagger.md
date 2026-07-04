**Proposition (conditional on a formally-real pivotal structure).**
Let $(\mathbf{C}, A, \tau)$ be a
[quantum universe](#def:quantum-universe) whose endomorphism ring
$\mathrm{End}(\mathbf{1}) \cong R$ is a formally-real ordered field,
equipped with a [Frobenius pairing](#def:frobenius-pairing)
$\langle a, b \rangle = \int_A(\mu(a \otimes b))$ and a pivotal antipode
$S$ that is self-adjoint for the pairing — so the Frobenius dagger,
defined below, satisfies $S^2 = \mathrm{id}$ and restricts to
$S = \dagger$ on $\mathrm{End}(\mathbf{1})$.

Define the *Frobenius dagger* on morphisms by

$$
  f^{\dagger} =  \int_A \circ\, \mu(S(f) \otimes -).
$$

Then $\dagger$ is a positive-definite
[involutive structure](#def:involutive-structure) on $\mathbf{C}$: for
every non-zero morphism $f \colon \mathbf{1} \to X$, the composite
$f^{\dagger} \circ f = \langle f, f\rangle$ is a positive element of
$\mathrm{End}(\mathbf{1}) \cong R$.
