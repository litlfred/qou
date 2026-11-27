## Scope — which trace, in which channel

This proposition concerns the **Jones / Temperley–Lieb** normalisation of the
$\mathrm{H}_3(q)$ Markov trace — the trace at Ocneanu parameter $z = q^3/(q^2+1)$ whose value on a braid closure is the
**Jones polynomial**. Its defining feature is $y_{(1^3)} \equiv 0$: the
Temperley–Lieb quotient annihilates the three-row partition.

Both the mass and binding channels use this trace uniformly across the framework, and the parameter is forced by the fibre decomposition: the [eigenbasis decomposition for the Feynman amplitude](#lem:feynman-eigenbasis-decomposition) imposes the row cap $\ell(\lambda) \leq 2$ inside the index set of $V^{\otimes n} \cong \bigoplus V_\lambda \otimes S_\lambda$, giving $y_{(1^3)} = 0$, and the [Markov-trace selection theorem](#prop:markov-trace-frobenius-selection) then makes $z = q^3/(q^2+1)$ the unique faithful normalised Markov trace (entering through the Borromean Markov trace and the dressing factor $F_{\mathrm{Bor}}$ into the nucleon mass). Independently, the Ocneanu parameter determines the fibre rank through $z \cdot [N]_q = q^{N-1} q = q^N$, which is injective in $N$ for $q > 1$ and yields the integer rank $N = 2$ at $z = q^3/(q^2+1)$. Note also the generator distinction in [primitive Markov-trace axioms (M1–M4)](#rem:markov-axioms-primitive) and [Categorical mass as Markov trace](../mass-endomorphism/categorical-mass-markov.md): the Temperley–Lieb loop reciprocal $1/\delta = 1/[2]_q$ evaluates the Temperley–Lieb generator $e_i = q - \sigma_i$, whereas under $\sigma$-stabilisation $\mathrm{tr}_M(e_i) = q - z = 1/[2]_q$ gives $z = q^3/(q^2+1)$. At $q = 1$ the weights reduce to $(\tfrac12,\tfrac14,0)$, and at $q_0$ they evaluate to $(0.5054,\,0.2473,\,0)$.

**What writhe $0$ does and does not buy.** For $\beta \in B_3$ with writhe $0$
and $\pi(\beta) = \mathrm{id}$ both one-dimensional characters equal $1$, so by
the corollary below the trace depends on the weights **only through**
$y_{(2,1)}$: the *split* between $y_{(3)}$ and $y_{(1^3)}$ is invisible, because
normalisation $\sum_\lambda y_\lambda d_\lambda = 1$ already pins $y_{(3)} + y_{(1^3)} = 1 - 2y_{(2,1)}$.
This is why the chirality asymmetry between $(3)$ and $(1^3)$ is unobservable on
such braids. It does **not** make $\mathrm{tr}_M(\beta)$ independent of the Markov parameter $z$: two normalised Markov
traces $\mathrm{tr}_M, \mathrm{tr}'_M$ with weights $y, y'$ agree on such a braid precisely when $y_{(2,1)} = y'_{(2,1)}$ or
$\chi^{(2,1)}(\beta) = 2$, and on $\beta_{\mathrm{Bor}}$ ($\chi^{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3h^4 - h^6 \neq 2$ for $h \neq 0$),

$$
  \mathrm{tr}_M(\beta_{\mathrm{Bor}}) - \mathrm{tr}'_M(\beta_{\mathrm{Bor}})
  \;=\;
  \bigl(y_{(2,1)} - y'_{(2,1)}\bigr)\bigl(-3h^4 - h^6\bigr).
$$

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
  Jones/Temperley–Lieb values** at $z = q^3/(q^2+1)$, for which $y_{(1^3)} \equiv 0$.
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
