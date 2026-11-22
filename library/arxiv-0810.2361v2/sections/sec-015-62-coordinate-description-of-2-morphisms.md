---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS"
section_id: sec-015-62-coordinate-description-of-2-morphisms
section_title: "Coordinate Description of 2-Morphisms"
section_number: 6.2
pages: 35-38
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.98
doc_brief: "2-VECTOR SPACES AND GROUPOIDS — This paper describes a relationship between essentially ﬁnite groupoids and 2-vector spaces."
---
[]{#sec:coordY label="sec:coordY"}

In this section, we discuss the behaviour of $\Lambda$ on 2-morphisms, namely the assignment of a natural transformation to a span of span maps. As discussed in Section [\[sec:kv2vsgrpd\]](#sec:kv2vsgrpd){reference-type="ref" reference="sec:kv2vsgrpd"}, any natural transformation between a pair of 2-linear maps between KV 2-vector spaces can be represented as a matrix of linear operators, as in ([\[eq:kvnattransmatrix\]](#eq:kvnattransmatrix){reference-type="ref" reference="eq:kvnattransmatrix"}). We would like to describe explicitly the linear maps composing $\Lambda(Y)$ and some consequences.

To motivate the rest, we can begin with the special case of $\hom_{\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})}(\boldsymbol{\operatorname{{1}}},\boldsymbol{\operatorname{{1}}})$, where $\boldsymbol{\operatorname{{1}}}$ is the trivial groupoid with one object (which we denote $\star$) and its identity morphism. We can summarize the effect of $\Lambda$ on this $\hom$-category by the following theorem:

