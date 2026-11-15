---
doc_id: arxiv-1203.6531v1
doc_title: "Groebner-Shirshov basis and reduced words for affine Weyl group A_n"
section_id: sec-002-3-counting-reduced-words
section_title: "Counting Reduced Words"
section_number: 3
pages: 7-10
source_pdf: 1203.6531v1.pdf
source_sha256: 29541f28c1c62d8f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.905
doc_brief: "Groebner-Shirshov basis and reduced words for affine Weyl group A_n — Using Buchberger-Shirshov Algorithm and Composition-Diamond lemma we obtain the reduced Gr¨obner-Shirshov bases of f An and"
---
::: thm
[]{#reduced label="reduced"} Let $\widehat{w}=a_{i_{s}}a_{i_{s-1}}\ldots a_{i_{1}}v^{(b_t)}$ where $a_{i_{j}}=r_{0}r_{nk_{j}}r_{nl_{j}}$.Then $a_{i_{j}}$'s are marked components of an arranged word $w=uv^{(b_t)}$ where $b_t=r_0r_{np}r_{1q}$ if and only if $k_{s}<k_{s-1}<\ldots<k_{1}<p$ and $q<l_{1}<l_{2}<\ldots<l_{s}<n$
:::

::: proof
*Proof.* By construction of arranged words, the marked components satisfy the given conditions. Conversely, if $\widehat{w}=a_{i_{s}}a_{i_{s-1}}\ldots a_{i_{1}}v^{(b_t)}$ is a word satisfying the conditions, then an arranged word $(w=u v^{(b_{t})})$ whose marked components are $a_{i_j}$'s can be obtained as follows:

The components up to $r_0r_{nk_s}r_{1l_s}$ are $$(r_{0}r_{n2}r_{1n})\cdots(r_{0}r_{nk_{s}}r_{1n})(r_{0}r_{nk_{s}}r_{1,n-1})\cdots(r_{0}r_{nk_{s}}r_{1l_{s}}),$$ the components between $(r_{0}r_{nk_{j}}r_{1l_{j}})$ and $(r_{0}r_{nk_{j-1}}r_{1l_{j-1}})$ are $$(r_{0}r_{nk_{j}}r_{1l_{j}})\cdots(r_{0}r_{nk_{j-1}r_{1l_{j}}})(r_{0}r_{nk_{j-1}}r_{1,l_{j}-1})\cdots(r_{0}r_{nk_{j-1}}r_{1l_{j-1}})$$ and the last part of the word$w=u v^{(b_{t})}$ is $$(r_{0}r_{nk_{2}}r_{1l_{2}})\cdots(r_{0}r_{nk_{1}r_{1l_{2}}})(r_{0}r_{nk_{1}}r_{1,l_{2}-1})\cdots(r_{0}r_{nk_{1}}r_{1l_{1}})(v^{(b_{t})}).$$ ◻
:::

Therefore the number of the elements in an arranged word $w=u v^{(b_t)}$ given by the generating function $$\frac{x^\alpha}{(1-x^{2n})(1-x^{2n-1})\cdots (1-x^{n+1})}$$ where $\alpha$ is the length of the word $\widehat{w}$. In order to count all reduced words starting with $r_0$ we have to find the number words $\widehat{w}$ whose length is $\alpha$ for any power $\alpha$. To do this, we will find a correspondence between these words and some special partitions of integers.

If $m$ is a positive integer, then a partition of $m$ is a nonincreasing sequence of positive integers $p_{1},p_{2},\ldots,p_{k}$ whose sum is $m$. Each $p_{i}$ is called a part of the partition. Let $n$ be a positive integer. Any partition $m=d_{1}+d_{2}+\ldots+d_{k}$ where $k\leq n$ can be identify by the $n-$tuple $(d_{1},d_{2},\ldots,d_{k},0,0,\ldots,0)$.

We can also represent each word $r_0r_{nk}r_{1l}$ with the n-tuple $(k,1,\ldots,1,0,\ldots,0)$, $r_{nk}$ with $(k,\ldots,0)$ and $r_{0l}$ with $(1,1\ldots,1,0,\ldots,0)$ where number one 1's is equal to $l$ for $2 \leq k \leq n-1, 1 \leq l \leq n$.

::: defn
Let $n$ be a positive integer. The $n$-tuples $(k,1\ldots,1,0,\ldots,0)$ where number of 1's is $l$ for $1\leq k\leq n$, $1\leq l\leq n-1$ are called basic partitions. The basic partition $(k_{1},1\ldots,1,0\ldots,0)$ is said to be connected to the basic partition $(k_{2},1,\ldots,1,0,\ldots,0)$ if $k_{1}>k_{2}$ and the number of 1's in the first one is greater than number of 1's in the second one. Hence a sequence of connected partition $a_{1},a_{2},\ldots,a_{m}$ corresponds to a word $\widehat{w}$ given in Theorem [\[reduced\]](#reduced){reference-type="ref" reference="reduced"}.
:::

::: thm
[]{#qbinomial label="qbinomial"} There is one to one correspondence between words $\widehat{w}$ and the partitions in which there are at most $n$ parts and in which no parts is larger than $n$.
:::

::: proof
*Proof.* Since we identify each word $\widehat{w}$ with a sequence of connected basic partitions, we must find a correspondence between sequences of connected partitions and the partitions fit into a box of size $n \times n$. Let $a_{1},a_{2},\ldots,a_{m}$ be a sequence of connected partitions where $a_{i}=(k_{i},\underaccent{l_{i}}{\underbrace{1,\ldots,1}}0,\ldots,0)$. Hence $k_{i}>k_{j}$ and $l_{i}>l_{j}$ for $1 \leq i < j\leq m$.

Define $$\bigoplus_{i=1}^{m}a_{i}=\sum_{i=1}^{m}\sigma_{1}^{i-1}(a_{i})$$

where $\sigma(p_{1},p_{2},\ldots,p_{n-1},p_{n})=(p_{n},p_{1},p_{2},\ldots,p_{n-1})$. Then

$$\bigoplus_{i=1}^{m}a_{i}=(k_{1},k_{2}+1,\ldots,k_{m}+m-1,\underaccent{l_{m}}{\underbrace{m,\ldots,m}},
 \underaccent{l_{m-1}-(l_{m}+1)}{\underbrace{m-1,\ldots,m-1}},\ldots,\underaccent{l_{1}-(l_{2}+1)}{\underbrace{1,\ldots,1}},0\ldots,0)$$

We prove the last equation by induction on $m$.

Let $m=2$, Since $l_1 -1 \geq l_2$,

$$\begin{aligned}

  a_{1}\oplus a_{2} &=& (k_{1},\underaccent{l_{1}}{\underbrace{1,\ldots,1}},0,\ldots,0)+(0,k_{2},\underaccent{l_{2}}{\underbrace{1,\ldots,1}},0,\ldots,0)  \\
 &=& (k_{1},k_{2}+1,\underaccent{l_{2}}{\underbrace{2,\ldots,2}},\underaccent{l_{1}-(l_{2}+1)}{\underbrace{1,\ldots,1}},0,\ldots,0)
\end{aligned}$$

Let us assume that $$\bigoplus_{i=1}^{m-1}a_{i}=(k_{1},k_{2}+1,\ldots,k_{m-1}+m-2,\underaccent{l_{m-1}}{\underbrace{m-1,\ldots,m-1}},\ldots,\underaccent{l_{1}-(l_{2}+1)}{\underbrace{1,\ldots,1}},0,\ldots,0).$$

$$\begin{aligned}

  \bigoplus_{i=1}^{m}a_{i} &=& \sum_{i=1}^{m}\sigma^{i-1}(a_{i}) \\
   &=& \sum_{i=1}^{m-1}\sigma^{i-1}(a_{i})+\sigma^{m-1}(a_{m})  \\
   &=& \bigoplus_{i=1}^{m-1}a_{i}+\sigma^{m-1}(a_{m}) \\
   &=& (k_{1},k_{2}+1,\ldots,k_{m-1}+m-2,\underaccent{l_{m-1}}{\underbrace{m-1,\ldots,m-1}},\ldots,\underaccent{l_{1}}{\underbrace{1,\ldots,1}},0,\ldots,0) \\
   &&  + \: (\underaccent{m-1}{\underbrace{0,0,\ldots,0}},k_{m},\underaccent{l_{m}}{\underbrace{1,\ldots,1}},0,\ldots,0) \\
   &=& (k_{1},k_{2}+1,\ldots,k_{m}+m-1,\underaccent{l_{m}}{\underbrace{m,\ldots,m}},\ldots,\underaccent{l_{1}-(l_{2}+1)}{\underbrace{1,\ldots,1}},0,\ldots,0)
\end{aligned}$$

The last equality easily follows from the fact $l_{m-1}-1 \geq l_{m}$. Since $n \geq k_1 \geq k_2+1 \geq \cdots > k_{m}+(m-1) \geq m$, the last line corresponds to a partition of $2n$ fits into a $n$ by $n$ box.

Conversely let $m=(m_1,m_2,\ldots,m_n)$ be a partition where $n \geq m_1 \geq m_2 \geq \cdots \geq m_n \geq 0$. If $i_1$ is the last index such that $m_{i_1} \neq 0$, then let $a_1=(m_1,1,\ldots,1,0,\ldots0)$ where the last $1$ in $i_1$-th position. Then let $$x=\sigma^{-1}(m-a_1)=(m_2-1,\ldots,m_{i_1}-1, 0,\ldots,0)$$ and $a_2=(m_2-1,\ldots,1,0,\ldots,0)$ where the position of the last nonzero element in $x$ and the position of last $1$ in $a_2$ are same. Clearly, $a_1$ and $a_2$ are basic partitions and $a_1$ is connected to $a_2$. Continuing the process until reaching the $(0,\ldots,0)$, one can obtain a sequence of connected basic partitions. ◻
:::

::: defn
Let be positive integers. The q-binomial is defined by $$\left(
  \begin{array}{c}
    m \\
    r \\
  \end{array}
\right)_q=\frac{(1-q^m)(1-q^{m-1}) \cdots (1-q^{m-r+1})}{(1-q)(1-q^2) \cdots (1-q^r)}$$
:::

Although the formula in the first clause appears to involve a rational function, it actually designates a polynomial, because the division is exact in $\mathbb{Z}[q]$. A standard combinatorial interpretation for q-binomial is that it counts the number of partitions that will fit into a box of size $k \times (n - k)$, weighted by the size of the partition. In particular the q-binomial $$\left(
  \begin{array}{c}
    2n \\
    n \\
  \end{array}
\right)_x
=\frac{(1-x^{2n})(1-x^{2n-1}) \cdots (1-x^{n+1})}{(1-x)(1-x^2) \cdots (1-x^{n})}$$ counts the number of partitions in which there are at most $n$ parts and in which no parts is larger than $n$.

Now, we can proof the main result of this paper.

::: thm
Then the reduced Gröbner-Shirshov basis of the affine Weyl group $\widetilde{A}_n$ is the set $G'$. Moreover all the reduced words are the form $rw$ where $r$ is a reduced word not including $r_0$ and $w$ is a arranged word.
:::

The reduced words not including $r_0$ is given in Lemma [\[ri\]](#ri){reference-type="ref" reference="ri"}. It is easy to see that the number of such words given by the generating function $$(1+x)(1+x+x^2)\cdots(1+x+ \cdots +x^n).$$ Theorem [\[reduced\]](#reduced){reference-type="ref" reference="reduced"} and Theorem [\[qbinomial\]](#qbinomial){reference-type="ref" reference="qbinomial"} imply that the number of arranged words given by the generating function

$$\begin{aligned}

  \frac{\left(
  \begin{array}{c}
    2n \\
    n \\
  \end{array}
\right)_x}{(1-x^{2n})(1-x^{2n-1})\cdots (1-x^{n+1})} &=& \frac{\frac{(1-x^{2n})(1-x^{2n-1}) \cdots (1-x^{n+1})}{(1-x)(1-x^2) \cdots (1-x^{n})}}{(1-x^{2n})(1-x^{2n-1})\cdots (1-x^{n+1})} \\
   &=& \frac{1}{(1-x)(1-x^2)\cdots(1-x^n)}.
\end{aligned}$$

By Lemma [\[rir0\]](#rir0){reference-type="ref" reference="rir0"}, the reduced words of $\widetilde{A}_n$ are in the form $rw$. Hence the number of reduced words given by the generating function $$\frac{(1+x)(1+x+x^2)\cdots(1+x+ \cdots +x^n)}{(1-x)(1-x^2)\cdots(1-x^n)}$$ which is well known Poincaré polynomial of the affine Weyl group $\widetilde{A}_n$. (see [@humphreys]). Therefore these are all reduced words of $\widetilde{A}_n$. Hence by Composition-Diamond Lemma, $G'$ is a Gröbner-Shirshov basis of $\widetilde{A}_n$. In fact, $G'$ is a reduced Gröbner-Shirshov basis.
