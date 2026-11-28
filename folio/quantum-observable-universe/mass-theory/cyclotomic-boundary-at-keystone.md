The binding $q$-deformation of the na-Stokes period
$S(n) = \sum_{\lambda \vdash n} \dim_q(\lambda)$ satisfies the recurrence

$$
S(n) \;=\; S(n-1) \;+\; [n-1]_q\,S(n-2) \;+\; D(n),
$$

whose deviation term $D(n)$ — the **Habiro tail** — carries a universal
$(q-1)^2$ double root at $q=1$ and is bar-even ($D(1/q)=D(q)$). The
conjecture asserts that $D(n)$ is **cyclotomic** — a product of cyclotomic
polynomials (times the $(q-1)^2$ factor and a $q$-monomial) — **if and
only if $n \leq 5$**, where $5$ is the quintic order $S_5 \supset A_5$.

**The alignment.** The cyclotomic-pure regime $n \leq 5$ coincides exactly
with the framework's calibration orders and the quintic order:

$$
\{\,n \leq 5 : D(n)\text{ cyclotomic}\,\}
\;=\;
\underbrace{\{n=2,3,4\}}_{\text{calibration orders } c=1,2,3}
\;\cup\;
\underbrace{\{n=5\}}_{S_5\text{ quintic order}}.
$$

The first non-cyclotomic (non-$q$-holonomic) content appears at the first
body order $n=6$ that is *neither* a calibration *nor* the quintic order.

**The arithmetic mechanism.** At $q=1$ one has $S(n)|_{q=1} = \sum_{\lambda
\vdash n} f^\lambda = I(n)$, the involution / telephone numbers (OEIS
A000085; the Frobenius–Schur identity, proved for all $n$ by RSK:
involutions $\leftrightarrow$ SYT). So $S(n)$ is the $q$-deformed involution
number — a Rogers–Szegő / $q$-Hermite moment — and the recurrence above is
the $q$-lift of $I(n)=I(n-1)+(n-1)I(n-2)$, with $D(n)$ its deviation. Prior
analysis of this $q$-involution kernel establishes the tail's structure: a
$(q-1)^2$ double root times a bar-even cofactor that is cyclotomic through
$n=5$ and acquires a genuine non-cyclotomic, **non-$q$-holonomic** factor
from $n=6$ — the same non-holonomicity that obstructs any fixed-order closed
form for $S(n)$. This is the mechanism that governs $D(n)$: it is a property
of *cancellation in the alternating sum*, not of any individual quantum
dimension.

**Why the individual quantum dimensions do not locate the boundary.** Every
$\dim_q(\lambda) = [n]_q!/\prod_c [h(c)]_q$ is a **product of cyclotomic
polynomials for every $n$** (a ratio of cyclotomic products that is a
polynomial). So cyclotomic-purity of the individual dimensions does not
distinguish $n=5$ from $n=6$: at both orders all $\dim_q(\lambda)$ are
cyclotomic. In particular the McKay observation below — that at $n=5$ the
four classes carry *single* quantum integers while at $n=6$ most are
*compound* products of several $[m]_q$ — is a single-$[m]_q$-vs-product
distinction, **not** a cyclotomic-vs-non-cyclotomic one (a product of
several cyclotomics is still cyclotomic). It does not, by itself, supply the
arithmetic mechanism above.