::: theorem
[]{#thm:groupoidification label="thm:groupoidification"} On $\hom_{\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})}(\boldsymbol{\operatorname{{1}}},\boldsymbol{\operatorname{{1}}})$, the 2-functor $\Lambda$, expressed in coordinates, reproduces groupoidification in the sense of ([\[eq:baezgpdify\]](#eq:baezgpdify){reference-type="ref" reference="eq:baezgpdify"}).
:::

::: proof
*Proof.* First, we note that $\Lambda(\boldsymbol{\operatorname{{1}}}) \cong \boldsymbol{\operatorname{{Vect}}}$, since the only irreducible representation of the trivial group (basis object) is $\mathbb{C}$ itself.

Since $\boldsymbol{\operatorname{{1}}}$ is terminal in $\boldsymbol{\operatorname{{FinGpd}}}$, any groupoid has a unique map into it. Thus, any span from $\boldsymbol{\operatorname{{1}}}$ to $\boldsymbol{\operatorname{{1}}}$ is of the form: $$\boldsymbol{\operatorname{{1}}} \stackrel{!}{\mathop{\leftarrow}} X \stackrel{!}{\mathop{\rightarrow}} \boldsymbol{\operatorname{{1}}}$$ which just amounts to a choice of $X$. Then $\Lambda(X) = !_{\ast}
!^{\ast}$ can be described as a $1 \times 1$ matrix of vector spaces, $$\begin{aligned}
\Lambda(X)_{(\star,\mathbb{C}),(\star,\mathbb{C})} & = \hom(!^{\ast}\mathbb{C},!^{\ast}\mathbb{C}) \\
 & \cong \bigoplus_{[x] \in \underline{X}} \mathbb{C}
\end{aligned}$$ since $!^{\ast}\mathbb{C}$ is the representation of $X$ assigning a copy of $\mathbb{C}$ to each object. In particular, inducing up the representation $\mathbb{C}$ gives, at each $x \in X$, the representation $$\mathbb{C}[Aut(\star)] \otimes_{\mathbb{C}[Aut(x)]} \mathbb{C} = \mathbb{C}$$ since $!^{\ast}\mathbb{C}$, is the trivial representation of $Aut(x)$.

For each isomorphism class in $\underline{X}$, we thus get a copy of $\hom{\mathbb{C},\mathbb{C}
  \cong \mathbb{C}}$. This is the vector space associated to $X$ by groupoidification.

Similarly, a 2-morphism $Y : X_1 \mathop{\rightarrow}X_2$ just amounts to an isomorphism class of spans of groupoids (since $Y$ and the $X_i$ have unique maps to $\boldsymbol{\operatorname{{!}}}$. Then the linear map $$\Lambda(Y)_{(\star,\mathbb{C}),(\star,\mathbb{C})} : \Lambda(X_1)_{(\star,\mathbb{C}),(\star,\mathbb{C})} \mathop{\rightarrow}\Lambda(X_2)_{(\star,\mathbb{C}),(\star,\mathbb{C})}$$ just becomes a map $$T(Y) : \mathbb{C}[\underline{X_1}] \mathop{\rightarrow}\mathbb{C}[\underline{X_2}]$$ given by $T(Y) = \epsilon_{L,t} \circ \eta_{R,s}$.

By the above, ([\[eq:rightunit\]](#eq:rightunit){reference-type="ref" reference="eq:rightunit"}), using $F(x_1) \cong \mathbb{C}$, can be written:

$$\eta_{R,s}(F)(y) : \mathbb{C} \mathop{\rightarrow}\bigoplus_{[y] | s(y) \cong x_1} \mathbb{C}[Aut(x_1)] \otimes_{\mathbb{C}[Aut(y)]} \mathbb{C}$$ So now for each $[x_1] \in \underline{X_1}$, every $y$ in the essential preimage of $x_1$ under $s$ gets a copy of the trivial representation $\mathbb{C}$ for each coset of $Im(Aut(y))$ in $Aut((x_1)$. This describes a decomposition of a representation of $Aut(y)$ in terms of irreps (all of which are necessarily trivial in this case). Call this representation $G$. In particular, a vector in $\Lambda{X_1}_{(\star,\mathbb{C}),(\star,\mathbb{C})}$ gives a complex number at each $[x_1]$. The unit $\eta_{R,s}$ takes such a vector $v$ to, at each $y$ with $s(y) \cong x_1$, $$\frac{1}{\# Aut(y)} \sum_{g \in Aut(x_1)} g^{-1} \otimes 1$$

By commutativity for the span of span maps (which is necessarily strict here!), we also must have that $$\bigoplus_{[y'] | t(y') \cong t(y)} \mathbb{C}[Aut(t(y))] \otimes_{\mathbb{C}[Aut(y')]}G(y') \cong \bigoplus_{[y'] | s(y') \cong s(y)} \mathbb{C}[Aut(s(y))] \otimes_{\mathbb{C}[Aut(y)]}\mathbb{C}$$

Similarly, then, using this ([\[eq:rightcounit\]](#eq:rightcounit){reference-type="ref" reference="eq:rightcounit"}) can be written: $$\epsilon_{L,t}(G)(y) : \bigoplus_{[y'] | t(y') \cong t(y)} \mathbb{C}[Aut(t(y))] \otimes_{\mathbb{C}[Aut(y')]}G(y') \mathop{\rightarrow}G(y)$$

So now consider the vector $v \in
\Lambda(X_1)_{(\star,\mathbb{C}),(\star,\mathbb{C})}$ which gives $1$ at $[x_1]$ and $0$ elsewhere. (That is, it gives the identity intertwining map between the copies of the representation $!^{\ast}\mathbb{C}$ at objects in $[x_1]$ and the zero intertwiner elsewhere). Then the natural transformation induces a map on the coefficient: $$\eta_{R,s}: v \mapsto \bigoplus_{[y] | s(y) \cong x_1} \frac{1}{\# Aut(y)} \sum_{g \in Aut(x_1)} g^{-1} \otimes 1$$ but then suppose we look for the coefficient of the result at $[x_2]
\in \underline{X_2}$. Only those $y$ over $[x_2]$ will contribute, but then, since the $g^{-1}$ have no effect on vectors in $\mathbb{C}$, we get: $$\epsilon_{L,t} : \bigoplus_{[y] | s(y) \cong x_1} \frac{1}{\# Aut(x_1)} \sum_{g \in Aut(x_1)} g^{-1} \otimes 1 \mapsto \sum_{y | (s,t)(y) \cong (x_1,x_2)} \frac{\# Aut(x_1)}{\# Aut(y)}$$

But this is just $$\# Aut(x_1) \sum_{y | (s,t)(y) \cong (x_1,x_2)} \frac{1}{\# Aut(y)} = \# Aut(x_1) | \widehat{(x_1,x_2)} |$$ where the second term is the groupoid cardinality of the essential preimage of $(x_1,x_2)$. This is just the coefficient we find in groupoidification in the sense of Baez and Dolan. ◻
:::

Similar calculations apply for less trivial situations as well, although for these we will require a little more of the representation theory of the groupoids $A_i$.

::: lemma
[]{#lemma:coordFVY label="lemma:coordFVY"}Given a (strict) span between spans, $Y : X_1 \mathop{\rightarrow}X_2$, for $X_1,X_2 : A_1 \mathop{\rightarrow}A_2$, then the natural transformation $$\Lambda(Y) : \Lambda(X_1) \mathop{\rightarrow}\Lambda(X_2)$$ is a natural transformation given by a matrix of linear operators: $$\Lambda(Y)_{([a_1],W_1),([a_2],W_2)} : \Lambda(X_2)_{([a_1],W_1),([a_2],W_2)} \mathop{\rightarrow}\Lambda(X_2)_{([a_1],W_1),([a_2],W_2)}$$ or equivalently $$\begin{aligned}
\label{eq:FVYhomsets}
\Lambda(Y)_{([a_1],W_1),([a_2],W_2)} & : \bigoplus_{[x_1]}\operatorname{hom}_{Rep(\operatorname{Aut}(x_1))}[s_1^{\ast}(W_1),t_1^{\ast}(W_2)]\\ 
\nonumber & \mathop{\rightarrow}\bigoplus_{[x_2]}\operatorname{hom}_{Rep(\operatorname{Aut}(x_2))}[s_2^{\ast}(W_1),t_2^{\ast}(W_2)]
\end{aligned}$$

Such that for each block $([x_1],[x_2])$, the corresponding linear operator behaves as follows: for $f \in
\operatorname{hom}[s_1^{\ast}(W_1),t_1^{\ast}(W_2)]$ we get: $$\Lambda(Y)_{([a_1],W_1),([a_2],W_2)}|_{(x_1,x_2)}(f) = |\widehat{(x_1,x_2)}| \sum_{g \in \operatorname{Aut}(x_1)} g^{-1} f g$$ where $\widehat{(x_1,x_2)}$ is the *essential preimage* of $(x_1,x_2)$ under $(s,t)$, namely the comma category $((s,t)
\downarrow (x_1,x_2))$.
:::

::: proof
*Proof.* The argument here is similar to that in Theorem [\[thm:groupoidification\]](#thm:groupoidification){reference-type="ref" reference="thm:groupoidification"}, except that we must deal with nontrivial representations of the $Aut(x_i)$. That is, when we apply the Nakayama isomorphism, and the evaluation maps, we cannot use triviality. The "group-averaging" acting on intertwiners in the expression we have given is exactly the exterior trace used in the Nakayama isomorphism. Here its function is to project a linear map (a "pulled-back" intertwiner) onto a space of intertwiners as we push it along the functor $t$.

In particular, the effect of $\eta_R,s$ on coordinates (i.e. choosing particular representations $W_i$) is to take an intertwiner $f \in
\operatorname{hom}[s_1^{\ast}(W_1),t_1^{\ast}(W_2)]$ and produce an intertwiner at the representations pulled back to $Y$. The counit $\eta_L,t$ "pushes" this down to an intertwiner in $\operatorname{hom}[s_2^{\ast}(W_1),t_2^{\ast}(W_2)]$. The group averaging ensures this will be an intertwiner itself. ◻
:::

::: remark
Using the formula for composition of 2-linear maps and natural transformations in a general 2-vector space, we can readily see how horizontal and vertical composition work.

Vertical composition is given by composition of linear maps component-wise, so we have: $$\Lambda(Y' \circ Y)_{([a_1],W_1),([a_2],W_2)}$$ with components given by by: $$\begin{aligned}
& \bigoplus_{([x_1],[x_3])} |\widehat{(x_1,x_3)}| \sum_{g \in \operatorname{Aut}(x_3)} g^{-1} f g \\
\nonumber = & \bigoplus_{([x_1],[x_3])} \sum_{[x_2]} |\widehat{(x_2,x_3)}| \cdot |\widehat{(x_1,x_2)}| \cdot \#\operatorname{Aut}(x_2) \Bigl{(} \sum_{g \in \operatorname{Aut}(x_3)} g^{-1} f g \Bigr{)}
\end{aligned}$$

This uses the fact that the two group averages each give projections into spaces of intertwiners, which is redundant, so we omit one, taking only the order of the group. We also use that $\widehat{(x_1,x_3)}$ is a subgroupoid of $Y' \circ Y$. In fact, it is a union over all equivalence classes $[x_2]$ in $X_2$ of the objects in the weak pullback $Y' \circ Y$ based over $[x_2]$, which gives the sum over $[x_2]$ (which performs the matrix multiplication in each component).

The horizontal composite, $\Lambda(Y' \circ Y) \cong \Lambda(Y') \circ
\Lambda(Y)$, on the other hand, involves "matrix multiplication" at the level of composition of 2-linear maps. The $(([a_1],W_1),([a_3],W_3))$ component of the product is a linear map given as a block matrix with one block for each basis 2-vector. The blocks consist of the tensor products of the matrices from the components of $\Lambda(Y)$ and $\Lambda(Y')$. In particular, the $\beta$ isomorphisms from the horizontal composition of source and target induce an isomorphism which acts on intertwiners $\iota \otimes \iota '$ by: $$\begin{aligned}
& \bigl{(} \bigoplus_{\stackrel{([x_1,f_1,x'_1])}{([x_2,f_2,x'_2])}} |\widehat{((x_1,x'_1),(x_2,x'_2))}| \sum_{(g,g') \in \operatorname{Aut}([x_1],[x'_1])} (g,g')^{-1} \iota \otimes \iota ' (g,g') \bigr{)} \\
\nonumber \cong & \bigoplus_{([a_2],W_2)} \Bigl{(} \bigoplus_{([x_1],[x_2])} |\widehat{(x_1,x_2)}| \sum_{g \in \operatorname{Aut}(x_1)} g^{-1} \iota g\Bigr{)} \otimes \bigl{(}\bigoplus_{([x'_1],[x'_2])} |\widehat{(x'_1,x'_2)}| \sum_{g' \in \operatorname{Aut}(x'_1)} (g')^{-1} \iota ' g' \Bigr{)} \\
\nonumber = & \bigoplus_{([a_2],W_2)} \Bigl{(} \bigoplus_{\stackrel{([x_1],[x_2])}{([x'_1],[x'_2])}} |\widehat{(x_1,x_2)}| \cdot |\widehat{(x'_1,x'_2)}| \sum_{(g,g') \in \operatorname{Aut}(x_1) \times \operatorname{Aut}(x'_1)} (g,g')^{-1} \iota \otimes \iota ' (g,g')\Bigr{)}
\end{aligned}$$

Here, we note that since $Y' \circ Y$ is a weak pullback over $A_2$, its objects consist of triples $(y,h,y')$, we implicitly have a sum over $[y,h,y']$ in the groupoid cardinality, which is $|\widehat{(x_1,x_2)}| \cdot |\widehat{(x'_1,x'_2)}| \cdot
|\operatorname{Aut}(a_2)$.
:::
