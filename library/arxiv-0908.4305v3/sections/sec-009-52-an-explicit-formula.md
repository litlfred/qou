---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidiﬁcation"
section_id: sec-009-52-an-explicit-formula
section_title: "An Explicit Formula"
section_number: 5.2
pages: 50-52
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 1.0
doc_brief: "Higher Dimensional Algebra VII: Groupoidiﬁcation — Groupoidiﬁcation is a form of categoriﬁcation in which vector spaces are replaced by groupoids and linear operators are replaced by spans of"
---
[]{#explicit label="explicit"}

Our calculations in the proof of Theorem [\[PROCESS1\]](#PROCESS1){reference-type="ref" reference="PROCESS1"} yield an explicit formula for the operator coming from a tame span, and a criterion for when a span is tame:

::: thm
[]{#matrix1 label="matrix1"} A span of groupoids $$\xymatrix{
& S\ar[dl]_{q} \ar[dr]^{p} & \\
Y & & X
}$$ is tame if and only if:

1.  For any object $y\in Y$, the groupoid $p^{-1}(x)\cap q^{-1}(y)$ is nonempty for objects $x$ in only a finite number of isomorphism classes of $X$.

2.  For every $x \in X$ and $y \in Y$, the groupoid $p^{-1}(x)\cap q^{-1}(y)$ is tame.

Here $p^{-1}(x)\cap q^{-1}(y)$ is the subgroupoid of $S$ whose objects lie in both $p^{-1}(x)$ and $q^{-1}(y)$, and whose morphisms lie in both $p^{-1}(x)$ and $q^{-1}(y)$.

If $S$ is tame, then for any $\psi \in {\mathbb R}^{\underline{X}}$ we have $$(\utilde{S} \psi)([y]) = 
\sum_{[x] \in \underline{X}} \;\,
\sum_{[s]\in\underline{p^{-1}(x)}\bigcap \underline{q^{-1}(y)}}
\frac{|{\rm Aut}(x)|}{|{\rm Aut}(s)|} \,\, \psi([x]) \,.$$
:::

::: proof
*Proof.* First suppose the span $S$ is tame and $v \colon\Psi \rightarrow X$ is a tame groupoid over $X$. Equations [\[formula1\]](#formula1){reference-type="ref" reference="formula1"} and [\[formula2\]](#formula2){reference-type="ref" reference="formula2"} show that if $S,X,Y,$ and $\Psi$ are skeletal, and $\Psi$ has just one object $\ast$, then $$\utilde{S \Psi}([y]) = \sum_{s \in p^{-1}(x) \cap q^{-1}(y)}
\frac{|{\rm Aut}(v(\ast))|}{|{\rm Aut}(s)| |{\rm Aut}(\ast)|}$$ On the other hand, $$\utilde{\Psi}([x]) = 
\begin{cases}\displaystyle{\frac{1}{|{\rm Aut}(\ast)|}} 
              & \textrm{if} \; v(\ast) = x \\ 
                                           \\
              0                     & \textrm{otherwise.}  
\end{cases}$$ So in this case, writing $\utilde{\Psi}$ as $\psi$, we have $$(\utilde{S} \psi)([y]) = 
\sum_{[x] \in X} \;\,
\sum_{[s]\in p^{-1}(x) \bigcap q^{-1}(y)}
\frac{|{\rm Aut}(x)|}{|{\rm Aut}(s)|} \,\, \psi([x]) \,.$$ Since both sides are linear in $\psi$, and every nonnegative function in ${\mathbb R}^{\underline{X}}$ is a pointwise convergent nonnegative linear combination of functions of the form $\psi = \utilde{\Psi}$ with $\Psi$ as above, the above equation in fact holds for *all* $\psi
\in {\mathbb R}^{\underline{X}}$.

Since all groupoids in sight are skeletal, we may equivalently write the above equation as $$(\utilde{S} \psi)([y]) = 
\sum_{[x] \in \underline{X}} \;\,
\sum_{[s]\in\underline{p^{-1}(x)}\bigcap \underline{q^{-1}(y)}}
\frac{|{\rm Aut}(x)|}{|{\rm Aut}(s)|} \,\, \psi([x]) \,.$$ The advantage of this formulation is that now both sides are unchanged when we replace $X$ and $Y$ by equivalent groupoids, and replace $S$ by an equivalent span. So, this equation holds for all tame spans, as was to be shown.

If the span $S$ is tame, the sum above must converge for all functions $\psi$ of the form $\psi = \utilde{\Psi}$. Any nonnegative function $\psi \colon\underline{X} \rightarrow{\mathbb R}$ is of this form. For the sum above to converge for *all* nonnegative $\psi$, this sum: $$\sum_{[s]\in\underline{p^{-1}(x)}\bigcap \underline{q^{-1}(y)}}
\frac{|{\rm Aut}(x)|} {|{\rm Aut}(s)|}$$ must have the following two properties:

1.  For any object $y \in Y$, it is nonzero only for objects $x$ in a finite number of isomorphism classes of $X$.

2.  For every $x \in X$ and $y \in Y$, it converges to a finite number.

These conditions are equivalent to conditions 1) and 2) in the statement of the theorem. We leave it as an exercise to check that these conditions are not only necessary but also sufficient for $S$ to be tame. ◻
:::

The previous theorem has many nice consequences. For example:

::: proposition
[]{#add_spans label="add_spans"} Suppose $S$ and $T$ are tame spans from a groupoid $X$ to a groupoid $Y$. Then $\utilde{S+T} = \utilde{S} + \utilde{T}$.
:::

::: proof
*Proof.* This follows from the explicit formula given in Theorem [\[matrix1\]](#matrix1){reference-type="ref" reference="matrix1"}. ◻
:::
