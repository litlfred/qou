The $q$-Collatz conjecture ([conj:q-collatz](#conj:q-collatz))
lives in the Skein module $\mathcal{S}(q) \cong \mathbb{Z}[q^{\pm 1}]$,
where parity is $[2]_q$-divisibility and crossing resolution
replaces arithmetic.  Three algebraic identities control
the dynamics, and the $(p_1^{k_1}, p_2^{k_2})$ family reveals
why the classical Collatz map $(2, 3)$ is arithmetically special.

### Three identities

| Identity | Formula | Role |
|----------|---------|------|
| Skein divisibility | $[3]_q = q[2]_q + 1$ | "$3n+1$ is even for odd $n$" |
| Contraction gap | $[2]_q^2 - [3]_q = q$ | Two halvings beat one tripling |
| Hecke reduction | $T^2 = (q-q^{-1})T + 1$ | Crossing words reduce |

The first ensures the odd branch is well-defined in
$\mathbb{Z}[q^{\pm 1}]$.  The second says two halvings
overpower one tripling, with margin $q$ — the substrate
parameter itself.  The third reduces quadratic crossing
words to linear, the algebraic engine of the Skein relation.

### Skein convexity

The Skein relation rewrites as:

$$
  J(L_+) = q^{-2}J(L_-) + (1-q^{-2})J(L_0).
$$

For $q > 1$ both coefficients are positive and sum to $1$:
a convex combination.  Crossing resolution is
non-expansive on Jones polynomial values.

### The $(p_1^{k_1}, p_2^{k_2})$ family

The Collatz map $(2, 3)$ — divide by $2$, multiply by $3$
— belongs to a family of generalized maps $(p_1, p_2)$:
divide by $p_1$ when divisible, apply $p_2 n + 1$ otherwise.
The $q$-deformed contraction condition requires $k_1$
halvings to overpower $k_2$ triplings:

$$
  [p_1]_q^{k_1}  >  [p_2]_q^{k_2}.
$$

The **contraction gap** $[p_1]_q^{k_1} - [p_2]_q^{k_2}$
is a polynomial in $\mathbb{Z}[q^{\pm 1}]$.  Its
coefficient structure determines the contraction regime.

**Trivial cases.** When $p_1^{k_1} \gg p_2^{k_2}$
classically, the gap polynomial has all positive
coefficients and contraction holds for all $q > 0$.
The $(a, a+1)$ family with $k_1 = 2$, $k_2 = 1$ is
always contractive: $[a]_q^2 - [a+1]_q$ has all
non-negative coefficients for every $a \geq 2$.

**Critical cases.** At the boundary
$p_1^{k_1} = p_2^{k_2} + 1$ (classical margin of $1$),
the $q$-gap polynomial may develop **negative
high-degree coefficients**, breaking contraction for
large $q$:

| $(p_1^{k_1}, p_2^{k_2})$ | Classical gap | $q$-gap | All $q > 0$? |
|--------------------------|--------------|---------|-------------|
| $(2^2, 3^1)$ — **Collatz** | $4 - 3 = 1$ | $q$ | **Yes** (monomial) |
| $(3^2, 8^1)$ | $9 - 8 = 1$ | $q + 2q^2 + q^3 - q^5 - q^6 - q^7$ | No |
| $(4^2, 15^1)$ | $16 - 15 = 1$ | negative high-degree terms | No |

### Why $(2, 3)$ is unique

Collatz $(2^2, 3^1)$ is the **unique** critical case
where the $q$-gap is a monomial.  The identity
$[2]_q^2 - [3]_q = q$ produces a gap with a single term
— the substrate parameter $q$ — which is positive for
all $q > 0$.  Every other critical case has a gap
polynomial with both positive and negative coefficients,
and the negative terms dominate for sufficiently large $q$.

This is not a coincidence.  The identity $[3]_q = q[2]_q + 1$
(Skein divisibility) forces $[2]_q^2 - [3]_q = [2]_q^2 - q[2]_q - 1
= [2]_q([2]_q - q) - 1 = [2]_q \cdot 1 - 1 = q$.  The
monomial form arises because $[3]_q$ is the **next**
$q$-integer after $[2]_q$, and the quadratic-minus-linear
structure of $[2]_q^2 - [3]_q$ cancels all but the
linear term.  For $[a]_q^2 - [a^2-1]_q$ with $a \geq 3$,
the gap polynomial has degree $2(a-1)$ vs $a^2 - 2$, and
the high-degree terms of $[a^2-1]_q$ overwhelm $[a]_q^2$.

### What is proved and what remains

**Proved (in Lean):**
- $[3]_q = q[2]_q + 1$ — Skein divisibility (`skein_divisibility`)
- $[2]_q^2 - [3]_q = q$ — contraction gap (`qInt_gap`)
- $[3]_q < [2]_q^2$ for $q > 0$ — contraction (`qInt3_lt_qInt2_sq`)
- $\sqrt{[3]_q/[2]_q^2} < 1$ — geometric mean (`geometric_mean_contraction`)
- $(3, 4)$ gap positive for $q > 0$ — trivial case (`qInt_gap_3_4`)
- $(3, 8)$ gap fails for $q > 2$ — critical failure (`qInt_gap_3_8_fails`)

**What remains conjectural:**
the orbit structure provides the two halvings.
The $[2]_q$-adic valuation of $\mathcal{C}_q(P)$ — how
deeply the result of each odd step is divisible by $[2]_q$
— must average to at least $2$
([contact boundary](#prop:collatz-contact-boundary)).
At $q = 1$ this average is exactly $2$ (a theorem).
The conjecture is that this holds for all $q > 1$.
