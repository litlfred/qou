---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-009-41-interpolating-sums-of-r-cycles
section_title: "Interpolating sums of r-cycles"
section_number: 4.1
pages: 23-26
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Re p(St)."
text_source: latex
latex_prose_ratio: 0.861
latex_coverage_ratio: 0.918
---
In this section we define morphisms in $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$ which "interpolate\" the action of the sum of all $r$-cycles on representations of symmetric groups. To begin, let $r$ and $d$ be positive integers with $r\leq d$.

::: definition
[]{#sums label="sums"} Let $\Omega_{r, d}\in FS_d$ denote the sum of all $r$-cycles in $S_d$.
:::

Since $\Omega_{r, d}$ is in the center of $FS_d$, the action of $\Omega_{r, d}$ on $V_d^{\otimes n}$ gives an element of $\text{End}_{S_d}(V_d^{\otimes n})$ for each integer $n\geq 0$. This, along with Theorem [\[sw\]](#sw){reference-type="ref" reference="sw"}, shows the following definition is valid.

::: definition
[]{#Cint label="Cint"} For nonnegative integers $r, n,$ and $d$ with $r\leq d$ and $2n\leq d$, let $C_n^{r}( d)$ denote the unique element of $FP_n(d)$ with $f(C_n^r(d))\in\text{End}_{S_d}(V_d^{\otimes n})$ given by the action of $\Omega_{r, d}$.
:::

The first goal of this section is to define elements of $FP_n(t)$ for arbitrary $t\in F$ which agree with the definition of $C_n^r(t)$ when $t$ is a sufficiently large integer. We are able to do this because, as we will show, $C_n^r(d)$ depends polynomially on $d$. The fact that $C_n^r(d)$ depends polynomially on $d$ boils down to the following combinatorial proposition.

::: proposition
[]{#rcycs label="rcycs"} Suppose $n$ is a nonnegative integer and $\pi\in P_{n, n}$. Fix the following notation.

-   Let $a$ denote the number of parts of $\pi$.

-   Let $b$ denote the number of parts $\pi_k$ of $\pi$ such that $j, j'\in \pi_k$ for some $1\leq j\leq n$.

-   Let $c$ denote the number of connected components in the trace diagram of $\pi$ (see section [\[trace\]](#trace){reference-type="ref" reference="trace"}).

-   Suppose $r$ and $d$ are positive integers with $d\geq r$, and ${\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}'\in[n, d]$ are such that the $({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}')$-coloring of $\pi$ is perfect. Let $S(\pi, r, d)$ denote the number of $r$-cycles, $\sigma\in S_d$, such that $\sigma(i_j)=i'_j$ for all $1\leq j\leq n$.

Fix a positive integer $r$.

\(1\) If $S(\pi, r, d)\not=0$ for some integer $d\geq r$, then $S(\pi, r, d')\not=0$ for all $d'\geq d$.

\(2\) If $S(\pi, r, d)$ is nonzero, then $$\label{rcycles}S(\pi, r, d)=\frac{(r-a+c-1)!}{(r-a+b)!}\prod_{k=1}^{r+b-a}(d-r-b+k).\footnote{If $r=a-b$ then the empty product $\prod\limits_{k=1}^{r+b-a}(d-r-b+k)$ is equal to 1, and (\ref{rcycles}) gives $S(\pi, r, d)=(c-b-1)!$.  If $r<a-b$ or $r\leq a-c$ then $S(\pi, r, d)$ is zero for all $d$, so (\ref{rcycles}) does not apply.}$$
:::

::: proof
*Proof.* Part (1) is clear. To prove part (2), since $S(\pi, r, d)$ does not depend on the choice of perfect coloring of $\pi$, we may assume $\{i_j, i_j'~|~j=1,\ldots, n\}=\{1,\ldots, a\}$. For $x, y\in\{1,\ldots, a\}$ write $x\to y$ if $x=i_j$ and $y=i_j'$ for some $1\leq j\leq n$. Generate the weakest equivalence relation on $\{1,\ldots, a\}$ such that $x$ and $y$ are equivalent whenever $x\to y$. Notice that the equivalence classes correspond precisely to the connected components in the trace diagram of $\pi$. Hence there are $c$ equivalence classes. Now assume $S(\pi, r, d)\not=0$. Then the following two implications must hold: if $x\to y$ and $x\to y'$ then $y=y'$; if $x\to y$ and $x'\to y$ then $x=x'$. In particular, there are exactly $b$ equivalence classes with only one element; hence the $c-b$ equivalence classes with more than one element must account for $a-b$ elements of $\{1,\ldots, a\}$.

Now, an $r$-cycle in $\sigma\in S_d$ can be thought of as a cyclic arrangement of $r$ distinct elements of $\{1,\ldots, d\}$. If $\sigma(i_j)=i_j'$ for all $1\leq j\leq n$, then among the elements in $\{1,\ldots, a\}$ the cyclic arrangement corresponding to $\sigma$ contains precisely the $a-b$ elements in equivalence classes with more than one element. Moreover, if $x\to y$ for distinct $x, y\in\{1,\ldots, a\}$, then $x$ and $y$ must be adjacent in the cyclic arrangement corresponding to $\sigma$. Hence $\sigma$ is determined by a cyclic arrangement of the following $r-a+c$ items: $c-b$ equivalence classes with more than one element; $r-a+b$ elements of $\{a+1,\ldots, d\}$. Finally, if such a $\sigma$ exists, then any choice of $r-a+b$ elements of $\{a+1,\ldots, d\}$ arranged cyclically with the equivalence classes containing more than one element determines an $r$-cycle in $S_d$ which maps $i_j\mapsto i_j'$. Since there are $(r-a+c-1)!$ cyclic arrangements of $r-a+c$ items, and ${d-a\choose r-a+b}$ different $(r-a+b)$-element subsets of $\{a+1,\ldots, d\}$, it follows that $S(\pi, r, d)=(r-a+c-1)!{d-a\choose r-a+b}$, which is equivalent to the desired formula. ◻
:::

::: example
Let $n=15$ and $$\includegraphics{diss43.pdf}$$ Then $a=14$, $b=3$, and $c=7$. For $d\geq 14$, let ${\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}'\in[n, d]$ be the functions which give the perfect $({\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}')$-coloring of $\pi$ below. $$\includegraphics{diss44.pdf}$$ For an $r$-cycle $\sigma\in S_d$ to satisfy $\sigma(i_j)=i'_j$ for $j=1,\ldots, n$, $\sigma$ must fix the $3=b$ numbers $3, 9, 10$, and map $$\label{chains}
1\to 5\to 13,\qquad 2\to 14,\qquad 4\to 11,\qquad 7\to 8\to 6\to 12.$$ Clearly, such an $r$-cycle exists if and only if $r\geq11=a-b$ and $d\geq r+3=r+b$. In that case, the number of such $r$-cycles can be counted as follows. There are $(r-8)!=(r-a+c-1)!$ ways to arrange the $4=c-b$ "chains\" listed in ([\[chains\]](#chains){reference-type="ref" reference="chains"}) along with the $r-11=r-a+b$ other entries within the cycle. Moreover, there are $d-14=d-a$ choices for the remaining $r-11=r-a+b$ entries within the $r$-cycle after the "chains\" in ([\[chains\]](#chains){reference-type="ref" reference="chains"}) have been taken into account. Hence the number of desired $r$-cycles is given by $(r-8)!{d-14\choose r-11}=(r-a+c-1)!{d-a\choose r-a+b}$ which agrees with ([\[rcycles\]](#rcycles){reference-type="ref" reference="rcycles"}).$\rotatebox{45}{$\Box$}$
:::

With Proposition [\[rcycs\]](#rcycs){reference-type="ref" reference="rcycs"} in mind, we are now ready for the following definition.

::: definition
[]{#omega label="omega"} For $t\in F$ and integers $r>0$, and $n\geq0$, define $\omega_n^r(t)\in FP_n(t)$ as follows. Using the basis $\{x_\pi\}$ for $FP_n(t)$ defined in ([\[xpi\]](#xpi){reference-type="ref" reference="xpi"}), set $$\omega_n^r(t)=\sum_{\pi\in P_{n,n}}q_{\pi, r, t}x_\pi$$ where, using the notation set up in Proposition [\[rcycs\]](#rcycs){reference-type="ref" reference="rcycs"}, $$q_{\pi, r, t}=\left\{\begin{array}{ll}
0,& \text{if }S(\pi, r, d)=0\text{ for all integers }d>1,\\
\frac{(r-a+c-1)!}{(r-a+b)!}\prod\limits_{k=1}^{r+b-a}(t-r-b+k), & \text{otherwise.}\end{array}\right.$$
:::

Although the definition of $\omega_n^r(t)$ may seem a bit complicated, for the rest of this paper we will only be concerned with the following (less complicated) properties of $\omega_n^r(t)$.

::: proposition
[]{#centralomega label="centralomega"} (1) Fix integers $r>0$ and $n\geq 0$. Whenever $d$ is a sufficiently large[^1] integer, $\omega_n^r(d)=C_n^r(d)$. In other words, when $d$ is a sufficiently large integer, the map $f(\omega_n^r(d)):V_d^{\otimes n}\to V_d^{\otimes n}$ is given by the action of $\Omega_{r, d}\in S_d$.

\(2\) Fix $t\in F$ and an integer $r>0$. The morphisms $\omega_n^r(t): [n]\to[n]$ for each nonnegative integer $n$ form an endomorphism of the identity functor on $\underline{\operatorname{Re}}\!\operatorname{p}_0(S_t; F)$. In particular, $\omega_n^r(t)$ is in the center of $FP_n(t)$ for every $t\in F$ and integer $n\geq 0$.
:::

::: proof
*Proof.* For ${\mbox{\boldmath${i}$}}, {\mbox{\boldmath${i}$}}'\in [n, d]$, let $\pi({{\mbox{\boldmath${i}$}},{\mbox{\boldmath${i}$}}'})\in P_{n,n}$ denote the unique partition which has a perfect $({\mbox{\boldmath${i}$}},{\mbox{\boldmath${i}$}}')$-coloring. Then the action of $\Omega_{r, d}$ on $V_d^{\otimes n}$ maps the basis vector $v_{\mbox{\boldmath${i}$}}\mapsto \sum_{{\mbox{\boldmath${i}$}}'\in [n, d]}S(\pi({\mbox{\boldmath${i}$}},{\mbox{\boldmath${i}$}}'), r, d)v_{{\mbox{\boldmath${i}$}}'}$. On the other hand, ([\[fx\]](#fx){reference-type="ref" reference="fx"}) shows that $f(\omega_n^r(t))$ maps $v_{\mbox{\boldmath${i}$}}\mapsto \sum_{{\mbox{\boldmath${i}$}}'\in [n, d]}q_{\pi({\mbox{\boldmath${i}$}},{\mbox{\boldmath${i}$}}'), r, d}v_{{\mbox{\boldmath${i}$}}'}$. By Proposition [\[rcycs\]](#rcycs){reference-type="ref" reference="rcycs"}, $S(\pi({\mbox{\boldmath${i}$}},{\mbox{\boldmath${i}$}}'), r, d)=q_{\pi({\mbox{\boldmath${i}$}},{\mbox{\boldmath${i}$}}'), r, d}$ for sufficiently large $d$. This proves part (1).

To prove part (2), choose $\mu\in P_{n,m}$. For an integer $d>r$, we know that $f(\mu):V_d^{\otimes n}\to V_d^{\otimes m}$ commutes with the action of $\Omega_{r, d}\in S_d$. Hence, by part (1), $f(\omega_m^r(d)\mu)=f(\mu\omega_n^r(d))$ when $d$ is a sufficiently large integer. Thus, by part (2) of Theorem [\[sw\]](#sw){reference-type="ref" reference="sw"}, $\omega_m^r(d)\mu=\mu\omega_n^r(d)$ when $d$ is a sufficiently large integer. If we set $\omega_m^r(t)\mu=:\sum_{\pi\in P_{n, m}}a_\pi(t)\pi$ and $\mu\omega_n^r(t)=:\sum_{\pi\in P_{n, m}}a'_\pi(t)\pi$ for each $t\in F$, then we have shown the polynomials $a_\pi(t)$ and $a'_\pi(t)$ are equal when $t$ is a sufficiently large integer. Hence they are always equal. ◻
:::

## Frobenius' formula

This section will be devoted to studying how $\omega^r_n(t)$ interacts with indecomposable objects in $\underline{\operatorname{Re}}\!\operatorname{p}(S_t; F)$. We start with the following proposition.

::: proposition
[]{#xi label="xi"} Fix $t\in F$ along with integers $r>0$ and $n\geq0$. If $e$ is a primitive idempotent in $FP_n(t)$, then there exist $\xi\in F$ and a positive integer $m$ such that $(\omega_n^r(t)-\xi)^me=0$.
:::

::: proof
*Proof.* Let $\bar{F}$ denote the algebraic closure of $F$ and write $\omega:=\omega_n^r(t)$. Let $a(x)$ (resp. $a'(x)$) denote the monic polynomial of minimal degree in $F[x]$ (resp. $\bar{F}[x]$) with $a(\omega)e$ (resp. $a'(\omega)e$) equal to zero.[^2] First we will show that $a(x)$ is a power of an irreducible polynomial in $F[x]$. To do so, suppose $b(x)$ and $c(x)$ are relatively prime monic polynomials in $F[x]$ with $a(x)=b(x)c(x)$. Then there exist polynomials $g(x), h(x)\in F[x]$ with $\deg g(x)<\deg c(x)$, $\deg h(x)<\deg b(x)$, and $g(x)b(x)+h(x)c(x)=1$. Hence $g(\omega)b(\omega)e+h(\omega)c(\omega)e=e$ is a decomposition of $e$ into orthogonal idempotents (here we are using the fact that $\omega$ is in the center of $FP_n(t)$, see Proposition [\[centralomega\]](#centralomega){reference-type="ref" reference="centralomega"}(2)). Since $e$ is primitive, this implies $g(\omega)b(\omega)e=0$ or $h(\omega)c(\omega)e=0$. The minimality of $a(x)$ implies that either $g(x)=0$ or $h(x)=0$, which implies $c(x)=1$ or $b(x)=1$. Thus $a(x)$ is a power of an irreducible polynomial in $F[x]$. Since $e$ is primitive in $\bar{F}P_n(t)$ (see Proposition [\[fieldex\]](#fieldex){reference-type="ref" reference="fieldex"}), the same line of reasoning shows $a'(x)$ is a power of an irreducible polynomial in $\bar{F}[x]$. Hence $a'(x)=(x-\xi)^m$ for some positive integer $m$ and $\xi\in\bar{F}$. Since $a(x)$ is a power of an irreducible polynomial in $F[x]$ and $(x-\xi)^m$ divides $a(x)$ in $\bar{F}[x]$, we conclude $\xi\in F$. ◻
:::

Next, we use a classical result of Frobenius to produce a formula for the scalar $\xi$ in Proposition [\[xi\]](#xi){reference-type="ref" reference="xi"}. The study of this formula will be the key to describing the blocks of $\underline{\operatorname{Re}}\!\operatorname{p}(S_t, F)$ in section [\[secblocks\]](#secblocks){reference-type="ref" reference="secblocks"}. First we state Frobenius' result on the symmetric group:

::: theorem
[]{#fro label="fro"} Fix integers $d\geq r\geq 1$. Given a Young diagram $\lambda=(\lambda_0, \lambda_1,\ldots)$ of size $d$, set $\mu_i=\lambda_i-i$ for each $i\geq 0$. Then $\Omega_{r, d}$, (Definition [\[sums\]](#sums){reference-type="ref" reference="sums"}), acts on the simple $S_d$-module corresponding to $\lambda$ by the scalar $$\label{frob}\xi^\lambda_{r, k}:=\frac{1}{r}\sum_{i=0}^k~(\mu_i+k-1)(\mu_i+k-2)\cdots(\mu_i+k-r)\prod_{0\leq j\leq k\atop j\not=i}\frac{\mu_i-\mu_j-r}{\mu_i-\mu_j}$$ where $k$ is any positive integer such that $\lambda_{k+1}=0$.
:::

The result of Theorem [\[fro\]](#fro){reference-type="ref" reference="fro"} first appeared in [@Frob]. A modern proof of Theorem [\[fro\]](#fro){reference-type="ref" reference="fro"} is outlined in [@MR1153249 exercise 4.17], (see also [@MR1354144 Example 7 in section I.7]).

We close this section by showing the scalar $\xi$ in Proposition [\[xi\]](#xi){reference-type="ref" reference="xi"} is given by Frobenius' formula.

::: proposition
[]{#minpoly label="minpoly"} Fix $t\in F$, a positive integer $r$, and a Young diagram $\lambda$. Suppose that $L(\lambda)=([n], e)$ in $\underline{\operatorname{Re}}\!\operatorname{p}(S_t, F)$. If $k$ is a positive integer such that $\lambda_{k+1}=0$, then $(\omega_n^r(t)-\xi^{\lambda(t)}_{r, k})^me=0$ for some positive integer $m$.
:::

::: proof
*Proof.* By Theorem [\[Youngclass\]](#Youngclass){reference-type="ref" reference="Youngclass"} we may assume $n=|\lambda|$. Let $\xi$ and $m$ be as in Proposition [\[xi\]](#xi){reference-type="ref" reference="xi"}, so that $(\omega_n^r(t)-\xi)^me=0$. Applying the quotient map $\psi:FP_n(t)\twoheadrightarrow FS_n$ (Lemma [\[ees\]](#ees){reference-type="ref" reference="ees"}(2)) to this equation yields $(\psi(\omega_n^r(t))-\xi)^mc_\lambda=0$ in $FS_n$ where $c_\lambda$ is a primitive idempotent in $FS_n$ corresponding to $\lambda$. Since $\psi(\omega_n^r(t))$ is central in $FS_n$, this implies $\psi(\omega_n^r(t))c_\lambda=\xi c_\lambda$. Hence, by Definition [\[omega\]](#omega){reference-type="ref" reference="omega"}, $\xi$ depends polynomially on $t$.

Now, assume $d$ is a positive integer such that $d\geq\lambda_1+|\lambda|$. By Proposition [\[Findy\]](#Findy){reference-type="ref" reference="Findy"}, applying the functor $\mathcal{F}$ to the equation $(\omega_n^r(d)-\xi)^me=0$ yields $(\Omega_{r, d}-\xi)^mc_{\lambda(d)}=0$. Thus, by Theorem [\[fro\]](#fro){reference-type="ref" reference="fro"}, $\xi=\xi^{\lambda(t)}_{r, k}$ whenever $t=d$ is a sufficiently large integer. Since $\xi$ depends polynomially on $t$, $\xi^{\lambda(t)}_{r, k}$ is a rational function in $t$, and $\xi=\xi^{\lambda(t)}_{r, k}$ for infinitely many values of $t$, we conclude that $\xi=\xi^{\lambda(t)}_{r, k}$ for all $t\in F$. ◻
:::

[^1]: The statement is certainly true for $d\geq 2n+r$, although this bound is not sharp.

[^2]: The polynomial $a(x)$ (resp. $a'(x)$) exists since $FP_n(t)$ (resp. $\bar{F}P_n(t)$) is finite dimensional over $F$ (resp. $\bar{F}$).
