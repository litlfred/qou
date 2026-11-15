---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidiﬁcation"
section_id: sec-002-3-homology-versus-cohomology
section_title: "Homology versus Cohomology"
section_number: 3
pages: 25-29
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
toc_source: outline
text_source: latex
latex_prose_ratio: 0.929
latex_coverage_ratio: 0.996
doc_brief: "Higher Dimensional Algebra VII: Groupoidiﬁcation — Groupoidiﬁcation is a form of categoriﬁcation in which vector spaces are replaced by groupoids and linear operators are replaced by spans of"
---
[]{#homology label="homology"}

The work we have described so far has its roots in the cohomology of groupoids. Any groupoid $X$ can be turned into a topological space, namely the geometric realization of its nerve [@GJ], and we can define the cohomology of $X$ to be the cohomology of this space. The set of connected components of this space is just the set of isomorphism classes of $X$, which we have denoted $\underline{X}$. So, the **zeroth cohomology** of the groupoid $X$, with real coefficients, is precisely the vector space ${\mathbb R}^{\underline{X}}$ that we have been calling the degroupoidification of $X$.

Indeed, one reason degroupoidification has been overlooked until recently is that every groupoid is equivalent to a disjoint union of one-object groupoids, which we may think of as groups. To turn a groupoid into a topological space it suffices to do this for each of these groups and then take the disjoint union. The space associated to a group $G$ is quite famous: it is the Eilenberg--Mac Lane space $K(G,1)$. Similarly, the cohomology of groups is a famous and well-studied subject. But the zeroth cohomology of a group is always just ${\mathbb R}$. So, zeroth cohomology is not considered interesting. Zeroth cohomology only becomes interesting when we move from groups to groupoids---and then only when we consider how a tame span of groupoids induces a map on zeroth cohomology.

These reflections suggest an alternate approach to degroupoidification based on homology instead of cohomology:

::: definition
Given a groupoid $X$, let the **zeroth homology** of $X$ be the real vector space with the set $\underline{X}$ as basis. We denote this vector space as ${\mathbb R}[\underline{X}]$.
:::

We can also think of ${\mathbb R}[\underline{X}]$ as the space of real-valued functions on $\underline{X}$ with finite support. This makes it clear that the zeroth homology ${\mathbb R}[\underline{X}]$ can be identified with a subspace of the zeroth cohomology ${\mathbb R}^{\underline{X}}$. If $X$ has finitely many isomorphism classes of objects, then the set $\underline{X}$ is finite, and the zeroth homology and zeroth cohomology are canonically isomorphic. For a groupoid with infinitely many isomorphism classes, however, the difference becomes important. The following example makes this clear:

::: example
[]{#polynomials label="polynomials"} [Let $E$ be the groupoid of finite sets and bijections. In Example [\[power_series\]](#power_series){reference-type="ref" reference="power_series"} we saw that $${\mathbb R}^{\underline{E}} \; \cong\; \lbrace \psi \colon{\mathbb N}\rightarrow{\mathbb R}\rbrace 
\; \cong \; {\mathbb R}[[z]] .$$ So, elements of ${\mathbb R}[\underline{E}]$ may be identified with formal power series with only finitely many nonzero coefficients. But these are just polynomials: $${\mathbb R}[\underline{E}] \; \cong \; {\mathbb R}[z]  .$$]{.upright}
:::

Before pursuing a version of degroupoidification based on homology, we should ask if there are other choices built into our recipe for degroupoidification that we can change. The answer is yes. Recalling Equation [\[operator_formula\]](#operator_formula){reference-type="ref" reference="operator_formula"}, which describes the operator associated to a tame span: $$(\utilde{S} \psi)([y]) = 
\sum_{[x] \in \underline{X}} \;\,
\sum_{[s]\in\underline{p^{-1}(x)}\bigcap \underline{q^{-1}(y)}}
\frac{|{\rm Aut}(x)|}{|{\rm Aut}(s)|} \,\, \psi([x]) \,.$$ one might wonder about the asymmetry of this formula. Specifically, one might wonder why this formula uses information about ${\rm Aut}(x)$ but not ${\rm Aut}(y)$. The answer is that we made an arbitrary choice of conventions. There is another equally nice choice, and in fact an entire family of choices interpolating between these two:

::: proposition
[]{#cohomological_alpha_degroupoidification label="cohomological_alpha_degroupoidification"} Given $\alpha \in {\mathbb R}$ and a tame span of groupoids: $$\xymatrix{
 & S\ar[dl]_q\ar[dr]^p & \\
 Y & & X \\
}$$ there is a linear operator called its **$\alpha$-degroupoidification**: $$\utilde{S_\alpha}\colon{\mathbb R}^{\underline{X}}\rightarrow{\mathbb R}^{\underline{Y}}$$ given by: $$(\utilde{S_\alpha} \psi)([y]) = 
\sum_{[x] \in \underline{X}} \;\,
\sum_{[s]\in\underline{p^{-1}(x)}\bigcap \underline{q^{-1}(y)}}
\frac{|{\rm Aut}(x)|^{1-\alpha}|{\rm Aut}(y)|^\alpha}{|{\rm Aut}(s)|} \,\, \psi([x]) \,.$$
:::

::: proof
*Proof.* The only thing that needs to be checked is that the sums converge for any fixed choice of $y \in Y$. This follows from our explicit criterion for tameness of spans, Theorem [\[matrix1\]](#matrix1){reference-type="ref" reference="matrix1"}. ◻
:::

The most interesting choices of $\alpha$ are $\alpha = 0$, $\alpha =
1$, and the symmetrical choice $\alpha = 1/2$. The last convention has the advantage that for a tame span $S$ with tame adjoint $S^\dagger$, the matrix for the degroupoidification of $S^\dagger$ is just the transpose of that for $S$. We can show:

::: proposition
[]{#alphaspancompose label="alphaspancompose"} For any $\alpha \in {\mathbb R}$ there is a functor from the category of groupoids and equivalence classes of tame spans to the category of real vector spaces and linear operators, sending:

-   each groupoid $X$ to its zeroth cohomology ${\mathbb R}^{\underline{X}}\,$, and

-   each tame span $S$ from $X$ to $Y$ to the operator $\utilde{S_\alpha} \colon{\mathbb R}^{\underline{X}} \rightarrow{\mathbb R}^{\underline{Y}}\,$.

In particular, if we have composable tame spans: $$\xymatrix{
& T\ar[dl]_{} \ar[dr]^{} & & S \ar[dl]_{} \ar[dr]^{}& \\
Z & & Y & & X
}$$ then their composite $$\xymatrix{
 & TS \ar[dl]_{} \ar[dr]^{} & \\
 Z & & X \\
}$$ is again tame, and $$\utilde{(TS)_\alpha} = \utilde{T_\alpha} \utilde{S_\alpha}  .$$
:::

We omit the proof because it mimics that of Theorem [\[functor\]](#functor){reference-type="ref" reference="functor"}. Note that a groupoid $\Psi$ over $X$ can be seen as a special case of a span, namely a span $$\xymatrix{
 & \Psi \ar[dl]_{v} \ar[dr]^{} & \\
 X & & 1 \\
}$$ where $1$ is the terminal groupoid---that is, the groupoid with one object and one morphism. So, $\alpha$-degroupoidification also gives a recipe for turning $\Psi$ into a vector in ${\mathbb R}^{\underline{X}}\,$: $$\label{alpha_degroupoidification_formula}
\utilde{\Psi_\alpha}{[x]} = |{\rm Aut}(x)|^\alpha {|v^{-1}(x)|} \,.$$ This idea yields the following result as a special case of Proposition [\[alphaspancompose\]](#alphaspancompose){reference-type="ref" reference="alphaspancompose"}:

::: proposition
[]{#alpha_degroupoidification_vector label="alpha_degroupoidification_vector"} Given a tame span: $$\xymatrix{
& S \ar[dl]_{q} \ar[dr]^{p}& \\
Y & & X
}$$ and a tame groupoid over $X$, say $v\colon\Psi\rightarrow X$, then $\utilde{(S\Psi)_\alpha}=\utilde{S_\alpha}\utilde{\Psi_\alpha}$
:::

Equation [\[alpha_degroupoidification_formula\]](#alpha_degroupoidification_formula){reference-type="ref" reference="alpha_degroupoidification_formula"} also implies that we can compensate for a different choice of $\alpha$ by doing a change of basis. So, our choice of $\alpha$ is merely a matter of convenience. More precisely:

::: proposition
Regardless of the value of $\alpha \in {\mathbb R}$, the functors in Proposition [\[alphaspancompose\]](#alphaspancompose){reference-type="ref" reference="alphaspancompose"} are all naturally isomorphic.
:::

::: proof
*Proof.* Given $\alpha,\beta \in {\mathbb R}$, Equation [\[alpha_degroupoidification_formula\]](#alpha_degroupoidification_formula){reference-type="ref" reference="alpha_degroupoidification_formula"} implies that $$\utilde{\Psi_\alpha}{[x]} = |{\rm Aut}(x)|^{\alpha-\beta} 
\utilde{\Psi_\beta}{[x]}$$ for any tame groupoid $\Psi$ over a groupoid $X$. So, for any groupoid $X$, define a linear operator $$T_X \colon{\mathbb R}[\underline{X}] \rightarrow{\mathbb R}[\underline{X}]$$ by $$(T_X \psi)([x]) = |{\rm Aut}(x)|^{\alpha-\beta} \psi([x])  .$$ We thus have $$\utilde{\Psi_\alpha} = T_X \utilde{\Psi_\beta}  .$$

By Proposition [\[alpha_degroupoidification_vector\]](#alpha_degroupoidification_vector){reference-type="ref" reference="alpha_degroupoidification_vector"}, for any tame span $S$ from $X$ to $Y$ and any tame groupoid $\Psi$ over $X$ we have $$\begin{array}{ccl}
 T_Y \utilde{S_\alpha} \utilde{\Psi_\alpha} 
&=& T_Y \utilde{(S\Psi)_\alpha} \\
&=& \utilde{(S\Psi)_\beta} \\
&=& \utilde{S_\beta} \utilde{\Psi_\beta} \\
&=& \utilde{S_\beta} T_X \utilde{\Psi_\alpha} 
\end{array}$$ Since this is true for all such $\Psi$, this implies $$T_Y \utilde{S_\alpha} = \utilde{S_\beta} T_X  .$$ So, $T$ defines a natural isomorphism between $\alpha$-degroupoidification and $\beta$-degroupoidification. ◻
:::

Now let us return to homology. We can also do $\alpha$-degroupoidification using zeroth homology instead of zeroth cohomology. Recall that while the zeroth cohomology of $X$ consists of all real-valued functions on $\underline{X}$, the zeroth homology consists of such functions *with finite support*. So, we need to work with groupoids over $X$ that give functions of this type:

::: definition
A groupoid $\Psi$ over $X$ is **finitely supported** if it is tame and $\utilde{\Psi}$ is a finitely supported function on $\underline{X}$.
:::

Similarly, we must use spans of groupoids that give linear operators preserving this finite support property:

::: definition
[]{#finitetypespan label="finitetypespan"} A span: $$\xymatrix{
& S \ar[dl]_{q} \ar[dr]^{p}& \\
Y & & X
}$$ is of **finite type** if it is a tame span of groupoids and for any finitely supported groupoid $\Psi$ over $X$, the groupoid $S\Psi$ over $Y$ (formed by weak pullback) is also finitely supported.
:::

With these definitions, we can refine the previous propositions so they apply to zeroth homology:

::: proposition
[]{#homological_alpha_degroupoidification label="homological_alpha_degroupoidification"} Given any fixed real number $\alpha$ and a span of finite type: $$\xymatrix{
 & S\ar[dl]_q\ar[dr]^p & \\
 Y & & X \\
}$$ there is a linear operator called its **$\alpha$-degroupoidification**: $$\utilde{S_\alpha}\colon{\mathbb R}[\underline{X}] \rightarrow{\mathbb R}[\underline{Y}]$$ given by: $$\utilde{S_\alpha} [x] =
\sum_{[y] \in \underline{Y}} \;\,
\sum_{[s]\in\underline{p^{-1}(x)}\bigcap \underline{q^{-1}(y)}}
\frac{|{\rm Aut}(x)|^{1-\alpha}|{\rm Aut}(y)|^\alpha}{|{\rm Aut}(s)|} \,\, [y]   \, .$$
:::

::: proposition
[]{#alphaspancomposefinite label="alphaspancomposefinite"} For any $\alpha \in {\mathbb R}$ there is a functor from the category of groupoids and equivalence classes of spans of finite type to the category of real vector spaces and linear operators, sending:

-   each groupoid $X$ to its zeroth homology ${\mathbb R}[\underline{X}]$, and

-   each span $S$ of finite type from $X$ to $Y$ to the operator $\utilde{S_\alpha}\colon{\mathbb R}[\underline{X}] \rightarrow{\mathbb R}[\underline{Y}]$.

Moreover, for all values of $\alpha \in {\mathbb R}$, these functors are naturally isomorphic.
:::

::: proposition
Given a span of finite type: $$\xymatrix{
& S \ar[dl]_{q} \ar[dr]^{p}& \\
Y & & X
}$$ and a finitely supported groupoid over $X$, say $v\colon\Psi\rightarrow X$, then $S\Psi$ is a finitely supported groupoid over $Y$, and $\utilde{(S\Psi)_\alpha} = 
\utilde{S_\alpha}\utilde{\Psi_\alpha}$.
:::

The moral of this section is that we have several choices to make before we apply degroupoidification to any specific example. The choice of $\alpha$ is merely a matter of convenience, but there is a real difference between homology and cohomology, at least for groupoids with infinitely many nonisomorphic objects. The process described in Section [\[degroupoidification\]](#degroupoidification){reference-type="ref" reference="degroupoidification"} is the combination of choosing to work with cohomology and the convention $\alpha=0$ for degroupoidifying spans. This will suffice for the majority of this paper. However, we will use a different choice in our study of Hall algebras.
