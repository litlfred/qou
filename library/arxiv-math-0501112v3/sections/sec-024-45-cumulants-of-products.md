---
doc_id: arxiv-math-0501112v3
doc_title: "arXiv:math/0501112v3 [math.CO] 31 May 2005"
section_id: sec-024-45-cumulants-of-products
section_title: "Cumulants of products"
section_number: 4.5
pages: 21-24
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.938
latex_coverage_ratio: 0.955
---
If $\rho=\{\rho_1,\dots,\rho_k\}$ is a partition of the set $\{1,\dots,n\}$ with blocks $\rho_i=\{\rho_{i,1},\dots,\rho_{i,m(i)}
\}$ we define partition--indexed cumulants given by a multiplicative extension of the usual cumulants: $$\label{eq:multiplikatywnie} k_{\rho}(X_1,\dots,X_n)= \prod_i
k(X_{\rho_{i,1} }, X_{\rho_{i,2}},\dots, X_{\rho_{i,m(i)}});$$ for example $$k_{ \{1,3,4\},\{2,5\}} (X_1,X_2,X_3,X_4,X_5)= k (X_1,X_3,X_4)\
k (X_2,X_5).$$

The following formula for cumulants of products of random variables was proved by Leonov and Sirjaev [@LeonovSiraev].

::: theorem
[]{#theo:leonovsiraev label="theo:leonovsiraev"} Let $i_1<i_2<\cdots<i_{n+1}$ be integers and let $X_{i_1+1},X_{i_1+2},\dots,X_{i_{n+1}}$ be a family of random variables; then $$\label{eq:leonovsiraev} k\Big(\prod_{i_1+1\leq
j\leq i_2} X_{j}, \dots , \prod_{i_n+1\leq j\leq i_{n+1}} X_{j}
\Big) = \sum_{\pi} k_{\pi}(X_{i_1+1},X_{i_1+2},\dots,X_{i_{n+1}}),$$ where the sum runs over all partitions $\pi$ of the set $\{i_1+1,i_1+2,\dots,i_{n+1}\}$ with the additional property that $$\pi \vee \big\{ \{i_1+1,i_1+2,\dots,i_2\}, \dots,
\{i_{n}+1,i_{n}+2,\dots,i_{n+1} \}   \big\}$$ is the maximal partition with only one block.
:::

