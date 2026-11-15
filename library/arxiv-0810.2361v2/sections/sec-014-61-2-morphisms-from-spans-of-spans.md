---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS"
section_id: sec-014-61-2-morphisms-from-spans-of-spans
section_title: "2-Morphisms from Spans of Spans"
section_number: 6.1
pages: 30-35
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.963
doc_brief: "2-VECTOR SPACES AND GROUPOIDS — This paper describes a relationship between essentially ﬁnite groupoids and 2-vector spaces."
---
We begin by noting that the diagram ([\[eq:spanspan\]](#eq:spanspan){reference-type="ref" reference="eq:spanspan"}), which weakly commutes up to isomorphisms $\zeta_s$ and $\zeta_t$, gives rise to a diagram of pullback functors: $$\label{eq:spanspanpullback}
\xymatrix{
 & [X_1,\boldsymbol{\operatorname{{Vect}}}] \ar[d]_{s^{\ast}} & \\
[A_1,\boldsymbol{\operatorname{{Vect}}}] \ar[dr]_{{s_2}^{\ast}} \ar[ur]_{{s_1}^{\ast}} & [Y,\boldsymbol{\operatorname{{Vect}}}] & [A_2,\boldsymbol{\operatorname{{Vect}}}] \ar[ul]^{{t_1}^{\ast}} \ar[dl]^{{t_2}^{\ast}} \\
 & [X_2,\boldsymbol{\operatorname{{Vect}}}] \ar[u]^{t^{\ast}} & \\
}$$ which commutes up to isomorphisms: $$\zeta_s^{\ast} : s^{\ast} \circ s_1^{\ast}(V) \tilde{\mathop{\rightarrow}} t^{\ast} \circ s_2^{\ast}(V)$$ and similarly $$\zeta_t^{\ast} : s^{\ast} \circ t_1^{\ast}(V) \tilde{\mathop{\rightarrow}} t^{\ast} \circ t_2^{\ast}(V)$$

We want to get a natural transformation from $\Lambda(X_1)$ and $\Lambda(X_2)$ from this diagram. In section [\[sec:coordY\]](#sec:coordY){reference-type="ref" reference="sec:coordY"} we show how this can be described as a "pull-push" process, similar to the one used to define the 2-linear maps, but first it can be defined in terms of the unit and counit maps we have already defined.

::: definition
[]{#def:Von2Span label="def:Von2Span"}Given a span between spans, $Y : X_1 \mathop{\rightarrow}X_2$, for $X_1,X_2 : A_1 \mathop{\rightarrow}A_2$, then $$\Lambda(Y) : \Lambda(X_1) \mathop{\rightarrow}\Lambda(X_2)$$ is the natural transformation given as $$\Lambda(Y) = \epsilon_{L,t} \circ ((\zeta_t)_{\ast} \otimes ((\zeta_s)^{\ast})^{-1} ) \circ \eta_{R,s} : (t_1)_{\ast} s_1^{\ast} \Longrightarrow (t_2)_{\ast} s_2^{\ast}$$ where $\epsilon_{L,t}$ is the counit ([\[eq:leftcounit\]](#eq:leftcounit){reference-type="ref" reference="eq:leftcounit"}) for the left adjunction associated to $t$, and $\eta_{R,s}$ is the unit ([\[eq:rightunit\]](#eq:rightunit){reference-type="ref" reference="eq:rightunit"}) for the right adjunction associated to $s$.
:::

We comment here that this composition of left unit followed by right counit can be interpreted as a "pull-push" in a sense that can be seen more precisely when we consider this natural transformation in coordinates. In the special case where $A_i = 1$, this recovers groupoidification in the sense of Baez and Dolan, as shown in Theorem [\[thm:groupoidification\]](#thm:groupoidification){reference-type="ref" reference="thm:groupoidification"}.

::: remark
Henceforth, we will assume that the diagram ([\[eq:spanspan\]](#eq:spanspan){reference-type="ref" reference="eq:spanspan"}) commutes strictly - that is, $\zeta_s$ and $\zeta_t$ are identity 2-morphisms. This is a mild assumption, since the diagram can always be "strictified" by taking equivalent groupoids for source and target which are skeletal. Similar arguments will follow through if not, but in this simpler case, we simply have: $$\Lambda(Y) = \epsilon_{L,t} \circ \eta_{R,s} : (t_1)_{\ast} s_1^{\ast} \Longrightarrow (t_2)_{\ast} s_2^{\ast}$$
:::

For our construction to give a 2-functor, this must agree with composition in two ways. The first is strict preservation of vertical composition; the second is preservation of horizontal composition as strictly as possible (i.e. up to the isomorphisms $\beta$ which make comparison possible - as we will see). We will show in

::: lemma
[]{#thm:vertcompos label="thm:vertcompos"}The assignment $\Lambda(Y)$ to spans of spans given in Definition [\[def:Von2Span\]](#def:Von2Span){reference-type="ref" reference="def:Von2Span"} preserves vertical composition strictly: $\Lambda(Y' \circ Y) = \Lambda(Y') \circ \Lambda(Y)$.
:::

::: proof
*Proof.* Suppose we have a vertical composite of two spans between spans, here written as 2-cells: $$\label{xy:verticalcomposition}
\xymatrix{
A_1 \ar@/^3pc/[rrr]^{X_1}="1" \ar[rrr]^{X_2}="2" \ar@/_3pc/[rrr]_{X_3}="3" & & & A_2 \\
 {\ar@{=>}"1"+<0ex,-2.5ex> ;"2"+<0ex,+2.5ex>^{Y}}
 {\ar@{=>}"2"+<0ex,-2.5ex> ;"3"+<0ex,+2.5ex>^{Y'}}
}$$

The composition is given by a weak pullback (taken up to isomorphism) - that is, a diagram of the form ([\[xy:wkpb\]](#xy:wkpb){reference-type="ref" reference="xy:wkpb"}), with the $Y$ and $Y'$ in place of $X$ and $X'$, and the $X_i$ in place of the $A_i$. We use the same notation for the maps in all these spans. Of course, each object in ([\[xy:verticalcomposition\]](#xy:verticalcomposition){reference-type="ref" reference="xy:verticalcomposition"}) comes equipped with (commuting) maps into $A_1$ and $A_2$, but we can ignore these here.

So the source and target maps for $Y$ are $s$ and $t$, and those for $Y'$ are $s'$ and $t'$, and we can easily write: $$\Lambda(Y') \circ \Lambda(Y) = \epsilon_{L,t'} \circ \eta_{R,s'} \circ \epsilon_{L,t} \circ \eta_{R,s}$$

Now, to write $\Lambda(Y' \circ Y)$, we recall that the vertical composite is formed by weak pullback of spans, with the resulting source and target maps $s \circ S$ and $t' \circ T$, where the groupoid in the span $Y' \circ Y$ is the comma category whose objects are of the form $(y',g_2,y)$, with $g_2 : t(y) \mathop{\rightarrow}s'(y')$ in $X_2$, and $S$ and $T$ are the natural projections onto $Y$ and $Y'$. Then of course $$\Lambda(Y' \circ Y) = \epsilon_{L,(t' \circ T)} \circ \eta_{R,(s \circ S)}$$

Now, a composite of adjunctions is an adjunction (see for instance MacLane [@maclane] IV.8), and the unit and counit of the composite is given in a standard way, so we have: $$\epsilon_{L,(t' \circ T)} = \epsilon_{L,t'} \circ (\operatorname{Id}_{(t')_{\ast}} \otimes \epsilon_{L,T} \otimes \operatorname{Id}_{(t')^{\ast}})$$ and $$\eta_{R,(s \circ S)} = (\operatorname{Id}_{s_{\ast}} \otimes \eta_{R,S} \otimes \operatorname{Id}_{s^{\ast}}) \circ \eta_{R,s}$$

So we get $$\Lambda(Y' \circ Y) = \epsilon_{L,t'} \circ (\operatorname{Id}_{(t')_{\ast}} \otimes \epsilon_{L,T} \otimes \operatorname{Id}_{(t')^{\ast}}) \circ (\operatorname{Id}_{s_{\ast}} \otimes \eta_{R,S} \otimes \operatorname{Id}_{s^{\ast}}) \circ \eta_{R,s}$$

So to get strict composition, we just need that $$(\operatorname{Id}_{(t')_{\ast}} \otimes \epsilon_{L,T} \otimes \operatorname{Id}_{(t')^{\ast}}) \circ (\operatorname{Id}_{s_{\ast}} \otimes \eta_{R,S} \otimes \operatorname{Id}_{s^{\ast}}) = \eta_{R,s'} \circ \epsilon_{L,t}$$ This follows the same pattern as the proof for the fact that $\Lambda$ weakly preserves composition of morphisms. Note that the two sides of this expression are the top and bottom of a (weak) pullback square. So in particular, the argument for weak preservation of composition of spans shows that we also have a pullback square for the induced functors.

In particular (ignoring the identity maps), we first get the right unit for $S : Y' \circ Y \mathop{\rightarrow}Y$, which at $y \in G(y) \cong G(a_1)$ gives: $$\eta_{R,S} : v \mapsto \bigoplus_{[(y,f,y')]} \frac{1}{\# Aut(y,f,y')} \sum_{g \in Aut(y)} (g^{-1}) \otimes g(v)$$ and the left counit for $T : Y' \circ Y \mathop{\rightarrow}Y'$ takes this to. So this gives $$\epsilon_{L,T} \circ \eta_{R,S}: v \mapsto \sum_{[(y,f,y')]} \frac{1}{\# Aut(y,f,y')} \sum_{g \in Aut(y)} (g^{-1}) \otimes g(v)$$ since the target space is now already a tensor product over $\mathbb{C}[Aut(x_2)]$. Similarly, on the other side we have first the left counit for $t : Y \mathop{\rightarrow}X_2$, then the right unit for $s' : Y' \mathop{\rightarrow}X_2$, giving: $$\eta_{R,s'} \circ \epsilon_{L,t} : v \mapsto \sum_{[y'] | s'(y') \cong t(y)} \frac{1}{\# Aut(t(y))} \sum_{g \in Aut(x_2)} g^{-1} \otimes g(v)$$ Since the sources and targets of the maps ([\[eq:leftcounit\]](#eq:leftcounit){reference-type="ref" reference="eq:leftcounit"}) and ([\[eq:rightunit\]](#eq:rightunit){reference-type="ref" reference="eq:rightunit"}) are in a pullback square, the coefficients arising from the Nakayama isomorphisms will yield the same group averages, and the terms of the implied direct sum correspond pairwise. So these maps are indeed equal. ◻
:::

We also must show that $\Lambda$ respects horizontal composition weakly. To make this clear, it will be convenient to write source and target 2-linear maps in the form ([\[eq:composedFV\]](#eq:composedFV){reference-type="ref" reference="eq:composedFV"}) and ([\[eq:FVcomposed\]](#eq:FVcomposed){reference-type="ref" reference="eq:FVcomposed"}).

::: lemma
[]{#thm:horizcompos label="thm:horizcompos"}The assignment $\Lambda(Y)$ to spans of spans given by Definition [\[def:Von2Span\]](#def:Von2Span){reference-type="ref" reference="def:Von2Span"} preserves horizontal composition strictly, up to the isomorphism weakly preserving composition of the source and target morphisms: $$\label{eq:horizcompos}
\xymatrix{
\Lambda(A_1) \ar@/^3pc/[rrrr]^{\Lambda({X'}_1 \circ X_1)}="a" \ar@{}[rrrr]^{}="c" \ar@/_3pc/[rrrr]_{\Lambda({X'}_2 \circ X_2)}="b" \ar@/^1pc/[rr]^{\Lambda(X_1)}="1" \ar@/_1pc/[rr]_{\Lambda(X_2)}="2"  & & \Lambda(A_2') \ar@/^1pc/[rr]^{\Lambda(X'_1)}="3" \ar@/_1pc/[rr]_{\Lambda({X'}_2)}="4" & & \Lambda(A_3) \\
 {\ar@{=>}"1"+<0ex,-2.5ex> ;"2"+<0ex,+2.5ex>^{\Lambda(Y)}}
 {\ar@{=>}"3"+<0ex,-2.5ex> ;"4"+<0ex,+2.5ex>^{\Lambda(Y')}}
 {\ar@{=>}"a"+<0ex,-2.5ex> ;"c"+<0ex,+2.5ex>^{\beta_{X_1,{X'}_1}}}
 {\ar@{=>}"c"+<0ex,-2.5ex> ;"b"+<0ex,+2.5ex>^{\beta_{X_2,{X'}_2}^{-1}}}
}
=
\xymatrix{
\Lambda(A_1) \ar@/^2pc/[rrrr]^{\Lambda({X'}_1 \circ X_1)}="1" \ar@/_2pc/[rrrr]_{\Lambda({X'}_2 \circ X_2)}="2" & & & & \Lambda(A_3) \\
 {\ar@{=>}"1"+<0ex,-2.5ex> ;"2"+<0ex,+2.5ex>^{\Lambda(Y' \circ Y)}}
}$$
:::

::: proof
*Proof.* (Elsewhere, we have used the same notation for horizontal and vertical composition of all kinds, to simplify notation and because context made this unambiguous. In this proof it will be helpful to distinguish the two, so we write vertical composition with no symbol, concatenating natural transformations between 2-linear maps.)

Begin by writing the spans explicitly. The situation for a horizontal composite of 2-morphisms in $\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$ looks like: $$\label{xy:horizontalcomposite}
\xymatrix{
 & & {X'}_1 \circ X_1 \ar[ld]_{S_1} \ar[rd]^{T_1} & & \\
 & X_1 \ar@{=>}[rr]^{\alpha_1}_{\sim} \ar[ld]_{s_1} \ar[rd]^{t_1} & & X'_1 \ar[ld]_{s'_1} \ar[rd]^{t'_1} & \\
A_1 & Y \ar[u]^{s} \ar[d]_{t} \ar@{-->}[l]_{\sigma} \ar@{-->}[r]^{\tau} & A_2 & Y' \ar[u]^{s'} \ar[d]_{t'} \ar@{-->}[l]_{\sigma '} \ar@{-->}[r]^{\tau '} & A_3 \\
 & X_2 \ar@{=>}[rr]^{\alpha_2}_{\sim} \ar[lu]^{s_2} \ar[ur]_{t_2} & & X'_2 \ar[lu]^{s'_2} \ar[ur]_{t'_2} & \\
 & & {X'}_2 \circ X_2 \ar[lu]^{S_2} \ar[ru]_{T_2} & &
}$$ (Note that here again we are assuming the 2-morphisms $Y$ and $Y'$ are strict, so that $s_1 \circ s = s_2 \circ t$ and similarly for the other composites. We represent these by the dotted arrows $\sigma$, $\tau$, $\sigma '$ and $\tau '$. As before, a similar argument would go through if these spans of span maps were only weakly commuting, but we would need the $\zeta$ natural transformations as discussed for ([\[xy:spanmapspan\]](#xy:spanmapspan){reference-type="ref" reference="xy:spanmapspan"})).

Now, the functor $\Lambda$ assigns 2-linear maps to the spans $X_1$, $X_2$, ${X'}_1$, and ${X'}_2$, and their composites, and natural transformations to $Y$ and $Y'$. Then the horizontal composite is a natural transformation between 2-linear maps: $$\label{eq:horizFV}
\Lambda(Y') \circ \Lambda(Y) : \Lambda({X'}_1) \circ \Lambda(X_1) \mathop{\rightarrow}\Lambda({X'}_2) \circ \Lambda(X_2)$$ And we can calculate as in the proof of Theorem [\[thm:vertcompos\]](#thm:vertcompos){reference-type="ref" reference="thm:vertcompos"} that: $$\Lambda(Y')(a_1) = \epsilon_{L,t'} \eta_{R,s'} : v \mapsto \bigoplus_{[y] | s'(y')  \cong x_1}\frac{\# Aut(y)}{\# Aut(y,f,y')} v$$ and $$\Lambda(Y) = \epsilon_{L,t} \eta_{R,s}$$

So the composite is just $$\Lambda(Y') \circ \Lambda(Y) = (\epsilon_{L,t'} \eta_{R,s'})\circ (\epsilon_{L,t} \eta_{R,s})$$

We recall that $\Lambda(X') \circ \Lambda(X)$ is described explicitly in ([\[eq:composedFV\]](#eq:composedFV){reference-type="ref" reference="eq:composedFV"}) and $\Lambda(X' \circ X)$ in ([\[eq:FVcomposed\]](#eq:FVcomposed){reference-type="ref" reference="eq:FVcomposed"}). Finding these for the $X_i$ gives a total of four functors here. We next describe natural transformations between these.

As shown in Theorem [\[thm:FVcomposfunc\]](#thm:FVcomposfunc){reference-type="ref" reference="thm:FVcomposfunc"}, there are comparison isomorphisms $$\beta_{X_i,{X'}_i} : \Lambda({X'}_i) \circ \Lambda(X_i) \mathop{\rightarrow}\Lambda({X'}_i \circ X_i)$$ which will necessarily be involved in the isomorphism we are looking for. These derive from the $\alpha$ isomorphisms in the weak pullback in ${X'}_i \circ X_i$.

Composing with these comparison isomorphisms as in ([\[eq:horizcompos\]](#eq:horizcompos){reference-type="ref" reference="eq:horizcompos"}) gives: $$(\operatorname{Id}_{s_1^{\ast}} \circ \beta_{X_1,{X'}_1} \circ \operatorname{Id}_{({t'}_1)^{\ast}}) (\epsilon_{L,t'} \eta_{R,s'})  (\epsilon_{L,t} \eta_{R,s}) (\operatorname{Id}_{{s_2}^{\ast}} \circ (\beta_{X_2,{X'}_2})^{-1} \circ \operatorname{Id}_{({t'}_2)^{\ast}})$$

Now, the $\beta$ isomorphisms simply allow us to identify the spaces here, so it suffices to describe the maps, and in particular the coefficients which arise. At any presheaf $G$ on $A_1$, in the summand for $[a_1] \in \underline{A_1}$ and $[x'_1] \in X'_1$: $$(\epsilon_{L,t} \eta_{R,s}) : v \mapsto \sum_{[y] | s(y) \cong x_1} \frac{1}{\# Aut(y)} \sum_{g \in Aut(x_1)} g^{-1} \otimes g(v)$$ which is a map between spaces of the form ([\[eq:firststepFV\]](#eq:firststepFV){reference-type="ref" reference="eq:firststepFV"}) associated to $X_1$ and $X_2$. Now this becomes the $v'$ when we take the full map between spaces like ([\[eq:composedFV\]](#eq:composedFV){reference-type="ref" reference="eq:composedFV"}), where we have: $$(\epsilon_{L,t'} \eta_{R,s'}): v' \mapsto \sum_{[y'] | s'(y) \cong {x'}_1} \frac{1}{\# Aut(y')} \sum_{h \in Aut({x'}_1)} h^{-1} \otimes h(v')$$ so finally we get: $$v \mapsto \sum_{[y'] | s'(y) \cong {x'}_1} \frac{1}{\# Aut(y')} \sum_{h \in Aut({x'}_1)} h^{-1} \otimes h \bigl{(} \sum_{[y] | s(y) \cong x_1} \frac{1}{\# Aut(y)} \sum_{g \in Aut(x_1)} g^{-1} \otimes g(v) \bigr{)}$$ which we want to show is the same as the natural transformation associated to $\Lambda(Y' \circ Y)$: $$\label{eq:FVhoriz}
\Lambda(Y' \circ Y) = \epsilon_{L,(t,t')} \circ \eta_{R,(s,s')} : \Lambda({X'}_1 \circ X_1) \mathop{\rightarrow}\Lambda({X'}_2 \circ X_2)$$ which is a map between two spaces of the form ([\[eq:FVcomposed\]](#eq:FVcomposed){reference-type="ref" reference="eq:FVcomposed"}).

This $Y' \circ Y : {X'}_1 \circ X_1 \mathop{\rightarrow}{X'}_2 \circ X_2$ is a span of span maps which is given as follows. We take the horizontal composite of the spans $A_1 \stackrel{\sigma}{\mathop{\leftarrow}} Y \stackrel{\tau}{\mathop{\rightarrow}} A_2$ and $A_2 \stackrel{\sigma '}{\mathop{\leftarrow}} Y' \stackrel{\tau '}{\mathop{\rightarrow}} A_3$. This is a weak pullback taken up to isomorphism. The pullback square commutes weakly, say up to $\xi$. Then the groupoid $Y' \circ Y$ has maps into $Y$ and $Y'$, and therefore by composition with $s$ and $s'$, it has maps into $X_1$ and ${X'}_1$. By the universal property of the weak pullback ${X'}_1 \circ X_1$, there is a map $S : Y' \circ
Y \mathop{\rightarrow}{X'}_1 \circ X_1$. Similarly, there is $T : Y' \circ Y \mathop{\rightarrow}
{X'}_2 \circ X_2$.

We can see what this is by taking the weak pullback giving $Y' \circ
Y$, which we take to be the comma category whose objects are of the form $(y,f,y')$ where $f : \tau(y) \mathop{\rightarrow}\sigma '(y')$ in $A_2$. Then the $S$ and $T$ given by the universal property are just $S = (s,s')$ giving objects like $(x_1,f,{x'}_1)$ and $T = (t,t')$ giving objects like $(x_2,f,{x'}_2)$. In particular, the morphism $f \in A_2$ is left intact. (Different isomorphic choices for weak pullback could of course change $f$).

Given this, we have, in the summand for a given $[a_1] \in \underline{A_1}$: and a particular $[(x_1,f,x'_1)] \in X'_1 \circ X_1$, we have: $$\eta_{R,(s,s')} : v \mapsto \mathop{\bigoplus_{\stackrel{[y,f,y']}{s(y) \cong x_1}}}_{s'(y') \cong x'_1} \frac{1}{\# Aut(y,f,y')} \sum_{(g,h) \in Aut(x,f,x')} (g,h)^{-1} \otimes (g,h)(v)$$ and then $$\epsilon_{L,(t,t')} \eta_{R,(s,s')} : v \mapsto \mathop{\sum_{\stackrel{[y,f,y']}{s(y) \cong x_1}}}_{s'(y') \cong x'_1}  \frac{1}{\# Aut(y,f,y')} \sum_{(g,g') \in Aut(x,f,x')} (g,h)^{-1} \otimes (g,h)(v)$$

So in fact, since we are in a weak pullback square, the size of the automorphism groups in the two expressions we have found will be in the same ratios, and so it becomes clear that, using the $\beta$ isomorphisms as seen in the proof of Theorem [\[thm:FVcomposfunc\]](#thm:FVcomposfunc){reference-type="ref" reference="thm:FVcomposfunc"}: $$\Lambda(Y' \circ Y) = \beta_{X_1,{X'}_1} (\Lambda(Y') \Lambda(Y)) (\beta_{X_2,{X'}_2})^{-1}$$ as required. ◻
:::
