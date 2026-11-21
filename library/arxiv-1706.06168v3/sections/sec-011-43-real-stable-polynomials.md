---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-011-43-real-stable-polynomials
section_title: "Real Stable Polynomials"
section_number: 4.3
pages: 13-14
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.994
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
[]{#stab_subsect label="stab_subsect"}

We now give a number of classical real stability results, along with a few results from [@bb1] and [@bb2]. Additionally, we state these results for homogeneous polynomials in $V_\mathbb{R}(\lambda)$, taking roots at infinity into account. The results of this section will come in to play mainly in §[\[Rops_sect\]](#Rops_sect){reference-type="ref" reference="Rops_sect"}, where we discuss real linear operators and operators preserving interval- and ray-rootedness.

The first result we will need for our considerations of $V_\mathbb{R}(\lambda)$ is a version of the Hermite-Biehler theorem, often called the Hermite-Kakeya-Obreschkoff theorem. We state here without proof the multivariate version essentially used in Theorem 1.9 of [@bb1] (see also §2.4 of [@wagner2011polys]). First we need a definition.

::: definition
[]{#pp_def label="pp_def"} We say that $p,q \in V_\mathbb{R}(\lambda)$ are in *proper position*, denoted $p \ll q$, if $q + ip$ is weakly $\mathcal{H}_+^m$-stable (equivalently, if $p + iq$ is weakly $\mathcal{H}_-^m$-stable).
:::

::: proposition
[]{#hermite-biehler label="hermite-biehler"} For $p,q \in V_\mathbb{R}(\lambda)$, $ap + bq$ is weakly real stable for all $a,b \in \mathbb{R}$ if and only if either $p \ll q$ or $q \ll p$.
:::

This result will be crucial to our consideration of real polynomials and real stability (as it was in [@bb1]). Its main use for us in this direction is made explicit in the following.

::: lemma
[]{#rs_lemma label="rs_lemma"} Fix $\lambda \in \mathbb{N}_0^m$, $\alpha \in \mathbb{N}_0^l$, and a linear operator $T: V(\lambda) \to V(\alpha)$ which restricts to a real linear operator from $V_\mathbb{R}(\lambda)$ to $V_\mathbb{R}(\alpha)$. If $T$ preserves weak real stability and $p \in V(\lambda)$ is stable, then $T(p)$ is either $\mathcal{H}_+^l$-stable, $\mathcal{H}_-^l$-stable, or identically zero.
:::

::: proof
*Proof.* By the Hermite-Biehler theorem, there exist $q,r \in V_\mathbb{R}(\lambda)$ such that $p = q + ir$ and $a q + b r$ is real stable or zero for all $a,b \in \mathbb{R}$. So, $a T(q) + b T(r)$ is real stable or zero for all $a,b \in \mathbb{R}$. By Hermite-Biehler again, $T(p) = T(q) + iT(r)$ is either $\mathcal{H}_+^l$-stable, $\mathcal{H}_-^l$-stable, or identically zero. ◻
:::

The next two results are from [@bb1], the first of which gives an equivalent characterization for a polynomial to be a scalar multiple of a real stable polynomial. This result will be specifically used in §[\[Rops_sect\]](#Rops_sect){reference-type="ref" reference="Rops_sect"} to generalize complex operator theoretic stability results to the real stability case.

::: lemma
[]{#scal_rs_lemma label="scal_rs_lemma"} Let $p \in V_\mathbb{C}(\lambda)$ be both $\mathcal{H}_+^m$-stable and $\mathcal{H}_-^m$-stable. Then, $p$ is a (complex) scalar multiple of a real stable polynomial. In particular, if nonzero $q,r \in V_\mathbb{R}(\lambda)$ are such that $q \ll r$ and $r \ll q$, then $r$ is a (real) scalar multiple of $q$.
:::

The next result provides the degeneracy cases in the Borcea-Brändén characterizations (recall the dimension restrictions of Theorems [\[BB_Cops_thm\]](#BB_Cops_thm){reference-type="ref" reference="BB_Cops_thm"} and [\[BB_Rops_thm\]](#BB_Rops_thm){reference-type="ref" reference="BB_Rops_thm"}). We will use this result to explicate the link between our operator characterization and the Borcea-Brändén characterization (see Lemmas [\[bb_Clink\]](#bb_Clink){reference-type="ref" reference="bb_Clink"} and [\[bb_Rlink\]](#bb_Rlink){reference-type="ref" reference="bb_Rlink"}).

::: lemma
[]{#dim_lemma label="dim_lemma"} Let $W \subseteq V_\mathbb{K}(\lambda)$ be a $\mathbb{K}$-vector subspace (for $\mathbb{K}= \mathbb{C}$ or $\mathbb{K}= \mathbb{R}$) consisting only of weakly stable (resp. weakly real stable) polynomials. We have:

1.  If $\mathbb{K}= \mathbb{C}$, then $\dim(W) \leq 1$.

2.  If $\mathbb{K}= \mathbb{R}$, then $\dim(W) \leq 2$.
:::

By applying appropriate Möbius transformations, note that $(a)$ of the above lemma can be generalized to $(C_1 \times \cdots \times C_m)$-stable polynomials for any open circular regions $C_1,\ldots,C_m \subseteq \mathbb{CP}^1$.

We now state the last result of this section, which refines the Hermite-Biehler theorem for top-degree monic polynomials in $V_\mathbb{R}(n)$. This refinement comes through the notion of *interlacing polynomials* and is much closer to the original statement of the classical Hermite-Biehler theorem (e.g., see Theorem 6.3.4 in [@rahman2002anthpoly]).

::: lemma
[]{#total_order_lemma label="total_order_lemma"} For top-degree monic $p,q \in V_\mathbb{R}(n)$, $p \ll q$ if and only if the roots of $p$ and $q$ (denoted in increasing order by $(\alpha_k:1)$ and $(\beta_k:1)$, respectively) interlace on the real line in the following way: $$\alpha_1 \leq \beta_1 \leq \alpha_2 \leq \beta_2 \leq \cdots \leq \alpha_n \leq \beta_n$$ Further, if these equivalent conditions hold, then $\ll$ gives a total order on the top-degree monic elements of the span of $p$ and $q$ in $V_\mathbb{R}(n)$. This order is equivalently defined via the order of the $k^\text{th}$ largest roots, for any $k \in [n]$ such that $\alpha_k \neq \beta_k$.
:::

::: proof
*Proof.* The fact that $p \ll q$ is equivalent to interlacing roots is the classical univariate Hermite-Biehler theorem. That $q$ has larger roots than $p$ can be obtained by the fact that the $(n-1)^\text{st}$ derivative of $q + ip$ must be $\mathcal{H}_+$-stable. Since both polynomials are top-degree monic, this $(n-1)^\text{st}$ derivative will be a complex linear combination of two linear terms. This complex linear combination is given as follows, where $s_q$ and $s_p$ denote the respective sums of the roots of $q$ and $p$: $$\partial_x^{n-1} \big(q(x,y) + ip(x,y)\big) = (n! \cdot x - (n-1)! \cdot s_q y) + i(n! \cdot x - (n-1)! \cdot s_p y) = n!(1+i)\left(x - \frac{s_q + i s_p}{n(1 + i)} y\right)$$ Since this polynomial is $\mathcal{H}_+$-stable, it must be that $\frac{s_q + i s_p}{n(1 + i)} \in \overline{\mathcal{H}_-}$. We further compute: $$\overline{\mathcal{H}_-} \ni \frac{s_q + i s_p}{n(1 + i)} = \frac{(s_q + i s_p)(1-i)}{2n} = \frac{s_q + s_p + i(s_p-s_q)}{2n}$$ Therefore $s_q \geq s_p$, which is the same as saying that the sum of the roots of $q$ is larger than that of $p$. Since we already know that the roots of $q$ and $p$ interlace, this implies that $q$ has larger roots than $p$.

As for the total ordering property, let $r$ and $s$ be two polynomials in the real span of $p$ and $q$. Any real linear combination of these polynomials is then a real linear combination of $p$ and $q$ (and hence is real-rooted), and Hermite-Biehler implies either $r \ll s$ or $s \ll r$. By the above interlacing condition, it is straightforward to see that this total order is given by looking at the order of the $k^\text{th}$ roots, for any $k \in [n]$. ◻
:::
