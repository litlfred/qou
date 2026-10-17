---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS"
section_id: sec-011-51-2-linear-maps-from-spans-of-groupoids
section_title: "2-Linear Maps from Spans of Groupoids"
section_number: 5.1
pages: 22-24
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
toc_source: outline
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.97
doc_brief: "2-VECTOR SPACES AND GROUPOIDS — This paper describes a relationship between essentially ﬁnite groupoids and 2-vector spaces."
---
[]{#sec:span2lin label="sec:span2lin"}

Given a span of groupoids as in Figure [\[fig:grpd-span\]](#fig:grpd-span){reference-type="ref" reference="fig:grpd-span"}, we can apply the functor $[ - , \boldsymbol{\operatorname{{Vect}}}]$ to the span diagram ([\[eq:spandiag\]](#eq:spandiag){reference-type="ref" reference="eq:spandiag"}). This functor is contravariant, so we get a cospan: $$\label{eq:zstep3}
\xymatrix{
  & [X,\boldsymbol{\operatorname{{Vect}}}] & \\
[A_1,\boldsymbol{\operatorname{{Vect}}}] \ar[ur]^{s^{\ast}} & & [A_2,\boldsymbol{\operatorname{{Vect}}}] \ar[ul]_{t^{\ast}} \\
}$$

We now recall that the pullbacks $s^{\ast}$ and $t^{\ast}$ have adjoints: this is a direct consequence of Theorem [\[thm:2mapadjoints\]](#thm:2mapadjoints){reference-type="ref" reference="thm:2mapadjoints"}. This reveals how to transport a $\boldsymbol{\operatorname{{Vect}}}$-presheaf on $A_1$ along this cospan. In fact, it gives two 2-linear maps, which are adjoint. Thinking of the span as a morphism in $\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$ from $A_1$ to $A_2$, we find a corresponding 2-linear map (though the adjoint is equally well defined). We first do a pullback along $s$, giving a $\boldsymbol{\operatorname{{Vect}}}$-presheaf on $X$. Then we use the adjoint map $t_{\ast}$. So we have the following:

::: definition
[]{#def:ZGonS label="def:ZGonS"} For a span of groupoids $X : A_1 \mathop{\rightarrow}A_2 \ in \operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$ define the 2-linear map: $$\label{eq:zstep4}
t_{\ast} \circ s^{\ast} : [A_1,\boldsymbol{\operatorname{{Vect}}}] \longrightarrow [A_2,\boldsymbol{\operatorname{{Vect}}}]$$
:::

Now, by Theorem [\[thm:2mapadjoints\]](#thm:2mapadjoints){reference-type="ref" reference="thm:2mapadjoints"}, both $s^{\ast}$ and $t_{\ast}$ are 2-linear maps, so the composite $t_{\ast} \circ s^{\ast}$ is also a 2-linear map.

::: remark
We can think of the pullback-pushforward construction as giving---in the language of quantum field theory---a "sum over histories" for evolving a 2-vector. Each 2-vector in $[A_1,\boldsymbol{\operatorname{{Vect}}}]$ picks out a vector space for each object of $A_1$. The 2-linear map we have described tells us how to evolve this 2-vector along a span. First we consider the pullback to $[X,\boldsymbol{\operatorname{{Vect}}}]$, which gives us a 2-vector consisting of all assignments of vector spaces to objects of $X$ which project to the chosen one in $A_1$. Each of these objects could be considered a "history" of the 2-vector along the span. We then "push forward" this assignment to $A_2$, which involves a colimit. This is more general than a sum, though so one could describe this as a "colimit of histories". It takes into account the symmetries between individual "histories" (i.e. morphisms in $X$).
:::

So, given a span $X : A_1 \mathop{\rightarrow}A_2$, we can write $\Lambda(X)$ in terms of its effect on a $\boldsymbol{\operatorname{{Vect}}}$-presheaf $G$ on $A_1$, which, at any object $a_2 \in A_2$ gives: $$\label{eq:FVX}
\Lambda(X)(G)(a_2) = ( \bigoplus_{[x] | t(x) \cong a_2} \mathbb{C}[Aut(a_2)] \otimes_{\mathbb{C}[Aut(x)]} G(s(x)) )$$ by exactly the same reasoning as in Section [\[sec:units\]](#sec:units){reference-type="ref" reference="sec:units"}.

It is sometimes useful---particularly when we look at composition of spans---to break up the direct sum into the contributions from different objects of $A_1$, like this: $$\label{eq:decomposedFVX}
\Lambda(X)(G)(a_2) = \bigoplus_{[a_1] \in \underline{A_1}} ( \mathop{\bigoplus_{\stackrel{[x]}{s(x) \cong a_1}}}_{{t(x) \cong a_2}} \mathbb{C}[Aut(a_2)] \otimes_{\mathbb{C}[Aut(x)]} G(a_1) )$$

Moreover, there is a convenient way to write down the components of the 2-linear map associated to a span, which is given by Frobenius reciprocity.

::: proposition
Given basis elements $(a_1,W_1) \in \Lambda(A_1)$ and $(a_2,W_2) \in \Lambda(A_2)$, the matrix elements are: $$\label{eq:frobenius} 
\Lambda(X)_{(a_1,W_1),(a_2,W_2)} \simeq \bigoplus_{[x]} \operatorname{hom}_{Rep(\operatorname{Aut}(x))}[s^{\ast}(W_1),t^{\ast}(W_2)]$$
:::

Here, the direct sum is taken over equivalence classes $[x]$ in the essential preimage of $(a_1,a_2)$: that is, objects of $X$ mapping to $a_1$ and $a_2$. For each $[x]$, the functors $s$ and $t$ define homomorphisms $$s_x : \operatorname{Aut}(x) \mathop{\rightarrow}\operatorname{Aut}(s(x))$$ and $$t_x : \operatorname{Aut}(x) \mathop{\rightarrow}\operatorname{Aut}(t(x))$$, which define the induced representations. We think of the terms of the direct sum as "lying over" the objects $x$.

So using the adjoint 2-linear map $$t_{\ast} : \Lambda(X) \mathop{\rightarrow}\Lambda(A_2)$$ to *push forward* a 2-vector $s^{\ast}F : X \mathop{\rightarrow}\boldsymbol{\operatorname{{Vect}}}$ to one on $A_2$, the above is also, by Frobenius reciprocity: $$\bigoplus_{[x]} \operatorname{hom}_{Rep(\operatorname{Aut}(a_2))}[(t_x)_{\ast} \circ (s_x)^{\ast} W_1 , W_2]$$

By Schur's lemma, this says: $$\Lambda(X)(a_1,W_1) = \bigoplus_{[x]} (t_x)_{\ast} \circ (s_x)^{\ast} (a_1,W_1)$$ since the components of $\Lambda(X)(a_1,W_1)$ count the number of copies of $W_2$ in the pushforward of $W_1$. (In the remainder of this paper, we will suppress the subscripts and denote $s_x$ by $s$ and $t_x$ by $t$ when the context makes clear that we mean the induced group homomorphism.)

So in fact, $\Lambda(X)(a_1,W_1)$ is a direct sum of irreducible 2-vectors in $\Lambda(A_2)$, given as a sum over $x \in X$ restricting to $a_1, a_2$ of the induced representations along each restriction map.
