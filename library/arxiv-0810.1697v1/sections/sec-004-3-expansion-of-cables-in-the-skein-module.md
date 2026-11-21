---
doc_id: arxiv-0810.1697v1
doc_title: "ON THE CABLE EXPANSION FORMULA"
section_id: sec-004-3-expansion-of-cables-in-the-skein-module
section_title: "Expansion of cables in the skein module"
section_number: 3
pages: 5-8
source_pdf: 0810.1697v1.pdf
source_sha256: 1aef66179da3c154
toc_source: outline
text_source: latex
latex_prose_ratio: 0.989
latex_coverage_ratio: 0.968
doc_brief: "ON THE CABLE EXPANSION FORMULA — In this paper, a generalized version of Morton’s formula [8] is proved."
---
[]{#thm label="thm"} []{#thm label="thm"} In this section, the framing convention is assumed.

Let $M$ be the standard solid torus $D \times S^1$, the link $L$, which is to be considered, consists of two components: $K_1$ is given by $$( \rho \exp(iq\theta), \exp(ip\theta))|_{0\le \theta \le 2\pi}$$ where $p,q$ are coprime integers, $0<\rho<1$; $K_2$ is the core of the solid torus $$(0, \exp(i\theta))|_{0\le \theta \le 2\pi}$$ Here $D$ is identified with the unit disk in the complex plane and $S^1$ with the unit circle.

Fix the framing of $K_2$ to be 0. The framing $\sigma$ of $K_1$ corresponds to some integer. By abuse of notation, it is also denoted by $\sigma$. Denote the color of $K_1$ by $N$. Denote the color of $K_2$ by $s$. Assume they are nonnegative. $\langle e_N,e_s\rangle_L$ is some element of $S(D \times S^1)$. Denote it by $T_\sigma^N(p,q;s)$.

As an element of $S(D \times S^1)$, $T_\sigma^N(p,q;s)$ can be expressed as a linear combination of the basis elements $\{e_l\}|_{l\ge 0}$. The coefficients before $e_l$ is denoted by $g_\sigma^l(p,q;s)$, i.e. $$T_\sigma^N(p,q;s)=\sum_{l\ge 0} g_\sigma^l(p,q;s)e_l$$

Note the range of $l$ is not restricted except that $l\ge 0$. These coefficients are all 0 but for finitely many $l$'s.

First some simple cases:

1.  If (p,q)=(0,1),then it follows from the second example in 2.1.2 that with $\sigma=0$ $$g_\sigma^l(0,1;s)=\delta_{ls}(-1)^N\frac{[(N+1)(s+1)]}{[s+1]}$$.

2.  If (p,q)=(1,0), we have two parallel strings, one with color s, the other with color N. It's clear from the multiplication formula of $e_n$'s that for framing $\sigma=0$, $g_\sigma^l(1,0;s)=1$ if (l,s,N) is an admissible triple, and $g_\sigma^l(1,0;s)=0$ otherwise. By introducing the $\delta$-function, which is $\delta(0)=1$ and $\delta(m)=0$ for nonzero m, we can encode these phrases into a formula $$g_\sigma^l(1,0;s)=\sum_{ \substack {k=-N\\ k+N\ even}}^N \{\delta(l-s-k)-\delta(l+s+2+k)\}$$

3.  If we change the framing $\sigma$ of the cable, by the remark in 2.1.2, we just add an overall phase factor to each of the $g^,$s, i.e. $$g_{\sigma+b}^l(p,q;s)=(-1)^{bN}A^{b(N^2+2N)}g_\sigma^l(p,q;s)$$

4.  Since (-p,-q) represents the same cable as (p,q) does, we shall always assume $p>0$.

The approach to calculate $g^,$s for general (p,q) are quite straightforward. We start from (1,0), then calculate the case(1,q), then (q,1), then (q,$1+bq$), then ($1+bq$,q)\... Formally, we express $\frac{q}{p}$ as a continued fraction $$\frac{q}{p}=a_0+\frac{1}{a_1}\ _{+}\ \frac{1}{a_2}\ _{+}\ ...\ _{+}\ \frac{1}{a_\gamma}$$ and then use induction on $\gamma$.

This is made possible by the following two lemmas.

::: lemma
$$g_\sigma^l(p,q+p;s)=(-1)^{l+s}A^{-s^2-2s+l^2+2l}g_{\sigma^\prime}^l(p,q;s)$$
:::

::: proof
*Proof.* Since to get the (p,q+p)-cable from a (p,q)-cable, one simply apply Dehn twist once around the meridian. And it follows from the remark in 2.1.2. The phase factor appear because twisting has changed the framing of the core string of the solid torus as well. ◻
:::

Now how to make transition from (q,p) to (p,q)? We use a multi-linear bracket associated to the following link in $S^3$: $L=K_1\cup K_2\cup K_3$

 

 

 

 

$$\scalebox{.25}{\psfig{file=link-L2.eps}}$$ each component has 0 framing. Let $H$ be the Hopf link. We have $$\langle x_1,x_2, x_3\rangle_L=\langle x_1\cdot x_2,x_3\rangle_H$$ where $x_1\cdot x_2$ is the multiplication in $S(D\times S^1)$.

Let $r$ be a positive integer, and $$\omega_r=\sum_{t=0}^{r-1} (-1)^t[t+1]e_t$$ then for $r>m>0$, we have $$\langle e_m,\omega_r\rangle_H\equiv 0$$ and $$\langle e_0,\omega_r\rangle_H\equiv \langle\omega_r\rangle_U$$ where $U$ is the unknot with framing 0, equivalence means equal at $A=exp\left(\frac {\pi i}{2(r+1)}\right)$. See Lemma 13.9 from Lickorish's book [@LBook].

Thus for $r>2l\ge0,r>2k\ge0$, we have $$\begin{aligned}
\langle e_l,e_k,\omega_r\rangle_L&=\langle e_l\cdot e_k,\omega_r\rangle_H\notag\\
                       &=\sum_{\substack{m\\(k,l,m)\ admissible}}\langle e_m,\omega_r\rangle_H\notag\\
                       &\equiv \sum_{\substack{m\\(k,l,m)\ admissible}}\delta(m)\langle\omega_r\rangle_U\notag
\end{aligned}$$ Thus we have $$\langle e_l,e_k,\omega_r\rangle_L\equiv\delta(l-k)\langle\omega_r\rangle_U\tag {*}$$

Then $$\langle e_l,\ T_\sigma(p,q;s),\omega_r\rangle_L\equiv g_\sigma^l(p,q;s)\langle\omega_r\rangle_U\tag {**}$$

Let $L_1$ be the second example mentioned in 2.1.2, we have $$\langle e_l,e_t\rangle_{L_1}=(-1)^l \frac{[(l+1)(t+1)]}{[t+1]} e_t$$ Map $D \times S^1$ to a tubular neighborhood of $K_3$, we have $$\begin{aligned}
 \langle e_l,\ T_\sigma(p,q;s),\omega_r\rangle_L&=\langle T_\sigma(p,q;s),\langle e_l,\omega_r\rangle_{L_1}\rangle_H\notag\\
&=\langle T_\sigma(p,q;s),\ \sum_{t=0}^{r-1}
(-1)^t[t+1]\langle e_l,e_t\rangle_{L_1}\rangle_H\notag\\
&=\langle T_\sigma(p,q;s),\ \sum_{t=0}^{r-1} (-1)^{l+t}[(t+1)(l+1)]
e_t\rangle_H\tag {***}
\end{aligned}$$

 

 

 

 

$$\scalebox{.25}{\psfig{file=link-L3.eps}} =
\scalebox{.25}{\psfig{file=link-L4.eps}}$$

Now we can go on. We have a link $T_\sigma(p,q;s)$ in the tubular neighborhood $N(K_2)$ of the second component $K_2$ of L, which consists of a string at the core of the solid torus, surrounded by a (p,q)-cable. Let's push this (p,q)-cable off to the boundary, and push it a little further so that it slides into the world on the other side of the boundary torus. Observe that $S^3-N(K_2)$ is still a solid torus, since $K_2$ is the unknot. The meridian of the $N(K_2)$ becomes a longitude when viewed from the other side, and the longitude we chose becomes a meridian of $S^3-N(K_2)$. And we push the cable further into $N(K_3)$, then the (p,q)-cable becomes (q,p)-cable in $N(K_3)$.

So $$\langle T_\sigma(p,q;s),\ \sum_{t=0}^{r-1} (-1)^{l+t}[(t+1)(l+1)]e_t\rangle_H=\langle e_s,\ \sum_{t=0}^{r-1}  (-1)^{l+t}[(t+1)(l+1)]
T_{\sigma}(q,p;t)\rangle_H\tag {****}$$ Then we expand $T_{\sigma}(q,p;t)$ on the right hand side, note that $$\langle e_s,e_k\rangle_H=(-1)^{s+k}[(s+1)(k+1)]$$ in this way get a relation between $g_\sigma^l(p,q;s)$ and $g_{\sigma}^k(q,p;t)$.

We summarize (\*\*),(\*\*\*),(\*\*\*\*) into the following lemma.

::: lemma
$$\begin{aligned}
 (-1)^{l+s}&g_\sigma^l(p,q;s)\langle\omega_r\rangle\notag\\
&\equiv \sum_{t=0}^{r-1}\sum_{k\ge 0} (-1)^{k+t}g_{\sigma}^k(q,p;t)[(t+1)(l+1)][(s+1)(k+1)]\notag
\end{aligned}$$ here equivalence means equal at $A=exp\left(\frac {\pi i}{2(r+1)}\right)$. Note that in this formula $g(p,q)$ and $g(q,p)$ have the same framing.
:::

Using the two lemmas and the formula for (p,q)=(1,0), we can now write down the general formula for $g^,$s.

::: theorem
Assume $p>0$,let $\epsilon, \beta, \alpha$ be such that $\epsilon=[\frac{q}{p}]$, $q=\epsilon p+\beta$ with $0\le \beta<p$, $\alpha=p\cdot\beta$.Then for framing $\sigma=pq$, we have $$\begin{aligned}
 g_\sigma^l(p,q;s)&=(-1)^{qN} A^{\epsilon
(-s^2-2s+l^2+2l)}\notag\\
&\times\sum_{ \substack {k=-N\\ k+N\ even}}^N A^{\alpha {k}^2+2\beta k
(s+1)}\{\delta(l-s-pk)-\delta(l+s+2+pk)\}\notag
\end{aligned}$$
:::

It seems to be complicated. But note there're at most two nonzero terms in this summation. Since for each value of $k$, the summand is nonzero only if $l-s-pk=0$ or $l+s+2+pk=0$.

::: theorem
Substitute the expression for $g$'s to the expansion of $T_\sigma(p,q;s)$, we have $$T_\sigma(p,q;s)=(-1)^{qN}\sum_{ \substack {k=-N\\ k+N\ even}}^N A^{pqk^2+2qk(s+1)} e_{pk+s}$$
:::

::: proof
*Proof of theorem 2.* Substitute the expression for $g$'s, then change the order of summation. Also note that $e_l=-e_{-l-2}$ and $e_{-1}=0$. ◻
:::
