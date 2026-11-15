---
doc_id: arxiv-math-0503227v2
doc_title: "An Inductive Proof of the Berry-Esseen Theorem for Character Ratios Running head: Berry-Esseen Theorem for Character Ratios"
section_id: sec-002-3-central-limit-theorem-for-jack-measure
section_title: "Central limit theorem for Jack measure"
section_number: 3
pages: 9-13
source_pdf: 0503227v2.pdf
source_sha256: 4e83adfdef827103
toc_source: outline
text_source: latex
latex_prose_ratio: 0.982
latex_coverage_ratio: 1.0
doc_brief: "An Inductive Proof of the Berry-Esseen Theorem for Character Ratios Running head: Berry-Esseen Theorem for Character Ratios — Bolthausen used a variation of Stein’s method to give an inductive proof"
---
[]{#jack label="jack"}

For $\alpha>0$ the Jack$_{\alpha}$ measure on partitions of size $n$ chooses a partition $\lambda$ with probability $$\frac{\alpha^n n!}{\prod_{x \in \lambda} (\alpha a(x) + l(x) +1)
(\alpha a(x) + l(x) + \alpha)},$$ where the product is over all boxes in the partition. Here $a(x)$ denotes the number of boxes in the same row of $x$ and to the right of $x$ (the "arm" of x) and $l(x)$ denotes the number of boxes in the same column of $x$ and below $x$ (the "leg" of x). For example the partition of 5 below $$\begin{array}{c c c} \framebox{\ }& \framebox{\ }& \framebox{\ } \\
\framebox{\ }& \framebox{\ }& \end{array}$$ would have Jack$_{\alpha}$ measure $$\frac{30 \alpha^2}{(3 \alpha+1) (\alpha+2)(2
\alpha+1)(\alpha+1)^2}.$$ Note that when $\alpha=1$, Jack measure reduces to Plancherel measure of the symmetric group. The papers [@O2], [@BO1] emphasize that for $\alpha$ fixed the study of Jack$_{\alpha}$ measure is an important open problem, about which relatively little is known for general values of $\alpha$. It is a discrete analog of eigenvalue ensembles from random matrix theory and like Jack polynomials [@GHJ], should also be relevant to the moduli space of curves.

Given $\alpha>0$, the quantity to be studied is $$T_{n,\alpha}(\lambda) = \frac{\sum_i (\alpha {\lambda_i
    \choose 2} - {\lambda_i' \choose 2})}{\sqrt{ \alpha {n \choose
    2}}},$$ where as usual $\lambda_i$ is the length of the ith row of $\lambda$ and $\lambda_i'$ is the length of the ith column of $\lambda$. It is of interest to study the quantity $T_{n,\alpha}(\lambda)$ under Jack measure for several reasons. When $\alpha=1$ it reduces to the study of the character ratio of transpositions under Plancherel measure. When $\alpha=2$ it is a spherical function of the Gelfand pair $(S_{2n},H_{2n})$ where $H_{2n}$ is the hyperoctahedral group of size $2^nn!$. Also by Corollary 1 of [@DHol], there is a natural random walk on perfect matchings of the complete graph on $n$ vertices, whose eigenvalues are precisely $\frac{T_{n,2}(\lambda)}{\sqrt{n(n-1)}}$, occurring with multiplicity proportional to the Jack$_2$ measure of $\lambda$.

The paper [@F2] used the "exchangeable pairs" version of Stein's method to prove a central limit theorem for $T_{n,\alpha}$ with error term $C_{\alpha} n^{-1/4}$ where $C_{\alpha}$ is a constant depending on $\alpha$. This was sharpened in [@F3] using martingales to $C_{\alpha,s}
    n^{-s}$ for any $s<\frac{1}{2}$.

The main result of this section is Theorem [\[main2\]](#main2){reference-type="ref" reference="main2"}.

::: theorem
[]{#main2 label="main2"} Suppose that $\alpha \geq 1$ and let $\lambda$ be chosen from the Jack$_{\alpha}$ measure on partitions of size $n$. Then there is a constant $C_{\alpha}$ depending on $\alpha$ so that for all $n \geq 2$ and real $x_0$, $$\left| \pp \left( T_{n,\alpha}(\lambda) \leq x_0
    \right) - \frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x_0} e^{-
    \frac{t^2}{2}} dt \right| \leq C_{\alpha} n^{-1/2}.$$
:::

Note that in Theorem [\[main2\]](#main2){reference-type="ref" reference="main2"} we suppose that $\alpha \geq
    1$ since the Jack$_{\alpha}$ probability of $\lambda$ is equal to the Jack$_{\frac{1}{\alpha}}$ probability of the transpose of $\lambda$, implying that for any $x$, the Jack$_{\alpha}$ probability that $T_{n,\alpha}=x$ is equal to the Jack$_{\frac{1}{\alpha}}$ probability that $T_{n,\frac{1}{\alpha}}=-x$. Also note that $C_{\alpha}$ must depend on $\alpha$, since by Corollary 5.3 of [@F2], the random variable $T_{n,\alpha}$ has mean 0, variance 1, and third moment $\frac{\alpha-1}{\sqrt{\alpha {n \choose 2}}}$.

There is no need to write out a proof of Theorem [\[main2\]](#main2){reference-type="ref" reference="main2"}, which uses exactly the same logic as that of Theorem [\[main1\]](#main1){reference-type="ref" reference="main1"}. But it is necessary to give analogs of Lemmas [\[ismart\]](#ismart){reference-type="ref" reference="ismart"}, [\[moments\]](#moments){reference-type="ref" reference="moments"}, [\[identity\]](#identity){reference-type="ref" reference="identity"}, and [\[boundmom\]](#boundmom){reference-type="ref" reference="boundmom"}, and we do that. The concentration inequality needed for $X_{n,\alpha}$ is Lemma 6.6 of [@F2] and can be used to give another proof of some results in this section.

There is an $\alpha$-analog of Kerov's growth process (due to Kerov [@K4]) giving a sequence of partitions $(\lambda(1),\cdots,\lambda(n))$ with $\lambda(j)$ distributed according to the Jack$_{\alpha}$ measure on partitions of size $j$; see [@F3] for details. Moreover from the definition of $T_{n,\alpha}$, it follows that $$T_{n,\alpha} =
\frac{1}{\sqrt{\alpha {n \choose 2}}} (X_{1,\alpha} + \cdots +
X_{n,\alpha}).$$ Here $X_{1,\alpha}=0$ and if $j \geq 2$ then $X_{j,\alpha}=c_{\alpha}(x)$ where $x$ is the box added to $\lambda(j-1)$ to obtain $\lambda(j)$ and the "$\alpha$-content" $c_{\alpha}(x)$ of a box $x$ is defined to be $\alpha$ (column number of x-1) - (row number of x-1).

Lemma [\[ismart2\]](#ismart2){reference-type="ref" reference="ismart2"} is an analog of Lemma [\[ismart\]](#ismart){reference-type="ref" reference="ismart"} and is generalized in [@F3] to arbitrary spherical functions of the Gelfand pair $(S_{2n},H_{2n})$.

::: lemma
[]{#ismart2 label="ismart2"} ([@F3])

1.  $\ee(X_{j,\alpha}|\lambda(j-1))=0$ for $2 \leq j \leq n$ and all partitions $\lambda(j-1)$.

2.  $\ee(X_{j,\alpha}|T_{n,\alpha})=\frac{(j-1) \sqrt{\alpha}}{\sqrt{ {n \choose 2}}} T_{n,\alpha}$ for all $1 \leq j \leq n$.

3.  $\ee(X_{j,\alpha}^2) = \alpha(j-1)$.

4.  $\ee(T_{n,\alpha}^2) = 1$.
:::

Lemma [\[moments2\]](#moments2){reference-type="ref" reference="moments2"} is the $\alpha$ version of Lemma [\[moments\]](#moments){reference-type="ref" reference="moments"}.

::: lemma
[]{#moments2 label="moments2"} Let $\lambda(j-1)$ be a partition of size $j-1 \geq 1$.

1.  ([@K4]) $\ee(X_{j,\alpha}^2|\lambda(j-1))= \alpha(j-1)$.

2.  ([@La]) $$\begin{aligned}
     \ee(X_{j,\alpha}^4|\lambda(j-1)) & = & \alpha^2 {j \choose 2} + \alpha(\alpha-1)^2(j-1) + 3 \alpha \sum_{x \in \lambda(j-1)} c_{\alpha}(x)^2 \\  & & + 3\alpha(\alpha-1) \sum_{x \in \lambda(j-1)} c_{\alpha}(x). 
    \end{aligned}$$
:::

Lemma [\[identity2\]](#identity2){reference-type="ref" reference="identity2"} is the $\alpha$ version of Lemma [\[identity\]](#identity){reference-type="ref" reference="identity"}. The proof is combinatorial, as opposed to the algebraic argument given for Lemma [\[identity\]](#identity){reference-type="ref" reference="identity"}.

::: lemma
[]{#identity2 label="identity2"} Consider the Jack$_{\alpha}$ measure on partitions of size $n$.

1.  If $m \geq 1$ is an integer then $$\ee \left( \prod_{x \in \lambda} (m+c_{\alpha}(x)) \right) = m^n.$$

2.  Let $e_{r,\alpha}(\lambda)$ denote the $r$th elementary symmetric function of the $\alpha$-contents of the boxes of $\lambda$. Then $\ee(e_{r,\alpha}(\lambda))=0$ for $1 \leq r \leq n$.
:::

::: proof
*Proof.* It suffices to prove the first assertion since the second assertion follows from the first by taking the coefficient of $m^{n-r}$ on both sides. Page 324 of [@Mac] proves the identity $$\sum_{\lambda}
 b_{\lambda}(q,t) P_{\lambda}(y;q,t) P_{\lambda}(z;q,t) = e^{ \sum_{n
 \geq 1} ( \frac{1}{n} \frac{1-t^n}{1-q^n} p_n(y) p_n(z))}$$ where the sum is over all $\lambda$ of all sizes, $P_{\lambda}(y;q,t)$ denotes a Macdonald symmetric function, $p_n(y) = \sum_i y_i^n$ denotes the nth power sum symmetric function, and $b_{\lambda}(q,t)$ is a number to be discussed more below. We apply the homomorphism of the ring of symmetric functions determined by $p_r(y) \mapsto mu^r$, $p_r(z)
 \mapsto l^{1-r}$ for all $r \geq 1$ where $m,l$ are positive integers; this is possible since the $p_r$'s are algebraically independent. Then we take the limit $q=t^{\alpha},t \mapsto 1$ in which Macdonald polynomials become Jack polynomials.

With these substitutions, consider the left hand side of the identity. By pages 380 and 381 of [@Mac], $$b_{\lambda}(q,t) \mapsto \prod_{x \in \lambda} \frac{\alpha
        a(x) + l(x)+1}{\alpha a(x) + l(x) + \alpha}$$ $$P_{\lambda}(y;q,t) \mapsto u^{|\lambda|} \prod_{x \in
        \lambda} \frac{m+c_{\alpha}(x)}{\alpha a(x) + l(x)+1}$$ $$P_{\lambda}(z;q,t) \mapsto \frac{1}{l^{|\lambda|}} \prod_{x
        \in \lambda} \frac{l+c_{\alpha}(x)}{\alpha a(x) + l(x)
        +1}.$$ Letting $l \rightarrow \infty$, one sees that the coefficient of $u^n$ in the left-hand side of the identity is $\frac{1}{\alpha^n n!} \ee \left( \prod_{x \in \lambda}
        (m+c_{\alpha}(x)) \right)$.

Consider the right hand side of the identity with these substitutions. One obtains $e^{\sum_{n \geq 1}
        (\frac{mu^n}{n \alpha l^{n-1}})}$. Letting $l \rightarrow \infty$, one obtains $e^{\frac{mu}{\alpha}}$, and taking the coefficient of $u^n$ gives $\frac{m^n}{\alpha^n
        n!}$. Comparing with the previous paragraph proves the first assertion of the lemma. ◻
:::

Finally, we give the analog of Lemma [\[boundmom\]](#boundmom){reference-type="ref" reference="boundmom"}.

::: lemma
[]{#boundmom2 label="boundmom2"} Suppose that $n \geq 3$. There is a constant $D_{\alpha}$ such that

1.  $\ee(|X_{n,\alpha}|^3) \leq D_{\alpha} n^{3/2}$.

2.  $\ee(|T_{n-1,\alpha}||X_{n,\alpha}|^3) \leq D_{\alpha} n^{3/2}$.
:::

::: proof
*Proof.* The proof method is the same as that of Lemma [\[boundmom\]](#boundmom){reference-type="ref" reference="boundmom"}, using the Cauchy-Schwarz inequality in the first part and the conditional Cauchy-Schwarz inequality in the second part. One uses that $\ee (X_{n,\alpha}^2|\lambda(n-1))=\alpha(n-1)$ for all $\lambda(n-1)$ (part 1 of Lemma [\[moments2\]](#moments2){reference-type="ref" reference="moments2"}). Also one needs that $$\begin{aligned}
\ee(X_{n,\alpha}^4) & = & \alpha^2 {n \choose 2} +
\alpha(\alpha-1)^2(n-1) + 3 \alpha \ee \left( \sum_{x \in
\lambda(n-1)} c_{\alpha}(x)^2 \right)\\ & = & \alpha^2 {n \choose 2} +
3 \alpha^2 {n-1 \choose 2} + \alpha(\alpha-1)^2(n-1). 
\end{aligned}$$ The first equality used part 2 of Lemma [\[moments2\]](#moments2){reference-type="ref" reference="moments2"} and the fact that $\ee(T_{n-1,\alpha}) = 0$. The second equality used part 4 of Lemma [\[ismart2\]](#ismart2){reference-type="ref" reference="ismart2"} and Lemma [\[identity2\]](#identity2){reference-type="ref" reference="identity2"} with $r=2$. ◻
:::
