---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS"
section_id: sec-008-42-the-ambidextrous-adjunction
section_title: "The Ambidextrous Adjunction"
section_number: 4.2
pages: 16-19
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.988
doc_brief: "2-VECTOR SPACES AND GROUPOIDS — This paper describes a relationship between essentially ﬁnite groupoids and 2-vector spaces."
---
[]{#sec:ambadj label="sec:ambadj"}

Now we want to highlight a result analogous to a standard result for set-valued presheaves (see, e.g. MacLane and Moerdijk [@macmoer], Theorem 1.9.2). This is that functors between groupoids induce 2-linear maps between the 2-vector spaces of $\boldsymbol{\operatorname{{Vect}}}$-presheaves on them. For $\boldsymbol{\operatorname{{Set}}}$-presheaves, there will be a left and a right adjoint to this functor. For $\boldsymbol{\operatorname{{Vect}}}$-presheaves, these coincide, as we have seen in Theorem [\[thm:biadjoint\]](#thm:biadjoint){reference-type="ref" reference="thm:biadjoint"} (an inspection of the proof shows that this is essentially because a finite dimensional vector space $V$ is naturally isomorphic to its double dual $V^{\dagger \dagger}$, while the analogous statement is false for sets). Thus, one says that the "pushforward" map is an *ambidextrous adjoint* for the pullback. For much more on ambidextrous adjunctions and their relation to TQFTs, see Lauda [@laudaambidjunction]). This is one important motivation for the present work. We summarize the statement as follows.

::: proposition
[]{#thm:2mapadjoints label="thm:2mapadjoints"}If $\boldsymbol{\operatorname{{X}}}$ and $\boldsymbol{\operatorname{{Y}}}$ are essentially finite groupoids, a functor $f:\boldsymbol{\operatorname{{Y}}}\mathop{\rightarrow}\boldsymbol{\operatorname{{X}}}$ gives two 2-linear maps between KV 2-vector spaces: $$f^{\ast} : [ \boldsymbol{\operatorname{{X}}}, \boldsymbol{\operatorname{{Vect}}}] \mathop{\rightarrow}[\boldsymbol{\operatorname{{Y}}},\boldsymbol{\operatorname{{Vect}}}]$$ called "pullback along $f$" and $$f_{\ast} : [\boldsymbol{\operatorname{{Y}}},\boldsymbol{\operatorname{{Vect}}}] \mathop{\rightarrow}[\boldsymbol{\operatorname{{X}}},\boldsymbol{\operatorname{{Vect}}}]$$ the (two-sided) adjoint to $f^{\ast}$, called "pushforward along $f$"
:::

::: proof
*Proof.* For any functor $F: \boldsymbol{\operatorname{{X}}}\mathop{\rightarrow}\boldsymbol{\operatorname{{Vect}}}$, $$f^{\ast}(F) = F \circ f$$ which is a functor from $\boldsymbol{\operatorname{{Y}}}$ to $\boldsymbol{\operatorname{{Vect}}}$, the pullback of $F$ along $f$.

To see that this is a 2-linear map, we recall that it is enough to show it is $\mathbb{C}$-linear, since then biproducts will automatically be preserved. But a linear combination of maps in some $\hom$-category in $[\boldsymbol{\operatorname{{X}}},\boldsymbol{\operatorname{{Vect}}}]$ is taken by $f^{\ast}$ to the corresponding linear combination in the $\hom$-category in $[\boldsymbol{\operatorname{{Y}}},\boldsymbol{\operatorname{{Vect}}}]$, where maps are now between vector spaces thought of over $y \in \boldsymbol{\operatorname{{Y}}}$.

So indeed there is a 2-linear map $f^{\ast}$. But then by Theorem [\[thm:biadjoint\]](#thm:biadjoint){reference-type="ref" reference="thm:biadjoint"}, there is a two-sided adjoint of $f^{\ast}$, denoted $f_{\ast}$. ◻
:::

<figure id="fig:grpdfn">
<div class="center">
<embed src="grpd-functor.eps" />
</div>
<figcaption><span id="fig:grpdfn" label="fig:grpdfn"></span>A Functor <span class="math inline"><em>F</em> : <strong>Y</strong>  → <strong>X</strong> </span> Between Groupoids</figcaption>
</figure>

In Figure [1](#fig:grpdfn){reference-type="ref" reference="fig:grpdfn"}, we see the essential information contained in a functor of groupoids. Any groupoid is equivalent to a skeletal one (that is, one with just one object in each isomorphism class), so we illustrate this case. A skeletal groupoid can be seen as a set of objects, each labelled by a group. A functor between groupoids is a set map, where each "strand" of the set map (i.e. each pair $(y_i,x_j)$ of source and image under the map) is labelled by a homomorphism $f_i$. This takes the group $G_i$ of automorphisms of the source $y_i$ to the group $H_j$ of automorphisms of the target $x_j$.

It will be useful to have another, more explicit, way to describe the "pushforward" map than the matrix-dependent view of Theorem [\[thm:biadjoint\]](#thm:biadjoint){reference-type="ref" reference="thm:biadjoint"}. Fortunately, there is a more intrinsic way to describe the 2-linear map $f_{\ast}$, the adjoint of $f^{\ast}$.

::: definition
[]{#def:pushcolimit label="def:pushcolimit"} For a given $x \in \boldsymbol{\operatorname{{X}}}$, the *comma category* $(f \downarrow x)$ has objects which are objects $y \in \boldsymbol{\operatorname{{Y}}}$ equipped with maps $f(y) \mathop{\rightarrow}
x$ in $\boldsymbol{\operatorname{{X}}}$, and morphisms which are morphisms $a : y \mathop{\rightarrow}y'$ whose images make the triangles $$\xymatrix{
f(y) \ar[d] \ar[r]^{f(a)} & f(y') \ar[dl] \\
x
}$$ in $\boldsymbol{\operatorname{{X}}}$ commute. Given a $\boldsymbol{\operatorname{{Vect}}}$-presheaf $G$ on $\boldsymbol{\operatorname{{Y}}}$, define $f_{\ast}(G)(x) = \operatorname{colim}G(f \downarrow x)$---a colimit in $\boldsymbol{\operatorname{{Vect}}}$.

The pushforward of a morphism $b:x \mathop{\rightarrow}x'$ in $\boldsymbol{\operatorname{{X}}}$, $f_{\ast}(G)(b) :
f_{\ast}(G)(x) \mathop{\rightarrow}f_{\ast}(G)(x')$ is the induced morphism.
:::

The comma category is the appropriate categorical equivalent of a *preimage*---rather than requiring $f(y) = x$, one accepts that they may be isomorphic, in different ways. So this colimit is a categorified equivalent of taking a sum over a preimage. The result is the *Kan extension* of $G$ along $f$.

Consider the effect of $f_{\ast}$ on a 2-vector $G:\boldsymbol{\operatorname{{Y}}}\mathop{\rightarrow}\boldsymbol{\operatorname{{Vect}}}$ by describing $f_{\ast}G : \boldsymbol{\operatorname{{X}}}\mathop{\rightarrow}\boldsymbol{\operatorname{{Vect}}}$. If $F : \boldsymbol{\operatorname{{X}}}\mathop{\rightarrow}\boldsymbol{\operatorname{{Vect}}}$ is as above, there should be a canonical isomorphism between $[G,f^{\ast}(F)]$ (a hom-set in $[\boldsymbol{\operatorname{{Y}}},\boldsymbol{\operatorname{{Vect}}}]$) and $[p_{\ast}(G),F]$ (a hom-set in $[\boldsymbol{\operatorname{{X}}},\boldsymbol{\operatorname{{Vect}}}]$).

The hom-set $[G,f^{\ast}(F)]$ is found by first taking the pullback of $F$ along $f$. This gives a presheaf on $\boldsymbol{\operatorname{{Y}}}$, namely $F(f(-))$. The hom-set is then the set of natural transformations $\alpha : G \mathop{\rightarrow}
f^{\ast}F$. Given an object $y$ in $\boldsymbol{\operatorname{{Y}}}$, $\alpha$ picks a linear map $\alpha_y : F(f(y)) \mathop{\rightarrow}G(y)$ subject to the naturality condition.

Now, we have seen that, given $f: \boldsymbol{\operatorname{{Y}}}\rightarrow \boldsymbol{\operatorname{{X}}}$, this $f_{\ast} :
[\boldsymbol{\operatorname{{Y}}},\boldsymbol{\operatorname{{Vect}}}] \rightarrow [\boldsymbol{\operatorname{{X}}},\boldsymbol{\operatorname{{Vect}}}]$ is a 2-linear map, and an ambidextrous adjoint for $f^{\ast}$. We would like to describe $f_{\ast}$ more explicitly. We shall want to make use of the units and counits from both the adjunction in which $f_{\ast}$ is a left adjoint, and that in which it is a right adjoint. These are described in the next section.

To describe $f_{\ast}$ in more detail, we use the fact that both $\boldsymbol{\operatorname{{Y}}}$ and $\boldsymbol{\operatorname{{X}}}$ are equivalent to unions of finite groups, and so a $\boldsymbol{\operatorname{{Vect}}}$-presheaf on $\boldsymbol{\operatorname{{Y}}}$ is a functor which assigns a representation of $Aut(y)$ to each object $y \in \boldsymbol{\operatorname{{Y}}}$. Furthermore, if $\boldsymbol{\operatorname{{Y}}}$ and $\boldsymbol{\operatorname{{X}}}$ are skeletal, then $f : \boldsymbol{\operatorname{{Y}}}\mathop{\rightarrow}\boldsymbol{\operatorname{{X}}}$ on objects can be any set map, taking objects in $\boldsymbol{\operatorname{{Y}}}$ to objects in $\boldsymbol{\operatorname{{X}}}$. For morphisms, $f$ gives, for each object $y \in \boldsymbol{\operatorname{{Y}}}$, a homomorphism from the group $Aut(y) =
\hom(y,y)$ to the group $Aut(f(y))$.

So the pullback $f^{\ast}$ is fairly straightforward: given $F : \boldsymbol{\operatorname{{X}}}
\mathop{\rightarrow}\boldsymbol{\operatorname{{Vect}}}$, the pullback $f^{\ast}F = F \circ f : \boldsymbol{\operatorname{{Y}}}\mathop{\rightarrow}\boldsymbol{\operatorname{{Vect}}}$ assigns to each $y \in \boldsymbol{\operatorname{{Y}}}$ the vector space $F(f(y))$, and gives a representation of $\operatorname{Aut}(y)$ on this vector space where $g : y \mathop{\rightarrow}y$ acts by $f(g)$. This is the *pullback representation*. If $f$ is an inclusion, this is usually called the *restricted representation*. The *pushforward*, or adjoint of pullback, for an inclusion is generally called finding the *induced representation*. We remark that for the case where $f$ is an inclusion, Sternberg [@sternberg] gives some classical discussion of this for complex representations, as does Benson [@benson] for more modules over the group ring with a more general base ring $R$. Here we use the same term for the more general case when $f$ is any homomorphism.

For any presheaf $F$, the pushforward $f_{\ast} F$ is determined by the colimit for each component of that essential preimage. Then for each $x \in \boldsymbol{\operatorname{{X}}}$, we first get: $$\bigoplus_{g : f(y) \mathop{\rightarrow}x} F(y)$$ Which is just the direct sum (i.e. biproduct) over the isomorphism classes in the essential preimage of the corresponding vector spaces. However, this is not the colimit: an object in the essential preimage is a pair $(y,g)$, but we note that if $y$ and $y'$ are isomorphic in $\boldsymbol{\operatorname{{Y}}}$, such isomorphisms induce isomorphisms of the spaces $F(y)$, and the colimit will be a quotient which identifies these spaces. In general, the colimit will be a direct sum over isomorphism classes $[y]$ in the essential preimage. Each term of the sum is isomorphic to the induced representation of $F(y)$ under the homomorphism determined by $f$.

Now, consider what the induced representations are for each isomorphism class. Any isomorphism class $[y]$ of objects in $\boldsymbol{\operatorname{{Y}}}$ determines a group $G = Aut(y)$, and similarly $[x] \in
\underline{\boldsymbol{\operatorname{{X}}}}$ determines $H = Aut(x)$. So this reduces to the case where $\boldsymbol{\operatorname{{Y}}}$ and $\boldsymbol{\operatorname{{X}}}$ are just groups (seen as one-object categories), so we have a group homomorphism $f : G \mathop{\rightarrow}H$. Using the induced algebra homomorphism $f : \mathbb{C}[G] \mathop{\rightarrow}\mathbb{C}[H]$, one can directly construct the induced homomorphism as a quotient: $f_{\ast}V
= \mathbb{C}[H] \otimes_{\mathbb{C}[G]} V$.

So for general groupoids, with $V=F(y)$, we have the direct sum: $$\label{eq:inducedrep}
(f_{\ast}F)(x) = \bigoplus_{f(y) \cong x} \mathbb{C}[Aut(x)] \otimes_{\mathbb{C}[Aut(y)]} F(y)$$

Figure [2](#fig:indrep){reference-type="ref" reference="fig:indrep"} illustrates the induced representation schematically, for a single object.

<figure id="fig:indrep">
<div class="center">
<embed src="indrep.eps" />
</div>
<figcaption><span id="fig:indrep" label="fig:indrep"></span>Induced Representation from Homomorphism</figcaption>
</figure>
