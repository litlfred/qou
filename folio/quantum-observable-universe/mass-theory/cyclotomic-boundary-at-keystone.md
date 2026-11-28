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
   **proved for $6 \le n \le 20$** (finite Lean certificates) and for every triangular $n$ and the families $n = T_j \pm 1$, but **not for all $n \geq 6$**; the
   cofactor's non-$q$-holonomic degree growth is the structural reason, not
   yet a proof. Generic high-degree bar-even integer polynomials are
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
normalisation (`coeff_sum_sym_qHook_of_eq`). Not yet formalised: the divisibility
$\prod_c [h(c)] \mid [n]!$ itself (Stanley, EC2, §7.21 \cite{stanley1999}), and the $\delta = 2$
count behind $a_2$.

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
coprime, each fraction must be an integer on its own: $B \mid (C-1)(C-3)$, $C \mid (B-1)^2$ and
$A \mid 2(C-1)(C-2)$. But no proof of finiteness is known.

*Open:* non-cyclotomicity for **every** $n \ge 6$. What remains is the non-triangular $n$
outside the two families with $j > 400000$.
