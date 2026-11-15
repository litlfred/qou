---
doc_id: arxiv-0810.2361v2
doc_title: "2-VECTOR SPACES AND GROUPOIDS"
section_id: sec-017-71-the-2-linearization-functor
section_title: "The 2-Linearization Functor"
section_number: 7.1
pages: 38-41
source_pdf: 0810.2361v2.pdf
source_sha256: 77d6d59a29596484
toc_source: outline
text_source: latex
latex_prose_ratio: 0.93
latex_coverage_ratio: 0.957
doc_brief: "2-VECTOR SPACES AND GROUPOIDS — This paper describes a relationship between essentially ﬁnite groupoids and 2-vector spaces."
---
We have been defining the maps involved in $\Lambda$ throughout the last few sections, so here we collect the full definition in one place.

::: definition
[]{#def:Vrep label="def:Vrep"} The 2-linearization process $\Lambda:
\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}}) \mathop{\rightarrow}\boldsymbol{\operatorname{{2Vect}}}$ is defined as follows:

-   For an essentially finite groupoid $A$ it assigns: $$\label{eq:VonGpd}
      \Lambda(A) = [A,\boldsymbol{\operatorname{{Vect}}}]$$

-   For a span of groupoids: $$A \mathop{\mathop{\leftarrow}}\limits^{s} X \mathop{\mathop{\rightarrow}}\limits^{t} B$$ it assigns: $$\label{eq:VonSpan}
      \Lambda(S) = t_{\ast} \circ s^{\ast}$$

