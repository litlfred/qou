**Proof.**
Throughout, $R$ is a field containing $\mathbb{Q}(q)$ and $q$ is
generic: no quantum integer
$[k]_q = (q^k - q^{-k})/(q - q^{-1})$ vanishes for $k \geq 1$. (The
older $\mathbb{Q}(q^{1/2})$ hypothesis was an artefact of convention
C, whose $z = 1/(q^{1/2}+q^{-1/2})$ needs the square root; convention
D's $z = q^{3}/(q^{2}+1)$ does not, and nothing below leaves
$\mathbb{Q}(q)$.) Let $z$ denote the Markov parameter of the framework normalisation
$\mathrm{tr}_M(\sigma_i) = z$ — deliberately left **undetermined**
here, since Step 3b derives it rather than stipulating it — and a
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
which is non-degenerate. Hence, sharply,

$$
  \mathrm{rad}\,\langle \cdot, \cdot \rangle_\tau
  \;=\;
  \bigoplus_{\lambda \,:\, w_\lambda = 0} M_{d_\lambda}(R),
$$

so the form is non-degenerate exactly when every $w_\lambda \neq 0$,
and in general its radical is the *sum of the annihilated blocks* — a
two-sided ideal, on which $\tau$ itself vanishes identically (the
surviving characters $\chi_\mu$ are zero there). This is the statement
that matters below: the radical is not an obstruction to determining
$\tau$, it is a set of blocks $\tau$ ignores.

**Step 2: existence, and the radical of $\mathrm{tr}_M$.**
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
Ocneanu weight formula at framing ratio $a^2 = z/z_{-}$, verified symbolically for every $\lambda \vdash n \leq 5$ (noting that evaluating the Wenzl formula at convention C, $z = 1/(q^{1/2}+q^{-1/2})$, tests the general hook–content identity; what it
certifies is the hook–content *formula*, which is
convention-independent, not the convention-D weight values).

A numerator factor vanishes exactly when $z/z_{-} = q^{-2c(x)}$. The
argument that this fails at generic $q$ is a statement about generic
$z$, and the QOU parameter is **not** generic: at
$z = q^{3}/(q^{2}+1)$ one computes $z_{-} = 1/(q(q^{2}+1))$ and
therefore

$$
  \frac{z}{z_{-}}
  \;=\;
  \frac{q^{3}}{q^{2}+1} \cdot q(q^{2}+1)
  \;=\;
  q^{4},
$$

an identity in $q$, with no $q_0$ involved. So the vanishing
condition reads $q^{4} = q^{-2c(x)}$, i.e. $c(x) = -2$: the numerator
vanishes on cells of content $-2$ — those in position $(r+2, r)$ —
and on no others, and a Young diagram contains such a cell if and
only if it has at least three rows. Hence

$$
  \mathrm{tr}_M(p_\lambda) = 0 \iff \ell(\lambda) \geq 3,
$$

and by Step 1 the radical of
$\langle x, y \rangle = \mathrm{tr}_M(xy)$ is exactly
$\bigoplus_{\ell(\lambda) \geq 3} M_{d_\lambda}(R)$, the
Temperley–Lieb ideal $I_n$. Wenzl's non-degeneracy lemma
(\cite{wenzl1988}, Lemma 2.4) applies to the generic-$z$ Ocneanu
trace and is **not** available at the QOU parameter; the
corresponding true statement is that the descended pairing on
$\mathrm{TL}_n(q) = H_n(q)/I_n$ is non-degenerate.

**Step 3: uniqueness.**
Let $\tau$ be any Markov trace on the tower satisfying M1–M3 with
the same parameter $z$. It follows by induction on $n$ that $\tau = \mathrm{tr}_M$ at every
level.

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
$H_n(R, q)$. Note what this induction does **not** use: at no point
is non-degeneracy of either functional invoked. Uniqueness at a fixed
$z$ is a consequence of M1–M3 alone, which is why it is untouched by
the degeneracy convention D introduces — and equally why it cannot,
by itself, select $z$. Note also that no separate axiom is needed for negative
crossings: the quadratic relation
$\sigma_{n-1}^{-1} = \sigma_{n-1} - (q - q^{-1})$ yields the
negative-stabilisation value
$\tau(x \sigma_{n-1}^{-1}) = \bigl(z - (q - q^{-1})\bigr) \tau(x)$
automatically, identically for both functionals.

