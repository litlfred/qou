---
doc_id: arxiv-0810.1697v1
doc_title: "ON THE CABLE EXPANSION FORMULA"
section_id: sec-005-4-proof-of-theorem-1
section_title: "Proof of Theorem 1"
section_number: 4
pages: 8-12
source_pdf: 0810.1697v1.pdf
source_sha256: 1aef66179da3c154
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.963
doc_brief: "ON THE CABLE EXPANSION FORMULA — In this paper, a generalized version of Morton’s formula [8] is proved."
---
[]{#proof label="proof"} []{#proof label="proof"}

::: proof
*Proof.*  

Assume it's true for (p,q), let's do the calculation in the case (q,p).

By explicit calculation, we got $$\langle\omega_r\rangle_U(A^2-A^{-2})^2\equiv -2(r+1)$$

So by lemma 2, $$\begin{aligned}
 &(-1)^{l+s}g_\sigma^l(q,p;s)(-2(r+1))\notag\\
&= 4\sum_{t=0}^{r-1}\sum_{k\ge 0} (-1)^{k+t}g_{\sigma}^k(p,q;t)\sinh((t+1)(l+1)C)\sinh((s+1)(k+1)C)\notag
\end{aligned}$$ where we evaluate these polynomials at $A=\exp(\frac{\pi i}{2(r+1)})$, and we denote the constant $\frac{\pi i}{r+1}$ by $C$.

And then using the formula for $g(p,q;t)$, we have $$\begin{aligned}
 &(-1)^{l+s}g_\sigma^l(q,p;s)(-2(r+1))\notag\\
&= (-1)^{qN}4\sum_{t=0}^{r-1}\sum_{k\ge 0}
(-1)^{k+t} \exp(\epsilon(-t^2-2t+k^2+2k)C/2)\notag\\
&\qquad\qquad\qquad\times\sinh((t+1)(l+1)C)\sinh((s+1)(k+1)C)\notag\\
&\times\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp((\alpha {k'}^2+2\beta k'
(t+1))C/2)\{\delta(k-t-pk')-\delta(k+t+2+pk')\}\notag
\end{aligned}$$

Note that $g_{\sigma}^k(p,q;t)$ is 0, unless $k+t+pN$ is even, so $(-1)^{k+t}=(-1)^{pN}$.

So $$(-1)^{l+s}g_\sigma^l(q,p;s)(-2(r+1))=(-1)^{qN}(-1)^{pN}\times S \tag{A}$$

where $$\begin{aligned}
 &S=4\sum_{t=0}^{r-1}\sum_{k\ge 0} \exp(\epsilon(-t^2-2t+k^2+2k)C/2)\notag\\
&\qquad\cdot\sinh((t+1)(l+1)C)\sinh((s+1)(k+1)C)\notag\\
&\qquad\quad\cdot\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp((\alpha {k'}^2+2\beta k'
(t+1))C/2)\{\delta(k-t-pk')-\delta(k+t+2+pk')\}\notag\\
&=4\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \sum_{t=0}^{r-1}\exp(\alpha {k^\prime}^2C/2+\beta
k^\prime(t+1)C)\sinh((t+1)(l+1)C)\notag\\
&\qquad\cdot \sum_{k\ge 0}
\exp(\epsilon(-t^2-2t+k^2+2k)C/2)\sinh((s+1)(k+1)C)\notag\\
&\qquad\quad\cdot\{\delta(k-t-pk')-\delta(k+t+2+pk')\}\notag
\end{aligned}$$

::: lemma
Let $f(x)$ be an even function and $g(x)$ be an odd function, then $$\begin{aligned}
 &\quad\sum_{k\ge 0}f(k+1)g(k+1)\{\delta(k-t-pk')-\delta(k+t+2+pk')\}\notag\\
&=f(pk'+t+1)g(pk'+t+1)\notag
\end{aligned}$$
:::

The proof of this lemma will be given later. Now we apply it to calculate the innermost summation of $S$.---- let $$f(x)=\exp(\epsilon(-(t+1)^2+x^2)C/2)$$ and $$g(x)=\sinh((s+1)Cx),$$ we have $$\begin{aligned}
S&=4\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \sum_{t=0}^{r-1}\exp(\alpha {k'}^2C/2+\beta
k'(t+1)C)\sinh((t+1)(l+1)C)\notag\\
&\times\exp(\epsilon pk'(pk'+2t+2)C/2)\sinh((s+1)(pk'+t+1)C)\notag\\
&=4\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \sum_{t=0}^{r-1}\exp(qp{k'}^2C/2+qk'(t+1)C)\notag\\
&\times \sinh((t+1)(l+1)C)\sinh((s+1)(pk'+t+1)C)\notag\\
&=4\sum_{t=0}^{r-1}\sinh((t+1)(l+1)C)\notag\\
&\times\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(qp{k'}^2C/2+qk'(t+1)C)\sinh((s+1)(pk'+t+1)C)\notag
\end{aligned}$$

Note that $\alpha+\epsilon p^2=qp$ and $\beta+\epsilon p=q$.

::: lemma
$$\begin{aligned}
 &\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1{k'}^2+\alpha_2k')\sinh(\alpha_3k'+\zeta)\notag\\
&=\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(\alpha_1{k'}^2+\alpha_3k')\sinh(\alpha_2k'+\zeta)\notag
\end{aligned}$$
:::

Apply this lemma to the inner summation of (3.4), we have

$$\begin{aligned}
S&=4\sum_{t=0}^{r-1}\sinh((t+1)(l+1)C)\notag\\
&\times\sum_{ \substack {k'=-N\\ k'+N\ even}}^N  \exp(qp{k^\prime}^2C/2+qk'(t+1)C)\sinh(pk'(s+1)C+(s+1)(t+1)C)\notag\\
&=4\sum_{t=0}^{r-1}\sinh((t+1)(l+1)C)\notag\\
&\times\sum_{ \substack {k'=-N\\ k'+N\ even}}^N  \exp(qp{k^\prime}^2C/2+pk'(s+1)C)\sinh(qk'(t+1)C+(s+1)(t+1)C)\notag\\
&=4\sum_{ \substack {k'=-N\\ k'+N\ even}}^N  \exp(qp{k^\prime}^2C/2+pk'(s+1)C)\notag\\
&\times\sum_{t=0}^{r-1}\sinh((t+1)(l+1)C)\sinh((t+1)(qk'+s+1)C)\notag\\
&=2\sum_{ \substack {k'=-N\\ k'+N\ even}}^N  \exp(qp{k^\prime}^2C/2+pk'(s+1)C)\notag\\
&\times\sum_{t=0}^{r-1}(\cosh((t+1)(l+s+2+qk')C)-\cosh((t+1)(l-s-qk')C))\notag
\end{aligned}$$

our calculation will be done with the help of the following lemma

::: lemma
Suppose r+1 is a prime number, $\eta$ an integer, and $r+1\nmid\eta$, then $$\sum_{t=0}^{r-1}\cosh((t+1)\eta C)=-\frac{1+cos(\eta\pi)}2$$ where $C=\frac{\pi i}{r+1}$
:::

So if both $l+s+2+qk'$ and $l-s-qk'$ are nonzero, by choosing a sufficiently large prime number r+1, we have $$\sum_{t=0}^{r-1}(\cosh((t+1)(l+s+2+qk')C)-\cosh((t+1)(l-s-qk')C)=0$$

if $l+s+2+qk'=0$, then $l-s-qk'$ is nonzero, since the sum of the two is $2l+2$, which is always positive and even, in this case $$\sum_{t=0}^{r-1}(\cosh((t+1)(l+s+2+qk')C)-\cosh((t+1)(l-s-qk')C)=r-(-1)=r+1$$

if $l-s-qk'=0$, the situation is similar, and we get $$\sum_{t=0}^{r-1}(\cosh((t+1)(l+s+2+qk')C)-\cosh((t+1)(l-s-qk')C)=-1-r$$

in summary,

$$\begin{aligned}
 &\sum_{t=0}^{r-1}(\cosh((t+1)(l+s+2+qk')C)-\cosh((t+1)(l-s-qk')C))\notag\\
&=-(r+1)\{\delta (l-s-qk')-\delta (l+s+2+qk')\}\notag
\end{aligned}$$

so $$\begin{aligned}
 S&=-2\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(qp{k^\prime}^2C/2+pk'(s+1)C)\notag\\
&\times(r+1)\{\delta (l-s-qk')-\delta (l+s+2+qk')\}\notag
\end{aligned}$$

Finally from (A) and the above result we have

$$\begin{aligned}
 (-1)^{l+s}g_\sigma^l(q,p;s)&(-2(r+1))=(-1)^{qN}(-1)^{pN}\times S\notag\\
&=(-1)^{pN+qN}(-2(r+1))\sum_{ \substack {k'=-N\\ k'+N\ even}}^N \exp(qp{k^\prime}^2C/2+pk'(s+1)C)\notag\\
&\times\{\delta(l-s-qk^{'})-\delta(l+s+2+qk^{'})\}\notag
\end{aligned}$$

cancel (-2(r+1)) from both sides, we got two polynomials which are equal at infinitely many points, i.e., the primitive 4(r+1)-th root of unity, hence the two polynomials are equal. Note further that $g_\sigma^l(q,p;s)=0$ unless $l+s+qN$ is even--due to the $\delta$ function, thus one can check that the sign factor before the summation takes the form as we expected, which is $(-1)^{pN}$. And our formula for $g^{,}$s is proved. ◻
:::
