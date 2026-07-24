**Conjecture ($q$-Collatz, within a QOU).**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q \in \mathbb{G}_m^{\mathrm{nt}}(k)$ ([torsion avoidance](#rem:substrate-gm-torsion)), and let $\mathcal{S}(q) \cong \mathbb{Z}[q^{± 1}]$ be the Skein module of its Reeb bundle $\mathcal{R}_p = (S^3 \to S^2, \xi_q)$ ([Reeb bundle](#def:reeb-bundle)). This is a statement about the $q$-deformed Skein dynamics *of the QOU* — not a claim about the classical Collatz problem, which it recovers only in the archimedean limit $q \to 1$, and only when the substrate admits a well-defined standard part.

We use the combinatorial $q$-integer $[n]_q = (q^n - 1)/(q - 1)$, giving $[2]_q = q + 1$ and $[3]_q = q^2 + q + 1$. The Iwahori--Hecke algebra convention $[n]_q = (q^n - q^{-n})/(q - q^{-1})$ differs by a factor of $q^{(n-1)/2}$. The combinatorial convention ensures the Skein divisibility identity $[3]_q = q[2]_q + 1$ and the contraction gap $[2]_q^2 - [3]_q = q$.

An element $P \in \mathbb{Z}[q^{± 1}]$ is $q$-even if $[2]_q \mid P$ and $q$-odd if $[2]_q \mid (P + 1)$. At $q = 1$, we recover integer parity ($[2]_1 = 2$).

Unlike the integers — where every element is even or odd — a Laurent polynomial need be neither: $P$ is $q$-even iff $P(-1) = 0$ and $q$-odd iff $P(-1) = -1$ (evaluating modulo $[2]_q$, i.e. at $q = -1$), so $\mathcal{C}_q$ is a **partial** map, undefined when $P(-1) \notin \{0, -1\}$. Moreover this domain is not forward-invariant: almost every positive element leaves it within a few steps. Accordingly the positive cone below is the **domain-stable** cone — the elements whose entire forward orbit remains $q$-even-or-$q$-odd — a feature with no classical analog.

Define the Skein-Collatz map $\mathcal{C}_q \colon \mathbb{Z}[q^{± 1}] \to \mathbb{Z}[q^{± 1}]$ by:

$$
\mathcal{C}_q(P) =
\begin{cases}
  P / [2]_q & P \text{ is } q\text{-even},\\[4pt]
  \bigl([3]_q P + 1\bigr) / [2]_q & P \text{ is } q\text{-odd}.
\end{cases}
$$

The odd branch is well-defined by the Skein divisibility identity:

$$
[3]_q = q[2]_q + 1.
$$

Since $P$ is $q$-odd ($[2]_q \mid P + 1$), the numerator is divisible by $[2]_q$. Writing $P + 1 = [2]_q Q$:

$$
\mathcal{C}_q(P) = qP + Q = [3]_q Q - q.
$$

At $q = 1$, $\mathcal{C}_1(n) = n/2$ (even) or $(3n+1)/2$ (odd), recovering the Syracuse map.

Each application of $\mathcal{C}_q$ corresponds to a crossing resolution in the Skein module ([skein generation](#prop:skein-generation)):

- **Even branch** ($P/[2]_q$): Markov destabilization removes one strand from the braid closure, dividing the Jones polynomial by the Markov parameter. This is the $q$-analog of "halving."
- **Odd branch** ($([3]_q P + 1)/[2]_q$): The Hecke relation $T^2 = (q - q^{-1})T + 1$ reduces a quadratic crossing word to linear, followed by destabilization.

The Skein relation $qL_+ - q^{-1}L_- = (q - q^{-1})L_0$ ensures each resolution step is a convex combination:

$$
J(L_+) = q^{-2}J(L_-) + (1 - q^{-2})J(L_0).
$$

For $q > 1$, both coefficients are positive and sum to $1$. The crossing resolution is non-expansive on the Jones polynomial.

The algebraic identity $[2]_q^2 - [3]_q = q$ controls the contraction. Over one Collatz cycle (one odd step followed by enough even steps to exhaust $[2]_q$-divisibility):

- The odd step maps $P \mapsto [3]_q Q - q$. The ratio $|P|/|Q| \approx [2]_q$.
- Subsequent even steps divide by $[2]_q$.

If each tripling is followed by at least two halvings on average, the orbit contracts. Two halvings multiply by $1/[2]_q^2$; one tripling multiplies by $[3]_q/[2]_q$. The net factor per cycle is $[3]_q / [2]_q^3 < 1$, with margin:

$$
[2]_q^2 - [3]_q = q.
$$

Two halvings beat one tripling by a factor $[2]_q^2 / [3]_q = 1 + q/[3]_q \approx 4/3$.

**Conjecture.** Given the QOU above, for all $q > 1$ and all $P \in \mathbb{Z}[q^{± 1}]_{>0}$ the orbit $\{\mathcal{C}_q^k(P)\}_{k \geq 0}$ reaches the fundamental $2$-cycle $\{q^{-1},\, 1 + q^{-1}\}$.

At the Skein level the attractor is this $2$-cycle, not the literal unknot polynomial $1$: since $1$ evaluates to $1 \notin \{0, -1\}$ modulo $[2]_q$ (i.e. at $q = -1$), it is neither $q$-even nor $q$-odd, so $\mathcal{C}_q(1)$ is undefined. The cycle $\{q^{-1}, 1 + q^{-1}\}$ is the $q$-lift of the classical $\{1, 2\}$; writing the classical target as "$1$" is the $q \to 1$ shorthand.

The Collatz obstruction $\kappa_C := \mathrm{res}_{C_q}(\kappa_0) \in H^2(\mathcal{S}_{C_q}, \mathbb{G}_m)$ ([classical limit obstruction](#def:classical-limit-obstruction), [QOU obstruction reduction](#thm:qou-obstruction-reduction)) measures the failure of Skein-Collatz orbits to converge. The conjecture $\kappa_C = 0$ is equivalent to stating that every element of the Skein module $\mathcal{S}(q) \cong \mathbb{Z}[q^{± 1}]$ reduces to the unknot polynomial $1$ under iterated crossing resolution via $\mathcal{C}_q$.
