**Proposition.** *There exist a real $t$ and a complex $a$ with*

$$
0 < t < 1, \qquad \mathrm{Im}\,a > 0,
$$

*both roots of the $5_2$ saddle cubic together with $\bar a$,*

$$
t^{3} - 2t^{2} + 3t - 1 = 0, \qquad
a^{3} - 2a^{2} + 3a - 1 = 0, \qquad
\bar a^{3} - 2\bar a^{2} + 3\bar a - 1 = 0,
$$

*such that the three extended dilogarithms sum to an explicit elementary
expression:*

$$
\mathrm{Li}_2^{\mathrm{ext}}(a) + \mathrm{Li}_2^{\mathrm{ext}}(\bar a) + \mathrm{Li}_2^{\mathrm{ext}}(t)
\;=\; -\frac{\pi^{2}}{6} - \frac{(\log t)^{2}}{2} + \frac{2}{3}\bigl(\arg a - \pi\bigr)^{2} .
$$

We call this the *$5_2$ saddle sum rule*.

## What the statement says

The left-hand side is the dilogarithm potential evaluated at all three
tetrahedron shapes of the $5_2$ complement at once — the geometric shape $a$,
its complex conjugate, and the real shape $t$. Summing over the three
embeddings of the trace field is a Galois trace, and the assertion is that this
trace *closes*: it equals a combination of $\pi^{2}$, a squared logarithm, and
a squared argument, with no dilogarithm left over.

Three features of the statement separate out.

**The right-hand side is real, and manifestly so.** Each of its three terms is
built from real data — $\pi$, $\log t$ for $t \in (0,1)$, and $\arg a$ — even
though two of the three left-hand summands are individually complex. The
imaginary parts of $\mathrm{Li}_2^{\mathrm{ext}}(a)$ and
$\mathrm{Li}_2^{\mathrm{ext}}(\bar a)$ cancel against each other, which is the
conjugate pair doing exactly what the $S_3$ structure of the trace field
predicts.

**The coefficient $2/3$ is forced.** It
descends from the branch relation

$$
2\ell_j - 3m_j = 2\pi i\,\varepsilon_j ,
$$

which the $5_2$ gluing equation $y^{2} = (1-y)^{3}$ imposes on the logarithms
$\ell_j, m_j$ of the shapes. Contracting that relation across the three
embeddings gives
$\sum_j \ell_j m_j = \tfrac{2}{3}\sum_j \ell_j^{2} - \tfrac{2\pi i}{3}\sum_j \varepsilon_j \ell_j$,
and the $2/3$ in the sum rule is the $2$ and the $3$ of the gluing exponents. The sum rule is an
identity, not a fit, and there is no free constant in it.

**The existence quantifier is essential.** The statement is $\exists\,t,a$ with
the listed properties, and it is proved by exhibiting them — the real root
supplies $t$, and the geometric root supplies $a$. It is not the assertion that
*every* triple of cubic roots satisfies the identity.

## The extended dilogarithm

$\mathrm{Li}_2^{\mathrm{ext}}$ is the corpus's integral continuation of the
dilogarithm; it agrees with the principal branch off $[1,\infty)$ and extends
across the cut so that the continuation used in the proof stays single-valued
along the transport path between the three shapes.

The branch bookkeeping is where the $(\arg a - \pi)^{2}$ term comes from: it
records how far the geometric shape's argument has been carried, and it is why
the closed form carries an argument-squared rather than only a
logarithm-squared. The $\varepsilon_j$ above are the same bookkeeping, in the
form the gluing relation sees them.

The proof chain is: the complex five-term identity at $(y_3, y_1)$ and
$(y_3, y_2)$; the anharmonic evaluations; the branch equations from
$y^{2} = (1-y)^{3}$; the root data; and the logarithm evaluations. Every step is
unconditional, and the existence of the three saddle roots follows from the
intermediate value theorem — so the closed form is a statement about the
**actual** roots of $X^{3} - 2X^{2} + 3X - 1$, rather than about a structure
that might be empty.

## Why the shape field is $\mathbb{Q}(\sqrt{-23})$ and not something smaller

The cubic $X^3 - 2X^2 + 3X - 1$ is irreducible over $\mathbb{Q}$ with
discriminant $-23$, so its splitting field contains the imaginary quadratic
subfield $\mathbb{Q}(\sqrt{-23})$. Contrast the figure-eight knot, whose shape
field is the Eisenstein field $\mathbb{Q}(\sqrt{-3})$ and whose tetrahedra are
regular. That extra arithmetic is exactly why the $5_2$ analysis does not reduce
to the $4_1$ argument: the $4_1$ squeeze rests on positivity of
$\langle 4_1\rangle_N$, which $\langle 5_2\rangle_N$ does not have.

## What this does and does not establish

It establishes an exact, parameter-free relation among the three shapes of a
chiral hyperbolic knot — the analogue, for $5_2$, of the closures available for
the amphichiral $4_1$.

**It is not the volume conjecture.** Three statements are distinct and must not
be conflated:

1. the sum rule above, which is proved;
2. $\mathrm{Vol}(S^3 \setminus 5_2) = 3\,D(y_1)$, a statement about a
   hyperbolic manifold, which is not proved here;
3. $\lim_{N} \frac{2\pi}{N}\log\langle 5_2\rangle_N =
   \mathrm{Vol}(S^3 \setminus 5_2)$, the volume conjecture for $5_2$ —
   Ohtsuki's theorem \cite{ohtsuki2016}, untouched.

The sum rule is an identity among dilogarithm values at algebraic points.
Nothing about a metric, a manifold, or an asymptotic follows from it.

It does **not** by itself supply a bar-odd action value, and no such value is
claimed here. The sum rule is symmetric in the conjugate pair: $a$ and $\bar a$
enter identically, so the quantity it pins is bar-**even**. Extracting a bar-odd
datum requires the *difference* across the conjugate pair, which lands on the
$\sqrt{-23}$ line of the trace field and is a separate question from this
identity.
