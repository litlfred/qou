Let $R$ be a commutative ring of characteristic zero (e.g.
$\mathbb{Q}, \mathbb{R}, \mathbb{C}$) in which all Jackson factorials
$[n]_q! = \prod_{k=1}^{n} \frac{1 - q^k}{1 - q}$ are invertible.  Over
$R$ the abstract grouplike
$\exp_q \in G(\mathcal{H}_q)$ ([$q$-exponential](#def:q-exponential)) is represented
by the convergent power series

$$
  \exp_q(x) \;=\; \sum_{n \ge 0} \frac{x^n}{[n]_q!}.
$$

*Proof.*  The categorical defining equation
$D_q\, \exp_q = \exp_q$ together with the boundary condition $\exp_q(0) = 1$
determines a unique formal power series $\exp_q(x) = \sum_{n\ge 0} a_n x^n$
in $R[\![x]\!]$.  The Jackson derivative acts on monomials by
$D_q(x^n) = [n]_q\, x^{n-1}$, so

$$
  D_q\,\sum_n a_n x^n
  \;=\; \sum_{n \ge 0} a_n [n]_q x^{n-1}
  \;=\; \sum_{m \ge 0} a_{m+1} [m+1]_q x^m.
$$

Setting this equal to $\sum_m a_m x^m$ yields the recursion
$a_{m+1} = a_m / [m+1]_q$.  With $a_0 = 1$:

$$
  a_n \;=\; \prod_{k=1}^{n} \frac{1}{[k]_q} \;=\; \frac{1}{[n]_q!},
$$

which is the claimed coefficient.  Convergence on a neighbourhood
of $0$ follows from $[n]_q! \to \infty$ faster than geometrically
whenever $|q| < 1$ or $|q| > 1$; at $|q| = 1$ irrational, convergence
still holds by Diophantine estimates.  This is the archimedean
realisation of the universal grouplike; its existence over
$\mathbb{C}$ is *not* a redefinition of $\exp_q$ but a theorem about
the $\mathbb{C}$-fibre of the moduli of grouplikes over
$\mathbb{Z}[q, q^{-1}]$.  $\qed$

**Special values.**

| Regime | $[n]_q!$ asymptotic | $\exp_q(x)$ behaviour |
|--------|---------------------|---------------------|
| $q = 1$ | $n!$ (classical) | $\exp_q(x) = e^x$ (ordinary exponential) |
| $0 < q < 1$ | $(1 - q)^{-n}\,n!\,(1 + O(q^n))$ | slow-growth; radius $\infty$ |
| $q > 1$ | $q^{\binom{n}{2}}\,n!_{q^{-1}}$ | faster-than-classical growth |
| $q \to \infty$ | $q^{\binom{n}{2}}$ | entire, type $\log q$ |

**Relation to physical constants.**  Evaluating at the QOU substrate
value $q_0$ ([local substrate $q$](#prop:local-substrate-q)) gives
$e_{q_0}(x) = \sum x^n / [n]_{q_0}!$, which generates the moments of
the Reeb-flow distribution on $\mathcal{S}$.  This series is
**convergent for all $x \in \mathbb{C}$** at $q_0 \approx 1.11$
because $[n]_{q_0}! \sim q_0^{\binom{n}{2}} n!_{q_0^{-1}}$ still grows
super-exponentially.  In particular, the q-heat kernel and its
Gaussian core ([$q$-Gaussian solves the $q$-heat equation](#prop:q-gaussian-solves-q-heat))
are well-defined at the physical value of $q$, without any $|q| \le 1$
restriction.
