Write $\langle a, b\rangle = \int_A \mu(a \otimes b)$ for the Frobenius
pairing, non-degenerate by
[Frobenius pairing exists](#prop:frobenius-pairing-exists). Throughout,
$R \cong \mathrm{End}(\mathbf{1})$ is the formally-real ordered field and
$S$ is the pivotal self-adjoint antipode of the hypotheses.

A positive-definite dagger structure requires two things: that
$\dagger$ is an involution, and that $f^{\dagger} \circ f$ is strictly
positive for every non-zero $f$. Each is verified in turn.

**Involutivity.** Because the antipode is pivotal, $S^2 = \mathrm{id}$.
Expanding
$(f^{\dagger})^{\dagger} = \int_A \mu(S(f^{\dagger}) \otimes -)$ and
applying $S^2 = \mathrm{id}$ together with Frobenius associativity
$\int_A \mu(\mu \otimes \mathrm{id}) = \int_A \mu(\mathrm{id} \otimes \mu)$
gives $(f^{\dagger})^{\dagger} = f$. Contravariance
$(g \circ f)^{\dagger} = f^{\dagger} \circ g^{\dagger}$ follows because
$S$ is an anti-homomorphism. Hence $\dagger$ is an involutive structure.

**Positive-definiteness.** For non-zero $f \colon \mathbf{1} \to X$,

$$
  f^{\dagger} \circ f
  = \int_A \mu(S(f) \otimes f)
  = \langle f, f\rangle \in \mathrm{End}(\mathbf{1}) \cong R.
$$

By the self-adjoint hypothesis $S = \dagger$, the pairing evaluates $f$
against its own adjoint, so $\langle f, f\rangle = s^2$ is a square in
$R$ (the categorical norm-square of $f$). Non-degeneracy of the pairing
forces $\langle f, f\rangle \neq 0$ whenever $f \neq 0$. In a
formally-real ordered field a non-zero square is strictly positive, so
$f^{\dagger} \circ f > 0$. Therefore $\dagger$ is a positive-definite
involutive structure.

This is the categorical Frobenius-norm / GNS positivity construction
(\cite{kock2004}, Ch. 2). The three hypotheses are exactly the inputs the
argument consumes: non-degeneracy gives $\langle f, f\rangle \neq 0$, the
pivotal adjoint identification gives the square, and formal reality turns
a non-zero square into a positive element. $\square$
