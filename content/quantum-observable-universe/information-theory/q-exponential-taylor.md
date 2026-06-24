Let $R$ be a commutative ring of characteristic zero (e.g.
$\mathbb{Q}, \mathbb{R}, \mathbb{C}$) in which all Jackson factorials
$[n]_q! = \prod_{k=1}^{n} \frac{1 - q^k}{1 - q}$ are invertible.  Over
$R$ the abstract grouplike
$\exp_q \in G(\mathcal{H}_q)$ ([$q$-exponential](#def:q-exponential)) is represented
by the convergent power series

$$
  \exp_q(x) \;=\; \sum_{n \ge 0} \frac{x^n}{[n]_q!}.
$$

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