::: corollary
[]{#cor:takieisiakie label="cor:takieisiakie"} Let permutations $\sigma_1,\dots,\sigma_n$ be disjoint cycles of length $l_1,\dots,l_n$. Then $$\begin{gathered}
\label{eq:happynewyear}
k^{\bullet}(\Sigma_{l_1},\dots,\Sigma_{l_n})= \\ \sum_{\pi^{(1)},
\pi^{(2)}} k_{\pi^{(1)}}(\sigma_{1},\dots,\sigma_{n}) \
k^{\bullet}_{\pi^{(2)}} (\Sigma_{\underbrace{1,\dots,1}_{l_1 \text{
times}} },\dots,\Sigma_{\underbrace{1,\dots,1}_{l_n \text{ times}}
}),
\end{gathered}$$ where the sum runs over all partitions $\pi^{(1)},\pi^{(2)}$ of the set $\{1,\dots,n\}$ such that $\pi^{(1)}\vee \pi^{(2)}= \big\{
\{1,\dots,n\} \big\}$.
:::

::: proof
*Proof.* We consider the algebra ${\mathbb{C}}(S_q)\otimes {\mathfrak{A}}^{\bullet}$ with the usual product on the first factor and the disjoint product on the second one: $(a_1\otimes b_1) (a_2\otimes b_2)=(a_1 a_2) \otimes (b_1
\bullet b_2)$.

For all integers $l_1,\dots,l_n\geq 1$ and disjoint cycles $\sigma_1,\dots,\sigma_{n}$ with appropriate lengths we clearly have $${\mathbb{E}}\big(\Sigma_{l_1} \bullet \cdots \bullet \Sigma_{l_n} \big)=
{\mathbb{E}}\big[ (\sigma_{1} \otimes \Sigma_{\underbrace{1,\dots,1}_{l_1
\text{ times}} } ) \cdots (\sigma_{n} \otimes
\Sigma_{\underbrace{1,\dots,1}_{l_n \text{ times}} } ) \big],$$ where the product on the left-hand side is taken in ${\mathfrak{A}}^{\bullet}$ and the product on the right-hand side is taken in ${\mathbb{C}}(S_q)\otimes
{\mathfrak{A}}^{\bullet}$. In other words: the mixed moments of the family of random variables $(\Sigma_{l_i})$ coincide with the mixed moments of the family $(\sigma_{i} \otimes \Sigma_{\underbrace{1,\dots,1}_{l_i
\text{ times}} })$. It follows that corresponding cumulants are equal: $$k^{\bullet} \big(\Sigma_{l_1},\dots,\Sigma_{l_n} \big)=
k(\sigma_{1} \otimes \Sigma_{\underbrace{1,\dots,1}_{l_1 \text{
times}} } , \dots ,\sigma_{n} \otimes
\Sigma_{\underbrace{1,\dots,1}_{l_n \text{ times}} } ).$$ We use now Theorem [\[theo:leonovsiraev\]](#theo:leonovsiraev){reference-type="ref" reference="theo:leonovsiraev"} to compute the right-hand side which finishes the proof. ◻
:::

In applications of this result we will find useful the following lemma.

::: lemma
[]{#lem:connections label="lem:connections"} Let $\pi=\{\pi_1,\dots,\pi_m\}$ be a partition which contributes to the right-hand side of [\[eq:leonovsiraev\]](#eq:leonovsiraev){reference-type="eqref" reference="eq:leonovsiraev"}. Then $$\sum_i \big( |\pi_i|-1 \big) \geq n-1.$$

Let $\pi^{(k)}=\{\pi^{(k)}_1,\dots,\pi^{(k)}_{m^{(k)}}\}$ for $k\in\{1,2\}$ be partitions which contribute to the right-hand side of [\[eq:happynewyear\]](#eq:happynewyear){reference-type="eqref" reference="eq:happynewyear"}. Then $$\sum_i \big( |\pi^{(1)}_i|-1 \big)+\sum_i \big( |\pi^{(2)}_i|-1 \big) \geq n-1.$$
:::

::: proof
*Proof.* Partition $\pi$ can be obtained from the trivial partition (every block consists of exactly one element) by performing $\sum_i \big(
|\pi_i|-1 \big)$ times the following operation: we select two blocks and merge them into a single one. Clearly, the number of blocks of partition $$\pi \vee \big\{ \{i_1+1,i_1+2,\dots,i_2\}, \dots,
\{i_{n}+1,i_{n}+2,\dots,i_{n+1} \}   \big\}$$ either decreases by one or stays the same in each step. The initial number of blocks is equal to $n$ and the final number of blocks is equal to $1$, which finishes the proof.

The proof of the second statement is analogous and we skip it. ◻
:::

::: corollary
[]{#cor:roznegradacjejednadegradacja label="cor:roznegradacjejednadegradacja"} Let $X$ be a set of generators of the algebra of conjugacy classes ${\mathfrak{A}}$. Suppose that $$\label{eq:quickdecay} k(a_1,\dots,a_n) q^{-\frac{\deg
a_1+\cdots+\deg a_n-2(n-1)}{2}  }= O(1)$$ holds true for all $n\geq 1$ and $a_1,\dots,a_n\in X$. Then [\[eq:quickdecay\]](#eq:quickdecay){reference-type="eqref" reference="eq:quickdecay"} holds true for all $n\geq 1$ and $a_1,\dots,a_n\in {\mathfrak{A}}$.
:::

::: proof
*Proof.* Clearly, it is enough to consider the case when $a_1,\dots,a_n$ are monomials in elements of $X$. In order to estimate each summand on the right-hand side of [\[eq:leonovsiraev\]](#eq:leonovsiraev){reference-type="eqref" reference="eq:leonovsiraev"} we apply Lemma [\[lem:connections\]](#lem:connections){reference-type="ref" reference="lem:connections"}. ◻
:::

::: remark
Note that the above Corollary holds true also when the cumulants $k$ are replaced by $k^{\bullet}$. In particular, this Corollary can be applied for [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"} and [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"}.
:::

## Proof of the main theorem: equivalence [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"}$\iff$[\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"}

::: proof
*Proof of the implication [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"} $\implies$ [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"}.* Our goal is to use Proposition [\[prop:Brillinger\]](#prop:Brillinger){reference-type="ref" reference="prop:Brillinger"} in order to express $k^{\bullet}(\Sigma_{l_1},\dots,\Sigma_{l_n})$ in terms of the cumulants $k^{\text{id}}$ and $k^{\bullet}$. To estimate a summand on the right-hand side of [\[eq:Brillinger\]](#eq:Brillinger){reference-type="eqref" reference="eq:Brillinger"} corresponding to a partition $\pi=\{\pi_1,\dots,\pi_m\}$ of $\{1,\dots,n\}$ we use Theorem [\[theo:kumulantykombinatoryczne\]](#theo:kumulantykombinatoryczne){reference-type="ref" reference="theo:kumulantykombinatoryczne"} and get $$\deg k^{\text{\rm{id}}}(x_i: i\in \pi_j)\leq \Big( \sum_{i\in\pi_j} \deg x_i
\Big)-2(|\pi_j|-1).$$ Thus $$\label{equ:szacowanie} \Big(\sum_{1\leq j\leq m} \deg
k^{\text{\rm{id}}}(x_i: i\in \pi_j)\Big) - 2(m-1) \leq \Big( \sum_i
\deg x_i \Big)-2(n-1).$$

Assumption [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"} and Corollary [\[cor:roznegradacjejednadegradacja\]](#cor:roznegradacjejednadegradacja){reference-type="ref" reference="cor:roznegradacjejednadegradacja"} show that $$k^{\bullet}\big[ k^{\text{\rm{id}}}(x_i: i\in \pi_j   ):
j=1,2,\dots \big] q^{\frac{-\sum_j \deg k^{\text{\rm{id}}}(x_i: i\in
\pi_j) + 2(m-1)}{2}}= O(1).$$ Now [\[equ:szacowanie\]](#equ:szacowanie){reference-type="eqref" reference="equ:szacowanie"} finishes the proof. ◻
:::

As a byproduct, in a similar way we obtain a proof of the identity $$\begin{gathered}
\label{eq:tttt}
 \lim_{q\to\infty}\mathop{\mathrm{Cov}}(\Sigma_{l_1},\Sigma_{l_2})
q^{-\frac{l_1+l_2}{2} }= \lim_{q\to\infty} \mathop{\mathrm{Cov}}^{\bullet}
(\Sigma_{l_1},\Sigma_{l_2}) q^{-
\frac{l_1+l_2}{2}  } +   \\ \sum_{r\geq 1}\sum_{\substack{a_1,\dots,a_r\geq 1\\
a_1+\dots+a_r=l_1}}  \sum_{\substack{b_1,\dots,b_r\geq 1\\
b_1+\dots+b_r=l_2}} \frac{l_1 l_2}{r} c_{a_1+b_1} \cdots c_{a_r+b_r}
\end{gathered}$$ which is a part of Theorem [\[theo:main2\]](#theo:main2){reference-type="ref" reference="theo:main2"}.

::: proof
*Proof of the implication [\[eq:faktoryzacja3\]](#eq:faktoryzacja3){reference-type="eqref" reference="eq:faktoryzacja3"} $\implies$ [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"}.* We will use induction with respect to $(\deg
\Sigma_{l_1}+\cdots+\deg \Sigma_{l_n})$. Equation [\[eq:Brillinger\]](#eq:Brillinger){reference-type="eqref" reference="eq:Brillinger"} can be written in the form $$\begin{gathered}
k^{\bullet}(\Sigma_{l_1},\dots,\Sigma_{l_n}) =
k(\Sigma_{l_1},\dots,\Sigma_{l_n})- \\ \sum_{\pi\neq\{ \{1,\dots,n\}
\}} k^{\bullet}\big[ k^{\text{\rm{id}}}(x_i: i\in \pi_j   ):
j=1,2,\dots \big] .
\end{gathered}$$ The inductive hypothesis can be used to estimate the right-hand side in the same way as in the proof of the opposite implication above. ◻
:::

## Proof of the main theorem: equivalence [\[eq:faktoryzacja1\]](#eq:faktoryzacja1){reference-type="eqref" reference="eq:faktoryzacja1"} $\iff$ [\[eq:faktoryzacja2\]](#eq:faktoryzacja2){reference-type="eqref" reference="eq:faktoryzacja2"}
