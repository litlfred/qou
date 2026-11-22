---
doc_id: arxiv-math-0503227v2
doc_title: "An Inductive Proof of the Berry-Esseen Theorem for Character Ratios Running head: Berry-Esseen Theorem for Character Ratios"
section_id: sec-001-2-central-limit-theorem-for-plancherel-measure
section_title: "Central limit theorem for Plancherel measure"
section_number: 2
pages: 3-9
source_pdf: 0503227v2.pdf
source_sha256: 4e83adfdef827103
toc_source: outline
text_source: latex
latex_prose_ratio: 0.977
latex_coverage_ratio: 1.0
doc_brief: "An Inductive Proof of the Berry-Esseen Theorem for Character Ratios Running head: Berry-Esseen Theorem for Character Ratios — Bolthausen used a variation of Stein’s method to give an inductive proof"
---
[]{#plancherel label="plancherel"}

The random variable we wish to study is $T_n(\lambda) =
    \frac{\sqrt{n \choose 2} \chi^{\lambda}(12)}{dim(\lambda)}$ where $\lambda$ is chosen from the Plancherel measure of the symmetric group $S_n$. To begin we write $T_n$ as a sum of other random variables. For this we need Kerov's growth process on partitions [@K2]; this has a natural generalization to arbitrary finite groups [@F3], but we only recall it in the case of interest. Given a partition $\lambda(j)$ of size $j$, one obtains a partition $\lambda(j+1)$ of size $j+1$ by choosing $\lambda(j+1)$ with probability $\frac{dim(\lambda(j+1))}{(j+1) dim(\lambda(j))}$ if $\lambda(j+1)$ can be obtained from $\lambda(j)$ by adding a single box, and with probability 0 otherwise. Thus starting from $\lambda(1)$, the unique partition of size $1$, one obtains a random sequence $(\lambda(1),\cdots,\lambda(n))$ of partitions. Kerov [@K2] proves that each $\lambda(j)$ is distributed according to the Plancherel measure of $S_j$.

Given Kerov's growth process, one can write $T_n =
    \frac{1}{\sqrt{{n \choose 2}}} (X_1+ \cdots +X_n)$ where $X_1=0$, $\chi^{\lambda(1)}(12)$ is defined as 0, and $$X_j=
    \frac{{j \choose 2} \chi^{\lambda(j)}(12)}{dim(\lambda(j))} -
    \frac{{j-1 \choose 2}
    \chi^{\lambda(j-1)}(12)}{dim(\lambda(j-1))}$$ for $j \geq 2$.

Lemma [\[ismart\]](#ismart){reference-type="ref" reference="ismart"} states that the $X_j$ are martingale differences satisfying special properties. We remark that [@F3] extends this lemma to more general conjugacy classes and groups. The notation $\ee(A|\cdot)$ means the expected value of $A$ given $\cdot$.

::: lemma
[]{#ismart label="ismart"} ([@F3])

1.  $\ee(X_j|\lambda(j-1))=0$ for $2 \leq j \leq n$ and all partitions $\lambda(j-1)$.

2.  $\ee(X_j|T_n)=\frac{j-1}{\sqrt{{n \choose 2}}} T_n$ for all $1
    \leq j \leq n$.

3.  $\ee(X_j^2) = j-1$.

4.  $\ee(T_n^2) = 1$.
:::

Frobenius [@Fr] found the following explicit formula for the character ratio of the symmetric group on transpositions: $$\frac{\chi^{\lambda}(12)}{dim(\lambda)} = \frac{1}{{n \choose
    2}} \sum_i \left({\lambda_i \choose 2} - {\lambda_i' \choose
    2} \right)$$ where $\lambda_i$ is the length of row $i$ of $\lambda$ and $\lambda_i'$ is the length of column $i$ of $\lambda$. From his formula it follows that $X_j = c(x)$ where $x$ is the box added to $\lambda(j-1)$ to obtain $\lambda(j)$ and the "content" $c(x)$ of a box is defined as column number of box - row number of box.

Lemma [\[moments\]](#moments){reference-type="ref" reference="moments"} gives the conditional second and fourth moments of the $X_j$'s. We emphasize that these were not derived or even stated in terms of character ratios, but rather were proved in a completely combinatorial way by studying the behavior of the moments of $c(x)$ where $x$ is the box added during Kerov's growth process. We remark that for other conjugacy classes, there is not an analog of the fact that $\ee(X_j^2|\lambda(j-1))$ is independent of $\lambda(j-1)$.

::: lemma
[]{#moments label="moments"} Let $\lambda(j-1)$ be a partition of size $j-1 \geq 1$.

1.  ([@K3]) $\ee(X_j^2|\lambda(j-1)) = j-1$.

2.  ([@La]) $\ee(X_j^4|\lambda(j-1)) = {j \choose 2} + 3 \sum_{x
    \in \lambda(j-1)} c(x)^2$.
:::

Lemma [\[identity\]](#identity){reference-type="ref" reference="identity"} is a useful identity. Although a combinatorial proof can be given using properties of Schur functions, we defer combinatorial arguments to the more general setting of Jack polynomials in Section [\[jack\]](#jack){reference-type="ref" reference="jack"} and give an algebraic proof.

::: lemma
[]{#identity label="identity"} Let $e_r(z_1,\cdots,z_n)= \sum_{1 \leq i_1<\cdots < i_r \leq n}
z_{i_1} \cdots z_{i_r}$ be the rth elementary symmetric function of $z_1,\cdots,z_n$. For $\lambda$ a partition of $n$, let $e_r(\lambda)$ denote the rth elementary symmetric function of the contents of the boxes of $\lambda$. Then $\ee(e_r(\lambda))=0$ for $1
\leq r \leq n$.
:::

::: proof
*Proof.* If $r=n$ the result is clear since the box in the first row and column of $\lambda$ has content 0, so that $e_n(\lambda)=0$ for all $\lambda$.

For $1 \leq r <n$, we use the theory of Murphy elements [@Mu]; a friendly reference giving background on these elements is [@DG]. For $2 \leq i \leq n$, the ith Murphy element is defined as the sum of transpositions $R_i = \sum_{1 \leq j < i}
 (j,i)$. Let $z$ be the element of the group algebra of $S_n$ which is the sum of all permutations with $n-r$ cycles. By Proposition 2.1 of [@DG], $z$ is the rth elementary symmetric function of the elements $R_2,\cdots,R_n$.

Since the elements $R_2,\cdots,R_n$ are simultaneously diagonalizable in every irreducible representation of the symmetric group, it follows from Murphy's determination of their eigenvalues that in the representation of $S_n$ parameterized by $\lambda$, $z$ is a scalar multiple of the $dim(\lambda) \times dim(\lambda)$ identity matrix with scalar equal to $e_r(\lambda)$. In the regular representation of $S_n$ the irreducible representation parameterized by $\lambda$ occurs with multiplicity $dim(\lambda)$. Hence the trace of $z$ in the regular representation is $n! \ee(e_r(\lambda))$. But the coefficient of the identity in $z$ is 0, so the trace of $z$ in the regular representation is 0, implying the result. ◻
:::

Lemma [\[boundmom\]](#boundmom){reference-type="ref" reference="boundmom"} gives upper bounds for $\ee(|X_n|^3)$ and for $\ee(|T_{n-1}||X_n|^3)$. One could prove a similar bound (with slightly worse constants) using the concentration inequality for $X_n$ in the proof of Theorem [\[main1\]](#main1){reference-type="ref" reference="main1"}.

::: lemma
[]{#boundmom label="boundmom"} Suppose that $n \geq 3$.

1.  $\ee(|X_n|^3) \leq (n-1) \sqrt{2n-3}$.

2.  $\ee(|T_{n-1}||X_n|^3) \leq (n-1) \sqrt{2n-3}$.
:::

::: proof
*Proof.* By the Cauchy-Schwarz inequality, $\ee(|X_n|^3) \leq \sqrt{\ee(X_n^2) \ee(X_n^4)}$. By Lemma [\[moments\]](#moments){reference-type="ref" reference="moments"}, $\ee(X_n^2) = n-1$ and $$\ee(X_n^4) =
\ee(\ee(X_n^4|\lambda(n-1))) = {n \choose 2} + 3 \ee \left( \sum_{x
\in \lambda(n-1)} c(x)^2 \right).$$ By Lemma [\[identity\]](#identity){reference-type="ref" reference="identity"} with $r=2$ and then part 4 of Lemma [\[ismart\]](#ismart){reference-type="ref" reference="ismart"}, $$\begin{aligned}
\ee \left( \sum_{x \in \lambda(n-1)} c(x)^2 \right) & = & \ee \left[ \left( \sum_{x \in
\lambda(n-1)} c(x) \right)^2 - 2 e_2(\lambda(n-1)) \right]\\ & = & {n-1 \choose
2} \ee ( T_{n-1}^2 )\\ & = & {n-1 \choose 2}. 
\end{aligned}$$ This proves the first assertion.

For the second assertion, note (using part 4 of Lemma [\[ismart\]](#ismart){reference-type="ref" reference="ismart"} in the final equality) that $$\begin{aligned}
\ee(|T_{n-1}||X_n|^3) & = &\ee(\ee(|T_{n-1}||X_n|^3|\lambda(n-1)))\\ &
= & \ee(|T_{n-1}| \ee(|X_n|^3|\lambda(n-1)))\\ & \leq &
\sqrt{\ee(T_{n-1}^2) \ee(\ee(|X_n|^3|\lambda(n-1))^2)}\\ & = &
\sqrt{ \ee(\ee(|X_n|^3|\lambda(n-1))^2)}. 
\end{aligned}$$ The conditional version of the Cauchy-Schwarz inequality and part 1 of Lemma [\[moments\]](#moments){reference-type="ref" reference="moments"} give that $\ee(|X_n|^3|\lambda(n-1))^2$ is at most $$\ee(X_n^2|\lambda(n-1)) \ee(X_n^4|\lambda(n-1)) = (n-1)
\ee(X_n^4|\lambda(n-1)).$$ Thus $$\sqrt{ \ee(\ee(|X_n|^3|\lambda(n-1))^2)} \leq \sqrt{(n-1) \ee(X_n^4)},$$ and the proof of the first assertion showed this to equal $(n-1) \sqrt{2n-3}$, as desired. ◻
:::

Now we adapt Bolthausen's [@Bol] inductive proof of the Berry-Esseen theorem for i.i.d. random variables to the setting of character ratios. We remark that the unpublished notes of Mann [@Man] are a useful exposition of Bolthausen's proof and we refer to them in the proof of Theorem [\[main1\]](#main1){reference-type="ref" reference="main1"}.

::: theorem
[]{#main1 label="main1"} Let $\lambda$ be chosen from the Plancherel measure on partitions of size $n$. Then for all $n \geq 2$ and real $x_0$, $$\left| \pp
    \left( T_n(\lambda) \leq x_0 \right) - \frac{1}{\sqrt{2 \pi}}
    \int_{-\infty}^{x_0} e^{- \frac{t^2}{2}} dt \right| \leq C
    n^{-1/2},$$ where $C$ is a universal constant.
:::

::: proof
*Proof.* It is sufficient to prove the result for $n \geq 3$, so we assume this.

For $z$ real, let $h_{z,0}=\ii_{(-\infty,z]}$ be the indicator function of the set $(-\infty,z]$. For $z$ real and $b>0$, let $h_{z,b}$ be the function which is 1 for $x \leq z$ and then drops linearly to the value 0 at $z+b$ and is 0 for $x \geq
    z+b$. Let $$\delta(b,n) = \sup_{z} \{| \ee(h_{z,b}(T_n)) -
    \Phi h_{z,b}| \}$$ where $\Phi f$ is the expected value of a function f under the normal distribution. Note that our ultimate goal is to upper bound $\delta(0,n)$.

As in Stein's method [@Stn], let $$f(x)=f_{z,b}(x) =
    e^{x^2/2} \int_{-\infty}^x (h_{z,b}(w) - \Phi h_{z,b})
    e^{-w^2/2} dw.$$ Then $f'(x) - x f(x) = h_{z,b}(x) - \Phi
    h_{z,b}$, so that $$\ee(h_{z,b}(T_n))-\Phi h_{z,b} = \ee[
    f'(T_n) - T_n f(T_n)] .$$ Part 2 of Lemma [\[ismart\]](#ismart){reference-type="ref" reference="ismart"} with $j=n$ implies that $$\ee(X_n f(T_n)) = \ee[f(T_n)
    \ee(X_n|T_n)] = \frac{n-1}{\sqrt{{n \choose 2}}} \ee(T_n
    f(T_n)),$$ so that $$\ee[
    f'(T_n) - T_n f(T_n)] = \ee \left[ f'(T_n) -
    \frac{\sqrt{{n \choose 2}}}{n-1} X_n f(T_n) \right].$$ By part 1 of Lemma [\[ismart\]](#ismart){reference-type="ref" reference="ismart"} and part 1 of Lemma [\[moments\]](#moments){reference-type="ref" reference="moments"}, this is equal to $$\begin{aligned}
 & & \ee \left[ f'(T_n) \right] + \ee \left[  \frac{X_n^2}{n-1} f'(\sqrt{\frac{n-2}{n}} T_{n-1}) -
    f'(\sqrt{\frac{n-2}{n}} T_{n-1}) \right]  \\ & & - \ee \left[
    \frac{\sqrt{{n \choose 2}}}{n-1} X_n f(T_n) - \frac{\sqrt{{n
    \choose 2}}}{n-1} X_n f(\sqrt{\frac{n-2}{n}} T_{n-1}) 
 \right]\\ & = & \ee
    \left[ f'(T_n) - f'(\sqrt{\frac{n-2}{n}} T_{n-1}) \right]\\ & & - \ee \left[
    \frac{X_n^2}{n-1} \int_0^1  f'(\sqrt{\frac{n-2}{n}}
    T_{n-1} + t \frac{X_n}{\sqrt{{n \choose 2}}}) -
    f'(\sqrt{\frac{n-2}{n}} T_{n-1}) dt \right]. 
\end{aligned}$$

Next we upper bound $\ee[ f'(T_n) - f'(\sqrt{\frac{n-2}{n}}
    T_{n-1})]$. Recall from [@Bol] or [@Man] that for any $x$ and $\Delta$, $$|f'(x+\Delta) - f'(x)| \leq |\Delta| \left( 3+
    2|x| + \frac{1}{b} \int_{0}^1 \ii_{[z,z+b]}(x+s \Delta) ds \right).$$ Thus $\ee[ f'(T_n) -
    f'(\sqrt{\frac{n-2}{n}} T_{n-1})] \leq A_1 + A_2 + A_3$ where

-   $A_1 = \frac{ 3 \ee(|X_n|)}{\sqrt{{n \choose 2}}}$.

-   $A_2 = \frac{2 \sqrt{\frac{n-2}{n}}}{\sqrt{{n \choose 2}}}
    \ee(|X_n||T_{n-1}|)$.

-   $A_3 = \ee \left[ \frac{|X_n|}{b \sqrt{{n \choose 2}}} \int_0^1
    \ii_{[z,z+b]}(\sqrt{\frac{n-2}{n}} T_{n-1}+
    \frac{s X_n}{\sqrt{{n \choose 2}}}) ds \right]$.

By part 3 of Lemma [\[ismart\]](#ismart){reference-type="ref" reference="ismart"}, $\ee(|X_n|) \leq \sqrt{\ee(X_n^2)} =
    \sqrt{n-1}$; thus $A_1 \leq \frac{3 \sqrt{2}}{\sqrt{n}}$. By parts 3 and 4 of Lemma [\[ismart\]](#ismart){reference-type="ref" reference="ismart"}, $$\ee(|X_n| |T_{n-1}|)
    \leq \sqrt{\ee(X_n^2) \ee(T_{n-1}^2)} = \sqrt{n-1}.$$ Thus $A_2 \leq \frac{2 \sqrt{2}}{\sqrt{n}}$.

Note that $A_3=A_3'+A_3''$ where $$A_3' = \ee \left[
    \ii(|X_n| \leq 2e \sqrt{n}) \frac{|X_n|}{b \sqrt{{n \choose
    2}}} \int_0^1 \ii_{[z,z+b]}(\sqrt{\frac{n-2}{n}} T_{n-1}+
    \frac{s X_n}{\sqrt{{n \choose 2}}} ) ds \right]$$ and $$A_3'' = \ee \left[ \ii(|X_n| > 2e \sqrt{n}) \frac{|X_n|}{b
    \sqrt{{n \choose 2}}} \int_0^1
    \ii_{[z,z+b]}(\sqrt{\frac{n-2}{n}} T_{n-1}+ \frac{s
    X_n}{\sqrt{{n \choose 2}}}) ds \right].$$ Clearly $$A_3' \leq \frac{2e \sqrt{n}}{b \sqrt{{n \choose 2}}} \ee
    \left[ \ii_{[z-\frac{2e \sqrt{n}}{\sqrt{{n \choose
    2}}},z+b+\frac{2e \sqrt{n}}{\sqrt{{n \choose 2}}}]} \left(
    \sqrt{\frac{n-2}{n}} T_{n-1} \right) \right].$$ Now use the fact (explained in [@Man]) that $$0 \leq \ee(\ii_B(c_1
    T_n + c_2)) \leq \frac{|B|}{c_1 \sqrt{2 \pi}} + 2 \delta(0,n)$$ for any interval $B$ and constants $c_1,c_2$ with $c_1 \neq
    0$. It follows that $A_3' \leq \frac{D_1}{\sqrt{n}} +
    \frac{D_2}{bn} + \frac{D_3 \delta(0,n-1)}{b \sqrt{n}}$ where $D_1,D_2,D_3$ are universal constants. To bound $A_3''$, note that since $|X_n| \leq n$, one has that $A_3'' \leq \frac{n}{b
    \sqrt{{n \choose 2}}} \pp(|X_n| > 2e \sqrt{n})$. The proof of Proposition 4.6 of [@F1] derives the concentration inequality $\pp(|X_n| > 2e \sqrt{n}) \leq 2e^{-2e
    \sqrt{n}}$. Since $b$ will later be chosen to be a constant multiplied by $n^{-1/2}$, it follows that $A_3''$ is much smaller than $A_3'$ for large $n$, and one concludes that $$A_3 \leq \frac{D_1}{\sqrt{n}} + \frac{D_2}{bn} + \frac{D_3
    \delta(0,n-1)}{b \sqrt{n}}$$ where $D_1,D_2,D_3$ are universal constants.

Combining the bounds on $A_1,A_2,A_3$, we conclude that $$\ee
    \left[ f'(T_n) - f'(\sqrt{\frac{n-2}{2}} T_{n-1}) \right] \leq
    \frac{D_1}{\sqrt{n}} + \frac{D_2}{bn} + \frac{D_3
    \delta(0,n-1)}{b \sqrt{n}}$$ where $D_1,D_2,D_3$ are universal constants.

Next, we upper bound $$\ee \left| \frac{ X_n^2}{n-1} \int_0^1
    \left[f'(\sqrt{\frac{n-2}{n}} T_{n-1} + t \frac{X_n}{\sqrt{{n
    \choose 2}}}) - f'(\sqrt{\frac{n-2}{n}} T_{n-1}) \right] dt \right|.$$ Arguing as in the previous paragraph this is at most $B_1+B_2+B_3$ where

-   $B_1 = \frac{1}{n-1} \int_{0}^1 \frac{3t \ee(|X_n|^3)}{\sqrt{{n
    \choose 2}}} dt = \frac{3 \ee(|X_n|^3)}{2 (n-1) \sqrt{{n \choose 2}}}$.

-   $B_2 = \frac{1}{n-1} \int_{0}^1 \frac{2t
    \sqrt{\frac{n-2}{n}}}{\sqrt{{n \choose 2}}} \ee(|T_{n-1}||X_n|^3) dt =
    \frac{\sqrt{\frac{n-2}{n}}}{(n-1) \sqrt{{n \choose 2}}}
    \ee(|T_{n-1}||X_n|^3)$.

-   $B_3 = \frac{1}{n-1} \ee \left[ \frac{|X_n|^3}{b \sqrt{n \choose 2}} \int_{0}^1 \int_0^1 t \ii_{[z,z+b]}(\sqrt{\frac{n-2}{n}} T_{n-1} + st \frac{X_n}{\sqrt{{n
    \choose 2}}}) ds dt \right]$.

To bound $B_1$, use part 1 of Lemma [\[boundmom\]](#boundmom){reference-type="ref" reference="boundmom"} to conclude that $B_1 \leq \frac{3}{\sqrt{n}}$. To bound $B_2$, use part 2 of Lemma [\[boundmom\]](#boundmom){reference-type="ref" reference="boundmom"} to conclude that $B_2
\leq \frac{2}{\sqrt{n}}$. To bound $B_3$, one uses an argument almost identical to that for $A_3$ to conclude that $$B_3 \leq
\frac{E_1}{\sqrt{n}} + \frac{E_2}{bn} + \frac{E_3 \delta(0,n-1)}{b
\sqrt{n}}$$ where $E_1,E_2,E_3$ are universal constants.

Summarizing, it has been proved that $$\delta(b,n) \leq
\frac{C_1}{\sqrt{n}} + \frac{C_2}{bn} + \frac{C_3 \delta(0,n-1)}{b
\sqrt{n}}$$ where $C_1,C_2,C_3$ are universal constants. From [@Bol] or [@Man], $\delta(0,n) \leq \delta(b,n) +
\frac{b}{\sqrt{2 \pi}}$ for all $b$, which implies that $$\delta(0,n)
\leq \frac{C_1}{\sqrt{n}} + \frac{C_2}{bn} + \frac{C_3
\delta(0,n-1)}{b \sqrt{n}} + \frac{b}{\sqrt{2 \pi}}.$$ We argue by induction that there is a universal constant $C$ so that $\delta(0,n)
\leq \frac{C}{\sqrt{n}}$ for all $n$. Assuming the result for $n-1$, one obtains that $$\delta(0,n) \leq \frac{C_1}{\sqrt{n}} + \frac{C_2}{bn} + \sqrt
{\frac{3}{2}} \frac{C \cdot C_3 }{b n} + \frac{b}{\sqrt{2 \pi}}.$$ Choosing $b= \frac{2 C_3}{\sqrt{n}}$, it follows that if $C$ is sufficiently large, the induction step will work for all $n$. This completes the proof. ◻
:::

To conclude this section, we note that it would be of interest to prove the following (more general) conjecture. An error term of $O(n^{-1/4})$ has recently been established by the method of exchangeable pairs [@F4].

::: center
:::

**Conjecture**: Let $i \geq 2$ be fixed. Then for all $n \geq i$ and real $x_0$, $$\left| \pp \left( \sqrt{\frac{n!}{(n-i)! i}}
\frac{\chi^{\lambda}(12 \cdots i)}{dim(\lambda)} \leq x_0 \right) -
\frac{1}{\sqrt{2 \pi}} \int_{-\infty}^{x_0} e^{-\frac{t^2}{2}} dt \right|
\leq C_i n^{-1/2}$$ where $C_i$ is a constant depending on $i$.
