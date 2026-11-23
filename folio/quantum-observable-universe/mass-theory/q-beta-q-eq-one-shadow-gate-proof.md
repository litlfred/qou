## Proof

Let $F(q)$ be a candidate Habiro element for the $\mathfrak{Q}_\beta$
precision ladder, generating coefficient functions $c_k(q)$ through
its $q$-difference kernel
([$c_k$ recursion](q-beta-c-k-recursion-from-habiro-q-difference.md)),
so that the ladder correction reads
$\prod_{k \ge 2}\bigl(1 + c_k(q)\,u^k\bigr)$ with
$u = b(q)\,\hbar_q^2$ the ladder variable. The gate asserts two
classical shadows of the canonical ladder,
$\lim_{q \to 1} c_2(q) = -1$ and $\lim_{q \to 1} c_3(q) = -2$, and
refutes any candidate failing either. The proof establishes the two anchor
values, then the rejection.

**Step 1 — the $c_2$ shadow is exact at every $q$.** By the
[$c_2$ structural identity](q-beta-c-2-eq-neg-one-structural.md), the
operator-valued $N = 2$ correction of the canonical ladder factorises
as the algebraic identity

$$
1 + c_2\,u^2 \;=\; 1 - b(q)^2\,\hbar_q^4 \;=\; 1 - u^2 ,
$$

valid over any commutative ring. Hence $c_2(q) = -1$ identically in
$q$ — a Taylor-exact constant, independent of $q_0$ and of all
experimental input. The classical shadow
$\lim_{q \to 1} c_2(q) = -1$ holds trivially, as the limit of a
constant function.

**Step 2 — the $c_3$ shadow equals $J_{\mathrm{Hopf}}(1) = -2$.** The
canonical $N = 3$ correction is anchored, per the registry anchoring
recorded in the statement, to the Jones polynomial of the Hopf link in
the classical limit; at the value level for $q \ne 1$ the coefficient
remains a near-match, which this gate does not use. It remains to
evaluate $J_{\mathrm{Hopf}}(1)$. Work in the normalization
$J_{\mathrm{unknot}} = 1$ with the skein relation
$J_{L_+} - J_{L_-} = (q - q^{-1})\,J_{L_0}$.

1. At $q = 1$ the right-hand side vanishes, so
   $J_{L_+}(1) = J_{L_-}(1)$: the evaluation at $q = 1$ is invariant
   under crossing changes.
2. Crossing changes transform any diagram of an $n$-component link
   into a diagram of the split union of $n$ unknots, so $J_L(1)$
   depends only on the number of components $n$.
3. In this normalization, adjoining a split unknotted component
   multiplies the invariant by the loop value
   $-(q^{1/2} + q^{-1/2})$, which at $q = 1$ equals $-2$; the unknot
   itself has value $1$.

Hence $J_L(1) = (-2)^{\,n-1}$ for every $n$-component link $L$. The
Hopf link has $n = 2$ components, so $J_{\mathrm{Hopf}}(1) = -2$, an
exact integer. (Consistency check: the positive Hopf link has
$J(q) = -q^{1/2} - q^{5/2}$, whose value at $q = 1$ is $-2$.)

**Step 3 — the gate.** The canonical ladder therefore satisfies
$c_2(1) = -1$ (Step 1, exactly, at every $q$) and $c_3(1) = -2$
(Step 2, via the registry anchoring). Both anchors are integers
evaluated at $q = 1$: the test lives entirely at the fibre level,
involves no substrate anchor $q_0$, and admits no experimental
tolerance — agreement is exact or it is not. Suppose a candidate $F$
generates $(c_2(q), c_3(q))$ with $c_2(1) \ne -1$ or
$c_3(1) \ne -2$. Then its coefficient functions disagree with the
canonical ladder's at order $u^2$ or $u^3$ in the classical limit;
since the $c_k$ are determined by $F$ through the $q$-difference
kernel, $F$ does not generate the canonical ladder. The candidate is
structurally refuted before any anchor sweep at $q_0$ — the
formalize-first rejection. $\blacksquare$
