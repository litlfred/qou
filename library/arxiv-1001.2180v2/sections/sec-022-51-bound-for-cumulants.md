---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-022-51-bound-for-cumulants
section_title: "Bound for cumulants"
section_number: 5.1
pages: 18-21
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.967
latex_coverage_ratio: 0.975
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
[]{#subsect:bound_cumulants label="subsect:bound_cumulants"} This sort of result (computing the fluctuations of an observable from the character values) has already been stated by P. Śniady in the case where the characters are small and the corresponding diagrams balanced. Here, we have to use different observables and a different gradation, but the ideas of the proof are the same, and the definitions of the different cumulants used here come from [@Sniady06]. In particular we shall use joint cumulants of random variables $k(X_1,\ldots,X_r)$, which can be defined by induction[^1] on $r$:

$$\mathbb{E}[X_1 \,X_2 \cdots X_r]=\sum_{\substack{\pi \text{ partition}\\ \text{of } \{1,2,\ldots,r\} }} \, k\big(X_{i \in \pi_1}\big) \, k\big(X_{i \in \pi_2}\big) \cdots k\big(X_{i \in \pi_\ell}\big).$$

A centered gaussian vector $(Y_1,\ldots,Y_k)$ is characterized by the fact that all $k(Y_{i_1},\ldots,Y_{i_r})$ are equal to $0$ for $r \neq 2$. Moreover, the values for $r=2$ give then the covariance matrix. Therefore, the proof of Proposition [\[prop:deviation_powersums\]](#prop:deviation_powersums){reference-type="ref" reference="prop:deviation_powersums"} consists in computing the limit of $k(W_{n,q,i_1},\ldots,W_{n,q,i_r})$. In fact, we will show a stronger result than the convergence towards $0$ for $r \geq 3$:

::: lemma
[]{#lem:ordre_cumulants label="lem:ordre_cumulants"} For any $x_1,x_2,\ldots,x_r \in \mathscr{O}$, one has: $$k(x_1,\ldots,x_r) = O\left(n^{\deg(x_1) + \cdots + \deg(x_r)-r+1}\right).$$
:::

The end of this subsection is devoted to the proof of this lemma. Thanks to the multi-linearity of cumulants (for $r\geq 2$) and some compatibility relation with respect to products (see [@LS59] and [@Sniady06 Theorem 4.4]), it is enough to prove this lemma with the $x_i$ in any graded algebraic basis of $\mathscr{O}$. A good choice is the basis $(\varSigma_k)_{k\geq 1}$; indeed, we have already computed the expectation of these observables under the $q$-Plancherel measure. Unfortunately, we do not know their joint moments $\mathbb{E}[\varSigma_{i_1} \cdots \varSigma_{i_r}]$, which are different from what we have computed in the previous section, namely, $\mathbb{E}[\varSigma_{i_1,\ldots,i_r}]$.

### Cumulants $k^\bullet$

This difficulty disappears if we use the algebra $\mathscr{O}^\bullet$, because $\Sigma_{i_1} \bullet \cdots \bullet \Sigma_{i_r}=\Sigma_{i_1,\ldots,i_r}$. This algebra gives rise to a new kind of cumulant, the so-called disjoint cumulants, which we shall denote by $k^\bullet(X_{1},\ldots,X_{r})$. Their definition is the same as for $k(X_1,\ldots,X_r)$, except that the product of observables is now the disjoint product: $$\label{eq:def_dis_cum}
\mathbb{E}[X_1 \bullet X_2 \bullet \cdots \bullet X_r]=\sum_{\substack{\pi \text{ partition}\\ \text{of } \{1,2,\ldots,r\} }} \, k^\bullet\big(X_{i \in \pi_1}\big) \, k^\bullet\big(X_{i \in \pi_2}\big) \cdots k^\bullet\big(X_{i \in \pi_\ell}\big).$$ It is easy to prove the analog of Lemma [\[lem:ordre_cumulants\]](#lem:ordre_cumulants){reference-type="ref" reference="lem:ordre_cumulants"} for these disjoint cumulants:

::: lemma
[]{#lem:ordre_disjoint_cumulants label="lem:ordre_disjoint_cumulants"} For any $x_1,x_2,\ldots,x_r \in \mathscr{O}$, one has: $$k^\bullet(x_1,\ldots,x_r) = O\left(n^{\deg(x_1) + \cdots + \deg(x_r)-r+1}\right).$$
:::

::: proof
*Proof.* As for classical cumulants, it is enough to prove it for $x_j=\varSigma_{i_j}$. In this case, the left-hand side of [\[eq:def_dis_cum\]](#eq:def_dis_cum){reference-type="eqref" reference="eq:def_dis_cum"} is simply $$\mathbb{E}[\varSigma_{i_1,\ldots,i_r}]=\frac{(q-1)^{i_1+\cdots+i_r}}{\prod(q^{i_j}-1)} n^{\downarrow (i_1+\cdots+i_r)}.$$ Except for the factor $n^{\downarrow (i_1+\ldots+i_r)}$, everything is multiplicative with respect to the parts of $\lambda$. More formally, there exist numbers $\alpha_i$ such that: $$\begin{aligned}
\mathbb{E}[\varSigma_{i_1,\ldots,i_r}] &= \left( \prod_j \alpha_{i_j} \right) n^{\downarrow (i_1+\cdots+i_r)};\\
&=\left( \prod_j \alpha_{i_j} \right) \mathbb{E}\big[\varSigma_{\!\!\!\!\underbrace{1,\ldots,1}_{i_1 + \cdots + i_r \text{ times}}}\big].
\end{aligned}$$ An immediate induction implies that: $$k^\bullet(\varSigma_{i_1},\ldots,\varSigma_{i_n})=\left( \prod_j \alpha_{i_j} \right) k^\bullet(\varSigma_{\underbrace{1,\ldots,1}_{i_1 \text{ times}}},\ldots,\varSigma_{\underbrace{1,\ldots,1}_{i_r \text{ times}}}).$$ But $\chi^\lambda(\varSigma_{1^{i}})=n^{\downarrow i}$ for any $\lambda$, so the corresponding cumulants do not depend on the measure considered on Young diagrams, and we can use the result of P. Śniady who proved ([@Sniady06 Lemma 4.8]) that: $$k^\bullet(\varSigma_{\underbrace{1,\ldots,1}_{i_1 \text{ times}}},\ldots,\varSigma_{\underbrace{1,\ldots,1}_{i_r \text{ times}}})=O(n^{i_1+\cdots+i_r-(r-1)}).$$ This ends the proof of this lemma. ◻
:::

### Cumulants $k^{\mathrm{id}}$

The last problem is to link classical and disjoint cumulants. Thanks to the commutativity of the diagram below $$\begin{diagram}
   \node{\mathscr{O}} \arrow{se,b}{\mathbb{E}=M_{n,q}}\arrow[2]{e,t}{\mathbb{E}^\mathrm{id}} \node[2]{\mathscr{O}^\bullet}\arrow{sw,b}{\mathbb{E}=M_{n,q}}\\
\node[2]{\mathbb{C}}
  \end{diagram}$$ this can be done by using a result of Brillinger [@Bri69]. One obtains the following formula, see [@Sniady06 Proposition 4.1]: $$\label{eq:link_2_cumulants}
k(X_1,X_2,\ldots,X_n)=\sum_{\pi\vdash n } k^\bullet(k^{\mathrm{id}}(X_{i \in \pi_1}), k^{\mathrm{id}}(X_{i \in \pi_2}),\ldots,k^{\mathrm{id}}(X_{i \in \pi_r})),$$ where $k^{\mathrm{id}}$ is the cumulant corresponding to the identity map $\mathbb{E}^\mathrm{id}$ of the diagram (note that $k^{\mathrm{id}}$ takes value in $\mathscr{O}$), that is to say that it is defined by $$X_1 X_2 \cdots X_r=\sum_{\substack{\pi \text{ partition}\\ \text{of } \{1,2,\ldots,r\} }} k^{\mathrm{id}}\big(X_{i \in \pi_1}\big) \bullet k^{\mathrm{id}}\big(X_{i \in \pi_2}\big) \bullet \cdots \bullet k^{\mathrm{id}}\big(X_{i \in \pi_{\ell}}\big).$$

We will prove the following bound on the degree of identity cumulants. For any $i_1,\ldots,i_r$, one has: $$\label{eq:major_deg_kid}
\deg\big(k^{\mathrm{id}}(\Sigma_{i_1},\ldots,\Sigma_{i_r})\big) \leq i_1 + \cdots + i_r - (r-1).$$ Note that it is not the same as [@Sniady06 Theorem 4.3]; indeed, we use a different gradation on the algebra of observables.

Let us begin by looking at $k^{\mathrm{id}}(\varSigma_{i_1},\ldots,\varSigma_{i_n})$ for small values of $n$. For $n=1$, by definition $k^{\mathrm{id}}(\varSigma_{i})=\varSigma_i$. For $n=2$, one has: $$k^{\mathrm{id}}(\varSigma_{i_1},\varSigma_{i_2})=\varSigma_{i_1} \cdot \varSigma_{i_2} - \varSigma_{i_1,i_2}.$$ But one also has $$\begin{aligned}
 \varSigma_{i_1} \cdot \varSigma_{i_2} &=\sum_{ A_1\in \mathcal{A}(n,i_1),\,A_2 \in \mathcal{A}(n,i_2)} C(A_1) \, C(A_2) ;\\
\varSigma_{i_1,i_2} &= \sum_{\substack{ A_1\in \mathcal{A}(n,i_1),\,A_2 \in \mathcal{A}(n,i_2)\\ A_1 \cap A_2 = \emptyset}} C(A_1)\, C(A_2).
\end{aligned}$$ so the difference $k^{\mathrm{id}}$ is equal to the same expression with the sum restricted to pairs of arrangements which have a non-empty intersection: $$k^{\mathrm{id}}(\varSigma_{i_1},\varSigma_{i_2} )=\sum_{ \substack{A_1\in\mathcal{A}(n,i_1),\,A_2 \in \mathcal{A}(n,i_2)\\ A_1 \cap A_2 \neq \emptyset}} C(A_1)\, C(A_2).$$ It turns out that the identity cumulants satisfy a similar identity in the general case, and the intersections between the $A_j$ play once again a significant role. First, note that: $$\varSigma_{i_1} \cdots  \varSigma_{i_r} =\sum_{ \forall j,\,\,A_j \in \mathcal{A}(n,i_j)} C(A_1) \cdots C(A_r)$$ Given a family $A_1,\ldots,A_r$ of arrangements, we consider the relation $\sim_1$ defined by $k \sim_1 l \Leftrightarrow A_k \cap A_l \neq \emptyset$. Its transitive closure is an equivalence relation; let us denote by $\pi(A_1,\ldots,A_r)$ the corresponding partition of $\left[\!\left[1,r\right]\!\right]$. Obviously, this partition depends only on which indices are equal and not on the values they take, so the sum of $C(A_1) \cdots C(A_r)$ over arrangements corresponding to a given partition is of the form $X_{i_1,\dots,i_r}^{\mathcal{G}}$ (notation of paragraph [\[subsect:bullet_product\]](#subsect:bullet_product){reference-type="ref" reference="subsect:bullet_product"}) and we can use Lemma [\[lem:bullet\]](#lem:bullet){reference-type="ref" reference="lem:bullet"} on this kind of expression.

::: lemma
For any $i_1,\ldots,i_r$, one has: $$k^{\mathrm{id}}(\varSigma_{i_1},\ldots,\varSigma_{i_r}) = \sum_{ \substack{\forall j,\,\,A_j \in \mathcal{A}(n,i_j) \\  \pi(A_1,\ldots,A_r)=\{\left[\!\left[1,r\right]\!\right]\}       }} C(A_1) \cdots C(A_r).$$
:::

::: proof
*Proof.* We will prove this statement by induction on $r$. As explained above, it is true for $r=1,2$. Let us suppose that it is true for all $s \leq r-1$. Because of the definition of the disjoint product $\bullet$, for every *non-trivial* set partition $\pi$, one has: $$k^{\mathrm{id}}\big(\varSigma_{i \in \pi_1}\big) \bullet k^{\mathrm{id}}\big(\varSigma_{i \in \pi_2}\big) \bullet \cdots \bullet k^{\mathrm{id}}\big(\varSigma_{i \in \pi_\ell}\big)=\sum_{\substack{\forall j,\,\,A_j \in \mathcal{A}(n,i_j) \\  \pi(A_1,\ldots,A_r)=\pi} } C(A_1) \cdots C(A_r).$$ Indeed, the induction hypothesis applies for each part $\pi_i$, so we only keep terms corresponding to sequences of arrangements for which two numbers in the same part of $\pi$ are in the same part of $\pi(A_1,\ldots,A_r)$. Besides, when we form the product $\bullet$, we take only disjoint set of indices (using Lemma [\[lem:bullet\]](#lem:bullet){reference-type="ref" reference="lem:bullet"}), so two numbers in different parts of $\pi$ cannot be in the same part of $\pi(A_1,\ldots,A_r)$.

We use now the inductive definition of $k^{\mathrm{id}}$: $$\begin{aligned}
k^{\mathrm{id}}(\varSigma_{i_1},\ldots,\varSigma_{i_r}) &= \,\,\,\,\varSigma_{i_1} \cdots \varSigma_{i_r}\quad  - \sum_{\pi \neq \{\left[\!\left[1,r\right]\!\right]\}} \, k^{\mathrm{id}}\big(\varSigma_{i \in \pi_1}\big) \bullet k^{\mathrm{id}}\big(\varSigma_{i \in \pi_2}\big) \bullet \cdots \bullet k^{\mathrm{id}}\big(\varSigma_{i \in \pi_\ell}\big) \\
&=\sum_{ \forall j,\,\,A_j\in \mathcal{A}(n,i_j)} \!\!\!\!C(A_1) \cdots C(A_r) \quad - \sum_{\pi \neq \{\left[\!\left[1,r\right]\!\right]\}} \left( \sum_{ \substack{ \forall j,\,\,A_j \in \mathcal{A}(n,i_j)\\ \pi(A_1,\ldots,A_r) =\pi}} C(A_1) \cdots C(A_r) \right)\\
& =\!\!\!\!\sum_{ \substack{\forall j,\,\,A_j \in \mathcal{A}(n,i_j) \\  \pi(A_1,\ldots,A_r)=\{\left[\!\left[1,r\right]\!\right]\}}} \!\!\!\!\!\!\!\!C(A_1) \cdots C(A_r),
\end{aligned}$$ which is exactly the equality we wanted at rank $r$. ◻
:::

Now, for every sequence of arrangements $A_1,\ldots,A_r$ such that $\pi(A_1,\ldots,A_r)$ is the trivial partition $\{\left[\!\left[1,r \right]\!\right]\}$, the cardinality of $|A_1 \cup \cdots \cup A_r|$ is smaller than $i_1 + \cdots + i_r - (r-1)$, because one has at least $r-1$ equalities between different elements of these arrangements. So, $k^{\mathrm{id}}(\varSigma_{i_1},\ldots,\varSigma_{i_r})$ can be written as a linear combination of $\varSigma_{\lambda}$ with $|\lambda| \leq i_1 + \cdots + i_r - (r-1)$, which ends the proof of equation [\[eq:major_deg_kid\]](#eq:major_deg_kid){reference-type="eqref" reference="eq:major_deg_kid"}.

Finally, equations [\[eq:link_2_cumulants\]](#eq:link_2_cumulants){reference-type="eqref" reference="eq:link_2_cumulants"} and [\[eq:major_deg_kid\]](#eq:major_deg_kid){reference-type="eqref" reference="eq:major_deg_kid"}, together with Lemma [\[lem:ordre_disjoint_cumulants\]](#lem:ordre_disjoint_cumulants){reference-type="ref" reference="lem:ordre_disjoint_cumulants"}, complete the proof of Lemma [\[lem:ordre_cumulants\]](#lem:ordre_cumulants){reference-type="ref" reference="lem:ordre_cumulants"}.

[^1]: It can also be defined via generating functions.
