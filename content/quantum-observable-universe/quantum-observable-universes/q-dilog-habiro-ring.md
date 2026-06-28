**Base-ring independence.** Like $\exp_q$ and $\log_q$,
$\mathrm{Li}_2^q$ is defined abstractly as an iterated primitive of
$\mathcal{H}_q$ — its existence and uniqueness are Hopf-algebraic, not
analytic. Over $\mathbb{F}_p$ the pentagon identity is a polynomial
equation over the base ring, solvable as long as the denominators
$1 - xy, [n]_q$ do not vanish; outside those loci $\mathrm{Li}_2^q$
descends to a finite-field element.

**Native algebraic home: the Habiro ring.**
*The series $\mathrm{Li}_2^q(x) = \sum_{n \geq 1} x^n / (n\,[n]_q)$
has $q$-Pochhammer denominators (each $[n]_q$ is a cyclotomic
factor), so its formal-series coefficients lie in
$\mathbb{Z}[q^{\pm 1}, (q-q^{-1})^{-1}]$ and the partial sums are
coherent modulo $((q;q)_m)$ as $m \to \infty$. Thus
$\mathrm{Li}_2^q(x)$ is accordingly an element of the Habiro ring
$\widehat{\mathbb{Z}[q]}[\![x]\!]$
([Habiro ring](#def:habiro-ring)) of formal power series with
Habiro-completed coefficients. This is the algebraic home that
makes "evaluation at any root of unity" well-defined without
invoking $\mathbb{C}$: the projection $\widehat{\mathbb{Z}[q]} \to
\mathbb{Z}[q]/\Phi_N(q)$ at the $N$-th cyclotomic ideal sends
$\mathrm{Li}_2^q$ to its level-$N$ truncated dilogarithm,
recovering Kontsevich–Zagier mod-$p$ and the colored-Jones
asymptotic data without any analytic continuation.*
