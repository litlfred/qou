The Hausdorff dimension recurrence ([Hausdorff recurrence](#rem:hausdorff-dimension-recurrence)) provides the only universal convergence proof in this paper. The map $q_{n+1} = (q_n^2 - q_n + 1)/q_n$ contracts for all $q > 3/4$, with $q = 1$ as a superattracting fixed point ($F'(1) = 0$). The $q$-Collatz conjecture shares a parallel structure, but with one critical difference.

### The Lyapunov function $\Phi = \log_q |P|$

The natural Lyapunov function for the Skein-Collatz uses
$q$ as the logarithm base:

$$
  \Phi(P)  :=  \log_q |P|.
$$

Why $q$?  Because the contraction gap is $q$ itself:
$[2]_q^2 - [3]_q = q$.  The base-$q$ logarithm converts
this gap into unit decrease: when a cycle has $v = 2$
halvings, $\Phi$ decreases by

$$
  |\Delta\Phi|
  = 
  \log_q \frac{[2]_q^2}{[3]_q}
  = 
  \log_q\!\left(1 + \frac{q}{[3]_q}\right).
$$

At $q_0 = 1.109978595554181\ldots$ (muon pin, 16 dps): $|\Delta\Phi| \approx 2.76$ per
cycle.  An orbit starting at $P$ with $\Phi_0 = \log_q |P|$
reaches the fixed point $\Phi = 0$ (i.e., $P = 1$) after
$\Phi_0 / |\Delta\Phi|$ cycles.

### Entropy cost of convergence

Each Collatz cycle with $v = 2$ halvings consists of $3$
Reeb steps ($1$ odd $+ 2$ even), each consuming
$\eta_q = (2q-1)/q^3$ $q$-bits of operational entropy
([operational entropy](#def:operational-entropy)).  The
total entropy budget to convergence is:

$$
  I_{\mathrm{total}}
  = 
  \frac{\Phi_0}{|\Delta\Phi|} \cdot 3\eta_q
   \approx 
  \Phi_0 \cdot \eta_q
  \quad q\text{-bits}.
$$

At $q_0$, converging from $|P| = 1000$ costs about $65$
$q$-bits — roughly $24$ Collatz cycles, each consuming
$\sim 2.7$ $q$-bits.  The orbit is an information-bounded
computation: it processes a finite, predictable amount
of entropy before terminating.

### The Hausdorff--Collatz comparison

See [Table](#tbl:collatz-hausdorff-comparison-table-data).

### The discrete phase transition at $v = 2$

The Hausdorff recurrence is smooth: the derivative
$F'(q) = 1 - 1/q^2$ varies continuously, reaching $0$
at the fixed point (superattraction).  The orbit
decelerates as it approaches $q = 1$ — each step costs
more entropy but covers less distance.

The Collatz contraction is **discrete**: the valuation
$v \in \{1, 2, 3, \ldots\}$ is an integer, and the
threshold $v^* \in (1, 2)$ falls between two integers.
There is no gradual approach.  The contraction ratio
jumps:

$$
  R(v) = \frac{[3]_q}{[2]_q^v}:
  \qquad
  R(1) \approx \tfrac{3}{2} > 1,
  \qquad
  R(2) \approx \tfrac{3}{4} < 1,
  \qquad
  R(3) \approx \tfrac{3}{8} < 1.
$$

This is a **discrete phase transition**: below $v = 2$
the orbit expands, at $v = 2$ it contracts by $3/4$,
and at $v \geq 3$ it contracts even faster.  There is
no critical slowing-down and no superattraction.

### Implications for the conjecture

The Hausdorff recurrence converges **unconditionally**
because $F'(q) < 1$ for all $q > 3/4$ — the derivative
is negative everywhere in the physical range, so every
orbit enters the basin of the superattracting fixed point.

The Collatz dynamics converge **conditionally**: the
contraction $R(2) < 1$ fires only when $v \geq 2$.  The
conjecture asks whether every orbit produces $v \geq 2$
often enough.  The algebra guarantees that $v = 2$
**suffices** ($[2]^2 > [3]$, gap $= q$); the
no-periodic-cycles theorem
([no cycles](#prop:collatz-no-cycles)) eliminates the
main alternative to convergence; and the classical
average $\mathbb{E}[v_2] = 2$ saturates the threshold.

### Connection via Planck steps

Both the Hausdorff recurrence and the Collatz cycle
advance by Planck-scale steps.  The Hausdorff map uses
$\delta q = \hbar_q$ as the step size (one Reeb phase
advance in $q$-space).  The Collatz cycle consumes
$n_R(q) = q/(q-1)$ Reeb iterations
([operations per Planck](#prop:reeb-operations-per-planck)).

The Hausdorff step and the Collatz Lyapunov step are
commensurate:

$$
  \frac{|\Delta\Phi|}{\hbar_q}
  = 
  \frac{\log_q([2]^2/[3])}{(q-1)/q}
   \approx  2.9
  \quad\text{at } q_0.
$$

Each Collatz cycle (at $v = 2$) covers about $3$ Planck
steps worth of Lyapunov decrease.  The Collatz orbit is
a discrete walk on the same parameter space that the
Hausdorff recurrence traverses smoothly, both using the
substrate parameter as their natural scale.