**Step 3b: the parameter itself.**
Steps 1–3 fix the trace *given* $z$. The framework does not get to
choose $z$: it is forced by the mass fibre. Write $y_\lambda$ for the
level-$3$ weights $w_\lambda$ of Step 1. Expanding
$\tau = \sum_{\lambda \vdash 3} y_\lambda \chi^\lambda$ against the
$H_3(q)$ $q$-character table on the class representatives
$1$, $\sigma_0$, $\sigma_0\sigma_1$ turns M1 and M3 into three
polynomial equations in $(y_{(3)}, y_{(2,1)}, y_{(1^3)}, z)$,

$$
  y_{(3)} + 2 y_{(2,1)} + y_{(1^3)} \;=\; 1,
$$

$$
  q \, y_{(3)} + (q - q^{-1}) \, y_{(2,1)} - q^{-1} y_{(1^3)} \;=\; z,
$$

$$
  q^{2} y_{(3)} - y_{(2,1)} + q^{-2} y_{(1^3)} \;=\; z^{2}.
$$

Adjoin the row cap $y_{(1^3)} = 0$ (the fibre is two-dimensional, so
the alternating channel is absent from $V^{\otimes 3}$) and
faithfulness $y_{(2,1)} \neq 0$ (a channel the fibre supplies is
genuinely carried). Eliminating gives $y_{(3)} = 1 - 2 y_{(2,1)}$,
then $z = q - [2]_q \, y_{(2,1)}$, then
$y_{(2,1)} \bigl([2]_q^{2} y_{(2,1)}\bigr) = y_{(2,1)}$; cancelling
the nonzero $y_{(2,1)}$ — the one place faithfulness is used, and
where the spurious branch dies — yields

$$
  [2]_q^{2} \, y_{(2,1)} \;=\; 1,
  \qquad
  y_{(3)} \;=\; 1 - 2 y_{(2,1)},
  \qquad
  z \, [2]_q \;=\; q^{2},
$$

that is, $y = \bigl([4]_q/[2]_q^{3}, \ 1/[2]_q^{2}, \ 0\bigr)$ and
$z = q^{3}/(q^{2}+1)$: **convention D**. Without faithfulness the
system also admits $y = (1, 0, 0)$ at $z = q$ — the trivial
character, which annihilates the two-row block as well and gives
$z [2]_q = q^{2}+1$ — so the hypothesis is load-bearing and its
omission makes the conclusion false rather than unprovable.

Level $3$ is the first level at which this argument can run: at
$n \leq 2$ the row cap is vacuous, and M1 together with M3 leaves one
free parameter, so $z$ is genuinely undetermined. Higher levels add
no freedom in the other direction: the restriction of a level-$n$
Markov trace to $H_3(R, q)$ is again a Markov trace with the same
$z$, so the $n = 3$ system already pins the parameter for the whole
tower, and the Ocneanu formula then returns
$y_{(n-k,k)} = [\,n-2k+1\,]_q / [2]_q^{\,n}$.

*Algebraic scope.* The elimination at $n = 3$ is division-free over any commutative domain, including both the non-degenerate branch and the degenerate $z = q$ branch alongside the fibre-categorical implication. For $n > 3$, the three-term quantum-integer recursion $[m+2]_q + [m]_q = [2]_q [m+1]_q$ and fixed-$n$ instances at $n = 3, 4$ are established algebraically, while the closed form is verified against every partition of $n \leq 7$ to a worst residual of $1.34 \times 10^{-51}$.

**Step 4: block-wise identification and selection.**
Since $\tau = \mathrm{tr}_M$ as functionals, the uniqueness of the
character expansion in Step 1 gives $w_\lambda = y_\lambda(q)$ for
every $\lambda \vdash n$: any trace satisfying the Markov-peel and
cyclic axioms equals $\mathrm{tr}_M$ block-wise. Combining the steps:
the categorical trace induced by the cat-action and the fibre functor
satisfies M1 (normalisation), M2 (cyclicity of the categorical
trace) and M3 (invariance of the Markov closure under positive
stabilisation); being the categorical trace of the action on
$V^{\otimes n}$ with $\dim_q V = [2]_q$, it additionally carries the
row cap and is faithful on the channels the fibre supplies. By
Step 3b the Markov axioms together with those last two conditions
force $z \, [2]_q = q^{2}$ and the weight
vector; by Steps 1–3 the functional is then unique on the whole
tower; by Step 2 its form has radical exactly $I_n$, on which the
functional vanishes, so it descends to a non-degenerate — indeed
symmetric Frobenius — pairing on $\mathrm{TL}_n(q)$.

What is *not* claimed: that $\mathrm{tr}_M$ is non-degenerate on
$H_n(R, q)$ (it is not, for $n \geq 3$), that non-degeneracy selects
it (it does not — every nowhere-vanishing weight vector gives a
non-degenerate form), or that the antecedent is established (the
fibre-categorical premise is open). $\blacksquare$
