**Proof.**
Throughout, $R$ is a field containing $\mathbb{Q}(q^{1/2})$ and $q$ is
generic: no quantum integer
$[k]_q = (q^k - q^{-k})/(q - q^{-1})$ vanishes for $k \geq 1$. We
write $z = 1/(q^{1/2} + q^{-1/2})$ for the Markov parameter fixed by
the framework normalisation $\mathrm{tr}_M(\sigma_i) = z$, and a
*Markov trace* means a compatible family of linear functionals
$\tau \colon H_n(R, q) \to R$, one for each level $n$ of the tower
$H_1 \subset H_2 \subset \cdots$, satisfying

1. **(M1, normalisation)** $\tau(1) = 1$;
2. **(M2, cyclicity)** $\tau(xy) = \tau(yx)$;
3. **(M3, Markov peel)** $\tau(x \sigma_{n-1}) = z \cdot \tau(x)$ for
   all $x \in H_{n-1}(R, q)$.

**Step 1: trace functionals on a split semisimple algebra.**
At generic $q$ the Iwahori–Hecke algebra is split semisimple, with
Wedderburn–Artin decomposition

$$
  H_n(R, q) \;\cong\; \bigoplus_{\lambda \vdash n} M_{d_\lambda}(R),
$$

one matrix block per partition $\lambda \vdash n$, where $d_\lambda$
is the number of standard Young tableaux of shape $\lambda$ (Wenzl
\cite{wenzl1988}). The irreducible characters
$\chi_\lambda$ form a basis of the space of cyclic functionals on a
split semisimple algebra, so every functional $\tau$ satisfying M2
admits a unique expansion

$$
  \tau \;=\; \sum_{\lambda \vdash n} w_\lambda \, \chi_\lambda,
  \qquad w_\lambda \in R.
$$

The associated bilinear form
$\langle x, y \rangle_\tau := \tau(xy)$ block-diagonalises along the
decomposition; on the block $M_{d_\lambda}(R)$ it equals $w_\lambda$
times the matrix-trace pairing $(x, y) \mapsto \mathrm{tr}(xy)$,
which is non-degenerate. Hence $\langle \cdot, \cdot \rangle_\tau$
is non-degenerate if and only if $w_\lambda \neq 0$ for every
$\lambda \vdash n$; equivalently, if and only if
$\tau(p_\lambda) \neq 0$ for one (hence every) primitive idempotent
$p_\lambda$ of each block, since $\tau(p_\lambda) = w_\lambda$.

**Step 2: existence and non-degeneracy of $\mathrm{tr}_M$.**
Jones (\cite{jones1987}, Theorem 6.1) constructs, for the parameter
$z$, a Markov trace $\mathrm{tr}_M$ on the tower satisfying M1–M3.
Its block weights admit the hook–content closed form

$$
  w_\lambda
  \;=\;
  \mathrm{tr}_M(p_\lambda)
  \;=\;
  \prod_{x \in \lambda}
  \frac{z\,q^{c(x)} - z_{-}\,q^{-c(x)}}{q^{h(x)} - q^{-h(x)}},
$$

where $c(x)$ and $h(x)$ are the content and hook length of the cell
$x$ and $z_{-} = z - (q - q^{-1})$ is the negative-crossing loop
value ([Markov axioms](#rem:markov-axioms-primitive)). This is the
Ocneanu weight formula at framing ratio $a^2 = z/z_{-}$, verified
exactly for every $\lambda \vdash n \leq 5$
([witness](computations/markov-trace-weights-wenzl.witness.json)).
A numerator factor vanishes only when $z/z_{-} = q^{-2c(x)}$, an
algebraic condition on $q$ with finitely many solutions per cell; at
generic $q$ every factor is non-zero, so
$\mathrm{tr}_M(p_\lambda) \neq 0$ for every $\lambda \vdash n$. By
Step 1, the Frobenius pairing
$\langle x, y \rangle = \mathrm{tr}_M(xy)$ is non-degenerate on
$H_n(R, q)$ — this is Wenzl's non-degeneracy lemma
(\cite{wenzl1988}, Lemma 2.4). In particular $\mathrm{tr}_M$ meets
the requirement $\tau(p_\lambda) \neq 0$ imposed by the Frobenius
co-Casimir construction (Step 3 of the chain in the statement
block).

**Step 3: uniqueness.**
Let $\tau$ be any Markov trace on the tower satisfying M1–M3 with
the same parameter $z$. We show $\tau = \mathrm{tr}_M$ at every
level, by induction on $n$.

*Base case.* $H_1(R, q) = R$, and M1 forces
$\tau(c) = c = \mathrm{tr}_M(c)$ for all $c \in R$.

*Inductive step.* Recall the Iwahori basis
$\{T_w\}_{w \in S_n}$ of $H_n(R, q)$, where
$T_w = \sigma_{i_1} \cdots \sigma_{i_\ell}$ for any reduced
expression $w = s_{i_1} \cdots s_{i_\ell}$. Every $w \in S_n$
either lies in $S_{n-1}$, or admits a reduced expression
$w = u \, s_{n-1} \, v$ with $u, v \in S_{n-1}$. Consequently

$$
  H_n(R, q)
  \;=\;
  H_{n-1}(R, q) \;+\; H_{n-1}(R, q)\, \sigma_{n-1}\, H_{n-1}(R, q).
$$

On the first summand, $\tau$ and $\mathrm{tr}_M$ agree by the
inductive hypothesis, since the restriction of a Markov trace to
$H_{n-1}(R, q)$ is again a Markov trace with the same parameter.
On the second summand, take $x, y \in H_{n-1}(R, q)$ and compute

$$
  \tau(x \, \sigma_{n-1} \, y)
  \;=\;
  \tau(y x \, \sigma_{n-1})
  \;=\;
  z \cdot \tau(yx)
  \;=\;
  z \cdot \mathrm{tr}_M(yx)
  \;=\;
  \mathrm{tr}_M(x \, \sigma_{n-1} \, y),
$$

using M2, then M3, then the inductive hypothesis, then M3 and M2
again for $\mathrm{tr}_M$. By linearity, $\tau = \mathrm{tr}_M$ on
$H_n(R, q)$. Note that no separate axiom is needed for negative
crossings: the quadratic relation
$\sigma_{n-1}^{-1} = \sigma_{n-1} - (q - q^{-1})$ yields the
negative-stabilisation value
$\tau(x \sigma_{n-1}^{-1}) = \bigl(z - (q - q^{-1})\bigr) \tau(x)$
automatically, identically for both functionals.

**Step 4: block-wise identification and selection.**
Since $\tau = \mathrm{tr}_M$ as functionals, the uniqueness of the
character expansion in Step 1 gives $w_\lambda = y_\lambda(q)$ for
every $\lambda \vdash n$: any trace satisfying the Markov-peel and
cyclic axioms equals $\mathrm{tr}_M$ block-wise. Combining the
steps: the QOU mass identity requires a non-degenerate Frobenius
pairing on $H_n(R, q)$ (Step 3 of the statement chain); the
categorical trace induced by the cat-action and the fibre functor
satisfies M1 (normalisation), M2 (cyclicity of the categorical
trace), and M3 (invariance of the Markov closure under positive
stabilisation, normalised so that a single positive crossing carries
the weight $z$).
By Steps 1–3 the only such functional is $\mathrm{tr}_M$, and by
Step 2 it is non-degenerate. Hence $\mathrm{tr}_M$ is the unique
non-degenerate Frobenius pairing on $H_n(R, q)$ compatible with
the categorical action, as claimed. $\blacksquare$
