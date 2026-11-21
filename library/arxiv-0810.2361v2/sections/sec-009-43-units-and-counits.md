---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS"
section_id: sec-009-43-units-and-counits
section_title: "Units and Counits"
section_number: 4.3
pages: 19-22
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
toc_source: outline
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.982
doc_brief: "2-VECTOR SPACES AND GROUPOIDS — This paper describes a relationship between essentially ﬁnite groupoids and 2-vector spaces."
---
[]{#sec:units label="sec:units"}

We have observed that the pullback and pushforward maps $f^{\ast}$ and $f_{\ast}$ are both left and right adjoints. Thus there are two adjunctions to consider: $f^{\ast} \dashv f_{\ast}$, where pushforward is right adjoint to pullback; and $f_{\ast} \dashv f^{\ast}$ where pushforward is left adjoint to pullback. For convenience, we refer to these as the "right adjunction" and "left adjunction" respectively, after the position of the pushforward. Each adjunction has unit and counit, so there are four natural transformations to describe. We will identify them as "right" and "left" unit and counit following the convention above. Thus, we have:

$$\begin{aligned}
\eta_L : & \operatorname{Id}_{[\boldsymbol{\operatorname{{Y}}},\boldsymbol{\operatorname{{Vect}}}]} \Longrightarrow f^{\ast} f_{\ast} \\
\epsilon_L : & f_{\ast} f^{\ast} \Longrightarrow \operatorname{Id}_{[\boldsymbol{\operatorname{{X}}},\boldsymbol{\operatorname{{Vect}}}]} \\
\eta_R : & \operatorname{Id}_{[\boldsymbol{\operatorname{{X}}},\boldsymbol{\operatorname{{Vect}}}]} \Longrightarrow f_{\ast} f^{\ast} \\
\epsilon_R : & f^{\ast} f_{\ast} \Longrightarrow \operatorname{Id}_{[\boldsymbol{\operatorname{{Y}}},\boldsymbol{\operatorname{{Vect}}}]}
\end{aligned}$$

Once again, it is useful for practical calculations to have a coordinate-dependent form for these maps, but there is a convenient intrinsic definition which we shall describe first. Here again, we note that Benson [@benson] describes the case where $f$ is an inclusion, in a more general setting than the complex representations we consider here.

To begin with, we should describe the functors $f^{\ast} f_{\ast}$ ("push-pull"), which is an endofunctor on $[\boldsymbol{\operatorname{{Y}}},\boldsymbol{\operatorname{{Vect}}}]$, and $f_{\ast}
f^{\ast}$ ("pull-push"), which is an endofunctor on $[\boldsymbol{\operatorname{{X}}},\boldsymbol{\operatorname{{Vect}}}]$.

For the "push-pull", $f^{\ast} f_{\ast}$, we first push a $\boldsymbol{\operatorname{{Vect}}}$-presheaf $F$ on $\boldsymbol{\operatorname{{Y}}}$ to one on $\boldsymbol{\operatorname{{X}}}$, then pull back to $\boldsymbol{\operatorname{{Y}}}$. On each object $y \in \boldsymbol{\operatorname{{Y}}}$, this gives a new presheaf where the vector space $F(y)$ is replaced by the pullback (i.e. induced representation of $Aut(y)$) of $f_{\ast}F (f(y))$. But $f_{\ast}F$ is a presheaf on $\boldsymbol{\operatorname{{X}}}$, which, at each $x \in \boldsymbol{\operatorname{{X}}}$, gives a colimit over the essential preimage of $x$ in $\boldsymbol{\operatorname{{Y}}}$, namely $\bigoplus_{[y'] | f(y') \cong x}
\mathbb{C}[Aut(x)] \otimes_{\mathbb{C}[Aut(y')]} F(y')$. In the case where $x = f(y)$, this means we get: $$f^{\ast} f_{\ast} F (x) = \bigoplus_{[y'] | f(y') \cong f(y)} \mathbb{C}[Aut(f(y))] \otimes_{\mathbb{C}[Aut(y')]} F(y')$$ thought of as a (left) representation of $Aut(y)$ in the obvious way (i.e. $g \in Aut(y)$ acts on this space as $f(g)$).

For the "pull-push", $f_{\ast} f^{\ast}$, we first pull a $\boldsymbol{\operatorname{{Vect}}}$-presheaf $G$ on $\boldsymbol{\operatorname{{X}}}$ back to $f^{\ast}G$ on $\boldsymbol{\operatorname{{Y}}}$. At each $y \in
\boldsymbol{\operatorname{{Y}}}$, this assigns the vector space $f^{\ast}G(y) = G(f(y))$ as a representation of $Aut(y)$. We then push forward to $\boldsymbol{\operatorname{{X}}}$ to get, at each $x \in \boldsymbol{\operatorname{{X}}}$, that: $$f_{\ast} f^{\ast} G (x) = \bigoplus_{[y] | f(y) \cong x} \mathbb{C}[Aut(x)] \otimes_{\mathbb{C}[Aut(y)]} G(x)$$ Note that *a priori* the last space would be $G(f(y))$, but since $f(y) \cong x$, we have also that $G(f(y)) \cong G(x)$ as representations of $Aut(y)$. Here we are implicitly taking a colimit over the essential preimage of $x$, whose objects are not just $y$ such that $f(y) \cong x$, but rather such $y$ equipped with a specific isomorphism. These therefore induce specific isomorphisms of $G(f(y))$ and $G(x)$, and the quotient implied by the colimit identifies these spaces.

Now, the description above accords with the usual description of these functors in the left adjunction. Since the adjunction is ambidextrous, it applies in both cases, but to describe the unit and counit properly, we should note that in general the canonical description of the left and right adjunctions are different. (Here again we note that Benson [@benson] shows this for modules over general rings, which in our case are the group algebras $\mathbb{C}[Aut(y)]$ etc., in the case of inclusion) We need to take account of the specific isomorphism between the form we have presented (natural for the left adjunction), and the form which is natural for the right adjunction.

The right adjoint is given as: $$f_{\ast} F (y) = \bigoplus_{[y] | f(y) \cong x} \hom_{\mathbb{C}[Aut(x)]}(\mathbb{C}[Aut(y)],F(y))$$ (Note that the case for groups, namely when $\boldsymbol{\operatorname{{Y}}}$ and $\boldsymbol{\operatorname{{X}}}$ have only one object, appears in each term of this direct sum). The *Nakayama isomorphism* gives the duality between the two descriptions of $f_{\ast}$, in terms of $\hom_{\mathbb{C}[Aut(x)]}$ and $\otimes_{\mathbb{C}[Aut(x)]}$, by means of the *exterior trace map*. The groupoid case is just the direct sum of group cases, which looks like: $$N : \bigoplus_{[y] | f(y) \cong x} \hom_{\mathbb{C}[Aut(y)]}(\mathbb{C}[Aut(x)],F(y)) \mathop{\rightarrow}\bigoplus_{[y] | f(y) \cong x} \mathbb{C}[Aut(x)] \otimes_{\mathbb{C}[Aut(y)]} F(y)$$ given by the *exterior trace map* in each factor of the sum: $$\label{eq:nakayama}
N : \bigoplus_{[y] | f(y) \cong x} \phi_y \mapsto \bigoplus_{[y] | f(y) \cong x} \frac{1}{\# Aut(y)}\sum_{g \in Aut(x)} g^{-1} \otimes \phi_y(g)$$ Note that the exterior trace map gives an $Aut(x)$-invariant vector, but the normalization is by the size of $Aut(y)$. In the case where the homomorphism is an inclusion, this is interpreted as trace given by a sum over cosets of $Aut(y)$ in $Aut(x)$, (which is the situation usually presented in the group case). We remark here that this factor will be important in interpreting our 2-functor $\Lambda$ as a form of groupoidification.

We can now write down the units and counits explicitly for both adjunctions in our preferred notation.

The left and right units are natural transformations which, for each $\boldsymbol{\operatorname{{Vect}}}$-presheaf on $\boldsymbol{\operatorname{{Y}}}$ or $\boldsymbol{\operatorname{{X}}}$ respectively, gives a morphism which is itself a natural transformation. So, in particular the left unit $$\label{eq:leftunit}
\eta_L(F)(y) : F(y) \mathop{\rightarrow}\bigoplus_{[y'] | f(y') \cong f(y)} \mathbb{C}[Aut(f(y))] \otimes_{\mathbb{C}[Aut(y')]} F(y')$$ is given by the natural map into the counit: $$v \mapsto \bigoplus_{[y]} (1 \otimes v)$$

Notice the unit map has no contribution in the image from any $y'$ which is not in the isomorphism class $[y]$. (It is a canonical map out of the limit which gives the usual form for $f_{\ast}$.)

The right unit map $$\label{eq:rightunit}
\eta_R(G)(x) : G(x) \mathop{\rightarrow}\bigoplus_{[y] | f(y) \cong x} \mathbb{C}[Aut(x)] \otimes_{\mathbb{C}[Aut(y)]} f^{\ast}G(x)$$ is found by composing the Nakayama isomorphism ([\[eq:nakayama\]](#eq:nakayama){reference-type="ref" reference="eq:nakayama"}) with the groupoid form of the canonical map for the right adjoint. This is a direct sum, in which each factor is given by the multiplication map: $$v \mapsto \bigl{(} g \mapsto g(v) \bigr{)}$$ Thus, the composite is: $$\eta_R(G)(x) : v \mapsto \bigoplus_{[y] | f(y) \cong x} \frac{1}{\# Aut(y)}\sum_{g \in Aut(x)} g^{-1} \otimes g(v)$$

The left and right counits are natural transformations which, for each $\boldsymbol{\operatorname{{Vect}}}$-presheaf on $\boldsymbol{\operatorname{{X}}}$ or $\boldsymbol{\operatorname{{Y}}}$ respectively, gives a morphism which is itself a natural transformation. So in particular, the left counit $$\label{eq:leftcounit}
\epsilon_L(G)(x) : \bigoplus_{[y] | f(y) \cong x} \mathbb{C}[Aut(x)] \otimes_{\mathbb{C}[Aut(y)]} f^{\ast} G(x) \mathop{\rightarrow}G(x)$$ is given by summing multiplication maps: $$\bigoplus_{[y] | f(y) \cong x} g_y \otimes v \mapsto \sum_{[y] | f(y) \cong x} f(g_y) v$$

The right counit map $$\label{eq:rightcounit}
\epsilon_R(F)(y) : \bigoplus_{[y'] | f(y') \cong f(y)} \mathbb{C}[Aut(f(y))] \otimes_{\mathbb{C}[Aut(y')]} F(y') \mathop{\rightarrow}F(y)$$ is given by composing the inverse of the Nakayama isomorphism ([\[eq:nakayama\]](#eq:nakayama){reference-type="ref" reference="eq:nakayama"}) with the evaluation map from the canonical form of the right adjoint. Again, the only factor which contributes is $y'
\cong y$, and so we have: $$\bigoplus_{[y'] | f(y') \cong f(y)}\phi_{y'} \mapsto \phi_y(1)$$ So finally, (by using that $\mathbb{C}[Aut(f(y))]$ is canonically isomorphic to its dual using the canonical inner product on the group algebra) the composite is: $$\epsilon_R(F)(y) : \bigoplus_{[y'] | f(y') \cong f(y)}g_{y'} \otimes v_{y'} \mapsto \frac{\# Aut(y)}{\# Aut(f(y))} g_y(v_y)$$ Here we are implicitly using the fact that the objects $y'$ in the essential preimage come equipped with isomorphisms $f(y') \mathop{\rightarrow}f(y)$ which induce specified isomorphisms $Aut(f(y')) \cong Aut(f(y))$. In the colimit which gave the direct sum over isomorphism classes, these are all naturally identified.

A straightforward check (cancelling the Nakayama isomorphisms) verifies the unit and counit identities: $$\begin{aligned}
(\epsilon_L \cdot Id_{f_{\ast}} ) \circ (Id_{f_{\ast}} \cdot \eta_L) = \operatorname{Id}_{f_{\ast}} \\
(Id_{f^{\ast}} \cdot \epsilon_L) \circ (\eta_L \cdot Id_{f^{\ast}}) = \operatorname{Id}_{f^{\ast}} \\
(\epsilon_R \cdot Id_{f^{\ast}} ) \circ (Id_{f^{\ast}} \cdot \eta_R) = \operatorname{Id}_{f^{\ast}} \\
(Id_{f_{\ast}} \cdot \epsilon_R) \circ (\eta_R \cdot Id_{f_{\ast}}) = \operatorname{Id}_{f_{\ast}}
\end{aligned}$$
