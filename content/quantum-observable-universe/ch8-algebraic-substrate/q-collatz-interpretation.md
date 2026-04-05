The $q$-Collatz conjecture ([conj:q-collatz](#conj:q-collatz))
reformulates the Collatz problem as crossing resolution in
the Skein module $\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$.

### Three algebraic identities

The construction rests on three identities in
$\mathbb{Z}[q^{\pm 1}]$:

| Identity | Formula | Role |
|----------|---------|------|
| Skein divisibility | $[3]_q = q\,[2]_q + 1$ | "$3n+1$ is even for odd $n$" |
| Contraction gap | $[2]_q^2 - [3]_q = q$ | Net contraction per cycle |
| Hecke reduction | $T^2 = (q-q^{-1})T + 1$ | Crossing number reduction |

The first identity ensures the odd branch is well-defined
in $\mathbb{Z}[q^{\pm 1}]$.  The second gives the Lyapunov
estimate $\lambda_q = \sqrt{[3]_q/[2]_q^2} < 1$.  The
third says the Hecke algebra reduces quadratic crossing
words to linear — the algebraic engine of Skein resolution.

### The Skein relation as convex combination

The Skein relation $q L_+ - q^{-1} L_- = (q-q^{-1}) L_0$
rewrites as:

$$
  J(L_+) = q^{-2}\,J(L_-) + (1-q^{-2})\,J(L_0).
$$

For $q > 1$: both coefficients $q^{-2}$ and $1-q^{-2}$
are in $(0, 1)$ and sum to $1$.  Each crossing resolution
is a **convex combination** of simpler Jones polynomial
values.  By convexity:

$$
  |J(L_+)| \;\leq\; \max\bigl(|J(L_-)|,\; |J(L_0)|\bigr).
$$

The crossing resolution is non-expansive.  This is the
$q$-analog of "division doesn't increase": the even
branch of classical Collatz ($n \to n/2$) is also
non-expansive.

### Why this formulation avoids the eigenspace problem

The earlier Reeb-rotation formulation failed because:
the Reeb flow $\phi^q_t$ preserves the eigenspaces
$A_H, A_V$ individually (it acts as a phase within
each space, not between them).  The $A_V$ component
grew unchecked.

The Skein formulation avoids this entirely.  There is
no eigenspace decomposition.  Instead:

- **Parity** is $[2]_q$-divisibility in $\mathbb{Z}[q^{\pm 1}]$,
  not weight-space membership
- **Contraction** comes from the Skein convexity (crossing
  resolution is a convex combination)
- **The map** operates on the Skein module (a ring),
  not on the Frobenius-Hopf algebra (a bimodule)

At $q = 1$: $\mathbb{Z}[q^{\pm 1}] / (q-1) \cong \mathbb{Z}$,
$[2]_q$-parity becomes ordinary parity, and $\mathcal{C}_1$
is the Syracuse map.

### The genuine gap in the Skein formulation

The algebraic identity $[3]_q < [2]_q^2$ gives the
contraction estimate $\lambda_q < 1$ per cycle, **but**
the cycle length is not fixed.  The number of even steps
after each odd step depends on the $[2]_q$-adic valuation
of the result.

**What is proved:**
- $[2]_q^2 - [3]_q = q$ (Lean: `qInt_gap`)
- The Skein resolution is a convex combination
- The accelerated odd step is well-defined: $[3]_q P + 1 \equiv 0 \pmod{[2]_q}$ for $q$-odd $P$

**What remains conjectural:**
- The $[2]_q$-adic valuation of $\mathcal{C}_q(P)$ is
  large enough, on average, that the number of even
  steps per cycle exceeds the critical threshold

This is the $q$-analog of the classical heuristic:
Collatz orbits hit even numbers often enough that the
halvings (each contracting by $1/[2]_q$) outweigh the
triplings (each expanding by $[3]_q/[2]_q$).
The identity $[3]_q < [2]_q^2$ guarantees that
**two halvings more than compensate one tripling** —
but the conjecture is that the orbit structure provides
those two halvings.

### The $(p_1^{k_1}, p_2^{k_2})$ family

The Collatz map $(2, 3)$ — divide by $2$, multiply by $3$
— is one member of a family of generalized maps
$(p_1, p_2)$: divide by $p_1$ when divisible, apply
$p_2 n + 1$ otherwise.  The $q$-deformed contraction
condition is:

$$
  [p_1]_q^{k_1} \;>\; [p_2]_q^{k_2}
$$

where $k_1$ halvings (by $[p_1]_q$) must overpower $k_2$
triplings (by $[p_2]_q$).  The **contraction gap** is the
polynomial $[p_1]_q^{k_1} - [p_2]_q^{k_2} \in
\mathbb{Z}[q^{\pm 1}]$.

**Trivial cases.** When $p_1^{k_1} \gg p_2^{k_2}$
classically, the gap polynomial has all positive
coefficients and the contraction holds for all $q > 0$.
Examples: $(3, 2)$, $(4, 3)$, $(a, a+1)$ with $k_1 = 2$,
$k_2 = 1$ for any $a \geq 2$.  The $(a, a+1)$ family is
always contractive because $[a]_q^2 - [a+1]_q$ has all
non-negative coefficients.

**Interesting cases.** When $p_1^{k_1}$ barely exceeds
$p_2^{k_2}$ classically ($p_1^{k_1} = p_2^{k_2} + 1$),
the gap polynomial may have **negative coefficients** at
high $q$-degree, and the contraction can fail for large
$q$.

| $(p_1^{k_1}, p_2^{k_2})$ | Classical gap | $q$-gap | Positive for $q > 0$? |
|--------------------------|--------------|---------|----------------------|
| $(2^2, 3^1)$ — **Collatz** | $4 - 3 = 1$ | $q$ (monomial) | **Yes** |
| $(3^2, 8^1)$ | $9 - 8 = 1$ | $q + 2q^2 + q^3 - q^5 - q^6 - q^7$ | No |
| $(4^2, 15^1)$ | $16 - 15 = 1$ | negative high-degree terms | No |

Collatz $(2^2, 3^1)$ is **unique** among the critical
cases $p_1^{k_1} = p_2^{k_2} + 1$: it is the only one
where the $q$-deformed gap is a **monomial** ($= q$) and
therefore positive for all $q > 0$.  Every other critical
case develops negative coefficients and fails for
sufficiently large $q$.

This singles out the $(2, 3)$ Collatz map as
arithmetically special in the $q$-deformed setting: it
sits at the unique point where the classical margin of $1$
lifts to a monomial $q$-margin — the substrate parameter
itself.

### Parallel with the five evaluations

| Evaluation | Module | Map | Classical shadow |
|------------|--------|-----|-----------------|
| Spectral | $H^2(\mathrm{Spec}(\xi_q))$ | Euler class restriction | RH |
| Collision | $H^2(\Sigma)$ | collision restriction | NS regularity |
| Elliptic | $H^2(\mathcal{E}_q)$ | elliptic restriction | BSD |
| Computational | $H^2(\mathcal{R})$ | resolution tree restriction | P $\neq$ NP |
| **Collatz** | $\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$ | Skein-Collatz iteration | **Collatz** |

The Collatz evaluation operates on the Skein module
itself — the natural home for the Hecke algebra and
crossing resolution — rather than on sheaf cohomology.
