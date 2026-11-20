Over $R = \mathbb{Z}[q, q^{-1}]\bigl[\tfrac{1}{[n]_q!} : n \ge 1\bigr]$
the element

$$
  \exp_q \;=\; \sum_{n \ge 0} \frac{x^n}{[n]_q!} \;\in\; \mathcal{H}_q
$$

is grouplike (via the $q$-binomial identity
$\Delta_q(x^n) = \sum_{k} \binom{n}{k}_q x^k \otimes x^{n-k}$) and
flow-invariant (via $D_q(x^n) = [n]_q x^{n-1}$, which shifts the
series by one index while preserving the sum).  Over $\mathbb{C}$, the non-root-of-unity condition
$q \notin \mu_\infty$
([existence of substrate parameter](#thm:substrate-parameter-exists),
Step 3) keeps each $[n]_q! \ne 0$, and the resulting series converges
to the analytic $q$-exponential
(the Taylor series of $\exp_q$, derived in the information-theory chapter).  Over
$\mathbb{F}_p$ the hypothesis fails
(the finite-field obstruction, remarked below);
a truncated existence result holds modulo $x^p = 0$.  Over
$\mathbb{Q}_p$ and $\mathbb{C}_p$ existence follows from the
Witt-vector lift (the $p$-adic $\exp_q$, remarked below).
