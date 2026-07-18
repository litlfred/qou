*Proof (balanced-holonomy sub-case).* The Skein-Collatz map is
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
condition forces $B = 0$. But $[2]_q$ and $[3]_q$ are **coprime** in
$\mathbb{Z}[q]$: the Skein divisibility identity

$$
  [3]_q - q[2]_q = 1
$$

gives $\gcd([2]_q, [3]_q) = 1$ by Bézout, so $[3]_q$ is a unit modulo
$[2]_q$ while $[2]_q^k \equiv 0 \pmod{[2]_q}$ for $k \geq 1$ — hence
$A = 1$ is **impossible for $k_{\mathrm{odd}} \geq 1$**. The only
$A = 1$ orbit is the all-even chain ($k_{\mathrm{odd}} = 0$),
$P \mapsto P/[2]_q^k = P$, forcing $P = 0$. So the coprimality identity
excludes every periodic orbit whose holonomy is *balanced* ($A = 1$),
other than the degenerate fixed point. $\square$

**Scope (do not over-claim).** This settles only the $A = 1$ sub-case.
The generic cycle has $A \neq 1$ — indeed coprimality *guarantees*
$A \neq 1$ for $k_{\mathrm{odd}} \geq 1$ — and then the cycle condition
has a **unique candidate solution**

$$
  P_0 = \frac{B}{1 - A} \in \mathbb{Q}(q),
$$

which in the contractive regime ($A < 1$, i.e.
$[3]_q^{k_{\mathrm{odd}}} < [2]_q^{k}$) is positive. Coprimality makes
this candidate *solvable*, not impossible; excluding it requires showing
$B/(1-A)$ never lands in $\mathbb{Z}[q^{\pm 1}]_{>0}$ consistently with
its own parity word — the $q$-analog of classical nontrivial-cycle
exclusion, which is **open**. See
[audit 2026-07-18](https://github.com/litlfred/qou/blob/claude/q-collatz-status-1v0pxv/docs/audits/2026-07-18-collatz-no-cycles-multiplicative-shadow-gap.md).

**Classical limit.** At $q = 1$: $\gcd(2, 3) = 1$ and
$3^a \neq 2^b$ for $a, b > 0$ (unique prime factorization).
The $q$-deformation lifts this to polynomial coprimality.

**The full $(a, a+1)$ family.** The identity
$\gcd([a]_q, [b]_q) = [\gcd(a,b)]_q$ shows that all
Collatz-type maps $(a, a+1)$ exclude periodic cycles,
since $\gcd(a, a+1) = 1$ for all $a$.  Cycle exclusion
is a consequence of consecutive integers being coprime
— a fact that lifts from $\mathbb{Z}$ to $\mathbb{Z}[q]$
via the $q$-integer functor.

**Remaining work.** This proposition settles only the
balanced-holonomy ($A = 1$) sub-case of cycle exclusion, not the full
no-cycles half. Two pieces remain open:

1. **Nontrivial-cycle exclusion** ($A \neq 1$): show the candidate
   $P_0 = B/(1-A)$ never realises a genuine positive Skein-module cycle
   — the $q$-analog of classical nontrivial-cycle exclusion.
2. **No divergent orbits**: the contact condition
   $\langle v_{[2]} \rangle \geq 2$
   ([contact boundary](#prop:collatz-contact-boundary)).

The classical $(a, a+1)$ remark below concerns the same $A = 1$
balanced sub-case; it does not extend to the affine problem.
