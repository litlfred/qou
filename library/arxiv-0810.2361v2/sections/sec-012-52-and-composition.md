---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS"
section_id: sec-012-52-and-composition
section_title: "and Composition"
section_number: 5.2
pages: 24-29
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.978
doc_brief: "2-VECTOR SPACES AND GROUPOIDS — This paper describes a relationship between essentially ﬁnite groupoids and 2-vector spaces."
---
Next we show that $\Lambda$ preserves horizontal composition of functors *weakly*---that is, up to a natural isomorphism. That is, the composition of the 2-linear maps must be compatible, in a weak sense, with composition of spans of groupoids.

To construct the isomorphism explicitly, we look at the weak pullback square in the middle of ([\[xy:wkpb\]](#xy:wkpb){reference-type="ref" reference="xy:wkpb"}), since the two 2-linear maps being compared differ only by arrows in this square. The square as given is a weak pullback, with the natural isomorphism $\alpha$ "horizontally" across the square. When considering a corresponding square of categories of $\boldsymbol{\operatorname{{Vect}}}$-presheaves, the arrows are reversed. So, including the adjoints of $t^{\ast}$ and $T^{\ast}$, namely $t_{\ast}$ and $T_{\ast}$, we have the square: $$\label{eq:adjunctionmatesquare}
\xymatrix{
   & [X'\circ X,\boldsymbol{\operatorname{{Vect}}}] \ar@<1ex>^{T_{\ast}}[rd] & \\
   [X,\boldsymbol{\operatorname{{Vect}}}] \ar^{S^{\ast}}[ur] \ar@<1ex>^{t_{\ast}}[rd] & & [X',\boldsymbol{\operatorname{{Vect}}}] \ar@<1ex>^{T^{\ast}}[ul] \\
   & [A_2,\boldsymbol{\operatorname{{Vect}}}] \ar_{(s')^{\ast}}[ur] \ar@<1ex>^{t^{\ast}}[ul] &
}$$

Note that there are two squares here---one by taking only the "pull" morphisms $(-)^{\ast}$ from the indicated adjunctions, and the other by taking only the "push" morphisms $(-)_{\ast}$. The first is just the square of pullbacks along morphisms from the weak pullback square of groupoids. Comparing these is the core of the following theorem, which gives one of the necessary properties for $\Lambda$ to be a weak 2-functor.

We give a more explicit description of the functors $\Lambda(X' \circ X)$ and $\Lambda(X') \circ \Lambda(X)$ below, but remark that this general result is discussed by Panchadcharam [@elango] (Proposition 0.0.1), and the general theory behind this elaborated on by Street [@street2].

::: theorem
[]{#thm:FVcomposfunc label="thm:FVcomposfunc"}The process $\Lambda$ weakly preserves composition. In particular, there is a natural isomorphism $$\beta_{X',X} : \Lambda(X' \circ X) \mathop{\rightarrow}\Lambda(X') \circ \Lambda(X)$$
:::

::: proof
*Proof.* Recall that, given the composite of two spans of groupoids in ([\[xy:wkpb\]](#xy:wkpb){reference-type="ref" reference="xy:wkpb"}), we have 2-linear maps: $$\Lambda(X' \circ X) = (t' \circ T)_{\ast} \circ (s \circ S)^{\ast}$$ and $$\Lambda(X') \circ \Lambda(X) = (t')_{\ast} \circ (s')^{\ast} \circ t_{\ast} \circ (s)^{\ast}$$ So we want to show there is a natural isomorphism: $$\beta_{X',X} : (t' \circ T)_{\ast} \circ (s \circ S)^{\ast} \mathop{\rightarrow}
(t')_{\ast} \circ (s')^{\ast} \circ t_{\ast} \circ (s)^{\ast}$$ It suffices to show that there is an isomorphism: $$\gamma: T_{\ast} \circ S^{\ast} \mathop{\rightarrow}(s')^{\ast} \circ t_{\ast}$$ between the upper and lower halves of the square in the middle of ([\[xy:wkpb\]](#xy:wkpb){reference-type="ref" reference="xy:wkpb"}) since then $\beta_{X',X}$ is obtained by tensoring with identities.

So first taking a $\boldsymbol{\operatorname{{Vect}}}$-presheaf $F$ on ${X}$, we get that $S^{\ast}F$ is a $\boldsymbol{\operatorname{{Vect}}}$-presheaf on ${X' \circ X}$. Now over any fixed object $x \in X$, we have a set of objects in ${X'
\circ X}$ which restrict to it: there is one for each choice $(g,x')$ which is compatible with $x$ in the sense that $(x,g,x')$ is an object in the weak pullback - that is, $g: t(x) \mathop{\rightarrow}s'(x')$. Each object of this form is assigned $$S^{\ast}F(x,g,x') = F(x)$$

Further, there are isomorphisms between such objects, namely pairs $(h,k)$ as above. There are thus no isomorphisms except between objects $(x,g_1,x')$ and $(x,g_2,x')$ for some fixed $x$ and $x'$. For any such fixed $x$ and $x'$, objects corresponding to $g_1$ and $g_2$ are isomorphic if $$g_2 t(h)  = {p'}_1(k) g_1$$. Denote the isomorphism class of any $g$ by $[g]$.

Then we get: $$T_{\ast} \circ S^{\ast} F (x') = \bigoplus_{x \in X} \Bigl{(}
\bigoplus_{[x']: t(x) \cong s'(x')} \mathbb{C}[Aut({x'})]
\otimes_{\mathbb{C}[Aut(x) \times_{Aut(t(x))} Aut({x'})]} F(x) \Bigr{)}$$ since $Aut(x) \times_{Aut(t(x))} Aut({x'})$ is the automorphism group of the object in ${X' \circ X}$ which restricts to $x$ and $x'$. Notice that although outside direct sum here is written over all objects $x$ on $S$, the only ones which contribute any factor are those for which $g : t(x) \mathop{\rightarrow}s'(x')$ for some $g$. The inside direct sum is over all isomorphism classes of elements $g$ for which this occurs: in the colimit, vector spaces over objects with isomorphisms between them are identified.

Note that in the direct sum over $[g]$, there is a tensor product term for each class $[g]: t(x) \mathop{\rightarrow}s'(x')$. By the definition of the tensor product over an algebra, we can pass elements of $\mathbb{C}[Aut(x)
\times_{Aut(t(x))} Aut({x'})]$ through the tensor product. These are generated by pairs $(h,k) \in Aut(x) \times Aut({x'})$ where the images of $h$ and $k$ are conjugate by $g$ so that $t(h) g = g s'(k)$. These are just automorphisms of $g$: so this says we are considering objects only up to these isomorphisms.

This is the result of the "pull-push" side of the square applied to $F$. Now consider the "push-pull" side: $(s')^{\ast} \circ t_{\ast}$.

First, pushing down to $A_2$, we get, on any object $a \in A_2$ $$t_{\ast}F(a) = \bigoplus_{[x] | t(x) \cong a} \mathbb{C}[Aut(a)] \otimes_{\mathbb{C}[Aut(x)]}F(x)$$

Then, pulling this back up to $X'$, we find: $$(s')^{\ast} \circ t_{\ast}F(x') = \bigoplus_{[x] | t(x) \cong s'(x')} \Bigl{(} \mathbb{C}[Aut(t(x))] \otimes_{\mathbb{C}[Aut({x})]} F(x)  \Bigr{)}$$ Now we define a natural isomorphism $$\gamma_{X,X'} :  T_{\ast} \circ S^{\ast} \mathop{\rightarrow}(s')^{\ast} \circ t_{\ast}$$ as follows. For each $x'$, this must be an isomorphism between the above vector spaces. The first step is to observe that there is a 1-1 correspondence *between* the terms of the first direct sums, and then secondly to note that the corresponding terms are isomorphic.

Since the outside direct sums are over all objects $x \in X$ for which $t(x) \cong s'(x')$, it suffices to get an isomorphism between each term. That is, between $$\label{eq:pullpushcomponentvs}

\mathbb{C}[Aut({x'})] \otimes_{\mathbb{C}[Aut(x) \times_{Aut(t(x))} Aut({x'})]} F(x)$$ and $$\label{eq:pushpullcomponentvs}
\mathbb{C}[Aut(t(x))] \otimes_{\mathbb{C}[Aut(x)]} F(x)$$

In order to define this isomorphism, first note that both of these vector spaces are in fact $\mathbb{C}[Aut({x'})]$-modules. An element of $Aut({x'})$ acts on ([\[eq:pullpushcomponentvs\]](#eq:pullpushcomponentvs){reference-type="ref" reference="eq:pullpushcomponentvs"}) in each component by the standard group algebra multiplication, giving an action of $\mathbb{C}[Aut({x'})]$ by extending linearly. An element $l \in
Aut({x'})$ acts on ([\[eq:pushpullcomponentvs\]](#eq:pushpullcomponentvs){reference-type="ref" reference="eq:pushpullcomponentvs"}) by the action of $s'(l)$ on $\mathbb{C}[Aut(t(x))]$. Two elements $l_1, l_2 \in [l]$ in the same equivalence class have the same action on this tensor product, since they differ precisely by $(h,k) \in Aut(x) \times Aut({x'})$, so that $l_2 t(h) = s'(k) l_1$.

Also, we notice that, in ([\[eq:pullpushcomponentvs\]](#eq:pullpushcomponentvs){reference-type="ref" reference="eq:pullpushcomponentvs"}), for each $g
\in Aut(t(x))$, the corresponding term of the form $\mathbb{C}[Aut({x'})]
\otimes_{\mathbb{C}[Aut(x) \times_{Aut(t(x))} Aut({x'})]} F(x)$ is generated by elements of the form $k \otimes v$, for $k \in \mathbb{C}[Aut({x'})]$. and $v \in F(x)$. These are subject to the relations that, for any $(h,k_1) \in \mathbb{C}[Aut({x})] \times \mathbb{C}[Aut({x'})]$ such that $t(h) = g^{-1} s'(k_1) g$: $$kk_1 \otimes v = k (h,k_1) \otimes v = k \otimes (h,k_1) v = k \otimes hv$$ since elements of $\mathbb{C}[Aut({x})] \times \mathbb{C}[Aut({x'})]$ act on $F(x)$ and $\mathbb{C}[Aut({x'})]$ by their projections into the first and second components respectively.

Now, we define the map $\gamma_{x,x'}$. First, for any element of the form $k \otimes v \in \mathbb{C}[Aut({x'})] \otimes_{\mathbb{C}[Aut(x)
\times_{Aut(t(x))} Aut({x'})]} F(x)$ in the $g$ component of the direct sum ([\[eq:pullpushcomponentvs\]](#eq:pullpushcomponentvs){reference-type="ref" reference="eq:pullpushcomponentvs"}): $$\gamma_{x,x'} (k\otimes v) = s'(k) g^{-1} \otimes v$$ which we claim is in $\mathbb{C}[Aut(t(x))] \otimes_{\mathbb{C}[Aut({x})]}
F(x)$. This map extends linearly to the whole space.

To check this is well-defined, suppose we have two representatives $k_1 \otimes v_1$ and $k_2 \otimes v_2$ of the class $k \otimes v$. So these differ by an element of $\mathbb{C}[Aut(x) \times_{Aut(t(x))} Aut({x'})]$, say $(h,k)$, so that $$k_1 = k_2 k$$, and $$h v_1 =  v_2$$ where $$t(h) = g s'(k) g^{-1}$$

But then $$\begin{aligned}
\gamma_{x,x'}(k_1 \otimes v_1) & = s'(k_1) g^{-1} \otimes v_1 \\
\nonumber & = s'(k_2 k) g^{-1} \otimes v_1 \\
\nonumber & = s'(k_2) g^{-1} g s'(k) g^{-1} \otimes v_1 \\
\nonumber & = s'(k_2) g^{-1} t(h) \otimes v_1\\
\nonumber & = s'(k_2) g^{-1} \otimes h v_1
\end{aligned}$$ while on the other hand, $$\begin{aligned}
\gamma_{x,x'} (k_2 \otimes v_2) & = s'(k_2) g^{-1} \otimes v_2\\
\nonumber & = s'(k_2) g^{-1} \otimes h v_1
\end{aligned}$$ But these are representatives of the same class in $\mathbb{C}[Aut(t(x))]
\otimes_{\mathbb{C}[Aut({x})]} F(x)$, so $\gamma$ is well defined on generators, and thus extends linearly to give a well-defined function on the whole space.

Now, to see that $\gamma$ is invertible, note that given an element $m
\otimes v \in \mathbb{C}[Aut(t(x))] \otimes_{\mathbb{C}[Aut({x})]} F(x)$, we can define $$\gamma^{-1}(m \otimes v) = 1 \otimes v \in  \bigoplus_{t(x) \mathop{\rightarrow}s'(x')} \mathbb{C}[Aut({x'})]
\otimes_{\mathbb{C}[Aut(x) \times_{Aut(t(x))} Aut({x'})]} F(x)$$ in the component coming from the isomorphism class of $g = m^{-1}$ (we will denote this by $(1 \otimes v)_{m^{-1}}$ to make this explicit, and in general an element in the class of $g$ will be denoted with subscript $g$ whenever we need to refer to $g$).

Now we check that this is well-defined. Given $m_1 \otimes v_1$ and $m_2 \otimes v_2$ representing the same element $m \otimes v$ of $\mathbb{C}[Aut(t(x)] \otimes_{\mathbb{C}[Aut({x})]} F(x)$, we must have $h_1
\in Aut(x)$ with $$m_1 t(h_1) = m_2$$ and $$h_1 v_2 = v_1$$ But then applying $\gamma^{-1}$, we get: $$\gamma^{-1}(m_1 \otimes v_1) = (1 \otimes v_1)_{m_1^{-1}} = (1 \otimes h_1 v_2)_{m_1^{-1}}$$ and $$\gamma^{-1}(m_2 \otimes v_2) = (1 \otimes v_2)_{m_2^{-1}} = (1 \otimes v_2)_{t(h_1)^{-1} m_1^{-1}}$$ but these are in the same component, since $g \sim g'$ when $g'
s'(k) = t(h) g$ for some $h \in Aut(x)$ and $k \in Aut({x'})$. But then, taking $k=1$ and $h = h_1^{-1}$, we get that $m_1^{-1} \sim
m_2^{-1}$, and hence the component of $\gamma(m \otimes v)$ is well defined.

But then, consider $m \otimes v = \gamma((k \otimes v)_g) = s'(k)
g^{-1} \otimes v$. Applying $\gamma^{-1}$ we get: $$\gamma^{-1} \circ \gamma (k \otimes v)_g = (1 \otimes v)_{g s'(k)^{-1}}$$ so we hope that these determine the same element. But in fact, notice that the morphism in the weak pullback which gives that $g^{-1}$ and $s'(k) g^{-1}$ are isomorphic is just labelled by $(h,k) = (1,k)$, which indeed takes $k$ to $1$ and leaves $v$ intact. So these are the corresponding elements under this isomorphism.

So $\gamma$ is invertible, hence an isomorphism. Thus we define $$\beta_{X,X'} = 1 \otimes \gamma \otimes 1$$ This is the isomorphism we wanted. ◻
:::

So the $\beta_{X,X'}$ can now be seen as natural transformations explicitly. First consider $\Lambda({X'}) \circ \Lambda(X)$, which acts on a presheaf $G$ on $A_1$ as follows. $$\begin{aligned}
\label{eq:firststepFV}
\Lambda(X)(G)(a_2) & = \bigoplus_{[x] | t(x) \cong a_2} \mathbb{C}[Aut(a_2)] \otimes_{\mathbb{C}[Aut(x)]} G(s(x)) ) \\
\nonumber & = \bigoplus_{[a_1] \in \underline{A_1}} (\mathop{\bigoplus_{\stackrel{[x]}{s(x) \cong a_1}}}_{{t(x) \cong a_2}} \mathbb{C}[Aut(a_2)] \otimes_{\mathbb{C}[Aut(x)]} (\Lambda(X)(G)(a_1))
\end{aligned}$$ and then applying $\Lambda(X')$ to this, we get, rearranging direct sums suitably: $$\begin{aligned}
\label{eq:composedFV}
& (\Lambda({X'}) \circ \Lambda(X))(G)(a_3) \\
\nonumber = & \bigoplus_{[a_2] \in \underline{A_2}} (\mathop{\bigoplus_{\stackrel{[x']}{s'(x') \cong a_2}}}_{{t'(x') \cong a_3}} \mathbb{C}[Aut(a_3)] \otimes_{\mathbb{C}[Aut({x'})]} (\Lambda(X)(G)(a_2)) \\
\nonumber = &  \bigoplus_{[a_1] \in \underline{A_1}} \bigl{(} \bigoplus_{[a_2] \in \underline{A_2}} \mathop{\bigoplus_{\stackrel{[x]}{s(x) \cong a_1}}}_{{t(x) \cong a_2}}   \mathop{\bigoplus_{\stackrel{[x']}{s'(x') \cong a_2}}}_{{t'(x') \cong a_3}} \mathbb{C}[Aut(a_3)] \otimes_{\mathbb{C}[Aut({x'})]} \mathbb{C}[Aut(a_2)] \otimes_{\mathbb{C}[Aut(x)]} G(a_1) \bigr{)}
\end{aligned}$$ We similarly have: $$\label{eq:FVcomposed}
(\Lambda(X') \circ \Lambda(X))(G)(a_3) = \bigoplus_{[a_1] \in \underline{A_1}} ( \mathop{\bigoplus_{\stackrel{[(x,f,x')]}{((s\circ S)(x,f,x') \cong a_1}}}_{{(t'\circ T(x,f,x') \cong a_3}} \mathbb{C}[Aut(a_3)] \otimes_{\mathbb{C}[Aut(x,f,x')]} G(a_1) )$$

The isomorphisms $\beta_{X,X'}$ allow us to identify ([\[eq:composedFV\]](#eq:composedFV){reference-type="ref" reference="eq:composedFV"}) and ([\[eq:FVcomposed\]](#eq:FVcomposed){reference-type="ref" reference="eq:FVcomposed"}).

::: remark
[]{#rk:composbeta label="rk:composbeta"} We can also describe the effect of $\beta$ in coordinates - that is, in the matrix form for a natural transformation of a 2-linear map. This illustrates the fact that $\mathbb{C}[Aut(a_2)] \cong \bigoplus_{W} W \otimes W^{\star}$, where the sum is over irreducible representations of $Aut(a_2)$. For suppose we have a composite of spans, $X' \circ X$. By Lemma [\[lemma:kv2linmatrix\]](#lemma:kv2linmatrix){reference-type="ref" reference="lemma:kv2linmatrix"}, we have that the functors $T_{\ast} \circ
S^{\ast}$ and $(s')^{\ast} \circ t_{\ast}$ can be written in the form of a matrix of vector spaces as in ([\[eq:kv2linmatrix\]](#eq:kv2linmatrix){reference-type="ref" reference="eq:kv2linmatrix"}).

First, $\Lambda(X' \circ X)$ is given by a matrix indexed by classes of objects and representations $([a_1],W_1)$ from $A_1$ and $([a_3],W_3)$ from $A_3$. In the form ([\[eq:frobenius\]](#eq:frobenius){reference-type="ref" reference="eq:frobenius"}), we see that $$\begin{aligned}
& \Lambda(X' \circ X)_{([a_1],W_1),([a_3],W_3)} \\
\nonumber \simeq & \bigoplus_{[(x,f,x')]} \operatorname{hom}_{Rep(\operatorname{Aut}(x,f,x'))}[(s \circ S)^{\ast}(W_1),(t' \circ T)^{\ast}(W_3)]
\end{aligned}$$ where $[(x,f,x')]$ represents an equivalence class of objects in the weak pullback.

The isomorphisms $\beta_{X,X'}$ take this to the matrix product of $\Lambda(X')$ with $\Lambda(X)$, which has components given by a direct sum over classes and representations $([a_2],W_2)$ from $A_2$: $$\begin{aligned}
\label{eq:cobmatmultcomponent}
& [\Lambda(X' \circ X)]_{([a_1],W_1),([a_3],W_3)} \\
\nonumber \mathop{\mathop{\rightarrow}}\limits^{\beta_{X,X'}} & \bigoplus_{([a_2],W)} [\Lambda(X)]_{([a_1],W_1),([a_2],W_2)} \otimes [\Lambda(X')]_{([a_2],W_2),([a_3],W_3)}
\end{aligned}$$ Recall that $[\Lambda(X)]_{([a_1],W_1),([a_2],W_2)}$, is a direct sum over isomorphism classes of objects of $X$ which restrict to $[a_1]$ and $[a_2]$, with each component being $$\hom_{\operatorname{Rep}(Aut(x))}(s^{\ast}W_1,t^{\ast}W_2)$$The component $[\Lambda(X')]_{([a_2],W_2),([a_3],W_3)}$, is a similar sum over classes of objects of $X'$ which restrict to $[a_2]$ and $[a_3]$.

The isomorphism $\beta_{X',X}$ identifies the composite, whose components are sums over objects of $X' \circ X$, with this product. This $\beta$ consists of isomorphisms in each component. So in fact, the $\beta$ are described by their components: $$\begin{aligned}
\label{eq:betaisomorphisms} & \bigoplus_{[(x,f,x')]} \bigl{[} \hom((s\circ S)^{\ast}(W_1),(t'\circ T)^{\ast}(W_3) \bigr{]} \\
\nonumber\stackrel{\beta_{X,X'}}{\longrightarrow} &  \bigoplus_{([a_2],W_2)} \bigl{[} \hom(s^{\ast}(W_1),t^{\ast}(W_2)) \otimes \hom((s')^{\ast}(W_2),(t')^{\ast}(W_3)) \bigr{]} 
\end{aligned}$$ Where the second sum is over equivalence classes of $(x,f,x')$ such that $f : t(x) \mathop{\rightarrow}s'(x')$, and for which $s(x)=a_1$ and $t'(x')=a_3$.

Since the choice of $[x]$ and $[x']$ amounts to the same thing as the choice of $[a_2]$, this isomorphism turns a sum over representations $W_2$ of tensor products of space (of intertwiners), into a sum over isomorphism (conjugacy) classes of $f \in \operatorname{Aut}([a_2])$. This isomorphism is describing how the representations in the big pullback decompose.
:::
