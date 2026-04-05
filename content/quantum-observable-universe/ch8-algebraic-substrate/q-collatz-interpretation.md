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
