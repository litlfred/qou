Classical Collatz hinges on parity. Parity is residue modulo $2$. The integer $2$ is the smallest prime, the only even prime, and the denominator of the halving step $n/2$.

In the QOU, the integer $2$ lifts to the quantum integer $[2]_q = q + 1$. The $[2]_q$-divisor is the locus where $[2]_q = 0$:

$$
D_{[2]} := \{q : [2]_q = 0\} = \{-1\}.
$$

This locus degenerates the halving step.

The point $q = -1$ belongs to $\mu_2$. The Kummer obstruction ([root-of-unity truncation](#prop:root-of-unity-truncation)) at level $n = 2$ asks whether $2$ divides $\chi(A) = -6$. It does. The obstruction vanishes. At $q = -1$, the residue ring is $\mathbb{Z}[q^{\pm 1}]/(q+1) \cong \mathbb{Z}$, and the $[2]_q$-adic valuation specializes to the ordinary $2$-adic valuation.

The Skein-Collatz map has two branches:

- **Even branch** ($P/[2]_q$): Each application decreases $\log|P|$ by $\log [2]_q$. The orbit moves toward $1$.
- **Odd branch** ($([3]_q P + 1)/[2]_q$): Multiplication by $[3]_q$ increases $\log|P|$ by $\log([3]_q/[2]_q)$, despite the single division by $[2]_q$.

Tripling inflates the orbit. Halving deflates it. Convergence requires halvings to dominate on average.

After each odd step, the result $\mathcal{C}_q(P)$ is $q$-even. The integer $v_{[2]}(\mathcal{C}_q(P))$ measures contact order with $D_{[2]}$. It dictates how many consecutive halvings follow before the next odd step.

| Quantity | Formula | At $q = 1$ | At $q_0$ |
|----------|---------|-----------|----------|
| Two halvings beat one tripling? | $[2]_q^2 > [3]_q$ | $4 > 3$ | $4.45 > 3.34$ |
| Margin | $[2]_q^2 - [3]_q = q$ | $1$ | $1.110$ |
| Relative margin | $q / [3]_q$ | $1/3$ | $0.332$ |
| Empirical $\langle v \rangle$ at $q=1$ | — | $2$ (exact) | — |

Two halvings overpower one tripling by a factor $[2]_q^2 / [3]_q = 1 + q/[3]_q \approx 4/3$. The margin $q/[3]_q \approx 1/3$ isolates the aether parameter.
