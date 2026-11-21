*Proof.* The Skein-Collatz map is
**affine**, not linear: the odd branch carries an additive term,
$\mathcal{C}_q(P) = ([3]_q P + 1)/[2]_q$, and the even branch is
$\mathcal{C}_q(P) = P/[2]_q$. A periodic orbit of length $k$ with
$k_{\mathrm{odd}}$ odd steps and $k_{\mathrm{even}}$ even steps satisfies
$\mathcal{C}_q^k(P) = P$. Iterating the affine steps,

$$
  \mathcal{C}_q^k(P) = A\,P + B,
  \qquad
  A = \frac{[3]_q^{k_{\mathrm{odd}}}}{[2]_q^{k}},
  \qquad
  k = k_{\mathrm{odd}} + k_{\mathrm{even}},
$$

where $A = \prod_i a_i$ is the multiplicative holonomy and
$B = \sum_i \bigl(\prod_{j>i} a_j\bigr) b_i$ collects the additive
contributions (each $b_i = 0$ on even steps and $b_i = 1/[2]_q^{\,\cdot} > 0$
on odd steps, for $q > 0$). The cycle condition is therefore

$$
  (1 - A)\,P = B.
$$

**When $A = 1$** — i.e. $[3]_q^{k_{\mathrm{odd}}} = [2]_q^{k}$ — the
condition forces $B = 0$. If $k_{\mathrm{odd}} \geq 1$, some $b_i$ is
nonzero, so $B$ is a nonempty sum of products of rational functions in $q$
with positive coefficients. Then $B > 0$ at every real $q > 0$, and $B \neq 0$
in $\mathbb{Q}(q)$ (evaluate at $q = 1$). So $B = 0$ fails and there is no
balanced cycle with an odd step, whether $q$ is formal or a real number
$q > 0$. This argument does not need $A \neq 1$.

Formally the $A = 1$ case never arises when $k_{\mathrm{odd}} \geq 1$:
$[2]_q$ and $[3]_q$ are **coprime** in
$\mathbb{Z}[q]$: the Skein divisibility identity

$$
  [3]_q - q[2]_q = 1
$$

gives $\gcd([2]_q, [3]_q) = 1$ by Bézout, so $[3]_q$ is a unit modulo
$[2]_q$ while $[2]_q^k \equiv 0 \pmod{[2]_q}$ for $k \geq 1$ — hence
$A = 1$ is **impossible in $\mathbb{Z}[q]$ for $k_{\mathrm{odd}} \geq 1$**.
At a real value of $q$ it can occur: at the plastic number $\rho$, the real
root of $q^3 = q + 1$, one has $1 + \rho + \rho^2 = \rho^5$ and
$1 + \rho = \rho^3$, so $[3]_\rho^{\,3} = \rho^{15} = [2]_\rho^{\,5}$.
The positivity of $B$ above still excludes the cycle there. The only
$A = 1$ orbit is the all-even chain ($k_{\mathrm{odd}} = 0$),
$P \mapsto P/[2]_q^k = P$, forcing $P = 0$. So the coprimality identity
excludes every periodic orbit whose holonomy is *balanced* ($A = 1$),
other than the degenerate fixed point, formally and at every real $q > 0$. $\square$

**Scope.** The coprimality argument settles only the $A = 1$ sub-case. The generic cycle has
$A \neq 1$ — indeed coprimality *guarantees* $A \neq 1$ in $\mathbb{Z}[q]$ for
$k_{\mathrm{odd}} \geq 1$ — and the cycle condition then has a unique
candidate solution

$$
  P_0 = \frac{B}{1 - A} \in \mathbb{Q}(q),
$$

positive in the contractive regime ($A < 1$, i.e.
$[3]_q^{k_{\mathrm{odd}}} < [2]_q^{k}$). Coprimality makes this candidate
*solvable*, not impossible. Excluding it needs a different argument, given
next.

**The affine case ($A \neq 1$) in $\mathbb{Z}[q^{\pm 1}]$.** The only
periodic orbits of $\mathcal{C}_q$ on $\mathbb{Z}[q^{\pm 1}]$ are $\{0\}$,
the odd fixed point $\{-q^{-2}\}$ and the fundamental cycle
$\{q^{-1},\, 1 + q^{-1}\}$. No positivity hypothesis and no real value of $q$
is used. The proof reads two integers off each end of a Laurent polynomial.
Write $b = \operatorname{ord}_q P$, let $\beta \neq 0$ be the coefficient of
$q^{b}$ and $\beta'$ that of $q^{b+1}$. Both branches divide by $[2]_q = 1 + q$,
which has constant term $1$, so $\operatorname{ord}_q$ is unchanged by an even
step, and also by an odd step when $b < 0$; hence $b$ is constant along a cycle
once it is negative.

