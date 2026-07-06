### From integer parity to the $[2]_q$-divisor

Classical Collatz hinges on a single question: is $n$ even
or odd?  Parity is residue mod $2$.  The number $2$ is
special: it is the smallest prime, the only even prime,
and the denominator of the halving step $n/2$.

In the QOU, the integer $2$ lifts to the quantum integer
$[2]_q = q + 1$ (combinatorial convention;
see [q-Collatz conjecture](#conj:q-collatz)).
The $[2]_q$-divisor is the locus where $[2]_q = 0$,
i.e. $q = -1$:

$$
  D_{[2]}  :=  \{q : [2]_q = 0\}
  =  \{-1\}.
$$

This is where the $q$-analog of "dividing by $2$"
degenerates — where the halving step ceases to exist.

**Kummer obstruction at the divisor.**
The point $q = -1$ belongs to $\mu_2$ (the 2nd roots
of unity).  The Kummer obstruction
([root-of-unity truncation](#prop:root-of-unity-truncation))
at level $n = 2$ asks: does $2$ divide $\chi(A) = -6$?
Yes — $6/2 = 3$.  The obstruction **vanishes**.  This
means the $[2]_q$-divisor is removable: the QOU axioms
can resolve the singularity.  At $q = -1$, the residue ring
is $\mathbb{Z}[q^{\pm 1}]/(q+1) \cong \mathbb{Z}$
(setting $q = -1$), and the $[2]_q$-adic valuation
([$[2]_q$-adic valuation](#def:two-q-adic-valuation))
specializes to the ordinary $2$-adic valuation.

### Necessity of orbit–divisor contact

The Skein-Collatz map
([conj:q-collatz](#conj:q-collatz)) has two branches:

- **Even branch** ($P/[2]_q$): each application
  **decreases** $\log|P|$ by $\log [2]_q$.  This is a
  halving — the orbit moves toward $1$.

- **Odd branch** ($([3]_q P + 1)/[2]_q$): the
  multiplication by $[3]_q$ **increases** $\log|P|$ by
  $\log([3]_q/[2]_q)$, despite the single division by
  $[2]_q$ built into the accelerated step.

The competition: each tripling (odd step) inflates the
orbit, and each subsequent halving deflates it.  The
orbit converges only if the halvings win on average.

After each odd step, the result $\mathcal{C}_q(P)$ is
$q$-even — the Skein divisibility identity $[3]_q = q[2]_q + 1$
guarantees this.  But **how even** is it?  The number
$v_{[2]}(\mathcal{C}_q(P))$ — the contact order with
$D_{[2]}$ — determines how many consecutive halvings
follow before the next odd step.

### The margin

| Quantity | Formula | At $q = 1$ | At $q_0$ |
|----------|---------|-----------|----------|
| Two halvings beat one tripling? | $[2]_q^2 > [3]_q$ | $4 > 3$ | $4.45 > 3.34$ |
| Margin | $[2]_q^2 - [3]_q = q$ | $1$ | $1.110$ |
| Relative margin | $q / [3]_q$ | $1/3$ | $0.332$ |
| Empirical $\langle v \rangle$ at $q=1$ | — | $2$ (exact) | — |

Two halvings overpower one tripling by a factor
$[2]_q^2 / [3]_q = 1 + q/[3]_q \approx 4/3$.  The margin
$q/[3]_q \approx 1/3$ is the substrate parameter divided
by the tripling factor — clean and algebraic.
