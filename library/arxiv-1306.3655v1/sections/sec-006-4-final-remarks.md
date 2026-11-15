---
doc_id: arxiv-1306.3655v1
doc_title: "The Murnaghan-Nakayama rule and some virtual S n characters"
section_id: sec-006-4-final-remarks
section_title: "Final remarks"
section_number: 4
pages: 9-10
source_pdf: 1306.3655v1.pdf
source_sha256: 45dd8bd55687ecce
toc_source: outline
text_source: latex
latex_prose_ratio: 0.711
latex_coverage_ratio: 0.967
doc_brief: "The Murnaghan-Nakayama rule and some virtual S n characters — We construct certain virtual characters for the symmetric groups, then compute a formula which calculates the values of these virtual"
---
::: remark
[]{#(1) label="(1)"} Let $n\ge 4$ and let $A_n$ be the set of partitions obtained by walking around $\nu=(1)$: $$A_n=\{(n),(1^n)\}\cup\{(r,2,1^{n-2-r})\mid 2\le r\le n-2\}.$$ Then $$\begin{aligned}
\label{(1)2}
\sum_{\lambda\in A_n}f^\lambda=(n-4)\cdot 2^{n-2}+4.
\end{aligned}$$

::: proof
*Proof.* Let $\lambda=(r,2,1^{n-2-r})$, then $$f^\lambda=\frac{n!}{(r-2)! (n-2-r)! r (n-r) (n-1)}=\frac{n(n-2)(n-3)}{r(n-r)}{n-4\choose r-2}.$$ Thus, omitting $\lambda\in \{(n),(1^n)\}$, we need to show that $$\begin{aligned}
\label{wz}
\sum_{r=0}^{n-4}\frac{n(n-2)(n-3)}{r(n-r)}{n-4\choose r-2} =(n-4)\cdot 2^{n-2}+2.
\end{aligned}$$ This can be proved by the Zeilberger Algorithm [@doron], and is implemented in Maple (function SumTools\[Hypergeometric\]\[Zeilberger\]). ◻
:::
:::

Here is a direct proof.

::: proof
*Zeilberger.* Note that $$\frac{1}{r(n-r)}=\frac{1}{n}\left( \frac{1}{r}+\frac{1}{n-r}\right),$$ so the sum in [\[wz\]](#wz){reference-type="eqref" reference="wz"} equals $$(n-2)(n-3)\sum_{r=2}^{n-2}\frac{1}{r}{n-4\choose r-2}+
(n-2)(n-3)\sum_{r=2}^{n-2}\frac{1}{n-r}{n-4\choose r-2}.$$ By symmetry these two summands are equal, so this equals $$2(n-2)(n-3)\sum_{r=2}^{n-2}\frac{1}{r}{n-4\choose r-2}=~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$$ $$2(n-2)(n-3)\sum_{r=2}^{n-2}\left(\int_0^1 x^{r-1} dx\right){n-4\choose r-2}=$$ $$2(n-2)(n-3)\sum_{r=2}^{n-2}\left(\int_0^1 x^{r-1} dx{n-4\choose r-2}\right)=$$ $$2(n-2)(n-3)\sum_{r=0}^{n-4}\left(\int_0^1 x^{r+1} dx{n-4\choose r}\right)=$$ $$2(n-2)(n-3)\int_0^1 x(1+x)^{n-4} dx=$$ $$2(n-2)(n-3)\left( \int_0^1 (1+x)^{n-3}dx- \int_0^1 (1+x)^{n-4}dx  \right)=$$ $$=(n-4) 2^{n-2}+2.$$ ◻
:::

Here is a second, combinatorial proof \[Zeilberger\].

Let $f(n)$ be the number of standard Young tableaux of shape $(r,2,1^{n-2-r})$ for some $2\le r\le n-2$, and look at the location of $n$.

Case 1: It is at the rightmost cell of the top row. Deleting it gives something counted by $f(n-1)$.

Case 2. The conjugate case, also yielding $f(n-1)$.

Case 3: $n$ is in the $(2,2)$ cell. Deleting it gives a tableau of strict hook shape (namely, not $(n-1)$ nor $(1^{n-1})$). Clearly, the number of these tableaux is $2^{n-1}-2$.

So we have the recurrence $f(n)=2f(n-1) +2^{n-1}-2$. Since $f(4)=2$, it follows by induction that $f(n)=(n-4) 2^{n-2}+2$.

## The polynomials $p_{\nu,n}(t)$

Recall Equation [\[v22\]](#v22){reference-type="eqref" reference="v22"}, replace minus $1$ by $t$ and get the polynomials $$\begin{aligned}
\label{v222}
p_{\nu,n}(t)=\sum_{j=1}^{n-k}f^{\nu*S_j}\cdot t^j.
\end{aligned}$$ In the case $\nu$ is empty we get $p_{\emptyset,n}(t)=(t+1)^{n-1}$. Denote $p_{(1),n}(t)=p_n(t)$ in the case $\nu=(1)$. By direct computations we got the following polynomials, for $1\le n\le 9$.

$p_4(t)=(t+1)^2$

$p_5(t)=(t+1)(t^2+4t+1)$

$p_6(t)=(t+1)^2(t^2+7t+1)$

$p_7(t)=(t+1)(t^4+13t^3+22t^2+13t+1)$

$p_8(t)=(t+1)^2 (t^4+18t^3+27t^2+18t+1)$

$p_9(t)=(t+1)(t^6+26t^5+79t^4+110t^3+79t^2+26t+1)$

$p_{10}(t)=(t+1)^2(t^6+33t^5+93t^4+131t^3+93t^2+33t+1)$

By [\[v22\]](#v22){reference-type="eqref" reference="v22"} $p_n(t)$ is divisible by $t+1$ for all $n$.

::: conjecture
We conjecture that when $n$ is even, the highest power of $t+1$ which divides $p_n(t)$ is 2, while when $n$ is odd, the highest power on $t+1$ which divides $p_n(t)$ is 1.

One also conjectures positiveness and unimodality on the coefficients of these polynomials.

Additional conjecture is as follows. Denote $p_{2k+1}(t)=(t+1)\cdot q_{2k+1}(t)$, then $q_{2k+1}(-1)=-2$.
:::
