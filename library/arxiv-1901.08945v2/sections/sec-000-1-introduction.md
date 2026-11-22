---
doc_id: arxiv-1901.08945v2
doc_title: "Decompositions of derived categories of gerbes and families of Brauer–Severi varieties"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: 1901.08945v2.pdf
source_sha256: df222d76e597057f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.958
doc_brief: "Decompositions of derived categories of gerbes and families of Brauer–Severi varieties — It is well known that the category of quasi-coherent sheaves on a gerbe banded by a diagonalizable group"
---
The concept of a *twisted sheaf* goes back to Giraud and his formal treatment of the Brauer group in terms of *gerbes* [@giraud1971 Section V.4]. During the last two decades, twisted sheaves and their derived categories have gained a renewed interest, starting with the thesis of Căldăraru [@caldararu2000], who studied moduli problems for semi-stable sheaves on varieties, and the work by de Jong [@dejong2004] and Lieblich [@lieblich2004; @lieblich2015] on the period--index problem for the Brauer group. For a survey on later developments, we refer to Lieblich [@lieblich2017 Section 4].

Although twisted sheaves have a rather elementary description in terms of 2-cocycles (cf. Remark [\[rem-twisted-2-cocycle\]](#rem-twisted-2-cocycle){reference-type="ref" reference="rem-twisted-2-cocycle"}), they are most naturally viewed as sheaves on gerbes banded by diagonalizable groups (see Definition [\[def:twisted\]](#def:twisted){reference-type="ref" reference="def:twisted"}). Our first result is the following theorem on the decomposition of the derived category associated to such a gerbe, generalizing a result by Lieblich [@lieblich2004 Section 2.2.4].

::: mtheorem
[]{#t:chi-splitting-D-qc-X-intro label="t:chi-splitting-D-qc-X-intro"} Let $S$ be an algebraic stack and $\pi\colon X \to S$ a gerbe banded by a diagonalizable group $\Delta$ with character group $A$. Then taking the coproduct defines an equivalence $$\label{eq-equivalence-derived-intro}
    \prod_{\chi \in A} {\operatorname{D}}_{{\operatorname{qc}}, \chi}(X) \xrightarrow[{}]{\sim}{\operatorname{D}}_{\operatorname{qc}}(X),
    \qquad
    (\mathcal{F}_\chi)_{\chi \in A} 
    \mapsto 
    \bigoplus_{\chi \in A} \mathcal{F}_\chi,$$ of triangulated categories, where ${\operatorname{D}}_{{\operatorname{qc}}, \chi}(X)$ denotes the full subcategory of ${\operatorname{D}}_{\operatorname{qc}}(X)$ of objects with $\chi$-homogeneous quasi-coherent cohomology (see Definition [\[def-homogeneous-sheaf\]](#def-homogeneous-sheaf){reference-type="ref" reference="def-homogeneous-sheaf"}).
:::

In the underived setting, a splitting similar as in the theorem above (see Theorem [\[t-qc-gerbe-split\]](#t-qc-gerbe-split){reference-type="ref" reference="t-qc-gerbe-split"}) is a consequence of the well-known fact that quasi-coherent representations of $\Delta$ split into subrepresentations corresponding to the characters of the group $\Delta$.

The result by Lieblich is the decomposition in Theorem [\[t:chi-splitting-D-qc-X-intro\]](#t:chi-splitting-D-qc-X-intro){reference-type="ref" reference="t:chi-splitting-D-qc-X-intro"} in the special case when $S$ is a quasi-compact, separated scheme. He proves and uses the fact that in this setting the obvious functor $$\label{eq-dqcoh-vs-dqcoh}
{\operatorname{D}}({\ensuremath{\operatorname{Qcoh}}}(X)) \to {\operatorname{D}}_{\operatorname{qc}}(X)$$ is an equivalence of categories [@lieblich2004 Proposition 2.2.4.6]. Note that, if the base $S$ is a scheme, the functor [\[eq-dqcoh-vs-dqcoh\]](#eq-dqcoh-vs-dqcoh){reference-type="eqref" reference="eq-dqcoh-vs-dqcoh"} only fails to be an equivalence in truly pathological situations. However, as shown by Hall--Neeman--Rydh [@hnr2018 Theorem 1.3], the functor [\[eq-dqcoh-vs-dqcoh\]](#eq-dqcoh-vs-dqcoh){reference-type="eqref" reference="eq-dqcoh-vs-dqcoh"} fails to be an equivalence for large classes of algebraic stacks, including the basic case when $X$ is the classifying stack $\mathop{\mathrm{B}}\mathop{\mathrm{GL}}_n$ of the general linear group (see Remark [\[rem-trivial-case\]](#rem-trivial-case){reference-type="ref" reference="rem-trivial-case"}). In particular, this kind of argument cannot be used to obtain the splitting of the derived category of one of the most fundamental examples of gerbes banded by ${\ensuremath{\mathbb{G}_{\operatorname{m}}}}$ --- namely the *gerbe of trivializations* $\mathop{\mathrm{B}}\mathop{\mathrm{GL}}_n \to \mathop{\mathrm{B}}\mathop{\mathrm{PGL}}_n$ for the universal Brauer--Severi scheme (see Remark [\[rem-universal-gerbe-of-trivializations\]](#rem-universal-gerbe-of-trivializations){reference-type="ref" reference="rem-universal-gerbe-of-trivializations"}).

In order to prove Theorem [\[t:chi-splitting-D-qc-X-intro\]](#t:chi-splitting-D-qc-X-intro){reference-type="ref" reference="t:chi-splitting-D-qc-X-intro"}, we study the more general problem whether suitable torsion pairs in abelian categories induce semi-orthogonal decompositions on the level of derived categories. We achieve the following theorem of independent interest.

::: mtheorem
[]{#t:sod-DBA-intro label="t:sod-DBA-intro"} Let $\mathcal{B}$ be a weak Serre subcategory of an abelian category $\mathcal{A}$. Let $\mathcal{T}$ and $\mathcal{F}$ be abelian subcategories of $\mathcal{B}$ forming a torsion pair $(\mathcal{T}, \mathcal{F})$ in $\mathcal{B}$. Assume that $$\mathop{\mathrm{Ext}}^n_{\mathcal{A}}(T, F)=0$$ for all objects $T \in \mathcal{T}$, $F \in \mathcal{F}$ and all integers $n$. Then $${\operatorname{D}}_{\mathcal{B}}^{\operatorname{b}}(\mathcal{A})=
    \langle {\operatorname{D}}_{\mathcal{F}}^{\operatorname{b}}(\mathcal{A}), 
    {\operatorname{D}}_{\mathcal{T}}^{\operatorname{b}}(\mathcal{A})\rangle$$ is a semi-orthogonal decomposition. Furthermore, if the inclusion ${\operatorname{D}}_{\mathcal{B}}(\mathcal{A})
  \subset {\operatorname{D}}(\mathcal{A})$ satisfies some technical conditions on homotopy limits and colimits formulated precisely in the statement of Theorem [\[t:sod-DBA\]](#t:sod-DBA){reference-type="ref" reference="t:sod-DBA"}, then $${\operatorname{D}}_{\mathcal{B}}(\mathcal{A})=
    \langle {\operatorname{D}}_{\mathcal{F}}(\mathcal{A}), 
    {\operatorname{D}}_{\mathcal{T}}(\mathcal{A})\rangle$$ is a semi-orthogonal decomposition.
:::

The theory of gerbes, hinging on the theory of stacks, used to have a reputation of being inaccessible, and Giraud's book on non-abelian cohomology [@giraud1971] introducing them is notorious for being a hard read, even among experts. However, in recent years the theory of algebraic stacks has become a main stream part of algebraic geometry, much owing to the excellent text books by Laumon--Moret-Bailly [@lmb2000] and Olsson [@olsson2016], and to the Stacks Project [@stacks-project]. Moreover, as explained in the thesis by Lieblich [@lieblich2004], only a small part of Giraud's theory is actually needed to develop a satisfactory theory of twisted sheaves. We illustrate the effectiveness of the language of gerbes by giving a short, simple and conceptually appealing proof of the following theorem, which generalizes a result by Bernardara [@bernardara-BS-schemes Theorem 4.1].

::: mtheorem
[]{#t:sod-brauer-severi-intro label="t:sod-brauer-severi-intro"} Let $S$ be an algebraic stack and $\pi\colon P \to S$ a Brauer--Severi scheme of relative dimension $n$ over $S$. Let $\beta \in \mathop{\mathrm{H}}^2(S_{\operatorname{fppf}}, {\ensuremath{\mathbb{G}_{\operatorname{m}}}})$ denote the Brauer class of $\pi$. Then, for any $a \in {\mathbb{Z}}$, the category ${\operatorname{D}}_{\operatorname{qc}}(P)$ admits a semi-orthogonal decomposition $$\label{eq:SOD-Dpf}
    {\operatorname{D}}_{\operatorname{qc}}(P) = \langle \mathcal{D}_a, \ldots, \mathcal{D}_{a+n}
    \rangle$$ into right admissible subcategories $\mathcal{D}_i$, where the category $\mathcal{D}_i$ is equivalent to the category ${\operatorname{D}}_{{\operatorname{qc}},\beta^i}(S)$ of $\beta^i$-twisted complexes on $S$ (see Definition [\[def:derived-twisted\]](#def:derived-twisted){reference-type="ref" reference="def:derived-twisted"} and Remark [\[r:image-twisted\]](#r:image-twisted){reference-type="ref" reference="r:image-twisted"}).

Similarly, we have corresponding decompositions for the category of perfect complexes, the category of locally bounded pseudo-coherent complexes and the singularity category. In particular, we also have such a decomposition for ${\operatorname{D}}^b_{\operatorname{coh}}(P)$ when $S$ is Noetherian.
:::

Bernardara's result is the semi-orthogonal decomposition [\[eq:SOD-Dpf\]](#eq:SOD-Dpf){reference-type="eqref" reference="eq:SOD-Dpf"} in the case when $S$ is a Noetherian, separated scheme with the property that any pair of points in $S$ is contained in an open affine subscheme (cf. Remark [\[r:bernardara\]](#r:bernardara){reference-type="ref" reference="r:bernardara"}). Apart from our Theorem [\[t:chi-splitting-D-qc-X-intro\]](#t:chi-splitting-D-qc-X-intro){reference-type="ref" reference="t:chi-splitting-D-qc-X-intro"}, the main ingredient in our proof of Theorem [\[t:sod-brauer-severi-intro\]](#t:sod-brauer-severi-intro){reference-type="ref" reference="t:sod-brauer-severi-intro"} is a classical result by Orlov regarding a semi-orthogonal decomposition of the derived category of a projectivized vector bundle [@orlov1992 Theorem 2.6], which we previously have generalized to algebraic stacks using the technique of *conservative descent* [@BS-conservative Theorem 6.7, Corollary 6.8].

While finishing the manuscript, we were informed by Brown and Moulinos of a result [@bm2019 Theorem 3.1] which is similar to our Theorem [\[t:sod-brauer-severi-intro\]](#t:sod-brauer-severi-intro){reference-type="ref" reference="t:sod-brauer-severi-intro"}.

## Outline

In Section [\[sec:torsion-pairs-decomp\]](#sec:torsion-pairs-decomp){reference-type="ref" reference="sec:torsion-pairs-decomp"}, we work mostly in the general setting of derived categories of abelian categories. This section contains the proof of Theorem [\[t:sod-DBA-intro\]](#t:sod-DBA-intro){reference-type="ref" reference="t:sod-DBA-intro"}. In Section [\[sec:gerbes-and-twisted\]](#sec:gerbes-and-twisted){reference-type="ref" reference="sec:gerbes-and-twisted"} and Section [\[sec:quasi-coher-sheav\]](#sec:quasi-coher-sheav){reference-type="ref" reference="sec:quasi-coher-sheav"}, we recall and collect some basic facts on gerbes, bandings and twisted sheaves which are scattered in the literature. We expect most of these results to be well known to experts. In Section [\[sec:decomp-deriv-categ\]](#sec:decomp-deriv-categ){reference-type="ref" reference="sec:decomp-deriv-categ"}, we turn our attention to derived categories of gerbes and twisted sheaves. We generalize some of the fundamental results by Căldăraru and Lieblich [@caldararu2000; @lieblich2004] to the case when we work over an algebraic stack. Most notably we prove Theorem [\[t:chi-splitting-D-qc-X-intro\]](#t:chi-splitting-D-qc-X-intro){reference-type="ref" reference="t:chi-splitting-D-qc-X-intro"}. Finally, in the last section, we give a brief summary on Giraud's treatment of the Brauer group [@giraud1971 Section V.4], and use the theory to prove Theorem [\[t:sod-brauer-severi-intro\]](#t:sod-brauer-severi-intro){reference-type="ref" reference="t:sod-brauer-severi-intro"}.

## Acknowledgments

The first named author was partially supported by the Danish National Research Foundation through the Niels Bohr Professorship of Lars Hesselholt, by the Max Planck Institute for Mathematics in Bonn, and by the DFG through SFB/TR 45. The second named author was partially supported by the DFG through a postdoctoral fellowship and through SFB/TR 45.

## Notation and conventions {#sec:conventions}

If $\mathcal{A}$ is an abelian category, we write ${\operatorname{D}}(\mathcal{A})$ for its unbounded derived category. We write ${\operatorname{D}}^{\leq n}(\mathcal{A})$ and ${\operatorname{D}}^{\geq n}(\mathcal{A})$ for its full subcategories of objects whose cohomology is concentrated in the indicated degrees, where $n \in {\mathbb{Z}}$. The (intelligent) truncation functors on ${\operatorname{D}}(\mathcal{A})$ are denoted $\tau_{\leq n}$ and $\tau_{\geq n}$. If $E$ and $F$ are objects of ${\operatorname{D}}(\mathcal{A})$, we sometimes abbreviate $\mathop{\mathrm{Ext}}^n_\mathcal{A}(E,F):=\mathop{\mathrm{Hom}}_{{\operatorname{D}}(\mathcal{A})}(E, \Sigma^nF)$.

By a *diagonalizable group* we mean a diagonalizable group scheme over $\mathop{\mathrm{Spec}}{\mathbb{Z}}$ that is isomorphic to the spectrum of the group ring of a finitely generated abelian group.

We use the definitions of algebraic space and algebraic stack given in the stacks project [@stacks-project [Tag 025Y](http://stacks.math.columbia.edu/tag/025Y), [Tag 026O](http://stacks.math.columbia.edu/tag/026O)]. In particular, we do not impose any separatedness conditions. The algebraic stacks form a 2-category where each 2-morphism is invertible. We will follow the common practice to often suppress 2-categorical details. For instance, we will usually simply write morphism of stacks instead of 1-morphism of stacks, subcategory of the category of stacks instead of 2-subcategory etc.

For the theory of quasi-coherent modules and derived categories in the context of algebraic stacks, we basically follow the approach of Laumon--Moret-Bailly [@lmb2000 Sections 12 and 13], which we now briefly recapitulate. Let $X$ be an algebraic stack. We denote the topos of sheaves on the big *fppf* site over $X$ by $X_{\operatorname{fppf}}$ and the topos of sheaves on the *lisse--étale* site over $X$ by $X_{\operatorname{lis-\acute{e}t}}$. For $\tau \in \{{\operatorname{fppf}}, {\operatorname{lis-\acute{e}t}}\}$, we let ${\ensuremath{\operatorname{Mod}}}(X_\tau, \mathcal{O}_X)$ denote category of $\mathcal{O}_X$-modules in $X_\tau$, and ${\ensuremath{\operatorname{Qcoh}}}(X_\tau, \mathcal{O}_X)$ the full subcategory of quasi-coherent modules (see [@stacks-project [Tag 03DL](http://stacks.math.columbia.edu/tag/03DL)]).

::: remark
[]{#rem-coherator label="rem-coherator"} The categories ${\ensuremath{\operatorname{Qcoh}}}(X_\tau, \mathcal{O}_X)$ and ${\ensuremath{\operatorname{Mod}}}(X_\tau, \mathcal{O}_X)$ are Grothendieck abelian categories [@stacks-project [Tag 0781](http://stacks.math.columbia.edu/tag/0781)]. In particular, since the inclusion functor ${\ensuremath{\operatorname{Qcoh}}}(X_\tau, \mathcal{O}_X) \hookrightarrow {\ensuremath{\operatorname{Mod}}}(X_\tau, \mathcal{O}_X)$ is colimit preserving, it admits a right adjoint. This right adjoint is called the *quasi-coherator*.
:::

The construction $(-)_\tau$ functorially associates an adjoint pair $$\label{eq-functorial-topos}
f^*\colon Y_\tau \rightleftarrows X_\tau \colon f_*$$ of functors to any morphism $f\colon X \to Y$ of algebraic stacks. Moreover, the functor $f^*$ preserves finite products. In particular, the adjunction [\[eq-functorial-topos\]](#eq-functorial-topos){reference-type="eqref" reference="eq-functorial-topos"} induces an adjunction $$\label{eq-functorial-module}
f^*\colon {\ensuremath{\operatorname{Mod}}}(Y_\tau, \mathcal{O}_Y) \rightleftarrows {\ensuremath{\operatorname{Mod}}}(X_\tau, \mathcal{O}_X) \colon f_*.$$ Moreover, the pull-back functor $f^*$ preserves quasi-coherence. The functor $$\label{eq-qc-push-forward}
f_*\colon {\ensuremath{\operatorname{Qcoh}}}(X_\tau, \mathcal{O}_X) \to {\ensuremath{\operatorname{Qcoh}}}(Y_\tau, \mathcal{O}_Y)$$ is defined as the right adjoint of the restriction of $f^*$ to quasi-coherent sheaves. The existence of such a right adjoint is guaranteed by the quasi-coherator (see Remark [\[rem-coherator\]](#rem-coherator){reference-type="ref" reference="rem-coherator"}).

::: remark
[]{#rem-qc-pf label="rem-qc-pf"} If $\tau = {\operatorname{lis-\acute{e}t}}$, then the functor [\[eq-qc-push-forward\]](#eq-qc-push-forward){reference-type="eqref" reference="eq-qc-push-forward"} is the restriction of the push-forward for sheaves of modules provided that $f$ is quasi-compact and quasi-separated, but not in general. If $\tau = {\operatorname{fppf}}$, then [\[eq-qc-push-forward\]](#eq-qc-push-forward){reference-type="eqref" reference="eq-qc-push-forward"} seldom is the restriction of the push-forward for sheaves of modules.
:::

The category ${\ensuremath{\operatorname{Mod}}}(X_\tau, \mathcal{O}_X)$ has a closed symmetric monoidal structure with operations given by the usual tensor product and the sheaf hom functor. The tensor operation preserves quasi-coherence and is preserved by pull-backs. In particular, we get an induced symmetric monoidal structure on ${\ensuremath{\operatorname{Qcoh}}}(X_\tau, \mathcal{O}_X)$.

::: remark
[]{#rem-qc-hom label="rem-qc-hom"} The symmetric monoidal structure on ${\ensuremath{\operatorname{Qcoh}}}(X_\tau, \mathcal{O}_X)$ induced by the tensor product is also closed. This follows from the existence of the quasi-coherator (see Remark [\[rem-coherator\]](#rem-coherator){reference-type="ref" reference="rem-coherator"}). For $\tau = {\operatorname{lis-\acute{e}t}}$, the internal hom functor coincides with the sheaf hom functor provided that the first argument is of finite presentation, but not in general.
:::

There is an obvious restriction functor $X_{\operatorname{fppf}}\to X_{\operatorname{lis-\acute{e}t}}$, which is compatible with push-forward. This induces a monoidal equivalence $$\label{eq-change-site}
{\ensuremath{\operatorname{Qcoh}}}(X_{\operatorname{fppf}}, \mathcal{O}_X) \xrightarrow[{}]{\sim}{\ensuremath{\operatorname{Qcoh}}}(X_{\operatorname{lis-\acute{e}t}}, \mathcal{O}_X),$$ functorial in $X$ (see [@stacks-project [Tag 07B1](http://stacks.math.columbia.edu/tag/07B1)]).

We denote the derived category ${\operatorname{D}}({\ensuremath{\operatorname{Mod}}}(X_{\operatorname{lis-\acute{e}t}}, \mathcal{O}_X))$ simply by ${\operatorname{D}}(X)$. The category ${\operatorname{D}}_{\operatorname{qc}}(X)$ is defined as the full subcategory of ${\operatorname{D}}(X)$ consisting of complexes with quasi-coherent cohomology sheaves. The derived tensor product on ${\operatorname{D}}(X)$ preserves objects in ${\operatorname{D}}_{\operatorname{qc}}(X)$, giving the latter category a symmetric monoidal structure, which is closed.

::: remark
[]{#rem-dqc-hom label="rem-dqc-hom"} The internal hom functor on ${\operatorname{D}}_{\operatorname{qc}}(X)$ is the restriction of the derived sheaf hom functor provided that the first argument is perfect, but not in general (see [@hr2017 Section 1.2]).
:::

Given an arbitrary morphism $f\colon X \to Y$ of algebraic stacks, we have an adjoint pair of functors $$\label{eq-pb-pf}
f^*\colon {\operatorname{D}}_{\operatorname{qc}}(Y) \to {\operatorname{D}}_{\operatorname{qc}}(X), \qquad f_*\colon {\operatorname{D}}_{\operatorname{qc}}(Y) \to {\operatorname{D}}_{\operatorname{qc}}(X),$$ and the formation of such pairs is functorial.

::: remark
[]{#rem-derived-pb label="rem-derived-pb"} The functor $f^*$ in [\[eq-pb-pf\]](#eq-pb-pf){reference-type="eqref" reference="eq-pb-pf"} coincides with the derived pull-back between the ambient categories provided that $f$ is smooth. For general $f$, the construction of $f^*$ is somewhat technical owing to the fact that the adjunction [\[eq-functorial-topos\]](#eq-functorial-topos){reference-type="eqref" reference="eq-functorial-topos"}, for $\tau = {\operatorname{lis-\acute{e}t}}$, does not form a morphism of topoi, as was first noted by Behrend [@behrend-derived-l-adic-stacks Warning 5.3.12]. The construction is worked out by Olsson [@olsson2007] in the bounded case and by Laszlo--Olsson [@lo2008 Example 2.2.5] in the unbounded case. We refer to [@hr2017 Section 1] for a concise summary on this.
:::

::: remark
[]{#rem-derived-pf label="rem-derived-pf"} The push-forward $f_*$ in [\[eq-pb-pf\]](#eq-pb-pf){reference-type="eqref" reference="eq-pb-pf"} coincides with the derived push-forward provided that $f$ is *concentrated* [@hr2017 Definition 2.4, Theorem 2.6(2)], but not in general.
:::

::: remark
It is also possible to construct ${\operatorname{D}}_{\operatorname{qc}}(X)$ using the topos $X_{\operatorname{fppf}}$. This approach is taken in the stacks project [@stacks-project [Tag 07B6](http://stacks.math.columbia.edu/tag/07B6)]. For $\tau = {\operatorname{fppf}}$ the adjunction [\[eq-functorial-topos\]](#eq-functorial-topos){reference-type="eqref" reference="eq-functorial-topos"} does give a morphism of topoi, making the construction of the pull-back in [\[eq-pb-pf\]](#eq-pb-pf){reference-type="eqref" reference="eq-pb-pf"} easier. On the other hand the inclusion ${\ensuremath{\operatorname{Qcoh}}}(X_{\operatorname{fppf}}, \mathcal{O}_X) \subset {\ensuremath{\operatorname{Mod}}}(X_{\operatorname{fppf}}, \mathcal{O}_X)$ is not exact [@stacks-project [Tag 06WU](http://stacks.math.columbia.edu/tag/06WU)], making the actual construction of ${\operatorname{D}}_{\operatorname{qc}}(X)$ quite technical. We will not use this point of view in the present article.
:::

::: notation
[]{#not-sheaf-op label="not-sheaf-op"} We conclude this section by summarizing our notational conventions regarding sheaves on stacks. In the discussion below, we let $\tau \in \{{\operatorname{fppf}}, {\operatorname{lis-\acute{e}t}}\}$.

1.  We simply write ${\ensuremath{\operatorname{Qcoh}}}(X)$ for any of the categories ${\ensuremath{\operatorname{Qcoh}}}(X_\tau, \mathcal{O}_X)$ when no distinction is necessary. This is motivated by the functorial equivalence [\[eq-change-site\]](#eq-change-site){reference-type="eqref" reference="eq-change-site"}.

2.  The monoidal operations on the categories $${\ensuremath{\operatorname{Qcoh}}}(X_\tau, \mathcal{O}_X), \qquad
    {\ensuremath{\operatorname{Mod}}}(X_\tau, \mathcal{O}_X), \qquad
    {\operatorname{D}}(X), \qquad
    {\operatorname{D}}_{\operatorname{qc}}(X)$$ are always denoted $-\otimes-$ and ${\mathcal{H}{om}}(-,-)$, respectively. In particular, we omit any derived decorations. The precise category we are working on will always be inferable from context. Note that in the cases ${\ensuremath{\operatorname{Qcoh}}}(X_\tau, \mathcal{O}_X)$ and ${\operatorname{D}}_{\operatorname{qc}}(X)$ the functor ${\mathcal{H}{om}}$ does not always coincide with ${\mathcal{H}{om}}$ on the ambient category (cf. Remark [\[rem-qc-hom\]](#rem-qc-hom){reference-type="ref" reference="rem-qc-hom"} and Remark [\[rem-dqc-hom\]](#rem-dqc-hom){reference-type="ref" reference="rem-dqc-hom"}).

3.  The pull-backs and push-forwards along a morphism $f\colon X \to Y$ are always denoted by $f^*$ and $f_*$, respectively. Which of the categories $$(-)_\tau,\qquad
    {\ensuremath{\operatorname{Mod}}}((-)_\tau, \mathcal{O}_{(-)}), \qquad
    {\ensuremath{\operatorname{Qcoh}}}((-)_\tau, \mathcal{O}_{(-)}),$$ $${\operatorname{D}}(-), \qquad
    {\operatorname{D}}_{\operatorname{qc}}(-),$$ we are working with will always be inferable from context. In particular, we do not use any derived decorations or any particular decorations for push-forward of quasi-coherent sheaves (cf. Remark [\[rem-qc-pf\]](#rem-qc-pf){reference-type="ref" reference="rem-qc-pf"} and Remark [\[rem-derived-pf\]](#rem-derived-pf){reference-type="ref" reference="rem-derived-pf"}).
:::
