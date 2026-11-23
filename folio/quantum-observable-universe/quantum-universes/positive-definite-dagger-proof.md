Write $h(f, g) = \int_A \mu(S(f) \otimes g)$ and $L_x$ for left
multiplication by $x \in A$.

**Adjoint of $L_x$.** Since $S$ is anti-multiplicative,
$S(x a) = S(a)\,S(x)$, so

$$
  h(L_x a, b) = \int_A \mu\bigl(S(a)\,S(x) \otimes b\bigr)
  = \int_A \mu\bigl(S(a) \otimes S(x)\, b\bigr) = h(a, L_{S(x)} b).
$$

**Uniqueness.** If $U$ is $R$-linear with $h(L_x a, b) = h(a, U b)$ for all
$a, b$, put $c = U b - S(x) b$. Then $h(c, c) = h(c, U b) - h(c, S(x) b) =
h(L_x c, b) - h(L_x c, b) = 0$, so $c = 0$ by positive definiteness.

**Involution and contravariance.** Applying the adjoint formula to $S(x)$
gives $h(L_{S(x)} a, b) = h(a, L_{S^2(x)} b) = h(a, L_x b)$, using
$S^2 = \mathrm{id}$. Applying it to $x y$ gives
$h(L_{xy} a, b) = h(a, L_{S(y)} L_{S(x)} b)$, using $S(xy) = S(y)\,S(x)$.
The involution $S^2 = \mathrm{id}$ is a hypothesis: for a pivotal Hopf
algebra $S^2$ is conjugation by the pivotal element, which is the identity
only in the involutory case.

**Scalars.** For $r \in R$, $S(r \cdot 1) = r\,S(1) = r \cdot 1$, so on
$\mathrm{End}(\mathbf{1}) \cong R$ the dagger is $S$ and fixes every scalar.

**Positivity.** $f^{\dagger} \circ f = \int_A \mu(S(f) \otimes f) = h(f, f)$,
which is positive for $f \neq 0$ by hypothesis. $\square$

Positivity does not follow from non-degeneracy of the pairing: a
non-degenerate form can have isotropic vectors. On $R^2$ the form
$\langle x, y\rangle = x_1 y_2 + x_2 y_1$ is non-degenerate and
$\langle e_1, e_1\rangle = 0$. The positivity of $h$ is therefore an input,
as in the GNS construction, where it is the positivity of the state
(\cite{kock2004}, Ch. 2, for the Frobenius side).
