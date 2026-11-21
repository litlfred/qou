Write $\langle a, b\rangle = \int_A \mu(a \otimes b)$ for the Frobenius
pairing and $h(f, g) = \langle S(f), g \rangle$.

**Involutivity.** Expanding
$(f^{\dagger})^{\dagger} = \int_A \mu(S(f^{\dagger}) \otimes -)$ and
applying the hypothesis $S^2 = \mathrm{id}$ together with Frobenius
associativity
$\int_A \mu(\mu \otimes \mathrm{id}) = \int_A \mu(\mathrm{id} \otimes \mu)$
gives $(f^{\dagger})^{\dagger} = f$. Contravariance
$(g \circ f)^{\dagger} = f^{\dagger} \circ g^{\dagger}$ follows because
$S$ is an anti-homomorphism. Hence $\dagger$ is an involutive structure.
The involution $S^2 = \mathrm{id}$ is a hypothesis: for a pivotal Hopf
algebra $S^2$ is conjugation by the pivotal element, which is the identity
only in the involutory case.

**The norm.** For $f \colon \mathbf{1} \to X$,

$$
  f^{\dagger} \circ f
  = \int_A \mu(S(f) \otimes f)
  = h(f, f) \in \mathrm{End}(\mathbf{1}) \cong R.
$$

**Positivity.** If $h$ is positive definite, $f^{\dagger} \circ f > 0$ for
every non-zero $f$, and $\dagger$ is positive definite. $\square$

Positivity does not follow from non-degeneracy of the pairing: a
non-degenerate form can have isotropic vectors. On $R^2$ the form
$\langle x, y\rangle = x_1 y_2 + x_2 y_1$ is non-degenerate and
$\langle e_1, e_1\rangle = 0$. Nor does self-adjointness of $S$ make
$h(f, f)$ a square. The positivity of $h$ is therefore an input, as in the
GNS construction, where it is the positivity of the state
(\cite{kock2004}, Ch. 2, for the Frobenius side).
