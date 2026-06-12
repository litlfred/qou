**Proposition (Closed-form Wenzl/Markov weights on $\mathrm{H}_3(q)$).**
*Let $y_\lambda(q)$ denote the Wenzl coefficient of $V_\lambda$ in the
Frobenius expansion $\mathrm{tr}_M = \sum_{\lambda \vdash 3} y_\lambda \,
\chi^\lambda$ of the Markov trace on $\mathrm{H}_3(q)$, in the
$V_{\mathrm{Jones}} / [2]_q^{\,c-1}$ closure normalisation of
[`prop:borromean-markov-trace-closed-form`](borromean-markov-trace-closed-form.md).
Then for all $q$:*

$$
  \boxed{\;\;
  y_{(3)}(q) \;=\; \frac{[4]_q}{[2]_q^{3}},
  \qquad
  y_{(2,1)}(q) \;=\; \frac{1}{[2]_q^{2}},
  \qquad
  y_{(1^3)}(q) \;=\; 0.
  \;\;}
$$

*At the symmetric point $q = 1$ these evaluate to*

$$
  \bigl(y_{(3)},\, y_{(2,1)},\, y_{(1^3)}\bigr)\big|_{q=1}
  \;=\;
  \bigl(\tfrac{1}{2},\, \tfrac{1}{4},\, 0\bigr)
  \qquad \text{— \emph{not} uniform.}
$$

**Proof.** Three steps, each forced.

**Step 1 — $y_{(1^3)} \equiv 0$ (Temperley–Lieb quotient).** The Jones
polynomial factors through the Temperley–Lieb algebra
$\mathrm{TL}_n(q)$ (Kauffman bracket), which is the quotient of
$\mathrm{H}_n(q)$ annihilating every $V_\lambda$ with more than two
rows. For $n = 3$ the only such partition is $(1^3)$, so the
Jones-normalised Markov trace assigns it weight zero **identically in
$q$**. Equivalently, the vanishing is the algebraic identity

$$
  [2]_q^{3} - 2\,[2]_q - [4]_q \;=\; 0,
$$

verified by direct expansion: with $[2]_q = q + q^{-1}$,
$[2]_q^3 = q^3 + 3q + 3q^{-1} + q^{-3}$, so
$[2]_q^3 - 2[2]_q = q^3 + q + q^{-1} + q^{-3} = [4]_q$.

**Step 2 — Markov normalisation.** $\mathrm{tr}_M(\mathbf{1}_3) = 1$
(the identity braid closes to the 3-component unlink, whose Jones
value is exactly the normalising $[2]_q^2$). With
$d_{(3)}, d_{(2,1)}, d_{(1^3)} = 1, 2, 1$ and Step 1:

$$
  y_{(3)}(q) + 2\, y_{(2,1)}(q) \;=\; 1.
$$

**Step 3 — uniqueness from the Borromean closed form.** For
$\beta_{\mathrm{Bor}}$ (writhe $0$, image $\mathrm{id} \in S_3$),
$\chi^{(3)}(\beta_{\mathrm{Bor}}) = 1$ exactly and
$\chi^{(2,1)}(\beta_{\mathrm{Bor}}) = 2 - 3h^4 - h^6$ with
$h = q - q^{-1}$. Substituting Steps 1–2:

$$
  \mathrm{tr}_M(\beta_{\mathrm{Bor}})
  \;=\;
  1 + y_{(2,1)}(q)\,\bigl(\chi^{(2,1)}(\beta_{\mathrm{Bor}}) - 2\bigr)
  \;=\;
  1 - y_{(2,1)}(q)\,\bigl(3h^4 + h^6\bigr).
$$

Comparing with the closed form
$\mathrm{tr}_M(\beta_{\mathrm{Bor}}) = (4 + h^2 - 3h^4 - h^6)/(h^2+4)
= 1 - (3h^4 + h^6)/(h^2 + 4)$, and noting $3h^4 + h^6 \neq 0$ for
$h \neq 0$:

$$
  y_{(2,1)}(q) \;=\; \frac{1}{h^2 + 4} \;=\; \frac{1}{[2]_q^{2}}
  \qquad\text{(uniquely, for all } q \neq 1\text{; at } q = 1 \text{ by continuity)}.
$$

Then Step 2 gives $y_{(3)} = 1 - 2/[2]_q^2 = ([2]_q^2 - 2)/[2]_q^2
= [4]_q / [2]_q^3$ using Step 1's identity. $\square$

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

## Why the weights are not uniform — chirality of the Jones trace

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

- $y_\lambda(q)$ — Wenzl/Markov coefficient (this proposition):
  appears in $\mathrm{tr}_M = \sum_\lambda y_\lambda \cdot \chi^\lambda$,
  normalised by $\sum_\lambda y_\lambda \, d_\lambda = 1$.
- $\chi^\lambda(g)$ — character: trace of the $V_\lambda$-representation
  on a specific element $g$ (e.g. a braid).
- $\mu_\lambda(q)$ — $q$-Laplacian eigenvalue on $V_\lambda$
  ([`prop:q-heat-kernel-peter-weyl`](../information-theory/q-heat-kernel-peter-weyl.md)):
  the heat-kernel decay rate, *not* a Markov-trace ingredient.
- $w_\lambda(q) = [n]_q! / H_q(\lambda)^2$ — Plancherel measure
  ([`rem:symmetric-point-resolution-loss`](../models-of-qous/symmetric-point-resolution-loss.md)):
  normalised by $\sum_\lambda w_\lambda = 1$; at $q = 1$ it is
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

> **Correction note.** An earlier draft of this proposition claimed the
> $q = 1$ weights were *uniform* ($y_\lambda(1) = 1/4$ for all
> $\lambda \vdash 3$) via a bar-involution argument. That claim was
> wrong — caught in review — for the reason documented in the chirality
> section above: the Jones trace is not sign-twist invariant. The
> corrected weights $(\tfrac12, \tfrac14, 0)$ are verified three ways:
> Schur orthogonality on the $q = 1$ cycle-counting trace, the exact
> $q$-dependent closed forms above, and numerical reproduction of the
> Borromean closed form at 30 digits.
