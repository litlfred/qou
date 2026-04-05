**Proposition ($[2]_q$-contact boundary).**
Let $\mathcal{R}_p = (S^3 \xrightarrow{\pi_H} S^2, \xi_q)$
be the Reeb bundle
([Reeb bundle](#def:reeb-bundle)) with $U(1)$ fiber
parametrized by $q = e^{i\theta}$, $\theta \in [0, 2\pi)$.

### The $[2]_q$-divisor on the fiber

The quantum integer $[2]_q = q + q^{-1} = 2\cos\theta$
vanishes at $\theta = \pi/2$ and $\theta = 3\pi/2$,
corresponding to $q = \pm i \in \mu_4$ (the 4th roots
of unity).  Define the **$[2]_q$-divisor** on $U(1)$:

$$
  D_{[2]} \;:=\; \{q \in U(1) : [2]_q = 0\}
  \;=\; \{i,\, -i\} \;\subset\; U(1).
$$

Since $4 \nmid \chi(A) = -6$, the Kummer obstruction
**persists** at level $n = 4$
([root-of-unity truncation](#prop:root-of-unity-truncation)).
The divisor $D_{[2]}$ is a genuine obstruction locus on
the fiber — it cannot be removed by the QOU axioms.

### The $[2]_q$-adic valuation

For $P \in \mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$,
define the **$[2]_q$-adic valuation**:

$$
  v_{[2]}(P) \;:=\; \max\bigl\{k \geq 0 :
  [2]_q^k \mid P \text{ in } \mathbb{Z}[q^{\pm 1}]\bigr\}.
$$

Geometrically: $v_{[2]}(P)$ is the **contact order** of
$P(e^{i\theta})$ with the divisor $D_{[2]}$ — the order
of vanishing of $P$ at $q = i$.

At $q = 1$: $[2]_1 = 2$, and $v_{[2]}$ recovers the
ordinary $2$-adic valuation $v_2$ on $\mathbb{Z}$.

### The residue ring and Gaussian integers

The quotient $\mathbb{Z}[q^{\pm 1}] / ([2]_q)$ identifies
$q + q^{-1} = 0$, giving $q^2 = -1$.  Therefore:

$$
  \mathbb{Z}[q^{\pm 1}] / ([2]_q)
  \;\cong\;
  \mathbb{Z}[i]
  \qquad (q \mapsto i).
$$

The $[2]_q$-adic valuation in $\mathbb{Z}[q^{\pm 1}]$
corresponds to the $(1+i)$-adic valuation in $\mathbb{Z}[i]$,
since $2 = -i(1+i)^2$ in $\mathbb{Z}[i]$.

### The contact threshold

**Proposition.** The Skein-Collatz orbit
$\{\mathcal{C}_q^k(P)\}$ converges if and only if the
time-averaged $[2]_q$-adic valuation exceeds the
**critical contact order**:

$$
  v^*(q) \;:=\; \frac{\log [3]_q}{\log [2]_q}.
$$

Precisely: define the **orbit contact average**

$$
  \langle v_{[2]} \rangle_N(P)
  \;:=\;
  \frac{1}{N_{\mathrm{odd}}}
  \sum_{\substack{0 \leq k < N \\
    \mathcal{C}_q^k(P) \text{ is } q\text{-odd}}}
  v_{[2]}\bigl(\mathcal{C}_q^{k+1}(P)\bigr),
$$

where $N_{\mathrm{odd}}$ counts the odd steps.  Then:

$$
  \text{orbit converges}
  \quad\Longleftrightarrow\quad
  \liminf_{N \to \infty}
  \langle v_{[2]} \rangle_N(P)
  \;>\; v^*(q).
$$

*Proof.* Each odd step multiplies by $[3]_q/[2]_q$
(expansion). Each subsequent even step divides by $[2]_q$
(contraction), applied $v_{[2]}$ times. The log-norm
change per odd+even cycle is:

$$
  \Delta \log\|P\|
  \;=\;
  \log\frac{[3]_q}{[2]_q}
  \;-\;
  v_{[2]} \cdot \log [2]_q
  \;=\;
  \log [3]_q - (1 + v_{[2]}) \log [2]_q.
$$

This is negative iff
$v_{[2]} > \log[3]_q / \log[2]_q - 1 = v^*(q) - 1$,
i.e., the total halvings (including the one in the
accelerated step) exceed $v^*(q)$.  $\square$

### The boundary

The **Collatz contact boundary** is the locus:

$$
  \mathcal{H}_{Col}(q)
  \;=\;
  \bigl\{P \in \mathcal{S}(q) :
  \langle v_{[2]} \rangle(P) = v^*(q)\bigr\}.
$$

This is a codimension-$1$ surface in the Skein module,
determined by the contact order of the orbit with the
$[2]_q$-divisor $D_{[2]} = \{i, -i\} \subset U(1)
\subset S^3$.

### Values and the margin

| Quantity | Formula | At $q = 1$ | At $q_0$ |
|----------|---------|-----------|----------|
| Threshold | $v^*(q) = \log[3]_q / \log[2]_q$ | $1.585$ | $1.616$ |
| Empirical average | $\langle v_{[2]} \rangle$ | $2.000$ | — |
| Margin | $\langle v \rangle - v^*$ | $0.415$ | — |

At $q = 1$: the average $2$-adic valuation of $3n+1$
for odd $n$ is **exactly $2$** (a theorem: for
uniformly distributed odd $n$, the probability that
$v_2(3n+1) = k$ is $2^{-k}$, giving expected value
$\sum k \cdot 2^{-k} = 2$).  The threshold $\log_2 3
\approx 1.585$ is exceeded by a margin of $0.415$ —
a $26\%$ excess.

### The $q$-Collatz conjecture as contact condition

The conjecture
([conj:q-collatz](#conj:q-collatz)) is equivalent to:

$$
  \boxed{
  \langle v_{[2]} \rangle(P) > v^*(q)
  \quad\text{for all } P \in \mathcal{S}(q)_{>0}.
  }
$$

Every orbit in the Skein module makes sufficient contact
with the $[2]_q$-divisor on the $U(1)$ fiber of the
Reeb bundle.