1. *Case $b \leq -2$.* An even step $P = (1+q)P'$ gives
   $\beta'(P') = \beta' - \beta$. An odd step $(1+q)P' = [3]_q P + 1$ leaves
   $\beta'$ unchanged, because $[3]_q P$ has coefficients $\beta$ and
   $\beta + \beta'$ in degrees $b$ and $b+1$, and the $+1$ sits in degree
   $0 > b + 1$. Around a cycle with $e$ even steps, $e\beta = 0$, so $e = 0$.
   An all-odd cycle satisfies $(1+q)D' = [3]_q D$ for $D = P + q^{-2}$, so
   $\bigl((1+q)^k - [3]_q^{k}\bigr) D = 0$, and $(1+q)^k \neq [3]_q^k$ (at
   $q = 1$, $2^k \neq 3^k$). Hence $P = -q^{-2}$.
2. *Case $b \geq 0$.* All terms are polynomials, and evaluation at $q = 0$
   gives $P'(0) = P(0)$ on an even step and $P'(0) = P(0) + 1$ on an odd
   step. A cycle therefore has no odd step, and an all-even cycle has
   $\bigl((1+q)^k - 1\bigr)P = 0$, so $P = 0$.
3. *Case $b = -1$.* Put $S = qP \in \mathbb{Z}[q]$; the odd step becomes
   $(1+q)S' = [3]_q S + q$. If some $S$ in the cycle is a constant $c$, an
   even step from it is impossible by degree and the odd step forces $c = 1$
   (evaluate at $q = -1$), so the orbit is $S \in \{1,\, 1+q\}$, the
   fundamental cycle. Otherwise every $S$ has degree $d \geq 1$. Reversing
   coefficients turns $(1+q)S' = [3]_q S + q$ into
   $(1+q)\tilde S' = [3]_q \tilde S + q^{d+1}$ with $d + 1 \geq 2$, while the
   even step reverses to itself, since $1+q$ and $[3]_q$ are palindromic. The
   count of case 1 applies to the reversed sequence, whose constant term is the
   leading coefficient of $S$, so there is no even step. Then
   $D = qP + 1$ obeys $(1+q)D' = [3]_q D$, forcing $qP = -1$, which is not a
   polynomial identity. So this sub-case has no cycle.

Formalised sorry-free as `cycle_classification` and
`laurent_cycle_classification` in
`QOU/AppendixSurreals/collatz_cycle_classification.lean`. This agrees with the
computational census over all primitive parity words through period $18$,
which finds only the positive $2$-cycle $\{q^{-1},\, 1 + q^{-1}\}$ and the
negative fixed point $-q^{-2}$, the $q$-lifts of the classical $\{1, 2\}$
and $\{-1\}$. The statement concerns the formal ring
$\mathbb{Z}[q^{\pm 1}]$ and says nothing about classical Collatz cycles: a
classical integer cycle need not lift to $\mathbb{Z}[q^{\pm 1}]$. $\square$

**Classical limit.** At $q = 1$: $\gcd(2, 3) = 1$ and
$3^a \neq 2^b$ for $a, b > 0$ (unique prime factorization).
The $q$-deformation lifts this to polynomial coprimality.

**The full $(a, a+1)$ family.** The identity
$\gcd([a]_q, [b]_q) = [\gcd(a,b)]_q$ shows that every
Collatz-type map $(a, a+1)$ excludes *balanced-holonomy* cycles,
since $\gcd(a, a+1) = 1$ for all $a$.  This exclusion
is a consequence of consecutive integers being coprime
— a fact that lifts from $\mathbb{Z}$ to $\mathbb{Z}[q]$
via the $q$-integer functor. Like the base case above, it
constrains the $A = 1$ locus and does not by itself reach the
affine ($A \neq 1$) cycle problem.

**Open directions.** Cycle exclusion is settled in
$\mathbb{Z}[q^{\pm 1}]$: the balanced case by coprimality above, the affine
case by the classification above. One piece remains open:

1. **No divergent orbits**: the contact condition
   $\langle v_{[2]} \rangle \geq 2$
   ([contact boundary](#conj:collatz-contact-boundary)).
