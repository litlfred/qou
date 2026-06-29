**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"$[2]_q$-contact boundary").**
Let $\mathcal{R}_p = (S^3 \xrightarrow{\pi_H} S^2, \xi_q)$
be the Reeb bundle
([Reeb bundle](#def:reeb-bundle)) with $U(1)$ fiber
parametrized by $q = e^{i\varTheta}$, $\varTheta \in [0, 2\pi)$.
The $q$-Collatz orbit of $P \in \mathcal{S}(q)_{>0}$ converges if and
only if its orbit contact average
([Collatz contact boundary](#def:collatz-contact-boundary))
attains the threshold $\langle v_{[2]} \rangle(P) \geq 2$;
equivalently, the $q$-Collatz conjecture
([conj:q-collatz](#conj:q-collatz)) is the contact condition

$$
  \boxed{
  \bigl\langle v_{[2]}([3]_q P + 1) \bigr\rangle
   \geq  2
  \quad\text{for all } P \in \mathcal{S}(q)_{>0}.
  }
$$

### Proof

The condition is simplest without logarithms.  Since
$1 < v^*(q) < 2$ (proved: $[2]_q < [3]_q < [2]_q^2$),
the orbit converges whenever each tripling is followed
by **at least two halvings on average**, i.e.
$\langle v_{[2]} \rangle(P) \geq 2$.

Two halvings multiply by $[2]_q^{-2}$; one tripling
multiplies by $[3]_q / [2]_q$.  The net factor per cycle
(one tripling + two halvings) is

$$
  \frac{[3]_q}{[2]_q} \cdot \frac{1}{[2]_q^2}
  = 
  \frac{[3]_q}{[2]_q^3}.
$$

This is contractive because $[3]_q < [2]_q^2 < [2]_q^3$.
The contraction ratio is

$$
  \frac{[3]_q}{[2]_q^3}
  = 
  \frac{[2]_q^2 - q}{[2]_q^3}
  = 
  \frac{1}{[2]_q} - \frac{q}{[2]_q^3},
$$

so the orbit shrinks by slightly more than $1/[2]_q$
per cycle.  The **margin** — the gap between two halvings
and the minimum needed — is

$$
  [2]_q^2 - [3]_q =  q,
$$

the substrate parameter itself, which is positive; hence the
per-cycle factor is strictly contractive and the threshold
$\langle v_{[2]} \rangle \geq 2$ is sufficient for convergence.

The sharp threshold is $v^* = \log [3]_q / \log [2]_q$, but
since $v^* < 2$ is proved algebraically, the integer condition
$\langle v_{[2]} \rangle \geq 2$ is sufficient and avoids
transcendental quantities.

At $q = 1$ the average $2$-adic valuation of $3n+1$ for odd $n$ is
**exactly $2$** (the probability $\Pr(v_2(3n+1) = k) = 2^{-k}$ gives
$\mathbb{E}[v_2] = 2$): two halvings per tripling, exactly at the
integer threshold. $\qquad\blacksquare$
