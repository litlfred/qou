The contact boundary
([prop:collatz-contact-boundary](#prop:collatz-contact-boundary))
establishes that the $q$-Collatz orbit contracts if and only
if each tripling is followed by at least two halvings on
average.  This condition has three equivalent faces — one
categorical, one arithmetic, one number-theoretic — and the
equivalence reveals why the classical Collatz conjecture
sits at a critical threshold.

### (a) The categorical face: Markov trace convergence

In the Iwahori--Hecke algebra $H_n(q)$, the Collatz step composes
two operations: Hecke reduction ($T^2 = (q-q^{-1})T + 1$,
which simplifies crossing words) and Markov destabilization
($\mathrm{tr}_M(xT_n) = z \cdot \mathrm{tr}_M(x)$, which
removes a strand).  The Markov trace
$\mathrm{tr}_M \colon H_n(q) \to \mathbb{Z}[q^{\pm 1}]$
sends braid words to Jones polynomials.

The conjecture in this language: for every $h \in H_n(q)$,
the iterated Markov trace converges to the unknot:

$$
  \mathrm{tr}_M\bigl(\mathcal{C}_q^k(h)\bigr)
  \xrightarrow{k \to \infty} 1.
$$

The identity braid is the unique attractor of the
Hecke--Collatz dynamics.  Every braid, no matter how
tangled, untangles to the unknot under iterated crossing
resolution and destabilization.  The Jones polynomial
$J_L(q)$ of the link $L$ decays to $J_{\bigcirc}(q) = 1$
step by step.

This is the most intrinsic formulation: it lives
entirely inside the Iwahori--Hecke algebra and the Markov trace,
with no reference to integers, parity, or divisibility.
The "convergence to $1$" is convergence to the unknot
polynomial — the categorical unit.

### (b) The arithmetic face: two halvings per tripling

The contact boundary translates (a) into a divisibility
condition on the Skein module
$\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$.

Each odd step produces $[3]_q P + 1$.  The Skein
divisibility identity $[3]_q = q[2]_q + 1$ guarantees
this is divisible by $[2]_q$ — one halving is built in.
The question is whether a **second** halving follows:
is the result divisible by $[2]_q^2$?

The accounting per cycle:
- One tripling: multiply by $[3]_q$ (expansion)
- The built-in halving: divide by $[2]_q$ once
  (part of the accelerated map)
- Additional halvings: divide by $[2]_q$ as many
  more times as $[2]_q$ divides the result

The net contraction per cycle with $v$ total halvings:

$$
  \text{factor} = \frac{[3]_q}{[2]_q^v}.
$$

This is contractive iff $[2]_q^v > [3]_q$.  Since
$[2]_q^1 < [3]_q$ (one halving is not enough) and
$[2]_q^2 > [3]_q$ (two halvings suffice, gap $= q$),
the integer threshold is exactly $v = 2$:

$$
  \bigl\langle v_{[2]}([3]_q P + 1) \bigr\rangle
   \geq  2.
$$

Two halvings per tripling.  Not one, not three — two.
The margin between "one is not enough" and "two is
enough" is $[2]_q^2 - [3]_q = q$, the substrate
parameter.

### (c) The residue face ($q = -1$)

The $[2]_q$-divisor is $q = -1$ (where $[2]_q = q + 1 = 0$).
Evaluating the Collatz output at this divisor: since
$[3]_q|_{q=-1} = (-1)^2 + (-1) + 1 = 1$ and $[2]_q|_{q=-1} = 0$,
the condition $v_{[2]} \geq 2$ becomes $(q+1)^2$-divisibility
of $[3]_q P + 1$ at $q = -1$.

At $q = 1$ (classical limit): $[2]_1 = 2$, and the
$(q+1)$-adic valuation specializes to the $2$-adic
valuation $v_2$ on $\mathbb{Z}$.

### Equivalence and the saturation phenomenon

The three faces are equivalent because they measure the
same quantity from different vantage points:

| Face | What it measures | Where it lives |
|------|-----------------|---------------|
| (a) Categorical | Markov trace decay | $H_n(q)$ |
| (b) Arithmetic | $[2]_q$-adic valuation | $\mathbb{Z}[q^{\pm 1}]$ |
| (c) Residue | $(q+1)$-adic valuation | $\mathbb{Z}$ (at $q=-1$) |

The passage (a) $\to$ (b) is the Markov trace: it sends
Iwahori--Hecke algebra elements to Laurent polynomials, converting
braid untangling to divisibility.  The passage (b) $\to$
(c) is evaluation at the $[2]_q$-divisor ($q = -1$): it
specializes the Laurent polynomial to an integer, converting
$[2]_q$-adic valuation to the ordinary $2$-adic valuation.

**The saturation.**  At $q = 1$ (the classical limit), the
expected $2$-adic valuation of $3n+1$ for uniformly
distributed odd $n$ is:

$$
  \mathbb{E}[v_2(3n+1)]
  =  \sum_{k=1}^{\infty} k \cdot 2^{-k}
  =  2.
$$

Exactly $2$ — the threshold itself.  The classical Collatz
conjecture lives at the knife-edge where the average number
of halvings per tripling exactly equals the minimum needed.
There is no margin.

For $q > 1$: the algebraic gap $[2]_q^2 - [3]_q = q > 1$
provides positive margin.  But $q = 1$ is a torsion point
($\mu_1$), and the QOU axioms fail there.  The classical
hardness of Collatz is the shadow of this torsion
degeneration: the gap collapses to $q = 1$, the margin
vanishes, and the question becomes whether every
**specific** orbit (not the ensemble average) achieves
the threshold.

This is the $q$-deformed diagnosis of why the Collatz
conjecture resists proof: the contraction mechanism works
on average ($\mathbb{E}[v_2] = 2 \geq 2$) but the margin
is zero, so individual orbits might fail.  The conjecture
asserts they never do.