**The McKay coincidence (rep-theory, link unproven).** At the quintic order $n=5$
the four conjugation classes $\{\lambda,\lambda'\}$ of $S_5$ carry quantum
dimensions equal to the **$E_8$ Coxeter marks** $[\mathrm{mark}]_q$:

$$
\dim_q(5)=[1]_q,\quad
\dim_q(4,1)=[4]_q,\quad
\dim_q(3,2)=[5]_q,\quad
\dim_q(3,1,1)=[5]_q+1,
$$

because $A_5 \cong 2I/\{\pm 1\}$ is the **icosahedral** group and $2I
\leftrightarrow \widehat{E}_8$ (McKay). The McKay–ADE ladder of alternating
groups is finite: $A_4 \cong$ tetrahedral ($2T \leftrightarrow
\widehat{E}_6$), $A_5 \cong$ icosahedral ($2I \leftrightarrow
\widehat{E}_8$), and $A_6 \cong \mathrm{PSL}(2,9)$ is **not** a binary
polyhedral group. Thus $A_5$ is the last alternating group that is the
rotation group of a Platonic solid, and $A_6$ ($n=6$) is the first
non-McKay. That the McKay-mark structure exits at the same order the tail
leaves the cyclotomic ring is a **coincidence of orders**; by the caveat
above it does not act *through* cyclotomic-purity of the dimensions, and its
bearing on the arithmetic mechanism is unproven.

**Status — three tiers of correlation, not to be conflated.**

1. *Arithmetic* (the substance): $D(n)$ is non-cyclotomic from $n=6$. This is
   **proved for $6 \le n \le 20$** (finite Lean certificates) and, computer-assisted, for all
   $n \ge 9$ by the cumulant argument below; see
   the proposition that $D(n)$ is a cyclotomic product exactly for $n \le 5$. Generic high-degree bar-even integer polynomials are
   non-cyclotomic, so non-cyclotomicity is the *expected* outcome — the
   content is entirely that $n \leq 5$ *are* cyclotomic, and that "for all
   $n \geq 6$, with no exceptions" is what a proof must supply.
2. *Alignment*: that boundary coincides with {calibration $\cup$ quintic}
   orders $\{2,3,4\}\cup\{5\}$.
3. *Rep-theory*: the McKay-mark / $S_6$-outer-automorphism coincidence at
   $n=6$.

The **causation** — whether the $A_5 \to A_6$ McKay exit or the $S_6$ outer
automorphism *forces* the boundary — is unproved, and the route through the
single-vs-compound quantum dimensions does **not** establish it. What can be
said is the dovetail with $S(n)=\sum_{\lambda\vdash n}\dim_q(\lambda)=
\sum_\lambda W_\lambda$: the same $S_5$ whose quantum dimensions are the
$E_8$ marks carries the Verlinde measure $W_\lambda$. Specific root
magnitudes are not interpreted.

**What is proved.** *Derived from the definition* (Lean,
`QOU.Mass.CyclotomicBoundaryCertified`): for $2 \le n \le 9$, over a generic field with the hook
brackets nonzero, the hook-length definition above gives $q^{m_n}D(n) = P_n(q)$ for an explicit
$P_n \in \mathbb{Z}[q]$. In particular $D(2) = D(3) = 0$, $D(4) = q^{-2}\Phi_1^2\Phi_3$ and
$D(5) = 2q^{-4}\Phi_1^2\Phi_2^2\Phi_3\Phi_6$, so the forward direction holds for every $n \le 5$.
*The converse through $n = 20$:* for $6 \le n \le 20$, $P_n$ is not $c\,q^j\prod_k\Phi_k$. The
certificate is finite integer arithmetic: if $P = c\,q^j\prod\Phi_k$ and $p \mid P(a)$,
$p \nmid a$, $p \nmid P(b)$, then $a^k \equiv 1 \pmod p$ for some factor $\Phi_k$, so the
order $m$ of $a$ mod $p$ divides $k$ and $\varphi(m) \le \varphi(k) \le \deg P$. One witness
$(p, a)$ with $\varphi(m) > \deg P_n$ per $n$ refutes the factorisation (for example $n = 6$:
$p = 47$, $a = 28$, $m = 23$, $\varphi(23) = 22 > 14$). This uses no analysis and no
discriminant. The polynomials $P_{10}, \dots, P_{20}$ in the certificate are computed by
`computations/cyclotomic_boundary_certificates.py`; for $n \le 9$ they are derived in Lean.
The earlier $n = 6$ route (the deg-8 core $C_6$, palindrome identity, $\mathrm{disc}(\tilde C)
= -44208 < 0$) remains proved in `QOU.Mass.CyclotomicBoundaryKeystone`.

**Two infinite families (pen-and-paper proof, 2026-11-27).** Write $n = T_j + r$ with
$T_j = j(j+1)/2$ and $1 \le r \le j+1$.

*Leading coefficient.* $\dim_q(\lambda) = q^{-e_\lambda}g_\lambda(q^2)$ is bar-even with
leading coefficient $1$, where $e_\lambda = \binom n2 - \sum_{(i,j)\in\lambda}(i+j)$. The
minimisers of $\sum(i+j)$ fill the antidiagonals $0,\dots,j-1$ (the staircase $\delta_j$) and put
$r$ cells on antidiagonal $j$, whose $j+1$ positions are all addable corners of $\delta_j$. So the
top coefficient of $S(n)$ is $\binom{j+1}{r}$. Let $d_k$ be the antidiagonal of the $k$-th cell in
this filling. The top degrees of $S(n-1)$ and $[n-1]_qS(n-2)$ lie below that of $S(n)$ by
$n-1-d_n \ge 2$ and by $n-1-d_n-d_{n-1}$, which is $\ge 1$ for $n \ge 7$. Hence, for $n \ge 7$,
$$\operatorname{lead}(P_n) = \binom{j+1}{r}.$$

*The divisibility test.* If $P_n = c\,q^k\prod\Phi_{k_i}$, then $c = \operatorname{lead}(P_n)$
divides every coefficient of $P_n$, because each $\Phi_k$ is monic in $\mathbb Z[q]$.

*Second coefficient.* The shapes with $\sum(i+j)$ one above the minimum are of two kinds: one
cell moved from antidiagonal $j$ to $j+1$, or one cell moved from $j-1$ to $j$. Counting them
gives, whenever the gap $n-1-d_n-d_{n-1}$ is $\ge 2$ (true for $n \ge 9$),
$$a_1(P_n) = N_1 = 2\binom{j}{r-2} + j\binom{j-1}{r-3} + j\binom{j-1}{r+1}.$$
This agrees with the exact $P_n$ for $9 \le n \le 24$.

* $n = T_{j+1} - 1$ ($r = j$), every $j \ge 3$: $N_1 = j^2(j-1)/2$, and
  $j^2(j-1) \equiv -2 \pmod{j+1}$, so $(j+1) \nmid N_1$. **$D(n)$ is not cyclotomic.**
* $n = T_j + 1$ ($r = 1$), every $j \ge 4$ with $j \ne 5$: $N_1 = j(j-1)(j-2)/2$, and
  $j(j-1)(j-2) \equiv -6 \pmod{j+1}$, so $(j+1) \nmid N_1$ unless $(j+1) \mid 6$.
  **$D(n)$ is not cyclotomic.** (The exception $j = 5$ is $n = 16$, covered by the finite
  certificate.)

*The power-sum test.* If $P = c\,q^k\prod\Phi_{k_i}$ has degree $d$, then over $\mathbb C$
every root of $P$ is $0$ or a root of unity. Writing $a_1, a_2$ for the coefficients of
$q^{d-1}, q^{d-2}$, Vieta gives $a_1^2 - 2c\,a_2 = c^2\sum_z z^2$, so
$$\bigl|a_1^2 - 2c\,a_2\bigr| \le c^2 d .$$
This is sharper than divisibility when $c = 1$.

*Third coefficient at triangular $n$.* Let $n = T_{j+1}$ with $j \ge 3$. The minimiser of
$\sum(i+j)$ is the staircase $\delta_{j+1}$ alone, so $c = 1$, and $a_1 = j(j+1)$ (the formula
for $N_1$ at $r = j+1$). The top degrees of $S(n-1)$ and $[n-1]_qS(n-2)$ lie $T_j$ and
$j(j-1)/2$ below the top, both $\ge 3$, so only $S(n)$ reaches $a_2$. Two kinds of term reach
it. The staircase itself contributes the second coefficient of $g_{\delta_{j+1}}$, which is
(corners $- 1$) $= j$. The shapes with $\sum(i+j)$ two above the minimum each contribute $1$.
A shape that removes a cell from antidiagonal $j-1$ must also remove its two neighbours on
antidiagonal $j$, which costs at least $4$. So these shapes remove two corners from antidiagonal
$j$ and add two cells on antidiagonal $j+1$ that do not rest on a removed corner. Two adjacent
corners block $3$ of the $j+2$ positions, and two non-adjacent corners block $4$. Hence
$$a_2 = j + j\binom{j-1}{2} + \Bigl(\binom{j+1}{2} - j\Bigr)\binom{j-2}{2}
      = j + \frac{j(j-1)^2(j-2)}{4}.$$
The degree is $d = 2\bigl(\binom n2 - \sum_{k \le j} k(k+1)\bigr) = j(j+1)(j+2)(3j+1)/12$.
Therefore
$$a_1^2 - 2a_2 - d = \frac{j(j-1)(3j^2 + 41j + 14)}{12} > 0 ,$$
and the power-sum test fails. **For every triangular $n \ge 10$, $D(n)$ is not cyclotomic.**
The formulas for $c, a_1, a_2, d$ agree with the exact $P_n$ for $n = 10, 15, 21, 28$, and with
the near-staircase partition count for every triangular $n \le 91$.

*Lean.* `QOU.Mass.CyclotomicPowerSum` proves both tests for every cyclotomic product
(`leadingCoeff_dvd_coeff`, `abs_powerSum_two_le`), sorry-free. It also proves the arithmetic
of the three families for every $j$, taking the top coefficients of $P_n$ as hypotheses
(`not_isCycloProduct_triangular_of_topCoeffs`, `…_rEqJ_of_topCoeffs`, `…_rEqOne_of_topCoeffs`).
The partition count that supplies those coefficients is proved above on paper. Its first step is
formalised in `QOU.Mass.StaircaseMinimisers`, sorry-free: for any set $s$ of $T_m + r$ cells of
$\mathbb N^2$ with $r \le m+1$, $N(s) \ge N(\delta_m) + rm$, with equality exactly when $s$ is
$\delta_m$ plus $r$ cells on antidiagonal $m$ (`le_N_of_card`, `N_eq_iff`). Each of these is a
Young diagram (`isLowerSet_stair_union`), and there are $\binom{m+1}{r}$ of them
(`card_choices`). The second step is `QOU.Mass.StaircaseTopCoeff`, also sorry-free. Among the
Young diagrams with $T_m + r$ cells ($1 \le r \le m+1$), exactly $\binom{m+1}{r}$ attain the
minimum (`card_minimisers`), and $3N(\delta_{m+1}) = m(m+1)(m+2)$ (`three_mul_N_stair`).
For any family of integer polynomials $f_\lambda$ of degree at most $M - N(\lambda)$ with
coefficient $1$ there, the coefficient of $\sum_\lambda f_\lambda$ at degree $M - N_{\min}$ is
$\binom{m+1}{r}$ (`coeff_sum_shapes_of_top`). This takes the top term of the $q$-hook formula as
a hypothesis. `QOU.Mass.QHookTop` (sorry-free) discharges that hypothesis from the
divisibility half of the $q$-hook formula. With $[k] = 1 + t + \dots + t^{k-1}$, if
$[n]! = g_\lambda \prod_{c}[h(c)]$, then $g_\lambda$ is monic of degree $\binom n2 - N(\lambda)$
(`qHook_top_of_eq`, via $\sum_c h(c) = n + N(\lambda)$, `sum_hook`), and its next coefficient is
(corners of $\lambda$) $- 1$ (`qHook_nextCoeff_of_eq`). The same file proves the degree check
(`top_exponent_gap`): when $2m < n-1$, $S(n-1)$ and $[n-1]S(n-2)$ stay strictly below the top
exponent of $S(n)$. `QOU.Mass.StaircaseNearMin` (sorry-free) proves the $\delta = 1$ count. For
$n = T_m + r$, write $N_{\min} = N(\mathrm{stair}_m) + rm$. A Young diagram with $N = N_{\min} + 1$
has one of two shapes (`nearMin_classify`). Either it is the staircase, plus $r-1$ cells on
antidiagonal $m$, plus one cell on antidiagonal $m+1$ resting on them. Or it is the staircase less
one cell $b$ of antidiagonal $m-1$, plus $r+1$ cells on antidiagonal $m$, none of them sitting on
$b$. For $m \ge 1$ there are
$2\binom{m}{r-2} + m\binom{m-1}{r-3} + m\binom{m-1}{r+1}$ such diagrams (`card_nearMin_eq`), which is
$a_1$. Under the same divisibility hypothesis, this count is the coefficient one step below the top
of $\sum_\lambda X^{N(\lambda)} g_\lambda(X^2)$, which is $q^{\binom n2} S(n)$ in the symmetric
normalisation (`coeff_sum_sym_qHook_of_eq`). `QOU.Mass.StaircaseNearMin2` (sorry-free) proves
the $\delta = 2$ count and the formula for $a_2$ below: every diagram with $N = N_{\min} + 2$ adds
a set $C$ of cells on antidiagonal $m+1$ and removes a set $B$ of cells of antidiagonal $m-1$ with
$|C| + |B| = 2$ (`nearMin2_classify`), the three families are counted in closed form
(`card_nearMin2_eq`), the minimisers have $r\binom{m+1}{r} + m\binom{m-1}{r}$ corners in total
(`sum_corners_minimisers`), and for $n \ge 3$ the coefficient two steps below the top is the sum
of the two (`coeff_sum_sym_qHook_two`). `QOU.Mass.QHookDvd` (sorry-free) proves the
divisibility $\prod_c [h(c)] \mid [n]!$ itself (`hookProd_dvd_qfact`; Stanley, EC2, §7.21
\cite{stanley1999}), so the three coefficient statements hold with no hypothesis
(`coeff_sum_qHook`, `coeff_sum_sym_qHook`, `coeff_sum_sym_qHook_two_uncond`). Since
$[k] = \prod_{1 < d \mid k} \Phi_d$, it suffices that for each $d \ge 2$ at most
$\lfloor n/d \rfloor$ cells have $d \mid h(c)$. With $L = n$ rows and beta numbers
$\beta_i = \lambda_i + L - 1 - i$, the cell $(i, j)$ gives a bead $\beta_i$ and an empty
position $\beta_i - h(i,j) = L + j - \lambda'_j$ on the same runner of the $d$-abacus, this map is
injective, and the beads satisfy $d \cdot \#\{\text{bead–gap pairs}\} + \binom L2 \le \sum_i \beta_i
= n + \binom L2$ (`bead_bound`, `mul_card_hook_dvd_le`).

Together with the finite certificates this settles $6 \le n \le 20$, every triangular $n$, and
every $n \in \{T_j + 1, T_{j+1} - 1\}$ with $j \ge 4$.

*Third coefficient for general $r$.* For $n = T_j + r$ with $1 \le r \le j+1$ and $n \ge 10$, the
same count gives $a_2$ as a sum of four kinds of term:
```tex
\[\begin{aligned}
a_2 ={}& \binom{j+1}{r}(r-1) + j\binom{j-1}{r}
  && \text{(corners of the minimisers)}\\
&+ 3\binom{j-1}{r-4} + 3(j-1)\binom{j-2}{r-5} + \Bigl(\binom j2 - j + 1\Bigr)\binom{j-3}{r-6}
  && \text{(two cells on antidiagonal } j+1)\\
&+ 2(j-1)\binom{j-2}{r-1} + 2\binom{j-1}{2}\binom{j-3}{r-2}
  && \text{(one corner of } \delta_j \text{ moved up two)}\\
&+ \Bigl(\binom j2 - j + 1\Bigr)\binom{j-3}{r+2} + (j-1)\binom{j-2}{r+2}
  && \text{(two corners of } \delta_j \text{ moved up one)}.
\end{aligned}\]
```
This agrees with the exact partition count for every $10 \le n \le 91$. With $c = \binom{j+1}{r}$,
$$\frac{a_1}{c} = -4j - 2 + \frac{2r(j-r)}{j+1} + \frac{j(j+2)}{r+1} + \frac{(j+2)^2}{j-r+2}.$$
Writing $B = r+1$, $C = j-r+2$ and $A = j+1 = B + C - 2$, this is
$$\frac{a_1}{c} = j - 2r + 1 + \frac{(C-1)(C-3)}{B} + \frac{(B-1)^2}{C} - \frac{2(C-1)(C-2)}{A},$$
so $c \mid a_1$ exactly when the last three fractions sum to an integer.
The power-sum test needs $c \mid a_1$ and then $c \mid 2a_2$. For non-triangular $n$ ($r \le j$)
and $j \le 400000$, $c \mid a_1$ happens only at
$(j,r) = (5,1), (5,3), (11,10), (14,6), (98,55), (143,109), (152,119), (440,153)$; there is no
solution with $440 < j \le 400000$. At each of the eight, $c \nmid 2a_2$. So the two tests settle
every $n$ with $j \le 400000$, that is every $n \le 80{,}000{,}600{,}000$
(`computations/cyclotomic_boundary_s1_scan.c` for the scan,
`computations/cyclotomic_boundary_power_sum.py` for $c \nmid 2a_2$). This is a finite check, not a
proof. A heuristic count suggests finitely many solutions. When $A$, $B$, $C$ are pairwise
coprime there are none. Modulo $A$ the numerator of the three fractions over $ABC$ is
$2C(C-1)(C-2)^2$, and $C - 2 \equiv -B$, so $A \mid 2(C-1)$. Since $0 < 2(C-1) < 2A$, this forces
$A = 2(C-1)$, that is $B = C$, which contradicts $\gcd(B, C) = 1$
(`QOU.Mass.StaircaseMinimisers.not_dvd_a1Num_of_coprime`, sorry-free). All eight solutions above
have a common factor between two of $A, B, C$. If only $A$ is coprime to $B$ and to $C$, the same
step still gives $B = C$, and then the three fractions sum to $(B-2)^2/B$, so $B \mid 4$ and
$(j, r) \in \{(1,1), (5,3)\}$ (`eq_and_dvd_four_of_coprime_A`). Every other solution has
$\gcd(A,B) > 1$ or $\gcd(A,C) > 1$. If $\gcd(A,B) = 1$, write $h = \gcd(B-1, C-1)$ and
$g = \gcd(A, C)$. Then $A \mid 2C(C-1)$ gives $A \in \{hg, 2hg\}$; the solutions $(11,10)$, $(14,6)$
and $(98,55)$ are of this kind. No proof of finiteness is known in general.

*A cumulant test.* Cumulants add under products, and
$\kappa_{2d}(\Phi_m) = \tfrac{B_{2d}}{2d}J_{2d}(m)$ with $J$ the Jordan totient
\cite{billeyswanson2023}. So a cyclotomic $P$, after removing its factors $(q-1)$, has
$12\kappa_2 = \sum_i J_2(k_i) \in \mathbb Z$. For $4 \le n \le 24$ every $D(n)$ has exactly the
factor $(q-1)^2$, and $12\kappa_2$ is an integer only for $n = 4, 5, 7$
(`computations/cyclotomic_boundary_cumulant_integrality.py`). This settles nothing beyond the
tests above, but it is independent of them.

*The expansion at $q = 1$.* Put $q = e^t$. Then $D(n) = d_2t^2 + d_4t^4 + O(t^6)$, the cleared
tail has $P(1) = d_2$, and $12\kappa_2 = 24d_4/d_2 - 2$. Expanding $\log[k]$ in $t$, writing the
hook power sums through contents ($\sum h^2 = \sum c^2 + n^2$ and
$\sum h^4 = \sum c^4 + 12n\sum c^2 + n^2 - 12(\sum c)^2$), and summing content power sums over
$\lambda$ with weight $f^\lambda$ through Jucys–Murphy elements and square-root counts gives,
with $x = I_{n-8}$, $y = I_{n-9}$ (involution numbers) and $c = (n-1)(n-2)(n-3)$,
$$6d_2 = c\,(n-6)(n^2-13)\,x + 2c\,(n-8)(n-5)(2n-5)\,y,$$
$$1080\,d_4 = c\,(n-6)\,Q_5(n)\,x + 2c\,(n-8)(n-5)\,Q_4(n)\,y,$$
with $Q_5 = 10n^5 - 51n^4 - 86n^3 + 774n^2 - 536n - 1695$ and
$Q_4 = 20n^4 - 157n^3 + 419n^2 - 333n - 219$. These agree with the exact $D(n)$ for
$9 \le n \le 24$. If $d_2 \mid 24d_4$, then $d_2$ divides $\Delta(n)\,x$ and $\Delta(n)\,y$, where
$$\Delta(n) = -2(n-8)(n-7)(n-6)(n-5)(n-4)\,c^2\,(5n^3 - 21n^2 - 101n + 201).$$
No odd prime divides both $I_m$ and $I_{m-1}$ (since $I_{m+p} \equiv I_m \pmod p$ and
$I_0 = I_1 = 1$), so the odd part of $d_2$ divides $\Delta(n)$. It does not for any
$9 \le n \le 3000$, so the test excludes all of these
(`computations/cyclotomic_boundary_q1_expansion.py`).

*All $n \ge 9$ (computer-assisted).* The steps above hold for every $n$:
- The two hook identities are polynomial identities in $\ell$ and the power sums of a beta-set
  $\{b_1 > \dots > b_\ell\}$, since hooks are the pairs $b > g$ with $b$ in the set and $g$ not.
  Both are proved in Lean for every finite beta-set (`QOU.Mass.HookContentBeta`, `hook_two`,
  `hook_four`, sorry-free).
- The sums $\sum_\lambda f^\lambda F(\lambda)$, with $F$ a content power sum or product of two,
  follow from expanding products of Jucys–Murphy transpositions over the orderings of their
  symbols. Each is a polynomial in $n$ times $I_{n-s}$ for each support $s$.
- $d_2$, $d_4$ and $\Delta$ then come out symbolically in $n$
  (`computations/cyclotomic_boundary_q1_proof_checks.py` checks all three as identities).
- $v_2(I_m) = \lfloor m/4\rfloor + (0,0,1,2)_{m \bmod 4}$ (`QOU.Mass.InvolutionTwoAdic`,
  sorry-free: $I_{4k} = 2^k\alpha$, $I_{4k+1} = 2^k\beta$ with $\alpha, \beta$ odd and
  $\alpha \equiv \beta \pmod 8$). A case split on $n \bmod 4$ then shows the two terms of
  $6d_2$ never have equal 2-adic valuation, so $v_2(d_2) \le v_2(c) + (n+1)/4$.
- So the odd part of $d_2$ is at least $(n-6)(n^2-13)I_{n-8}/(6 \cdot 2^{(n+1)/4})$, while
  $0 < |\Delta(n)| < 10n^{14}$. The first beats the second for $46 \le n \le 400$. Since
  $I_{m+2} \ge (m+1)I_m$, the ratio is multiplied by at least $(n-7)/(\sqrt2\,(1+2/n)^{14}) > 1$
  from $n$ to $n+2$ once $n \ge 40$, so the bound holds for all $n \ge 46$; $9 \le n \le 3000$ is
  checked directly.

Hence $12\kappa_2 \notin \mathbb Z$ and $D(n)$ is not cyclotomic for every $n \ge 9$. With the
certificates for $6 \le n \le 8$, $D(n)$ is cyclotomic exactly for $n \le 5$. This argument is
checked by computer algebra and one Lean file, and was checked by an independent review that
recomputed $d_2$, $d_4$ from the exact $D(n)$ at $n = 9, 12, 17, 25, \dots, 28$. The full chain is not
yet in Lean. The arithmetic statement is
the proposition that $D(n)$ is a cyclotomic product exactly for $n \le 5$; what stays
conjectural here is the alignment and its cause.
