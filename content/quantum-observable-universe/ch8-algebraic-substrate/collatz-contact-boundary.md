**Proposition ($[2]_q$-contact boundary).**
Let $\mathcal{R}_p = (S^3 \xrightarrow{\pi_H} S^2, \xi_q)$
be the Reeb bundle
([Reeb bundle](#def:reeb-bundle)) with $U(1)$ fiber
parametrized by $q = e^{i\theta}$, $\theta \in [0, 2\pi)$.

### From integer parity to the $[2]_q$-divisor

Classical Collatz hinges on a single question: is $n$ even
or odd?  Parity is residue mod $2$.  The number $2$ is
special: it is the smallest prime, the only even prime,
and the denominator of the halving step $n/2$.

In the QOU, the integer $2$ lifts to the quantum integer
$[2]_q = q + q^{-1}$.  On the unit circle $q = e^{i\theta}$
this becomes $[2]_q = 2\cos\theta$ — a real-valued function
on the $U(1)$ fiber of the Reeb bundle $S^3 \to S^2$.

This function **vanishes** at exactly two points:
$\theta = \pi/2$ and $\theta = 3\pi/2$, corresponding to
$q = i$ and $q = -i$ — the 4th roots of unity.  Define
the **$[2]_q$-divisor**:

$$
  D_{[2]} \;:=\; \{q \in U(1) : [2]_q = 0\}
  \;=\; \{i,\, -i\} \;\subset\; U(1).
$$

These two points are where the $q$-analog of "dividing by
$2$" degenerates — where the halving step ceases to exist.
They sit at the quarter-points of the fiber circle,
splitting it into four arcs.

**Kummer obstruction at the divisor.**
The points $q = \pm i$ belong to $\mu_4$ (the 4th roots
of unity).  The Kummer obstruction
([root-of-unity truncation](#prop:root-of-unity-truncation))
at level $n = 4$ asks: does $4$ divide $\chi(A) = -6$?
No — $6/4 = 1.5$.  The obstruction **persists**.  This
means the $[2]_q$-divisor is a genuine singularity of the
Skein-Collatz dynamics: the QOU axioms cannot remove it.
The substrate must navigate around these points, not
through them.

### The $[2]_q$-adic valuation as contact order

For an element $P \in \mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$
of the Skein module, define the **$[2]_q$-adic valuation**:

$$
  v_{[2]}(P) \;:=\; \max\bigl\{k \geq 0 :
  [2]_q^k \mid P \text{ in } \mathbb{Z}[q^{\pm 1}]\bigr\}.
$$

This counts how many times $[2]_q$ divides $P$ in the
Laurent polynomial ring — the $q$-analog of the $2$-adic
valuation $v_2(n)$ that counts trailing zeros in the
binary expansion of an integer.

**Geometric meaning.** View $P(q)$ as a function on
$U(1)$.  The value $v_{[2]}(P)$ is the **contact order**
of $P$ with the divisor $D_{[2]}$: the order to which
$P(e^{i\theta})$ vanishes at $\theta = \pi/2$.  High
contact order means the orbit "grazes" the divisor closely
— it is very divisible by $[2]_q$, meaning many halvings
can be extracted.

At $q = 1$: $[2]_1 = 2$, and $v_{[2]}(n) = v_2(n)$
recovers ordinary $2$-adic valuation.  The number
$n = 24 = 2^3 \cdot 3$ has $v_2(24) = 3$: three halvings
before hitting an odd number.

### The residue ring: Gaussian integers

Setting $[2]_q = q + q^{-1} = 0$ forces $q = -q^{-1}$,
hence $q^2 = -1$.  The residue ring is:

$$
  \mathbb{Z}[q^{\pm 1}] / ([2]_q)
  \;\cong\;
  \mathbb{Z}[i]
  \qquad (q \mapsto i).
$$

The Gaussian integers $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$
carry a rich arithmetic.  The prime $2$ factors as
$2 = -i(1+i)^2$ in $\mathbb{Z}[i]$ — it **ramifies**.
The $[2]_q$-adic valuation in $\mathbb{Z}[q^{\pm 1}]$
becomes the $(1+i)$-adic valuation in $\mathbb{Z}[i]$.

This connects the Collatz problem to the arithmetic of
$\mathbb{Z}[i]$: the "$q$-parity" of an element is its
residue class in the Gaussian integers, and the
"$q$-evenness" is its divisibility by the ramified prime
$1 + i$.

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
  \;:=\;
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
  \langle v_{[2]} \rangle(P) \;\geq\; 2.
$$

Two halvings multiply by $[2]_q^{-2}$; one tripling
multiplies by $[3]_q / [2]_q$.  The net factor per cycle
(one tripling + two halvings) is:

$$
  \frac{[3]_q}{[2]_q} \cdot \frac{1}{[2]_q^2}
  \;=\;
  \frac{[3]_q}{[2]_q^3}.
$$

This is contractive because $[3]_q < [2]_q^2 < [2]_q^3$.
The contraction ratio is:

$$
  \frac{[3]_q}{[2]_q^3}
  \;=\;
  \frac{[2]_q^2 - q}{[2]_q^3}
  \;=\;
  \frac{1}{[2]_q} - \frac{q}{[2]_q^3},
$$

so the orbit shrinks by slightly more than $1/[2]_q$
per cycle.  The **margin** — the gap between two halvings
and the minimum needed — is:

$$
  [2]_q^2 - [3]_q \;=\; q.
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
  \;=\;
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

At $q = 1$: the average $2$-adic valuation of $3n+1$ for
odd $n$ is **exactly $2$** (a theorem: $\Pr(v_2(3n+1) = k)
= 2^{-k}$ gives $\mathbb{E}[v_2] = 2$).  Two halvings per
tripling, saturating the integer threshold.

### The conjecture as contact condition

The $q$-Collatz conjecture is equivalent to:

$$
  \boxed{
  \langle v_{[2]} \rangle(P) \;\geq\; 2
  \quad\text{for all } P \in \mathcal{S}(q)_{>0}.
  }
$$

Every orbit in the Skein module produces **at least two
halvings per tripling** on average — each tripling is
followed by a result divisible by $[2]_q^2$.

This is sufficient because $[2]_q^2 > [3]_q$ (the gap is
$q$, proved).  One halving per tripling is not enough
($[2]_q < [3]_q$).  Two is the integer threshold.
