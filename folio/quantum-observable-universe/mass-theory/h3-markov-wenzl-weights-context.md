## Scope — which trace, in which channel

This proposition concerns the **Jones / Temperley–Lieb** normalisation of the
$\mathrm{H}_3(q)$ Markov trace — the trace whose value on a braid closure is the
**Jones polynomial**. Its defining feature is $y_{(1^3)} \equiv 0$: the
Temperley–Lieb quotient annihilates the three-row partition. In the
[trace-convention registry](../../../docs/coordination/trace-convention-registry.md)
this is **convention D**, with Ocneanu parameter $z = q^3/(q^2+1)$.

Both the mass and binding channels use the canonical Convention-D trace uniformly across the framework.

The mass and binding channels use convention D, and the choice is forced: `lem:feynman-eigenbasis-decomposition` puts the row cap $\ell(\lambda) \leq 2$ in the mass channel's decomposition, giving $y_{(1^3)} = 0$, and `markovWeights_eq_jones_of_threeRow_eq_zero` then makes $z = q^3/(q^2+1)$ the unique faithful normalised Markov trace. The full-Hecke Ocneanu trace of convention C, $z = 1/(q^{1/2}+q^{-1/2})$, has $y_{(1^3)}(q) \neq 0$ for $q \neq 1$ and is not used.

By contrast, **the production mass channel uses convention D** — the closed form
of this proposition, entering as `trM_borromean` $\to$ `F_Bor` $\to$
`canonical_mass`.

**The mass channel is convention D.** The two blocks that *define* the mass channel already
fix its fibre: `lem:feynman-eigenbasis-decomposition` carries the row cap
$\ell(\lambda) \leq 2$ inside the index set of
$V^{\otimes n} \cong \bigoplus V_\lambda \otimes S_\lambda$, and
`feynman-markov-identification` carries it inside $\mathrm{tr}_M$ itself, with
closed-form weights that evaluate at $N = 2$, $n = 3$ to exactly the
convention-D vector. So $y_{(1^3)} = 0$ is stated, not assumed, and D follows.
Independently, the Ocneanu parameter determines the fibre dimension through
$z \cdot [N]_q = q^N$, which is injective in $N$: convention D gives $N = 2$
exactly, while convention C gives $N \approx 2.5995$ — **no integer fibre
dimension at all.** Convention C is a legitimate Markov trace on
$\mathrm{H}_3(q)$; it is not the trace of any fibre, so it cannot be the
mass trace.

What remains is a **definitional erratum, not a production defect**: the $z$
stipulated in `rem:markov-axioms-primitive` selects C, while that block and
[Categorical mass as Markov trace](../mass-endomorphism/categorical-mass-markov.md)
both *name* the Jones–Markov trace, which is D. The stipulated value
$1/(q^{1/2}+q^{-1/2})$ is the Temperley–Lieb loop reciprocal $1/\delta$ —
correct for the TL generator $e_i$, but applied there to the Hecke generator
$\sigma_n$; the value that lands on Jones under $\sigma$-stabilisation is
$z = q^3/(q^2+1)$. The registry channel `mass` records this resolution.
Correcting the stipulation is tracked as an open item, and the separate question
of whether the **binding** channel should also move to D is untouched by this
proposition and remains open.

The two traces **coincide at the symmetric point** $q = 1$ (both give
$(\tfrac12,\tfrac14,0)$) and **diverge for $q \neq 1$**: the convention-C
weights at the substrate are $(0.4154,\,0.2809,\,0.0227)$ against convention
D's $(0.5054,\,0.2473,\,0)$.

**What writhe $0$ does and does not buy.** For $\beta \in B_3$ with writhe $0$
and $\pi(\beta) = \mathrm{id}$ both one-dimensional characters equal $1$, so by
the corollary below the trace depends on the weights **only through**
$y_{(2,1)}$: the *split* between $y_{(3)}$ and $y_{(1^3)}$ is invisible, because
normalisation $\sum_\lambda y_\lambda d_\lambda = 1$ already pins their sum.
This is exactly why the chirality asymmetry discussed below is unobservable on
such braids. It does **not** make two conventions agree. Two normalised Markov
traces agree on such a braid precisely when they share $y_{(2,1)}$ or when
$\chi^{(2,1)}(\beta) = 2$, and $\beta_{\mathrm{Bor}}$ satisfies neither
($y^{C}_{(2,1)} \neq 1/[2]_q^{2} = y^{D}_{(2,1)}$):

$$
  \mathrm{tr}^{D}_M(\beta_{\mathrm{Bor}}) - \mathrm{tr}^{C}_M(\beta_{\mathrm{Bor}})
  \;=\;
  \bigl(y^{D}_{(2,1)} - y^{C}_{(2,1)}\bigr)\bigl(-3h^4 - h^6\bigr)
  \;\approx\; 1.9554 \times 10^{-4},
$$

