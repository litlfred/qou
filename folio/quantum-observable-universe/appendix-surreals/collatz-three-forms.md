The contact boundary ([conj:collatz-contact-boundary](#conj:collatz-contact-boundary)) establishes that the $q$-Collatz orbit contracts if and only if each tripling is followed by at least two halvings on average. This condition has equivalent categorical, arithmetic, and residue faces.

In the Iwahori--Hecke algebra $H_n(q)$, the Collatz step composes Hecke reduction ($T^2 = (q-q^{-1})T + 1$) and Markov destabilization ($\mathrm{tr}_M(xT_n) = z \cdot \mathrm{tr}_M(x)$). The Markov trace $\mathrm{tr}_M \colon H_n(q) \to \mathbb{Z}[q^{\pm 1}]$ sends braid words to Jones polynomials.

The categorical conjecture asserts that for every $h \in H_n(q)$, the iterated Markov trace converges to the unknot:

$$
\mathrm{tr}_M\bigl(\mathcal{C}_q^k(h)\bigr) \xrightarrow{k \to \infty} 1.
$$

The identity braid is the unique attractor of the Hecke--Collatz dynamics. Every braid untangles to the unknot under iterated crossing resolution and destabilization.

The contact boundary translates this into a divisibility condition on the Skein module $\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$. Each odd step produces $[3]_q P + 1$. The Skein divisibility identity $[3]_q = q[2]_q + 1$ guarantees one built-in halving. The net contraction per cycle with $v$ total halvings is $[3]_q / [2]_q^v$. This is contractive if and only if $[2]_q^v > [3]_q$. The integer threshold is exactly $v = 2$. Two halvings per tripling are required.

The $[2]_q$-divisor is $q = -1$. Evaluating the Collatz output at this divisor: since $[3]_q|_{q=-1} = 1$ and $[2]_q|_{q=-1} = 0$, the condition $v_{[2]} \geq 2$ becomes $(q+1)^2$-divisibility of $[3]_q P + 1$ at $q = -1$.

At $q = 1$ (the classical limit), the expected $2$-adic valuation of $3n+1$ for uniformly distributed odd $n$ is:

$$
\mathbb{E}[v_2(3n+1)] = \sum_{k=1}^{\infty} k \cdot 2^{-k} = 2.
$$

The classical Collatz conjecture lives at the critical threshold where the average number of halvings per tripling exactly equals the minimum needed. There is no margin.

For $q > 1$, the algebraic gap $[2]_q^2 - [3]_q = q > 1$ provides positive margin. However, $q = 1$ is a torsion point ($\mu_1$) where the QOU axioms fail. The classical hardness of Collatz reflects this torsion degeneration: the gap collapses to $q = 1$, the margin vanishes, and individual orbits might fail. The conjecture asserts they never do.
