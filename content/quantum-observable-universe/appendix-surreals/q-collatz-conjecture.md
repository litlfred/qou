**Conjecture ($q$-Collatz).**
Let $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$ be a substrate parameter ([torsion avoidance](#rem:substrate-gm-torsion)) and let $\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$ be the Skein module of the Reeb bundle $\mathcal{R}_p = (S^3 \to S^2, \xi_q)$ ([Reeb bundle](#def:reeb-bundle)).

**Convention.** We use the combinatorial $q$-integer $[n]_q = (q^n - 1)/(q - 1)$. This gives $[2]_q = q + 1$ and $[3]_q = q^2 + q + 1$. The paper's Iwahori--Hecke algebra convention $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ differs by a factor of $q^{(n-1)/2}$. The combinatorial convention ensures the Skein divisibility identity $[3]_q = q[2]_q + 1$ and the contraction gap $[2]_q^2 - [3]_q = q$.

### $q$-parity in the Skein module

An element $P \in \mathbb{Z}[q^{\pm 1}]$ is **$q$-even** if $[2]_q \mid P$ and **$q$-odd** if $[2]_q \mid (P + 1)$. At $q = 1$, we recover integer parity.

### The Skein-Collatz map

Define $\mathcal{C}_q \colon \mathbb{Z}[q^{\pm 1}] \to \mathbb{Z}[q^{\pm 1}]$ by:

$$
  \mathcal{C}_q(P)
  = 
  \begin{cases}
    P / [2]_q
      & P \text{ is } q\text{-even},\\[4pt]
    \bigl([3]_q P + 1\bigr) / [2]_q
      & P \text{ is } q\text{-odd}.
  \end{cases}
$$

The odd branch is well-defined by the **Skein divisibility identity**:

$$
  [3]_q =  q[2]_q + 1.
$$

Since $P$ is $q$-odd, $P + 1 = [2]_q Q$. Then $[3]_q P + 1 = q[2]_q P + (P + 1)$, and the numerator is divisible by $[2]_q$:

$$
  \mathcal{C}_q(P) = qP + Q = [3]_qQ - q.
$$

**Classical limit.** At $q = 1$, we recover $\mathcal{C}_1(n) = n/2$ (even) or $(3n+1)/2$ (odd). This is the Syracuse map.

### Skein-theoretic interpretation

Each application of $\mathcal{C}_q$ corresponds to a **crossing resolution** in the Skein module ([skein generation](#prop:skein-generation)):

- **Even branch** ($P/[2]_q$): Markov destabilization removes one strand from the braid closure. This is the $q$-analog of halving.
- **Odd branch** ($([3]_q P + 1)/[2]_q$): We apply the Hecke relation $T^2 = (q - q^{-1})T + 1$ to reduce a quadratic crossing word to linear, then destabilize.

The Skein relation $qL_+ - q^{-1}L_- = (q - q^{-1})L_0$ ensures each resolution step is a **convex combination**:

$$
  J(L_+) = q^{-2}J(L_-) + (1 - q^{-2})J(L_0).
$$

For $q > 1$ both coefficients are positive and sum to $1$. The crossing resolution is non-expansive on the Jones polynomial.

### The contraction estimate

The algebraic identity $[2]_q^2 - [3]_q = q$ yields contraction. Over one Collatz cycle:
- The odd step maps $P \mapsto [3]_qQ - q$, where $Q = (P+1)/[2]_q$. The ratio $|P|/|Q| \approx [2]_q$.
- The subsequent even steps divide by $[2]_q$.

If each tripling is followed by at least **two halvings** on average, the orbit contracts. Two halvings multiply by $1/[2]_q^2$. One tripling multiplies by $[3]_q/[2]_q$. The net factor per cycle is $[3]_q / [2]_q^3 < 1$. The margin is:

$$
  [2]_q^2 - [3]_q =  q.
$$

Two halvings beat one tripling by a factor $[2]_q^2 / [3]_q = 1 + q/[3]_q \approx 4/3$.

### The conjecture

$$
  \boxed{
  \text{For all } q > 1 \text{ and all } P \in \mathbb{Z}[q^{\pm 1}]_{>0}, \text{ the orbit } \{\mathcal{C}_q^k(P)\}_{k \geq 0} \text{ reaches } 1.
  }
$$

### Connection to the obstruction framework

The Collatz obstruction $\kappa_C := \mathrm{res}_{C_q}(\kappa_0) \in H^2(\mathcal{S}_{C_q}, \mathbb{G}_m)$ ([classical limit obstruction](#def:classical-limit-obstruction), [QOU obstruction reduction](#thm:qou-obstruction-reduction)) measures the failure of Skein-Collatz orbits to converge.

The conjecture $\kappa_C = 0$ is equivalent to the statement that every element of the Skein module $\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$ reduces to the unknot polynomial $1$ under iterated crossing resolution via $\mathcal{C}_q$.
