Let $H_q$ be the $q$-shuffle Hopf algebra
([$q$-exponential](#def:q-exponential)) over a base ring $R$ in which
the Jackson integers $[n]_q = (1 - q^n)/(1 - q)$ are invertible for
all $n \ge 1$.  Then there exists a grouplike
$\exp_q \in G(H_q)$ satisfying the flow equation

$$
  D_q \exp_q \;=\; \exp_q,
  \qquad
  \epsilon(\exp_q) \;=\; 1.
$$

**Construction.**  Over $R = \mathbb{Z}[q, q^{-1}]\bigl[\tfrac{1}{[n]_q!} : n \ge 1\bigr]$
the element

$$
  \exp_q \;=\; \sum_{n \ge 0} \frac{x^n}{[n]_q!} \;\in\; H_q
$$

is grouplike (verified by the $q$-binomial identity
$\Delta_q(x^n) = \sum_{k} \binom{n}{k}_q x^k \otimes x^{n-k}$) and
flow-invariant (verified by $D_q(x^n) = [n]_q x^{n-1}$, which shifts
the series by one index while preserving the sum).  Over $\mathbb{C}$
this construction recovers the convergent Taylor series
([Taylor series of $\exp_q$](#prop:q-exponential-taylor)).  Over
$\mathbb{F}_p$ the hypothesis fails
([finite-field obstruction](#rem:q-exp-finite-field-obstruction)); a
truncated existence result holds modulo $x^p = 0$.  Over
$\mathbb{Q}_p$ and $\mathbb{C}_p$ existence follows from the
Witt-vector lift ([$p$-adic $\exp_q$](#rem:q-exp-p-adic)).

Uniqueness is ([uniqueness of $\exp_q$](#prop:q-exponential-unique)).