-   For a (strictly commuting) span of maps between two spans with the same source and target: $$\xymatrix{
     & X_1 \ar[dl]_{s_1} \ar[dr]^{t_1} & \\
    A & Y \ar[u]_{s} \ar[d]^{t} & B  \\
     & X_2  \ar[ul]_{s_2} \ar[ur]^{t_2} & \\
    }$$ $\Lambda$ assigns a natural transformation: $$\Lambda(Y) = \epsilon_{L,t} \circ \eta_{R,s} : (t_1)_{\ast}s_1^{\ast} \Longrightarrow (t_2)_{\ast}s_2^{\ast}$$ (and analogously for weakly commuting spans of maps as in Definition [\[def:Von2Span\]](#def:Von2Span){reference-type="ref" reference="def:Von2Span"})

$\Lambda$ also associates the following:

-   For each composable pair $X : A_1 \mathop{\rightarrow}A_2$ and $X' : A_2 \mathop{\rightarrow}A_3$, a natural isomorphism $$\beta : \Lambda( X' \circ X ) \mathop{\rightarrow}\Lambda(X') \circ \Lambda(X)$$, as described in Theorem [\[thm:FVcomposfunc\]](#thm:FVcomposfunc){reference-type="ref" reference="thm:FVcomposfunc"}.

-   For each object $X \in \boldsymbol{\operatorname{{FinGpd}}}$, the natural transformation $$U_B : 1_{\Lambda(B)} \stackrel{\sim}{\mathop{\rightarrow}} \Lambda(1_B)$$ is the natural transformation induced by the equivalence between ${B}$ and ${1_B}$.
:::

Then we have the following:

::: theorem
[]{#thm:mainthm label="thm:mainthm"} The construction given in Definition [\[def:Vrep\]](#def:Vrep){reference-type="ref" reference="def:Vrep"} defines a weak 2-functor $\Lambda: \operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}}) \mathop{\rightarrow}\boldsymbol{\operatorname{{2Vect}}}$ .
:::

::: proof
*Proof.* First, we note that by the result of Lemma [\[lemma:fgkv\]](#lemma:fgkv){reference-type="ref" reference="lemma:fgkv"}, we know that $\Lambda$ assigns a 2-vector space to each object of $\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$.

If $S : B \mathop{\rightarrow}B'$ span of essentially finite groupoids---i.e. a morphism in $\operatorname{Span}(\boldsymbol{\operatorname{{FinGpd}}})$, the map $\Lambda(S)$ defined in Definition [\[def:ZGonS\]](#def:ZGonS){reference-type="ref" reference="def:ZGonS"} is a linear functor by the result of Theorem [\[thm:2mapadjoints\]](#thm:2mapadjoints){reference-type="ref" reference="thm:2mapadjoints"}, since it is a composite of two linear maps. This respects composition of morphisms, as shown in Theorem [\[thm:FVcomposfunc\]](#thm:FVcomposfunc){reference-type="ref" reference="thm:FVcomposfunc"}, and of 2-morphisms in both horizontal and vertical directions, as shown in Theorems [\[thm:vertcompos\]](#thm:vertcompos){reference-type="ref" reference="thm:vertcompos"} and [\[thm:horizcompos\]](#thm:horizcompos){reference-type="ref" reference="thm:horizcompos"}.

Next we need to check that our $\Lambda$ satisfies the remaining properties of a weak 2-functor: that the isomorphisms from the weak preservation of composition and units satisfy the requisite coherence conditions; and that $\Lambda$ strictly preserves horizontal and vertical composition of natural transformations.

The coherence conditions for the compositor morphisms $$\beta_{S,T} :   \Lambda(T \circ S) \mathop{\rightarrow}\Lambda(T) \circ \Lambda(S)$$ and the associator say that these must make the following diagram commute for all composable triples $(X,X',X'')$: $$\label{eq:wk2fncassoc}
\xy
 (0,20)*+{\Lambda(X'') \circ \Lambda(X') \circ \Lambda(X)}="top";
 (35,4)*+{\Lambda(X'' \circ X') \circ \Lambda(X)}="rttop";
 (25,-20)*+{\Lambda( (X'' \circ X') \circ X )}="rtbot";
 (-25,-20)*+{\Lambda(X'' \circ (X' \circ X) )}="leftbot";
 (-35,4)*+{\Lambda(X'') \circ \Lambda(X' \circ X)}="leftop";
     {\ar^{1 \otimes \beta_{2,1}} "leftop";"top"}
     {\ar_{\beta_{3,2} \otimes 1} "rttop";"top"}
     {\ar^{\beta_{3,21}} "leftbot";"leftop"}
     {\ar_{\beta_{32,1}} "rtbot";"rttop"}
     {\ar_{\Lambda(\alpha_{X'',X',X})} "leftbot";"rtbot"}
\endxy$$

We implicitly assume here a trivial associator for the 2-linear maps in the expression $\Lambda(X'') \circ \Lambda(X') \circ \Lambda(X)$. This is because each 2-linear map is just a composite of functors, so this composition is associative. But note that we can similarly assume, without loss of generality, that the associator $\alpha$ for composition of spans is trivial. The composite $X' \circ X$ is a weak pullback. This is only defined up to isomorphism, but one candidate is the comma category for any $x \in A_2$. Any other candidate is isomorphic to this one. But then, the associator $$\alpha_{X'',X',X} : \Lambda( X'' \circ (X' \circ X) ) \mathop{\rightarrow}\Lambda( (X'' \circ X') \circ X )$$ is just given by the obvious canonical map between the comma categories. In particular, both composites give comma categories whose objects are determined by choices $(x,f,x',g,x'')$ where $f :
t_1(x) \mathop{\rightarrow}s_2(x')$ and $g : t_2(x') \mathop{\rightarrow}s_3(x'')$, and whose morphisms are triples of morphisms in $X \times X' \times X''$ making the appropriate diagrams commute. However, these comma categories are defined in terms of pairs, with different parenthesizations. So $\alpha_{X'',X',X}$ is the evident isomorphism between these composites.

So it suffices to show that, up to this identification: $$(1 \otimes \beta_{X',X}) \circ \beta_{X'',X'\circ X} = (\beta_{X'',X'} \otimes 1) \circ \beta_{X'' \circ X',X}$$ The $\beta$ isomorphisms are given by the $\alpha$ up to which the weak pullbacks commute, and so are given by choices of the functions $f \in A_2$ and $g \in A_3$ in the comma categories. The associator isomorphism induces an corresponding isomorphism between these composite $\beta$ maps by the correspondence between the choices of $f$ and $g$ in the pullback squares on each side of this equation. So indeed, this is true.

In general, the coherence conditions for the "unit" isomorphism $$U_A : 1_{\Lambda(A)} \stackrel{\sim}{\mathop{\rightarrow}} \Lambda(1_A)$$ which accomplishes weak preservation of identities, say that it must make the following commute for any span $X: A_1 \mathop{\rightarrow}A_2$: $$\label{eq:wk2fncunit}
\xymatrix{
\Lambda(X)  & & \\
 & &  \\
\Lambda(X) \circ \Lambda(1_{A_1}) \ar[uu]_{1 \otimes U_{A_1}} &  & \Lambda(X \circ 1_{A_1})\ar[uull]_{\Lambda(r_X)} \ar[ll]_{\beta_{X,1_{A_1}}}
}$$ where $r_{A_1}$ is the right unitor for $A_1$. There is also the symmetric condition for the left unitor.

We notice that, as with $\Lambda(1_{A_1})$, $\Lambda(r_{A_1})$ is equivalent to the identity. The map $r_X : X \circ 1_{A_1} \mathop{\rightarrow}X$ is the canonical isomorphism taking composition of $X$ with an identity span to $X$ which is just a projection from a comma category. Since $X \circ 1_{A_1}$ and $X$ are thus isomorphic, .

So the condition amounts to the fact that $\beta_{X,1_{A_1}} : \Lambda(X
\circ 1_{A_1}) \mathop{\rightarrow}\Lambda(X) \circ \Lambda(1_{A_1}) = \Lambda(X)$ is equivalent to the identity in such a way that ([\[eq:wk2fncunit\]](#eq:wk2fncunit){reference-type="ref" reference="eq:wk2fncunit"}) commutes. But this is immediate since this $\beta$ map is being applied to an identity span. ◻
:::
