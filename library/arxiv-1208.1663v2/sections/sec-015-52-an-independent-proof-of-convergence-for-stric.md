---
doc_id: arxiv-1208.1663v2
doc_title: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES"
section_id: sec-015-52-an-independent-proof-of-convergence-for-stric
section_title: "An independent proof of convergence for strict index structures"
section_number: 5.2
pages: 16-18
source_pdf: 1208.1663v2.pdf
source_sha256: 87e94e429d58386c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.905
latex_coverage_ratio: 0.945
doc_brief: "THE 3D INDEX OF AN IDEAL TRIANGULATION AND ANGLE STRUCTURES — The 3D index of Dimofte-Gaiotto-Gukov a partially deﬁned function on the set of ideal triangulations of 3-manifolds with r torii boundary"
---
[]{#sub.independent.strict label="sub.independent.strict"}

Theorem [\[thm.IMconv\]](#thm.IMconv){reference-type="ref" reference="thm.IMconv"} implies that $I_{\mathbf M}$ converges when $\mathbf M$ admits a strict index structure. In this section we give an independent proof of this fact without using the restriction of the summand of the index to a ray.

::: proposition
[]{#prop.IMconv.strict label="prop.IMconv.strict"} If $\mathbf M$ supports a strict index structure, then $I_{\mathbf M}(m,e)(q) \in \mathbb Z((q^{1/2}))$ is convergent for all $m,e \in \mathbb Z^s$.
:::

The proof of proposition [\[prop.IMconv.strict\]](#prop.IMconv.strict){reference-type="ref" reference="prop.IMconv.strict"} requires some lemmas.

::: lemma
[]{#lem.Iconv label="lem.Iconv"} Fix positive real numbers $\alpha,\beta>0$ with $\alpha+\beta< 1/2$ and let $\gamma= \min\{\alpha,\beta,1/2-\alpha-\beta\}$. Then for all for all integers $m,e$ we have: $$\delta(I_{\Delta}(m,e) q^{-\beta m + \alpha e}) \geq \gamma\max\{|m|,|e|,|m+e|\} 

\,.$$
:::

::: proof
*Proof.* (of Lemma [\[lem.Iconv\]](#lem.Iconv){reference-type="ref" reference="lem.Iconv"}) Let $L_+(m,e)=\max\{|m|,|e|,|m+e|\}$. $L_+(m,e)$ is a piece-wise linear function given by Figure [1](#fig.Lplus){reference-type="ref" reference="fig.Lplus"}.

<figure id="fig.Lplus">
<div class="center">
<embed src="draws/Lplus.pdf" />
</div>
<figcaption>A piece-wise linear function <span class="math inline"><em>L</em><sub>+</sub></span>.</figcaption>
</figure>

With the notation of Lemma [\[lem.degID\]](#lem.degID){reference-type="ref" reference="lem.degID"}, we need to show that $$\label{eq.degDL}
\delta(m,e)-\beta m + \alpha e \geq \gamma L_+(m,e) \,.$$ First, consider the three rays of $\delta(m,e)$:

::: center
         ray         left hand side of [\[eq.degDL\]](#eq.degDL){reference-type="eqref" reference="eq.degDL"}   right hand side of [\[eq.degDL\]](#eq.degDL){reference-type="eqref" reference="eq.degDL"}
  ----------------- ------------------------------------------------------------------------------------------ -------------------------------------------------------------------------------------------
   $m=0, e \geq 0$                                          $\alpha e$                                                                                 $\gamma e$
   $e=0, m \leq 0$                                          $-\beta m$                                                                                 $-\gamma m$
    $m=-e \geq 0$                                     $m(1/2-\alpha-\beta)$                                                                            $\gamma m$
:::

This proves inequality [\[eq.degDL\]](#eq.degDL){reference-type="eqref" reference="eq.degDL"} in the three rays and shows that the choice of $\gamma$ is optimal. Now, in the interior of each of the $6$ cones of linearity of $L_+$, $\delta(m,e) -\beta m + \alpha e$ is given by a quadratic polynomial of $m,e$. The degree $2$ (resp. $1$) part of this polynomial is always greater than or equal to $1/2 L_+(m,e)$ (resp. $(1/2-\gamma) L_+(m,e)$) by a case computation. For example, in the cone $m \geq 0, e \leq 0, e+m \geq 0$ with rays $\mathbb R_+(1,0)$ and $\mathbb R_+(1,-1)$ we have $\delta(m,e)=m(m+e)/2+m/2$ and $L_+(m,e)=m$ and $$\begin{aligned}
\delta(m,e)-\beta m + \alpha e &=& \frac{m(e+m)}{2}+\frac{m}{2}-\beta m+\alpha e
\\ & \geq & \frac{m}{2} + \frac{m}{2} -\beta m+\alpha e
\\ &= & (1-\beta-\alpha) m + \alpha(m+e) 
\\ & \geq & (1-\beta-\alpha) m \geq (1-\beta-\alpha) L_+(m,e) 
\end{aligned}$$ The other cases are similar. ◻
:::

The next lemma is well-known [@Ziegler].

::: lemma
[]{#lem.Pv label="lem.Pv"} Consider the convex polytope $P$ in $\mathbb R^r$ defined by $$P=\{ x \in \mathbb R^r \, | v_i \cdot x \leq c_i \quad i=1,\dots s \} \,$$ where $v_i \in \mathbb R^r$ and $c_i \in \mathbb R$ for $i=1,\dots,s$. Then $P$ is compact if and only if the linear span of the set $\{v_i| i=1,\dots,s\}$ is $\mathbb R^r$ and $0$ is a $\mathbb R_{\geq 0}$-linear combination of elements of $\{v_i| i=1,\dots,s\}$.
:::

::: proof
*Proof.* (of Proposition [\[prop.IMconv.strict\]](#prop.IMconv.strict){reference-type="ref" reference="prop.IMconv.strict"}) Let $a_i$ and $b_i$ for $i=1,\dots,s$ denote the columns of $(\mathbf A|\mathbf B)$. If $\mathbf M$ admits a strict index structure then there exist $\alpha_i, \gamma_i >0$ that satisfy $a_i + \gamma_i < 1$ for all $i$ such that $$\sum_{i=1}^s \alpha_i a_i + \gamma_i \beta_i = \nu \,.$$ It follows that $$I_{\mathbf M}(m,e)(q)=\sum_{k \in \mathbb Z^r}
\prod_{i=1}^s I(m_i-b_i \cdot k, e_i+a_i \cdot k)(q) 
q^{\frac{\beta_i}{2} b_i \cdot k + \frac{\alpha_i}{2} a_i \cdot k} \,.$$ Applying Lemma [\[lem.Iconv\]](#lem.Iconv){reference-type="ref" reference="lem.Iconv"}, it follows that for every $k \in \mathbb Z^d$, the degree of the summand is bounded below by $$\sum_{i=1}^s \left( \beta_i m_i - \alpha_i e_i \right)
+ \gamma' \sum_{i=1}^s \left( |-m_i+b_i \cdot k| +|e_i+a_i \cdot k| \right)  

\,.$$ Now, Lemma [\[lem.Pv\]](#lem.Pv){reference-type="ref" reference="lem.Pv"} and admissibility implies that for fixed $N_0$, there are finitely many $k \in \mathbb Z^d$ such that the above degree is less than $N_0$. Proposition [\[prop.IMconv.strict\]](#prop.IMconv.strict){reference-type="ref" reference="prop.IMconv.strict"} follows. ◻
:::