exact as a rational function in $q$, and $195.8$ ppm at the substrate.
Consequently the closed forms below should be read as the **convention-D**
(Jones-polynomial) weights, not as the convention-C $y_\lambda$ used by the
binding pipeline.

## Immediate corollary — the Borromean closed form in one line

For any writhe-$0$ braid $\beta \in B_3$ with $\pi(\beta) = \mathrm{id} \in S_3$:

$$
  \mathrm{tr}_M(\beta)
  \;=\;
  1 + \frac{\chi^{(2,1)}(\beta) - 2}{[2]_q^{2}}.
$$

The entire $h$-dependence of such traces is carried by the single
standard-channel character; the Borromean closed form is this identity
evaluated at $\chi^{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3h^4 - h^6$.

## Non-uniformity of the weights — chirality of the Jones trace

A bar-involution argument would suggest $y_{(3)} = y_{(1^3)}$ (the
transpose pair). It fails: the transpose symmetry $\lambda
\leftrightarrow \lambda^T$ is induced by the sign-twist automorphism
$\sigma_i \mapsto -q\,\sigma_i^{-1}$, and the Jones-normalised Markov
trace is **not invariant** under this automorphism — it is chiral,
weighting the $\sigma$- and $\sigma^{-1}$-eigenchannels asymmetrically.
The extreme expression of this asymmetry is $y_{(1^3)} \equiv 0$
against $y_{(3)}(1) = 1/2$.

At $q = 1$ the trace reduces to the cycle-counting trace
$\mathrm{tr}_M(w) = 2^{\,c(w) - n}$ on $\mathbb{C}[S_3]$ ($c(w)$ =
number of cycles), and Schur orthogonality reproduces
$(\tfrac12, \tfrac14, 0)$ directly.

## Notation note — $y_\lambda$, $\mu_\lambda$, $\chi^\lambda$, $w_\lambda$ are distinct

Four $\lambda$-indexed scalars appear in the Hecke-algebra blocks of
this paper. They are easy to conflate by symbol similarity but encode
independent data:

- $y_\lambda(q)$ — Wenzl/Markov coefficient: appears in
  $\mathrm{tr}_M = \sum_\lambda y_\lambda \cdot \chi^\lambda$, normalised by
  $\sum_\lambda y_\lambda \, d_\lambda = 1$. **This proposition gives the
  Jones/TL values** ($y_{(1^3)} \equiv 0$), i.e. convention D; the full-Hecke
  Ocneanu trace (convention C) used by the binding pipeline has *different*
  $y_\lambda$ at $q \neq 1$ ($y_{(1^3)} \neq 0$) — see the Scope note above.
- $\chi^\lambda(g)$ — character: trace of the $V_\lambda$-representation
  on a specific element $g$ (e.g. a braid).
- $\mu_\lambda(q)$ — $q$-Laplacian eigenvalue on $V_\lambda$
  ([Peter--Weyl decomposition of the $q$-heat kernel (archimedean)](../information-theory/q-heat-kernel-peter-weyl.md)):
  the heat-kernel decay rate, *not* a Markov-trace ingredient.
- $w_\lambda(q) = [n]_q! / H_q(\lambda)^2$ — Plancherel measure
  ([The symmetric point loses resolution, not spectrum](../models-of-qous/symmetric-point-resolution-loss.md)):
  normalised by $\sum_\lambda w_\lambda(1) = 1$ at $q = 1$ only — the $q$-deformed sum $\sum_\lambda w_\lambda(q)$ is **not** $1$ (0.987 at $n = 3$, 1.051 at $n = 8$); at $q = 1$ it is
  non-uniform in a *different* pattern ($\tfrac16, \tfrac23, \tfrac16$
  for $n = 3$) from the Wenzl weights of this proposition
  ($\tfrac12, \tfrac14, 0$).

## Significance for the Borromean derivation

The $1/4$ factor in
[$h^4(\mathrm{tr}_M(\beta_{\mathrm{Bor}})) = (-3) \cdot (1/4) = -3/4$](borromean-h4-categorical-derivation.md)
is $y_{(2,1)}(q = 1) = 1/[2]_q^2|_{q=1}$ from this proposition — and
the identity $y_{(2,1)}(q) = 1/[2]_q^2$ holds **exactly for all $q$**,
not only at the symmetric point. The Borromean $h^4$ separation into
character coefficient $\times$ Markov normalisation is therefore an
exact structural fact, with the $(h^2 + 4)$ denominator of the closed
form being precisely $[2]_q^2 = 1/y_{(2,1)}(q)$.

The $q = 1$ weights $(\tfrac12, \tfrac14, 0)$ are not uniform, since the
Jones trace is not sign-twist invariant. They are verified three ways:
Schur orthogonality on the $q = 1$ cycle-counting trace, the exact
$q$-dependent closed forms above, and canonical reproduction of the
Borromean closed form at 30 digits.
