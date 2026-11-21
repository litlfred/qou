*Proof.* The categorical defining equation $D_q\, \exp_q = \exp_q$, joined with the boundary condition $\exp_q(0) = 1$, determines a unique formal power series $\exp_q(x) = \sum_{n\ge 0} a_n x^n$ in $R[\![x]\!]$. The Jackson derivative acts on monomials via $D_q(x^n) = [n]_q\, x^{n-1}$. One substitutes this into the equation:

$$
  D_q\,\sum_n a_n x^n
  \;=\; \sum_{n \ge 0} a_n [n]_q x^{n-1}
  \;=\; \sum_{m \ge 0} a_{m+1} [m+1]_q x^m.
$$

Equating this to $\sum_m a_m x^m$ forces the recursion $a_{m+1} = a_m / [m+1]_q$. With $a_0 = 1$, one obtains:

$$
  a_n \;=\; \prod_{k=1}^{n} \frac{1}{[k]_q} \;=\; \frac{1}{[n]_q!}.
$$

This verifies the claimed coefficient. Convergence on a neighbourhood of $0$ holds because $[n]_q! \to \infty$ faster than geometrically when $|q| < 1$ or $|q| > 1$. When $|q| = 1$, write $q = e^{2\pi i\theta}$; for irrational $\theta$ convergence holds by Diophantine estimates on $\theta$. This series provides the archimedean realisation of the universal grouplike. Its existence over $\mathbb{C}$ forms a theorem about the $\mathbb{C}$-fibre of the moduli of grouplikes over $\mathbb{Z}[q, q^{-1}]$, not a redefinition of $\exp_q$. $\qed$

**Special values.**

| Regime | $[n]_q!$ asymptotic | $\exp_q(x)$ behaviour |
|--------|---------------------|---------------------|
| $q = 1$ | $n!$ (classical) | $\exp_q(x) = e^x$ (ordinary exponential) |
| $0 < q < 1$ | $(1 - q)^{-n}\,n!\,(1 + O(q^n))$ | slow-growth; radius $\infty$ |
| $q > 1$ | $q^{\binom{n}{2}}\,n!_{q^{-1}}$ | faster-than-classical growth |
| $q \to \infty$ | $q^{\binom{n}{2}}$ | entire, type $\log q$ |

**Relation to physical constants.**
Evaluating at the QOU substrate value $q_0$ ([local substrate $q$](#prop:local-substrate-q)) yields $e_{q_0}(x) = \sum x^n / [n]_{q_0}!$. This series generates the moments of the Reeb-flow distribution on $\mathcal{S}$. Because $[n]_{q_0}! \sim q_0^{\binom{n}{2}} n!_{q_0^{-1}}$ grows super-exponentially at $q_0 \approx 1.11$, the series **converges for all $x \in \mathbb{C}$**.
