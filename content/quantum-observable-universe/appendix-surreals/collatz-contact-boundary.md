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
specializes to the ordinary $2$-adic valuation.

### The $[2]_q$-adic valuation as contact order

For an element $P \in \mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$
of the Skein module, define the **$[2]_q$-adic valuation**:

$$
  v_{[2]}(P)  :=  \max\bigl\{k \geq 0 :
  [2]_q^k \mid P \text{ in } \mathbb{Z}[q^{\pm 1}]\bigr\}.
$$

This counts how many times $[2]_q$ divides $P$ in the
Laurent polynomial ring — the $q$-analog of the $2$-adic
valuation $v_2(n)$ that counts trailing zeros in the
binary expansion of an integer.

**Geometric meaning.** The value $v_{[2]}(P)$ is the
**contact order** of $P$ with the divisor $D_{[2]}$: the
order to which $P(q)$ vanishes at $q = -1$.  High contact
order means the orbit "grazes" the divisor closely — it
is very divisible by $[2]_q$, meaning many halvings can be
extracted.

At $q = 1$: $[2]_1 = 2$, and $v_{[2]}(n) = v_2(n)$
recovers ordinary $2$-adic valuation.  The number
$n = 24 = 2^3 \cdot 3$ has $v_2(24) = 3$: three halvings
before hitting an odd number.

### Why the orbit needs to touch the divisor

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

### The contact threshold

**Proposition.** The orbit converges if and only if the
average contact order exceeds a critical threshold.

Define the **orbit contact average**: over the first $N$
steps, restrict to the odd steps (there are $N_{\mathrm{odd}}$
of them), and average the $[2]_q$-adic valuation of the
results:

$$
  \langle v_{[2]} \rangle_N(P)
   := 
  \frac{1}{N_{\mathrm{odd}}}
  \sum_{\substack{0 \leq k < N \\
    \mathcal{C}_q^k(P) \text{ is } q\text{-odd}}}
  v_{[2]}\bigl(\mathcal{C}_q^{k+1}(P)\bigr).
$$

The condition is simplest without logarithms.  Since
$1 < v^*(q) < 2$ (proved: $[2]_q < [3]_q < [2]_q^2$),
the orbit converges whenever each tripling is followed
by **at least two halvings on average**:

$$
  \text{orbit converges}
  \quad\Longleftarrow\quad
  \langle v_{[2]} \rangle(P)  \geq  2.
$$

Two halvings multiply by $[2]_q^{-2}$; one tripling
multiplies by $[3]_q / [2]_q$.  The net factor per cycle
(one tripling + two halvings) is:

$$
  \frac{[3]_q}{[2]_q} \cdot \frac{1}{[2]_q^2}
  = 
  \frac{[3]_q}{[2]_q^3}.
$$

This is contractive because $[3]_q < [2]_q^2 < [2]_q^3$.
The contraction ratio is:

$$
  \frac{[3]_q}{[2]_q^3}
  = 
  \frac{[2]_q^2 - q}{[2]_q^3}
  = 
  \frac{1}{[2]_q} - \frac{q}{[2]_q^3},
$$

The orbit shrinks by slightly more than $1/[2]_q$
per cycle.  The **margin** — the gap between two halvings
and the minimum needed — is:

$$
  [2]_q^2 - [3]_q =  q.
$$

The margin is the substrate parameter itself.

**The sharp threshold** (for the record) is
$v^* = \log [3]_q / \log [2]_q$, but since
$v^* < 2$ is proved algebraically, the integer
condition $\langle v \rangle \geq 2$ is sufficient
and avoids transcendental quantities.

**Classical verification.**  At $q = 1$: the average
$2$-adic valuation of $3n+1$ for odd $n$ is **exactly
$2$** (a theorem: the probability $\Pr(v_2(3n+1) = k)
= 2^{-k}$ gives $\mathbb{E}[v_2] = 2$).  Two halvings
per tripling, exactly at the integer threshold.

### The boundary

The **Collatz contact boundary** is the codimension-$1$
locus where the orbit's contact with $D_{[2]}$ is exactly
critical:

$$
  \mathcal{H}_{Col}(q)
  = 
  \bigl\{P \in \mathcal{S}(q) :
  \langle v_{[2]} \rangle(P) = v^*(q)\bigr\}.
$$

Elements **above** the boundary (high contact, many
halvings) converge.  Elements **below** (insufficient
contact, too few halvings) diverge.  The conjecture says
no element is below.

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

### The conjecture as contact condition

The $q$-Collatz conjecture
([conj:q-collatz](#conj:q-collatz)) is equivalent to:

$$
  \boxed{
  \bigl\langle v_{[2]}([3]_q P + 1) \bigr\rangle
   \geq  2
  \quad\text{for all } P \in \mathcal{S}(q)_{>0}.
  }
$$

Two halvings per tripling, on average over every orbit.
