The contact boundary ([prop:collatz-contact-boundary](#prop:collatz-contact-boundary)) establishes that the $q$-Collatz orbit contracts if and only if each tripling is followed by at least two halvings on average. This condition has three equivalent faces: categorical, arithmetic, and number-theoretic. The equivalence reveals why the classical Collatz conjecture sits at a critical threshold.

### (a) The categorical face: Markov trace convergence

In the Iwahori--Hecke algebra $H_n(q)$, the Collatz step composes two operations: Hecke reduction ($T^2 = (q-q^{-1})T + 1$) and Markov destabilization ($\mathrm{tr}_M(xT_n) = z \cdot \mathrm{tr}_M(x)$). The Markov trace $\mathrm{tr}_M \colon H_n(q) \to \mathbb{Z}[q^{\pm 1}]$ sends braid words to Jones polynomials.

The conjecture asserts that for every $h \in H_n(q)$, the iterated Markov trace converges to the unknot:

$$
  \mathrm{tr}_M\bigl(\mathcal{C}_q^k(h)\bigr)
  \xrightarrow{k \to \infty} 1.
$$

The identity braid is the unique attractor of the Hecke--Collatz dynamics. Every braid untangles to the unknot under iterated crossing resolution and destabilization. The Jones polynomial $J_L(q)$ decays to $J_{\bigcirc}(q) = 1$.

This intrinsic formulation lives entirely inside the Iwahori--Hecke algebra and the Markov trace. It requires no reference to integers, parity, or divisibility. Convergence to $1$ is convergence to the categorical unit.

### (b) The arithmetic face: two halvings per tripling

The contact boundary translates (a) into a divisibility condition on the Skein module $\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$.

Each odd step produces $[3]_q P + 1$. The Skein divisibility identity $[3]_q = q[2]_q + 1$ guarantees divisibility by $[2]_q$. One halving is built in. The question is whether a second halving follows. Is the result divisible by $[2]_q^2$?

The accounting per cycle:
- Tripling: multiply by $[3]_q$
- Built-in halving: divide by $[2]_q$ once
- Additional halvings: divide by $[2]_q$ as many more times as $[2]_q$ divides the result

The net contraction per cycle with $v$ total halvings:

$$
  \text{factor} = \frac{[3]_q}{[2]_q^v}.
$$

This contracts if and only if $[2]_q^v > [3]_q$. Since $[2]_q^1 < [3]_q$ and $[2]_q^2 > [3]_q$, the integer threshold is exactly $v = 2$:

$$
  \bigl\langle v_{[2]}([3]_q P + 1) \bigr\rangle
   \geq  2.
$$

Two halvings per tripling. The margin is $[2]_q^2 - [3]_q = q$.

### (c) The residue face ($q = -1$)

The $[2]_q$-divisor is $q = -1$. Evaluating the Collatz output at this divisor yields $[3]_q|_{q=-1} = 1$ and $[2]_q|_{q=-1} = 0$. The condition $v_{[2]} \geq 2$ becomes $(q+1)^2$-divisibility of $[3]_q P + 1$ at $q = -1$.

At $q = 1$, $[2]_1 = 2$. The $(q+1)$-adic valuation specializes to the $2$-adic valuation $v_2$ on $\mathbb{Z}$.

### Equivalence and the saturation phenomenon

The three faces measure the same quantity from different vantage points:

| Face | What it measures | Where it lives |
|------|-----------------|---------------|
| (a) Categorical | Markov trace decay | $H_n(q)$ |
| (b) Arithmetic | $[2]_q$-adic valuation | $\mathbb{Z}[q^{\pm 1}]$ |
| (c) Residue | $(q+1)$-adic valuation | $\mathbb{Z}$ (at $q=-1$) |

The Markov trace maps (a) to (b), converting braid untangling to divisibility. Evaluation at the $[2]_q$-divisor maps (b) to (c), converting $[2]_q$-adic valuation to $2$-adic valuation.

**The saturation.** At $q = 1$, the expected $2$-adic valuation of $3n+1$ for uniformly distributed odd $n$ is:

$$
  \mathbb{E}[v_2(3n+1)]
  =  \sum_{k=1}^{\infty} k \cdot 2^{-k}
  =  2.
$$

The classical Collatz conjecture lives at the knife-edge where the average number of halvings per tripling exactly equals the minimum needed. There is no margin.

For $q > 1$, the algebraic gap $[2]_q^2 - [3]_q = q > 1$ provides a positive margin. However, $q = 1$ is a torsion point ($\mu_1$), and the QOU axioms fail there. The classical hardness of Collatz is the shadow of this torsion degeneration: the gap collapses to $q = 1$, the margin vanishes, and the question becomes whether every specific orbit achieves the threshold.

The contraction mechanism works on average ($\mathbb{E}[v_2] = 2 \geq 2$) but the margin is zero. Individual orbits might fail. The conjecture asserts they never do.
